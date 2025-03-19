from textnode import TextNode, TextType


class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        if not self.props:
            return ""
        if not isinstance(self.props, dict):
            raise TypeError("Props must be a dictionary")
        props_str = ""
        props_dict = self.props.copy()
        for k in props_dict:
            props_str = props_str + f" {k}=\"{props_dict[k]}\""
        return props_str

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props) # super() doesn't require self
        # None is passed to the parent class __init__ for children

    def to_html(self):
        if not self.value: # raises exception if no value
            raise ValueError("Leaf Nodes cannot be empty")
        if not self.tag: # handles no tag
            return f"{self.value}"
        if not self.props: # handles leaf nodes with no props
            return f"<{self.tag}>{self.value}</{self.tag}>"
        else: # handles leaf nodes w/ props
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("Parent Node must contain tag")
        if not self.children:
            raise ValueError("Parent Node must contain children")
        results = ""
        # ***Forgot about polymorphism - I checked isinstance for the Nodes rather than relying on
        #     each classes own personalized to_html function***
        # for child in self.children:
        #     if isinstance(child, LeafNode):
        #         results += f"<{child.tag}>{child.value}</{child.tag}>"
        #     elif isinstance(child, ParentNode):
        #         #results += f"<{child.tag}>{child.to_html()}</{child.tag}>"
        #         p_results = f"{child.to_html()}"
        #         results += p_results
        for child in self.children:
            results += child.to_html()
        #return f"<{self.tag}>{results}</{self.tag}>"
        return f"<{self.tag}{self.props_to_html()}>{results}</{self.tag}>"


def text_node_to_html_node(text_node):
    if not isinstance(text_node, TextNode):
        raise ValueError("input must be TextNode object")
    if text_node.text_type not in TextType:
        raise ValueError("please use a supported text type")
    if text_node.text_type == TextType.TEXT: # evaluating enums based on Enum rather than the Enum value
        node = LeafNode(None, text_node.text, None)
    elif text_node.text_type == TextType.BOLD:
        node = LeafNode("b", text_node.text, None)
    elif text_node.text_type == TextType.ITALIC:
        node = LeafNode("i", text_node.text, None)
    elif text_node.text_type == TextType.CODE:
        node = LeafNode("code", text_node.text, None)
    elif text_node.text_type == TextType.LINK:
        if not text_node.url:
            raise ValueError("URL missing from link TextNode object")
        node = LeafNode("a", text_node.text, {"href": text_node.url})
    elif text_node.text_type == TextType.IMAGE:
        if not text_node.url:
            raise ValueError("Source image URL missing from image TextNode object")
        node = LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    return node