from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages



def index(request):

    try:
            
        stats = Statistics.objects.first()  
        stats_data = {
            'clients_count': stats.clients_count,
            'projects_count': stats.projects_count,
            'upcoming_projects_count': stats.upcoming_projects_count,
            'events_count': stats.events_count,
        }
    except:

         stats_data = {
            'clients_count': 0,
            'projects_count': 0,
            'upcoming_projects_count': 0,
            'events_count':0,
        }

    context = {
        'stats': stats_data
    }
    return render(request, 'index.html', context)
    # return render(request, 'index.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        contact_message = ContactMessage(name=name, email=email, message=message)
        contact_message.save()

        messages.success(request, 'Your message has been sent successfully!')

      
        referer = request.META.get('HTTP_REFERER')
        if referer:
            if 'contact' in referer:
                return redirect('contact')
            else:
                return redirect('home')

    return render(request, 'contact.html')


def chunk_list(data, chunk_size):
    
    for i in range(0, len(data), chunk_size):
        yield data[i:i + chunk_size]


def about(request):
    team_members = TeamMember.objects.all()
    team_member_chunks = list(chunk_list(team_members, 4)) 
    return render(request, 'about.html', {'team_member_chunks': team_member_chunks})


def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects.html', {'projects': projects})


def events(request):
    section = request.GET.get('section', 'ongoing')
    ongoing_events = Event.objects.filter(status='ongoing').order_by('created_at')
    upcoming_events = Event.objects.filter(status='upcoming').order_by('created_at')

    return render(request, 'events.html', {
        'ongoing_events': ongoing_events,
        'upcoming_events': upcoming_events,
        'section': section
    })

def gallery(request):
    gallery_images = GalleryImage.objects.all().order_by('-uploaded_at')[:12] 
    return render(request, 'gallery.html', {'gallery_images': gallery_images})

def load_more_images(request):
    offset = int(request.GET.get('offset', 0))
    limit = 12
    gallery_images = GalleryImage.objects.all().order_by('-uploaded_at')[offset:offset + limit]
    images = [{
        'src': image.image.url,
        'alt': f"Gallery Image {offset + idx + 1}",
        'description': image.description
    } for idx, image in enumerate(gallery_images)]
    return JsonResponse({'images': images})


def media(request):
    highlight_media = HighlightMedia.objects.last()
    media_items = Media.objects.all().order_by('-uploaded_at')[:8]
    return render(request, 'media.html', {
        'highlight_media': highlight_media,
        'media_items': media_items,
    })


def load_more_media(request):
    offset = int(request.GET.get('offset', 0))
    limit = 8
    media_items = Media.objects.all().order_by('-uploaded_at')[offset:offset + limit]
    items = [{
        'title': item.title,
        'media_type': item.media_type,
        'video_file': item.video_file.url if item.video_file else '',
        'video_id': item.video_id() if item.media_type == 'youtube' else '',

    } for item in media_items]
    return JsonResponse({'media_items': items})


def newsletter(request):
    return render(request, 'newsletter.html')


def terms_of_use(request):
    return render(request, 'termsofuse.html')


def privacy_policy(request):
    return render(request, 'privacy.html')


def helps(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if name and email and subject and message:
            SupportMessage.objects.create(name=name, email=email, subject=subject, message=message)
            messages.success(request, 'Your message has been sent successfully.')
            return redirect('help')
        else:
            messages.error(request, 'Please fill out all fields.')

    return render(request, 'help.html')


def faq(request):
    return render(request, 'faq.html')


def career(request):
    job_openings = JobOpening.objects.filter(is_active=True)

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        position_id = request.POST.get('position')
        message = request.POST.get('message')
        resume = request.FILES['resume']

        position = JobOpening.objects.get(id=position_id)
        job_application = JobApplication(
            name=name,
            email=email,
            position=position,
            message=message,
            resume=resume
        )
        job_application.save()

       
        return redirect('career')

    return render(request, 'career.html', {
        'job_openings': job_openings,
    })
