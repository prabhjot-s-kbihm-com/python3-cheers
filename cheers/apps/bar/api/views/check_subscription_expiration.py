from datetime import datetime

from rest_framework.response import Response
from rest_framework.views import APIView


class ViewAPIBarCheckSubscriptionExpire(APIView):
    """
    This view check the user subscription expiration date.
    """

    def get(self, request, *args, **kwargs):
        """
        This method check the expiration date.
        """
        try:
            subscription = request.user.subscription
            if self.request.user.is_today_order_allowed:
                today_order = True
            else:
                today_order = False
            if datetime.now().date() > subscription.expiration.date():
                subscription.active = False
                subscription.save()
                return Response({'expiration': True, "plan_id": None, "cancellation": False, "today_order": False})
            return Response(
                {'expiration': False, "plan_id": subscription.plan.id, "cancellation": subscription.cancellation,
                 "today_order": today_order})
        except AttributeError:
            return Response({'expiration': True, "plan_id": None, "cancellation": False, "today_order": False})
