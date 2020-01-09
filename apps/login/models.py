from __future__ import unicode_literals
from django.db import models

class UserManager(models.Manager):
	def validation(self, form_data):
		errors = []
		if len(form_data['name']) == 0:
			errors.append("Name is Required.")
		if len(form_data['name']) < 2:
			erros.append('Name must be longer.')
		if not errors:
			user = User.objects.filter(name=form_data['name'])
			if user:
				errors.append('User Already Exists.')

	def create_user(self, form_data):
		
		return User.objects.create(
            name = form_data['name'],
            username = form_data['username'],
    )


# Create your models here.
class User(models.Model):
	name = models.CharField(max_length=255)
	username = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	objects = UserManager()

	def __str__(self):
		return "{}".format(self.name)























