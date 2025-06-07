from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    TIPO_CHOICES = (
        ('aluno', 'Aluno'),
        ('professor', 'Professor'),
    )
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    matricula = models.CharField(max_length=20, unique=True, null=True, blank=True)

class Disciplina(models.Model):
    nome = models.CharField(max_length=100)
    codigo = models.CharField(max_length=20, unique=True)
    professor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='disciplinas_lecionadas')
    alunos = models.ManyToManyField(Usuario, related_name='disciplinas_matriculadas')

    def __str__(self):
        return self.nome

class Nota(models.Model):
    aluno = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='notas')
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, related_name='notas')
    valor = models.DecimalField(max_digits=4, decimal_places=2)
    data = models.DateField(auto_now_add=True)
    observacao = models.TextField(blank=True, null=True)

    class Meta:
        unique_together = ['aluno', 'disciplina']

    def __str__(self):
        return f"{self.aluno.username} - {self.disciplina.nome}: {self.valor}" 