"""
URL configuration for setup project.

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

from django.urls import path
from django.views.generic import RedirectView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from careers.views import CareersView, CareerDetailView

urlpatterns = [
    path('careers/', CareersView.as_view(), name='careers'),
    path('careers/<int:pk>/', CareerDetailView.as_view(), name='career_detail'),
    # Redirecionar para a versão com a barra
    path('careers/<int:pk>', RedirectView.as_view(pattern_name='career_detail', permanent=True)),
]

urlpatterns += staticfiles_urlpatterns()
