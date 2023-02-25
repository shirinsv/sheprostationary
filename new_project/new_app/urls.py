from django.urls import path
from . import views
app_name='new_app'
urlpatterns = [
    path('', views.index,name='index'),
    path('product/<int:product_id>/',views.detail,name='detail'),
    path('add/',views.add_products,name='add_products'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete')
    ]
