import json
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from django.http import HttpResponse

@api_view(['GET'])
@permission_classes([AllowAny])
def ok_view(request, format=None):
    content = {
        'name': 'Digitalsys API',
    }
    return HttpResponse(json.dumps(content), content_type="application/json")