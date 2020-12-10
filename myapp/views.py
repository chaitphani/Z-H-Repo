from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse

# import models
from myapp.models import *

# third party library
import random

# Create your views here.
def dashboard(request):
    template_name = 'myapp/index.html'
    purchase_status_model_obj = PurchaseStatusModel.objects.all()
    
    x_axis_data = ''
    y_axis_data = ''
    random_objs = random.sample(list(purchase_status_model_obj), 10)

    total = 0
    for ran_data in random_objs:
        x_axis_data += str(ran_data.purchase.purchaser_name) + ','
        y_axis_data += str(ran_data.purchase.quantity) + ','
        total += ran_data.purchase.quantity

    print("Average--",total/10)
    status_list = dict(PurchaseStatusModel._meta.get_field('status').choices)
    return render(request, template_name, {'x_axis_data':x_axis_data, 'y_axis_data':y_axis_data, 'status_list':status_list})

def filterbymonth(request):
    if request.method == "POST":
        try:
            datefilter = request.POST['datefilter']
            selected_status = request.POST["selected_status"]
            
            if len(datefilter) > 0 and len(selected_status) > 0:
                splited_date = datefilter.split('-')
                purchase_status_model_obj = PurchaseStatusModel.objects.filter(status=selected_status, created_at__year=splited_date[1], created_at__month=splited_date[0])
            else:
                if len(datefilter) > 0:
                    splited_date = datefilter.split('-')
                    purchase_status_model_obj = PurchaseStatusModel.objects.filter(created_at__year=splited_date[1], created_at__month=splited_date[0])
                else:
                    purchase_status_model_obj = PurchaseStatusModel.objects.filter(status=selected_status)

            x_axis_data = ''
            y_axis_data = ''
            random_objs = random.sample(list(purchase_status_model_obj), 10)

            total = 0
            for ran_data in random_objs:
                x_axis_data += str(ran_data.purchase.purchaser_name) + ','
                y_axis_data += str(ran_data.purchase.quantity) + ','
                total += ran_data.purchase.quantity
            print("Average--",total/10)
            return JsonResponse({'x_axis_data':x_axis_data, 'y_axis_data':y_axis_data})
        except:
            return redirect('/')
