from django.urls import path

from . import views


urlpatterns = [
	path('',views.HomePageView.as_view(), name='home'),
	path('compForm/', views.compPageView.as_view(), name='compForm'),
	path('mask/', views.maskPageView.as_view(), name='mask'),
	path('blog_list/', views.blogPageView.as_view(), name='blog_list'),
	
	]
