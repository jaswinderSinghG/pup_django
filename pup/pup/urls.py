"""pup URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from app import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('app', include('app.urls')),

    #Ishan sir, yeh comment wale saare urls sirf app mein mention kia hue hai, aur yeh chal rahe hai
    # path('', views.home, name='home'),
    # path('present_members', views.present_members, name='present_members'),
   
    # path('logout', views.logout_view, name='logout_view'),
    # path('login', views.login_view, name = 'login'),
    # path('admin_name', views.admin_name, name = 'admin_name'),
    # path('school', views.school, name = 'school'),
    #path('gallery', views.gallery, name = 'gallery'),

    #Aur yeh neeche wale urls mere ko dono jagah mention karne pade hai, 
    #yeh app mein bhi hai aur jaha par bhi, inko jaha se delete karke chalana hai.
    #Yeh urls tab accessible hai jab aap login karloge
    
    path('School_item_delete/<int:id>', views.School_item_delete, name='School_item_delete'),
    path('delete_gallery_item/<int:id>', views.delete_gallery_item, name='delete_gallery_item'),
    path('edit/<int:id>', views.edit, name ='edit'),
    path('article_image_delete/<int:id>', views.article_image_delete, name = 'article_image_delete'),
    path('delete/<int:id>', views.delete_items, name='delete'),
    path('home_update', views.home_update, name = 'home_update'),
    path('school_view', views.school_view, name = 'school_view'),
    path('school_admission', views.school_admission, name = 'school_admission'),
    path('upload_image', views.upload_image, name='upload_image'),
    path('delete/<int:id>', views.delete_items, name='delete'),
    path('home_dynamic_images', views.home_dynamic_images, name = 'home_dynamic_images'),
    path('show_data', views.show_data, name = 'show_data'),
    path('running_delete/<int:id>', views.running_delete, name = 'running_delete'),
    path('social_notice', views.social_notice, name = 'social_notice'),
    path('auth', include('social_django.urls', namespace='social')),
    path('delete_social_notice/<int:id>', views.delete_social_notice, name='delete_social_notice'),
    path('user_form_delete/<int:id>', views.user_form_delete, name = 'user_form_delete'),
    path('Admin_item_delete/<int:id>', views.Admin_item_delete, name = 'Admin_item_delete'),
    path('feedback_signup_view', views.feedback_signup_view, name = 'feedback_signup_view'),

    
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
