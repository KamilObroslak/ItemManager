from django.utils import translation
from django.utils.translation import gettext as _

from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def index(request):
    accept_language = request.META.get('HTTP_ACCEPT_LANGUAGE', '')
    language_code = accept_language.split(',')[0][:2]
    supported_languages = ['pl', 'en']

    if language_code in supported_languages:
        translation.activate(language_code)
    else:
        translation.activate('en')

    message = _("Hello, world. You're at the backend index.")

    return Response({'message', message})
