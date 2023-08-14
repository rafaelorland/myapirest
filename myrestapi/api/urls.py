from . import views
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('', views.getRoutes),
    path('projetos/', views.getProjetos),
    path('perfil/', views.getProfile),
    path('users/token/', TokenObtainPairView.as_view(), name = 'token_obtain_pair'),
]
