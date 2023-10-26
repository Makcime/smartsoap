from . import client

import json
import base64

def get_user_details_by_username(accesscode, username):
    """
    Fetches user details based on the provided username.
    
    Parameters:
    - accesscode (str): Web services password.
    - username (str): User identifier (username).
    
    Returns:
    dict: User details in JSON format.
    """
    
    response = client.service.getUserDetailsByUsername(accesscode, username)
    
    # Assuming the SOAP service responds with a string that is JSON-formatted:
    return json.loads(response)


def get_all_accounts(accesscode, code, recursive):
    """
    Fetches the first name, last name, identifier, and internal numbers of users in a group.
    
    Parameters:
    - accesscode (str): Web services password.
    - code (str): Unique class or group code to retrieve.
    - recursive (str): Retrieve sub-groups as well ('0' if not required, '1' if required).
    
    Returns:
    dict: User details extracted from base64-encoded XML.
    """

    response = client.service.getAllAccounts(accesscode, code, recursive)
    print(response)
    
    # Decoding the base64 XML response
    decoded_response = base64.b64decode(response)
    
    # You might want to convert the XML to a dictionary or another format.
    # For simplicity, let's return the decoded XML string.
    return decoded_response


def get_all_accounts_extended(accesscode, code, recursive):
    """
    Fetches all profile fields (except passwords and profile photo), 
    the official class number, group memberships of users in a group, 
    and the last connections. The method returns a JSON object.
    
    Parameters:
    - accesscode (str): Web services password.
    - code (str): Unique class or group code to retrieve.
    - recursive (str): Retrieve sub-groups as well ('0' if not required, '1' if required).
    
    Returns:
    dict: User extended details in JSON format.
    """
    
    response = client.service.getAllAccountsExtended(accesscode, code, recursive)
    
    # Assuming the SOAP service responds with a string that is JSON-formatted:
    return json.loads(response)
