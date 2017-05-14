# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import request
from django.shortcuts import render, get_object_or_404

def homepage():
    return render(request, 'mauridb/index.html', {})

def description():
    context = {
        'description': 'calc how much time i spend to create a web app with django'
    }
    return render(request, 'mauridb/description.html', context)

def mauri():
    context = {
        'mauridb':{
            'age': 75,
            'name': 'Sherlock',
            'surname': 'Holmes',
            'job': 'software developer'
        }
    }
    return render(request, 'mauridb/mauridetails', context)
