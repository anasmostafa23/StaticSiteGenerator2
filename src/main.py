from copy_function import *
from extract_title import *
import os


def main():
    #copy_directory("/home/mx/StaticSiteGenerator2/Static", "/home/mx/StaticSiteGenerator2/public")
    markdown = """# Tolkien Fan Club

**I like Tolkien**. Read my [first post here](/majesty) (sorry the link doesn't work yet)

> All that is gold does not glitter

## Reasons I like Tolkien

    
    """

    extract_title(markdown)


main()
