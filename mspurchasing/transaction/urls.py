from django.urls import path
from .views import PurchaseOrderAPIView, PurchaseOrderDetailAPIView, CategoryAPIView, VendorAPIView, ProductTypeAPIView, ProductAPIView, PriorityAPIView, ResponsibleAPIView

urlpatterns = [
    path('purchases/', PurchaseOrderAPIView.as_view(), name='purchase_orders'),
    path('purchases/<int:pk>/', PurchaseOrderDetailAPIView.as_view(), name='purchase_order_detail'),
    path('categories/', CategoryAPIView.as_view()),
    path('vendors/', VendorAPIView.as_view()),
    path('product_type/', ProductTypeAPIView.as_view()),
    path('product/', ProductAPIView.as_view()),
    path('priority/', PriorityAPIView.as_view()),
    path('responsible/', ResponsibleAPIView.as_view()),
]
