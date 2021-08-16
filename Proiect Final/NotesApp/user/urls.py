from django.urls import path
from user import views

app_name = 'user'

urlpatterns = [
    path('update_profile/<int:pk>', views.UpdateProfileView.as_view(), name='update_profile'),
    path('new_account/', views.CreateNewAccount.as_view(), name='new_account'),
]