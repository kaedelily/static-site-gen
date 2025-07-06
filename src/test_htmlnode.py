import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(props={"cats": "beautiful", "dogs": "ok"})
        expected = ' cats="beautiful" dogs="ok"'
        self.assertEqual(node.props_to_html(), expected)

    def test_repr(self):
        tag = "p"
        value = "Nolly is a cat"
        props = {"cats": "beautiful", "dogs": "ok"}

        node = HTMLNode(tag, value, props=props)
        expected = f"HTMLNode({tag}, {value}, {None}, {props})"
        self.assertEqual(node.__repr__(), expected)

    def test_props_to_html_none(self):
        node = HTMLNode()
        expected = ""
        self.assertEqual(node.props_to_html(), expected)


if __name__ == "__main__":
    unittest.main()