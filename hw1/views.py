from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponse

from .models import InputForm
from .compute import compute

def index(request):
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            return present_output(form)
    else:
        form = InputForm()

    return render(request,'hw1.html',{'form': form})

def present_output(form):
    r = form.r
    s = compute(r)
    return HttpResponse('Hello, World! sin(%s)=%s' % (r, s))