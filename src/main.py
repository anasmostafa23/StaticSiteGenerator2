from copy_function import *
from extract_title import *
import os
from generate_page import *


def main():
    #generate_pages_recursive("source_directory", "html_template_directory","destination_directory")
    generate_pages_recursive("/home/user/StaticSiteGenerator2/content","/home/user/StaticSiteGenerator2/template.html","/home/mx/StaticSiteGenerator2/public/")
    

main()
