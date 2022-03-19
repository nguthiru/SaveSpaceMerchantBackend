from django.urls import path,include
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
urlpatterns=[
    path('', include('rest_auth.urls')),
    path('register/', include('rest_auth.registration.urls'))
]

urlpatterns+=router.urls