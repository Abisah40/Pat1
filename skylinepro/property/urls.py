from django.urls import path
from .views import (Create_new_property,View_new_property,update_property,delete_property)


urlpatterns = [
    path('post-property/', Create_new_property.as_view(), name= 'property-create'),
    path('view-property/', View_new_property.as_view(), name= 'property-list'),
    path('update-property/<int:pk>/', update_property.as_view(), name= 'update-property'),
    path('delete-property/<int:pk>/', delete_property.as_view(), name= 'delete-property'),

]


