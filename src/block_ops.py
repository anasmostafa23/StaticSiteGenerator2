block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_olist = "ordered_list"
block_type_ulist = "unordered_list"



def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks

def block_to_block_type(block) : 

    lines = block.split("\n")
    block_type = "paragraph"
    if lines[0][0] == "#" :
        block_type = "heading"

    

    if lines[0][0:3] == lines[-1][-3:] == "```" :
        block_type = "code"

    for line in lines : 
        if line[0] == '>' :
            q = True
            continue 
        else :
            q = False
            break 

    if q == True :
        
     block_type = "quote"
     return block_type

    for line in lines : 
        if line[0] == '* ' or line[0] == '- ':
            u = True
            continue 
        else :
            u= False
            break 

    if u == True :
        
     block_type = "unordered_list"
     return block_type

    for i in range(len(lines)) :
        if lines[i][0:2] == f"{i+1}." :
            o = True
        else :
            o = False

    if o : 
        block_type = "ordered_list"
        return block_type
    
    return block_type

        

        
            
        

       
