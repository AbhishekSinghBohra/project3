from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Techpile Technology</h1>")
