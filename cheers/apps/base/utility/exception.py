from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)
    try:
        data = response.data
        response.data = {}

        for field, value in data.items():
            if type(value) == list:
                response.data[field] = ", ".join(value)
            else:
                response.data[field] = value
    except AttributeError:
        pass

    return response
