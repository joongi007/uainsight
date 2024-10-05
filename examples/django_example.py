from django.conf import settings
from django.core.wsgi import get_wsgi_application
from django.http import JsonResponse
from django.urls import path

# Django settings
settings.configure(
    DEBUG=True,
    SECRET_KEY="your-secret-key",
    ROOT_URLCONF=__name__,
    MIDDLEWARE=[
        "django.middleware.common.CommonMiddleware",
        "useragent_parser.integrations.django.DjangoUserAgentMiddleware",
    ],
)


# View
def user_agent_info(request):
    ua = request.user_agent
    return JsonResponse(
        {
            "browser": f"{ua.browser.name} {ua.browser.version}",
            "os": f"{ua.os.name} {ua.os.version}",
            "device": ua.device,
            "is_mobile": ua.is_mobile,
            "is_tablet": ua.is_tablet,
            "is_desktop": ua.is_desktop,
            "is_bot": ua.is_bot,
        }
    )


# URL configuration
urlpatterns = [
    path("", user_agent_info),
]

# WSGI application
application = get_wsgi_application()

if __name__ == "__main__":
    from django.core.management import execute_from_command_line

    execute_from_command_line(["", "runserver", "0.0.0.0:8000"])
