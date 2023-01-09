# pyodk.OCIAutoscalerApi

All URIs are relative to *https://pl1-api.oktawave.com/services*

Method | HTTP request | Description
------------- | ------------- | -------------
[**instances_disable_instance_autoscaler**](OCIAutoscalerApi.md#instances_disable_instance_autoscaler) | **POST** /instances/{id}/autoscaler/disable_ticket | Disables autoscaling for instance
[**instances_enable_instance_autoscaler**](OCIAutoscalerApi.md#instances_enable_instance_autoscaler) | **POST** /instances/{id}/autoscaler/enable_ticket | Enables autoscaling for instance
[**instances_get_autoscaler**](OCIAutoscalerApi.md#instances_get_autoscaler) | **GET** /instances/{id}/autoscaler | Returns instace autoscaler configuration
[**instances_update_autoscaler**](OCIAutoscalerApi.md#instances_update_autoscaler) | **PUT** /instances/{id}/autoscaler | Updates instance autoscaler configuration


# **instances_disable_instance_autoscaler**
> Ticket instances_disable_instance_autoscaler(id)

Disables autoscaling for instance

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
api_instance = pyodk.OCIAutoscalerApi(pyodk.ApiClient(configuration))
id = 56 # int | Instance id

try:
    # Disables autoscaling for instance
    api_response = api_instance.instances_disable_instance_autoscaler(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OCIAutoscalerApi->instances_disable_instance_autoscaler: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Instance id | 

### Return type

[**Ticket**](Ticket.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instances_enable_instance_autoscaler**
> Ticket instances_enable_instance_autoscaler(id)

Enables autoscaling for instance

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
api_instance = pyodk.OCIAutoscalerApi(pyodk.ApiClient(configuration))
id = 56 # int | Instance id

try:
    # Enables autoscaling for instance
    api_response = api_instance.instances_enable_instance_autoscaler(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OCIAutoscalerApi->instances_enable_instance_autoscaler: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Instance id | 

### Return type

[**Ticket**](Ticket.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instances_get_autoscaler**
> Autoscaler instances_get_autoscaler(id, fields=fields)

Returns instace autoscaler configuration

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
api_instance = pyodk.OCIAutoscalerApi(pyodk.ApiClient(configuration))
id = 56 # int | Instance id
fields = 'fields_example' # str | Response fields filter (optional)

try:
    # Returns instace autoscaler configuration
    api_response = api_instance.instances_get_autoscaler(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OCIAutoscalerApi->instances_get_autoscaler: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Instance id | 
 **fields** | **str**| Response fields filter | [optional] 

### Return type

[**Autoscaler**](Autoscaler.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instances_update_autoscaler**
> Object instances_update_autoscaler(id, command)

Updates instance autoscaler configuration

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
api_instance = pyodk.OCIAutoscalerApi(pyodk.ApiClient(configuration))
id = 56 # int | 
command = pyodk.AutoscalerUpdateCommand() # AutoscalerUpdateCommand | 

try:
    # Updates instance autoscaler configuration
    api_response = api_instance.instances_update_autoscaler(id, command)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OCIAutoscalerApi->instances_update_autoscaler: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **command** | [**AutoscalerUpdateCommand**](AutoscalerUpdateCommand.md)|  | 

### Return type

[**Object**](Object.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

