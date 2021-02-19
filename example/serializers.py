from rest_framework import serializers
from example.models import Course, Contact, Branch, Category


class ContactSerializers(serializers.ModelSerializer):
  class Meta:
    model = Contact
    fields = ("name", "value")


class BranchSerializers(serializers.ModelSerializer):
  class Meta:
    model = Branch
    fields = ("latitude", "longitude", "address")


class CourseSerializers(serializers.ModelSerializer):
  # contact = ContactSerializers(many=True, read_only=True)
  # branch = BranchSerializers(many=True, read_only=True)
  category = serializers.PrimaryKeyRelatedField(queryset = Category.objects.all())

  class Meta:
    model = Course
    fields = ("name", "description", "category", "logo", "contacts", "branches")

  def to_representation(self, instance):
    data = super().to_representation(instance)
    data['contacts'] = ContactSerializers(
      Contact.objects.get(pk=data['contacts'])).data
    data['branches'] = BranchSerializers(
      Branch.objects.get(pk=data['branches'])).data
    return data