from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('painel/', views.painel_professor, name='painel_professor'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('criar-quiz/', views.criar_quiz, name='criar_quiz'),
    path('criar-pergunta/<int:quiz_id>/', views.criar_pergunta, name='criar_pergunta'),
    path('criar-resposta/<int:pergunta_id>/', views.criar_resposta, name='criar_resposta'),
    path('quizzes/', views.quizzes_aluno, name='quizzes_aluno'),
    path('jogar-quiz/<int:quiz_id>/', views.jogar_quiz, name='jogar_quiz'),
    path('desempenho-quiz/<int:quiz_id>/', views.desempenho_quiz, name='desempenho_quiz'),
]
