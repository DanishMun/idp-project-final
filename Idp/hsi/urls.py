from django.urls import path
from .views import show_images, show_multiframe, show_home

urlpatterns = [
    path('showimages/<path:filename>', show_images, name='showimages'),
    path('showmultiframe/<path:filename>', show_multiframe, name='showimages'),
    path('home/', show_home, name='showhome'),

]