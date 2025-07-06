import unittest
from extractmarkdown import extract_markdown_images


class TestExtractMarkdownImages(unittest.TestCase):
    def test_extract_markdown_images(self):
        res = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        expt = [("image", "https://i.imgur.com/zjjcJKZ.png")]
        self.assertListEqual(res, expt)

    def test_extract_markdown_images_no_alt(self):
        res = extract_markdown_images(
            "Blah blah words ![](https://internet.com/image.piss)"
        )
        expt = [("", "https://internet.com/image.piss")]
        self.assertListEqual(res, expt)

    def test_extract_markdown_images_no_url(self):
        res = extract_markdown_images("Blah blah words ![image alt text]()")
        expt = [("image alt text", "")]
        self.assertListEqual(res, expt)

    def test_extract_markdown_images_no_url_no_alt(self):
        res = extract_markdown_images("Blah blah words ![]()")
        expt = [("", "")]
        self.assertListEqual(res, expt)

    def test_multiple_images_in_text(self):
        res = extract_markdown_images(
            "Blah blah words ![alt text 1](https://internet.com/image.piss) and more stuff with ![some other image](https://dogs.cats.cool) here"
        )
        expt = [
            ("alt text 1", "https://internet.com/image.piss"),
            ("some other image", "https://dogs.cats.cool"),
        ]
        self.assertListEqual(res, expt)