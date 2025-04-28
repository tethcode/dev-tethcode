from django.shortcuts import render, redirect
from .models import Projects, Stack
from django.core.mail import send_mail
from django.http import JsonResponse
from django.contrib import messages
import socket
import smtplib
from django.conf import settings


def main(request):
    projects = Projects.objects.all().order_by("-date")
    stacks = Stack.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        try:
            send_mail(
                'Portfolio Contact Form',
                message,
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False
            )
            messages.success(request, "Email sent successfully!")
            return redirect('/')
        except socket.gaierror:
            return JsonResponse({'error': "No internet connection. Please try again later."}, status=503)
        except smtplib.SMTPConnectError:
            return JsonResponse({'error': "Could not connect to the SMTP server. Try again later"}, status=503)
        except Exception as e:
            return JsonResponse({'error': f"An unexpected error occured: {str(e)}"}, status=500)
    return render(request, 'index.html', { 'projects': projects, 'stacks': stacks })