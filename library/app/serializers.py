from rest_framework import serializers  
from .models import AdminUser, Books

class AdminUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminUser
        fields = [
            'email',
            'username'
        ]
    
class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = [
            'id',
            'title',
            'author',
            'isbn',
            'publish_date',
            'added_by',
        ]