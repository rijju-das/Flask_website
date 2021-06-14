# -*- coding: utf-8 -*-

from pdf2image import convert_from_path, convert_from_bytes

path=r'M.Tech._passCertificate.pdf'


from pdf2image import convert_from_path
def pdf2img():
    images = convert_from_path(path,dpi=200,poppler_path=r'poppler-0.68.0_x86\bin')
    for i, image in enumerate(images):
        fname = 'image'+str(i)+'.png'
        image.save(fname, "PNG")

