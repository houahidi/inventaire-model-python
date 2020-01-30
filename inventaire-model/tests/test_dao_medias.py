

from unittest import TestCase

from models.medias import Media
from  dao.dao_medias import MediaDao

class TestMediaDao(TestCase):

    @classmethod
    def tearDownClass(cls):
        cls.dao = None

    @classmethod
    def setUpClass(cls):
        cls.dao = MediaDao("test.db")
        cls.dao.initialiser_base()

    def test_1_ajouter(self):
        m = Media(1, "Python", "SG")
        self.dao.ajouter(m)
        medias = self.dao.listerMedias()
        self.assertEqual(1, len(medias))
    def test_1_supprimer(self):
        self.dao.supprimer(1)
        medias = self.dao.listerMedias()
        self.assertEqual(0, len(medias))