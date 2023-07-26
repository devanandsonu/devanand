from django.db import models


# Create your models here.

class LookupField(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True)
    code = models.CharField(max_length=50, null=True, blank=True)
    desc = models.TextField(null=True, blank=True)
    image = models.FileField(upload_to='lookup_image', null=True, blank=True)

    attr1 = models.CharField(max_length=50, null=True, blank=True)
    attr2 = models.CharField(max_length=50, null=True, blank=True)
    attr3 = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.title


class Service(models.Model):
    title = models.CharField(max_length=500, null=True, blank=True)
    desc = models.TextField(null=True, blank=True)
    image = models.FileField(upload_to='service_image', null=True, blank=True)

    attr1 = models.CharField(max_length=50, null=True, blank=True)
    attr2 = models.CharField(max_length=50, null=True, blank=True)
    attr3 = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.title


class MediaGallery(models.Model):
    code = models.CharField(max_length=50, default='media', null=True, blank=True)
    poster = models.FileField(upload_to='media_poster', null=True, blank=True)

    def __str__(self):
        return self.code

class MediaImages(models.Model):
    media_id = models.ForeignKey(MediaGallery, on_delete=models.CASCADE)
    images = models.FileField(upload_to='media_images', null=True, blank=True)
