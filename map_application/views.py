from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from .models import CoordinatesModel
from django.contrib.gis.geos import Point


def rendermap(request):
    return render(request, 'index.html')


@csrf_exempt
def post_dot(request):
    if request.method == "POST":
        a = request.body
        print(a)
        a = a.decode('utf-8', )
        a = a.replace('LatLng', '').replace('(', '').replace(')', '')
        b, c = [i for i in a.split(',')]
        longitude = float(b)
        latitude = float(c)
        pnt = Point(latitude, longitude)
        created = CoordinatesModel.objects.get_or_create(
            coordinates=pnt
        )
    return HttpResponse('Done')

def get_dot(request):
   template = 'value.html'
   q = CoordinatesModel.objects.all()
   query_set = {'coordinate': q}
   return render(request, template, context=query_set)
