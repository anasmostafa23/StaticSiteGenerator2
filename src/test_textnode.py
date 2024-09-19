import unittest

from textnode import *



class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)
    def test_eq_false(self):
        node = TextNode("This is a text node", "italic")
        node2 = TextNode("This is a text node", "bold")
        self.assertNotEqual(node, node2)

    def test_eq_false2(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node2", "bold")
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node", "text", "https://www.boot.dev")
        node2 = TextNode("This is a text node", "text", "https://www.boot.dev")

    class TestTextNodeToHTMLNode(unittest.TestCase):
        def test_text(self):
            node = TextNode("This is a text node", "text")
            html_node = text_node_to_html_node(node)
            self.assertEqual(html_node.tag, None)
            self.assertEqual(html_node.value, "This is a text node")

        def test_image(self):
            node = TextNode("This is an image", "image", "https://www.boot.dev")
            html_node = text_node_to_html_node(node)
            self.assertEqual(html_node.tag, "img")
            self.assertEqual(html_node.value, "")
            self.assertEqual(
                html_node.props,
                {"src": "https://www.boot.dev", "alt": "This is an image"},
            )

        def test_bold(self):
            node = TextNode("This is bold", "bold")
            html_node = text_node_to_html_node(node)
            self.assertEqual(html_node.tag, "b")
            self.assertEqual(html_node.value, "This is bold")
    


if __name__ == "__main__":
    unittest.main()