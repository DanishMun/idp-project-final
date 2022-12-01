from django.db import models

class BinaryImages(models.Model):
    filename = models.CharField(max_length=50)
    wavelength = models.CharField(max_length=500, default=None, blank=True, null=True)
    cube = models.CharField(max_length=500, default=None, blank=True, null=True)
    metadata = models.CharField(max_length=500, default=None, blank=True, null=True)

    def __str__(self):
        return 'Image-' + self.filename

class MaskImages(models.Model):
    linkimage = models.ForeignKey('BinaryImages', default=None, on_delete=models.SET_DEFAULT)
    url = models.CharField(max_length=50)

    def __str__(self):
        return 'URL-' + self.url





