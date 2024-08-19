
from django.urls import path
from . import views

urlpatterns = [
    path('demo', views.demo),
    path('create', views.create),
    path('', views.dashboard),
    path('delete/<rid>', views.delete),
    path('edit/<rid>',views.edit)
]
