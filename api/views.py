from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from . import serializers
from . import models
from . import permissions


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles creating, creating and updating profiles."""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


class LoginViewSet(viewsets.ViewSet):
    """Checks e-mail and password and returns an auth token."""

    serializer_class = AuthTokenSerializer

    def create(self, request):
        """Use the ObtainAuthToken APIView to validate and create a token."""

        return ObtainAuthToken().post(request)


class WeekViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ToDoSerializer
    queryset = models.toDo.objects.all()
    # permission_classes = (permissions.PostOwnStatus,)# IsAuthenticated)

    def create(self, request):

        serializer = serializers.ToDoSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            description = serializer.data.get('description')
            message = '{0}'.format(description)
            return Response({'message': message})
        else:
            return Response({'message': 'failed'})

    def partial_update(self, request):
        return Response({'http_method': 'PATCH'})


class DoneViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ToDoSerializer
    queryset = models.toDo.objects.all()
    # permission_classes = (permissions.PostOwnStatus,)# IsAuthenticated)

    def list(self, request):
        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)'
            'Automatically maps to URLS using Routers',
            'Provides more functionality with less code'
        ]

        return Response({'message': 'Hello!', 'a_viewset': a_viewset})

    def partial_update(self, request):
        return Response({'http_method': 'PATCH'})


class LateViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ToDoSerializer
    queryset = models.toDo.objects.all()
    # permission_classes = (permissions.PostOwnStatus,)# IsAuthenticated)

    def list(self, request):
        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)'
            'Automatically maps to URLS using Routers',
            'Provides more functionality with less code'
        ]

        return Response({'message': 'Hello!', 'a_viewset': a_viewset})

    def partial_update(self, request):
        return Response({'http_method': 'PATCH'})
