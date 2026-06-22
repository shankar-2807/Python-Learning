from django.urls import path
from . import views

urlpatterns = [
    path('demo1',views.demo1),    
    path('showResult',views.showResult),
    path('addProduct',views.addProduct),
    path('saveProduct',views.saveProduct),
    path('showProducts',views.showAllProducts),
    path('updateProduct',views.updateProduct),
]
