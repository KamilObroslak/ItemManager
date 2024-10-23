from django.utils import translation
from django.utils.translation import gettext as _

from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.http import JsonResponse
from .models import ClientProfile, MerchantProfile
from django.views.decorators.csrf import csrf_exempt
import json

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

    message_text = _("Hello, world. You're at the backend index.")

    return Response({'message', message_text})


@csrf_exempt
def create_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        first_name = data.get('first_name')
        last_name = data.get('last_name')
        email = data.get('email')
        phone_number = data.get('phone_number')
        user_type = data.get('user_type')

        if user_type == 1:  # Client
            if ClientProfile.objects.filter(email=email).exists():
                return JsonResponse({'error': 'Email already exists'}, status=400)

            user = ClientProfile.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone_number=phone_number
            )

        elif user_type == 2:  # Merchant
            if MerchantProfile.objects.filter(email=email).exists():
                return JsonResponse({'error': 'Email already exists'}, status=400)

            user = MerchantProfile.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone_number=phone_number,
                business_name=data.get('business_name')  # Wymaga podania nazwy firmy
            )

        else:
            return JsonResponse({'error': 'Invalid user type'}, status=400)

    return Response({'message', message})
        return JsonResponse({'message': 'User created successfully'}, status=201)
    return JsonResponse({'error': 'Invalid request method'}, status=405)
