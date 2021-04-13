from django.contrib import admin
from django.urls import path
from .import views
app_name='crud'
urlpatterns = [

    path('',views.index,name='index'),
    path('store',views.store,name='store'),
    path('<int:id>/edit',views.edit,name='edit'),
    path('<int:id>/update',views.update,name='update'),
    path('<int:id>/delete',views.delete,name='delete'),

]
