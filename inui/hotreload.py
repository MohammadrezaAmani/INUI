import asyncio
import http.server
import importlib.util
import logging
import os
import socketserver
import threading

try:
    import websockets
except ImportError:
    raise "you must install websockets, run `python3 -m pip install websockets"
try:
    from watchdog.events import FileSystemEventHandler
    from watchdog.observers import Observer
except ImportError:
    raise "you must install watchdog, run `python3 -m pip install watchdog"


global _host, _port, _file_to_watch, _variable_name, _sleep_time, _static_dir

_host = "localhost"
_port = 8000
_file_to_watch = ""
_variable_name = ""
clients = set()
_sleep_time = 1
_static_dir = "."
# module_name, variable_name = module.split(":")
# file_to_watch = f"{module_name.replace('.', '/')}.py"


def get_file_contents(file_name, variable_name):
    try:
        module_name = os.path.splitext(os.path.basename(file_name))[0]
        spec = importlib.util.spec_from_file_location(module_name, file_name)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return str(getattr(module, variable_name))
    except Exception as err:
        logging.error(f"Error getting file contents: {err}")
        return f"<h1>{err}</h1>"


def hot_reload_script(host, port):
    return f"""
        <script>
            var ws = new WebSocket("ws://{host}:{port}/ws");
            ws.onopen = function() {{
                console.log("Connected to WebSocket");
            }};
            ws.onmessage = function(event) {{
                console.log("Message received:", event.data);
                document.body.innerHTML = event.data;
            }};
            ws.onclose = function() {{
                console.log("Disconnected from WebSocket");
            }};
        </script>
    """


class HTMLFileHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith(".py"):
            logging.info(
                f"Detected changes in {event.src_path}, updating HTML content."
            )
            asyncio.run(update_html_content(event.src_path))


async def send_update(html_content):
    if clients:
        await asyncio.gather(*(client.send(html_content) for client in clients))
        logging.info("Sent updated HTML content to clients.")


async def websocket_handler(websocket, path):
    clients.add(websocket)
    logging.info("New client connected.")
    try:
        async for _ in websocket:
            pass
    finally:
        clients.remove(websocket)
        logging.info("Client disconnected.")


async def update_html_content(*args):
    html_content = get_file_contents(_file_to_watch, _variable_name)
    if not isinstance(html_content, str):
        html_content = str(html_content)
    await send_update(html_content)


def monitor_file(_file_to_watch: str, sleep_time: float):
    event_handler = HTMLFileHandler()
    observer = Observer()
    observer.schedule(event_handler, path=os.getcwd(), recursive=False)
    observer.start()
    logging.info("Started monitoring file changes.")
    try:
        while True:
            asyncio.run(asyncio.sleep(sleep_time))
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


class RequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            content = get_file_contents(
                _file_to_watch, _variable_name
            ) + hot_reload_script(host=_host, port=_port + 1)
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.send_header(
                "Cache-Control", "no-store, no-cache, must-revalidate, proxy-revalidate"
            )
            self.end_headers()
            self.wfile.write(str(content).encode())
            logging.info("Served HTML content.")
        else:
            self.path = f"/{_static_dir}{self.path}"
            super().do_GET()


def run_server(host, port):
    with socketserver.TCPServer((host, port), RequestHandler) as httpd:
        logging.info(f"Server started on: http://{host}:{port}")
        httpd.serve_forever()


def hot_reload(
    host: str,
    port: int,
    module: str,
    variable_name: str,
    sleep_time: float,
    static_dir: str,
):
    global _host, _port, _file_to_watch, _variable_name, _sleep_time, _static_dir
    file_to_watch = f"{module.replace('.', '/')}.py"

    _host, _port, _file_to_watch, _variable_name, _sleep_time, _static_dir = (
        host,
        port,
        file_to_watch,
        variable_name,
        sleep_time,
        static_dir,
    )

    def run_async():
        new_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(new_loop)

        async def start_websocket_server():
            start_server = await websockets.serve(
                lambda x: websocket_handler(x, _file_to_watch), host, port + 1
            )
            await start_server.wait_closed()

        new_loop.run_until_complete(start_websocket_server())

    threading.Thread(
        target=monitor_file, args=(_file_to_watch, _sleep_time), daemon=True
    ).start()

    threading.Thread(target=run_server, args=(host, port), daemon=True).start()

    websocket_thread = threading.Thread(target=run_async, daemon=True)
    websocket_thread.start()

    websocket_thread.join()
