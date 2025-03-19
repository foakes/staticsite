from enum import Enum
# solution files had this import for the function below
#from htmlnode import LeafNode

class TextType(Enum):
	TEXT = "text"
	BOLD = "bold"
	ITALIC = "italic"
	CODE = "code"
	LINK = "link"
	IMAGE = "image"


class TextNode():
	def __init__(self, text, text_type, url=None):
		self.text = text
		self.text_type = text_type
		self.url = url

	def __eq__(obj1, obj2):
		return obj1.text == obj2.text and obj1.text_type == obj2.text_type and obj1.url == obj2.url

	def __repr__(self):
		return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
	
# Solution files have this function in this file, but I ran into circular import errors. Moved it to htmlnode.py

# def text_node_to_html_node(text_node):
# 	if not isinstance(text_node, TextNode):
# 		raise ValueError("input must be TextNode object")
# 	if text_node.text_type.value not in TextType:
# 		raise ValueError("please use a supported text type")
# 	node = None
# 	if text_node.text_type.value == "text":
# 		node = LeafNode(None, text_node.text, None)
# 	elif text_node.text_type.value == "bold":
# 		node = LeafNode("b", text_node.text, None)
# 	elif text_node.text_type.value == "italic":
# 		node = LeafNode("i", text_node.text, None)
# 	elif text_node.text_type.value == "code":
# 		node = LeafNode("code", text_node.text, None)
# 	elif text_node.text_type.value == "link":
# 		node = LeafNode("a", text_node.text, {"href": f"{text_node.url}"})
# 	elif text_node.text_type.value == "image":
# 		node = LeafNode("img", None, {"src": f"{text_node.url}", "alt": f"{text_node.text}"})
# 	return node
	