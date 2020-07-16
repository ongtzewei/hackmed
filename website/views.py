from django.shortcuts import render
from django.template import RequestContext
from django.views.decorators.http import require_GET
from website.models import Dish

@require_GET
def get_main(request, *args, **kwargs):
    dishes = Dish.objects.all()
    return render(request, 'website/sidebar.html', {'dishes':dishes})