import urllib.parse
import time
import hmac
import hashlib
import base64

#https://gist.github.com/sedouard/8412cb51629ef9614fd4

def _sign_string(uri, key, key_name):

    '''
    100000 = milsecond expiry
    '''
    expiry = int(time.time() + 100000000)

    string_to_sign = urllib.parse.quote_plus(uri) + '\n' + str(expiry)
    # print ('url: ' + str(uri))
    # print ('url encoded: ' + str(string_to_sign))

    key = key.encode('utf-8')
    string_to_sign = string_to_sign.encode('utf-8')
    # print ('url encoded: ' + str(string_to_sign))
    signed_hmac_sha256 = hmac.HMAC(key, string_to_sign, hashlib.sha256)
    signature = signed_hmac_sha256.digest()
    signature = base64.b64encode(signature)


    return 'SharedAccessSignature sr=' + str(urllib.parse.quote_plus(uri))  + '&sig=' + str(urllib.parse.quote(signature)) + '&se=' + str(expiry) + '&skn=' + str(key_name)

# print _sign_string('https://<Service Bus Namespace>.servicebus.windows.net/<Hub Name>/publishers/<Device Id>/messages', '<Your Shared Access Token>', '<Your Key Name>')



# print (_sign_string("https://cloudassignment34ed0.servicebus.windows.net/taskqueue",shared_access_key_value,shared_access_key_name))