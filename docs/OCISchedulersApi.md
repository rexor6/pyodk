# pyodk.OCISchedulersApi

All URIs are relative to *https://pl1-api.oktawave.com/services*

Method | HTTP request | Description
------------- | ------------- | -------------
[**instance_schedulers_delete**](OCISchedulersApi.md#instance_schedulers_delete) | **DELETE** /instances/schedulers/{id} | Deletes instance scheduler
[**instance_schedulers_get**](OCISchedulersApi.md#instance_schedulers_get) | **GET** /instances/schedulers/{id} | Gets scheduler by identifier
[**instance_schedulers_get_instance_schedulers**](OCISchedulersApi.md#instance_schedulers_get_instance_schedulers) | **GET** /instances/{id}/schedulers | Gets instance schedulers
[**instance_schedulers_post**](OCISchedulersApi.md#instance_schedulers_post) | **POST** /instances/{id}/schedulers | Creates instance scheduler
[**instance_schedulers_put**](OCISchedulersApi.md#instance_schedulers_put) | **PUT** /instances/schedulers/{id} | Updates instance scheduler
[**instances_get_schedulers**](OCISchedulersApi.md#instances_get_schedulers) | **GET** /instances/schedulers | Gets schedulers by search params


# **instance_schedulers_delete**
> instance_schedulers_delete(id)

Deletes instance scheduler

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
api_instance = pyodk.OCISchedulersApi(pyodk.ApiClient(configuration))
id = 56 # int | Scheduler id

try:
    # Deletes instance scheduler
    api_instance.instance_schedulers_delete(id)
except ApiException as e:
    print("Exception when calling OCISchedulersApi->instance_schedulers_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Scheduler id | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instance_schedulers_get**
> InstanceScheduler instance_schedulers_get(id, fields=fields)

Gets scheduler by identifier

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
api_instance = pyodk.OCISchedulersApi(pyodk.ApiClient(configuration))
id = 56 # int | Scheduler id
fields = 'fields_example' # str | Response fields filter (optional)

try:
    # Gets scheduler by identifier
    api_response = api_instance.instance_schedulers_get(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OCISchedulersApi->instance_schedulers_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Scheduler id | 
 **fields** | **str**| Response fields filter | [optional] 

### Return type

[**InstanceScheduler**](InstanceScheduler.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instance_schedulers_get_instance_schedulers**
> ApiCollectionInstanceScheduler instance_schedulers_get_instance_schedulers(id, fields=fields)

Gets instance schedulers

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
api_instance = pyodk.OCISchedulersApi(pyodk.ApiClient(configuration))
id = 56 # int | Instance id
fields = 'fields_example' # str | Response fields filter (optional)

try:
    # Gets instance schedulers
    api_response = api_instance.instance_schedulers_get_instance_schedulers(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OCISchedulersApi->instance_schedulers_get_instance_schedulers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Instance id | 
 **fields** | **str**| Response fields filter | [optional] 

### Return type

[**ApiCollectionInstanceScheduler**](ApiCollectionInstanceScheduler.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instance_schedulers_post**
> InstanceScheduler instance_schedulers_post(id, command)

Creates instance scheduler

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
api_instance = pyodk.OCISchedulersApi(pyodk.ApiClient(configuration))
id = 56 # int | Instance id
command = pyodk.CreateUpdateInstanceSchedulerCommand() # CreateUpdateInstanceSchedulerCommand | Create instance scheduler command

try:
    # Creates instance scheduler
    api_response = api_instance.instance_schedulers_post(id, command)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OCISchedulersApi->instance_schedulers_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Instance id | 
 **command** | [**CreateUpdateInstanceSchedulerCommand**](CreateUpdateInstanceSchedulerCommand.md)| Create instance scheduler command | 

### Return type

[**InstanceScheduler**](InstanceScheduler.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instance_schedulers_put**
> InstanceScheduler instance_schedulers_put(id, command)

Updates instance scheduler

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
api_instance = pyodk.OCISchedulersApi(pyodk.ApiClient(configuration))
id = 56 # int | Scheduler id
command = pyodk.CreateUpdateInstanceSchedulerCommand() # CreateUpdateInstanceSchedulerCommand | Create instance scheduler command

try:
    # Updates instance scheduler
    api_response = api_instance.instance_schedulers_put(id, command)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OCISchedulersApi->instance_schedulers_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Scheduler id | 
 **command** | [**CreateUpdateInstanceSchedulerCommand**](CreateUpdateInstanceSchedulerCommand.md)| Create instance scheduler command | 

### Return type

[**InstanceScheduler**](InstanceScheduler.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instances_get_schedulers**
> ApiCollectionInstanceScheduler instances_get_schedulers(instance_id=instance_id, action_type_id=action_type_id, query=query, page_size=page_size, page_number=page_number, order_by=order_by, fields=fields)

Gets schedulers by search params

Acceptable order values are: Name, CreationDate, StartDate, Instance, ActionType

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
api_instance = pyodk.OCISchedulersApi(pyodk.ApiClient(configuration))
instance_id = 56 # int | Instance id filter (optional)
action_type_id = 56 # int | Action type id filter (optional)
query = 'query_example' # str | Query (optional)
page_size = 56 # int | Page size (optional)
page_number = 56 # int | Page number (optional)
order_by = 'order_by_example' # str | Order by (optional)
fields = 'fields_example' # str | Response fields filter (optional)

try:
    # Gets schedulers by search params
    api_response = api_instance.instances_get_schedulers(instance_id=instance_id, action_type_id=action_type_id, query=query, page_size=page_size, page_number=page_number, order_by=order_by, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OCISchedulersApi->instances_get_schedulers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **int**| Instance id filter | [optional] 
 **action_type_id** | **int**| Action type id filter | [optional] 
 **query** | **str**| Query | [optional] 
 **page_size** | **int**| Page size | [optional] 
 **page_number** | **int**| Page number | [optional] 
 **order_by** | **str**| Order by | [optional] 
 **fields** | **str**| Response fields filter | [optional] 

### Return type

[**ApiCollectionInstanceScheduler**](ApiCollectionInstanceScheduler.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

