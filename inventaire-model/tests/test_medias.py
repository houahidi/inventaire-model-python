

from unittest import TestCase

from models import medias

class TestMedia(TestCase):
    def test_is_media(self):
        m = medias.Media(1, "Python", "SG")
        self.assertTrue(isinstance(m, medias.Media))
        self.assertEqual("Python", m.libelle)