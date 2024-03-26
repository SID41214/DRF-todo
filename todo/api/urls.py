from api import views
from django.urls import path


urlpatterns = [
    path('register/',views.RegisterAPIView.as_view(),name='register'),
    
]
