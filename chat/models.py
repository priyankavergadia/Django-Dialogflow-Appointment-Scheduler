# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.



class Statement(models.Model):
    text = models.CharField(max_length=400)

    def __str__(self):
        if len(self.text.strip()) > 60:
            return '{}...'.format(self.text[:57])
        elif len(self.text.strip()) > 0:
            return self.text

        return '<empty>'


class Response(models.Model):
    statement = models.ForeignKey(Statement, on_delete=models.CASCADE)
    response = models.CharField(max_length=400)

    created_at = models.DateTimeField(
        default=timezone.now,
        help_text='The date and time that this statement was created at.'
    )

    created_at = models.DateTimeField(
        default=timezone.now,
        help_text='The date and time that this response was created at.'
    )

    def __str__(self):
        statement = self.statement.text
        response = self.response
        return '{} => {}'.format(
            statement if len(statement) <= 20 else statement[:17] + '...',
            response if len(response) <= 40 else response[:37] + '...'
        )