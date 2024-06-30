
from django.urls import path
from contact import views

#name que referencia a qual app aqquelas urls pertencem para evitar conflito de chamadas
app_name =  'contact'

urlpatterns = [
    #contact (CRUD)
    path('contact/<int:contact_id>/', views.contact, name='contact'),
    path('contact/create/', views.create, name='create'),
    # path('contact/<int:contact_id>/update', views.contact, name='contact'),
    # path('contact/<int:contact_id>/delete', views.contact, name='contact'),
    
    
    
    
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
]
