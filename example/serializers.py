from rest_framework import serializers
from example.models import Course, Contact, Branch, Category


# class CategorySerializer(serializers.ModelSerializer):

#   class Meta:
#     model = Category
#     fields = '__all__'


class ContactSerializers(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ("name", "value")


class BranchSerializers(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ("latitude", "longitude", "address")


class CourseSerializers(serializers.ModelSerializer):
    contacts = ContactSerializers(many=False)
    branches = BranchSerializers(many=False)
    # category = CategorySerializer(many=False)
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())

    class Meta:
        model = Course
        fields = ("name", "description", "category", "logo", "contacts", "branches",)

    def create(self, validated_data):
        branches = validated_data.pop('branches')
        contacts = validated_data.pop('contacts')
        # category = validated_data.pop('category')
        contact = Contact.objects.create(
            **contacts)  # создание контакта с данными полученного из validated_data **распаковка
        branch = Branch.objects.create(**branches)  # создание branch с данными полученного из validated_data
        # category = Category.objects.create(**category) # создание категории с данными полученного из validated_data
        course = Course.objects.create(branches=branch, contacts=contact, **validated_data)  # (category = category, branches=branch, contacts=contact, **validated_data)
        return course
