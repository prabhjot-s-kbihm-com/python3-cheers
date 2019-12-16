from oauth2_provider.models import AccessToken
from oauth2_provider.models import Application
from oauth2_provider.models import RefreshToken
from oauth2_provider.settings import oauth2_settings
from oauthlib.oauth2.rfc6749.tokens import random_token_generator
from datetime import timedelta
import datetime
import pprint
import logging

from cheers.settings import DEFAULT_OAUTH_APP_NAME

logger = logging.getLogger(__name__)


def generate_oauth2_access_token(request, user):
    """
    This method is used to generate an oauth2 access token programatically.
    """

    logger.debug('Generating OAUTH token for user %s', user)

    expire_seconds = \
        oauth2_settings.user_settings['ACCESS_TOKEN_EXPIRE_SECONDS']

    scopes = " ".join(list(oauth2_settings.user_settings['SCOPES'].keys()))

    # the default name of the application is created via the web /o/applications/
    application = Application.objects.get(name=DEFAULT_OAUTH_APP_NAME)

    expires = datetime.datetime.now() + timedelta(seconds=expire_seconds)

    # generate the oauth2 access token
    access_token = AccessToken.objects.create(
        user=user,
        application=application,
        token=random_token_generator(request),
        expires=expires,
        scope=scopes
    )

    # generate the oauth2 regresh token
    refresh_token = RefreshToken.objects.create(
        user=user,
        token=random_token_generator(request),
        access_token=access_token,
        application=application
    )

    token = {
        'access_token': access_token.token,
        'token_type': 'Bearer',
        'expires_in': expire_seconds,
        'refresh_token': refresh_token.token,
        'scope': scopes
    }

    # token.update({'user': request.user.serialized_data})

    logger.debug('\r\n\r\n%s\n\n\t\tOAUTH2 TOKEN GENERATED FOR THIS SESSION '
                 '\r\n\r\nUSER: %s\nTOKEN DATA: \n%s\n%s\n',
                 '*' * 80,
                 user,
                 pprint.pformat(token),
                 '*' * 80, )

    return token