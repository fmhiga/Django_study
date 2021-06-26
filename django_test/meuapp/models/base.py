from django.db import models

# criado para definições genericas
class Basemodel(models.Model):
    class Meta:
        abstract = True
        app_label = 'meuapp'