from django.shortcuts import render
from .models import Agencia
from .models import Persona
from .models import Empresa
from .models import RegistroDeEmpleados
from .models import OfertaDeTrabajo
from .models import	TipoDeTrabajo

# Create your views here.

def index(request):
	return render(request, 'sistema/startbootstrap-freelancer-gh-pages/index.html', {})



