# pyodk.OCISnapshotsApi

All URIs are relative to *https://pl1-api.oktawave.com/services*

Method | HTTP request | Description
------------- | ------------- | -------------
[**instances_get_snapshots**](OCISnapshotsApi.md#instances_get_snapshots) | **GET** /instances/{id}/snapshots | Returns instance snapshots
[**instances_post_snapshot**](OCISnapshotsApi.md#instances_post_snapshot) | **POST** /instances/{id}/snapshots | Creates snapshot
[**snapshots_delete**](OCISnapshotsApi.md#snapshots_delete) | **DELETE** /snapshots/{id} | Delete snapshot
[**snapshots_get**](OCISnapshotsApi.md#snapshots_get) | **GET** /snapshots | Returns snapshot collection
[**snapshots_get_0**](OCISnapshotsApi.md#snapshots_get_0) | **GET** /snapshots/{id} | Gets snapshot
[**snapshots_put**](OCISnapshotsApi.md#snapshots_put) | **PUT** /snapshots/{id} | Update snapshot
[**snapshots_restore**](OCISnapshotsApi.md#snapshots_restore) | **POST** /snapshots/{id}/restore_ticket | Restore snapshot


# **instances_get_snapshots**
> ApiCollectionSnapshot instances_get_snapshots(id, fields=fields)

Returns instance snapshots

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
api_instance = pyodk.OCISnapshotsApi(pyodk.ApiClient(configuration))
id = 56 # int | Instance identifier
fields = 'fields_example' # str | Response fields filter (optional)

try:
    # Returns instance snapshots
    api_response = api_instance.instances_get_snapshots(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OCISnapshotsApi->instances_get_snapshots: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Instance identifier | 
 **fields** | **str**| Response fields filter | [optional] 

### Return type

[**ApiCollectionSnapshot**](ApiCollectionSnapshot.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instances_post_snapshot**
> Ticket instances_post_snapshot(id, command)

Creates snapshot

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
api_instance = pyodk.OCISnapshotsApi(pyodk.ApiClient(configuration))
id = 56 # int | Instance id
command = pyodk.CreateUpdateSnapshotCommand() # CreateUpdateSnapshotCommand | Create snapshot command

try:
    # Creates snapshot
    api_response = api_instance.instances_post_snapshot(id, command)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OCISnapshotsApi->instances_post_snapshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Instance id | 
 **command** | [**CreateUpdateSnapshotCommand**](CreateUpdateSnapshotCommand.md)| Create snapshot command | 

### Return type

[**Ticket**](Ticket.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **snapshots_delete**
> Ticket snapshots_delete(id)

Delete snapshot

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
api_instance = pyodk.OCISnapshotsApi(pyodk.ApiClient(configuration))
id = 56 # int | Snapshot id

try:
    # Delete snapshot
    api_response = api_instance.snapshots_delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OCISnapshotsApi->snapshots_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Snapshot id | 

### Return type

[**Ticket**](Ticket.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **snapshots_get**
> ApiCollectionSnapshot snapshots_get(instance_id=instance_id, query=query, page_size=page_size, page_number=page_number, order_by=order_by, fields=fields)

Returns snapshot collection

Acceptable order values are: CreationDate, Description, IsCurrent, Name, Instance.

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
api_instance = pyodk.OCISnapshotsApi(pyodk.ApiClient(configuration))
instance_id = 56 # int | Instance id (optional)
query = 'query_example' # str | Query (optional)
page_size = 56 # int | Page size (optional)
page_number = 56 # int | Page number (optional)
order_by = 'order_by_example' # str | Order by (optional)
fields = 'fields_example' # str | Response fields filter (optional)

try:
    # Returns snapshot collection
    api_response = api_instance.snapshots_get(instance_id=instance_id, query=query, page_size=page_size, page_number=page_number, order_by=order_by, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OCISnapshotsApi->snapshots_get: %s\n" % e)
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

[**ApiCollectionSnapshot**](ApiCollectionSnapshot.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **snapshots_get_0**
> Snapshot snapshots_get_0(id, fields=fields)

Gets snapshot

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
api_instance = pyodk.OCISnapshotsApi(pyodk.ApiClient(configuration))
id = 56 # int | Snapshot id
fields = 'fields_example' # str | Response fields filter (optional)

try:
    # Gets snapshot
    api_response = api_instance.snapshots_get_0(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OCISnapshotsApi->snapshots_get_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Snapshot id | 
 **fields** | **str**| Response fields filter | [optional] 

### Return type

[**Snapshot**](Snapshot.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **snapshots_put**
> Snapshot snapshots_put(id, command)

Update snapshot

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
api_instance = pyodk.OCISnapshotsApi(pyodk.ApiClient(configuration))
id = 56 # int | Snapshot id
command = pyodk.CreateUpdateSnapshotCommand() # CreateUpdateSnapshotCommand | Update snapshot command

try:
    # Update snapshot
    api_response = api_instance.snapshots_put(id, command)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OCISnapshotsApi->snapshots_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Snapshot id | 
 **command** | [**CreateUpdateSnapshotCommand**](CreateUpdateSnapshotCommand.md)| Update snapshot command | 

### Return type

[**Snapshot**](Snapshot.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **snapshots_restore**
> Ticket snapshots_restore(id)

Restore snapshot

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
api_instance = pyodk.OCISnapshotsApi(pyodk.ApiClient(configuration))
id = 56 # int | Snapshot id

try:
    # Restore snapshot
    api_response = api_instance.snapshots_restore(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OCISnapshotsApi->snapshots_restore: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Snapshot id | 

### Return type

[**Ticket**](Ticket.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

