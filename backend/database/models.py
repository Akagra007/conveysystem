from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Customer(models.Model):

	user = models.OneToOneField(User)
	customer_id=models.IntegerField()
	customer_street=models.CharField()
	customer_phone=models.IntegerField()
	customer_city=models.CharField()
	customer_zip_code=models.IntegerField()

	def __str__(self):
		self.customer_id

class Order(models.Model):

	order_id=models.IntegerField()
	customer_id=models.IntegerField()
	to_state=models.CharField()
	to_city=models.CharField()
	to_zip_code=models.IntegerField()
	address=models.CharField()

	def __str__(self):
		self.order_id

class Product(models.Model):
	product_id=models.IntegerField()
	product_name=models.CharField()
	product_price=models.IntegerField()

	def __str__(self):
		self.product_id
