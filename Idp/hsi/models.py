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


class Patient(models.Model):
    patient_id = models.IntegerField(unique=True)


class HSISoftware(models.Model):
    hsi_software_name = models.CharField('Software Name', default='Senope', max_length=2048)
    hsi_software_version = models.CharField('Software version', max_length=2048)


class ImagingSettings(models.Model):
    class LightSource(models.TextChoices):
        XENON = 'Xenon'
        BLUE400 = 'Blue400'
        YELLOW500 = 'Yellow500'

    class Reference(models.TextChoices):
        REFLECTANCE = 'Reflectance'
        ABSORBANCE = 'Absorbance'

    class EnvDesc(models.TextChoices):
        OR301 = 'OR301'
        OR302 = 'OR302'
        OR303 = 'OR303'
        WETLAB = 'Wetlab'

    acquisition_type = models.CharField('Acquisition Type', max_length=2048)
    light_source_desc = models.CharField('Light Source Description', choices=LightSource.choices, max_length=2048)
    light_intensity = models.IntegerField()
    hsi_camera_name = models.CharField('Camera Name', default='Senop HSC-2', max_length=2048)
    optic_imaging_system = models.CharField('Optic Imaging System', default='Pentero 900', max_length=2048)
    hsi_camera_name = models.CharField('Camera Name', default='Senop HSC-2', max_length=2048)
    hsi_adapter_name = models.CharField('HSI Adapter Name', max_length=2048)
    reference = models.CharField('Reference', choices=Reference.choices, max_length=2048)
    environment_desc = models.CharField('Environment Description', choices=EnvDesc.choices, max_length=2048)
    software = models.ForeignKey(HSISoftware, on_delete=models.CASCADE)


class HSIImage(models.Model):
    hsi_id = models.IntegerField(unique=True)
    hsi_filename = models.CharField('Filename', max_length=2048)
    creation_timestamp = models.TimeField(auto_now_add=True)
    last_update_timestamp = models.TimeField(auto_now=True)
    bandpass_min = models.IntegerField()
    bandpass_max = models.IntegerField()
    hsi_height = models.IntegerField()
    hsi_width = models.IntegerField()
    hsi_bands = models.IntegerField()
    frames = models.IntegerField()
    data_size = models.IntegerField()
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    settings = models.ForeignKey(ImagingSettings, on_delete=models.CASCADE)


class Annotation(models.Model):
    annot_file_type = models.CharField('Annotation File Type', max_length=2048)
    annot_rate = models.IntegerField()
    hsi_image = models.OneToOneField(HSIImage, on_delete=models.CASCADE)


class Mask(models.Model):
    mask_filename = models.CharField('Mask filename', max_length=2048)
    annotation = models.ForeignKey(Annotation, on_delete=models.CASCADE)





