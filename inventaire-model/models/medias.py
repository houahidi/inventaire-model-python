
class Media:
    def __init__(self, ident, libelle, auteur=None):
        self.ident = ident
        self.libelle = libelle
        self.auteur = auteur
        self.categories = []
    def __str__(self):
        return "Media : id={0}, libelle={1}".format(self.ident, self.libelle)
