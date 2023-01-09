# pyodk.OCITemplatesApi

All URIs are relative to *https://pl1-api.oktawave.com/services*

Method | HTTP request | Description
------------- | ------------- | -------------
[**templates_delete**](OCITemplatesApi.md#templates_delete) | **DELETE** /templates/{id} | Deletes template
[**templates_get**](OCITemplatesApi.md#templates_get) | **GET** /templates | Returns templates list
[**templates_get_0**](OCITemplatesApi.md#templates_get_0) | **GET** /templates/{id} | Returns template by identifier
[**templates_put**](OCITemplatesApi.md#templates_put) | **PUT** /templates/{id} | Updates template


# **templates_delete**
> Object templates_delete(id)

Deletes template

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
api_instance = pyodk.OCITemplatesApi(pyodk.ApiClient(configuration))
id = 56 # int | Template id

try:
    # Deletes template
    api_response = api_instance.templates_delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OCITemplatesApi->templates_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Template id | 

### Return type

[**Object**](Object.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templates_get**
> ApiCollectionTemplate templates_get(source=source, query=query, page_size=page_size, page_number=page_number, order_by=order_by, fields=fields)

Returns templates list

Acceptable order values are: Name, Version, creationDate, SystemCategory.

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
api_instance = pyodk.OCITemplatesApi(pyodk.ApiClient(configuration))
source = 'source_example' # str | Source (optional)
query = 'query_example' # str | Query (optional)
page_size = 56 # int | Page size (optional)
page_number = 56 # int | Page number (optional)
order_by = 'order_by_example' # str | Order by (optional)
fields = 'fields_example' # str | Response fields filter (optional)

try:
    # Returns templates list
    api_response = api_instance.templates_get(source=source, query=query, page_size=page_size, page_number=page_number, order_by=order_by, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OCITemplatesApi->templates_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | **str**| Source | [optional] 
 **query** | **str**| Query | [optional] 
 **page_size** | **int**| Page size | [optional] 
 **page_number** | **int**| Page number | [optional] 
 **order_by** | **str**| Order by | [optional] 
 **fields** | **str**| Response fields filter | [optional] 

### Return type

[**ApiCollectionTemplate**](ApiCollectionTemplate.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templates_get_0**
> Template templates_get_0(id, fields=fields)

Returns template by identifier

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
api_instance = pyodk.OCITemplatesApi(pyodk.ApiClient(configuration))
id = 56 # int | Template identifier
fields = 'fields_example' # str | Response fields filter (optional)

try:
    # Returns template by identifier
    api_response = api_instance.templates_get_0(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OCITemplatesApi->templates_get_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Template identifier | 
 **fields** | **str**| Response fields filter | [optional] 

### Return type

[**Template**](Template.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templates_put**
> Template templates_put(id, command)

Updates template

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
api_instance = pyodk.OCITemplatesApi(pyodk.ApiClient(configuration))
id = 56 # int | Template id
command = pyodk.UpdateTemplateCommand() # UpdateTemplateCommand | Update command

try:
    # Updates template
    api_response = api_instance.templates_put(id, command)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OCITemplatesApi->templates_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Template id | 
 **command** | [**UpdateTemplateCommand**](UpdateTemplateCommand.md)| Update command | 

### Return type

[**Template**](Template.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

