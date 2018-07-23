from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Record
from .serializers import RecordSerializer
from .permissions import IsOwner


class RecordCreateView(ListCreateAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    permission_classes = (
        IsAuthenticated,
        IsOwner,
    )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class RecordDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    permission_classes = (
        IsAuthenticated,
        IsOwner,
    )
