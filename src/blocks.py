from enum import Enum


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered list"
    ORDERED_LIST = "ordered list"

def block_to_block_type(markdown_block):
    headings = ["#", "##", "###", "####", "#####", "######"]
    for heading in headings:
        if markdown_block.startswith(heading):
            return BlockType.HEADING
    if markdown_block.startswith("```") and markdown_block.endswith("```"):
        return BlockType.CODE
    line_checker = markdown_block.split("\n")
    prediction = BlockType.PARAGRAPH
    line_counter = 1
    for line in line_checker:
        if line.startswith(">"):
            prediction = BlockType.QUOTE
        elif line.startswith(str(line_counter)+"."):
            prediction = BlockType.ORDERED_LIST
            line_counter += 1
        elif line.startswith("- "):
            prediction = BlockType.UNORDERED_LIST
    return prediction

def markdown_to_blocks(markdown):
    if not markdown:
        raise ValueError("no input")
    raw_blocks = markdown.split('\n\n')
    # for i in range(0, len(blocks)):
    #     if blocks[i] == "":
    #         blocks.pop(blocks[i])
    #     blocks[i] = blocks[i].strip()
    new_blocks = []
    for block in raw_blocks:
        if block.strip():
           new_blocks.append(block.strip())
    return new_blocks

md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""

print(markdown_to_blocks(md))