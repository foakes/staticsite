import unittest
import textwrap
from blocks import markdown_to_blocks, block_to_block_type, BlockType

class MDToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
        blocks,
            [
            "This is **bolded** paragraph",
            "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
            "- This is a list\n- with items",
            ],
            )
    
    import textwrap

    def test_markdown_to_blocks(self):
        md = textwrap.dedent(
            """\
            This is **bolded** paragraph

            This is another paragraph with _italic_ text and `code` here
            This is the same paragraph on a new line

            - This is a list
            - with items
            """
        )
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
    
    def test_paragraph_blocktype(self):
        md = "This is a paragraph"
        blocktype = block_to_block_type(md)
        self.assertEqual(blocktype, BlockType.PARAGRAPH)

    def test_heading1_blocktype(self):
        md = "# Biggest Heading"
        blocktype = block_to_block_type(md)
        self.assertEqual(blocktype, BlockType.HEADING)

    def test_heading2_blocktype(self):
        md = "## Next Biggest Heading"
        blocktype = block_to_block_type(md)
        self.assertEqual(blocktype, BlockType.HEADING)
    
    def test_heading3_blocktype(self):
        md = "### Slightly Over Half Of All Headings"
        blocktype = block_to_block_type(md)
        self.assertEqual(blocktype, BlockType.HEADING)

    def test_heading4_blocktype(self):
        md = "#### Slightly Under Half Of All Headings"
        blocktype = block_to_block_type(md)
        self.assertEqual(blocktype, BlockType.HEADING)

    def test_heading5_blocktype(self):
        md = "##### The Second Smallest Heading"
        blocktype = block_to_block_type(md)
        self.assertEqual(blocktype, BlockType.HEADING)
    
    def test_heading6_blocktype(self):
        md = "###### The Smallest Heading"
        blocktype = block_to_block_type(md)
        self.assertEqual(blocktype, BlockType.HEADING)
    
    def test_code_blocktype(self):
        md = "```Hello World```"
        blocktype = block_to_block_type(md)
        self.assertEqual(blocktype, BlockType.CODE)
    
    def test_single_line_quote_blocktype(self):
        md = ">Veni, Vedi, Vici"
        blocktype = block_to_block_type(md)
        self.assertEqual(blocktype, BlockType.QUOTE)
    
    def test_multi_line_quote_blocktype(self):
        md = textwrap.dedent(
            """\
            >Never gonna give you up
            >Never gonna let you down
            >Never gonna run around and
            >Desert you
            """
            )
        blocktype = block_to_block_type(md)
        self.assertEqual(blocktype, BlockType.QUOTE)
    
    def test_ordered_list_blocktype(self):
        md = textwrap.dedent(
            """\
            1. Never gonna give you up
            2. Never gonna let you down
            3. Never gonna run around and
            4. Desert you
            """
            )
        blocktype = block_to_block_type(md)
        self.assertEqual(blocktype, BlockType.ORDERED_LIST)
    
    def test_unordered_list_blocktype(self):
        md = textwrap.dedent(
            """\
            - Never gonna give you up
            - Never gonna let you down
            - Never gonna run around and
            - Desert you
            """
            )
        blocktype = block_to_block_type(md)
        self.assertEqual(blocktype, BlockType.UNORDERED_LIST)

