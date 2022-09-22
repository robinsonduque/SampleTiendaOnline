from calendar import Calendar
from django import forms


class ContactoForm(forms.Form):
    nombre = forms.CharField(label="Your name", max_length=100, required=True)
    email = forms.EmailField(label="email", required=True)
    mensaje = forms.CharField(label="Contenido", widget=forms.Textarea, required=False)
