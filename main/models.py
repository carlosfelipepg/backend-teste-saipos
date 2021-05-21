from django.db import models
from django.utils import timezone


class Tarefas(models.Model):
    id = models.AutoField(primary_key=True)
    responsavel = models.CharField(max_length=180, blank=True, null=True)
    email = models.CharField(max_length=180, blank=True, null=True)
    descricao = models.CharField(max_length=255, blank=True, null=True)
    status = models.BooleanField(default=0)
    status_change_count = models.IntegerField(default=0)
    data_criacao = models.DateField(default=timezone.now, blank=True, null=True)

    class Meta:
        verbose_name = 'Tarefa'
        verbose_name_plural = 'Tarefas'
