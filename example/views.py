from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, generics
from rest_framework import status

from example.models import *
from example.serializers import *


class Courses(APIView):
  
  def get(self, request):
    coursess = Course.objects.all()
    serializerss = CourseSerializers(coursess, many=True)
    return Response(serializerss.data)

  def post(self, request):
    serializer = CourseSerializers(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CoursesId(APIView):

  def get_object(self, pk):
    return Course.objects.get(pk=pk)

  def get(self, request, pk):
    courses = self.get_object(pk)
    serializers = CourseSerializers(courses)
    return Response(serializers.data)

  def delete(self, request, pk):
    serializer = self.get_object(pk)
    serializer.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
  