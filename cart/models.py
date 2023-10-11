from django.db import models
from django.utils.translation import gettext as _


class Order(models.Model):
    first_name = models.CharField(_('first name'), max_length=50)
    last_name = models.CharField(_('last name'), max_length=50)
    email = models.EmailField(_('mail'),)
    address = models.CharField(_('adress'), max_length=150)
    date = models.DateField(_('delivery date'))
    number = models.BigIntegerField(_('phone number'), blank=True, null=True)
    comments = models.CharField(_('comment'), max_length=100, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created', )

    def __str__(self):
        return f"{self.first_name}-{self.last_name}"

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"