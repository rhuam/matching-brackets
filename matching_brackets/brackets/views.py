from django.shortcuts import render, redirect
from brackets.forms import QueryForm
from brackets.processor import Processor

#####
# View: Verifica se a request eh GET ou POST
# Intancia os objetos: query (Informacoes do formulario), proc (Processador para validacao da entrada)
# value (valores de retorno, onde 0- Resultado, 1- Entrada, 2- Comentario sobre a entrada)
#####

def home(request, get = None):
    form = QueryForm(request.POST or None)
    value = "", "", ""
    if (request.method == 'POST'):
        if (form.is_valid()):
            query = form.save(commit=False)
            proc = Processor(query.value)
            value = proc.findErro()
    elif(request.method == 'GET' and not(get == None)):
        if (form.is_valid()):
            query = form.save(commit=False)
            query.value = get
            proc = Processor(query.value)
            value = proc.findErro()
   
    return render(request, 'index.html', {'form':form, 'result':value[0],'value':value[1], 'comment':value[2]})