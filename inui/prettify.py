from bs4 import BeautifulSoup as bs


class Pretiffy:
    def __init__(self, text="", filePath=""):
        self.filePath = filePath
        self.text = text
        if self.filePath != "":
            self.fromFile()

    def save(self, out="out.html"):
        with open(out, "w", encoding="utf-8") as fi:
            fi.write(self.pretiffy_string())

    def fromFile(self):
        if self.filePath != "":
            with open(self.filePath, "r", encoding="utf-8") as f:
                self.text = f.read()

    def pretiffy_string(self):
        soup = bs(self.text, "html.parser")
        return soup.prettify()

    def __str__(self) -> str:
        return self.pretiffy_string()

    def __repr__(self) -> str:
        return self.pretiffy_string()
