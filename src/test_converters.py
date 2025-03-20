from textnode import TextNode, TextType
from converters import split_nodes_delimiter
import unittest

class TestMDtoTextConverter(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        print(f"{new_nodes}")
        # self.assertEqual(new_nodes[0], TextNode("This is text with a ", TextType.TEXT))
        # self.assertEqual(new_nodes[1], TextNode("code block", TextType.CODE))
        # self.assertEqual(new_nodes[2], TextNode(" word", TextType.TEXT))
