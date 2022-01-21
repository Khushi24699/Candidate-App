from django.urls import path  
from . import views

urlpatterns= [
     path('', views.home, name='home'),
     path('profile/', views.my_profile, name='my-profile'),
    path('profile/edit/', views.edit_profile, name='edit-profile'),
    path('profile/<slug>', views.profile_view, name='profile-view'),
    path('introduction/', views.candidate_details, name='detail-candidates'),
    path('delete_skills/', views.delete_skill, name='skill-delete'),
    path('delete_profile/', views.delete_profile, name='profile-delete'),

]
