from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Recipe
from recipe import serializers

class RecipeViewSet(viewsets.ModelViewSet):
    """
        VIEW FOR MANAGING RECIPE APIs
    """

    serializer_class = serializers.RecipeDetailSerializer
    queryset = Recipe.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        '''
            RECIPES FOR AUTHETICATED USERS
        '''
        return self.queryset.filter(user=self.request.user).order_by('-id')
    
    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.RecipeSerializer
        return self.serializer_class