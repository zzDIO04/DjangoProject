from django.db import models
from escola.models import Disciplina, Usuario

# Create your models here.

# principal/models.py
from django.db import models

class PaginaInicial(models.Model):
    titulo = models.CharField(max_length=100)
    conteudo = models.TextField()

    def __str__(self):
        return self.titulo

class Jogo(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    icone = models.CharField(max_length=100, help_text='Nome do ícone SVG ou URL da imagem')
    cor_fundo = models.CharField(max_length=30, default='#f3eaff', help_text='Cor de fundo do card (ex: #f3eaff)')
    slug = models.SlugField(unique=True, help_text='URL do quiz, ex: matematica, ciencias')

    def __str__(self):
        return self.titulo

class Quiz(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, related_name='quizzes')
    criado_por = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='quizzes_criados')
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class Pergunta(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='perguntas')
    texto = models.TextField()

    def __str__(self):
        return self.texto

class Resposta(models.Model):
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE, related_name='respostas')
    texto = models.CharField(max_length=255)
    correta = models.BooleanField(default=False)

    def __str__(self):
        return self.texto

class TentativaQuiz(models.Model):
    aluno = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='tentativas')
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='tentativas')
    acertos = models.PositiveIntegerField()
    total = models.PositiveIntegerField()
    data = models.DateTimeField(auto_now_add=True)

    def percentual(self):
        if self.total:
            return int((self.acertos / self.total) * 100)
        return 0

    def __str__(self):
        return f"{self.aluno.username} - {self.quiz.titulo} ({self.percentual()}%)"

