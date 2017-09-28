from django.shortcuts import render
from .models import Agencia
from .models import Persona
from .models import Empresa
from .models import RegistroDeEmpleados
from .models import OfertaDeTrabajo
from .models import	TipoDeTrabajo

# Create your views here.

def post_list(request):
	return render(request, 'sistema/post_list.html', {})
