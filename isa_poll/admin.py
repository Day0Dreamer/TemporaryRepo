from django.contrib import admin
from .models import Question, Answer, Topic, TopicGroup, Questioner, QuestionerResult

# Register your models here.

admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Topic)
admin.site.register(TopicGroup)
admin.site.register(Questioner)
admin.site.register(QuestionerResult)
