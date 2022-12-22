from PIL import Image

#we create the function
def blur(org_file, dest_file, blur_x, blur_y):
    org_img = Image.open(org_file)
    height, width = org_img.size
    dest_img = Image.new("RGB",(height, width))

    for y in range(blur_y):
        for x in range(blur_x):
            r, g, b = org_img.getpixel(x,y)
            c = int((r+g+b)/3)
            dest_img.putpixel((x,y),(c,c,c))
    dest_img.save(dest_file)
    dest_img.show()

