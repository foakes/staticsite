import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

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


class TestLeafNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_grandchildren_and_cousins(self):
        grandchild_nephew = LeafNode("b", "nephew")
        grandchild_neice = LeafNode("b", "neice")
        mother_of_both = ParentNode("span", [grandchild_neice, grandchild_nephew])
        parent_of_mother = ParentNode("div", [mother_of_both])
        self.assertEqual(
            parent_of_mother.to_html(),
            "<div><span><b>neice</b><b>nephew</b></span></div>",
        )

    def test_to_html_w_props(self):
        child_node = LeafNode("a", "Click here", {"href": "www.boot.dev", "target": "_blank"})
        parent_node = ParentNode("section", [child_node], {"class": "link-container"})
        self.assertEqual(
            parent_node.to_html(), 
            '<section class="link-container"><a href="www.boot.dev" target="_blank">Click here</a></section>'
        )

if __name__ == "__main__":
    unittest.main()