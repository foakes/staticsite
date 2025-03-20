from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in range(0, len(old_nodes)):
        if old_nodes[node].text_type != TextType.TEXT:
            new_nodes.append(old_nodes)
        else:
            split_node = old_nodes[node].text.split(delimiter, maxsplit=2)
            if len(split_node) < 3:
                raise TypeError("Incorrect Markdown syntax")
            new_nodes.append(TextNode(split_node[0], TextType.TEXT))
            if delimiter == "**":
                new_nodes.append(TextNode(split_node[1], TextType.BOLD))
            elif delimiter == "_":
                new_nodes.append(TextNode(split_node[1], TextType.ITALIC))
            elif delimiter == "`":
                new_nodes.append(TextNode(split_node[1], TextType.CODE))
            new_nodes.append(TextNode(split_node[2], TextType.TEXT))
    return new_nodes


                             

    
    #print(new_nodes)

# node = TextNode("Bold Test", TextType.BOLD)
# split_nodes_delimiter(node, "**", TextType.BOLD)

node1 = TextNode("This **is** a test", TextType.TEXT)
node2 = TextNode("This is **a** test", TextType.TEXT)
print(split_nodes_delimiter([node1, node2], "**", TextType.BOLD))


# def split_nodes_delimiter(old_nodes, delimiter, text_type):
#     converted = []
#     if old_nodes and isinstance(old_nodes, list):
#         for node in range(0, len(old_nodes)):
#             current_node = old_nodes[node].text.split(delimiter, maxsplit=1)
#             new_node = TextNode(current_node, text_type)
#             converted.append(split_nodes_delimiter(old_nodes[node+1:], delimiter, text_type))
#     return converted
        
            


