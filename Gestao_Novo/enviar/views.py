from django.shortcuts import render,HttpResponse, get_object_or_404, get_list_or_404
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from .models import Usuario
# Create your views here.

def mail(request):
    return render(request, 'formulario_de_envio.html')

def enviar(request):
    destinatario = []
    if request.method == "POST":
        remetente = request.POST['remetente']
        if request.POST['destinatario1']:
            verifica = True
            n = 1
            while verifica == True:
                print(n)
                dsn = f'destinatario{n}'
                if dsn in request.POST:
                    destino = request.POST[dsn]
                    n += 1
                    destinatario.append(destino)
                else:
                    verifica = False
        if request.POST['assunto']:
            assunto = request.POST['assunto']
        if request.POST['mensagem']:
            mensagem = request.POST['mensagem']

        htmlcontent = render_to_string('envio.html', {'mensagem': mensagem})
        convertido = strip_tags(htmlcontent)
        emailenviado = EmailMultiAlternatives(assunto, convertido, remetente, destinatario)
        emailenviado.attach_alternative(htmlcontent, 'text/html')
        emailenviado.send()
        # send_mail(assunto, mensagem, remetente, destinatario)
    return HttpResponse('Enviado')

def enviar_todos(request):
    emails = get_list_or_404(Usuario)
    
    if request.method == "POST":
        if request.POST['assunto']:
            assunto = request.POST['assunto']
        if request.POST['mensagem']:
            mensagem = request.POST['mensagem']
    
    for mali in emails:
        htmlcontent = render_to_string('envio.html',{'nome':mali.nome,'mensagem':mensagem})
        convertido = strip_tags(htmlcontent)
        emailenviado = EmailMultiAlternatives(assunto, convertido, 'ouvidoriaadocicafornasa@gmail.com', [mali.e_mail])
        emailenviado.attach_alternative(htmlcontent, 'text/html')
        emailenviado.send()
    # send_mail(assunto, mensagem, remetente, destinatario)
    return HttpResponse('Enviado')
    