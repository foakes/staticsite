import unittest

from textnode import TextNode, TextType



class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_ineq_type(self):
        node = TextNode("Not Equal", TextType.TEXT)
        node2 = TextNode("Not Equal", TextType.BOLD)
        self.assertNotEqual(node, node2)
    
    def test_ineq_text(self):
        node = TextNode("Equal", TextType.TEXT)
        node2 = TextNode("Not Equal", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_eq_link(self):
        node = TextNode("Link", TextType.LINK, "https://www.google.com")
        node2 = TextNode("Link", TextType.LINK, "https://www.google.com")
        self.assertEqual(node, node2)

    def test_eq_no_link(self):
        node = TextNode("Link", TextType.LINK)
        node2 = TextNode("Link", TextType.LINK)
        self.assertEqual(node, node2)


# class TestTextNodeToHTML(unittest.TestCase):
#     def test_text(self):
#         node = TextNode("This is a text node", TextType.TEXT)
#         html_node = text_node_to_html_node(node)
#         self.assertEqual(html_node.tag, None)
#         self.assertEqual(html_node.value, "This is a text node")

if __name__ == "__main__":
    unittest.main()