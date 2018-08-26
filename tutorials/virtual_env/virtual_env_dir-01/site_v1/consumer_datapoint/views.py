# -*- coding: utf-8 -*-
# from __future__ import unicode_literals
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

# from .models import Choice, Question



class IndexView(generic.TemplateView):
    template_name = 'consumer_datapoint/index.html'

class LoginView(generic.TemplateView):
    template_name = 'consumer_datapoint/login.html'

class UserAccountLandingView(generic.TemplateView):
    template_name = 'consumer_datapoint/user_account.html'

class DataPointsView(generic.TemplateView):
    template_name = 'consumer_datapoint/datapoints.html'

class DataPointView(generic.TemplateView):
    template_name = 'consumer_datapoint/datapoint.html'

class CreateDataPointView(generic.TemplateView):
    template_name = 'consumer_datapoint/datapoints.html'

class DataPointGroupsView(generic.TemplateView):
    template_name = 'consumer_datapoint/datapoint_groups.html'

class DataPointGroupView(generic.TemplateView):
    template_name = 'consumer_datapoint/datapoint_group.html'

class CreateDataPointGroupView(generic.TemplateView):
    template_name = 'consumer_datapoint/datapoint_groups.html'

class ProfilesView(generic.TemplateView):
    template_name = 'consumer_datapoint/profiles.html'

class ProfileView(generic.TemplateView):
    template_name = 'consumer_datapoint/profile.html'

class CreateProfileView(generic.TemplateView):
    template_name = 'consumer_datapoint/profiles.html'



# class IndexView(generic.ListView):
#     template_name = 'polls/index.html'
#     context_object_name = 'latest_question_list'
#
#     def get_queryset(self):
#         """Return the last five published questions."""
#         return Question.objects.order_by('-pub_date')[:5]
#
#
# class DetailView(generic.DetailView):
#     model = Question
#     template_name = 'polls/detail.html'
#
#
# class ResultsView(generic.DetailView):
#     model = Question
#     template_name = 'polls/results.html'
#
#
# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(request, 'polls/detail.html', {
#             'question': question,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
