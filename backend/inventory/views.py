from rest_framework import viewsets
from .models import Item
from .serializers import ItemSerializer
from rest_framework import generics, viewsets, filters
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from .models import Item
from .serializers import ItemSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all().order_by('-created_at') # Order by newest first
    serializer_class = ItemSerializer

    # ACTIVATE THE FILTERS
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    
    # 1. Exact Match Filtering (for Shape and Color)
    filterset_fields = ['shape', 'color']
    
    # 2. Fuzzy Search (for Name)
    search_fields = ['name']

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny] # Allow strangers to register

class CustomLoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email,
            'is_staff': user.is_staff
        })