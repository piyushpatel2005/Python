from django.urls import path
from . import views

app_name = 'blog' # used to organize urls by application

urlpatterns = [
    # You can se re_path() to define complex URL patterns with Python regular expressions
    # path('', views.post_list, name='post_list'),
    path('', views.PostListView.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_details, name='post_detail'),
    path('<int:post_id>/share/', views.post_share, name='post_share'),
]