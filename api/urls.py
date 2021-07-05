from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('subject-list/', views.subjectList, name="subject-list"),
    path('subject-detail/<str:pk>/', views.subjectDetail, name="subject-detail"),
    path('branch-list/', views.branchList, name="branch-list"),
    path('branch-detail/<str:pk>/', views.branchDetail, name="branch-detail"),
    path('course-list/', views.courseList, name="course-list"),
    path('course-detail/<str:pk>/', views.courseDetail, name="course-detail"),
    path('user-list/', views.UserList, name="user-list"),
    path('user-detail/<str:pk>/', views.userDetail, name="user-detail"),
    path('textbook-list/', views.TextbookList.as_view(), name='textbook-list'),
    path('textbook-detail/<str:pk>/', views.TextbookDetail.as_view(), name='textbook-detail'),
]
