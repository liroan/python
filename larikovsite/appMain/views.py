from django.shortcuts import render
from .models import MainPageM

# Create your views here.
def main_page(request):
    data = MainPageM.objects.all()
    return render(request, 'appMain/main_page.html', {'data': data})

