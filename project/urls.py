from django.contrib import admin
from django.urls import path
from AppRodriguezFinal.views import (index, RecetaList, RecetaDetail, RecetaUpdate, RecetaDelete, RecetaCreate,
RecetaSearch, Login, SignUp, Logout, RecetaMineList, ProfileCreate, ProfileUpdate, MensajeList, MensajeCreate, MensajeDelete )

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name= "index"),
    path('receta/list', RecetaList.as_view(), name="receta_list"),
    path('receta/<pk>/detail', RecetaDetail.as_view(), name="receta_detail"),
    path('receta/<pk>/update', RecetaUpdate.as_view(), name="receta_update"),
    path('receta/<pk>/delete', RecetaDelete.as_view(), name="receta_delete"),
    path('receta/create', RecetaCreate.as_view(), name="receta_create"),
    path('receta/search', RecetaSearch.as_view(), name="receta_search"),
    path('login/', Login.as_view(), name="login"),
    path('signup/', SignUp.as_view(), name="signup"),
    path('logout/', Logout.as_view(), name="logout"),
    path('receta/list', RecetaMineList.as_view(), name="receta_mine"),
    path('profile', ProfileCreate.as_view(), name="profile_create"),
    path('profile/<pk>/update', ProfileUpdate.as_view(), name="profile-update" ),
    path('mensaje/list', MensajeList.as_view(), name="mensaje-list" ),
    path('mensaje/create', MensajeCreate.as_view(), name="mensaje-create" ),
    path('mensaje/<pk>/delete', MensajeDelete.as_view(), name="mensaje-delete"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)