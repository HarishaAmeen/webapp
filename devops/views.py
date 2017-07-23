from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
	images = ['devops/images/slide1.jpg', 'devops/images/slide2.jpg', 'devops/images/slide2.jpg']
	context = {'images': images }
	return render(request, 'devops/index.html', context)