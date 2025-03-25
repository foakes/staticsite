from textnode import TextNode, TextType
from extractors import extract_markdown_links, extract_markdown_images


def split_nodes_image(old_nodes):
    new_nodes = []
    counter = 0
    for old_node in old_nodes:
        counter += 1
        print(f"{old_node} @@@@@")
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
        else:
            image_tuple_list = extract_markdown_images(old_node.text)
            raw_text = old_node.text
            split_text = raw_text.split("![")
            if len(split_text) % 2 == 0:
                new_nodes.append(TextNode(split_text[0], TextType.TEXT))
                new_nodes.append(TextNode(image_tuple_list[0][0], TextType.LINK, image_tuple_list[0][1]))
                final_split = split_text[1].split(")")
                new_nodes.append(TextNode(final_split[1], TextType.TEXT))
            else:
                raise Exception("add support for more than 1 image")





            
    print(image_tuple_list)
    print(counter)
    print(new_nodes)



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


linknode = TextNode(
    "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
      TextType.TEXT,
        )
imagenode = TextNode(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
        TextType.TEXT,
    )
oneimagenode = TextNode(
    "This is text with an ![image](https://i.imgur.com/dfkjsdd.png) of a bird",
    TextType.TEXT,
)

split_nodes_image([oneimagenode])
# split_nodes_delimiter(node, "**", TextType.BOLD)

# node1 = TextNode("This **is** a test", TextType.TEXT)
# node2 = TextNode("This is **a** test", TextType.TEXT)
# print(split_nodes_delimiter([node1, node2], "**", TextType.BOLD))


# def split_nodes_delimiter(old_nodes, delimiter, text_type):
#     converted = []
#     if old_nodes and isinstance(old_nodes, list):
#         for node in range(0, len(old_nodes)):
#             current_node = old_nodes[node].text.split(delimiter, maxsplit=1)
#             new_node = TextNode(current_node, text_type)
#             converted.append(split_nodes_delimiter(old_nodes[node+1:], delimiter, text_type))
#     return converted
        
            


