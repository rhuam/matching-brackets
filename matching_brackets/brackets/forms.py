from django.forms import ModelForm, TextInput
from brackets.models import Query

class QueryForm(ModelForm):
    class Meta:
        model = Query
        fields = ['value']
        widgets = {
            'value': TextInput(attrs={'class': 'form-control form-control-lg m-2',
                'placeholder': '{[()]}', 'style':'letter-spacing:5px;'
            })
        }
    
    def getValue(self):
        return self.value
        
        