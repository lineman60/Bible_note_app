__author__ = 'Beryl'
from django import forms
from note_app.models import Anote, BookName


class NoteForm(forms.ModelForm):
        book = forms.ChoiceField(BookName.books_of_the_bible_choices,help_text="Book")
        chapter = forms.IntegerField(help_text="Chapter")
        verse = forms.IntegerField(help_text="Verse", required=False)
        note_text = forms.CharField(widget=forms.Textarea, max_length=400, help_text="Note")
        note_source = forms.CharField(max_length=60, help_text="Source", required=False)
        is_public = forms.BooleanField(help_text="Make the Note Public", required=False)
        contributor = forms.CharField(widget=forms.HiddenInput(),)

        class Meta:
            model = Anote
