import livereload

"""
this module is still under development and at this time just use livereload package
"""
class HotReload:
    def __init__(self, text=None, path='.', delay=None, recurse=True,
                 include='', exclude='', pattern='*', port=1904, ip='127.0.0.1', debug=False,name='index.html') -> None:
        self.text = text
        self.path = path
        self.delay = delay
        self.recursive = recurse
        self.include = include
        self.exclude = exclude
        self.pattern = pattern
        self.ip = ip
        self.port = port
        self.name = name
        self.textFilePath = '.'
        self.debug = debug
        self.laststate = None

    def start_server(self, webbrowseropen=True):
        import webbrowser
        try:
            print("Starting livereload server at port", self.port)
            self.server = livereload.Server()
            self.server.watch(self.path)
            if webbrowseropen:
                webbrowser.open('http://'+self.ip.strip()+':' +
                                str(self.port))
            self.server.serve(port=self.port, host=self.ip,
                              debug=self.debug, default_filename=self.name)
        except KeyboardInterrupt:
            print("Livereload server stopped.")
        except Exception as e:
            print(e)
