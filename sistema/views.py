from django.shortcuts import render
from django.utils import timezone
from .models import Agencia

# Create your views here.

def post_list(request):
	return render(request, 'sistema/post_list.html', {})
