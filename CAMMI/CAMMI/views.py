from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.views import login

def custom_login(request):
    if request.user.is_authenticated():
        return redirect('/' + str(request.user.id)+"/")
    else:
        return render(request, 'registration/login.html',{
            'form.username.label_tag':'<label for=\"id_username\">Username:</label>',
            'form.username':'<input autofocus=\"\" id=\"id_username\" maxlength=\"254\" name=\"username\" type=\"text\" required />',
            'form.password.label_tag':'<label for=\"id_password\">Password:</label>',
            'form.password':'<input id=\"id_password\" name=\"password\" type=\"password\" required />',
        })
