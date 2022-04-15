from unicodedata import name
from django.shortcuts import render
from contactUs.models import Contact

# Create your views here.

def index(request):        
    if request.method == 'POST':
        full_name = request.POST['name']
        email = request.POST['email']
        phone_number = request.POST['phn_num']
        subject = request.POST['subject']
        message = request.POST['message']

        # print(full_name, email, phone_number, subject, message)
        ins = Contact(name=full_name, email=email, phn_num=phone_number, subject=subject, message=message)
        ins.save()
        # print("data has been writteen to the db")
        
    return render(request, 'contactUs/index1.html')

