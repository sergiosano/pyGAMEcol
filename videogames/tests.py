from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Videogame, Platform, Format


class VideogameTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        User = get_user_model()
        cls.user = User.objects.create_user(username='testusertest', email='testusertest@domain.com', password='testpass123')
        cls.platform = Platform.objects.create(name='PC', icon='platforms/icons/PC.png')
        cls.format = Format.objects.create(name='CD-ROM')

    def test_create_videogame(self):
        videogame = Videogame.objects.create(owner=self.user, title="Baldur's Gate", platform=self.platform, formato=self.format, release_date='1998-12-21', front_cover='videogames/front_covers/BG.png',
                                             description="Baldur's Gate es un videojuego de rol de fantasía desarrollado por BioWare y publicado en 1998 por Interplay Entertainment.")
        self.assertEqual(videogame.owner, self.user)
        self.assertEqual(videogame.title, "Baldur's Gate")
        self.assertEqual(videogame.platform, self.platform)
        self.assertEqual(videogame.formato, self.format)
        self.assertEqual(videogame.release_date, '1998-12-21')
        self.assertEqual(videogame.front_cover, 'videogames/front_covers/BG.png')
        self.assertEqual(videogame.description, "Baldur's Gate es un videojuego de rol de fantasía desarrollado por BioWare y publicado en 1998 por Interplay Entertainment.")