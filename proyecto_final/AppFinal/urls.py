from django.urls import path
from AppFinal.views import *

urlpatterns = [

    path('', inicio, name='AppFinalInicio'),
    path('monotribustista/', monotributista, name='AppFinalMonotributista'),
    path('responsableinscripto/', responsable_inscripto, name='AppFinalResponsable'),
    path('impuesto/', impuestos, name='AppFinalImpuesto'),
    path('formulario/', formulario, name='AppFinalFormulario'),
    
]