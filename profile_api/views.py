from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from profile_api import serializers
from profile_api import models
from profile_api import permissions


class MyApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Return a list of APIView features"""
        my_list = ['A','B','C']
        return Response({'message':'Hello View', 'my_list':my_list})

    def post(self, request):
        """Create a hello message with a name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Update a list of object"""
        return Respone({'method':'PUT'})

    def patch(self, request, pk=None):
        """Partially update an object"""
        return  Response({'method':'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method':'DELETE'})


class HelloVeiwset(viewsets.ViewSet):
    """Test API Viewset"""
    serializer_class = serializers.HelloSerializer

    def list(self,request):
        """Return a message"""
        list = ['W','X','Y','Z']
        return Response({'message':'Hello', 'list':list})

    def create(self,request):
        """create a new hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message':message})

        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self,request,pk=None):
        """Handle getting an object by its ID"""
        return Response({'HTTP_Method': 'GET'})

    def update(self,request,pk=None):
        """Handle Updating an object"""
        return Response({'HTTP_Method':'PUT'})

    def partial_update(self,request,pk=None):
        """Handle partial update of an object"""
        return Response({'HTTP_Method':'PATCH'})

    def destroy(self,request,pk=None):
        """Delete an object by its id"""
        return Response({'HTTP_Method':'DELETE'})


class UserProfileViewset(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = [TokenAuthentication,]
    permission_classes = [permissions.UpdateOwnProfile,]
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email')

class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication token"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
