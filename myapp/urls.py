from django.urls import path
from . import views

urlpatterns = [
  path('Search/',views.search_page,name='Search'),
  path('Add/',views.add_people,name='Add'),
  path('student/<int:pk>/', views.delete_people, name='student_delete'),
  path('update-person/<int:pk>/', views.update_person, name='update_person'),

  # path('',views.index,name='Index')
]