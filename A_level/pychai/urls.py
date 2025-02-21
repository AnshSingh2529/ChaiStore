from django.urls import path
from . import views

urlpatterns = [
      path('', views.all_pychai, name='all_pychai'),
      path("<int:chai_id>/", views.pychai_detail, name="pychai_detail"),
      path('add_pychai/', views.add_pychai, name='add_pychai'),
      path('<int:chai_id>/edit/', views.edit_pychai, name='edit_pychai'),
      path('<int:chai_id>/delete/', views.delete_pychai, name='delete_pychai'),
      # path('create_store/', views.create_store, name='create_store'),
      # path('pychai_store/', views.pychai_store, name='pychai_store'),
      
]     