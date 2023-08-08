from django.shortcuts import render,redirect

from common.models import LookupField, Service,MediaGallery,MediaImages


# Create your views here.
def homepage(request):
    site_logo = LookupField.objects.get(code='site_logo')

    header_banner = LookupField.objects.get(code='header_banner')
    header_banner = header_banner.image

    #social links
    try:

        facebook = LookupField.objects.get(code='facebook')
        facebook = facebook.desc

        youtube = LookupField.objects.get(code='youtube')
        youtube = youtube.desc

        instagram = LookupField.objects.get(code='instagram')
        instagram = instagram.desc

        twitter = LookupField.objects.get(code='twitter')
        twitter = twitter.desc

        whatsapp = LookupField.objects.get(code='whatsapp')
        whatsapp = whatsapp.desc
    except:
        pass


    service = Service.objects.all().order_by('-id')
    context = {
        'site_logo':site_logo,
        'header_banner':header_banner,
        'service':service,
        'facebook':facebook,
        'youtube':youtube,
        'instagram':instagram,
        'twitter':twitter,
        'whatsapp':whatsapp,
    }
    return render(request,'index.html',context)

def about(request):
    site_logo = LookupField.objects.get(code='site_logo')

    # header_banner = LookupField.objects.get(code='header_banner')
    # header_banner = header_banner.image

    about = LookupField.objects.get(code='about')

    #social links
    try:

        facebook = LookupField.objects.get(code='facebook')
        facebook = facebook.desc

        youtube = LookupField.objects.get(code='youtube')
        youtube = youtube.desc

        instagram = LookupField.objects.get(code='instagram')
        instagram = instagram.desc

        twitter = LookupField.objects.get(code='twitter')
        twitter = twitter.desc

        whatsapp = LookupField.objects.get(code='whatsapp')
        whatsapp = whatsapp.desc
    except:
        pass

    context = {
        'site_logo':site_logo,
        # 'header_banner':header_banner,
        'about':about,
        'facebook':facebook,
        'youtube':youtube,
        'instagram':instagram,
        'twitter':twitter,
        'whatsapp':whatsapp,
    }
    return render(request,'about.html',context)

def media_gallery(request):
    site_logo = LookupField.objects.get(code='site_logo')

    # header_banner = LookupField.objects.get(code='header_banner')
    # header_banner = header_banner.image

    image_title = MediaGallery.objects.all()

    #social links
    try:

        facebook = LookupField.objects.get(code='facebook')
        facebook = facebook.desc

        youtube = LookupField.objects.get(code='youtube')
        youtube = youtube.desc

        instagram = LookupField.objects.get(code='instagram')
        instagram = instagram.desc

        twitter = LookupField.objects.get(code='twitter')
        twitter = twitter.desc

        whatsapp = LookupField.objects.get(code='whatsapp')
        whatsapp = whatsapp.desc
    except:
        pass

    context = {
        'site_logo':site_logo,
        # 'header_banner':header_banner,
        'title':image_title,
        'facebook':facebook,
        'youtube':youtube,
        'instagram':instagram,
        'twitter':twitter,
        'whatsapp':whatsapp,
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

        #social links
    try:

        facebook = LookupField.objects.get(code='facebook')
        facebook = facebook.desc

        youtube = LookupField.objects.get(code='youtube')
        youtube = youtube.desc

        instagram = LookupField.objects.get(code='instagram')
        instagram = instagram.desc

        twitter = LookupField.objects.get(code='twitter')
        twitter = twitter.desc

        whatsapp = LookupField.objects.get(code='whatsapp')
        whatsapp = whatsapp.desc
    except:
        pass
        context = {
            'site_logo':site_logo,
            # 'header_banner':header_banner,
            'title':title,
            'facebook':facebook,
            'youtube':youtube,
            'instagram':instagram,
            'twitter':twitter,
            'whatsapp':whatsapp,
        }
        return render(request,'upload_gallery.html',context)

def view_gallery(request, id):
    site_logo = LookupField.objects.get(code='site_logo')

    images = MediaImages.objects.filter(media_id_id=id)

    #social links
    try:

        facebook = LookupField.objects.get(code='facebook')
        facebook = facebook.desc

        youtube = LookupField.objects.get(code='youtube')
        youtube = youtube.desc

        instagram = LookupField.objects.get(code='instagram')
        instagram = instagram.desc

        twitter = LookupField.objects.get(code='twitter')
        twitter = twitter.desc

        whatsapp = LookupField.objects.get(code='whatsapp')
        whatsapp = whatsapp.desc
    except:
        pass
    context = {
        'site_logo':site_logo,
        'images':images,
        'facebook':facebook,
        'youtube':youtube,
        'instagram':instagram,
        'twitter':twitter,
        'whatsapp':whatsapp,
    }
    return render(request,'view_gallery.html', context)

def view_service(request, id):
    site_logo = LookupField.objects.get(code='site_logo')

    service = Service.objects.get(id=id)

    #social links
    try:

        facebook = LookupField.objects.get(code='facebook')
        facebook = facebook.desc

        youtube = LookupField.objects.get(code='youtube')
        youtube = youtube.desc

        instagram = LookupField.objects.get(code='instagram')
        instagram = instagram.desc

        twitter = LookupField.objects.get(code='twitter')
        twitter = twitter.desc

        whatsapp = LookupField.objects.get(code='whatsapp')
        whatsapp = whatsapp.desc
    except:
        pass
    context = {
        'site_logo':site_logo,
        'service':service,
        'facebook':facebook,
        'youtube':youtube,
        'instagram':instagram,
        'twitter':twitter,
        'whatsapp':whatsapp,
    }
    return render(request,'view_service.html', context)
