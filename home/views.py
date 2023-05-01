from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm

from django.shortcuts import redirect

class signupInterface(CreateView):
    form_class = UserCreationForm
    template_name = 'home/signup.html'
    success_url = 'smart/notes'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('notes.list')
        return super().get(request, *args, **kwargs)
        
class loginInterfaceView(LoginView):
    template_name = 'home/login.html'

class logoutView(LogoutView):
    template_name = 'home/logout.html'

class HomeView(TemplateView):
    template_name = 'home/welcome.html'
    extra_context = {'today' : datetime.today()}

# Create your views here.
# def home(request):
#     # return HttpResponse("Hello, world!!")
#     return render(request, 'home/welcome.html', {'today' : datetime.today()})

class AuthorizedView(LoginRequiredMixin,TemplateView):
    template_name = 'home/authorization.html'
    login_url = '/admin'

# @login_required(login_url='/admin')
# def authorization(request):
#     return render(request, 'home/authorization.html', {})

class testView(TemplateView):
    template_name = "home/test.html"

# def test(request):
#     return render(request, "home/test.html", {})