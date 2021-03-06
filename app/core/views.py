from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from app.core.models import *
from app.core.forms import *

def get_current_user(request):
    user = request.user
    user.refresh_from_db()
    return user

def home(request):
    if (request.user.is_authenticated()):
        return redirect('private')
    return render(request, 'home.html')

def inicio(request):
    return render(request, 'inicio.html')

def registrate(request):
    return render(request, 'registrate.html')

def post_list(request):
    return render(request, 'post_list.html')

@login_required
def private(request):
    user = request.user
    user.refresh_from_db()
    return render(request, 'private.html', {'user': user})

def registro_desocupado(request):
    # Cuando algo llega a esta vista (llamada desde una URL) puede venir por dos
    # vias distintas. Como una petición GET (Se ingresó en la barra de direccion
    # del navegador la URL o se siguió un link a esa URL) o como POST (Se envió
    # un formulario a esa dirección). Por tanto tengo que procesar ambas
    # alternativas.
    if request.method == "GET":
        # Como es GET solo debo mostrar la página. Llamo a otra función que se
        # encargará de eso.
        return get_registro_desocupado_form(request)
    elif request.method == 'POST':
        # Como es POST debo procesar el formulario. Llamo a otra función que se
        # encargará de eso.
        return handle_registro_desocupado_form(request)

def get_registro_desocupado_form(request):
    form = RegistroDesocupado()
    return render(request, 'signup.html', {'form': form})

def handle_registro_desocupado_form(request):
    form = RegistroDesocupado(request.POST)
    # Cuando se crea un formulario a partir del request, ya se obtienen a traves
    # de este elemento los datos que el usuario ingresó. Como el formulario de
    # Django ya está vinculado a la entidad, entonces hacer form.save() ya crea
    # un elemento en la base de datos.
    if form.is_valid():
        # Primero hay que verificar si el formulario es válido, o sea, si los
        # datos ingresados son correctos. Sino se debe mostrar un error.
        form.save()
        # Si se registró correctamente, se lo envía a la pantalla de login
        return redirect('login')
    else:
        # Quedarse en la misma página y mostrar errores
        return render(request, 'signup.html', {'form': form})

def registro_empresa(request):
    if request.method == "GET":
        return get_registro_empresa_form(request)
    elif request.method == 'POST':
        return handle_registro_empresa_form(request)

def get_registro_empresa_form(request):
    form = RegistroEmpresa()
    return render(request, 'signup.html', {'form': form})

def handle_registro_empresa_form(request):
    form = RegistroEmpresa(request.POST)
    if form.is_valid():
        form.save()
        return redirect('login')
    else:
        return render(request, 'signup.html', {'form': form})


@login_required
def edit_user(request):
    if request.method == "GET":
        return get_edit_user(request, request.user.id)
    elif request.method == "POST":
        return handler_edit_user(request, request.user.id)

def get_edit_user(request, pk):
    user = request.user
    user.refresh_from_db()
    if request.user.is_desocupado():
        form = EditarDesocupado(instance= User.objects.get(id=request.user.id).desocupado)
    else:
        form = EditarEmpresa(instance= User.objects.get(id=request.user.id).empresa)
    return render(request, 'edit_user.html', {'form': form})

def handler_edit_user(request, pk):
    user = request.user
    user.refresh_from_db()
    if request.user.is_desocupado():
        form = EditarDesocupado(request.POST, instance= User.objects.get(id=request.user.id).desocupado)
    else: 
        form = EditarEmpresa(request.POST, instance= User.objects.get(id=request.user.id).empresa)
    if form.is_valid():
        form.save()
        return redirect('edit_user')
    else:
        return render(request, 'edit_user.html', {'form': form})


@login_required
def user_delete(request):
    User.objects.get(id=request.user.id).delete()
    return redirect('logout')



def registrarOfertaDeTrabajo(request):
    if request.method == "GET":
        return get_registrarOfertaDeTrabajo_form(request)
    elif request.method == 'POST':
        return handle_registrarOfertaDeTrabajo_form(request)

def get_registrarOfertaDeTrabajo_form(request):
    form = RegistrarOfertaDeTrabajo()
    return render(request, 'oferta de trabajo.html', {'form': form})

def handle_registrarOfertaDeTrabajo_form(request):
    form = RegistrarOfertaDeTrabajo(request.POST)
    if form.is_valid():
        form.save()
        return redirect('lista_ofertas')
    else:
        return render(request, 'oferta de trabajo.html', {'form': form})

@login_required
def edit_oferta(request, pk):
    if request.method == "GET":
        return get_edit_oferta(request, pk)
    elif request.method == 'POST':
        return handler_edit_oferta(request, pk)

def get_edit_oferta(request, pk):
    form = EditarOferta(instance=OfertaDeTrabajo.objects.get(id=pk))
    return render(request, 'edit_oferta.html', {'form': form, 'user': get_current_user(request)})

def handler_edit_oferta(request, pk):
    form = EditarOferta(request.POST, instance=OfertaDeTrabajo.objects.get(id=pk))
    if form.is_valid():
        form.save()
        return redirect('lista_ofertas')
    else:
        return render(request, 'edit_oferta.html', {'form': form, 'user': get_current_user(request)})

@login_required
def oferta_delete(request, pk):
    OfertaDeTrabajo.objects.get(id=pk).delete()
    return redirect('lista_ofertas')

@login_required
def lista_ofertas(request):
    ofertasvar = OfertaDeTrabajo.objects.all()
    return render(request, 'lista_ofertas.html', {'ofertas': ofertasvar})
