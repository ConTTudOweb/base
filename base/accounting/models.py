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
    code = models.CharField(max_length=5, unique=True)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.description


class DepositAccount(models.Model):

    class DepositAccountTypes(enum.Enum):
        current_account = 'cur'
        money = 'mon'
        investment = 'inv'

    entity = models.ForeignKey('Entity', on_delete=models.CASCADE)
    type = models.CharField(max_length=3, choices=[
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


class Account(models.Model):
    class AccountTypes(enum.Enum):
        normal = 'nor'
        recurrent = 'rec'
        parcelled = 'par'

    class AccountFrequencys(enum.Enum):
        weekly = 'weekly'
        biweekly = 'biweekly'
        monthly = 'monthly'
        bimonthly = 'bimonthly'
        quarterly = 'quarterly'
        semiannual = 'semiannual'
        annual = 'annual'

    entity = models.ForeignKey('Entity', on_delete=models.CASCADE)
    document = models.CharField(max_length=60, null=True)
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    due_date = models.DateField()
    type = models.CharField(max_length=3, choices=[
        (AccountTypes.normal.value, 'Normal'),
        (AccountTypes.recurrent.value, 'Recurrent'),
        (AccountTypes.parcelled.value, 'Parcelled'),
    ])
    frequency = models.CharField(max_length=15, null=True, choices=[
        (AccountFrequencys.weekly.value, 'Weekly'),
        (AccountFrequencys.biweekly.value, 'Biweekly'),
        (AccountFrequencys.monthly.value, 'Monthly'),
        (AccountFrequencys.bimonthly.value, 'Bimonthly'),
        (AccountFrequencys.quarterly.value, 'Quarterly'),
        (AccountFrequencys.semiannual.value, 'Semiannual'),
        (AccountFrequencys.annual.value, 'Annual'),
    ])
    number_of_parcels = models.IntegerField(null=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True)
    document_emission_date = models.DateField(null=True)
    expected_deposit_account_id = models.ForeignKey('DepositAccount', on_delete=models.CASCADE, null=True)
    person = models.ForeignKey('People', on_delete=models.CASCADE, null=True)
    classification_center = models.ForeignKey('ClassificationCenter', on_delete=models.CASCADE, null=True)
    observation = models.TextField(null=True)

    def __str__(self):
        return self.description

    class Meta:
        abstract = True


class AccountPayable(Account):
    pass


class AccountReceivables(Account):
    pass
