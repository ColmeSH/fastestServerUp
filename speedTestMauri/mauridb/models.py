# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class BadBoy(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    age = models.IntegerField()
    description = models.CharField(max_length=200)
    votes = models.IntegerField()

    def speak_about_random_something(self):
        desc = str(self.description)
        desc.split("")

        list_odd_words = [word for word, index in enumerate(desc) if index % 2 != 0]

        return list_odd_words

    def get_full_name(self):
        return "{} - {}".format(self.name, self.surname)

    def get_age(self):
        return "i am {}years old".format(self.age)
