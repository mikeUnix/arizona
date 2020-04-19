from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.views.generic import View
from .models import Post, Tag
from .utils import*
from .forms import TagForm , PostForm



# Create your views here.

def posts_list(request):
	posts = Post.objects.all()
	return render(request,'Arizona/index.html',context={'posts':posts})



class PostDetail(ObjectDetailMixin, View):
	model = Post
	template = 'Arizona/post_detail.html'
	

class PostCreate(ObjectCreateMixin,View):
	model_form = PostForm
	template = 'Arizona/post_create_form.html'

class PostUpdate(ObjectUpdateMixin, View):
	model = Post
	model_form = PostForm
	template = 'Arizona/post_update_form.html'




class TagDetail(ObjectDetailMixin, View):
	model = Tag
	template = 'Arizona/tag_detail.html'


class TagCreate(ObjectCreateMixin,View):
	model_form = TagForm
	template = 'Arizona/tag_create.html'


class TagUpdate(ObjectUpdateMixin, View):

	model = Tag 
	model_form = TagForm
	template = 'Arizona/tag_update_form.html'
#	def get(self,request,slug):
#		tag = Tag.objects.get(slug__iexact=slug) #slug__iexact
#		bound_form = TagForm(instance=tag) 
#		return render(request, 'Arizona/tag_update_form.html', context={'form': bound_form, 'tag': tag})
#
#	def post(self,request,slug):
#		tag = Tag.objects.get(slug__iexact=slug) #slug__iexact
#		bound_form = TagForm(request.POST,instance=tag)
#
#		if bound_form.is_valid():
#			new_tag = bound_form.save()
#			return redirect(new_tag)
#		return render(request, 'Arizona/tag_update_form', context={'form': bound_form, 'tag': tag})



def tags_list(request):
	tags = Tag.objects.all()
	return render(request,'Arizona/tags_list.html',context={'tags':tags})