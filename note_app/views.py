from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from note_app.models import Anote
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
        #if not add
        form = NoteForm()
    return  render(request, 'add_note.html', {'form': form})

@login_required
def edit_note(request, id=None):
    temp_note = get_object_or_404(Anote,pk=id)
    if id:
    # if request.method == 'POST':
        #if Anote.contributor != request.user:
        if temp_note.contributor != request.user:
            print(request.user)
            print(temp_note.contributor)
            return HttpResponseForbidden()
        else:
             form = NoteForm(instance=temp_note)
             if form.is_valid():
                form.save(commit=True)
             else:
                print form.errors
        return render(request, 'edit_note.html', {'form': form})





