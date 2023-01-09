# pyodk.DictionariesApi

All URIs are relative to *https://pl1-api.oktawave.com/services*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dictionaries_get_dictionaries**](DictionariesApi.md#dictionaries_get_dictionaries) | **GET** /dictionaries | Returns dictionaries
[**dictionaries_get_dictionaries_items**](DictionariesApi.md#dictionaries_get_dictionaries_items) | **GET** /dictionaries/{ids} | Returns dictionaries items
[**dictionaries_get_languages**](DictionariesApi.md#dictionaries_get_languages) | **GET** /dictionaries/languages | Returns languages


# **dictionaries_get_dictionaries**
> ApiCollectionDictionary dictionaries_get_dictionaries(fields=fields)

Returns dictionaries

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
api_instance = pyodk.DictionariesApi(pyodk.ApiClient(configuration))
fields = 'fields_example' # str | Response fields filter (optional)

try:
    # Returns dictionaries
    api_response = api_instance.dictionaries_get_dictionaries(fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DictionariesApi->dictionaries_get_dictionaries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Response fields filter | [optional] 

### Return type

[**ApiCollectionDictionary**](ApiCollectionDictionary.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dictionaries_get_dictionaries_items**
> ApiCollectionDictionaryItem dictionaries_get_dictionaries_items(ids, fields=fields)

Returns dictionaries items

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
api_instance = pyodk.DictionariesApi(pyodk.ApiClient(configuration))
ids = 'ids_example' # str | Dictionaries ids
fields = 'fields_example' # str | Response fields filter (optional)

try:
    # Returns dictionaries items
    api_response = api_instance.dictionaries_get_dictionaries_items(ids, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DictionariesApi->dictionaries_get_dictionaries_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **str**| Dictionaries ids | 
 **fields** | **str**| Response fields filter | [optional] 

### Return type

[**ApiCollectionDictionaryItem**](ApiCollectionDictionaryItem.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dictionaries_get_languages**
> ApiCollectionDictionaryItem dictionaries_get_languages(fields=fields)

Returns languages

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
api_instance = pyodk.DictionariesApi(pyodk.ApiClient(configuration))
fields = 'fields_example' # str | Response fields filter (optional)

try:
    # Returns languages
    api_response = api_instance.dictionaries_get_languages(fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DictionariesApi->dictionaries_get_languages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Response fields filter | [optional] 

### Return type

[**ApiCollectionDictionaryItem**](ApiCollectionDictionaryItem.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

