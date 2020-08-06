from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Nombre',required=True, widget=forms.TextInput(attrs={'class':'form-control',
    'placeholder':'Escribe tú nombre'}),max_length=100,min_length=3)
    email = forms.EmailField(label='Email',required=True, widget=forms.EmailInput(attrs={'class':'form-control',
    'placeholder':'Escribe tú email'}),max_length=100,min_length=3)
    content = forms.CharField(label='Contenido',required=True,widget=forms.Textarea(attrs={'class':'form-control',
    'placeholder':'Escribe tú mensaje'}),max_length=300,min_length=3)