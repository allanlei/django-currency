from currencies import currencies

def currencies(request):
    return {
        'CURRENCIES': currencies,
    }
