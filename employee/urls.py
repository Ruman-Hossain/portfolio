from django.urls import path
from .import views


urlpatterns = [
    path('',views.employee),
    path('profile',views.profile,name='employe.profile'),



    #ROUT GROUPING
    # path('index',views.profile,name='employe.index'),
    # path('store',views.profile,name='employe.store'),
    # path('edit',views.profile,name='employe.edit'),
    # path('delete',views.profile,name='employe.delete'),

]
