# pyodk.OVSApi

All URIs are relative to *https://pl1-api.oktawave.com/services*

Method | HTTP request | Description
------------- | ------------- | -------------
[**disks_attach_to_instance**](OVSApi.md#disks_attach_to_instance) | **POST** /disks/{id}/attach_to_instance_ticket | Attach disk to instance
[**disks_change_subregion**](OVSApi.md#disks_change_subregion) | **POST** /disks/{id}/change_subregion_ticket | Change disk subregion
[**disks_change_tier**](OVSApi.md#disks_change_tier) | **POST** /disks/{id}/change_tier_ticket | Change disk tier
[**disks_delete**](OVSApi.md#disks_delete) | **DELETE** /disks/{id} | Delete disk
[**disks_detach_from_instance**](OVSApi.md#disks_detach_from_instance) | **POST** /disks/{id}/detach_from_instance_ticket | Detach disk from instance
[**disks_extend**](OVSApi.md#disks_extend) | **POST** /disks/{id}/extend_ticket | Extend disk
[**disks_get**](OVSApi.md#disks_get) | **GET** /disks/{id} | Returns disk by identifier
[**disks_get_disks**](OVSApi.md#disks_get_disks) | **GET** /disks | Returns disk list
[**disks_post**](OVSApi.md#disks_post) | **POST** /disks | Creates disk
[**disks_put**](OVSApi.md#disks_put) | **PUT** /disks/{id} | Update disk


# **disks_attach_to_instance**
> Ticket disks_attach_to_instance(id, instance_id)

Attach disk to instance

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
api_instance = pyodk.OVSApi(pyodk.ApiClient(configuration))
id = 56 # int | Disk id
instance_id = 56 # int | Instance id

try:
    # Attach disk to instance
    api_response = api_instance.disks_attach_to_instance(id, instance_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OVSApi->disks_attach_to_instance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Disk id | 
 **instance_id** | **int**| Instance id | 

### Return type

[**Ticket**](Ticket.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disks_change_subregion**
> Ticket disks_change_subregion(id, subregion_id)

Change disk subregion

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
api_instance = pyodk.OVSApi(pyodk.ApiClient(configuration))
id = 56 # int | Disk id
subregion_id = 56 # int | Subregion id

try:
    # Change disk subregion
    api_response = api_instance.disks_change_subregion(id, subregion_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OVSApi->disks_change_subregion: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Disk id | 
 **subregion_id** | **int**| Subregion id | 

### Return type

[**Ticket**](Ticket.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disks_change_tier**
> Ticket disks_change_tier(id, tier_id)

Change disk tier

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
api_instance = pyodk.OVSApi(pyodk.ApiClient(configuration))
id = 56 # int | Disk id
tier_id = 56 # int | Tier id

try:
    # Change disk tier
    api_response = api_instance.disks_change_tier(id, tier_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OVSApi->disks_change_tier: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Disk id | 
 **tier_id** | **int**| Tier id | 

### Return type

[**Ticket**](Ticket.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disks_delete**
> Ticket disks_delete(id)

Delete disk

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
api_instance = pyodk.OVSApi(pyodk.ApiClient(configuration))
id = 56 # int | Disk id

try:
    # Delete disk
    api_response = api_instance.disks_delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OVSApi->disks_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Disk id | 

### Return type

[**Ticket**](Ticket.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disks_detach_from_instance**
> Ticket disks_detach_from_instance(id, instance_id)

Detach disk from instance

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
api_instance = pyodk.OVSApi(pyodk.ApiClient(configuration))
id = 56 # int | Disk id
instance_id = 56 # int | Instance id

try:
    # Detach disk from instance
    api_response = api_instance.disks_detach_from_instance(id, instance_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OVSApi->disks_detach_from_instance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Disk id | 
 **instance_id** | **int**| Instance id | 

### Return type

[**Ticket**](Ticket.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disks_extend**
> Ticket disks_extend(id, space_capacity)

Extend disk

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
api_instance = pyodk.OVSApi(pyodk.ApiClient(configuration))
id = 56 # int | Disk id
space_capacity = 56 # int | Disk space capacity in GB

try:
    # Extend disk
    api_response = api_instance.disks_extend(id, space_capacity)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OVSApi->disks_extend: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Disk id | 
 **space_capacity** | **int**| Disk space capacity in GB | 

### Return type

[**Ticket**](Ticket.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disks_get**
> Disk disks_get(id, fields=fields)

Returns disk by identifier

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
api_instance = pyodk.OVSApi(pyodk.ApiClient(configuration))
id = 56 # int | Disk identifier
fields = 'fields_example' # str | Response fields filter (optional)

try:
    # Returns disk by identifier
    api_response = api_instance.disks_get(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OVSApi->disks_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Disk identifier | 
 **fields** | **str**| Response fields filter | [optional] 

### Return type

[**Disk**](Disk.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disks_get_disks**
> ApiCollectionDisk disks_get_disks(disk_type=disk_type, query=query, page_size=page_size, page_number=page_number, order_by=order_by, fields=fields)

Returns disk list

Acceptable order values are: SpaceCapacity, Name, Tier, IsShared, Subregion

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
api_instance = pyodk.OVSApi(pyodk.ApiClient(configuration))
disk_type = 'disk_type_example' # str | Disk type (optional)
query = 'query_example' # str | Query (optional)
page_size = 56 # int | Page size (optional)
page_number = 56 # int | Page number (optional)
order_by = 'order_by_example' # str | Order by (optional)
fields = 'fields_example' # str | Response fields filter (optional)

try:
    # Returns disk list
    api_response = api_instance.disks_get_disks(disk_type=disk_type, query=query, page_size=page_size, page_number=page_number, order_by=order_by, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OVSApi->disks_get_disks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **disk_type** | **str**| Disk type | [optional] 
 **query** | **str**| Query | [optional] 
 **page_size** | **int**| Page size | [optional] 
 **page_number** | **int**| Page number | [optional] 
 **order_by** | **str**| Order by | [optional] 
 **fields** | **str**| Response fields filter | [optional] 

### Return type

[**ApiCollectionDisk**](ApiCollectionDisk.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disks_post**
> Ticket disks_post(command)

Creates disk

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
api_instance = pyodk.OVSApi(pyodk.ApiClient(configuration))
command = pyodk.CreateDiskCommand() # CreateDiskCommand | Create disk command

try:
    # Creates disk
    api_response = api_instance.disks_post(command)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OVSApi->disks_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **command** | [**CreateDiskCommand**](CreateDiskCommand.md)| Create disk command | 

### Return type

[**Ticket**](Ticket.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disks_put**
> Ticket disks_put(id, command)

Update disk

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
api_instance = pyodk.OVSApi(pyodk.ApiClient(configuration))
id = 56 # int | Disk id
command = pyodk.UpdateDiskCommand() # UpdateDiskCommand | Update disk command

try:
    # Update disk
    api_response = api_instance.disks_put(id, command)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OVSApi->disks_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Disk id | 
 **command** | [**UpdateDiskCommand**](UpdateDiskCommand.md)| Update disk command | 

### Return type

[**Ticket**](Ticket.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

