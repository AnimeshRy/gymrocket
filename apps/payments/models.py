from django.db import models
from apps.members.models import Member


class Payments(models.Model):
    """ Payment Model associated with Member Model generated on member creation or updation """
    user = models.ForeignKey(Member, on_delete=models.CASCADE)
    payment_date = models.DateField()
    payment_period = models.IntegerField()
    payment_amount = models.IntegerField()
