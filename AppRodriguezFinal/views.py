from django.shortcuts import render
from AppRodriguezFinal.models import Receta
from AppRodriguezFinal.forms import RecetaForm
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


def index(request):
    return render(request, "AppRodriguezFinal/index.html")

class RecetaList(ListView):
    model = Receta
    context_object_name = "recetas"

class RecetaMineList(RecetaList):
    
    def get_queryset(self):
        return Receta.objects.filter(publisher=self.request.user.id)

class RecetaDetail(DetailView):
    model = Receta
    context_object_name = "receta"

class RecetaUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Receta
    success_url = reverse_lazy("receta_list")
    fields = '__all__'

    def test_func(self):
        user_id = self.request.user.id
        post_id = self.kwargs.get("pk")
        return Receta.objects.filter(publisher=user_id, id=post_id).exists()

class RecetaDelete(LoginRequiredMixin, DeleteView):
    model = Receta
    context_object_name = "receta"
    success_url = reverse_lazy("receta_list")

    def test_func(self):
        user_id = self.request.user.id
        post_id = self.kwargs.get("pk")
        return Receta.objects.filter(publisher=user_id,id=post_id).exists()

class RecetaCreate(LoginRequiredMixin, CreateView):
    model = Receta
    success_url = reverse_lazy("receta_list")
    fields = '__all__'

    def form_valid(self, form):
        form.instance.publisher = self.request.user
        return super().form_valid(form)

class RecetaSearch(ListView):
    model = Receta
    context_object_name = "recetas"

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
    template_name = "registration/logout.html"


class SignUp(CreateView):
    form_class = UserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy('receta_list')
