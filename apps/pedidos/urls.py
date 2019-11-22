from django.urls import include, path, re_path
from . import views

app_name = 'pedidos'

urlpatterns = [
    # re_path(r'^api/pedidos/(?P<pk>[0-9]+)$', # Url to get update or delete a movie
    #     views.get_delete_update_movie.as_view(),
    #     name='get_delete_update_movie'
    # ),
    path('api/pedidos/', views.get_post_pedidos.as_view(), name='get_post_pedidos'
    )
]