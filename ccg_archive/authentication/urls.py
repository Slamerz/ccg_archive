from django.urls import path
from ccg_archive.authentication import views

urlpatterns = [
    path('login/', views.LoginUserView.as_view(), name='login'),
    path('logout/', views.LogoutUserView.as_view(), name='logout'),
    path('register/', views.RegisterUserView.as_view(), name='registeruser'),
    path('edituser/', views.UserEditView.as_view(), name='edituser')
]
