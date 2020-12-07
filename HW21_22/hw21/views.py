from django.shortcuts import render, redirect
from django.http import HttpResponse

from hw21.forms import PersonForm
from hw21.models import Person


# Create your views here.
def hw21_home_page(request):
    context = {'person':Person.objects.all()}
    return render(request, 'hw21_home_page.html', context = context)


def add_person(request):
    if request.method == 'GET':
        context = {'person_form': PersonForm}
        return render(request, 'add_person.html', context=context)
    elif request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('hw21_home_page')
