from django.contrib import admin
from .models import BinaryImages, MaskImages, Patient, HSISoftware, ImagingSettings, HSIImage, Annotation, Mask

admin.site.register(BinaryImages)
admin.site.register(MaskImages)
admin.site.register(Patient)
admin.site.register(HSISoftware)
admin.site.register(ImagingSettings)
admin.site.register(HSIImage)
admin.site.register(Annotation)
admin.site.register(Mask)

