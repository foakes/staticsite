import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        test1 = HTMLNode("p", "first", None, {"p":"first dict value"})
        print(test1.__repr__())

    def test_prop(self):
        test1 = HTMLNode("a", "https://www.google.com", None, {"href": "https://www.google.com"})
        print(test1.props_to_html())

    def test_props(self):
        test1 = HTMLNode("a", "https://www.google.com", None, {"href": "https://www.doogle.com", "target": "_blank"})
        print(test1.props_to_html())

    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )

    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    def test_repr(self):
        node = HTMLNode(
            "p",
            "What a strange world",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, What a strange world, None, {'class': 'primary'})",
        )

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_no_tag(self):
        node = LeafNode(None, "Hello world!")
        self.assertEqual(node.to_html(), "Hello world!")
    
    def test_no_value(self):
        node = LeafNode(None, None)
        self.assertRaises(ValueError)
    
    def test_leaf_with_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://example.com", "class": "button"})
        self.assertEqual(node.to_html(), '<a href="https://example.com" class="button">Click me!</a>')


if __name__ == "__main__":
    unittest.main()