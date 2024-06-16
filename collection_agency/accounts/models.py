from django.db import models


class Account(models.Model):
  client_ref_no = models.CharField(max_length=255)
  balance = models.DecimalField(max_digits=10, decimal_places=2)
  status = models.CharField(max_length=50)
  consumer_name = models.CharField(max_length=255)
  consumer_address = models.CharField(max_length=255)
  ssn = models.CharField(max_length=20)

  def __str__(self):
    return f'{self.client_ref_no} - {self.balance} - {self.status} - {self.consumer_name} - {self.consumer_address} - {self.ssn} '
