from django.db import models

# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=50)
    website = models.URLField()

class Author(models.Model):
    salutation = models.CharField(max_length=10)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    #headshot = models.ImageField(upload_to='/tmp')

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField()

class test(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    def __str__(self):
        return self.username
		
class User(models.Model):
	username = models.CharField(max_length=64)
	password = models.CharField(max_length=256)
	def __str__(self):
		return self.username

class Answer(models.Model):
	user = models.ForeignKey(User)
	date = models.DateField()
	content = models.TextField()
	def __str__(self):
		return self.content
		
class Question(models.Model):
	title = models.CharField(max_length=64)
	date = models.DateField()
	content = models.TextField()
	answer = models.ManyToManyField(Answer)
	def __str__(self):
		return self.title
	

