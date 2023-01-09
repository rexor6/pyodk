# pyodk.OCIGroupsApi

All URIs are relative to *https://pl1-api.oktawave.com/services*

Method | HTTP request | Description
------------- | ------------- | -------------
[**groups_change_assignments_in_group**](OCIGroupsApi.md#groups_change_assignments_in_group) | **PUT** /groups/{id}/assignments | Changes group assignments
[**groups_create**](OCIGroupsApi.md#groups_create) | **POST** /groups | Creates group
[**groups_create_container_scheduler**](OCIGroupsApi.md#groups_create_container_scheduler) | **POST** /groups/{id}/schedulers | Creates a group scheduler
[**groups_delete**](OCIGroupsApi.md#groups_delete) | **DELETE** /groups/{id} | Deletes group
[**groups_delete_group_scheduler**](OCIGroupsApi.md#groups_delete_group_scheduler) | **DELETE** /groups/schedulers/{id} | Deletes group scheduler
[**groups_get_assignments_in_group**](OCIGroupsApi.md#groups_get_assignments_in_group) | **GET** /groups/{id}/assignments | Returns group assignments
[**groups_get_group**](OCIGroupsApi.md#groups_get_group) | **GET** /groups/{id} | Returns group
[**groups_get_group_autoscaler**](OCIGroupsApi.md#groups_get_group_autoscaler) | **GET** /groups/{id}/autoscaler | Returns group autoscaler settings
[**groups_get_group_scheduler**](OCIGroupsApi.md#groups_get_group_scheduler) | **GET** /groups/schedulers/{id} | Returns group scheduler
[**groups_get_group_schedulers**](OCIGroupsApi.md#groups_get_group_schedulers) | **GET** /groups/{id}/schedulers | Returns group schedulers
[**groups_get_groups**](OCIGroupsApi.md#groups_get_groups) | **GET** /groups | Returns a list of groups
[**groups_get_load_balancers**](OCIGroupsApi.md#groups_get_load_balancers) | **GET** /groups/load_balancers | Gets load balancers
[**groups_set_group_autoscaler**](OCIGroupsApi.md#groups_set_group_autoscaler) | **POST** /groups/{id}/autoscaler | Sets group autoscaler
[**groups_turnoff_group_autoscaler**](OCIGroupsApi.md#groups_turnoff_group_autoscaler) | **DELETE** /groups/{id}/autoscaler | Turns off group autoscaler
[**groups_update**](OCIGroupsApi.md#groups_update) | **PUT** /groups/{id} | Updates group
[**groups_update_group_scheduler**](OCIGroupsApi.md#groups_update_group_scheduler) | **PUT** /groups/schedulers/{id} | Updates a group scheduler
[**instances_get_groups**](OCIGroupsApi.md#instances_get_groups) | **GET** /instances/{id}/groups | Returns a list of instance groups
[**load_balancers_change_service_status**](OCIGroupsApi.md#load_balancers_change_service_status) | **PUT** /groups/{id}/load_balancer/services | Changes load balancer service state
[**load_balancers_create**](OCIGroupsApi.md#load_balancers_create) | **POST** /groups/{id}/load_balancer | Create load balancer for group
[**load_balancers_delete**](OCIGroupsApi.md#load_balancers_delete) | **DELETE** /groups/{id}/load_balancer | Delete load balancer
[**load_balancers_get_load_balancer**](OCIGroupsApi.md#load_balancers_get_load_balancer) | **GET** /groups/{id}/load_balancer | Gets load balancer for group
[**load_balancers_get_load_balancer_details**](OCIGroupsApi.md#load_balancers_get_load_balancer_details) | **GET** /groups/{id}/load_balancer/details | Gets load balancer detail for group
[**load_balancers_update**](OCIGroupsApi.md#load_balancers_update) | **PUT** /groups/{id}/load_balancer | Update load balancer for group


# **groups_change_assignments_in_group**
> ApiCollectionGroupAssignment groups_change_assignments_in_group(id, command)

Changes group assignments

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
api_instance = pyodk.OCIGroupsApi(pyodk.ApiClient(configuration))
id = 56 # int | Id of a group
command = pyodk.ChangeContainerAssignmentsCommand() # ChangeContainerAssignmentsCommand | Change group assignments command

try:
    # Changes group assignments
    api_response = api_instance.groups_change_assignments_in_group(id, command)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OCIGroupsApi->groups_change_assignments_in_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of a group | 
 **command** | [**ChangeContainerAssignmentsCommand**](ChangeContainerAssignmentsCommand.md)| Change group assignments command | 

### Return type

[**ApiCollectionGroupAssignment**](ApiCollectionGroupAssignment.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_create**
> Group groups_create(command)

Creates group

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
api_instance = pyodk.OCIGroupsApi(pyodk.ApiClient(configuration))
command = pyodk.CreateGroupCommand() # CreateGroupCommand | Create group command

try:
    # Creates group
    api_response = api_instance.groups_create(command)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OCIGroupsApi->groups_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **command** | [**CreateGroupCommand**](CreateGroupCommand.md)| Create group command | 

### Return type

[**Group**](Group.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_create_container_scheduler**
> GroupScheduler groups_create_container_scheduler(id, command)

Creates a group scheduler

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
api_instance = pyodk.OCIGroupsApi(pyodk.ApiClient(configuration))
id = 56 # int | Group Id
command = pyodk.CreateUpdateGroupSchedulerCommand() # CreateUpdateGroupSchedulerCommand | Create group scheduler command

try:
    # Creates a group scheduler
    api_response = api_instance.groups_create_container_scheduler(id, command)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OCIGroupsApi->groups_create_container_scheduler: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Group Id | 
 **command** | [**CreateUpdateGroupSchedulerCommand**](CreateUpdateGroupSchedulerCommand.md)| Create group scheduler command | 

### Return type

[**GroupScheduler**](GroupScheduler.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_delete**
> Object groups_delete(id)

Deletes group

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
api_instance = pyodk.OCIGroupsApi(pyodk.ApiClient(configuration))
id = 56 # int | Id of a group

try:
    # Deletes group
    api_response = api_instance.groups_delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OCIGroupsApi->groups_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of a group | 

### Return type

[**Object**](Object.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_delete_group_scheduler**
> Object groups_delete_group_scheduler(id)

Deletes group scheduler

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
api_instance = pyodk.OCIGroupsApi(pyodk.ApiClient(configuration))
id = 56 # int | Id of a group scheduler

try:
    # Deletes group scheduler
    api_response = api_instance.groups_delete_group_scheduler(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OCIGroupsApi->groups_delete_group_scheduler: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of a group scheduler | 

### Return type

[**Object**](Object.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_get_assignments_in_group**
> ApiCollectionGroupAssignment groups_get_assignments_in_group(id, fields=fields)

Returns group assignments

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
api_instance = pyodk.OCIGroupsApi(pyodk.ApiClient(configuration))
id = 56 # int | Id of a group
fields = 'fields_example' # str | Response fields filter (optional)

try:
    # Returns group assignments
    api_response = api_instance.groups_get_assignments_in_group(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OCIGroupsApi->groups_get_assignments_in_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of a group | 
 **fields** | **str**| Response fields filter | [optional] 

### Return type

[**ApiCollectionGroupAssignment**](ApiCollectionGroupAssignment.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_get_group**
> Group groups_get_group(id, fields=fields)

Returns group

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
api_instance = pyodk.OCIGroupsApi(pyodk.ApiClient(configuration))
id = 56 # int | Id of group
fields = 'fields_example' # str | Response fields filter (optional)

try:
    # Returns group
    api_response = api_instance.groups_get_group(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OCIGroupsApi->groups_get_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of group | 
 **fields** | **str**| Response fields filter | [optional] 

### Return type

[**Group**](Group.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_get_group_autoscaler**
> GroupAutoscaler groups_get_group_autoscaler(id, fields=fields)

Returns group autoscaler settings

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
api_instance = pyodk.OCIGroupsApi(pyodk.ApiClient(configuration))
id = 56 # int | Id of a group
fields = 'fields_example' # str | Response fields filter (optional)

try:
    # Returns group autoscaler settings
    api_response = api_instance.groups_get_group_autoscaler(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OCIGroupsApi->groups_get_group_autoscaler: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of a group | 
 **fields** | **str**| Response fields filter | [optional] 

### Return type

[**GroupAutoscaler**](GroupAutoscaler.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_get_group_scheduler**
> GroupScheduler groups_get_group_scheduler(id, fields=fields)

Returns group scheduler

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
api_instance = pyodk.OCIGroupsApi(pyodk.ApiClient(configuration))
id = 56 # int | Group scheduler Id
fields = 'fields_example' # str | Response fields filter (optional)

try:
    # Returns group scheduler
    api_response = api_instance.groups_get_group_scheduler(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OCIGroupsApi->groups_get_group_scheduler: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Group scheduler Id | 
 **fields** | **str**| Response fields filter | [optional] 

### Return type

[**GroupScheduler**](GroupScheduler.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_get_group_schedulers**
> ApiCollectionGroupScheduler groups_get_group_schedulers(id, fields=fields)

Returns group schedulers

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
api_instance = pyodk.OCIGroupsApi(pyodk.ApiClient(configuration))
id = 56 # int | Id of a group
fields = 'fields_example' # str | Response fields filter (optional)

try:
    # Returns group schedulers
    api_response = api_instance.groups_get_group_schedulers(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OCIGroupsApi->groups_get_group_schedulers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of a group | 
 **fields** | **str**| Response fields filter | [optional] 

### Return type

[**ApiCollectionGroupScheduler**](ApiCollectionGroupScheduler.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_get_groups**
> ApiCollectionGroup groups_get_groups(page_size=page_size, page_number=page_number, order_by=order_by, fields=fields)

Returns a list of groups

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
api_instance = pyodk.OCIGroupsApi(pyodk.ApiClient(configuration))
page_size = 56 # int | Page size (optional)
page_number = 56 # int | Page number (optional)
order_by = 'order_by_example' # str | Order by (optional)
fields = 'fields_example' # str | Response fields filter (optional)

try:
    # Returns a list of groups
    api_response = api_instance.groups_get_groups(page_size=page_size, page_number=page_number, order_by=order_by, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OCIGroupsApi->groups_get_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| Page size | [optional] 
 **page_number** | **int**| Page number | [optional] 
 **order_by** | **str**| Order by | [optional] 
 **fields** | **str**| Response fields filter | [optional] 

### Return type

[**ApiCollectionGroup**](ApiCollectionGroup.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_get_load_balancers**
> ApiCollectionLoadBalancer groups_get_load_balancers(page_size=page_size, page_number=page_number, order_by=order_by, fields=fields)

Gets load balancers

Acceptable order values are: GroupName

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
api_instance = pyodk.OCIGroupsApi(pyodk.ApiClient(configuration))
page_size = 56 # int | Page size (optional)
page_number = 56 # int | Page number (optional)
order_by = 'order_by_example' # str | Order by (optional)
fields = 'fields_example' # str | Response fields filter (optional)

try:
    # Gets load balancers
    api_response = api_instance.groups_get_load_balancers(page_size=page_size, page_number=page_number, order_by=order_by, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OCIGroupsApi->groups_get_load_balancers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| Page size | [optional] 
 **page_number** | **int**| Page number | [optional] 
 **order_by** | **str**| Order by | [optional] 
 **fields** | **str**| Response fields filter | [optional] 

### Return type

[**ApiCollectionLoadBalancer**](ApiCollectionLoadBalancer.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_set_group_autoscaler**
> GroupAutoscaler groups_set_group_autoscaler(id, command)

Sets group autoscaler

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
api_instance = pyodk.OCIGroupsApi(pyodk.ApiClient(configuration))
id = 56 # int | Id of a group
command = pyodk.SetGroupAutoscalerCommand() # SetGroupAutoscalerCommand | Set group autoscaler command

try:
    # Sets group autoscaler
    api_response = api_instance.groups_set_group_autoscaler(id, command)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OCIGroupsApi->groups_set_group_autoscaler: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of a group | 
 **command** | [**SetGroupAutoscalerCommand**](SetGroupAutoscalerCommand.md)| Set group autoscaler command | 

### Return type

[**GroupAutoscaler**](GroupAutoscaler.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_turnoff_group_autoscaler**
> Object groups_turnoff_group_autoscaler(id)

Turns off group autoscaler

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
api_instance = pyodk.OCIGroupsApi(pyodk.ApiClient(configuration))
id = 56 # int | Id of a group

try:
    # Turns off group autoscaler
    api_response = api_instance.groups_turnoff_group_autoscaler(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OCIGroupsApi->groups_turnoff_group_autoscaler: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of a group | 

### Return type

[**Object**](Object.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_update**
> Group groups_update(id, command)

Updates group

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
api_instance = pyodk.OCIGroupsApi(pyodk.ApiClient(configuration))
id = 56 # int | Id of a group
command = pyodk.CreateGroupCommand() # CreateGroupCommand | Update group command

try:
    # Updates group
    api_response = api_instance.groups_update(id, command)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OCIGroupsApi->groups_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of a group | 
 **command** | [**CreateGroupCommand**](CreateGroupCommand.md)| Update group command | 

### Return type

[**Group**](Group.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_update_group_scheduler**
> GroupScheduler groups_update_group_scheduler(id, command)

Updates a group scheduler

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
api_instance = pyodk.OCIGroupsApi(pyodk.ApiClient(configuration))
id = 56 # int | Group scheduler Id
command = pyodk.CreateUpdateGroupSchedulerCommand() # CreateUpdateGroupSchedulerCommand | Create group scheduler command

try:
    # Updates a group scheduler
    api_response = api_instance.groups_update_group_scheduler(id, command)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OCIGroupsApi->groups_update_group_scheduler: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Group scheduler Id | 
 **command** | [**CreateUpdateGroupSchedulerCommand**](CreateUpdateGroupSchedulerCommand.md)| Create group scheduler command | 

### Return type

[**GroupScheduler**](GroupScheduler.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instances_get_groups**
> ApiCollectionGroup instances_get_groups(id, fields=fields)

Returns a list of instance groups

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
api_instance = pyodk.OCIGroupsApi(pyodk.ApiClient(configuration))
id = 56 # int | Instance id
fields = 'fields_example' # str | Response fields filter (optional)

try:
    # Returns a list of instance groups
    api_response = api_instance.instances_get_groups(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OCIGroupsApi->instances_get_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Instance id | 
 **fields** | **str**| Response fields filter | [optional] 

### Return type

[**ApiCollectionGroup**](ApiCollectionGroup.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **load_balancers_change_service_status**
> LoadBalancer load_balancers_change_service_status(id, command)

Changes load balancer service state

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
api_instance = pyodk.OCIGroupsApi(pyodk.ApiClient(configuration))
id = 56 # int | Id of a group
command = pyodk.ChangeContainerServiceStateCommand() # ChangeContainerServiceStateCommand | Change service status command

try:
    # Changes load balancer service state
    api_response = api_instance.load_balancers_change_service_status(id, command)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OCIGroupsApi->load_balancers_change_service_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of a group | 
 **command** | [**ChangeContainerServiceStateCommand**](ChangeContainerServiceStateCommand.md)| Change service status command | 

### Return type

[**LoadBalancer**](LoadBalancer.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **load_balancers_create**
> LoadBalancer load_balancers_create(id, command)

Create load balancer for group

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
api_instance = pyodk.OCIGroupsApi(pyodk.ApiClient(configuration))
id = 56 # int | Group id
command = pyodk.SetLoadBalancerCommand() # SetLoadBalancerCommand | Create load balancer command

try:
    # Create load balancer for group
    api_response = api_instance.load_balancers_create(id, command)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OCIGroupsApi->load_balancers_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Group id | 
 **command** | [**SetLoadBalancerCommand**](SetLoadBalancerCommand.md)| Create load balancer command | 

### Return type

[**LoadBalancer**](LoadBalancer.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **load_balancers_delete**
> Object load_balancers_delete(id)

Delete load balancer

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
api_instance = pyodk.OCIGroupsApi(pyodk.ApiClient(configuration))
id = 56 # int | Group id

try:
    # Delete load balancer
    api_response = api_instance.load_balancers_delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OCIGroupsApi->load_balancers_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Group id | 

### Return type

[**Object**](Object.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **load_balancers_get_load_balancer**
> LoadBalancer load_balancers_get_load_balancer(id, fields=fields)

Gets load balancer for group

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
api_instance = pyodk.OCIGroupsApi(pyodk.ApiClient(configuration))
id = 56 # int | Group id
fields = 'fields_example' # str | Response fields filter (optional)

try:
    # Gets load balancer for group
    api_response = api_instance.load_balancers_get_load_balancer(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OCIGroupsApi->load_balancers_get_load_balancer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Group id | 
 **fields** | **str**| Response fields filter | [optional] 

### Return type

[**LoadBalancer**](LoadBalancer.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **load_balancers_get_load_balancer_details**
> LoadBalancer load_balancers_get_load_balancer_details(id, fields=fields)

Gets load balancer detail for group

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
api_instance = pyodk.OCIGroupsApi(pyodk.ApiClient(configuration))
id = 56 # int | Group id
fields = 'fields_example' # str | Response fields filter (optional)

try:
    # Gets load balancer detail for group
    api_response = api_instance.load_balancers_get_load_balancer_details(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OCIGroupsApi->load_balancers_get_load_balancer_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Group id | 
 **fields** | **str**| Response fields filter | [optional] 

### Return type

[**LoadBalancer**](LoadBalancer.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **load_balancers_update**
> LoadBalancer load_balancers_update(id, command)

Update load balancer for group

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
api_instance = pyodk.OCIGroupsApi(pyodk.ApiClient(configuration))
id = 56 # int | Group id
command = pyodk.SetLoadBalancerCommand() # SetLoadBalancerCommand | Update load balancer command

try:
    # Update load balancer for group
    api_response = api_instance.load_balancers_update(id, command)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OCIGroupsApi->load_balancers_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Group id | 
 **command** | [**SetLoadBalancerCommand**](SetLoadBalancerCommand.md)| Update load balancer command | 

### Return type

[**LoadBalancer**](LoadBalancer.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

