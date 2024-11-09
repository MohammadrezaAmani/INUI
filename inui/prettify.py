from typing import List

try:
    from bs4 import BeautifulSoup, Tag
except ImportError:
    raise "you must install bs4, run `python3 -m pip install bs4"


class Pretiffy:
    def __init__(
        self, text: str = "", file_path: str = "", parser: str = "html.parser"
    ):
        """
        Initialize the Pretiffy object.

        Args:
            text (str): The HTML content as a string.
            file_path (str): The path to the HTML file.
            parser (str): The parser to use with BeautifulSoup (default is 'html.parser').
        """
        self.file_path = file_path
        self.text = text
        self.parser = parser
        if self.file_path:
            self.from_file()

    def save(self, out: str = "out.html") -> None:
        """
        Save the prettified HTML content to a file.

        Args:
            out (str): The output file path (default is 'out.html').
        """
        with open(out, "w", encoding="utf-8") as f:
            f.write(self.prettify_string())

    def from_file(self) -> None:
        """
        Read HTML content from a file and set it as the current text.
        """
        if self.file_path:
            with open(self.file_path, "r", encoding="utf-8") as f:
                self.text = f.read()

    def prettify_string(self) -> str:
        """
        Prettify the HTML content using BeautifulSoup.

        Returns:
            str: The prettified HTML content.
        """
        soup = BeautifulSoup(self.text, self.parser)
        return soup.prettify()

    def find_tags(self, tag_name: str) -> List[Tag]:
        """
        Find all occurrences of a specific HTML tag.

        Args:
            tag_name (str): The name of the HTML tag to find.

        Returns:
            List[Tag]: A list containing all occurrences of the specified tag.
        """
        soup = BeautifulSoup(self.text, self.parser)
        return soup.find_all(tag_name)

    def remove_tags(self, tags_to_remove: List[str]) -> str:
        """
        Remove specified HTML tags from the content.

        Args:
            tags_to_remove (List[str]): A list of tag names to remove.

        Returns:
            str: The HTML content after removing the specified tags.
        """
        soup = BeautifulSoup(self.text, self.parser)
        for tag in tags_to_remove:
            for elem in soup.find_all(tag):
                elem.decompose()
        return str(soup)

    def replace_tags(self, old_tag: str, new_tag: str) -> str:
        """
        Replace occurrences of a specific HTML tag with another tag.

        Args:
            old_tag (str): The name of the HTML tag to replace.
            new_tag (str): The name of the HTML tag to replace with.

        Returns:
            str: The HTML content after replacing the specified tags.
        """
        soup = BeautifulSoup(self.text, self.parser)
        for elem in soup.find_all(old_tag):
            elem.name = new_tag
        return str(soup)

    def __str__(self) -> str:
        """
        Return the prettified HTML content as a string.

        Returns:
            str: The prettified HTML content.
        """
        return self.prettify_string()

    def __repr__(self) -> str:
        """
        Return the prettified HTML content as a string.

        Returns:
            str: The prettified HTML content.
        """
        return self.prettify_string()
