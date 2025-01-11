from django.shortcuts import render
from django.core.mail import send_mail
from django.shortcuts import render
from .forms import ContactForm
import os

def index(request):
    success = False  # Inicializar variable de éxito
    
    if request.method == 'POST':
        form = ContactForm(request.POST)  # Captura los datos del formulario
        
        if form.is_valid():
            # Obtener los datos del formulario
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            # Componer el mensaje
            full_message = f"Message from {first_name} {last_name} ({email}):\n\n{message}"

            # Enviar el correo
            send_mail(
                subject,
                full_message,
                email,
                ['icarpiodeveloper@gmail.com'],
                fail_silently=False,
            )

            success = True  # Si el formulario fue enviado correctamente

            # Crear una nueva instancia del formulario vacío
            form = ContactForm()

    else:
        form = ContactForm()  # Si la solicitud no es POST, mostrar el formulario vacío
    

    return render(request, 'landingpage/index.html', {'form': form, 'success': success})


