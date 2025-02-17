
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from base.models import Item
from .serializers import ItemSerializer


@api_view(['GET'])
def getData(request):
  items = Item.objects.all()
  serializer = ItemSerializer(items, many=True)

  return Response(serializer.data)

@api_view(['POST'])
def addItem(request):
  serializer = ItemSerializer(data=request.data)
  if serializer.is_valid():
    serializer.save()
  return Response(serializer.data)

@api_view(['PUT'])
def updateItem(request):
  try:
    dataId = request.data.get('id')
    item = Item.objects.get(pk=dataId)
  except:
    return Response(data=request.data, status=status.HTTP_404_NOT_FOUND)
  
  serializer = ItemSerializer(instance=item, data=request.data)
  if(serializer.is_valid()):
    serializer.save()
    return Response(status=status.HTTP_200_OK)
  else:
    return Response(status=status.HTTP_400_BAD_REQUEST)