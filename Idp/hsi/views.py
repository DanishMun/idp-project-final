from django.shortcuts import render, redirect
from PIL import Image, ImageSequence
from django.views.decorators.csrf import csrf_exempt
from os.path import dirname, abspath
from .models import BinaryImages, MaskImages
from .spectral_tiffs import read_stiff
from django.core.exceptions import ObjectDoesNotExist
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

@csrf_exempt
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
    cube, wavelengths, preview_image, metadata = read_stiff(filepath + filename)
    try:
        img_inst = BinaryImages.objects.get(filename=filename)
    except ObjectDoesNotExist:
        img_inst = None
        pass

    if img_inst:
        img_inst.cube = str(cube)
        img_inst.wavelength = str(wavelengths)
        img_inst.metadata = str(metadata)
        img_inst.save()

    for i, page in enumerate(ImageSequence.Iterator(img)):
        try:
            img.seek(i)
            img.save(filepath + 'masks\\' + str(i) + filename.replace(' ','+').replace('.tif', '.png'), format='png')
            urlpath = maskpath + str(i) + filename.replace(' ','+').replace('.tif', '.png')
            images.append(urlpath)
            if img_inst:
                maskimg = MaskImages(linkimage=img_inst, url=urlpath)
                maskimg.save()

        except EOFError:
            break

    return render(request, 'hsi/details.html', {'imageurls': images,
                                                'imgnames': imagenames,
                                                'cube': cube,
                                                'wavelengths': wavelengths,
                                                'metadata': metadata})

def show_home(request):
    imagenames = []
    spectralimg = BinaryImages.objects.all()
    for img in spectralimg:
        imagenames.append(img.filename)
    return render(request, 'hsi/home.html', {'imgnames': imagenames})

