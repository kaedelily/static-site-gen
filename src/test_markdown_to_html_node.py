import unittest

from markdown_to_html_node import (
    markdown_to_html_node,
)


class TestMarkdownToHtmlNode(unittest.TestCase):

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_headings(self):
        md = """
# This is correct heading
## Also correct heading
### Also correct heading
#### Also correct heading
##### Also correct heading
###### Also correct heading

####### And there's no h7 heading to this is paragraph
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div>"
            +"<h1>This is correct heading</h1>"
            +"<h2>Also correct heading</h2>"
            +"<h3>Also correct heading</h3>"
            +"<h4>Also correct heading</h4>"
            +"<h5>Also correct heading</h5>"
            +"<h6>Also correct heading</h6>"
            +"<p>####### And there's no h7 heading to this is paragraph</p>"
            +"</div>"
        )


    def test_unordered_lists(self):
        md = """
- This
- is 
- unordered
- list
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        print(f"unordered lists in html:\n{html}")
        self.assertEqual(
            html,
            "<div><ul><li>This</li><li>is</li><li>unordered</li><li>list</li></ul></div>"       
            )


    def test_ordered_lists(self):
        # doesn't support situation when every line starts with one number
        # in other words - they are calculated so every other elem should be n+1
        md = """
1. This
2. is 
3. unordered
4. list
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        print(f"unordered lists in html:\n{html}")
        self.assertEqual(
            html,
            "<div><ol><li>This</li><li>is</li><li>unordered</li><li>list</li></ol></div>"       
            )

    def test_block_quotes(self):
        # doesn't support situation when every line starts with one number
        # in other words - they are calculated so every other elem should be n+1
        md = """
> This
> is 
> block
>of
>quote
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        print(f"unordered lists in html:\n{html}")
        self.assertEqual(
            html,
            "<div><blockquote>This is block of quote</blockquote></div>"
            )