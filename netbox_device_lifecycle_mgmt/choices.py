from utilities.choices import ChoiceSet

__all__ = [
    'CurrencyChoices',
    'ContractTypeChoices',
]


class ContractTypeChoices(ChoiceSet):
    key = 'Contract.Type'

    TYPE_HARDWARE = 'hardware'
    TYPE_SOFTWARE = 'software'

    CHOICES = [
        (TYPE_HARDWARE, 'Hardware'),
        (TYPE_SOFTWARE, 'Software'),
    ]


class CurrencyChoices(ChoiceSet):
    key = 'Contract.Currency'

    CURRENCY_USD = 'USD'
    CURRENCY_EUR = 'EUR'
    CURRENCY_CAD = 'CAD'

    CHOICES = [
        (CURRENCY_USD, 'USD'),
        (CURRENCY_EUR, 'EUR'),
        (CURRENCY_CAD, 'CAD'),
    ]
