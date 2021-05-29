from django import forms

class BidAomount(forms.Form):
    price = forms.IntegerField()