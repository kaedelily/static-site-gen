import re
from text_node_to_html_node import text_node_to_html_node
from textnode import (
    TextType,
    TextNode,
)
from htmlnode import (
    LeafNode,
    ParentNode
)
from inline_markdown import (
    text_to_textnodes,
)
from block_markdown import (
    BlockType,
    markdown_to_blocks, 
    block_to_block_type
)

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    nodes = []
    for block in blocks:
        if block_to_block_type(block) == BlockType.PARAGRAPH:
            nodes.append(markdown_paragraph_to_html_node(block))
        if block_to_block_type(block) == BlockType.HEADING:
            nodes.append(markdown_heading_to_html_node(block))
        if block_to_block_type(block) == BlockType.CODE:
            nodes.append(markdown_code_block_to_html_node(block))
        if block_to_block_type(block) == BlockType.QUOTE:
            nodes.append(markdown_quote_block_to_html_node(block))
        if block_to_block_type(block) == BlockType.UNORDERED_LIST:
            nodes.append(markdown_unordered_list_to_html_node(block))
        if block_to_block_type(block) == BlockType.ORDERED_LIST:
            nodes.append(markdown_ordered_list_to_html_node(block))

    div_node = ParentNode(tag="div", children=nodes)
    return div_node
    
def markdown_paragraph_to_html_node(block):
    children = block_to_children(block)
    parent = ParentNode(tag="p", children=children)
    return parent

def markdown_heading_to_html_node(block):
    node = block_to_children(block)
    return node

def markdown_code_block_to_html_node(block):
    text_value = ""
    for value in block.split("```"):
        if value != "":
            text_value += value.lstrip("\n")
    text_node = TextNode(text=text_value, text_type=TextType.CODE)
    internal_html = text_node_to_html_node(text_node)
    parent_node = ParentNode(tag="pre", children=[internal_html])
    return parent_node

def markdown_quote_block_to_html_node(block):
    children = block_to_children(block)
    quote_block_parent = ParentNode(tag="blockquote", children=children)
    return quote_block_parent

def markdown_unordered_list_to_html_node(block):
    children = block_to_children(block)
    unordered_list_parent = ParentNode(tag="ul", children=children)
    return unordered_list_parent

def markdown_ordered_list_to_html_node(block):
    children = block_to_children(block)
    unordered_list_parent = ParentNode(tag="ol", children=children)
    return unordered_list_parent

def block_to_children(block):
    if block_to_block_type(block) == BlockType.PARAGRAPH:
        joined_block = " ".join(block.split("\n"))
        text_nodes = text_to_textnodes(joined_block)
        html_nodes = []
        for node in text_nodes:
            html_nodes.append(text_node_to_html_node(node))
        return html_nodes

    elif block_to_block_type(block) == BlockType.HEADING:
        match = re.match(r"^(#{1,6}) (.*)", block)
        html_nodes = []
        if match:
            heading_level = len(match.group(1))
            heading_text = match.group(2)
            heading_node = LeafNode(tag=f'h{heading_level}', value=heading_text, props=None)
            return heading_node


    elif block_to_block_type(block) == BlockType.QUOTE:
        block_values = []
        for inline in block.split("\n"):
            if inline != "":
                if inline.startswith("> "):
                    block_values.append(inline[2:].strip("\n"))
                elif inline.startswith(">"):
                    block_values.append(inline[1:].strip("\n"))
        final_string = " ".join(block_values)
        text_nodes = text_to_textnodes(final_string)
        html_nodes = []
        for node in text_nodes:
            html_nodes.append(text_node_to_html_node(node))
        return html_nodes
    elif block_to_block_type(block) == BlockType.UNORDERED_LIST:
        # so currently code doesn't handle elems in unorderes lists which
        # start with '* '
        block_values = []
        list_elem_nodes = []
        for inline in block.split("- "):
            if inline != "":
                block_values.append(inline.strip("\n"))
        for value in block_values:
            text_nodes = text_to_textnodes(value)
            html_nodes = []
            for node in text_nodes:
                html_nodes.append(text_node_to_html_node(node))
            parent = ParentNode(tag="li", children=html_nodes)
            list_elem_nodes.append(parent)
        return list_elem_nodes
    elif block_to_block_type(block) == BlockType.ORDERED_LIST:
        block_values = []
        list_elem_nodes = []
        for inline in block.split("\n"):
            if inline != "":
                block_values.append(inline[3:].strip("\n"))
        for value in block_values:
            text_nodes = text_to_textnodes(value)
            html_nodes = []
            for node in text_nodes:
                html_nodes.append(text_node_to_html_node(node))
            parent = ParentNode(tag="li", children=html_nodes)
            list_elem_nodes.append(parent)
        return list_elem_nodes