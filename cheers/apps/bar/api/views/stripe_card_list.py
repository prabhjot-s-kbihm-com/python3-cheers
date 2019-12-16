from rest_framework.response import Response
from rest_framework.views import APIView
import stripe

from cheers.settings import STRIPE_SECRET_KEY


class ViewAPIBarStripeCardList(APIView):
    """
    THis method return the list of stripe cards.
    """

    def get(self, request, *args, **kwargs):

        stripe.api_key = STRIPE_SECRET_KEY

        cards = stripe.Customer.list_sources(
            request.user.stripe_customer['id'],
            limit=3,
            object='card'
        )

        return Response(cards)

