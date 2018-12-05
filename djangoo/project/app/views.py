from django.shortcuts import render
from django.http import HttpResponse
from app.models import MyModels
from django.core.files import File
from wsgiref.util import FileWrapper
# Create your views here.

def index(request):
    return render(request, 'index.html')

def send_data(request):
    name = request.POST.get("Name")
    email = request.POST.get("Email")
    phone = request.POST.get("Number")

    myModels_database = MyModels(name = name , email = email , phone = phone)

    myModels_database.save()
    f = open("app/files/Database_Details.txt", 'w+')
    f.write("Name : {0}\n".format(name))
    f.write("Email : {0}\n".format(email))
    f.write("Phone : {0}\n".format(phone))
    f.close()

    return render(request, 'thanks.html')

def download_link(request):
    wrapper = FileWrapper(open("app/files/Database_Details.txt"))
    response = HttpResponse(wrapper, content_type = 'app/files/')
    response['Content-Disposition'] = 'attachment ; filename : Database_Details.txt'

    return response