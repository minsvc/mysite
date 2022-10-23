from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("welcome to django.")

def user_list(request):
    return render(request, "user_list.html")

def user_add(request):
    return HttpResponse("添加用户")
