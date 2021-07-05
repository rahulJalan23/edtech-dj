from typing import List
from rest_framework import serializers

from django.shortcuts import render
from django.http import JsonResponse, Http404
import rest_framework
from rest_framework import pagination

from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework import status

from django.contrib.auth.models import User
from .models import (Subject, 
					Branch, 
					Course,
					Textbook)
from .serializers import (CourseSerializer, 
						  SubjectSerializer,
						  BranchSerializer,
						  UserSerializer,
						  TextbookSerializer)

# Create your views here.

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List Textbooks':'/textbook-list/',
		'Textbook Detail View':'/textbook-detail/<str:pk>/',
        'List Teachers': '/teacher-list/',
        'Teacher Detail View': '/teacher-detail/<str:pk>/',
        'List Courses':'/course-list/',
		'Course Detail View':'/course-detail/<str:pk>/',
        'List Branches':'/branch-list/',
		'Branche Detail View':'/branch-detail/<str:pk>/',
        'List Subjects': '/subject-list/',
        'Subject Detail View':'/subject-detail/<str:pk>/',
		'List Users': '/user-list/',
        'User Detail View':'/user-detail/<str:pk>/',
	}

	return Response(api_urls)


# utility
class ResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 50



# @api_view(['GET'])
# def subjectList(request):
# 	subjects = Subject.objects.all()
# 	serializer = SubjectSerializer(subjects, many=True)
# 	return Response(serializer.data)
# 	# return JsonResponse(serializer.data, safe=False)
# 	# return JsonResponse(serializer.data, json_dumps_params={'indent': 2}, safe=False)


# @api_view(['GET'])
# def subjectDetail(request, pk):
# 	subject = Subject.objects.get(id=pk)
# 	serializer = SubjectSerializer(subject, many=False)
# 	return Response(serializer.data)


# @api_view(['GET'])
# def branchList(request):
# 	branches = Branch.objects.all()
# 	serializer = BranchSerializer(branches, many=True)
# 	return Response(serializer.data)


# @api_view(['GET'])
# def branchDetail(request, pk):
# 	branch = Branch.objects.get(id=pk)
# 	serializer = BranchSerializer(branch, many=False)
# 	return Response(serializer.data)


# @api_view(['GET'])
# def courseList(request):
# 	courses = Course.objects.all()
# 	serializer = CourseSerializer(courses, many=True)
# 	return Response(serializer.data)


# @api_view(['GET'])
# def courseDetail(request, pk):
# 	course = Course.objects.get(id=pk)
# 	serializer = CourseSerializer(course, many=False)
# 	return Response(serializer.data)


@api_view(['GET'])
def UserList(request):
	users = User.objects.all()
	serializer = UserSerializer(users, many=True)
	return Response(serializer.data)


@api_view(['GET'])
def userDetail(request, pk):
	user = User.objects.get(id=pk)
	serializer = UserSerializer(user, many=False)
	return Response(serializer.data)


""" Subject """
class SubjectList(ListAPIView):
	"""
	List all Subjects [GET] or create a new Texbook
	"""

	# return the list of subjects
	queryset = Subject.objects.all()
	serializer_class = SubjectSerializer
	pagination_class = ResultsSetPagination

	
	def post(self, request, format=None):
		serializer = SubjectSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SubjectDetail(APIView):
	"""
	Retrieve, update or delete a Subject instance.
	"""
	def get_object(self, pk):
		try:
			return Subject.objects.get(pk=pk)
		except Subject.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None):
		subject = self.get_object(pk)
		serializer = SubjectSerializer(subject)
		return Response(serializer.data)
	
	def put(self, request, pk, format=None):
		subject = self.get_object(pk)
		serializer = SubjectSerializer(subject, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
		subject = self.get_object(pk)
		subject.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)


""" Branch """
class BranchList(ListAPIView):
	"""
	List all Subjects [GET] or create a new Branch
	"""

	# return the list of subjects
	queryset = Branch.objects.all()
	serializer_class = BranchSerializer
	pagination_class = ResultsSetPagination

	
	def post(self, request, format=None):
		serializer = BranchSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BranchDetail(APIView):
	"""
	Retrieve, update or delete a Branch instance.
	"""
	def get_object(self, pk):
		try:
			return Branch.objects.get(pk=pk)
		except Branch.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None):
		branch = self.get_object(pk)
		serializer = BranchSerializer(branch)
		return Response(serializer.data)
	
	def put(self, request, pk, format=None):
		branch = self.get_object(pk)
		serializer = BranchSerializer(branch, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
		branch = self.get_object(pk)
		branch.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)



""" Course """
class CourseList(ListAPIView):
	"""
	List all Subjects [GET] or create a new Course
	"""

	# return the list of subjects
	queryset = Course.objects.all()
	serializer_class = CourseSerializer
	pagination_class = ResultsSetPagination

	
	def post(self, request, format=None):
		serializer = CourseSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CourseDetail(APIView):
	"""
	Retrieve, update or delete a Course instance.
	"""
	def get_object(self, pk):
		try:
			return Course.objects.get(pk=pk)
		except Course.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None):
		course = self.get_object(pk)
		serializer = CourseSerializer(course)
		return Response(serializer.data)
	
	def put(self, request, pk, format=None):
		course = self.get_object(pk)
		serializer = CourseSerializer(course, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
		course = self.get_object(pk)
		course.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)


"""  Textbook  """		

class TextbookList(ListAPIView):
	"""
	List all Textbooks [GET] or create a new Textbook.
	"""
	queryset = Textbook.objects.all()
	serializer_class = TextbookSerializer
	pagination_class = ResultsSetPagination

	# def get(self, request, format=None):
		# textbooks = Textbook.objects.all()
		# serializer = TextbookSerializer(textbooks, many=True)
		# return Response(serializer.data)

	def post(self, request, format=None):
		serializer = TextbookSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class TextbookDetail(APIView):
	"""
	Retrieve, update or delete a snippet instance.
	"""
	def get_object(self, pk):
		try:
			return Textbook.objects.get(pk=pk)
		except Textbook.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None):
		textbook = self.get_object(pk)
		serializer = TextbookSerializer(textbook)
		return Response(serializer.data)
	
	def put(self, request, pk, format=None):
		textbook = self.get_object(pk)
		serializer = TextbookSerializer(textbook, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
		textbook = self.get_object(pk)
		textbook.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

	

	