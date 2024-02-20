from rest_framework import viewsets
from .models import Receipts
from .serializer import ReceiptSerializer


class ReceiptViewSet(viewsets.ModelViewSet):
    queryset = Receipts.objects.all()
    serializer_class = ReceiptSerializer
