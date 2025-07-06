from enum import Enum

from htmlnode import LeafNode

class TextType(Enum):
    """
    Enum representing different types of text nodes for a Markdown parser.
    """
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    """
    Represents a text node for parsing Markdown.

    Attributes:
        text (str): The text content of the node.
        text_type (TextType): The type of text this node contains.
        url (str, optional): The URL of the link or image if the text_type is LINK or IMAGE.
                             Defaults to None.
    """

    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        """
        Compares two TextNode objects for equality based on their properties.

        Args:
            other: The other TextNode object to compare.

        Returns:
            True if all properties of the two objects are equal, False otherwise.
        """
        if not isinstance(other, TextNode): # Checks if the other object is an instance of TextNode
            return False
        return (
            self.text == other.text and
            self.text_type == other.text_type and
            self.url == other.url
        )

    def __repr__(self):
        """
        Returns a string representation of the TextNode object.

        Returns:
            A string in the format "TextNode(TEXT, TEXT_TYPE, URL)".
        """
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            return LeafNode("a", text_node.text, {"href": text_node.url})
        case TextType.IMAGE:
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
        case _:
            raise ValueError(
                f"O SHIT, `{text_node.text_type}` is not a valid text type"
            )