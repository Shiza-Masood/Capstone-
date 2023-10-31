from django.shortcuts import render
from rest_framework.views import APIView
from .models import Menu,Booking
from .serializers import MenuSerializer,BookingSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class MenuItemsView(APIView):
   def get(self,request):
      items = Menu.objects.all()
      serializer = MenuSerializer(items,many=True)
      return Response(serializer.data)

   def post(self,request):
      serializer = MenuSerializer(data=request.data)

      if serializer.is_valid():
         serializer.save()
         return Response({'status':'success','data':serializer.data})


class SingleMenuItemView(APIView):
    def get(self, request, menu_item_unique):
        try:
            menu_item = Menu.objects.get(unique=menu_item_unique)
            #Serialize the menu item data if needed
            serializer = MenuSerializer(menu_item)
            return Response(serializer.data)

        except Menu.DoesNotExist:
            return Response(
                {"error": "Menu item not found"},
                status=status.HTTP_404_NOT_FOUND
            )

    def put(self, request, menu_item_id):
        menu_item = Menu.objects.get(id=menu_item_id)
        # Update menu item details based on request data
        serializer = MenuSerializer(menu_item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        menu_item.name = request.data.get('name', menu_item.name)
        menu_item.price = request.data.get('price', menu_item.price)
        menu_item.description = request.data.get('description', menu_item.description)
        menu_item.save()
        return Response({'message': 'Menu item updated successfully'})

    def delete(self, request, menu_item_id):
        menu_item = Menu.objects.get(id=menu_item_id)
        menu_item.delete()
        return Response({'message': 'Menu item deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

