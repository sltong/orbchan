from django import forms

from orbs.models import Thread


class ThreadForm(forms.Form):
    subject = forms.CharField(max_length=127)
    text = forms.CharField(widget=forms.Textarea())
    image = forms.ImageField()
    file = forms.FileField(required=False)

    subject.widget.attrs.update({"class": "bg-zinc-800 rounded-full"})
    text.widget.attrs.update({"class": "form-textarea bg-zinc-800 rounded-md", "cols": "24"})
