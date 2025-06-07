from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Jogo, Quiz, Pergunta, Resposta, TentativaQuiz
from escola.models import Disciplina, Usuario
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def index(request):
    jogos = Jogo.objects.all()
    return render(request, 'principal/index.html', {'jogos': jogos})

@login_required
def painel_professor(request):
    if not hasattr(request.user, 'tipo') or request.user.tipo != 'professor':
        return redirect('index')
    quizzes = Quiz.objects.filter(criado_por=request.user)
    tentativas = TentativaQuiz.objects.filter(quiz__in=quizzes)

    # Alunos ativos
    alunos_ativos = tentativas.values_list('aluno', flat=True).distinct().count()
    # Quizzes completados
    quizzes_completados = tentativas.count()
    # Média geral
    media_geral = 0
    if quizzes_completados > 0:
        media_geral = int(sum(t.acertos / t.total for t in tentativas) / quizzes_completados * 100)

    # Desempenho dos alunos por matéria
    desempenho = {}
    for tentativa in tentativas:
        aluno = tentativa.aluno.username
        materia = tentativa.quiz.disciplina.nome
        percentual = tentativa.percentual()
        if aluno not in desempenho:
            desempenho[aluno] = {}
        if materia not in desempenho[aluno]:
            desempenho[aluno][materia] = []
        desempenho[aluno][materia].append(percentual)
    # Calcular média por aluno/matéria
    for aluno in desempenho:
        for materia in desempenho[aluno]:
            notas = desempenho[aluno][materia]
            desempenho[aluno][materia] = int(sum(notas) / len(notas))

    # Descobrir todas as matérias dos quizzes do professor
    materias = list(quizzes.values_list('disciplina__nome', flat=True).distinct())

    return render(request, 'principal/painel_professor.html', {
        'quizzes': quizzes,
        'alunos_ativos': alunos_ativos,
        'media_geral': media_geral,
        'quizzes_completados': quizzes_completados,
        'desempenho': desempenho,
        'materias': materias,
    })

def login_view(request):
    mensagem = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            mensagem = 'Usuário ou senha inválidos.'
    return render(request, 'principal/login.html', {'mensagem': mensagem})

def logout_view(request):
    logout(request)
    return redirect('index')

# Cadastro de Quiz
@login_required
def criar_quiz(request):
    if not request.user.tipo == 'professor':
        return redirect('index')
    disciplinas = Disciplina.objects.all()
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        disciplina_id = request.POST.get('disciplina')
        disciplina = get_object_or_404(Disciplina, id=disciplina_id)
        quiz = Quiz.objects.create(titulo=titulo, descricao=descricao, disciplina=disciplina, criado_por=request.user)
        messages.success(request, 'Quiz criado com sucesso!')
        return redirect('painel_professor')
    return render(request, 'principal/criar_quiz.html', {'disciplinas': disciplinas})

# Cadastro de Pergunta
@login_required
def criar_pergunta(request, quiz_id):
    if not request.user.tipo == 'professor':
        return redirect('index')
    quiz = get_object_or_404(Quiz, id=quiz_id, criado_por=request.user)
    if request.method == 'POST':
        texto = request.POST.get('texto')
        pergunta = Pergunta.objects.create(quiz=quiz, texto=texto)
        messages.success(request, 'Pergunta criada! Agora adicione as respostas.')
        return redirect('criar_resposta', pergunta_id=pergunta.id)
    return render(request, 'principal/criar_pergunta.html', {'quiz': quiz})

# Cadastro de Resposta
@login_required
def criar_resposta(request, pergunta_id):
    if not request.user.tipo == 'professor':
        return redirect('index')
    pergunta = get_object_or_404(Pergunta, id=pergunta_id, quiz__criado_por=request.user)
    if request.method == 'POST':
        texto = request.POST.get('texto')
        correta = bool(request.POST.get('correta'))
        Resposta.objects.create(pergunta=pergunta, texto=texto, correta=correta)
        if 'adicionar_outra' in request.POST:
            return redirect('criar_resposta', pergunta_id=pergunta.id)
        else:
            return redirect('painel_professor')
    return render(request, 'principal/criar_resposta.html', {'pergunta': pergunta})

# Listagem de quizzes para alunos
@login_required
def quizzes_aluno(request):
    quizzes = Quiz.objects.all()
    return render(request, 'principal/quizzes_aluno.html', {'quizzes': quizzes})

@login_required
def jogar_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    perguntas = list(quiz.perguntas.all())
    total = len(perguntas)
    if total == 0:
        return render(request, 'principal/jogar_quiz.html', {'quiz': quiz, 'mensagem': 'Este quiz ainda não possui perguntas.'})

    # Controle de progresso do quiz na sessão
    if 'quiz_progress' not in request.session or request.session.get('quiz_id') != quiz_id:
        request.session['quiz_progress'] = 0
        request.session['quiz_acertos'] = 0
        request.session['quiz_id'] = quiz_id

    progresso = request.session['quiz_progress']
    acertos = request.session['quiz_acertos']

    if progresso >= total:
        pontuacao = int((acertos / total) * 100)
        # Salva tentativa
        TentativaQuiz.objects.create(
            aluno=request.user,
            quiz=quiz,
            acertos=acertos,
            total=total
        )
        # Limpa progresso ao finalizar
        del request.session['quiz_progress']
        del request.session['quiz_acertos']
        del request.session['quiz_id']
        return render(request, 'principal/jogar_quiz.html', {
            'quiz': quiz,
            'finalizado': True,
            'pontuacao': pontuacao,
            'total': total,
            'acertos': acertos
        })

    pergunta = perguntas[progresso]
    respostas = list(pergunta.respostas.all())
    feedback = None

    if request.method == 'POST':
        resposta_id = int(request.POST.get('resposta'))
        resposta = get_object_or_404(Resposta, id=resposta_id)
        if resposta.correta:
            acertos += 1
            request.session['quiz_acertos'] = acertos
            feedback = 'Correto!'
        else:
            feedback = 'Incorreto!'
        request.session['quiz_progress'] = progresso + 1
        # Redireciona para evitar reenvio do formulário
        return HttpResponseRedirect(reverse('jogar_quiz', args=[quiz_id]))

    return render(request, 'principal/jogar_quiz.html', {
        'quiz': quiz,
        'pergunta': pergunta,
        'respostas': respostas,
        'progresso': progresso + 1,
        'total': total,
        'feedback': feedback
    })

@login_required
def desempenho_quiz(request, quiz_id):
    if not request.user.tipo == 'professor':
        return redirect('index')
    quiz = get_object_or_404(Quiz, id=quiz_id, criado_por=request.user)
    tentativas = quiz.tentativas.select_related('aluno').order_by('-data')
    return render(request, 'principal/desempenho_quiz.html', {'quiz': quiz, 'tentativas': tentativas})

