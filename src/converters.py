from textnode import TextNode, TextType
from extractors import extract_markdown_links, extract_markdown_images


def text_to_textnodes(text):
    delimiters_dict = {"**": TextType.BOLD, "_": TextType.ITALIC, "`": TextType.CODE}
    if text == "":
        return []
    raw_textnode = [TextNode(text, TextType.TEXT)]
    raw_textnode = split_nodes_image(raw_textnode)
    raw_textnode = split_nodes_link(raw_textnode)
    for delimiter in delimiters_dict:
        raw_textnode = split_nodes_delimiter(raw_textnode, delimiter, delimiters_dict[delimiter])
    return raw_textnode



def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
        else:
            image_tuple_list = extract_markdown_images(old_node.text)
            original_text = old_node.text
            if len(image_tuple_list) == 0:
                new_nodes.append(old_node)
                continue
            for tup in image_tuple_list:
                image_alt = tup[0]
                image_link = tup[1]
                sections = original_text.split(f"![{image_alt}]({image_link})", 1)
                if len(sections) != 2:
                    raise ValueError("invalid markdown input for image")
                if sections[0] != "":
                    new_nodes.append(TextNode(sections[0], TextType.TEXT))
                new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_link))
                original_text = sections[1]
            if original_text != "":
                new_nodes.append(TextNode(original_text, TextType.TEXT))
            else:
                continue
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
        else:
            link_tuple_list = extract_markdown_links(old_node.text)
            original_text = old_node.text
            if len(link_tuple_list) == 0:
                new_nodes.append(old_node)
                continue
            for tup in link_tuple_list:
                link_text = tup[0]
                link_url = tup[1]
                sections = original_text.split(f"[{link_text}]({link_url})", 1)
                if len(sections) != 2:
                    raise ValueError("invalid markdown input for link")
                if sections[0] != "":
                    new_nodes.append(TextNode(sections[0], TextType.TEXT))
                new_nodes.append(TextNode(link_text, TextType.LINK, link_url))
                original_text = sections[1]
            if original_text != "":
                new_nodes.append(TextNode(original_text, TextType.TEXT))
            else:
                continue
    return new_nodes


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
        else:
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
    return new_nodes
    
