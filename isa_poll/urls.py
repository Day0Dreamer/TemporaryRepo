from django.urls import path, re_path
from django.views.generic import TemplateView
from . import views

app_name = "isa_poll"
urlpatterns = [
    path("", views.PollSelector.as_view(template_name="isa_poll/poll_selector.html"), name="poll selector"),
    path("result/<poll_result_id>/", views.PollComplete.as_view(template_name="isa_poll/poll_complete.html"), name="poll complete"),
]
