from django import forms
from .models import Persona

class PersonaForm(forms.ModelForm):
	class Meta:
		model = Persona
		fields = ('nombre', 'apellido', 'dni', 'fechaNac', 'tipoDeTrabajo', 'activo', '')
	
			

