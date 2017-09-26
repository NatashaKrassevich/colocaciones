from django.contrib import admin
from .models import Agencia
from .models import Persona
from .models import Empresa
from .models import RegistroDeEmpleados
from .models import OfertaDeTrabajo
from .models import TipoDeTrabajo

# Register your models here.

admin.site.register(Agencia)
admin.site.register(Persona)
admin.site.register(Empresa)
admin.site.register(RegistroDeEmpleados)
admin.site.register(OfertaDeTrabajo)
admin.site.register(TipoDeTrabajo)