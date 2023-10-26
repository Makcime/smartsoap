import os


from zeep import Client

# WSDL_URL = 'URL_TO_YOUR_WSDL_HERE'  # Replace with the URL to your WSDL
# WSDL_URL = 'https://yourschool.smartschool.be/Webservices/V3?wsdl'  # Replace with the URL to your WSDL
WSDL_URL = os.environ.get("WSDL_URL")

client = Client(WSDL_URL)

