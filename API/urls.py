
from django.urls import path
#Menually added
from . import views


urlpatterns = [

    path('', views.Test ),
    path('blog', views.BlogPosts),
    path('blog/<int:pk>', views.BlogPost)
    
]
