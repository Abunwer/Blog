from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Posts
# Create your views here.


class HomeView(TemplateView):
	template_name = "index.html"

	def get(self,request):
		posts = Posts.objects.all()
		return render(request,self.template_name,{'posts':posts})

class AboutView(TemplateView):
	template_name = "about.html"

class ContactView(TemplateView):
	template_name = "contact.html"

class PostView(TemplateView):
	template_name = "post.html"

	def get(self,request,post_id):
		post = Posts.objects.get(pk=post_id)
		return render(request,self.template_name,{'post':post})