from django.urls import path
from . import views

urlpatterns = [
    # path('hello',views.helloFromFirst),
    # path('demo',views.demoHtml),
    # path('login', views.login),
    path('displayName',views.displayName),
    path('displayList',views.displayList),
    path('displayDict',views.displayDict),
    path('displayStudent',views.displayStudent),

    
]

