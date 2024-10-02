def extract_title(markdown) : 
    
    if not markdown.startswith("# ") :
        raise Exception ("markdown has no header")
    else : 
        lines = markdown.split("\n") 
        x= lines[0].strip().lstrip("# ")
       

    return(x)