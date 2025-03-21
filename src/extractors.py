import re


def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)


def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

match = extract_markdown_images("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)")
print(match)