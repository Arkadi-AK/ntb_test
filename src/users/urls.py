from django.urls import path

from users.views import user_login, register, user_logout

urlpatterns = [
    # path('', include('django.contrib.auth.urls')),
    path('login/', user_login, name='login'),
    path('register/', register, name='register'),
    path('logout/', user_logout, name='logout'),
]
