from datetime import datetime

from rest_framework import generics
from rest_framework import serializers

from students.models import Students


class StudentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Students
        fields = "__all__"
        extra_kwargs = {
            "id": {"read_only": True},
            "name": {"required": True},
            "birthday": {"required": True},
        }


class StudentsView(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StudentsSerializer
    queryset = Students.objects.filter(deleted_at__isnull=True)


class StudentInfoView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StudentsSerializer

    def get_object(self):
        return Students.objects.filter(deleted_at__isnull=True, id=self.kwargs['pk']).first()

    def perform_destroy(self, instance):
        instance.delete_at = datetime.now()
        instance.save()
