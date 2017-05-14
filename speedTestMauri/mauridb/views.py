# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from .models import BadBoy


def homepage(request):
    return render(request, 'mauridb/index.html', {})


def description(request):
    context = {
        'description': 'calc how much time i spend to create a web app with django'
    }
    return render(request, 'mauridb/description.html', context)


def mauri(request):
    m = BadBoy.objects.get(name='mauri')

    if request.method == 'POST' and request.POST.get('upvote', ''):
        m.votes += 1
        # you have to save the change of the model!!!! c'mon!!!!
        m.save()
    elif request.method == 'POST' and request.POST.get('downvote', ''):
        if m.votes > 0:
            m.votes -= 1
            m.save()
    elif request.method == 'POST' and request.POST.get('reset', ''):
        m.votes = 0
        m.save()
    context = {
        'mauridb': {
            'age': m.age,
            'name': m.name,
            'surname': m.surname,
            'job': 'software developer',
            'votes': m.votes,
        }
    }

    return render(request, 'mauridb/mauridetails.html', context)
