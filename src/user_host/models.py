from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy


class Host(models.Model):
    class Resource(models.TextChoices):
        wait = 0, gettext_lazy('Windows')
        works = 1, gettext_lazy('Unix')
        done = 2, gettext_lazy('SQL')

    ip_address = models.CharField(max_length=150, verbose_name='IP адрес')
    port = models.IntegerField(verbose_name='Порт')
    type_of_resource = models.CharField(
        max_length=2,
        choices=Resource.choices,
        default=Resource.wait,
        verbose_name='Тип ресурса',
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Owner', verbose_name='Владелец')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def __str__(self):
        return f"{self.author} | {self.ip_address} | {self.port}"

    def get_absolute_url(self):
        return reverse('view_host', kwargs={'pk': self.pk})
