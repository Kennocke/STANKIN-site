from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse
from .models import Records
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from django.http import JsonResponse
import json

def home(request):
    """Renders the home page."""
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def reg(request):
    return render(request, 'app/reg_page.html')

@csrf_exempt
def diary(request):
    records = Records.objects.all()
    current_date = datetime.now().strftime('%Y-%m-%d')
    if request.method == "POST":
        if request.POST.get("click")=="true":
            response_data = {}
            one_record = Records.objects.get(pk=request.POST.get("id"))
            response_data['created_date'] = one_record.created_date.strftime('%Y-%m-%d')
            response_data['title'] = one_record.title
            response_data['main_text'] = one_record.text
            return JsonResponse(response_data)
        record = Records()
        record.title = request.POST.get("title","")
        record.text = request.POST.get("main_text","")
        record.save()
        return redirect('/diary_page/', {"records": records, "current_date": current_date})
    return render(request, 'app/diary_page.html', {"records": records, "current_date": current_date})
