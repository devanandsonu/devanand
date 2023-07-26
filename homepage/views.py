from django.shortcuts import render,redirect

from common.models import LookupField, Service,MediaGallery,MediaImages


# Create your views here.
def homepage(request):
    site_logo = LookupField.objects.get(code='site_logo')

    header_banner = LookupField.objects.get(code='header_banner')
    header_banner = header_banner.image

    service = Service.objects.all().order_by('-id')
    context = {
        'site_logo':site_logo,
        'header_banner':header_banner,
        'service':service
    }
    return render(request,'index.html',context)

def about(request):
    site_logo = LookupField.objects.get(code='site_logo')

    # header_banner = LookupField.objects.get(code='header_banner')
    # header_banner = header_banner.image

    about = LookupField.objects.get(code='about')

    context = {
        'site_logo':site_logo,
        # 'header_banner':header_banner,
        'about':about
    }
    return render(request,'about.html',context)

def media_gallery(request):
    site_logo = LookupField.objects.get(code='site_logo')

    # header_banner = LookupField.objects.get(code='header_banner')
    # header_banner = header_banner.image

    image_title = MediaGallery.objects.all()

    context = {
        'site_logo':site_logo,
        # 'header_banner':header_banner,
        'title':image_title
    }
    return render(request,'media_gallery.html',context)

def upload_gallery(request):
    if request.method == 'POST':
        id = request.POST.getlist('title_id')
        images = request.FILES.getlist('image')
        for i in range(len(images)):
            MediaImages.objects.create(media_id_id=id[0], images=images[i])
        return redirect('/')
    else:
        site_logo = LookupField.objects.get(code='site_logo')

        # header_banner = LookupField.objects.get(code='header_banner')
        # header_banner = header_banner.image

        title = MediaGallery.objects.all()
        context = {
            'site_logo':site_logo,
            # 'header_banner':header_banner,
            'title':title
        }
        return render(request,'upload_gallery.html',context)

def view_gallery(request, id):
    site_logo = LookupField.objects.get(code='site_logo')

    images = MediaImages.objects.filter(media_id_id=id)
    context = {
        'site_logo':site_logo,
        'images':images
    }
    return render(request,'view_gallery.html', context)

def view_service(request, id):
    site_logo = LookupField.objects.get(code='site_logo')

    service = Service.objects.get(id=id)
    print(service,'============service')
    context = {
        'site_logo':site_logo,
        'service':service
    }
    return render(request,'view_service.html', context)
