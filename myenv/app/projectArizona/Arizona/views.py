from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import View
from .models import Post, Tag
from .utils import*
from .forms import TagForm , PostForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.db.models import Q


# Create your views here.

def posts_list(request):
	search_query = request.GET.get('search','')
	if search_query:
		posts = Post.objects.filter(Q(title__icontains=search_query) or Q(body__icontains=search_query))
	else:
		posts = Post.objects.all()
	
	paginator = Paginator(posts, 10)

	

	page_number = request.GET.get('page',1)
	page = paginator.get_page(page_number)
	is_paginated = page.has_other_pages()
	if page.has_previous():
		prev_url = '?page={}'.format(page.previous_page_number())
	else:
		prev_url = ''
	
	if page.has_next():
		next_url = '?page={}'.format(page.next_page_number())
	else:
		next_url = ''

	context = {
	'page_object': page,
	'is_paginated': is_paginated,
	'next_url': next_url,
	'prev_url': prev_url

	}




	#http://127.0.0.1:8000/Arizona/?page=2
	return render(request,'Arizona/index.html',context=context)



class PostDetail(ObjectDetailMixin, View):
	model = Post
	template = 'Arizona/post_detail.html'
	

class PostCreate(LoginRequiredMixin, ObjectCreateMixin, View):
	model_form = PostForm
	template = 'Arizona/post_create_form.html'
	raise_exeption = False

class PostUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
	model = Post
	model_form = PostForm
	template = 'Arizona/post_update_form.html'
	raise_exeption = False

class PostDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
	model = Post
	template = 'Arizona/post_delete_form.html'
	redirect_url = 'posts_list_url'
	raise_exeption = False




class TagDetail(ObjectDetailMixin, View):
	model = Tag
	template = 'Arizona/tag_detail.html'


class TagCreate(LoginRequiredMixin, ObjectCreateMixin,View):
	model_form = TagForm
	template = 'Arizona/tag_create.html'
	raise_exeption = False


class TagUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):

	model = Tag 
	model_form = TagForm
	template = 'Arizona/tag_update_form.html'
	raise_exeption = False

class TagDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
	model = Tag
	template = 'Arizona/tag_delete_form.html'
	redirect_url = 'tags_list_url'
	raise_exeption = False

	
def tags_list(request):
	tags = Tag.objects.all()
	return render(request,'Arizona/tags_list.html',context={'tags':tags})