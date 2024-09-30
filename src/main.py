from textnode import *
from htmlnode import *
from delimiter import *
from link_extractor import *
from text_to_textnodes import *
import re
def main () :
    leaf1 = LeafNode("p", "This is a paragraph of text.")
    leaf2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})

    leaf1.to_html()
    leaf2.to_html()
    node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
    
    
text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)" 



    
        
    

   






    
    

if __name__ == "__main__":
    main()