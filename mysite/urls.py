from django.urls import path, include
from .views import (CompanyView, CompanyCreate, CompanyDetail,
                    AdView, AdCreate, AdDetail, AdUpdate, ImageViewSet)

from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('image', ImageViewSet)

# image/ -> image/ -> GET -> image.objects.all()
# image/3/ -> GET -> image.objects.get(pk=3)
# image/ -> POST -> image.objects.create()
# image/3/ -> PUT -> update
# image/3/ -> PATCH -> partial_update
# image/3/ -> DELETE -> delete


urlpatterns = [
    # Company end points
    path('company/list/', CompanyView.as_view(), name='company_list'),
    path('company/create/', CompanyCreate.as_view(), name='company_create'),
    path('company/<int:pk>/', CompanyDetail.as_view(), name='company_detail'),
    # Company Advertisement end points
    path('ad/list/', AdView.as_view(), name='ad_list'),
    path('ad/create/', AdCreate.as_view(), name='ad_create'),
    path('ad/<int:pk>/', AdDetail.as_view(), name='ad_detail'),
    path('ad/<int:pk>/update/', AdUpdate.as_view(), name='ad_update'),
    # Image router
    path('', include(router.urls)),
]