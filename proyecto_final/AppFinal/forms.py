from django import forms


class Formulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    edad = forms.IntegerField()
    mail = forms.EmailField()

class BusquedaNombreFormulario(forms.Form):
    nombre = forms.CharField()