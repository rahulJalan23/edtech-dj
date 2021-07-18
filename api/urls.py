from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('college-list/', views.CollegeList.as_view(), name='college-list'),
    path('college-detail/<str:college_code>/', views.CollegeDetail.as_view(), name='college-detail'),
    # path('subject-list/', views.SubjectList.as_view(), name="subject-list"),
    # path('subject-detail/<str:pk>/', views.SubjectDetail.as_view(), name="subject-detail"),
    # path('branch-list/', views.BranchList.as_view(), name="branch-list"),
    # path('branch-detail/<str:pk>/', views.BranchDetail.as_view(), name="branch-detail"),
    # path('course-list/', views.CourseList.as_view(), name="course-list"),
    # path('course-detail/<str:pk>/', views.CourseDetail.as_view(), name="course-detail"),
    # path('user-list/', views.UserList, name="user-list"),
    # path('user-detail/<str:username>/', views.userDetail, name="user-detail"),
    # path('textbook-list/', views.TextbookList.as_view(), name='textbook-list'),
    # path('textbook-detail/<str:pk>/', views.TextbookDetail.as_view(), name='textbook-detail'),
    # path('lecture-list/', views.LectureList.as_view(), name='lecture-list'),
    # path('day-list/', views.DayList.as_view(), name='day-list'),
    # path('timetable-list/', views.TimetableList.as_view(), name='timetable-list'),
    # path('portion-list/', views.PortionList.as_view(), name='portion-list'),
    # path('portion-detail/<str:pk>/', views.PortionDetail.as_view(), name='portion-detail'),
    # path('material-list/', views.MaterialList.as_view(), name='material-list'),
    
    # path('faculty-list/', views.FacultyList.as_view(), name='faculty-list'),
    # path('gsheettable-list/', views.GsheettableList.as_view(), name='gsheettable-list'),
]
