from django.contrib import admin
from .models import LookupField,MediaGallery,Service,MediaImages
# Register your models here.
admin.site.register(LookupField)
admin.site.register(MediaGallery)
admin.site.register(MediaImages)
admin.site.register(Service)
