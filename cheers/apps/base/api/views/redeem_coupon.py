from django.forms import model_to_dict
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from cheers.apps.base.models import ModelBaseCoupon
from django.utils.translation import ugettext_lazy as _


class ViewAPIBaseRedeemCoupon(APIView):
    """
    This class handle the country.
    """

    pagination_class = None

    def post(self, request, *args, **kwargs):

        code = self.request.data.get('code')
        error = {'code': _('empty code not accepted')}

        if code:
            coupon_user, error = ModelBaseCoupon.redeem_code(self.request.user, code)

            if coupon_user:
                return Response(model_to_dict(coupon_user))

        return Response(error, status=status.HTTP_400_BAD_REQUEST)
