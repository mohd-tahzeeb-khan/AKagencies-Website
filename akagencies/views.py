from django.http import HttpResponse
from django.shortcuts import render
from contact.models import contactus
from contact.forms import formcontactus


def index(request):
    contact=formcontactus(request.POST)
    print(contact)
    data={'form':contact}
    return render(request, "index.html", data)
def savecontact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        mobileno=request.POST.get('mobileno')
        description=request.POST.get('description')
        savedata=contactus(name=name, email=email, mobile=mobileno, message=description)
        savedata.save()
        return HttpResponse("Thank You so Much")

