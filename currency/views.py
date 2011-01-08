from fixtures.regions import REGIONS
from django.shortcuts import render_to_response

def test(request, region=None):
    context = {
        'regions': [region for i in range(500)] if region is not None else sorted(REGIONS.keys()),
    }
    return render_to_response('test.html', context)
