from django.shortcuts import redirect, render
from django.urls import reverse
import json

# Create your views here.
def index(request):
    print('req_dict', request.__dict__)
    print('req.session', request.session.__dict__)
    if 'identity_context_data' in request.GET: 
        identity_context_data = request.GET.get('identity_context_data')
        request.session['identity_context_data'] = json.loads(identity_context_data)
        get_full_name = request.session['identity_context_data'].get('_username')
        print(request.session['identity_context_data'])
    get_full_name = ''
    # print('r.ude', request.identity_context_data)
    current_url = request.build_absolute_uri()
    # identity_context_data = request.session['identity_context_data']
    context = {'get_full_name': get_full_name, 'current_url': current_url}
    return render(request, 'azure_ad_api/index.html', context)


def login_user(request):
    current_url = request.build_absolute_uri()+'/index'
    context = {'get_full_name': 'get_full_name', 'current_url': current_url}
    return render(request, 'azure_ad_api/login.html', context)
