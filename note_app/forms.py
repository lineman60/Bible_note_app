__author__ = 'Beryl'
from django import forms
from note_app.models import Anote


class NoteForm(forms.ModelForm):
        book = forms.CharField(max_length=60)
        chapter = forms.IntegerField()
        verse = forms.IntegerField()
        note_text = forms.TextField(max_length=400)
        note_source = forms.CharField(max_length=60)
        is_public = forms.BooleanField(default=False)
        contributor = forms.CharField(max_length=128)

        class Meta:
            model = Anote
           # exclude = ('contributor')
