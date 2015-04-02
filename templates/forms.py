from django import forms
from .models import Template
from .models import Answer
from .models import Question

class TemplateForm(forms.ModelForm):
    class Meta:
        model = Template
        exclude =  ('user',)
        widgets={
            "name":forms.TextInput(attrs={'class':'form-control', 'placeholder':'User Survay', 'autocomplete':'off'}),
            "description":forms.TextInput(attrs={'class':'form-control', 'placeholder':'This is a form to test the user satisfaction', 'autocomplete':'off'}),
        }

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        exclude =  ('template',)
        widgets={
            "question":forms.TextInput(attrs={'class':'form-control', 'placeholder':'What do you think of the site'}),
            'type':forms.Select(attrs={'class':'form-control', 'placeholder':'Please select the type of question you would like'})
        }


class AnsweForm(forms.ModelForm):
    class Meta:
        model = Answer