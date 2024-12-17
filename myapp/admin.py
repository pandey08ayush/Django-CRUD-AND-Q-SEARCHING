
# Register your models here.
from django.contrib import admin
from myapp.models import Brand,Product,Person,Student,Store
from django import forms

# admin.site.register(Brand)
# admin.site.register(Product)
# admin.site.register(Person)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
  pass
  list_display=(
    "name",
    "college",
    "mobile_number",
    "age"
  )
  search_fields = ("name","mobile_number")
  readonly_fields=("mobile_number",)

