from django.shortcuts import render

# Create your views here.
def index(request):
    request.session.set_expiry(300)
    return render(request, "dashboard/index.html")