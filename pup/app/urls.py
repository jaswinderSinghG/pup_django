from django.conf.urls import url
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views
# from django.contrib.auth import views as auth_view
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', views.home, name='home'),
    path('present_members', views.present_members, name='present_members'),
    path('login', views.login_view, name = 'login'),
    path('upload_image', views.upload_image, name='upload_image'),
    path('logout', views.logout_view, name='logout_view'),
    path('delete/<int:id>', views.delete_items, name='delete'),
    path('article_image_delete/<int:id>', views.article_image_delete, name = 'article_image_delete'),
    path('edit/<int:id>', views.edit, name ='edit'),
    path('social_login', LoginView.as_view, name='social_login'),
    path('show_data', views.show_data, name = 'show_data'),
    path('home_update', views.home_update, name = 'home_update'),
    path('admin_name', views.admin_name, name = 'admin_name'),
    path('school', views.school, name = 'school'),
    path('school_view', views.school_view, name = 'school_view'),
    path('school_admission', views.school_admission, name = 'school_admission'),
    path('gallery', views.gallery, name = 'gallery'),
    path('activity', views.activity, name = 'activity'),
    path('run_activity', views.run_activity, name ='run_activity'),
    path('running_delete/<int:id>', views.running_delete, name = 'running_delete'),
    path('home_dynamic_images', views.home_dynamic_images, name = 'home_dynamic_images'),
    path('social_notice', views.social_notice, name = 'social_notice'),
    path('delete_social_notice/<int:id>', views.delete_social_notice, name='delete_social_notice'),
    path('delete_gallery_item/<int:id>', views.delete_gallery_item, name='delete_gallery_item'),
    path('School_item_delete/<int:id>', views.School_item_delete, name='School_item_delete'),
    path('public_notice', views.public_notice, name = 'public_notice'),
    path('user_form_msg', views.user_form_msg, name = 'user_form_msg'),
    path('user_form_delete/<int:id>', views.user_form_delete, name = 'user_form_delete'),
    path('Admin_item_delete/<int:id>', views.Admin_item_delete, name = 'Admin_item_delete'),
    path('feedback_signup_view', views.feedback_signup_view, name = 'feedback_signup_view'),
    
    
    
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)