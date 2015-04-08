# coding: utf-8
from django import forms
from eventex.subscriptions.models import Subscription


class SubscriptionForm(forms.ModelForm):
    class Meta:
        fields = ('name', 'cpf', 'email', 'phone')
        model = Subscription