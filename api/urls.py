from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('subject-list/', views.SubjectList.as_view(), name="subject-list"),
    path('subject-detail/<str:pk>/', views.SubjectDetail.as_view(), name="subject-detail"),
    path('branch-list/', views.BranchList.as_view(), name="branch-list"),
    path('branch-detail/<str:pk>/', views.BranchDetail.as_view(), name="branch-detail"),
    path('course-list/', views.CourseList.as_view(), name="course-list"),
    path('course-detail/<str:pk>/', views.CourseDetail.as_view(), name="course-detail"),
    path('user-list/', views.UserList, name="user-list"),
    path('user-detail/<str:username>/', views.userDetail, name="user-detail"),
    path('textbook-list/', views.TextbookList.as_view(), name='textbook-list'),
    path('textbook-detail/<str:pk>/', views.TextbookDetail.as_view(), name='textbook-detail'),
    # path('lecture-list/', views.LectureList.as_view(), name='lecture-list'),
    # path('timetable-list/', views.TimetableList.as_view(), name='timetable-list'),
]
