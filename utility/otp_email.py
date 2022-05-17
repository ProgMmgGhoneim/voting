import string
import logging
import random

from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context

from django.conf import settings

logger = logging.getLogger(__name__)


class OTPEmail:

    @staticmethod
    def generate_random_otp(size=10):
        """
            Generate random OTP from upper, lower and digit 
        """
        return ''.join([random.choice(string.ascii_uppercase +
                                      string.ascii_lowercase +
                                      string.digits)
                        for n in range(size)])

    @staticmethod
    def send_otp_email(username: str, subject: str, from_email: str,
                       to_email: list, otp: str):
        # Get html & text template
        email_text = get_template("otp_email.txt")
        email_html = get_template("otp_email.html")

        # render context
        context = {
            "user": username,
            "otp": otp
        }
        text_content = email_text.render(context)
        html_content = email_html.render(context)

        try:
         # Sending Email
            msg = EmailMultiAlternatives(
                subject, text_content, from_email, [to_email])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            return True
        except BaseException as e:
            logger.debug(
                '[REGISTER][SENDING OTP] Exception Error IS: {}'.format(e))
            return False
