import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase): 
    def test_eq(self):
        node = HTMLNode("h1", "header",None, {
    "href": "https://www.google.com", 
    "target": "_blank", })
        node2 =  HTMLNode("h1", "header",None, {
    "href": "https://www.google.com", 
    "target": "_blank",})
        self.assertEqual(node, node2)
    def test_eq_false(self):
        node = HTMLNode("p", "paragraph")
        node2 = HTMLNode("h1", "header")
        self.assertNotEqual(node, node2)

    def test_eq_false2(self):
       node = HTMLNode("h1", "header",None, {
                         "href": "https://www.google.com", 
                         "target": "_blank", })
                                            
       node2 =  HTMLNode("h1", "header",None, {
                   "href": "https://www.google.com", 
                    "target": "_",})
       
       self.assertNotEqual(node, node2)
                                            
        
    




if __name__ == "__main__":
    unittest.main()
