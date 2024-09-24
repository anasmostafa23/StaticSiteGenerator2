from textnode import *
from htmlnode import *
from delimiter import *
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
    

    
    x = "This is `outer `inner` content` and another` sd ` `"
    

    z= find_matching_delimiters(x , '`')

    print (z)
    





    
    

if __name__ == "__main__":
    main()