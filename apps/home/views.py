# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render

from .forms import QuestionnaireForm

from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/home.html')
    return HttpResponse(html_template.render(context, request))

def about_depression(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/about-depression.html')
    return HttpResponse(html_template.render(context, request))

def assessment(request):
    form = QuestionnaireForm()
    context = {
        'form': form 
    }

    html_template = loader.get_template('home/assessment.html')
    return HttpResponse(html_template.render(context, request))

def analyze(request):
    if request.method == 'POST':
        message = request.POST["message"]
        message = message.strip()

        tokenizer = AutoTokenizer.from_pretrained("ShreyaR/finetuned-roberta-depression")
        model = AutoModelForSequenceClassification.from_pretrained("ShreyaR/finetuned-roberta-depression")
        inputs = tokenizer(message, padding=True, truncation=True, return_tensors="pt")
        labels = torch.tensor([1]).unsqueeze(0)  # Batch size 1
        outputs = model(**inputs, labels=labels)
        logits = outputs.logits
        results = torch.softmax(logits, dim=1).tolist()[0]

        nondep = int(round(results[0]*100))
        dep = int(round(results[1]*100))
        
        dict = {
            'message': message,
            'nondep': nondep,
            'dep' : dep
        }
        return render(request, 'home/assessment.html', dict)
    else:
        return render(request, 'home/assessment.html')

def questionnaire(request):
    if request.method == 'POST':
        form = QuestionnaireForm(request.POST)
    else:
        form = QuestionnaireForm()

    return render(request, 'home/assessment.html', {'form':form})  

def help(request):
    context = {'segment': 'help'}

    html_template = loader.get_template('home/help.html')
    return HttpResponse(html_template.render(context,request))

def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
