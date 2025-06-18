from django.urls import path
from . import views

urlpatterns=[
    path('register/', views.register_view,name='register'),
    path('login/', views.login_view,name='login'),
    path('logout/', views.logout_view,name='logout'),
    path('dashboard/', views.dashboard_view,name='dashboard'),
    path('diary/',views.diary_view,name='diary'),
    path('entry/<int:pk>/update/',views.update_entry,name='update_entry'),
    path('entry/<int:pk>/delete/',views.delete_entry,name='delete_entry'),
    path('entry/<int:pk>/', views.entry_detail,name='entry_detail'),
    path('news/',views.news_index,name='news'),
    path('', views.index_view, name='index'),
]