from django.shortcuts import render, redirect
from brackets.forms import QueryForm
from brackets.processor import Processor


def home(request, get = None):
    
    form = QueryForm(request.POST or None)
    query = form.save(commit=False)
    value = query.value
    
    if (request.method == 'POST'):
        if (form.is_valid()):
            query = form.save(commit=False)
            proc = Processor(query.value)
            value = proc.findErro()
    elif(request.method == 'GET' and not(get == None)):
        proc = Processor(get)
        value = proc.findErro()

    return render(request, 'index.html', {'form':form, 'result':value[0],'value':value[1], 'comment':value[2]})