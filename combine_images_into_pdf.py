from fpdf import FPDF
pdf = FPDF()

from PIL import Image

im1 = "Pictures\\a.jpg"
im2 = "Pictures\\b.jpg"
im3 = "Pictures\\c.jpg"
im_list = [im1,im2,im3]

pdf1_filename = "Pictures\\image_pdf.pdf"

for image in im_list:

    print str(image)
    im = Image.open(image)
    width, height = im.size
    print str(width) + ' x ' +str(height)
    if height > 500:
        while height > 500:
            width = width / 10
            height = height / 10

    if width > 500:
        while width > 500:
            width = width / 10
            height = height / 10

    print str(width) + ' x ' +str(height)
    x,y,w,h = 0,0,width,height

    pdf.add_page()
    pdf.image(image,x,y,w,h)
pdf.output("Pictures\\image_pdf.pdf", "F")
