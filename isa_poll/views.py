from django.db.models import Q
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Questioner, QuestionerResult, Answer, Topic, Question, TopicGroup


class PollSelector(TemplateView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["templates"] = Questioner.objects.all()
        context["template_results"] = QuestionerResult.objects.all()
        return context


class PollComplete(TemplateView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            questioner_result = QuestionerResult.objects.get(id=context['poll_result_id'])
            context['questioner_result'] = questioner_result
        except Exception:
            # TODO Improve this exception
            print('FIX ME NOW')
            return context

        questioner = questioner_result.questioner  # type:Questioner

        result = []

        for topic_group in TopicGroup.objects.all():
            for topic in questioner.topic_list.filter(topic_group=topic_group):
                for question in Question.objects.filter(topic=topic):
                    for answer in Answer.objects.filter(Q(question=question) & Q(questioner_result=questioner_result)):
                        data_row = {'topic_group': topic_group, 'topic': topic, 'question': question, 'answer': answer}
                        result.append(data_row)

        context['answers'] = result

        return context
