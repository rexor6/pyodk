# pyodk.NetworkingApi

All URIs are relative to *https://pl1-api.oktawave.com/services*

Method | HTTP request | Description
------------- | ------------- | -------------
[**opns_delete**](NetworkingApi.md#opns_delete) | **DELETE** /opns/{id} | Deletes an OPN
[**opns_get**](NetworkingApi.md#opns_get) | **GET** /opns | Returns OPNs
[**opns_post**](NetworkingApi.md#opns_post) | **POST** /opns | Creates an OPN
[**opns_put**](NetworkingApi.md#opns_put) | **PUT** /opns/{id} | Updates OPN


# **opns_delete**
> Ticket opns_delete(id)

Deletes an OPN

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
api_instance = pyodk.NetworkingApi(pyodk.ApiClient(configuration))
id = 56 # int | OPN id

try:
    # Deletes an OPN
    api_response = api_instance.opns_delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkingApi->opns_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| OPN id | 

### Return type

[**Ticket**](Ticket.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **opns_get**
> ApiCollectionOpn opns_get(instance_id=instance_id, query=query, page_size=page_size, page_number=page_number, order_by=order_by, fields=fields)

Returns OPNs

Acceptable order values are: Name

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
api_instance = pyodk.NetworkingApi(pyodk.ApiClient(configuration))
instance_id = 56 # int | Instance id (optional)
query = 'query_example' # str | Query (optional)
page_size = 56 # int | Page size (optional)
page_number = 56 # int | Page number (optional)
order_by = 'order_by_example' # str | Order by (optional)
fields = 'fields_example' # str | Response fields filter (optional)

try:
    # Returns OPNs
    api_response = api_instance.opns_get(instance_id=instance_id, query=query, page_size=page_size, page_number=page_number, order_by=order_by, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkingApi->opns_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **int**| Instance id | [optional] 
 **query** | **str**| Query | [optional] 
 **page_size** | **int**| Page size | [optional] 
 **page_number** | **int**| Page number | [optional] 
 **order_by** | **str**| Order by | [optional] 
 **fields** | **str**| Response fields filter | [optional] 

### Return type

[**ApiCollectionOpn**](ApiCollectionOpn.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **opns_post**
> Ticket opns_post(command)

Creates an OPN

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
api_instance = pyodk.NetworkingApi(pyodk.ApiClient(configuration))
command = pyodk.CreateOpnCommand() # CreateOpnCommand | Create OPN command

try:
    # Creates an OPN
    api_response = api_instance.opns_post(command)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkingApi->opns_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **command** | [**CreateOpnCommand**](CreateOpnCommand.md)| Create OPN command | 

### Return type

[**Ticket**](Ticket.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **opns_put**
> Object opns_put(id, command)

Updates OPN

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
api_instance = pyodk.NetworkingApi(pyodk.ApiClient(configuration))
id = 56 # int | OPN id
command = pyodk.UpdateOpnCommand() # UpdateOpnCommand | Update OPN command

try:
    # Updates OPN
    api_response = api_instance.opns_put(id, command)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkingApi->opns_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| OPN id | 
 **command** | [**UpdateOpnCommand**](UpdateOpnCommand.md)| Update OPN command | 

### Return type

[**Object**](Object.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

