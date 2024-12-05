"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)


from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .router import router
from core.usuario.views import verify_email
from core.mooner.views import HistoryDestroyView
from core.microservice.mercadopago import AssignView
from core.alternative_api.recomendations import RecomendationView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path('api/verify_email/<str:verification_token>/', verify_email, name='verify_email'),
    path('api/history/destroy/', HistoryDestroyView.as_view(), name='history_destroy'),
    path('api/payment/<str:email>/', AssignView.as_view(), name='mp_assign'),
    path('api/payment/', AssignView.as_view(), name='mp_assign'),
    path('api/recomendations/<str:user>/', RecomendationView.as_view(), name='recomendation'),
    path(
        "api/swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
    path('api/', include(router.urls)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
