from django.contrib import admin

# Register your models here.
from .models import Template
from .models import Question
from .models import Answer



class TemplateAdmin(admin.ModelAdmin):
    class Meta:
        model = Template

class QuestionAdmin(admin.ModelAdmin):
    class Meta:
        model = Question

class AnswerAdmin(admin.ModelAdmin):
    class Meta:
        model = Answer

admin.site.register(Template, TemplateAdmin)
admin.site.register(Question, TemplateAdmin)
admin.site.register(Answer, TemplateAdmin)