from django.contrib import admin
from django.urls import path
from AppRodriguezFinal.views import index, loging, RecetaList, RecetaDetail, RecetaUpdate, RecetaDelete, RecetaCreate, RecetaSearch

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index, name= "index"),
    path("loging/", loging, name= "loging"),
    path("receta/list", RecetaList.as_view(), name="receta_list"),
    path('receta/<pk>/detail', RecetaDetail.as_view(), name="receta_detail"),
    path('receta/<pk>/update', RecetaUpdate.as_view(), name="receta_update"),
    path('receta/<pk>/delete', RecetaDelete.as_view(), name="receta_delete"),
    path('receta/create', RecetaCreate.as_view(), name="receta_create"),
    path('receta/search', RecetaSearch.as_view(), name="receta_search"),
]
