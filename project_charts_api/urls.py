"""project_charts_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from project_charts_api.api.views import axis_data_views
from project_charts_api.api.views import axis_labels_views

urlpatterns = [
    url(r'^axis_labels/$', axis_labels_views.AllAxisLabels.as_view(), name='all_labels'),
    url(r'^axis_labels/(?P<pk>[0-9]+)/$', axis_labels_views.AxisLabels.as_view(), name='axis_labels'),
    url(r'^axis_data/$', axis_data_views.AllAxisData.as_view(), name='all_data'),
    url(r'^axis_data/(?P<pk>[0-9]+)/', axis_data_views.AxisData.as_view(), name='axis_data'),
    url(r'^admin/', admin.site.urls),
]

urlpatterns = format_suffix_patterns(urlpatterns)