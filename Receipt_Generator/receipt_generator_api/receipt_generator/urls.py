from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import ReceiptViewSet
from receipt_generator import views

router = DefaultRouter()
router.register(r'receipts', ReceiptViewSet)

urlpatterns = [
    path("receipts/", include(router.urls)),
]
