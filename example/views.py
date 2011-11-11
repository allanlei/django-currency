from django.views import generic

from currencies.templatetags.currency import currency

class TestView(generic.base.TemplateView):
    template_name = 'test.html'
    
    def get_context_data(self, **kwargs):
        print currency(123456789, 'USD')
        return super(TestView, self).get_context_data(**kwargs)
