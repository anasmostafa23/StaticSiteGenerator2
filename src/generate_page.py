from markdown_blocks import *
from extract_title import *
import re , os


def read_file_contents(file_path):
    with open(file_path, 'r') as file:
        contents = file.read()
    return contents

# Then in your generate_page function:


def generate_page(from_path, template_path, dest_path) :
   
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    markdown_content = read_file_contents(from_path)
    template_content = read_file_contents(template_path)

    html_nodes = markdown_to_html_node (markdown_content)
    html_content = html_nodes.to_html()

    title = extract_title(markdown_content)

    filled_template = template_content.replace("{{ Title }}", title)
    filled_template = filled_template.replace("{{ Content }}", html_content)


    # Ensure the directory exists
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    # Write the content to the file
    with open(dest_path, 'w') as file:
        file.write(filled_template)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    entries = os.listdir(dir_path_content)
    
    for entry in entries:
        source_path = os.path.join(dir_path_content, entry)
        if os.path.isfile(source_path):
            # What should we do if it's a file?
            # Hint: Check if it's a markdown file, then generate the HTML
            if source_path.endswith(".md") or source_path.endswith(".markdown") : 
                # Assuming `source_path` is the full path of the markdown file
                relative_path = os.path.relpath(source_path, start=dir_path_content)
                destination_path = os.path.join(dest_dir_path, os.path.splitext(relative_path)[0] + '.html')
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                generate_page(source_path, template_path, destination_path)
                
        else :
            # What should we do if it's a directory?
            # Hint: We want to handle subdirectories too!   
            # Calculate the destination path for the current directory
            destination_dir = os.path.join(dest_dir_path, os.path.relpath(source_path, dir_path_content))
            os.makedirs(destination_dir, exist_ok=True)

            # Now call the recursion with this updated destination directory
            generate_pages_recursive(source_path, template_path, destination_dir)
            




