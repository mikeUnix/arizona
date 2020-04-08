from django.shortcuts import render
from django.views.generic import View
from .models import Post, Tag

# Create your views here.

def posts_list(request):
	posts = Post.objects.all()
	return render(request,'Arizona/index.html',context={'posts':posts})


#def post_detail(request,slug):
#	post = Post.objects.get(slug__iexact=slug)
#	return render(request, 'Arizona/post_detail.html',context={'post':post})
#######
def tags_list(request):
	tags = Tag.objects.all()
	return render(request,'Arizona/tags_list.html',context={'tags':tags})

#def tag_detail(request,slug):
#	tag = Tag.objects.get(slug__iexact=slug)
#	return render(request, 'Arizona/tag_detail.html', context={'tag':tag})

class PostDetail(View):
	def get(self,reqest,slug):
		post = Post.objects.get(slug__iexact=slug)
		return render(request, 'Arizona/post_detail.html',context={'post':post})

class TagDetail(View):
	def get(self,request,slug):
		tag = Tag.objects.get(slug__iexact=slug)
		return render(request, 'Arizona/tag_detail.html', context={'tag':tag})


		

