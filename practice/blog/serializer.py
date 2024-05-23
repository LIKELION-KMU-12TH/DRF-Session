<<<<<<< HEAD
=======
# serializer.py

>>>>>>> 7b4a247334409ecc4f201fd6c81ff925389d25b6
from .models import Blog
from rest_framework import serializers

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
<<<<<<< HEAD
        fields = '__all__'
=======
        fields = '__all__'

>>>>>>> 7b4a247334409ecc4f201fd6c81ff925389d25b6
