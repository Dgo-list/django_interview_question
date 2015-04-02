from django.db import models
from django.contrib.auth.models import User

# Model to define Templates table
class Template(models.Model):
    name = models.CharField(max_length=120)
    description = models.CharField(max_length=1024)
    user = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.name


# Model to define Questions table
class Question(models.Model):
    question = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)

    types_choice = (
        ('0', 'boolean'),
        ('1', 'int')
    )
    type = models.CharField(max_length=1, choices=types_choice)
    template = models.ForeignKey(Template)

    def __str__(self):
        return self.question

    def answers(self):
        return Answer.objects.filter(question=self.id)

# Model to define Answers table
class Answer(models.Model):
    answer = models.CharField(max_length=520)
    question = models.ForeignKey(Question)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.answer

    @classmethod
    def create(cls, answer, question):
        book = cls(answer=answer, question=question)
        # do something with the book
        return book