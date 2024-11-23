"""
URL configuration for assproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from assapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('forgot-password/', views.forgot_password_view, name='forgot_password'),
    path('requests/', views.request_list, name='request_list'),
    path('create_request/', views.create_request, name='create_request'),
    path('search_customer/', views.search_customer, name='search_customer'),
    path('delete_request/<int:id>/', views.delete_request, name='delete_request'),
    path('view_request/<int:request_id>/', views.view_request, name='view_request'),
    path('edit_request/<int:request_id>/', views.edit_request, name='edit_request'),
    path('delete_file/<int:request_id>/', views.delete_file, name='delete_file'),
    path('export/<int:request_id>/', views.export_to_excel, name='export_to_excel')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)