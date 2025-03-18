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
        for child in self.children:
            if isinstance(child, LeafNode):
                results += f"<{child.tag}>{child.value}</{child.tag}>"
            elif isinstance(child, ParentNode):
                #results += f"<{child.tag}>{child.to_html()}</{child.tag}>"
                p_results = f"{child.to_html()}"
                results += p_results
        return f"<{self.tag}>{results}</{self.tag}>"

