from django.shortcuts import render
from AppRodriguezFinal.models import Receta
from AppRodriguezFinal.forms import RecetaForm
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm


def index(request):
    return render(request, "AppRodriguezFinal/index.html")

class RecetaList(ListView):
    model = Receta
    context_object_name = "recetas"

class RecetaDetail(DetailView):
    model = Receta
    context_object_name = "receta"

class RecetaUpdate(UpdateView):
    model = Receta
    success_url = reverse_lazy("receta_list")
    fields = '__all__'

class RecetaDelete(DeleteView):
    model = Receta
    context_object_name = "receta"
    success_url = reverse_lazy("receta_list")

class RecetaCreate(CreateView):
    model = Receta
    success_url = reverse_lazy("receta_list")
    fields = '__all__'

class RecetaSearch(ListView):
    model = Receta
    context_object_name = "receta_list"

    def get_queryset(self):
        criterio = self.request.GET.get("criterio")
        result = Receta.objects.filter(Nombre_de_receta__icontains=criterio).all()
        return result

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Resultados"
        return context

class Login(LoginView):
    next_page = reverse_lazy('receta_list')

class Logout(LogoutView):
    next_page = reverse_lazy('index')


class SignUp(CreateView):
    form_class = UserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy('receta_list')
