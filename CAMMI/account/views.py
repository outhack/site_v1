from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

#Constants
nav_links = ["CONSUMER"]

# Create your views here.
@login_required(login_url='/login/')
def accountSettings(request, account_id):
    if str(request.user.id) == account_id:
        return render(request, 'account/settings.html',{
            'username':request.user.username,
            'message':"accountSettings",
            'valid_user': request.user.id
        })
    else:
        return redirect("/" + str(request.user.id))

@login_required(login_url='/login/')
def accountHome(request, account_id):
    if str(request.user.id) == account_id:
        return renderHomePage(request)
    else:
        return pageNotFound(request)


def renderHomePage(request):
    return render(request, 'account/account_home.html',{
        # 'user':user,
        'username':request.user.username,
        # 'page': 'consumer app homepage',
        # 'message':"consumerHome",
        # 'account_id':account_id,
        'title':"Account Homepage",
    })

def pageNotFound(request):
    return render(request, 'security/page_not_found.html',{
        # 'user':user,
        'username':request.user.username,
        # 'page': 'consumer app homepage',
        # 'message':"consumerHome",
        'title':"Account Homepage",
    })
