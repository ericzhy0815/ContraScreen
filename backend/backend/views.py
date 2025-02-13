from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import requests
import json
import logging

User = get_user_model()
logger = logging.getLogger(__name__)

@csrf_exempt
def google_auth_callback(request):
    print("Google Auth Callback")
    logger.debug(f"Redirect URI: {request.build_absolute_uri()}")  # Logs the

    if request.method != "POST":
        return JsonResponse({"error": "Invalid request !!"}, status=400)

    try:
        data = json.loads(request.body)
        token = data.get("token")

        # Verify the token with Google
        google_response = requests.get(
            f"https://www.googleapis.com/oauth2/v3/tokeninfo?id_token={token}"
        ).json()

        if "email" not in google_response:
            return JsonResponse({"error": "Invalid token"}, status=400)

        email = google_response["email"]
        name = google_response.get("name", "")

        # Check if user exists or create one
        user, _ = User.objects.get_or_create(email=email, defaults={"username": email, "first_name": name})

        # Generate Django auth token
        from rest_framework.authtoken.models import Token
        token, _ = Token.objects.get_or_create(user=user)

        return JsonResponse({"access": token.key})

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
