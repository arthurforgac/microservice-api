from rest_framework import viewsets, status
from .models import Post
from .serializers import PostSerializer
from rest_framework.response import Response
import requests


class PostViewSet(viewsets.ViewSet):
    def list(self, request):  # /api/posts/  GET
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response({"posts": serializer.data})


    def create(self, request):  # /api/posts/  POST
        users = requests.get("https://jsonplaceholder.typicode.com/users").json()
        if request.data["userid"] not in [user["id"] for user in users]:
            return Response(status=status.HTTP_403_FORBIDDEN)
        data_with_id = dict({"id": Post.objects.latest('id').id + 1}, **request.data)
        serializer = PostSerializer(data=data_with_id)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


    def retrieve_by_id(self, request, pk=None):  # /api/posts/<str:id>  GET
        try:
            post = Post.objects.get(id=pk)
        except:
            posts = requests.get("https://jsonplaceholder.typicode.com/posts").json()
            try:
                for i, post in enumerate(posts):
                    if int(post["id"]) == int(pk):
                        post_raw = post
                        break
                else:
                    raise LookupError

                post = {}
                for attr in post_raw:
                    if hasattr(Post, attr.lower()):
                        post[attr.lower()] = post_raw[attr]

                serializer = PostSerializer(data=post)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                return Response(serializer.data)
            except LookupError:
                return Response(status=status.HTTP_204_NO_CONTENT)
        serializer = PostSerializer(post)
        return Response(serializer.data)


    def update(self, request, pk=None):  # /api/posts/<str:id>  PUT
        ids = [post.id for post in Post.objects.all()]
        if int(pk) not in ids:
            return Response(status=status.HTTP_204_NO_CONTENT)
        post = Post.objects.get(id=pk)
        serializer = PostSerializer(instance=post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)


    def destroy(self, request, pk=None):  # /api/posts/<str:id>  DELETE
        post = Post.objects.get(id=pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserViewSet(viewsets.ViewSet):
    def retrieve_by_userid(self, request, pk=None):  # /api/user/<str:id>
        posts = Post.objects.filter(userid=pk)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)


