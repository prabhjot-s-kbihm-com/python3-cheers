# import logging
#
# from django.core.exceptions import ImproperlyConfigured
# from django.core.files import File
# from django.template.loader import render_to_string
#
# from ds.settings import DEFAULT_FROM_EMAIL
# from ds.settings import ENVIRONMENT
# from mailqueue.models import MailerMessage
#
#
# logger = logging.getLogger(__name__)
#
# #------------------------------------------------------------------------------
# # send_email
# #------------------------------------------------------------------------------
# def send_email(subject, to_address, context_data,
#                text_template_path, html_template_path, cc_address="",
#                bcc_address="", from_address=DEFAULT_FROM_EMAIL,
#                file_attachments=[]):
#     """
#     http://django-mail-queue.readthedocs.io/en/latest/usage.html
#     """
#
#     if not to_address and not bcc_address:
#         raise ImproperlyConfigured("you have not set any sender address. "
#                                    "No value found for to address and bcc address")
#
#     html_content = render_to_string(html_template_path, context_data)
#     text_content = render_to_string(text_template_path, context_data)
#
#     if ENVIRONMENT == 'production':
#         app_name = 'ds'
#     elif ENVIRONMENT == 'staging':
#         app_name = 'ds [STAGING]'
#     else:
#         app_name = 'ds [DEVELOPMENT]'
#
#     new_message = MailerMessage()
#     new_message.subject = subject
#     new_message.to_address = to_address
#     new_message.cc_address = cc_address
#     new_message.bcc_address = bcc_address
#     new_message.from_address = from_address
#     new_message.content = text_content
#     new_message.html_content = html_content
#     new_message.app = app_name
#
#     for file in file_attachments:
#         file = File(open(file, "rb"))
#         new_message.add_attachment(file)
#
#
#     new_message.save()
