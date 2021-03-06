from django.forms import ModelForm, TextInput
from brackets.models import Query
from brackets.processor import Processor

#####
# Form: Essa classe define o comportamento do formulario, seus campos e parametros
# o metodo is_valid() verifica se a entrada possui apenas caracteres validos.
#####


class QueryForm(ModelForm):
    class Meta:
        model = Query
        fields = ['value']
        widgets = {
            'value': TextInput(attrs={'class': 'form-control form-control-lg m-2',
                'placeholder': '{[()]}', 'style':'letter-spacing:5px;',  'required': ''
            })
        }
    
    def is_valid(self):
        self.ValidationError = "ERRO: Entrada inv&aacute;lida"

        query = self.save(commit=False)
        proc = Processor(query.value)
        
        for l in proc.value:
            if not (l in "([{)]}"):
                return False
        
        return True
        
        