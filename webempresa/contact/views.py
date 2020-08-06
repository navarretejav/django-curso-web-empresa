from django.shortcuts import render, redirect
from django.urls import reverse 
from django.core.mail import EmailMessage
from .forms import ContactForm

# Create your views here.
    
def contact(request):
    form = ContactForm() 

    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name','')
            email = request.POST.get('email','')
            content = request.POST.get('content','')
            #Suponemos que todo ha ido bien
            # return redirect('/contact/?ok')
            #Hace lo mismo que lo anterior pero usamos la función reverse àra poder usar el Template TAG contact
            # return redirect(reverse('contact')+'?ok')
            # Enviamos el email
            x=EmailMessage()
            email = EmailMessage(
                'La Caffeteriera: nuevo mensaje de contacto',
                'De {} <{}>\n\nEscribió:\n\n{}'.format(name,email,content),
                'navarretejav@hotmail.com',
                ['navarretejav@gmail.com'],
                reply_to=[email]
            )
            try:
                email.send()
                return redirect(reverse('contact')+'?ok')
            except:
                return redirect(reverse('contact')+'?fail')

    return render(request,'contact/contact.html',{'form':form})