from django.urls import path,include
from .views import index,all_medicine,add,cart,delete_cart
urlpatterns = [
   path('',index ,name ='index'),
   path('all/',all_medicine ,name ='all'),
   path('drug/<int:med_id>',add ,name ='drug'),
   path('cart/',cart ,name ='cart'),
   path('delete/<int:d_id>',delete_cart ,name ='delete'),
]