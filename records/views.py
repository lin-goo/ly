from datetime import datetime

from rest_framework import generics
from rest_framework import serializers
from records.models import Records


class RecordsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Records
        fields = "__all__"
        extra_kwargs = {
            "id": {"read_only": True},
            "user_id": {"required": True},
            "category_type": {"required": True},
            "category_content": {"required": True},
        }


class RecordsView(generics.ListCreateAPIView):
    serializer_class = RecordsSerializer
    queryset = Records.objects.filter(deleted_at__isnull=True)


class RecordInfoView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RecordsSerializer

    def get_object(self):
        return Records.objects.filter(deleted_at__isnull=True, id=self.kwargs['pk']).first()

    def perform_destroy(self, instance):
        instance.delete_at = datetime.now()
        instance.save()
