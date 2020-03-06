from django.shortcuts import render
from django.http import Http404
from poll.models import *

# Create your views here.

def index(request):
    questions = Question.objects.all()
    context = {}
    context['title'] = 'polls'
    context['questions'] = questions
    return render(request, 'polls/index.html',context)

def details(request, id=None):
    context = {}
    try:
        questions = Question.objects.get(id=id)
    except :
        raise Http404
    context['questions'] = questions
    return render(request, 'polls/index.html',context)

def poll(request, id=None):
    if request.method == "GET":
        context = {}
        try:
            questions = Question.objects.get(id=id)
        except :
            raise Http404
        context['questions'] = questions
        return render(request, 'polls/index.html',context)

        return render(request, 'polls/poll.html')