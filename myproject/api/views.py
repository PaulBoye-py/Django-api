# Import Response from rest_framework.response
# Response object takes in python data or any other serialized data that is passed into it, and
# render it out as json
from rest_framework.response import Response

#import api_view from rest_framework.decorators if you are using function-based views
from rest_framework.decorators import api_view
from base.models import Item
from .serializers import ItemSerializer

# get request view
@api_view(['GET'])
def getData(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)

# post request view
@api_view(['POST'])
def addData(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
