import unittest
from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        node3 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)
        self.assertNotEqual(node3, node2)
        self.assertEqual(node, node3)


if __name__ == "__main__":
    unittest.main()