import enum

from django.db import models


class Entity(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Category(models.Model):
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.description


class Bank(models.Model):
    code = models.CharField(max_length=5)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.description


class DepositAccount(models.Model):

    class DepositAccountTypes(enum.Enum):
        current_account = 'cur'
        money = 'mon'
        investment = 'inv'

    entity = models.ForeignKey('Entity', on_delete=models.CASCADE)
    type = models.CharField(max_length=15, choices=[
        (DepositAccountTypes.current_account.value, 'Current Account'),
        (DepositAccountTypes.money.value, 'Money'),
        (DepositAccountTypes.investment.value, 'Investment'),
    ])
    bank = models.ForeignKey('Bank', on_delete=models.CASCADE, null=True)
    agency_number = models.CharField(max_length=30, null=True)
    agency_digit = models.CharField(max_length=2, null=True)
    account_number = models.CharField(max_length=30, null=True)
    account_digit = models.CharField(max_length=2, null=True)

    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class People(models.Model):
    customer = models.BooleanField(default=False)
    supplier = models.BooleanField(default=False)
    name = models.CharField(max_length=30)

    def is_customer(self):
        return self.customer

    def is_supplier(self):
        return self.supplier

    def __str__(self):
        return self.name


class ClassificationCenter(models.Model):
    entity = models.ForeignKey('Entity', on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    cost_center = models.BooleanField(default=False)
    revenue_center = models.BooleanField(default=False)

    def is_cost_center(self):
        return self.cost_center

    def is_revenue_center(self):
        return self.revenue_center

    def __str__(self):
        return self.name
