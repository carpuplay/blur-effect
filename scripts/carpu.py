from PIL import Image

#we create the function
def blur(org_file, dest_file, blur_x, blur_y, pos_x, pos_y):
    org_img = Image.open(org_file)
    height, width = org_img.size
    dest_img = Image.new("RGB",(height, width))

    for y in range(height):
        for x in range(width):

            if (x > pos_x) and (x < (pos_x + blur_x)) and (y > pos_y) and (y < (pos_y + blur_y)):
                r_tmp = []
                g_tmp = []
                b_tmp = []
                
                for y1 in range(15):    #change the range value for more blur
                    for x1 in range(15):
                        r, g, b = org_img.getpixel((x + x1 ,y + y1))
                        r_tmp.append(r)
                        g_tmp.append(g)
                        b_tmp.append(b)
                r = int(sum(r_tmp) / len(r_tmp))
                g = int(sum(g_tmp) / len(g_tmp))
                b = int(sum(b_tmp) / len(b_tmp))
                dest_img.putpixel((x,y),(r, g, b))
            
            else:
                r, g, b = org_img.getpixel((x, y))
                dest_img.putpixel((x, y), (r, g, b))  
    dest_img.save(dest_file)
    dest_img.show()

blur('./assets/cat.PNG', 'new.PNG', 215, 200, 300, 650)
