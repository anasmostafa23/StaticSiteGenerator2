from textnode import *
from htmlnode import *
from delimiter import *
from link_extractor import *
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
    

    
    text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
    
    print(extract_markdown_links(text))






    
    

if __name__ == "__main__":
    main()