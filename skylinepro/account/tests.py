
from django.core import mail
from django.test import override_settings
from rest_framework.test import APITestCase

from .models import PasswordResetOTP, User


@override_settings(EMAIL_BACKEND="django.core.mail.backends.locmem.EmailBackend")
class PasswordResetRequestTests(APITestCase):
    def test_request_creates_and_emails_otp_without_requesting_one(self):
        user = User.objects.create_user(email="user@example.com", password="old-password")

        response = self.client.post(
            "/api/reset-password-request/",
            {"email": user.email},
            format="json",
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {"message": "Password reset OTP sent."})
        otp_record = PasswordResetOTP.objects.get(user=user, is_used=False)
        self.assertEqual(len(otp_record.otp), 6)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].to, [user.email])
        self.assertIn(otp_record.otp, mail.outbox[0].body)
