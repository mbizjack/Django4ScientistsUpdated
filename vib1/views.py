from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponse

from .models import InputForm
from .compute import compute

import os

def index(request):
    os.chdir(os.path.dirname(__file__))
    result = None
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            form2 = form.save(commit=False)
            result = compute(form2.A, form2.b, form2.w, form2.T)
            result = result[7:] # remove static from filename, original code below doesn't work
            #result = result.replace('static/', '')
    else:
        form = InputForm()

    return render(request,'vib1.html',
            {'form': form,
             'result': result,
             })