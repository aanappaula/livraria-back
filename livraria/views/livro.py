from rest_framework.viewsets import ModelViewSet

from livraria.models import Livro
from livraria.serializers import (LivroSerializer, LivroDetailSerializer)


class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.all()
    # permission_classes = [IsAuthenticated]
    # serializer_class = LivroSerializer

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return LivroDetailSerializer
        return LivroSerializer
    