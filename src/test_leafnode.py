import unittest

from htmlnode import *

class TestLeafNode(unittest.TestCase):

    def test_leaf_node_creation_no_children(self):
        with self.assertRaises(ValueError):
            LeafNode(tag='p', value='Hello', children=[HTMLNode(tag='span', value='Inner')])

    def test_leaf_node_to_html(self):
        leaf = LeafNode(tag='p', value='Hello, World!', props={'class': 'text'})
        expected_html = '<p class="text">Hello, World!</p>'
        self.assertEqual(leaf.to_html(), expected_html)

    def test_leaf_node_to_html_no_value_error(self):
        leaf = LeafNode(tag='p', value=None)
        with self.assertRaises(ValueError):
            leaf.to_html()

    def test_leaf_node_no_props(self):
        leaf = LeafNode(tag='p', value='No props')
        expected_html = '<p>No props</p>'
        self.assertEqual(leaf.to_html(), expected_html)

if __name__ == "__main__":
    unittest.main()