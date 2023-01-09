# pyodk.OCIEventsApi

All URIs are relative to *https://pl1-api.oktawave.com/services*

Method | HTTP request | Description
------------- | ------------- | -------------
[**events_delete**](OCIEventsApi.md#events_delete) | **DELETE** /events/{id} | Deletes event
[**events_get_event**](OCIEventsApi.md#events_get_event) | **GET** /events/{id} | Returns instance event
[**events_get_events**](OCIEventsApi.md#events_get_events) | **GET** /events | Returns all instances events
[**instances_delete_events**](OCIEventsApi.md#instances_delete_events) | **DELETE** /instances/{id}/events | Deletes instance events
[**instances_get_events**](OCIEventsApi.md#instances_get_events) | **GET** /instances/{id}/events | Returns instance events


# **events_delete**
> events_delete(id)

Deletes event

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
api_instance = pyodk.OCIEventsApi(pyodk.ApiClient(configuration))
id = 56 # int | Event id

try:
    # Deletes event
    api_instance.events_delete(id)
except ApiException as e:
    print("Exception when calling OCIEventsApi->events_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Event id | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **events_get_event**
> ApiCollectionInstanceEvent events_get_event(id, fields=fields)

Returns instance event

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
api_instance = pyodk.OCIEventsApi(pyodk.ApiClient(configuration))
id = 789 # int | Event id
fields = 'fields_example' # str | Response fields filter (optional)

try:
    # Returns instance event
    api_response = api_instance.events_get_event(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OCIEventsApi->events_get_event: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Event id | 
 **fields** | **str**| Response fields filter | [optional] 

### Return type

[**ApiCollectionInstanceEvent**](ApiCollectionInstanceEvent.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **events_get_events**
> ApiCollectionInstanceEvent events_get_events(type_ids=type_ids, status_ids=status_ids, date_from=date_from, date_to=date_to, page_size=page_size, page_number=page_number, order_by=order_by, fields=fields)

Returns all instances events

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
api_instance = pyodk.OCIEventsApi(pyodk.ApiClient(configuration))
type_ids = 'type_ids_example' # str | Type IDs (optional)
status_ids = 'status_ids_example' # str | Status IDs (optional)
date_from = '2013-10-20T19:20:30+01:00' # datetime | Date from (optional)
date_to = '2013-10-20T19:20:30+01:00' # datetime | Date to (optional)
page_size = 56 # int | Page size (optional)
page_number = 56 # int | Page number (optional)
order_by = 'order_by_example' # str | Order by (optional)
fields = 'fields_example' # str | Response fields filter (optional)

try:
    # Returns all instances events
    api_response = api_instance.events_get_events(type_ids=type_ids, status_ids=status_ids, date_from=date_from, date_to=date_to, page_size=page_size, page_number=page_number, order_by=order_by, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OCIEventsApi->events_get_events: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type_ids** | **str**| Type IDs | [optional] 
 **status_ids** | **str**| Status IDs | [optional] 
 **date_from** | **datetime**| Date from | [optional] 
 **date_to** | **datetime**| Date to | [optional] 
 **page_size** | **int**| Page size | [optional] 
 **page_number** | **int**| Page number | [optional] 
 **order_by** | **str**| Order by | [optional] 
 **fields** | **str**| Response fields filter | [optional] 

### Return type

[**ApiCollectionInstanceEvent**](ApiCollectionInstanceEvent.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instances_delete_events**
> instances_delete_events(id, command)

Deletes instance events

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
api_instance = pyodk.OCIEventsApi(pyodk.ApiClient(configuration))
id = 56 # int | Instance id
command = pyodk.DeleteEventsCommand() # DeleteEventsCommand | Delete events command

try:
    # Deletes instance events
    api_instance.instances_delete_events(id, command)
except ApiException as e:
    print("Exception when calling OCIEventsApi->instances_delete_events: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Instance id | 
 **command** | [**DeleteEventsCommand**](DeleteEventsCommand.md)| Delete events command | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instances_get_events**
> ApiCollectionInstanceEvent instances_get_events(id, user_id=user_id, date_from=date_from, date_to=date_to, operation_type_id=operation_type_id, page_size=page_size, page_number=page_number, order_by=order_by, fields=fields)

Returns instance events

Acceptable order values are: OperationType, User, Date, Instance, OperationStatus

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
api_instance = pyodk.OCIEventsApi(pyodk.ApiClient(configuration))
id = 56 # int | Instance identifier
user_id = 56 # int | User id (optional)
date_from = '2013-10-20T19:20:30+01:00' # datetime | Date from (optional)
date_to = '2013-10-20T19:20:30+01:00' # datetime | Date to (optional)
operation_type_id = 56 # int | Operation type id (optional)
page_size = 56 # int | Page size (optional)
page_number = 56 # int | Page number (optional)
order_by = 'order_by_example' # str | Order by (optional)
fields = 'fields_example' # str | Response fields filter (optional)

try:
    # Returns instance events
    api_response = api_instance.instances_get_events(id, user_id=user_id, date_from=date_from, date_to=date_to, operation_type_id=operation_type_id, page_size=page_size, page_number=page_number, order_by=order_by, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OCIEventsApi->instances_get_events: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Instance identifier | 
 **user_id** | **int**| User id | [optional] 
 **date_from** | **datetime**| Date from | [optional] 
 **date_to** | **datetime**| Date to | [optional] 
 **operation_type_id** | **int**| Operation type id | [optional] 
 **page_size** | **int**| Page size | [optional] 
 **page_number** | **int**| Page number | [optional] 
 **order_by** | **str**| Order by | [optional] 
 **fields** | **str**| Response fields filter | [optional] 

### Return type

[**ApiCollectionInstanceEvent**](ApiCollectionInstanceEvent.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

