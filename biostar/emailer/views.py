from django.shortcuts import render
from .models import *
from django.db.models import Count

from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponse

def index(request):

    groups = EmailGroup.objects.all().annotate(count=Count('subscription')).order_by("-count")

    subs = EmailSubscription.objects.all()[:20]

    context = dict(groups=groups,subs=subs)
    return render(request, "emailer/index.html", context=context)



def send_bcc_email(request):
    subject = 'Test Email with BCC'
    from_email = 'from@example.com'
    to_email = ["bioconductor.digest@gmail.com"]  # Empty, because we don't want anyone in the 'To' field
    bcc_email = ['bcc@example.com', 'anotherbcc@example.com']

    # Create the email message with HTML and plain text parts
    msg = EmailMultiAlternatives(
        subject, 'This is the plain text body', from_email, to_email, bcc=bcc_email
    )
    msg.attach_alternative('<p>This is the HTML body</p>', 'text/html')

    print("BCC Recipents:", msg.bcc)
    # Send the email
    msg.send(fail_silently=False)

    return HttpResponse('Email Sent (check the console for details)')

