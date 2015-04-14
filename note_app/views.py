from django.shortcuts import render
from django.http import HttpResponse
from note_app.forms import NoteForm

def index(request):
    return HttpResponse("Hold page for Index")

def add_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print form.errors
    else:
        form = NoteForm()

    return  render(request, 'add_note.html', {'form': form})



# Create your views here.
