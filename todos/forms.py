from django import forms
from .models import Autores, Livros, Videos, Usuarios, EmprestimoLivro, EmprestimoVideo


class AutoresForm(forms.ModelForm):
    class Meta:
        model = Autores
        fields = ['nome_autor']


class LivrosForm(forms.ModelForm):
    class Meta:
        model = Livros
        fields = ['titulo', 'qtlivros', 'estante']


class VideosForm(forms.ModelForm):
    class Meta:
        model = Videos
        fields = ['nome_video', 'qtvideos', 'colecao']


class UsuariosForm(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = ['nome_usuario', 'numeroRA', 'situacaoaluno']


class EmprestimoLivroForm(forms.ModelForm):
    class Meta:
        model = EmprestimoLivro
        fields = ['livros_id', 'data_emprestimo', 'data_devolucao']


class EmprestimoVideoForm(forms.ModelForm):
    class Meta:
        model = EmprestimoVideo
        fields = ['videos_id']
