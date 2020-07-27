from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import Question


def index(request):
    latests = Question.objects.order_by('-pub_date')[:5]
    return render(request, 'polls/index.html', {'latests': latests})


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    response = 'Estas viendo los resultados de la pregunta %s'
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse('Estas viedo los votos para la pregunta %s' % question_id)
