from django.shortcuts import render
from django.http import HttpResponse, HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from note_app.models import Anote
from note_app.forms import NoteForm
from django.db.models import Q


def index(request):
    note_list = Anote.objects.filter(contributor__exact=request.user.username)
    pub_note_list = Anote.objects.filter(~Q(contributor__exact=request.user.username) & Q(is_public__exact=True))
    note_dict = {'your_notes': note_list,'pub_true':pub_note_list}
    return render(request,'main.html', note_dict)




@login_required
def add_note(request):
    # posting data (push filed in form to server)
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print form.errors
    else:
        # if not posting the form show the blank form
        form = NoteForm()
        # sets hidden field to user
        form.fields["contributor"].initial = request.user
    return render(request, 'add_note.html', {'form': form})


@login_required
def edit_note(request, id=None):
    temp_note = Anote.objects.get(pk=id)
    if id:
        if temp_note.contributor != request.user.username:
            return HttpResponseForbidden()
        else:
             form = NoteForm(instance=temp_note)
             if form.is_valid():
                form.save(commit=True)
             else:
                print form.errors
        return render(request, 'edit_note.html', {'form': form})
