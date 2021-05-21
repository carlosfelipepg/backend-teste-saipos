import requests
import json

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from main.serializers import TarefasSerializer
from main.models import Tarefas


class TarefasViewSet(viewsets.ModelViewSet):
    queryset = Tarefas.objects.all()
    serializer_class = TarefasSerializer

    def create(self, request, *args, **kwargs):
        data = request.data

        url = f"http://apilayer.net/api/check?access_key=66a89d3a056eb4dc7a023a7c507e8a77&email={data['email']}"
        response = requests.request("GET", url)
        result = json.loads(response.text)

        if not result['format_valid']:
            return Response({'message': f'E-mail invalído, segue o e-mail endicado {result["did_you_mean"]}'})
        Tarefas.objects.create(**data)
        return Response({'message': 'Tarefa criada com sucesso'})

    @action(methods=['POST'], detail=False)
    def listar_tarefas(self, request):
        status = request.data['status']
        tarefas = Tarefas.objects.filter(status=status)
        data = TarefasSerializer(tarefas, many=True).data
        return Response(data)

    @action(methods=['POST'], detail=False)
    def mudar_status(self, request):
        status = request.data['status']
        id = request.data['id']
        senha = request.data.get('senha', None)
        tarefa = Tarefas.objects.get(id=id)
        if tarefa.status and not status and senha != 'TrabalheNaSaipos':
            return Response({'message': 'Senha não informada ou incorreta'})
        if tarefa.status_change_count == 2 and not status:
            return Response({'message': 'Tarefa já marcada como pendente duas vezes'})
        if not status:
            tarefa.status_change_count += 1
        tarefa.status = status
        tarefa.save()
        return Response({'message': 'Tarefa atualizada com sucesso'})

    @action(methods=['GET'], detail=False)
    def sem_tarefas(self, request):
        responsavel = 'eu'
        email = 'eu@me.com'
        url = "https://cat-fact.herokuapp.com/facts/random?animal_type=cat&amount=3"
        response = requests.request("GET", url)
        result = json.loads(response.text)
        for obj in result:
            Tarefas.objects.create(responsavel=responsavel, email=email, descricao=obj['text'])
        return Response({'message': 'Tarefas criadas com sucesso'})
