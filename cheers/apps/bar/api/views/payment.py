from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
import stripe

from cheers.apps.account.models import ModelAccountUser
from cheers.apps.bar.api.serializers.payment import SerializerBarPayment
from cheers.apps.bar.models import ModelBarPlan
from cheers.settings import STRIPE_SECRET_KEY
import logging

logger = logging.getLogger(__name__)


class ViewAPIBarPayment(APIView):
    """
    This class is used for payment
    """

    serializer_class = SerializerBarPayment

    def post(self, request):
        """
        Send the data for payment and created the subscription for the user.
        """

        serializer = self.serializer_class(data=request.data, context={"request":self.request})
        serializer.is_valid(raise_exception=True)

        plan = ModelBarPlan.objects.get(id=serializer.data.get("plan"))

        stripe.api_key = STRIPE_SECRET_KEY
        token = serializer.data.get('stripe_token')
        is_saved = serializer.data.get('is_saved')
        card_token = serializer.data.get('card_token')
        try:
            if token:
                if is_saved:
                    source = stripe.Customer.create_source(request.user.stripe_customer['id'], source=token)
                else:
                    source = token
                charge = stripe.Charge.create(
                    amount=round(plan.price) * 100,  # convert cent to dollar
                    currency=plan.currency,
                    description=plan.title,
                    source=source,
                )
            else:
                source = card_token
                charge = stripe.Charge.create(
                    amount=round(plan.price) * 100,  # convert cent to dollar
                    currency=plan.currency,
                    description=plan.title,
                    source=source,
                    customer=request.user.stripe_customer['id'],
                )
        except Exception as e:
            logger.error('Error while accepting payment: %s', e.__str__())
            return Response({"error": "Some error occured in payment. Please try again"},
                            status=status.HTTP_400_BAD_REQUEST)


        if charge.get("status") == "succeeded":
            plan.subscribe(request.user, transaction_details=charge, language=request.META.get('HTTP_ACCEPT_LANGUAGE', ''))

        return Response(charge, status=status.HTTP_200_OK)
