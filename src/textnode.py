class TextNode:
    def __init__(self, text, font_text_type, url = None):
        self.text = text
        self.font_text_type = font_text_type
        self.url = url

    def __eq__(self, other):
        if not isinstance(other, TextNode):
            return NotImplemented
        return (self.text == other.text and
                self.font_text_type == other.font_text_type and
                self.url == other.url)

    # Optionally, override __repr__ for improved debugging output
    def __repr__(self):
        return f"TextNode(text={self.text}, font_text_type={self.font_text_type}, url={self.url})"