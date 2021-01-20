from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib import messages
from twilio.rest import Client
import mimetypes
from django.http import HttpResponse

from .forms import ContactForm
from .models import Contact

# Create your views here.

def homePage(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = request.POST.get('name')
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            description = request.POST.get('description')
            
            userMessage = Contact.objects.create(name=name, email=email, subject=subject, description=description)
            userMessage.save()

            # get submitted data
            user_email = form.cleaned_data.get('email')
            user_subject = form.cleaned_data.get('subject')
            user_Descr = form.cleaned_data.get('description')

            messages.success(request, 'Your Message on ' + user_subject + ' was submitted Successfully. I will be in touch you as soon as possible.')

            # twilio credetials
            account_sid = settings.TWILIO_ACCOUNT_SID
            auth_token = settings.TWILIO_AUTH_TOKEN
            client = Client(account_sid, auth_token)
            message = client.messages.create(
                            body='Yooh Oliver, You\'ve a message on your site.\nIt was sent by '+ user_email +' .\nSubject: '+ user_subject + '.\nDescription:\n '+ user_Descr +' ',
                            from_= settings.TWILIO_NUMBER,
                            to='+254799773244'
                        )
            

            return redirect('home')
        else:
            form = ContactForm()

    context = {'form':form}
    return render(request, 'myprofileTemp/index.html', context)


def downloadFile(request):
    filePath = settings.RESUME_URL
    fileName = 'resume.pdf'
    
    f = open(filePath, 'r')
    mime_type, _ = mimetypes.guess_type(filePath)
    response = HttpResponse(f, content_type=mime_type)
    response['Content-Disposition'] = "attachment; fileName=%s" % fileName
    return response

    
