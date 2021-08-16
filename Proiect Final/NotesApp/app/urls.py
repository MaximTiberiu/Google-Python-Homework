from django.urls import path
from app import views

app_name = 'app'
urlpatterns = [
    path('', views.NotesView.as_view(), name='home'),
    path('add_note/', views.CreateNoteView.as_view(), name='create_note'),
    path('edit_note/<int:pk>', views.UpdateNoteView.as_view(), name='edit_note'),
]