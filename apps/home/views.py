# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from urllib import response
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import redirect, render

import json
import requests

from .forms import QuestionnaireForm

from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

API_TOKEN = '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'
headers = {"Authorization": f"Bearer {API_TOKEN}"}
API_URL = "https://api-inference.huggingface.co/models/ShreyaR/finetuned-roberta-depression"

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/senseit.html')
    return HttpResponse(html_template.render(context, request))

def about_depression(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/about-depression.html')
    return HttpResponse(html_template.render(context, request))

def query(payload):
    data = json.dumps(payload)
    response = requests.request("POST", API_URL, headers=headers, data=data)
    return json.loads(response.content.decode("utf-8"))

def assessment(request):
    form = QuestionnaireForm()
    if request.method == 'POST':
        if request.POST.get("message",False):
            message = request.POST.get("message", False)
            message = message.strip()

            #tokenizer = AutoTokenizer.from_pretrained("ShreyaR/finetuned-roberta-depression")
            #model = AutoModelForSequenceClassification.from_pretrained("ShreyaR/finetuned-roberta-depression")
            #inputs = tokenizer(message, padding=True, truncation=True, return_tensors="pt")
            #labels = torch.tensor([1]).unsqueeze(0)  # Batch size 1
            #outputs = model(**inputs, labels=labels)
            #logits = outputs.logits
            #results = torch.softmax(logits, dim=1).tolist()[0]

            #nondep = int(round(results[0]*100))
            #dep = int(round(results[1]*100))

            data = query({"inputs": message}) 
            res1 = data[0][0]['score']*100         
            res2 = data[0][1]['score']*100
            nondep = "{:.2f}".format(res1)
            dep = "{:.2f}".format(res2)
            #dep = data.
            context = {
                'message': message,
                'nondep': nondep,
                'dep' : dep,
                #'res' : res,
                'form': form
            }
            return render(request, 'home/assessment.html', context)
        if is_ajax(request=request) and request.method == "POST":
            f = QuestionnaireForm("request.POST")
            x = range(1, 16)
            sum = 0
            for n in x:
                sum += int(request.POST["field" + str(n)])
        
            msg = str(sum) 
            #print(msg)       
            return HttpResponse(msg)
    else:
        context = {
                'form': form
            }
        #html_template = loader.get_template('home/assessment.html')
        return render(request, 'home/assessment.html', context)

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
