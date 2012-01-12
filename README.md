# Requirements #

* Python 2.7+
* Django 1.3+


# Installation #

* Add 'currencies' to INSTALLED_APPS
* Add 'currencies.context_processors.currencies' to TEMPLATE_CONTEXT_PROCESSORS if you need access to all the currencies in templates

# Usage #

### Template Filters ###

```
{% load currency %}
{{ 1000.010|currency:'USD' }}
```

### Manual ###
```
from currencies.utils import format
format(100.01, symbol='$')
```