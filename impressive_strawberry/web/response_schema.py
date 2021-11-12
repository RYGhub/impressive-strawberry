"""
This module contains common HTTP responses to include in schemas.
"""

UNAUTHORIZED = {
    401: {
        "description": "The method requires an Authorization header, but none was provided."
    },
}

FORBIDDEN = {
    403: {
        "description": "You are not authorized to call the method on the object."
    }
}

NOT_FOUND = {
    404: {
        "description": "The requested object was not found."
    },
}
