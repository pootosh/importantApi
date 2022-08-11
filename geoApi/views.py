from django.views import View
from django.http import JsonResponse
from .reusableCode.Location import Location

class GeoLocation(View):
    def get(self, request):
        return JsonResponse({"myLocation":Location.my_location(request.GET.get("mLocation"))})

    def post(self, request):
        distance = Location.distance_from_my_Location(request.POST.get('dLocation'))
        return JsonResponse({"minDistance": distance*1.1,"maxDistance": distance*1.2})

    
