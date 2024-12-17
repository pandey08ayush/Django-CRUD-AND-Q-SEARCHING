from django.db import models
from myapp.utils import generateSlug

# Create your models here.
class College(models.Model):
  college_address = models.CharField(max_length=100)
  college_name = models.CharField(max_length=100)

class Student(models.Model):
  college = models.ForeignKey(College,on_delete=models.CASCADE,null=True,blank=True)
  name = models.CharField(max_length=100)
  mobile_number = models.CharField(max_length=12)
  age = models.IntegerField(null=True , blank=True)

class Brand (models.Model):
  brand_name = models.CharField(max_length=100)
  country = models.CharField(default="IN",max_length=100)

class Product(models.Model):
  brand=models.ForeignKey(Brand,on_delete=models.CASCADE,null=True,blank=True)
  product_name = models.CharField(max_length=100)
  slug = models.SlugField(max_length=100, null=True, blank=True)

  def save(self, *args, **kwargs)->None:
    if not self.id:
      self.slug = generateSlug(self.product_name,Product)
    return super().save(*args,**kwargs)
  
class Person(models.Model):
    person_name = models.CharField(max_length=1000)


class Store(models.Model):
  bmp_id = models.CharField(unique=True, max_length=100)
  store_name = models.CharField(max_length=100)
  