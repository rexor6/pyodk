# pyodk.AccountApi

All URIs are relative to *https://pl1-api.oktawave.com/services*

Method | HTTP request | Description
------------- | ------------- | -------------
[**account_delete_ssh_key**](AccountApi.md#account_delete_ssh_key) | **DELETE** /account/sshkeys/{sshKeyId} | Deletes SSH key
[**account_get**](AccountApi.md#account_get) | **GET** /account | Returns account details
[**account_get_ssh_key**](AccountApi.md#account_get_ssh_key) | **GET** /account/sshkeys/{sshKeyId} | Returns SSH key
[**account_get_ssh_keys**](AccountApi.md#account_get_ssh_keys) | **GET** /account/sshkeys | Returns SSH keys
[**account_post_ssh_key**](AccountApi.md#account_post_ssh_key) | **POST** /account/sshkeys | Creates new SSH key for user


# **account_delete_ssh_key**
> account_delete_ssh_key(ssh_key_id)

Deletes SSH key

### Example
```python
from __future__ import print_function
import time
import pyodk
from pyodk.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = pyodk.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = pyodk.AccountApi(pyodk.ApiClient(configuration))
ssh_key_id = 56 # int | SSH key id

try:
    # Deletes SSH key
    api_instance.account_delete_ssh_key(ssh_key_id)
except ApiException as e:
    print("Exception when calling AccountApi->account_delete_ssh_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ssh_key_id** | **int**| SSH key id | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_get**
> Account account_get(fields=fields)

Returns account details

### Example
```python
from __future__ import print_function
import time
import pyodk
from pyodk.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = pyodk.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = pyodk.AccountApi(pyodk.ApiClient(configuration))
fields = 'fields_example' # str | Response fields filter (optional)

try:
    # Returns account details
    api_response = api_instance.account_get(fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->account_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Response fields filter | [optional] 

### Return type

[**Account**](Account.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_get_ssh_key**
> SshKey account_get_ssh_key(ssh_key_id, fields=fields)

Returns SSH key

### Example
```python
from __future__ import print_function
import time
import pyodk
from pyodk.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = pyodk.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = pyodk.AccountApi(pyodk.ApiClient(configuration))
ssh_key_id = 56 # int | SSH key id
fields = 'fields_example' # str | Response fields filter (optional)

try:
    # Returns SSH key
    api_response = api_instance.account_get_ssh_key(ssh_key_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->account_get_ssh_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ssh_key_id** | **int**| SSH key id | 
 **fields** | **str**| Response fields filter | [optional] 

### Return type

[**SshKey**](SshKey.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_get_ssh_keys**
> ApiCollectionSshKey account_get_ssh_keys(page_size=page_size, page_number=page_number, order_by=order_by, fields=fields)

Returns SSH keys

Acceptable order values are: OwnerUser, Name, Id

### Example
```python
from __future__ import print_function
import time
import pyodk
from pyodk.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = pyodk.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = pyodk.AccountApi(pyodk.ApiClient(configuration))
page_size = 56 # int | Page size (optional)
page_number = 56 # int | Page number (optional)
order_by = 'order_by_example' # str | Order by (optional)
fields = 'fields_example' # str | Response fields filter (optional)

try:
    # Returns SSH keys
    api_response = api_instance.account_get_ssh_keys(page_size=page_size, page_number=page_number, order_by=order_by, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->account_get_ssh_keys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| Page size | [optional] 
 **page_number** | **int**| Page number | [optional] 
 **order_by** | **str**| Order by | [optional] 
 **fields** | **str**| Response fields filter | [optional] 

### Return type

[**ApiCollectionSshKey**](ApiCollectionSshKey.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_post_ssh_key**
> SshKey account_post_ssh_key(command)

Creates new SSH key for user

### Example
```python
from __future__ import print_function
import time
import pyodk
from pyodk.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = pyodk.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = pyodk.AccountApi(pyodk.ApiClient(configuration))
command = pyodk.CreateSshKeyCommand() # CreateSshKeyCommand | Create SSH key command

try:
    # Creates new SSH key for user
    api_response = api_instance.account_post_ssh_key(command)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->account_post_ssh_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **command** | [**CreateSshKeyCommand**](CreateSshKeyCommand.md)| Create SSH key command | 

### Return type

[**SshKey**](SshKey.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

