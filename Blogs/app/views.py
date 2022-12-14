from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import BlogSerializer
from .models import Blog
from .producer import publish
# Create your views here.

class BlogView(APIView):
    def get(self,request):
        id = request.query_params.get('id')
        if id is not None:
            blog = Blog.objects.get(id=id)
            serializer = BlogSerializer(blog)
            return Response(serializer.data)
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            publish('blog_created', serializer.data)
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def put(self,request):
        id = request.query_params.get('id')
        blog = Blog.objects.get(id=id)
        serializer = BlogSerializer(blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            publish('blog_updated', serializer.data)
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
        
    def delete(self,request):
        id = request.query_params.get('id')
        blog = Blog.objects.get(id=id)
        blog.delete()
        publish('blog_deleted', id)
        return Response(status=204)
        
    def patch(self,request):
        id = request.query_params.get('id')
        blog = Blog.objects.get(id=id)
        serializer = BlogSerializer(blog, data=request.data, partial=True)    
        if serializer.is_valid():
            serializer.save()
            publish('blog_updated', serializer.data)
            return Response(serializer.data)
        return Response(serializer.errors, status=400)