from PIL import Image

def fluter(fichier_origine,fichier_fin,fichier_destination,n=24):
    image_origine = Image.open(fichier_origine)
    image_fin = Image.open(fichier_fin)
    largeur , hauteur = image_origine.size
    image_dest=[]
    for i in range(n):
        image_dest.append(Image.new("RGB",(largeur,hauteur)))
    for y in range(hauteur):
        for x in range(largeur):
            r0,g0,b0=image_origine.getpixel((x,y))
            r1,g1,b1=image_fin.getpixel((x,y))
    for i in range
    