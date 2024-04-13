from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect, render
from .forms import AutoresForm, LivrosForm, VideosForm, UsuariosForm, EmprestimoLivroForm, EmprestimoVideoForm

def home(request):
    if request.user.is_authenticated:
        # Se o usuário estiver autenticado, redireciona para a página de administração do Django
        return redirect('/admin/')
    else:
        # Se o usuário não estiver autenticado, renderiza a tela inicial de boas-vindas
        return render(request, 'todos/home.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')  # Redireciona para a página inicial após o registro
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def sua_visualizacao(request):
    if request.method == 'POST':
        form = SeuFormulario(request.POST)
        if form.is_valid():
            # Processar os dados do formulário se forem válidos
            # Exemplo: salvar os dados ou executar alguma ação com eles
            # Após o processamento bem-sucedido, você pode redirecionar o usuário para outra página
            return redirect('login')  # Substitua 'login' pelo nome da rota da página de login
    else:
        form = SeuFormulario()

    return render(request, 'login.html', {'form': form})

from .forms import LivrosForm

def minha_view(request):
    if request.method == 'POST':
        form = LivrosForm(request.POST)
        if form.is_valid():
            form.save()
            # redirecionar ou fazer algo após salvar
    else:
        form = LivrosForm()
    return render(request, 'template.html', {'livros_form': form})

from .forms import VideosForm

def minha_view(request):
    if request.method == 'POST':
        form = VideosForm(request.POST)
        if form.is_valid():
            form.save()
            # redirecionar ou fazer algo após salvar
    else:
        form = VideosForm()
    return render(request, 'template.html', {'Videos_form': form})






