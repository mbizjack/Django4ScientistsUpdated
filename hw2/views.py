from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponse

from .models import InputForm
from .compute import compute

def index(request):
    s = None # initial value of result
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            r = form.r
            s = compute(r)
    else:
        form = InputForm()

    return render(request,'hw2.html',
            {'form': form,
            's': '%.5f' % s if isinstance(s, float) else ''},
            )

def present_output(form):
    r = form.r
    s = compute(r)
    return HttpResponse('Hello, World! sin(%s)=%s' % (r, s))