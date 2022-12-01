from django.shortcuts import render, redirect
from PIL import Image, ImageSequence
from os.path import dirname, abspath
from .models import BinaryImages, MaskImages
# from .spectral_tiffs import read_stiff
import numpy as np
import os, io

def show_images(request, filename):
    imageurls = []
    app_path = dirname(abspath(__file__))
    # filepath = os.path.abspath('static') + '\images'
    filepath = app_path + '\static\images'
    from django.contrib.staticfiles import finders

    maskfiles = os.path.abspath('static') + "\images\masks"
    # os.mkdir(maskfiles)
    print(maskfiles)
    # img = Image.open(filepath + '\\' + filename)
    imageurls.append(filepath + '\\' + filename)

    for i, page in enumerate(ImageSequence.Iterator(img)):
        try:
            img.seek(i)
            # img.show()
        except EOFError:
            # Not enough frames in img
            break
    return render(request, 'hsi/home.html', {'imageurls': imageurls})

def show_multiframe(request, filename):
    images = []
    imagenames = []
    app_path = dirname(abspath(__file__))
    spectralimg = BinaryImages.objects.all()
    for img in spectralimg:
        imagenames.append(img.filename)
    # filepath = os.path.abspath('static') + '\images' + '\\'
    filepath = app_path + '\static\images' + '\\'
    maskpath = '/static/images/masks/'
    img = Image.open(filepath + filename)
    # cube, wavelengths, preview_image, metadata = read_stiff(filepath + filename)
    for i, page in enumerate(ImageSequence.Iterator(img)):
        try:
            img.seek(i)
            img.save(filepath + 'masks\\' + str(i) + filename.replace('.tif', '.png'), format='png')
            images.append(maskpath + str(i) + filename.replace('.tif', '.png'))

        except EOFError:
            break
    # png_images = []
    # for img_arr in images:
    #     png_buffer = io.BytesIO()
    #     image = Image.fromarray(img_arr)
    #     image.save(png_buffer, format='png')
    #     png_images.append(png_buffer.seek(0))
    return render(request, 'hsi/details.html', {'imageurls': images,
                                                'imgnames': imagenames})

def show_home(request):
    imagenames = []
    spectralimg = BinaryImages.objects.all()
    for img in spectralimg:
        imagenames.append(img.filename)
    return render(request, 'hsi/home.html', {'imgnames' : imagenames})

