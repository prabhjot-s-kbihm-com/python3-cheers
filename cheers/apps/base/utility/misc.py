import random
import string
from datetime import timedelta
from django.utils.text import slugify
from django.utils import timezone
from dateutil.relativedelta import relativedelta

#------------------------------------------------------------------------------
# get_user_media_path
#------------------------------------------------------------------------------
def get_user_media_upload_path(user, uploadtype="image"):
    """
    Method to return the path for user file uploads
    for uploadtype 'image' path will become
        images/users/<email>/
    similarly for 'file'
        files/users/<email>
    """
    return '{0}s/users/{1}'.format(uploadtype,
                                   slugify(user.email))


#-------------------------------------------------------------------------------
# days_from_now
#-------------------------------------------------------------------------------
def days_from_now(days=1):
    """
    This method makes the registration code expire after 24 hours from the day
    of registering on the system.
    """

    return timezone.now() + timedelta(days=days)


def add_duration_from_now(days=0, months=0):
    return timezone.now() + relativedelta(days=days, months=months)


def randomStringDigits(stringLength=6):
    """Generate a random string of letters and digits """

    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))
