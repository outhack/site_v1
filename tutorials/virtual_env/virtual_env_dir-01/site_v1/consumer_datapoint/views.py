# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404, render, redirect
from django.forms import modelformset_factory
from django.http import HttpResponse
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Account, UserAccount, DataPoint
from django.forms import ModelForm
from .forms import DataPointForm


@login_required
def consumer_datapoint(request):
    return render(request, 'consumer_datapoint/consumer_datapoint.html',{
        'username':request.user.username,
        'logo': 'logo',
        'page':consumer_datapoint.__name__,
        'app_links':["datapoint", "datapoint_group", "profile"],
        'login':"logout",
    })

@login_required
def datapoints(request):
    datapoint_list = DataPoint.objects.all()
    return render(request, 'consumer_datapoint/datapoints.html',{
        'username':request.user.username,
        'logo': 'logo',
        'page':datapoints.__name__,
        'app_links':["create"],
        # 'app_link_urls':["create_form","delete_action"],
        'login':"logout",
        'datapoint_list':datapoint_list,
    })

@login_required
def datapoint(request, dppk):
    datapnt = DataPoint.objects.get(pk=dppk)
    if(request.method == 'POST'):
        form = DataPointForm(request.POST, instance=datapnt)
        if(form.is_valid()):
            form.save()
            return redirect("/consumer_datapoint/datapoint")
    else:
        form = DataPointForm(instance=datapnt)
        return render(request,'consumer_datapoint/datapoint.html',{'form':form})

@login_required
def create_datapoint(request):
    if request.method == 'POST':
        form = DataPointForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/consumer_datapoint/datapoint")
    form = DataPointForm()
    return render(request, 'consumer_datapoint/create_datapoint.html', {
        'username':request.user.username,
        'logo': 'logo',
        'page':create_datapoint.__name__,
        'app_links':[],
        'login':"logout",
        'form':form,
    })

@login_required
def delete_datapoint(request,dppk):
    DataPoint.objects.filter(pk=dppk).delete()
    return redirect("/consumer_datapoint/datapoint/")

###########

@login_required
def datapoint_group(request):
    return render(request, 'consumer_datapoint/datapoint_group.html',{
        'username':request.user.username,
        'logo': 'logo',
        'page':datapoint_group.__name__,
        'app_links':["datapoint", "datapoint_group", "profile"],
        'login':"logout",
    })

@login_required
def profile(request):
    return render(request, 'consumer_datapoint/profile.html',{
        'username':request.user.username,
        'logo': 'logo',
        'page':profile.__name__,
        'app_links':["datapoint", "datapoint_group", "profile"],
        'login':"logout",
    })


# from django.http import HttpResponseRedirect
# from django.urls import reverse
# from django.contrib.auth.mixins import LoginRequiredMixin

# class ConsumerDataPointView(LoginRequiredMixin,generic.DetailView):
#     login_url = '/account/login/'
#     model = User
    # accountModel = Account
    # user_account = UserAccount
    # template_name = 'consumer_datapoint/consumer_datapoint.html'

    # context_object_name = 'username'

    # def get_context_data(self):
    #     return self.request.user
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
        # context['now'] = datetime.now()
        # return context
    #Do you have an account? No: Redirect to unknown_account page, Yes: Continue
    #Is the account active? No: Redirect to inactive_account page, Yes: Display user data on page

# class LoginView(generic.TemplateView):
#     template_name = 'consumer_datapoint/login.html'
#
# class UserAccountLandingView(generic.TemplateView):
#     template_name = 'consumer_datapoint/user_account.html'
#
# class DataPointsView(generic.TemplateView):
#     template_name = 'consumer_datapoint/datapoints.html'
#
# class DataPointView(generic.TemplateView):
#     template_name = 'consumer_datapoint/datapoint.html'
#
# class CreateDataPointView(generic.TemplateView):
#     template_name = 'consumer_datapoint/datapoints.html'
#
# class DataPointGroupsView(generic.TemplateView):
#     template_name = 'consumer_datapoint/datapoint_groups.html'
#
# class DataPointGroupView(generic.TemplateView):
#     template_name = 'consumer_datapoint/datapoint_group.html'
#
# class CreateDataPointGroupView(generic.TemplateView):
#     template_name = 'consumer_datapoint/datapoint_groups.html'
#
# class ProfilesView(generic.TemplateView):
#     template_name = 'consumer_datapoint/profiles.html'
#
# class ProfileView(generic.TemplateView):
#     template_name = 'consumer_datapoint/profile.html'
#
# class CreateProfileView(generic.TemplateView):
#     template_name = 'consumer_datapoint/profiles.html'



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
