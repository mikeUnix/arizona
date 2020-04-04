from django.shortcuts import render


# Create your views here.

def post_list(request):
	a=['KotVasya','Koshka','Murka','Shalashovka']
	return render(request,'Arizona/index.html',context={'names':a})
