from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView

from app.models import Note


class NotesView(ListView):
    model = Note
    template_name = 'app/notes_index.html'


class CreateNoteView(CreateView):
    pass


class UpdateNoteView(UpdateView):
    pass
