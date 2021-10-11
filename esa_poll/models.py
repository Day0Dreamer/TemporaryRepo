from django.db import models
from django.db.models import Model, FileField, ManyToManyField
from ckeditor.fields import RichTextField



# Create your models here.
class Question(Model):
    rich_text = RichTextField()

    def __str__(self):
        return str(self.rich_text)

class Answer(Model):
    question = models.ForeignKey(Question, on_delete=models.PROTECT)
    plain_text = models.CharField("Text", max_length=2048, null=True, blank=True)
    rich_text = RichTextField(null=True, blank=True)
    media_file = FileField(null=True, blank=True)

    def __str__(self):
        return self.plain_text or self.rich_text or ''

class TopicGroup(Model):
    name = models.CharField("Text", max_length=128)

    def __str__(self):
        return self.name

class Topic(Model):
    topic_group = models.ForeignKey(TopicGroup, on_delete=models.PROTECT, null=True, blank=True)
    name = models.CharField("Text", max_length=128)
    question_list = models.ManyToManyField(
        Question, blank=True, default=None
    )

    def __str__(self):
        return self.name
