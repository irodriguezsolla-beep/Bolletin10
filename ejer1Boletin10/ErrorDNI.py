class DniError(Exception):
    def __init__(self, mensaxe):
        super().__init__()
        self.mensaxe = mensaxe
    def __str__(self):
        return "Error "+ str(self.mensaxe)