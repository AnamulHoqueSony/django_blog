from . import views
from django.urls import path

urlpatterns = [
    path('',views.home,name = 'blog-name'),
    path('About/',views.About,name = 'About-name'),
]
