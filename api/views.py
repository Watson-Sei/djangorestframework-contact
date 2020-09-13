from django.http import HttpResponse
from .models import ContactEmail
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def contactemail(request):
    if request.method == 'POST':
        c = ContactEmail()
        c.username = request.POST['username']
        c.email = request.POST['email']
        c.subject = request.POST['subject']
        c.contents = request.POST['contents']
        c.save()
        return HttpResponse(status=200)

    return HttpResponse(status=204)
