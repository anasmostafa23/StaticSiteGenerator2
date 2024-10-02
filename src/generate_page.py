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





