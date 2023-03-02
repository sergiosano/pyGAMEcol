from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from videogames.models import Format, Platform, Videogame


def fill_initial_data():
    
    if len(Format.objects.all()) == 0:
        Format.objects.create(name='3DS Game Card')
        Format.objects.create(name='Blue-ray Disc')
        Format.objects.create(name='Cartucho ROM')
        Format.objects.create(name='Casete')
        Format.objects.create(name='CD-ROM')
        Format.objects.create(name='Digital')
        Format.objects.create(name='Disquete de 5¼"')
        Format.objects.create(name='Disquete de 3½"')
        Format.objects.create(name='DS Game Card')
        Format.objects.create(name='DVD')
        Format.objects.create(name='GameCube Game Disc')
        Format.objects.create(name='GD-ROM')
        Format.objects.create(name='PS Vita Card')
        Format.objects.create(name='Switch Game Card')
        Format.objects.create(name='Wii Optical Disc')
        Format.objects.create(name='Wii U Optical Disc')
    
    if len(Platform.objects.all()) == 0:
        Platform.objects.create(name='NES', icon='platforms/icons/Nintendo.svg')
        Platform.objects.create(name='Game Boy', icon='platforms/icons/Nintendo.svg')
        Platform.objects.create(name='Super Nintendo', icon='platforms/icons/Nintendo.svg')
        Platform.objects.create(name='Virtual Boy', icon='platforms/icons/Nintendo.svg')
        Platform.objects.create(name='Nintendo 64', icon='platforms/icons/Nintendo.svg')
        Platform.objects.create(name='GameBoy Color', icon='platforms/icons/Nintendo.svg')
        Platform.objects.create(name='Nintendo GameCube', icon='platforms/icons/NintendoGameCube.svg')
        Platform.objects.create(name='GameBoy Advance', icon='platforms/icons/Nintendo.svg')
        Platform.objects.create(name='Nintendo DS', icon='platforms/icons/Nintendo.svg')
        Platform.objects.create(name='Wii', icon='platforms/icons/Nintendo.svg')
        Platform.objects.create(name='Nintendo 3DS', icon='platforms/icons/Nintendo3DS.svg')
        Platform.objects.create(name='Wii U', icon='platforms/icons/Nintendo.svg')
        Platform.objects.create(name='Nintendo Switch', icon='platforms/icons/NintendoSwitch.svg')
        Platform.objects.create(name='Master System', icon='platforms/icons/Sega.svg')
        Platform.objects.create(name='Mega Drive', icon='platforms/icons/Sega.svg')
        Platform.objects.create(name='Game Gear', icon='platforms/icons/Sega.svg')
        Platform.objects.create(name='Saturn', icon='platforms/icons/Sega.svg')
        Platform.objects.create(name='Dreamcast', icon='platforms/icons/Sega.svg')
        Platform.objects.create(name='PC', icon='platforms/icons/PC.svg')
        Platform.objects.create(name='PlayStation', icon='platforms/icons/PlayStation.svg')
        Platform.objects.create(name='PlayStation 2', icon='platforms/icons/PlayStation2.svg')
        Platform.objects.create(name='PlayStation 3', icon='platforms/icons/PlayStation3.svg')
        Platform.objects.create(name='PlayStation 4', icon='platforms/icons/PlayStation4.svg')
        Platform.objects.create(name='PlayStation 5', icon='platforms/icons/PlayStation5.svg')
        Platform.objects.create(name='PSP', icon='platforms/icons/Sony.svg')
        Platform.objects.create(name='PS Vita', icon='platforms/icons/PSVita.svg')
        Platform.objects.create(name='XBOX', icon='platforms/icons/XBOX.svg')
        Platform.objects.create(name='XBOX 360', icon='platforms/icons/XBOX.svg')
        Platform.objects.create(name='XBOX One', icon='platforms/icons/XBOX.svg')
        Platform.objects.create(name='XBOX One X', icon='platforms/icons/XBOX.svg')
        Platform.objects.create(name='XBOX Series S', icon='platforms/icons/XBOX.svg')
        Platform.objects.create(name='XBOX Series X', icon='platforms/icons/XBOX.svg')

    if not User.objects.filter(username='democol'):
        user = User.objects.create_user(username='democol', email='democol@democol.com', password='democol23')
        Videogame.objects.create(owner=user, title="Baldur's Gate", platform=Platform.objects.get(name='PC'), formato=Format.objects.get(name='CD-ROM'), release_date='1998-12-21', front_cover='videogames/front_covers/BG1.png',
                                             description="Baldur's Gate es un videojuego de rol de fantasía desarrollado por BioWare y publicado en 1998 por Interplay Entertainment.")
        
        Videogame.objects.create(owner=user, title="Baldur's Gate II: Shadows Of Amn", platform=Platform.objects.get(name='PC'), formato=Format.objects.get(name='CD-ROM'), release_date='2000-09-24', front_cover='videogames/front_covers/BG2SOA.jpg',
                                             description="Baldur's Gate II: Shadows of Amn es un videojuego de rol desarrollado por Bioware en el año 2000 para PC.")
        
        Videogame.objects.create(owner=user, title="Fallout", platform=Platform.objects.get(name='PC'), formato=Format.objects.get(name='CD-ROM'), release_date='1997-10-10', front_cover='videogames/front_covers/Fallout.jpg',
                                             description="Fallout es un videojuego de rol de 1997 desarrollado y publicado por Interplay Productions.")
        
        Videogame.objects.create(owner=user, title="Half-Life 2", platform=Platform.objects.get(name='PC'), formato=Format.objects.get(name='CD-ROM'), release_date='2004-11-16', front_cover='videogames/front_covers/HL2.jpg',
                                             description="Half-Life 2 (HL2) es la continuación del videojuego Half-Life, una videoaventura de disparos en primera persona.")
        
        Videogame.objects.create(owner=user, title="Sonic The Hedgehog", platform=Platform.objects.get(name='Mega Drive'), formato=Format.objects.get(name='Cartucho ROM'), release_date='1991-06-23', front_cover='videogames/front_covers/SonicTH.jpg',
                                             description="Sonic the Hedgehog es un videojuego de plataforma desarrollado por Sonic Team y publicado por Sega para la consola de videojuegos doméstica Sega Mega Drive.")
        
        Videogame.objects.create(owner=user, title="Resident Evil 4", platform=Platform.objects.get(name='Nintendo GameCube'), formato=Format.objects.get(name='GameCube Game Disc'), release_date='2005-01-11', front_cover='videogames/front_covers/RE4.jpg',
                                             description="Resident Evil 4, es un videojuego de acción-aventura y disparos en tercera persona de estilo terror y supervivencia desarrollado por Capcom Production Studio 4.")
        
        Videogame.objects.create(owner=user, title="Mario Kart 8 Deluxe", platform=Platform.objects.get(name='Nintendo Switch'), formato=Format.objects.get(name='Switch Game Card'), release_date='2017-04-28', front_cover='videogames/front_covers/MK8D.jpg',
                                             description="Mario Kart 8 Deluxe (マリオカート8 デラックス. Mario Kāto Eito Derakkusu) es un videojuego de carreras desarrollado y publicado por Nintendo para la consola Nintendo Switch.")
        
        Videogame.objects.create(owner=user, title="Metal Gear Solid 3: Snake Eater", platform=Platform.objects.get(name='PlayStation 2'), formato=Format.objects.get(name='DVD'), release_date='2004-11-17', front_cover='videogames/front_covers/MGS3SE.jpg',
                                             description="Metal Gear Solid 3: Snake Eater es un videojuego de acción, aventura e infiltración dirigido por Hideo Kojima y producido por la subsidiaria Konami Computer Entertainment Japan.")


def index(request):
    fill_initial_data()

    if request.user.is_authenticated:
        return redirect('collection')
    
    return render(request, 'index/index.html')