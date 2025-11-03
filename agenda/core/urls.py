from django.urls import path
from core.views import login, logout, home, create_contact, list_contacts, detail_contact, update_contact, delete_contact

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('index/', home, name='index'),
    path('create_contact/', create_contact, name='create'),
    path('list_contacts/', list_contacts, name='list'),
    path('detail_contact/<int:pk>/', detail_contact, name='detail'),
    path('delete_contact/<int:pk>/', delete_contact, name='delete'),
    path('update_contact/<int:pk>/', update_contact, name='update'),
    path('', home, name='home')
]