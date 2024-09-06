class HTMLNode():
    def __init__(self,tag = None, value = None , children = None , props = None) :
        self.tag = tag 
        self.value = value
        self.children = children
        self.props = props 

    def to_html(self) :
        raise NotImplementedError 
    
    def props_to_html(self) :
       for key, value in self.props.items():
           print (f'{key}="{value}" ')

    def __repr__(self): 
        return f"tag = {self.tag} , value = {self.value} , children = {self.children} , props = {self.props.items()}"
        
    def __eq__(self, other):
        if not isinstance(other, HTMLNode):
            return NotImplemented
        return (self.tag == other.tag  and
                self.value == other.value and
                self.children == other.children and
                self.props == other.props)