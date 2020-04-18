from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.views.generic import View
from .models import Post, Tag
from .utils import ObjectDetailMixin
from .forms import TagForm , PostForm



# Create your views here.

def posts_list(request):
	posts = Post.objects.all()
	return render(request,'Arizona/index.html',context={'posts':posts})



def tags_list(request):
	tags = Tag.objects.all()
	return render(request,'Arizona/tags_list.html',context={'tags':tags})



class PostDetail(ObjectDetailMixin, View):
	model = Post
	template = 'Arizona/post_detail.html'
	

class PostCreate(View):
	def  get(self,request):
		form = PostForm()
		return render (request, 'Arizona/post_create_form.html', context={'form':form})

	def post (self, request):
		bound_form = PostForm(request.POST)
		if bound_form.is_valid():
			new_post = bound_form.save()
			return redirect(new_post)
		return render(request, 'Arizona/post_create_form.html', context={'form': bound_form})
			

class TagDetail(ObjectDetailMixin, View):
	model = Tag
	template = 'Arizona/tag_detail.html'


class TagCreate(View):
	def get(self, request):
		form = TagForm()
		return render(request, 'Arizona/tag_create.html', context={'form': form})

	def post(self,request):
		bound_form = TagForm(request.POST)

		if bound_form.is_valid():
			new_tag = bound_form.save()
			return redirect(new_tag)
		return render(request, 'Arizona/tag_create.html',context={'form': bound_form})
		


		

