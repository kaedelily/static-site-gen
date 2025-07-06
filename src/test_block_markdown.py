import unittest
from block_markdown import (
    BlockType,
    markdown_to_blocks,
    block_to_block_type
)

class TestBlockMarkdown(unittest.TestCase):

    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

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

# == Here are tests for checking block type ==

    def test_block_type_text(self):
        md_text = """
Just a raw text here
"""
        blocks = markdown_to_blocks(md_text)
        for block in blocks:
            block_type = block_to_block_type(block)
            self.assertEqual(
                block_type,
                BlockType.PARAGRAPH
            )

    def test_block_type_text_multiple(self):
        md_text = """
Just a raw text here

Another paragraph text

And another
"""
        blocks = markdown_to_blocks(md_text)
        for block in blocks:
            block_type = block_to_block_type(block)
            self.assertEqual(
                block_type,
                BlockType.PARAGRAPH
            )

    def test_block_type_heading_simple(self):
        # two bugs spotted here:
        # 1. some error with ####### heading 7
        # investiage
        # 2. Even when between # and text no space, program sees it as
        # heading, but it must be paragraph
        md_text = """
# Heading 1

## Heading 2

### Heading 3

#### Heading 4

##### Heading 5

###### Heading 6

"""
        blocks = markdown_to_blocks(md_text)
        for block in blocks:
            block_type = block_to_block_type(block)
            self.assertEqual(
                block_type,
                BlockType.HEADING
            )


    def test_block_type_code(self):
        md_text = """
```
Block in code quotes
```

```and another code text```
"""
        blocks = markdown_to_blocks(md_text)
        for block in blocks:
            block_type = block_to_block_type(block)
            self.assertEqual(
                block_type,
                BlockType.CODE
            )


    def test_block_type_quote(self):
        md_text = """
>quote may be without space
> or with space
> > or even two quotes
> but quote must be the first symbol
"""
        blocks = markdown_to_blocks(md_text)
        for block in blocks:
            block_type = block_to_block_type(block)
            self.assertEqual(
                block_type,
                BlockType.QUOTE
            )



    def test_block_type_unordered_list(self):
        md_text = """
- just
* unordered
- list
"""
        blocks = markdown_to_blocks(md_text)
        for block in blocks:
            block_type = block_to_block_type(block)
            self.assertEqual(
                block_type,
                BlockType.UNORDERED_LIST
            )



    def test_block_type_ordered_list(self):
        md_text = """
1. just
2. ordered
3. list
"""
        blocks = markdown_to_blocks(md_text)
        for block in blocks:
            block_type = block_to_block_type(block)
            self.assertEqual(
                block_type,
                BlockType.ORDERED_LIST
            )