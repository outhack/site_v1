from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/login/')
def displayAccountSettings(request, account_id):
    if request.user.id == account_id:
        return render(request, 'consumer/index.html',{
            # 'user':user,
            'message':"accountSettings",
            'valid_user': request.user.id
        })
    else:
        return redirect("/" + str(request.user.id))

@login_required(login_url='/login/')
def accountHome(request, account_id):
    if str(request.user.id) == str(account_id):
        return render(request, 'consumer/index.html',{
            # 'user':user,
            'message':"accountHome",
            'valid_user':request.user.id,
            'username': account_id,
            'page':'Account \'' + str(request.user.id) +'\' Home'
        })
    else:
        return render(request, 'consumer/index.html',{
            # 'user':user,
            'message':"accountNotHome",
            'valid_user':request.user.id,
            'page':'Restricted Access',
        })
