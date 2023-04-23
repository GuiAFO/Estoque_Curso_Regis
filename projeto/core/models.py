from django.db import models

#Atualiza a data somente quando algo for criado
class TimeStampedModel(models.Model):
    created = models.DateTimeField(
        'criado em',
        auto_now_add=True,
        auto_now=False
    )
#Atualiza data e hora quando algo for modificado
    modified = models.DateTimeField(
        'modificado em',
        auto_now_add=False,
        auto_now=True
    )
#Herança de classe para outros models
    class Meta:
        abstract = True
