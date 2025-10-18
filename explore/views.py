from django.template import loader
from django.http import HttpResponse

# Create your views here.
def explore(request):
    template = loader.get_template('explore.html')
    return HttpResponse(template.render())