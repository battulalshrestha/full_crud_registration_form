#from django.template import loader
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Question,Question_choice
from django.shortcuts import render,get_object_or_404
from django.urls import reverse
# Create your views here.
from django.http import HttpResponse
def index(request):
    questions = Question.objects.all()
    return render(request,'index.html',{'questions':questions,'title':'Question'})

def detail(request,question_id):
    question = Question.objects.get(pk = question_id)
    data = {'question':question}
    return render(request,'detail.html',data)

def Votes(request,question_id):
    question = get_object_or_404(Question,pk = question_id)
    try:
        selected_choice = question.choice_set.get(pk = request.POST['choice'])
    except (KeyError,Question_choice.DoesNotExist):
       #pass
       return render(request,'detail.html',{
           'question':question,
           'error_message':"you are not able to choice.",
       })
    else:
        # if choice found, update choice with a new vote
        selected_choice.vote += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('poll:result',args= (question_id,)))