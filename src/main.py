from copy_function import *
from extract_title import *
import os
from generate_page import *


def main():
    #copy_directory("/home/mx/StaticSiteGenerator2/Static", "/home/mx/StaticSiteGenerator2/public")
    generate_page("/home/mx/StaticSiteGenerator2/content/index.md","/home/mx/StaticSiteGenerator2/template.html","/home/mx/StaticSiteGenerator2/public/index.html")
    

main()
