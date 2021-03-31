from django.urls import path
from rajsekhar import views
urlpatterns = [
 path('',views.home),
 path("demo/",views.chk),
 path("ht/",views.homepage),
 path("lg/",views.lgn),
 path("rg/",views.reg),
]