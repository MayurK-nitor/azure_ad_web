import json
from cryptography.fernet import Fernet
from django.shortcuts import redirect, render
from django.urls import reverse

#pip install cryptography==41.0.4

encryption_key = b'85m-3ExDEz2wCCNERphWTMVJH29tLn-TEa4DpyDRCWM='
cipher_suite = Fernet(encryption_key)

# Create your views here.
def index(request):
    if 'identity_context_data' in request.GET: 
        identity_context_data = request.GET.get('identity_context_data')

        # Decrypt the parameter
        identity_context_data = cipher_suite.decrypt(identity_context_data.encode()).decode()
        request.session['identity_context_data'] = json.loads(identity_context_data)
        get_full_name = request.session['identity_context_data'].get('_username')
    current_url = request.build_absolute_uri()
    context = {'get_full_name': get_full_name, 'current_url': current_url}
    return render(request, 'azure_ad_api/index.html', context)


def login_user(request):
    current_url = request.build_absolute_uri()+'/index'
    request.session['current_url'] = current_url
    return render(request, 'azure_ad_api/login.html', context={'current_url':current_url})

