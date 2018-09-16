from django.db import models
import datetime

# Create your models here.


class Categories(models.Model):
	name = models.CharField(max_length=20)

	def __str__(self):
		return self.name;


class Posts(models.Model):
	categorie = models.ForeignKey(Categories,on_delete=models.CASCADE)
	title = models.CharField(max_length=20)
	content = models.CharField(max_length=1000)
	#image = models.ImageField(upload_to=,blank=True,null=True)
	create_at = models.DateField("Date", default=datetime.date.today)
	updated_at = models.DateField("Date", default=datetime.date.today)
	aproved = models.BooleanField(default=True)
	tags = models.CharField()

	def __str__(self):
		return self.title


class Comments(models.Model):
	post = models.ForeignKey(Posts,on_delete=models.CASCADE)
	name = models.CharField(max_length=20)
	content = models.CharField(max_length=200)
	create_at = models.DateField("Date", default=datetime.date.today)
	updated_at = models.DateField("Date", default=datetime.date.today)
	aproved = models.BooleanField(default=True)

	def __str__(self):
		return self.name

