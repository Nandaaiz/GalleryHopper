class Node:
    def __init__(self, name, neighborhood, art_style):  # exhibition_date removed for now
        self.name = name
        self.neighborhood = neighborhood
        self.art_style = art_style
        self.left = None
        self.right = None