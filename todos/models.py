from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone
from django.shortcuts import reverse

class Autores(models.Model):
    autor_id = models.AutoField(primary_key=True)
    nome_autor = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nome_autor

    class Meta:
        ordering = ['nome_autor']
        verbose_name = "Cadastro de Autor"
        verbose_name_plural = "Cadastro de Autores"

class Livros(models.Model):
    livros_id = models.AutoField(primary_key=True)
    autor_id = models.ForeignKey(Autores, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100, verbose_name='Titulo do livro')
    qtlivros = models.BigIntegerField()
    estante = models.CharField(max_length=100)

    TIPOSTATUS_CHOICES = [
        ('Aluno', 'Aluno'),
        ('Professor', 'Professor'),
        ('Outros', 'Outros')
    ]
    tipostatus = models.CharField(max_length=30, choices=TIPOSTATUS_CHOICES, default='Aluno', verbose_name='Status do livro')

    edicao = models.CharField(max_length=100, blank=True)  # tornando o campo opcional
    assunto = models.CharField(max_length=100, blank=True)  # tornando o campo opcional
    data_publicacao = models.DateField()
    observacao = models.CharField(max_length=100, blank=True)  # tornando o campo opcional
    data_cadastro = models.DateField(default=timezone.now)  # Usando timezone.now como padrão

    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ['titulo']
        verbose_name = "Cadastro de Livros"
        verbose_name_plural = "Cadastro de Livros"

class Videos(models.Model):
    videos_id = models.AutoField(primary_key=True)
    colecao = models.CharField(max_length=100)
    nome_video = models.CharField(max_length=100, verbose_name='Nome do Video ')
    qtvideos = models.BigIntegerField()
    estante = models.CharField(max_length=50, blank=True)  # tornando o campo opcional
    observacao = models.CharField(max_length=100, blank=True)  # tornando o campo opcional
    data_cadastro = models.DateField(default=timezone.now)  # Usando timezone.now como padrão

    def __str__(self):
        return self.nome_video

    class Meta:
        ordering = ['nome_video']
        verbose_name = "Cadastro de Videos"
        verbose_name_plural = "Cadastro de Videos"

class Usuarios(models.Model):
    usuarios_id = models.AutoField(primary_key=True)
    nome_usuario = models.CharField(max_length=100)
    numeroRA = models.CharField(max_length=30)
    situacaoaluno = models.CharField(max_length=30)
    serie = models.CharField(max_length=20, unique=True)
    observacao = models.CharField(max_length=200, blank=True)  # tornando o campo opcional

    def __str__(self):
        return self.nome_usuario

    class Meta:
        ordering = ['nome_usuario']
        verbose_name = "Cadastro de Usuários"
        verbose_name_plural = "Cadastro de Usuários"

class EmprestimoLivro(models.Model):
    emprestimo_id = models.AutoField(primary_key=True)
    data_emprestimo = models.DateTimeField(default=timezone.now)
    data_devolucao = models.DateTimeField(blank=True, null=True)
    usuarios_id = models.ForeignKey('Usuarios', on_delete=models.CASCADE)
    livros_id = models.ForeignKey('Livros', on_delete=models.CASCADE, related_name='emprestimos_livro', blank=True,
                                  null=True)

    def save(self, *args, **kwargs):
        if self._state.adding:
            # Verifica se há estoque disponível antes de emprestar
            if self.livros_id.qtlivros > 0:
                # Subtrai 1 do estoque ao emprestar o livro
                self.livros_id.qtlivros -= 1
                self.livros_id.save()
            else:
                raise ValidationError("Este livro não tem estoque para empréstimo.")
        elif self.data_devolucao is not None:
            # Adiciona 1 ao estoque ao devolver o livro
            self.livros_id.qtlivros += 1
            self.livros_id.save()

        # Salva o objeto
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        # Redireciona para o menu após salvar o empréstimo
        return reverse('admin:index')

    class Meta:
        ordering = ['data_emprestimo']
        verbose_name = "Cadastrar Empréstimo de Livros"
        verbose_name_plural = "Cadastrar Empréstimo de Livros"

class EmprestimoVideo(models.Model):
    emprestimo_id = models.AutoField(primary_key=True)
    data_emprestimo = models.DateTimeField(default=timezone.now)
    data_devolucao = models.DateTimeField(blank=True, null=True)
    usuarios_id = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    videos_id = models.ForeignKey(Videos, on_delete=models.CASCADE, related_name='emprestimos_video', blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.pk is None:
            # Verifica se há estoque disponível antes de emprestar
            if self.videos_id and self.videos_id.qtvideos <= 0:
                raise ValidationError("Não há estoque disponível para este vídeo.")

            # Subtrai 1 do estoque ao emprestar o vídeo
            self.videos_id.qtvideos -= 1
        elif self.data_devolucao is not None:
            # Adiciona 1 ao estoque ao devolver o vídeo
            self.videos_id.qtvideos += 1

        # Garante que o estoque não seja negativo
        if self.videos_id and self.videos_id.qtvideos < 0:
            raise ValueError("Erro ao atualizar o estoque.")

        # Salva o objeto
        super().save(*args, **kwargs)

        # Atualiza o estoque do vídeo no banco de dados
        if self.videos_id:
            self.videos_id.save()

    class Meta:
        ordering = ['data_emprestimo']
        verbose_name = "Cadastrar Empréstimo de Videos"
        verbose_name_plural = "Cadastrar Empréstimo de Videos"

    def __str__(self):
        if self.usuarios_id and self.videos_id:
            return f"Usuário: {self.usuarios_id.nome_usuario} - Nome do Vídeo: {self.videos_id.nome_video} - Data Empréstimo: {self.data_emprestimo} - Data Devolução: {self.data_devolucao}"
        return f"Emprestimo ID: {self.emprestimo_id} - Data Empréstimo: {self.data_emprestimo} - Data Devolução: {self.data_devolucao}"


