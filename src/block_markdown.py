import re
from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def markdown_to_blocks(markdown):
    lines = [line.rstrip() for line in markdown.splitlines()]
    blocks = []
    block = []
    for line in lines:
        if line.strip() == "":
            if block:
                blocks.append("\n".join(block).strip())
                block = []
            continue
        if re.match(r"^#{1,6} ", line) and block:
            blocks.append("\n".join(block).strip())
            block = []
        block.append(line)
    if block:
        blocks.append("\n".join(block).strip())
    return [b for b in blocks if b]
def block_to_block_type(block):

    if block[0] == "#":
        head_count = 1
        for n in range(1, 8):
            if block[n] == "#":
                head_count += 1
            elif block[n] == " ":
                return BlockType.HEADING
            elif block[n] != " " and block[n] != "#":
                return BlockType.PARAGRAPH
            if head_count > 6:
                return BlockType.PARAGRAPH
            else:
                continue
    elif block.strip().split("```")[0] == "" and block.strip().split("```")[-1] == "":
        return BlockType.CODE
    elif block.strip().split("\n")[0][0] == ">":
        line_num = len(block.strip().split("\n"))
        quote_line_num = 0
        for n in block.strip().split("\n"):
            if n[0] == ">":
                quote_line_num += 1
        if quote_line_num == line_num:
            return BlockType.QUOTE
        raise Exception("Markdown Quote Block is not properly formatted")
    elif (
          block.strip().split("\n")[0][:2] == "- "
          or block.strip().split("\n")[0][:2] == "* "
          ):
        line_num = 0
        list_line_num = 0
        for n in block.strip().split("\n"):
            line_num += 1
            if (
                n[:2] == "- "
                or n[:2] == "* "
            ):
                list_line_num += 1
        if line_num == list_line_num:
            return BlockType.UNORDERED_LIST
        raise Exception("Unordered Markdown List is not properly formatted")

    elif block.strip().split("\n")[0][:2] == "1.":
        line_num = 0
        list_line_num = 0

        for n in block.strip().split("\n"):
            line_num += 1
            if (
                n[:2] == f"{line_num}."
                and n[2] == " "
            ):
                list_line_num += 1

        if line_num == list_line_num:
            return BlockType.ORDERED_LIST
        elif line_num != list_line_num:
            raise Exception("Ordered Markdown List is not properly formatted")

    else:
        return BlockType.PARAGRAPH