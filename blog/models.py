from django.db import models

class Post(models.Model): #creating subclass of models.Model called Post,using this subclass functionality we have access to everything within django.models.Model
	title = models.CharField(max_length = 200)
	author = models.ForeignKey( #For author, we use many-one relationship
		'auth.user',
		on_delete=models.CASCADE,
		)
	body = models.TextField()

	def __str__(self):
		return self.title