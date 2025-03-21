from textnode import TextNode, TextType


# def split_nodes_delimiter(old_nodes, delimiter, text_type):
#     new_nodes = []
#     for old_node in old_nodes:
#         if old_node.text_type != TextType.TEXT:
#             new_nodes.append(old_node)
#             continue
#         split_nodes = []
#         sections = old_node.text.split(delimiter)
#         if len(sections) % 2 == 0:
#             raise ValueError("invalid markdown, formatted section not closed")
#         for i in range(len(sections)):
#             if sections[i] == "":
#                 continue
#             if i % 2 == 0:
#                 split_nodes.append(TextNode(sections[i], TextType.TEXT))
#             else:
#                 split_nodes.append(TextNode(sections[i], text_type))
#         new_nodes.extend(split_nodes)
#     return new_nodes


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
        else:
            if delimiter not in old_node.text:
                raise ValueError(f"Delimiter '{delimiter}' not found in node: {old_node.text}")
            if old_node.text.count(delimiter) % 2 != 0:
                raise ValueError(f"Delimiter {delimiter} not closed")
            split_nodes = []
            split_text = old_node.text.split(delimiter)
            if len(split_text) % 2 == 0:
                raise ValueError("Incorrect Markdown syntax")
            for i in range(len(split_text)):
                if split_text[i] == "":
                    continue
                if i % 2 == 0:
                    split_nodes.append(TextNode(split_text[i], TextType.TEXT))
                else:
                    split_nodes.append(TextNode(split_text[i], text_type))
            new_nodes.extend(split_nodes)
            
            # ***Unnecessary, the expected TextType is already defined in the input function

            # if delimiter == "**":
            #     new_nodes.append(TextNode(split_node[1], TextType.BOLD))
            # elif delimiter == "_":
            #     new_nodes.append(TextNode(split_node[1], TextType.ITALIC))
            # elif delimiter == "`":
            #     new_nodes.append(TextNode(split_node[1], TextType.CODE))
            
            
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
        
            


