from django.contrib import admin

# Register your models here.
# principal/admin.py
from django.contrib import admin
from .models import PaginaInicial, Jogo, Quiz, Pergunta, Resposta, TentativaQuiz

admin.site.register(PaginaInicial)
admin.site.register(Jogo)
admin.site.register(Quiz)
admin.site.register(Pergunta)
admin.site.register(Resposta)
admin.site.register(TentativaQuiz)
