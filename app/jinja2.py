from django.conf import settings
from django.urls import reverse_lazy
from django.contrib.staticfiles.storage import staticfiles_storage
from jinja2 import Environment, PackageLoader


def environment(**_):
    env = Environment(
        loader=PackageLoader('app'),
        autoescape=True
    )
    env.globals.update({
        'static': staticfiles_storage.url,
        'url': reverse_lazy,
        'settings': settings,
    })
    return env
