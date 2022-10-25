import mimetypes
import os
from datetime import datetime
from django.shortcuts import render,HttpResponse

def download_file(request, filename=''):
    if filename != '':
        data = datetime.now()
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        filepath = BASE_DIR + '/excel/' + filename
        path = open(filepath, 'rb')
        mime_type, _ = mimetypes.guess_type(filepath)
        response = HttpResponse(path, content_type=mime_type)
        response['Content-Disposition'] = "attachment; filename=%s" % f"{data}.xlsx"
        return response
    else:
        return render(request, 'file.html')
