from django.contrib import admin

# Register your models here.
from example.models import *

class CourseAdmin(admin.ModelAdmin):
  list_display = ("name", "description", "category", "logo", "contacts", "branches")

class CategoryAdmin(admin.ModelAdmin):
  list_display = ("name", "imgpath")

class BranchAdmin(admin.ModelAdmin):
  list_display = ("address", "latitude", "longitude")

class ContactAdmin(admin.ModelAdmin):
  list_display = ("name", "value")
  

admin.site.register(Course, CourseAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Branch, BranchAdmin)
admin.site.register(Contact, ContactAdmin)


 