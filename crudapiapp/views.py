from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view


#For READ operation using GET
@csrf_exempt
@api_view(['GET'])
def student_api(request):
    if request.method == 'GET':
        id = request.GET.get('id', None)
        if id is not None:
            try:
                stu = Student.objects.get(id=id)
                serializer = StudentSerializer(stu)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except Student.DoesNotExist:
                return Response({"error": "Student not found"}, status=404)

        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

 
    return Response({"error": "Unsupported HTTP method"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


#For CREATE operation using POST
@api_view(['POST'])
def create_student(request):
    if request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()   
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    return Response({"error": "Unsupported HTTP method"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        
        
#For PUT and PATCH operation
@api_view(['PUT', 'PATCH'])
def update_student(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = StudentSerializer(student, data=request.data)
    elif request.method == 'PATCH':
        serializer = StudentSerializer(student, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#For DELETE operation
@api_view(['DELETE'])
def delete_student(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)

    student.delete()   

    return Response({"message": "Student deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
