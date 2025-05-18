# -*- coding: utf-8 -*-
# __author__ = "Mohammad Sajjad Mortazavi"
#license.py

import clr 

clr.AddReference("System.Net.Http")
clr.AddReference("System.Net")
clr.AddReference("System")
clr.AddReference("System.Core")
clr.AddReference("System.Security")

from System.Net.Http import HttpClient
import base64
from datetime import datetime
import json

from System.Net.Http import HttpClient, HttpRequestMessage, HttpMethod
from System.Net.Http.Headers import HttpRequestHeaders
from System.Net import ServicePointManager, SecurityProtocolType
from System.Net.Security import RemoteCertificateValidationCallback

def decrypt_data(encrypted_data):
    """
    Decrypts the given base64 encoded string.

    Args:
        encrypted_data (str): The base64 encoded string to decrypt.

    Returns:
        str: The decrypted string.
    """
    encrypted_data_bytes = base64.b64decode(encrypted_data)
    decrypted_data = encrypted_data_bytes.decode('utf-8')
    return decrypted_data

def getInit_(key):
    """
    Checks if the license associated with the given key is valid based on its expiration date.

    Args:
        key (str): The license key to check.

    Returns:
        bool: True if the license is valid, False otherwise.
    """
    try:
        client = HttpClient()
        response = client.GetStringAsync(key).Result
        data = json.loads(response)
        encrypted_expire_date = data.get('ExpireDate', None)

        if encrypted_expire_date:
            decrypted_expire_date = decrypt_data(encrypted_expire_date)
            expire_date = datetime.strptime(decrypted_expire_date, "%Y-%m-%d")

            return expire_date >= datetime.now()
        else:
            return False
    
    except Exception as e:
        return False

ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12
ServicePointManager.ServerCertificateValidationCallback = RemoteCertificateValidationCallback(lambda sender, certificate, chain, sslPolicyErrors: True)

def getInit(license_key_integer):
    """
    Validates the license key by sending a request to the license server.

    Args:
        license_key_integer (int): The license key to validate.

    Returns:
        bool: True if the license is valid, False otherwise.
    """
    try:
        base_url = "https://api.bimpars.com/api/License/CheckLicense?licenseKey="
        url = base_url + str(license_key_integer)
        
        client = HttpClient()
        request = HttpRequestMessage(HttpMethod.Post, url)
        request.Headers.Add("accept", "*/*")  
        
        response = client.SendAsync(request).Result
        
        if response.IsSuccessStatusCode:
            response_content = response.Content.ReadAsStringAsync().Result
            data = json.loads(response_content)
            
            encrypted_expire_date = data.get('ExpireDate', None)
            if encrypted_expire_date:
                decrypted_expire_date = decrypt_data(encrypted_expire_date)
                expire_date = datetime.strptime(decrypted_expire_date, "%m/%d/%Y %I:%M:%S %p")
                
                return expire_date >= datetime.now()
            else:
                return False
        else:
            return False
    
    except Exception as e:
        return False
