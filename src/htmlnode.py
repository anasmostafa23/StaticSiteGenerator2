class HTMLNode():
    def __init__(self,tag = None, value = None , children = None , props = None) :
        self.tag = tag 
        self.value = value
        self.children = children if children is not None else []
        self.props = props if props is not None else {}

    def to_html(self) :
        raise NotImplementedError 
    
    def props_to_html(self):
        # Returns a string of HTML properties
        return ' '.join(f'{key}="{value}"' for key, value in self.props.items())

    def __repr__(self): 
        return f"tag = {self.tag} , value = {self.value} , children = {self.children} , props = {self.props.items()}"
        
    def __eq__(self, other):
        if not isinstance(other, HTMLNode):
            return NotImplemented
        return (self.tag == other.tag  and
                self.value == other.value and
                self.children == other.children and
                self.props == other.props)
    

class LeafNode(HTMLNode):
    def __init__ (self,tag = None, value = None, props = None , children = None) :
        if children:
            raise ValueError("LeafNode cannot have children")
        super().__init__(tag = tag, value = value, children=  children , props = props)
       
    def to_html(self):
       
        if self.value is None :
            raise ValueError
        if self.value == "" :
            raise ValueError

        
        if self.tag != None and self.tag != "":
            
            html_opening_tag = f"<{self.tag}"
            if self.props:
                html_opening_tag += f" {self.props_to_html()}"
            html_opening_tag += ">"

            html_closing_tag = f"</{self.tag}>"
        elif self.tag == None :
            html_closing_tag = html_opening_tag = ""
        # Construct and return the full HTML string
        return( f"{html_opening_tag}{self.value}{html_closing_tag}")

class ParentNode(HTMLNode) :
    def __init__ (self,tag = None, children = None, props = None , value = None) :
        if value:
            raise ValueError("ParentNode cannot have value")
        super().__init__(tag = tag, value = value, children=  children , props = props)
       

    def to_html(self):
         if self.tag is None : 
            raise ValueError("tag is required")
         if self.children is None :
            raise ValueError("child is rquired for ParentNode")
         children_html = ""
         for child in self.children:
            children_html += child.to_html()
         return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"

    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"