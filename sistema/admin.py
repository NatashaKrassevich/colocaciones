from django.contrib import admin
from .models import Agencia
from .models import Persona
from .models import Empresa
from .models import RegistroDeEmpleados
from .models import OfertaDeTrabajo
from .models import TipoDeTrabajo

# Register your models here.

admin.site.register(Agencia)
