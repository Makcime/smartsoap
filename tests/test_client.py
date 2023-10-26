import os

from smartsoap.client import get_user_details_by_username

ACCESS_CODE = os.environ.get("SMARTSOAP_ACCESSCODE")
USER_TEST = os.environ.get("USER_TEST")


def test_get_user_details_by_username():
    accesscode = ACCESS_CODE
    username = USER_TEST
    
    response = get_user_details_by_username(accesscode, username)
    
    assert response is not None
    # Add more assertions based on your expected response structure.

