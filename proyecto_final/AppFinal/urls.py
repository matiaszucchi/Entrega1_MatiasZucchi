from django.urls import path
from AppFinal.views import *

urlpatterns = [

    path('', inicio, name='AppFinalInicio'),
    path('monotribustista/', monotributista, name='AppFinalMonotributista'),
    path('responsableinscripto/', responsable_inscripto, name='AppFinalResponsable'),
    path('impuesto/', impuestos, name='AppFinalImpuesto'),
    path('formulario/', formulario, name='AppFinalFormulario'),
    path('busqueda_nombre/', busqueda_nombre, name='AppFinalBusquedaNombre'),
    path('busqueda_nombre_post/', busqueda_nombre_post, name='AppFinalBusquedaNombrePost'),
    
]