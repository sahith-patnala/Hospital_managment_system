"""
URL configuration for myproject project.

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
# from django.contrib import admin
# from django.urls import path
# from myapp import views

# urlpatterns = [
#     path("admin/",admin.site.urls),
#     path('home/', views.home, name='home'),
#     path('predict/', views.predict, name='predict'),
#     path('Appionment/', views.Appionment, name='Appionment'),
# ]


from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path("", views.index, name='index'),
    path("index1/", views.index1, name='index1'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('relief/', views.relief, name='relief'),
    path('youtube/', views.youtube, name='youtube'),
    path('self/', views.self, name='self'),
    path('articles/', views.articles, name='articles'),
    path('logout/', views.logout, name='logout'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('help/', views.help, name='help'),
    path('predict/', views.predict, name='predict'),
    path('appointment/', views.appointment, name='appointment'),  # Corrected name
]
