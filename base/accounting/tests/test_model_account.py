import datetime

from base.accounting.models import Account
from base.accounting.tests.test_model_entity import create_entity


def create_account(_description):
    account = {
        'entity': create_entity(),
        'document': None,
        'description': _description,
        'amount': 0.01,
        'due_date': datetime.date.today(),
        'type': Account.AccountTypes.normal.value,
        'frequency': None,
        'number_of_parcels': None,
        'category': None,
        'document_emission_date': None,
        'expected_deposit_account_id': None,
        'person': None,
        'classification_center': None,
        'observation': None
    }
    return account
