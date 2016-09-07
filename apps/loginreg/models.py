from __future__ import unicode_literals
from django.db import models
import re
EMAIL_REGEX=re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
number_check = re.compile(r'^[a-zA-Z ]+$')
import bcrypt
from datetime import datetime, date
# Create your models here.

class UserManager(models.Manager):
	def register(self, data):
		errors=[]
		if not len(data['name']) > 2 or not number_check.match(data['name']): 
			errors.append("Name must be no fewer than 3 characters & contain letters and spaces only")
		if not len(data['alias']) > 1: 
			errors.append("Alias must be no fewer than 2 characters")
		if not EMAIL_REGEX.match(data['email']) or not len(data['email']) > 1:
			errors.append("Your email is invalid")	
		if not len(data['password']) > 7:
			errors.append("Password should be at least 8 characters")
		if not data['password'] == data['confirm_password']:
			errors.append("Passwords must match")
		if data['birthday'] == "" or datetime.strptime(data['birthday'], '%Y-%m-%d') > datetime.now():
			errors.append("Birthday is invalid")
		try:
			user = User.objects.filter(email=data['email'])
			if user:
				errors.append("User already exists")	
			user_password = user.password.encode()
			if not bcrypt.hashpw(password, user_password) == user_password:
				errors.append("Password or Username does not match record")
		except:
			pass
		if not errors:
			password = data['password'].encode()
			hashed = bcrypt.hashpw(password, bcrypt.gensalt())
			user = User.objects.create(name=data['name'], alias=data['alias'], email=data['email'], password=hashed, birthday=data['birthday'])
			return(True, user)
		return(False, errors)
	def login(self, data):
		try:
			user = User.objects.get(email = data['email'])
		except:
			return(False, "User does not exist")
		password = data['password'].encode()
		user_password = user.password.encode()
		if not user or not password or not bcrypt.hashpw(password, user_password) == user_password:
			return(False, "Password does not match record")
		else:
			return(True, user)

class User(models.Model):
	name = models.CharField(max_length=45)
	alias = models.CharField(max_length=45)
	email = models.CharField(max_length=100)
	password = models.CharField(max_length=100)
	birthday = models.DateField()
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	userManager = UserManager()
	objects = models.Manager()