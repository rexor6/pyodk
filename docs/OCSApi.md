# pyodk.OCSApi

All URIs are relative to *https://pl1-api.oktawave.com/services*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ocs_get_projects**](OCSApi.md#ocs_get_projects) | **GET** /ocs/projects | Returns the list of OCS projects


# **ocs_get_projects**
> ApiCollectionOcsProject ocs_get_projects(fields=fields)

Returns the list of OCS projects

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
api_instance = pyodk.OCSApi(pyodk.ApiClient(configuration))
fields = 'fields_example' # str | Response fields filter (optional)

try:
    # Returns the list of OCS projects
    api_response = api_instance.ocs_get_projects(fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OCSApi->ocs_get_projects: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Response fields filter | [optional] 

### Return type

[**ApiCollectionOcsProject**](ApiCollectionOcsProject.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

