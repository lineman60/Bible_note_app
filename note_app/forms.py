__author__ = 'Beryl'
from django import forms
from note_app.models import Anote


class NoteForm(forms.ModelForm):
        book = forms.CharField(max_length=60, help_text="Book")
        chapter = forms.IntegerField(help_text="Chapter")
        verse = forms.IntegerField(help_text="Verse")
        note_text = forms.CharField(widget=forms.Textarea, max_length=400, help_text="Note")
        note_source = forms.CharField(max_length=60, help_text="Source", required=False)
        is_public = forms.BooleanField(help_text="Make the Note Public", required=False)
        # contributor = forms.CharField(max_length=128, help_text="User Name")
        # contributor = forms.CharField(max_length=128,)
        contributor = forms.CharField(widget=forms.HiddenInput(),)

        class Meta:
            model = Anote
            # exclude = ('contributor',)
