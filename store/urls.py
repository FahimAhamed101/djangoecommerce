from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home,name="home"  ),
    path('product/<slug:product_slug>',views.product_info,name="product-info"  ),
    path('search/<slug:category_slug>',views.list_categories,name="list-categories"  ),
]
