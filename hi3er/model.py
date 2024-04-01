class Valk:
    def __init__(self,id, name, acronym,image,color_hex):
        self.id = id
        self.name = name
        self.acronym = acronym
        self.build = None
        self.image = image
        self.color_hex = color_hex
        
    def __repr__(self):
        return f"Valks(valk_name={self.name} acronym={self.acronym} image={self.image} color_hex={self.color_hex})"

class SignetCategory:
    def __init__(self, name):
        self.name = name

class Signet:
    def __init__(self, name, category):
        self.name = name
        self.category = category

class Build:
    def __init__(self, name, valk, signets):
        self.name = name
        self.valk = valk
        self.signets = signets
