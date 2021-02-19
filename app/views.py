from django.shortcuts import render,redirect
from app.models import UserModel
from django.contrib import messages
import json
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')


def save_details(request):
    na = request.POST.get('r1')
    add = request.POST.get('r2')
    st = request.POST.get('r3')
    et = request.POST.get('r4')
    UserModel(name=na,address=add,start_time=st,end_time=et).save()
    messages.success(request,'Data Added Successfully')
    return redirect('main')


def viewall(request):
    data =UserModel.objects.all()
    dict_data = {}
    for x in data:
        d = {
            x.idno : {
                'name':x.name,
                'address':x.address,
                'start_time':x.start_time.strftime('%B %d %Y %H:%M%p '),
                'end_time':x.end_time.strftime('%B %d %y %H:%M%p')
            }
        }
        dict_data.update(d)
    json_data = json.dumps(dict_data)
    return HttpResponse(json_data,content_type='application/json')