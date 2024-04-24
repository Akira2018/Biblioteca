from django.contrib import admin
from django.core.exceptions import ValidationError
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Autores, Livros, Videos, Usuarios, EmprestimoLivro, EmprestimoVideo

@admin.register(Autores)
class AutoresAdmin(admin.ModelAdmin):
    # Definindo a exibição do nome no aplicativo Django Admin
    verbose_name = "Cadastro de Autores"
    verbose_name_plural = "Cadastro de Autores"
    search_fields = ['nome_autor']
    list_display = ['nome_autor']

@admin.register(Livros)
class LivrosAdmin(admin.ModelAdmin):
    # Definindo a exibição do nome no aplicativo Django Admin
    verbose_name = "Cadastro de Livros"
    verbose_name_plural = "Cadastro de Livros"
    search_fields = ('titulo', 'qtlivros', 'estante')
    list_display = ('titulo', 'qtlivros', 'estante')

@admin.register(Videos)
class VideosAdmin(admin.ModelAdmin):
    # Definindo a exibição do nome no aplicativo Django Admin
    verbose_name = "Cadastro de Videos"
    verbose_name_plural = "Cadastro de Videos"
    search_fields = ['nome_video', 'qtvideos', 'colecao']
    list_display = ['nome_video', 'qtvideos', 'colecao']

@admin.register(Usuarios)
class UsuariosAdmin(admin.ModelAdmin):
    # Definindo a exibição do nome no aplicativo Django Admin
    verbose_name = "Cadastro de Usuários"
    verbose_name_plural = "Cadastro de Usuários"
    search_fields = ['nome_usuario', 'numeroRA', 'situacaoaluno']
    list_display = ['nome_usuario', 'numeroRA', 'situacaoaluno']

@admin.register(EmprestimoLivro)
class EmprestimoLivroAdmin(admin.ModelAdmin):
    # Definindo a exibição do nome no aplicativo Django Admin
    verbose_name = "Cadastro de Empréstimo de Livros"
    verbose_name_plural = "Cadastro de Empréstimo de Livros"
    search_fields = ['nome_usuario', 'livros_id__titulo', 'data_emprestimo', 'data_devolucao']
    list_display = ['usuarios_nome','get_tipo_item','livro_titulo', 'formatted_data_emprestimo', 'formatted_data_devolucao']

    def response_add(self, request, obj, post_url_continue=None):
        # Redirecionando para a página de lista de empréstimos de livro
        return HttpResponseRedirect(reverse('admin:todos_emprestimolivro_changelist'))

    def save_model(self, request, obj, form, change):
        try:
            obj.full_clean()  # Validação de modelo antes de salvar
            obj.save()
            # Personalizando a mensagem de sucesso após adicionar um novo objeto
            self.message_user(request, "O empréstimo do livro foi adicionado com sucesso.", level='SUCCESS')
        except ValidationError as e:
            if 'Este livro não tem estoque para empréstimo.' in e.messages:
                # Exibir uma mensagem de erro amigável para o usuário
                self.message_user(request, "Este livro não tem estoque disponível para empréstimo.", level='ERROR')
            else:
                raise e  # Se for outra exceção de validação, levanta novamente para o admin

    def get_tipo_item(self, obj):
        return 'Livro'
    get_tipo_item.short_description = 'Tipo de Item'

    def usuarios_nome(self, obj):
        return obj.usuarios_id.nome_usuario if obj.usuarios_id else None
    usuarios_nome.short_description = 'Nome do Usuário'

    def livro_titulo(self, obj):
        return obj.livros_id.titulo if obj.livros_id else None
    livro_titulo.short_description = 'Título do Livro'

    def formatted_data_emprestimo(self, obj):
        return obj.data_emprestimo.strftime('%d/%m/%Y %H:%M:%S') if obj.data_emprestimo else None
    formatted_data_emprestimo.short_description = 'Data Empréstimo'

    def formatted_data_devolucao(self, obj):
        return obj.data_devolucao.strftime('%d/%m/%Y %H:%M:%S') if obj.data_devolucao else None
    formatted_data_devolucao.short_description = 'Data Devolução'

@admin.register(EmprestimoVideo)
class EmprestimoVideoAdmin(admin.ModelAdmin):
    # Definindo a exibição do nome no aplicativo Django Admin
    verbose_name = "Cadastro de Empréstimo de Videos"
    verbose_name_plural = "Cadastro de Empréstimo de Videos"
    list_display = ('usuario_nome', 'formatted_data_emprestimo', 'formatted_data_devolucao', 'video_nome')
    list_filter = ('data_emprestimo', 'data_devolucao', 'usuarios_id')
    search_fields = ('usuarios_id__nome_usuario', 'videos_id__nome_video')
    date_hierarchy = 'data_emprestimo'
    ordering = ('-data_emprestimo',)

    def response_add(self, request, obj, post_url_continue=None):
        # Redirecionar para a lista de empréstimos de vídeos após adição bem-sucedida
        return HttpResponseRedirect(reverse('admin:todos_emprestimovideo_changelist'))

    def save_model(self, request, obj, form, change):
        try:
            obj.full_clean()  # Validação de modelo antes de salvar
            obj.save()
            # Personalizando a mensagem de sucesso após adicionar um novo objeto
            self.message_user(request, "O empréstimo do vídeo foi adicionado com sucesso.", level='SUCCESS')
            return HttpResponseRedirect(reverse('admin:todos_emprestimovideo_changelist'))  # Redirecionar para a lista de empréstimos de vídeo após adição bem-sucedida
        except ValidationError as e:
            if 'Não há estoque disponível para este vídeo.' in e.messages:
                # Exibir uma mensagem de erro amigável para o usuário
                self.message_user(request, "Não há estoque disponível para este vídeo.", level='ERROR')
            else:
                raise e  # Se for outra exceção de validação, levanta novamente para o admin

    def usuario_nome(self, obj):
        return obj.usuarios_id.nome_usuario if obj.usuarios_id else None
    usuario_nome.short_description = 'Nome do Usuário'

    def video_nome(self, obj):
        return obj.videos_id.nome_video if obj.videos_id else None
    video_nome.short_description = 'Nome do Vídeo'

    def formatted_data_emprestimo(self, obj):
        return obj.data_emprestimo.strftime('%d/%m/%Y %H:%M:%S') if obj.data_emprestimo else None
    formatted_data_emprestimo.short_description = 'Data Empréstimo'

    def formatted_data_devolucao(self, obj):
        return obj.data_devolucao.strftime('%d/%m/%Y %H:%M:%S') if obj.data_devolucao else None
    formatted_data_devolucao.short_description = 'Data Devolução'