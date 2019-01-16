from django.urls import path

from .views import BlogListView, BlogDetailView

urlpatterns = [
	path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'), #int:pk is the primary key that is id. We can call id or pk.
	path('', BlogListView.as_view(), name='home'),
]