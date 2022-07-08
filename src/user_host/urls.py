from django.urls import path

from user_host.views import Home, ViewHost, add_host, edit_host

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('host/<int:pk>/', ViewHost.as_view(), name='view_host'),
    path('host/<int:id>/edit_host/', edit_host, name='edit_host'),
    path('host/add_host/', add_host, name='add_host'),
]
