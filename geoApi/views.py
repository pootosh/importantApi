from django.views import View
from django.http import JsonResponse
from .reusableCode.Location import Location

class GeoLocation(View):
    def get(self, request):
        return JsonResponse({"myLocation":Location.my_location()})

    def post(self, request):
        my_location = Location.my_location()
        dest_location = Location.get_location_by_address(request.POST.get('dLocation'))
        
        return JsonResponse({"myLocation": my_location, "destLocation": dest_location})

    
