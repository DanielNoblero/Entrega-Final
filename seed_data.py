from AppRodriguezFinal.models import Receta

for _ in range(0,5):
    Receta(Nombre_de_reseta ="Nombre de reseta", 
    Autor="Autor",
    Rendimiento="Rendimiento",
    Horas_de_prepracion="Horas de prepracion",
    Direccion= "Direccion",
    ).save()