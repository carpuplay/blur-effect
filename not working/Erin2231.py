from PIL import Image

def blurear(fichier_origine,fichier_destination,n, o, p, x0=0, y0=0): #n est le niveau de blur que l'on veut (se sera le normbre de pixels avec lequel on fera la moyenne pour le blur). On devra changer des para mètre pour pouvoir plasser le rectangñle ou l'on voudra. 
    image_origine = Image.open(fichier_origine)         #o largeur du rectangle de blur. p hauteur de rectangle de blur. (x0,y0) point à gauche du rectangle. 
    largeur , hauteur = image_origine.size
    image_dest=Image.new("RGB",(largeur,hauteur))
    for y in range(hauteur):
        for x in range(largeur):
            r,g,b = image_origine.getpixel((x,y))
            if x>=x0 and x<=x0+o and y>=y0 and y<=y0+p:
                r,g,b = image_origine.getpixel((x,y))
                for k in range (n):
                    for z in range (n):
                        Tr=0
                        Tg=0
                        Tb=0
                        for i in range ((o//n)*k):
                            for j in range ((p//n)*z):
                                r, g, b = image_origine.getpixel((((k*o) //n)+i),(((z*p)//n)+j))
                                Tr = Tr + r
                                Tg = Tg + g
                                Tb = Tb + b
                        r = (Tr//(o//n)*(p//n))
                        g = (Tg//(o//n)*(p//n))
                        b = (Tb//(o//n)*(p//n))           
            image_dest.putpixel((x,y),(r,g,b))
    image_dest.save(fichier_destination)
