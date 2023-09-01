from inui.elements import *


class React:
    def __init__(
        self,
        path: str = "./",
        title="inui",
        lang="en",
        description="INUI project",
        favicon="%PUBLIC_URL%/favicon.ico",
        theme_color="#000000",
        apple_touch_icon="%PUBLIC_URL%/logo192.png",
        manifest="%PUBLIC_URL%/manifest.json",
        viewport="width=device-width, initial-scale=1",
        charset="utf-8",
    ) -> None:
        pass
        self.__is_initialed = False
        self.path = path
        self.title = title
        self.lang = lang
        self.description = description
        self.favicon = favicon
        self.theme_color = theme_color
        self.apple_touch_icon = apple_touch_icon
        self.manifest = manifest
        self.viewport = viewport
        self.charset = charset

    @property
    def path(self):
        return self._path

    def root(
        self,
        head_childs=[],
        header_body_childs=[],
        footer_body_childs=[],
    ):
        return str(
            Html(
                lang=self.lang,
                data=(
                    Head(
                        data=(
                            Meta(
                                charset=self.charset,
                            ),
                            Link(
                                rel="icon",
                                href=self.favicon,
                            ),
                            Meta(
                                name="viewport",
                                content=self.viewport,
                            ),
                            Meta(
                                name="theme-color",
                                content=self.theme_color,
                            ),
                            Meta(
                                name="description",
                                content=self.description,
                            ),
                            Link(
                                rel="apple-touch-icon",
                                href=self.apple_touch_icon,
                            ),
                            Link(
                                rel="manifest",
                                href=self.manifest,
                            ),
                            Title(self.title),
                            *head_childs,
                        )
                    ),
                    Body(
                        data=(
                            Noscript(
                                data=("You need to enable JavaScript to run this app.",)
                            ),
                            *header_body_childs,
                            Div(
                                id="root",
                            ),
                            *footer_body_childs,
                        )
                    ),
                ),
            )
        )

    @path.setter
    def path(self, path: str = "./"):
        path = str(path)
        if not path.endswith("/"):
            path = path + "/"
        self.__path = path
        self.__public_path = "public/"
        self.__src_path = "src/"

    def initial(
        self,
        head_childs=[],
        header_body_childs=[],
        footer_body_childs=[],
    ):
        import os

        os.chdir(path=self.__path)
        try:
            os.mkdir(self.__public_path)
            os.mkdir(self.__src_path)
        except FileExistsError:
            pass
        with open(self.__public_path + "index.html", "w", encoding="utf-8") as f:
            f.write(self.root(head_childs, header_body_childs, footer_body_childs))


p = React("test")
p.initial()
