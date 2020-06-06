from django.db import models

class TodoModel(models.Model):
	todo_description = models.CharField(max_length = 300)
	todo_created_date = models.DateTimeField(auto_now_add=True)
	todo_modified_date = models.DateTimeField(auto_now=True)

class UserModel(models.Model):
	user_id = models.CharField(max_length = 10)
	email = models.CharField(max_length = 40)
	first_name = models.CharField(max_length = 20)
	last_name = models.CharField(max_length = 20)
	gender = models.CharField(max_length = 15)
	phone_number = models.CharField(max_length = 10)
	dob = models.DateField()