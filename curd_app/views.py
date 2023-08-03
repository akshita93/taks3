from rest_framework .views import APIView
from rest_framework.response import Response
from .models import Project
from .serializers import ProjectModelSerializers
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
import logging

logger = logging.getLogger("django")


class ProjectAPI(APIView):

    authentication_classes = [JWTAuthentication]
    permissions_classes = [IsAuthenticated]


    def get(self,request):
        project =  Project.objects.all()
        serializers = ProjectModelSerializers(project, many=True)
        logger.info("All record fetched")
        return Response(data=serializers.data, status=status.HTTP_200_OK)
    

    def post(self,request):
        serializer = ProjectModelSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info("Project created successfully")
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ProjectDetailsAPI(APIView):

    authentication_classes = [JWTAuthentication]
    permissions_classes = [IsAuthenticated]

    def get(self,request, pk=None):
        obj = get_object_or_404(Project, pk=pk)
        serializer = ProjectModelSerializers(obj)
        logger.info("Project record fetched")
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    def put(self,request, pk=None):
        obj = get_object_or_404(Project, pk=pk)
        serializer = ProjectModelSerializers(data=request.data, instance=obj)
        if serializer.is_valid():
            serializer.save()
            logger.info("project update successfully")
            return Response(data=serializer.data,status=status.HTTP_205_RESET_CONTENT)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk=None):
        obj = get_object_or_404(Project, pk=pk)
        serializer = ProjectModelSerializers(data=request.data, instance=obj, partial = True)
        if serializer.is_valid():
            serializer.save()
            logger.info("Record partial update successfully")
            return Response(data=serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def delete(self, request, pk=None):
        obj= get_object_or_404(Project, pk=pk)
        obj.delete()
        logger.info("Record is deleted")
        return Response(data=None, status=status.HTTP_204_NO_CONTENT)


    

