from rest_framework import status, generics, mixins
from .models import Contact
from .serializers import ContactSerializer


class ContactViews(generics.GenericAPIView,mixins.CreateModelMixin,
                   mixins.ListModelMixin,mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        obj = queryset.get(pk=self.request.data.get('id'))
        return obj

    def filter_queryset(self, queryset):
        if self.request.query_params.get('id'):
            queryset = queryset.filter(id=self.request.query_params.get('id'))
        return queryset

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        self.destroy(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)