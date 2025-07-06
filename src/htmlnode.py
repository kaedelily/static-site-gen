class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag if tag is not None else ""
        self.value = value if value is not None else ""
        self.children = children if children is not None else []
        self.props = props if props is not None else {}
    
    def to_html(self):
        """
        Converts the HTMLNode to an HTML string representation.
        
        Returns:
            str: The HTML string representation of the node.
        """
        raise NotImplementedError("This method should be implemented by subclasses.")
    
    def props_to_html(self):
        """
        Converts the properties of the HTMLNode to an HTML attribute string.
        
        Returns:
            str: The HTML attribute string.
        """
        return " ".join(f'{key}="{value} "' for key, value in self.props.items())

    def __repr__(self):
        """
        Returns a string representation of the HTMLNode object.
        
        Returns:
            str: A string in the format "HTMLNode(TAG, VALUE, PROPS, CHILDREN)".
        """
        return f"HTMLNode({self.tag}, {self.value}, {self.props}, {self.children})"