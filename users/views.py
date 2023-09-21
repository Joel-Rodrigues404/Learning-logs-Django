from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def logout_view(request):
    """ Faz logout do usuario """
    logout(request)
    return HttpResponseRedirect(reverse('learning_logs:index'))

def register(request):
    """ Faz o cadastro de novos usuarios """
    if request.method != 'POST':
        #Exibe um formulario de cadastro em branco
        form = UserCreationForm()
    else:
        #Processa um formulario preenchido
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            #faz login do usuario e retorna para a pagina inicial
            authenticated_user = authenticate(
                username = new_user.username,
                password = request.POST['password1']
            )
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('learning_logs:index'))
    context = {'form':form}
    return render(request, 'users/register.html', context)

