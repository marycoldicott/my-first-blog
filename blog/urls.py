from django.urls import path
from . import views
import lists.views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),
    path('contact/', views.contact, name="contact"),
    path('drafts/', views.post_draft_list, name='post_draft_list'),
    path('post/<pk>/publish/', views.post_publish, name='post_publish'),
    path('cv/', lists.views.cv_page, name="cv"),
    #path('cv/phoo=t', lists.views.cv_add_photo, name="cv_add_photo"),
]