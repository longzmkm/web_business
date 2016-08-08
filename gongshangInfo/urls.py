from django.conf.urls import url
from gongshangInfo import views



urlpatterns = [
    url(r'^poems/$', views.CompanyListView.as_view(),name='CompanyListView'),
    url(r'^poem/(?P<pk>[0-9]+)$',views.company_detail,name='showCompany'),
]
