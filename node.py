class Node:
    def __init__(self, name, neighborhood, art_style, type, alias=None):  # exhibition_date removed for now
        self.name = name
        self.neighborhood = neighborhood
        self.art_style = art_style
        self.type = type #Gallery or Museums
        self.alias = alias #optinal alternative names
        self.left = None
        self.right = None