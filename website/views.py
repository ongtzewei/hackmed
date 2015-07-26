from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.http import require_GET
from website.models import Dish

@require_GET
def get_main(request, *args, **kwargs):
    dishes = Dish.objects.all()
    return render_to_response('website/sidebar.html', {'dishes':dishes},
                              context_instance=RequestContext(request))