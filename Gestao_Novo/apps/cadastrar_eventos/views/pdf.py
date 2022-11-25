from django.shortcuts import get_object_or_404, get_list_or_404
from ..models import Evento, Inscrito_Evento
from xhtml2pdf import pisa
from django.http import HttpResponse
from django.template.loader import get_template

def customer_render_pdf_view(request, *args, **kwargs):
    id = kwargs.get('id')
    evento = Evento.objects.filter(id=id)
    evento_id = get_object_or_404(Evento, id=id)
    inscrito = Inscrito_Evento.objects.filter(evento=evento_id)
    evento = get_object_or_404(Evento, id=id)
    a = len(inscrito)
    if len(inscrito) > 1:
        inscrito = get_list_or_404(Inscrito_Evento, evento=evento_id)

    template_path = 'teste0pdf.html'
    context = {
            'eventos' : evento,
            'inscritos': inscrito,
            'as': a
        }
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    #if download:
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    #if diplay:
    response['Content-Disposition'] = f'attachment; filename="{evento.nome_evento}.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>',context)
    return response

def render_pdf_view(request, id):
    evento = Evento.objects.filter(id=id)
    evento_id = get_object_or_404(Evento, id=id)
    inscrito = Inscrito_Evento.objects.filter(evento=evento_id)
    evento = get_object_or_404(Evento, id=id)
    a = len(inscrito)
    if len(inscrito) > 1:
        inscrito = get_list_or_404(Inscrito_Evento, evento=evento_id)

    template_path = 'teste0pdf.html'
    context = {
            'eventos' : evento,
            'inscritos': inscrito,
            'as': a
        }
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    #if download:
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    #if diplay:
    response['Content-Disposition'] = f'filename="{evento.nome_evento}.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>',context)
    return response