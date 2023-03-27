from django.shortcuts import render
from AppRodriguezFinal.models import Receta
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

def index(request):
    return render(request, "AppRodriguezFinal/index.html")

def loging(request):
    return render(request, "AppRodriguezFinal/loging.html")


def receta_list(request):
    return render(request, "AppRodriguezFinal/receta_list.html")

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
    success_url = reverse_lazy("receta_list")

class RecetaCreate(CreateView):
    model = Receta
    success_url = reverse_lazy("receta_list")
    fields = '__all__'

class RecetaSearch(ListView):
    model = Receta
    context_object_name = "recetas"
    def get_queryset(self):
        criterio = self.request.GET.get("criterio")
        result = Receta.objects.filter(Nombre_de_receta__icontains=criterio).all()
        return result