from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('login',views.logins,name='login'),
    path('logout',views.logouts,name='logout'),
    path('user',views.user,name='user'),
    path('superuser',views.superuser,name='superuser'),
    path('update',views.update,name='update'),
    path('accept',views.accept,name='accept'),
    # path('reject',views.reject,name='reject'),
]