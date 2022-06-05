from email import message
from os import stat, stat_result
from turtle import st
from warnings import catch_warnings
from django.shortcuts import render
from django.views import View
from rest_framework.response import Response
from rest_framework.decorators import api_view,renderer_classes
from rest_framework.views import APIView
from rest_framework import status

import api.extern as extern
from api.models import Post
from api.serializers import serializePosts
from api.utils import checkInputData
# Create your views here.

@api_view(['GET'])
def findPost(req):
    userID =  req.query_params.get('userId')
    postID = req.query_params.get('id')
    many = False
    concate = None
    if not userID and not postID:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    try:
        posts = Post.objects
        if userID:
            posts = posts.filter(userId=userID)
        if postID:
            posts = posts.filter(id=postID)
        many = posts.count() > 1
        if(posts.count() == 0):
            raise Exception('No record locally')
        print('got from local database')
        concate = extern.getPost(userID,None)

    except:
        try:
            posts = extern.getPost(userID,postID)
        except Exception as e:
            return Response({'message': e.__str__()},status=status.HTTP_404_NOT_FOUND)
        if (not userID and postID):
            Post(posts).save()
        if (userID and not postID):
            many = True
        print('got from extern database')
    return Response(serializePosts(posts,many=many,concate=concate))


class modifyPost(APIView):
    def post(self,req):
        body = req.data
        try:
            checkInputData(body,(('userId',int,True),('title',str,True),('body',str,True)))
        except Exception as e:
            return Response({'message' : e.__str__()},status=status.HTTP_406_NOT_ACCEPTABLE)
        if(not extern.validateId(body['userId'])):
            return Response(status=status.HTTP_401_UNAUTHORIZED)
                
        obj = Post(userId=body['userId'],title=body['title'],body=body['body'])
        obj.save()
        return Response(serializePosts(obj), status=status.HTTP_201_CREATED)


    def patch(self,req):
        body = req.data
        obj = None

        try: # check if body contains all the reuquired fields and are formated right
            checkInputData(body)
        except Exception as e:
            return Response({'message' : e.__str__()},status=status.HTTP_406_NOT_ACCEPTABLE)

        try:
            obj = Post.objects.filter(id=body['id'])
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        objects = Post.objects.filter(id=body['id'],userId=body['userId'])
        if(objects.count() == 0):
            return Response(status=status.HTTP_409_CONFLICT)
        
        if ('title' in body):
            objects.update(title=body['title'])
        if('body' in body):
            objects.update(body=body['body'])

        return Response(serializePosts(objects),status=status.HTTP_200_OK)


    def delete(self,req):
        userID =  req.query_params.get('userId')
        postID = req.query_params.get('id')
        if not userID or not postID: 
            return Response(status=status.HTTP_400_BAD_REQUEST)
        objects = Post.objects.filter(id=postID,userId=userID)
        if(objects.count() == 0):
            return Response(status=status.HTTP_409_CONFLICT)
        objects.delete()
        return Response(status=status.HTTP_200_OK)
    
