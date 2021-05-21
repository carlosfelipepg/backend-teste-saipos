from rest_framework import serializers
from main.models import Tarefas


class TarefasSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()

    class Meta:
        model = Tarefas
        fields = '__all__'

    def get_status(self, obj):
        if not obj.status:
            return 'Pendente'
        return 'Finalizada'
