from django.urls import path
from .views import *


urlpatterns = [
	path('',HomeView.as_view()),
	path('about',AboutView.as_view()),
	path('post/<int:post_id>',PostView.as_view(),name='post'),
	path('contact',ContactView.as_view()),
]