# pyodk.SubregionsApi

All URIs are relative to *https://pl1-api.oktawave.com/services*

Method | HTTP request | Description
------------- | ------------- | -------------
[**subregions_get**](SubregionsApi.md#subregions_get) | **GET** /subregions | Gets subregions
[**subregions_get_0**](SubregionsApi.md#subregions_get_0) | **GET** /subregions/{id} | Gets subregion


# **subregions_get**
> ApiCollectionSubregion subregions_get(fields=fields)

Gets subregions

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
api_instance = pyodk.SubregionsApi(pyodk.ApiClient(configuration))
fields = 'fields_example' # str | Response fields filter (optional)

try:
    # Gets subregions
    api_response = api_instance.subregions_get(fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubregionsApi->subregions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Response fields filter | [optional] 

### Return type

[**ApiCollectionSubregion**](ApiCollectionSubregion.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subregions_get_0**
> Subregion subregions_get_0(id, fields=fields)

Gets subregion

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
api_instance = pyodk.SubregionsApi(pyodk.ApiClient(configuration))
id = 56 # int | Subregion id
fields = 'fields_example' # str | Response fields filter (optional)

try:
    # Gets subregion
    api_response = api_instance.subregions_get_0(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubregionsApi->subregions_get_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Subregion id | 
 **fields** | **str**| Response fields filter | [optional] 

### Return type

[**Subregion**](Subregion.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

