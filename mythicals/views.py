from rest_framework import viewsets
from .serializers import MythicalSerializer
from .models import Mythical

class MythicalViewset(viewsets.ModelViewSet):
    queryset = Mythical.objects.all()
    serializer_class = MythicalSerializer
