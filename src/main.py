from textnode import *
from htmlnode import *
def main () :
    leaf1 = LeafNode("p", "This is a paragraph of text.")
    leaf2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})

    leaf1.to_html()
    leaf2.to_html()


    
    

if __name__ == "__main__":
    main()