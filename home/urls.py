from django.urls import path

from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name='home'),
    # path("auth", views.AuthorizedView.as_view()),
    # path("test", views.testView.as_view()),
    path("login", views.loginInterfaceView.as_view(), name='login'),
    path("logout", views.logoutView.as_view(), name='logout'),
    path("signup", views.signupInterface.as_view(), name='signup'),
]