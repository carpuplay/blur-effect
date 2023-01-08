from PIL import Image

def blur(fichier_origine,fichier_destination,p1=(1,1),p2=(1918,1078)):
    image_origine = Image.open(fichier_origine)
    largeur , hauteur = image_origine.size
    image_dest=Image.new("RGB",(largeur,hauteur))


    for x in range (largeur):
        for y in range (hauteur):
            if (x>p1[0]) and (x<p2[0]) and (y>p1[1]) and (y<p2[1]):
                n=[-1,0,1]
                temp_r=[]
                temp_g=[]
                temp_b=[]

                for i in range(len(n)):
                    for j in range(len(n)):
                        r,g,b=image_origine.getpixel((x+n[i],y+n[j]))
                        temp_r.append(r)
                        temp_g.append(g)
                        temp_b.append(b)

                #print(len(temp_r))

                r=int(sum(temp_r)/len(temp_r))
                g=int(sum(temp_g)/len(temp_g))
                b=int(sum(temp_b)/len(temp_b))

                image_dest.putpixel((x+1,y),(r,g,b))
                image_dest.putpixel((x-1,y),(r,g,b))
                image_dest.putpixel((x,y+1),(r,g,b))
                image_dest.putpixel((x,y-1),(r,g,b))
                image_dest.putpixel((x+1,y+1),(r,g,b))
                image_dest.putpixel((x+1,y-1),(r,g,b))
                image_dest.putpixel((x-1,y+1),(r,g,b))
                image_dest.putpixel((x-1,y-1),(r,g,b))
                image_dest.putpixel((x,y),(r,g,b))

            else:
                r,g,b=image_origine.getpixel((x,y))
                image_dest.putpixel((x,y),(r,g,b))

    image_dest.save(fichier_destination)
    #image_dest.show()

def blur2(fichier_origine,fichier_destination,n=3,p1=(1,1),p2=(1918,1078)):
    image_origine = Image.open(fichier_origine)
    largeur , hauteur = image_origine.size
    image_dest=Image.new("RGB",(largeur,hauteur))
    val=[]
    for l in range(n):
        a=0-l
        val.append(a)
        b=0+l
        val.append(b)

    for x in range (largeur):
        for y in range (hauteur):
            if (x>p1[0]) and (x<p2[0]) and (y>p1[1]) and (y<p2[1]):

                temp_r=[]
                temp_g=[]
                temp_b=[]

                for i in range(len(val)):
                    for j in range(len(val)):
                        r,g,b=image_origine.getpixel((x+val[i],y+val[j]))
                        temp_r.append(r)
                        temp_g.append(g)
                        temp_b.append(b)

                #print(len(temp_r))

                r=int((sum(temp_r)/len(temp_r))*1.2)
                g=int((sum(temp_g)/len(temp_g))*1.2)
                b=int((sum(temp_b)/len(temp_b))*1.2)

                image_dest.putpixel((x+1,y),(r,g,b))
                image_dest.putpixel((x-1,y),(r,g,b))
                image_dest.putpixel((x,y+1),(r,g,b))
                image_dest.putpixel((x,y-1),(r,g,b))
                image_dest.putpixel((x+1,y+1),(r,g,b))
                image_dest.putpixel((x+1,y-1),(r,g,b))
                image_dest.putpixel((x-1,y+1),(r,g,b))
                image_dest.putpixel((x-1,y-1),(r,g,b))
                image_dest.putpixel((x,y),(r,g,b))

            else:
                r,g,b=image_origine.getpixel((x,y))
                image_dest.putpixel((x,y),(r,g,b))

    image_dest.save(fichier_destination)
    #image_dest.show()
