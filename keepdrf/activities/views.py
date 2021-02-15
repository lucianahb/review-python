from rest_framework import viewsets
from .serializers import ActivitySerializer, TagSerializer, ResponsibleSerializer
from .models import Activity, Tag, Responsible


class ActivityViewSet (viewsets.ModelViewSet):
    queryset = Activity.objects.all().order_by('deadline')
    serializer_class = ActivitySerializer


class TagViewSet (viewsets.ModelViewSet):
    queryset = Tag.objects.all().order_by('tag')
    serializer_class = TagSerializer


class ResponsibleViewSet (viewsets.ModelViewSet):
    queryset = Responsible.objects.all().order_by('responsible')
    serializer_class = ResponsibleSerializer
