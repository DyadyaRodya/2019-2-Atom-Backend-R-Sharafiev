from django.shortcuts import render
from django.http import HttpResponseNotAllowed

# Create your views here.
def hello_page(request):
    if request.method != 'GET':
        return HttpResponseNotAllowed(permitted_method=['GET'])
    try:
        return render(request, 'hello_page.html')
    except:
        raise Http404