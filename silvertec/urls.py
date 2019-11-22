from django.contrib import admin
from django.conf.urls import include, url
from .views import RegistroView, CustomLoginView



urlpatterns = [
    url(r'^', include('apps.pedidos.urls')),
    url(r'^rest-auth/login/', CustomLoginView.as_view()),
    url(r'^rest-auth/registration/', RegistroView.as_view()),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^admin/', admin.site.urls),
]
