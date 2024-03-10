# myapp/middleware.py

from django.http import JsonResponse

from django.conf import settings

class Verify:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        API_key = request.headers.get('key')
        print(API_key)
        if API_key != settings.APIKEY:
            return JsonResponse({"reason":'invalid Access Key'},status=404)
        # Log information about the incoming request

        # Call the next middleware or view
        response = self.get_response(request)

        return response
