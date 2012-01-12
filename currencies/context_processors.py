from currencies import CURRENCIES


def currencies(request):
    return {
        'CURRENCIES': CURRENCIES,
    }
