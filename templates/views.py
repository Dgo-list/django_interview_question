from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response, RequestContext
from .forms import *

# Create your views here.

@login_required(login_url='login')
def createTemplate(request):

    form = TemplateForm(request.POST or None)

    if form.is_valid():
        template = form.save(commit=False)
        template.user = request.user
        template.save()


    return render_to_response("template/create.html",
                              locals(),
                              context_instance=RequestContext(request))

def userIndexTemplate(request):
    templates = Template.objects.filter(user= request.user.id)

    return render_to_response("template/index.html",
                              locals(),
                              context_instance=RequestContext(request))

def viewTemplate(request, template_id):

    template = Template.objects.get(id=int(template_id))

    questions = Question.objects.filter(template=template.id)


    return render_to_response("template/views.html",
                              locals(),
                              context_instance=RequestContext(request))

def createQuestion(request, template_id):

    form = QuestionForm(request.POST or None)

    question = None;
    if form.is_valid():
        if request.POST['type'] == 0:
            question = form.save(commit=False)
            question.template = Template.objects.get(id=int(template_id))
            question.save()
            return HttpResponseRedirect('/templates/index/')
        else:
            question = form.save(commit=False)
            question.template = Template.objects.get(id=int(template_id))
            question.save()
            for answer in request.POST.getlist('answers[]'):
                newAnswer = Answer.create(answer, question)
                newAnswer.save()

            return HttpResponseRedirect('/templates/index/')

    return render_to_response("question/create.html",
                              locals(),
                              context_instance=RequestContext(request))