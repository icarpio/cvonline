from django.conf import settings


def inf_var(request):
    return {
        'image': settings.IMAGE,
    }