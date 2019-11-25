from django.contrib import admin
from django.conf.urls import include, url
from .views import RegistroView, CustomLoginView
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views


router = DefaultRouter()
# # router.register('', UsersViewSet, base_name='user')
# router.register('montar', ComputadoresViewset , basename='Computadores')
# router.register('pedidos', , basename='Pedidos')


urlpatterns = [
    # url(r'^', include(router.urls)),
    url(r'^', include('apps.pedidos.urls')),
    url(r'^rest-auth/login/', CustomLoginView.as_view()),
    url(r'^rest-auth/registrar/', RegistroView.as_view()),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^admin/', admin.site.urls),
]
