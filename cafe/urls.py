from django.urls import path, re_path
from .views import CategoryLV,CategoryDV
from. import views

app_name = "cafe"

urlpatterns = [
    path("categories", CategoryLV.as_view(), name="index"),  
    re_path(r'categories/(?P<slug>[-\w]+)/$', views.CategoryDV.as_view(), name="category_detail"), 
]   