# pyodk.OCIApi

All URIs are relative to *https://pl1-api.oktawave.com/services*

Method | HTTP request | Description
------------- | ------------- | -------------
[**instances_change_name**](OCIApi.md#instances_change_name) | **POST** /instances/{id}/change_name_ticket | Change instance name
[**instances_change_subregion**](OCIApi.md#instances_change_subregion) | **POST** /instances/{id}/change_subregion_ticket | Change instance subregion
[**instances_change_type**](OCIApi.md#instances_change_type) | **POST** /instances/{id}/change_scsi_controllers_type_ticket | Change SCSI controllers type
[**instances_change_type_0**](OCIApi.md#instances_change_type_0) | **POST** /instances/{id}/change_type_ticket | Change instance type
[**instances_clone**](OCIApi.md#instances_clone) | **POST** /instances/{id}/clone_ticket | Clone instance
[**instances_convert_to_template**](OCIApi.md#instances_convert_to_template) | **POST** /instances/{id}/convert_to_template_ticket | Converts instance to template
[**instances_create_vnc_connection**](OCIApi.md#instances_create_vnc_connection) | **POST** /instances/{id}/remote_console_connection | Creates remote console connection
[**instances_delete**](OCIApi.md#instances_delete) | **DELETE** /instances/{id} | Delete instance
[**instances_delete_vnc_connection**](OCIApi.md#instances_delete_vnc_connection) | **DELETE** /instances/{id}/remote_console_connection | Deletes remote console connection
[**instances_get**](OCIApi.md#instances_get) | **GET** /instances | Returns instance list
[**instances_get_0**](OCIApi.md#instances_get_0) | **GET** /instances/{id} | Returns instance by identifier
[**instances_get_access_data**](OCIApi.md#instances_get_access_data) | **GET** /instances/{id}/access_data | Returns instance access data
[**instances_get_disks**](OCIApi.md#instances_get_disks) | **GET** /instances/{id}/disks | Returns instance disk list
[**instances_get_instance_init_script**](OCIApi.md#instances_get_instance_init_script) | **GET** /instances/{id}/init_script | Returns instance init script
[**instances_get_instance_software**](OCIApi.md#instances_get_instance_software) | **GET** /instances/{id}/software | Returns instance software
[**instances_get_instance_type**](OCIApi.md#instances_get_instance_type) | **GET** /instances/types/{id} | Returns instance type
[**instances_get_instances_types**](OCIApi.md#instances_get_instances_types) | **GET** /instances/types | Returns all available instances types
[**instances_get_screenshot**](OCIApi.md#instances_get_screenshot) | **GET** /instances/{id}/screenshot | Returns instance screenshot
[**instances_get_software**](OCIApi.md#instances_get_software) | **GET** /instances/software | Returns software
[**instances_get_ssh_keys**](OCIApi.md#instances_get_ssh_keys) | **GET** /instances/{id}/ssh_keys | Returns SSH keys uploaded to instances
[**instances_get_vnc_connection**](OCIApi.md#instances_get_vnc_connection) | **GET** /instances/{id}/remote_console_connection | Returns remote console connection
[**instances_post**](OCIApi.md#instances_post) | **POST** /instances | Creates instance
[**instances_power_off**](OCIApi.md#instances_power_off) | **POST** /instances/{id}/power_off_ticket | Power off instance
[**instances_power_on**](OCIApi.md#instances_power_on) | **POST** /instances/{id}/power_on_ticket | Power on instance
[**instances_reboot**](OCIApi.md#instances_reboot) | **POST** /instances/{id}/reboot_ticket | Reboot instance
[**instances_reset**](OCIApi.md#instances_reset) | **POST** /instances/{id}/reset_ticket | Reset instance
[**instances_shutdown**](OCIApi.md#instances_shutdown) | **POST** /instances/{id}/shutdown_ticket | Shutdown instance
[**instances_update_vnc_connection**](OCIApi.md#instances_update_vnc_connection) | **PUT** /instances/{id}/remote_console_connection | Updates remote console connection


# **instances_change_name**
> Ticket instances_change_name(id, name)

Change instance name

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
api_instance = pyodk.OCIApi(pyodk.ApiClient(configuration))
id = 56 # int | Instance identifier
name = 'name_example' # str | Name of an instance

try:
    # Change instance name
    api_response = api_instance.instances_change_name(id, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OCIApi->instances_change_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Instance identifier | 
 **name** | **str**| Name of an instance | 

### Return type

[**Ticket**](Ticket.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instances_change_subregion**
> Ticket instances_change_subregion(id, command)

Change instance subregion

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
api_instance = pyodk.OCIApi(pyodk.ApiClient(configuration))
id = 56 # int | Instance identifier
command = pyodk.ChangeInstanceSubregionCommand() # ChangeInstanceSubregionCommand | Change instance subregion command

try:
    # Change instance subregion
    api_response = api_instance.instances_change_subregion(id, command)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OCIApi->instances_change_subregion: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Instance identifier | 
 **command** | [**ChangeInstanceSubregionCommand**](ChangeInstanceSubregionCommand.md)| Change instance subregion command | 

### Return type

[**Ticket**](Ticket.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instances_change_type**
> Ticket instances_change_type(id, scsi_controller_type_id)

Change SCSI controllers type

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
api_instance = pyodk.OCIApi(pyodk.ApiClient(configuration))
id = 56 # int | Instance identifier
scsi_controller_type_id = 56 # int | Type id

try:
    # Change SCSI controllers type
    api_response = api_instance.instances_change_type(id, scsi_controller_type_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OCIApi->instances_change_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Instance identifier | 
 **scsi_controller_type_id** | **int**| Type id | 

### Return type

[**Ticket**](Ticket.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instances_change_type_0**
> Ticket instances_change_type_0(id, type_id)

Change instance type

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
api_instance = pyodk.OCIApi(pyodk.ApiClient(configuration))
id = 56 # int | Instance identifier
type_id = 56 # int | Type id

try:
    # Change instance type
    api_response = api_instance.instances_change_type_0(id, type_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OCIApi->instances_change_type_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Instance identifier | 
 **type_id** | **int**| Type id | 

### Return type

[**Ticket**](Ticket.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instances_clone**
> Ticket instances_clone(id, command)

Clone instance

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
api_instance = pyodk.OCIApi(pyodk.ApiClient(configuration))
id = 56 # int | Instance Id
command = pyodk.CloneInstanceCommand() # CloneInstanceCommand | Clone instance command

try:
    # Clone instance
    api_response = api_instance.instances_clone(id, command)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OCIApi->instances_clone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Instance Id | 
 **command** | [**CloneInstanceCommand**](CloneInstanceCommand.md)| Clone instance command | 

### Return type

[**Ticket**](Ticket.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instances_convert_to_template**
> Ticket instances_convert_to_template(id, command)

Converts instance to template

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
api_instance = pyodk.OCIApi(pyodk.ApiClient(configuration))
id = 56 # int | Instance identifier
command = pyodk.ConvertInstanceToTemplateCommand() # ConvertInstanceToTemplateCommand | Convert instance to template command

try:
    # Converts instance to template
    api_response = api_instance.instances_convert_to_template(id, command)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OCIApi->instances_convert_to_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Instance identifier | 
 **command** | [**ConvertInstanceToTemplateCommand**](ConvertInstanceToTemplateCommand.md)| Convert instance to template command | 

### Return type

[**Ticket**](Ticket.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instances_create_vnc_connection**
> VncConnection instances_create_vnc_connection(id, command)

Creates remote console connection

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
api_instance = pyodk.OCIApi(pyodk.ApiClient(configuration))
id = 56 # int | Instance id
command = pyodk.CreateUpdateVncConnectionCommand() # CreateUpdateVncConnectionCommand | Create remote console connection command

try:
    # Creates remote console connection
    api_response = api_instance.instances_create_vnc_connection(id, command)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OCIApi->instances_create_vnc_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Instance id | 
 **command** | [**CreateUpdateVncConnectionCommand**](CreateUpdateVncConnectionCommand.md)| Create remote console connection command | 

### Return type

[**VncConnection**](VncConnection.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instances_delete**
> Ticket instances_delete(id, deep=deep)

Delete instance

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
api_instance = pyodk.OCIApi(pyodk.ApiClient(configuration))
id = 56 # int | Instance identifie
deep = true # bool | Deletes also additional disks attached to instance (optional)

try:
    # Delete instance
    api_response = api_instance.instances_delete(id, deep=deep)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OCIApi->instances_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Instance identifie | 
 **deep** | **bool**| Deletes also additional disks attached to instance | [optional] 

### Return type

[**Ticket**](Ticket.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instances_delete_vnc_connection**
> Object instances_delete_vnc_connection(id)

Deletes remote console connection

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
api_instance = pyodk.OCIApi(pyodk.ApiClient(configuration))
id = 56 # int | Instance id

try:
    # Deletes remote console connection
    api_response = api_instance.instances_delete_vnc_connection(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OCIApi->instances_delete_vnc_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Instance id | 

### Return type

[**Object**](Object.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instances_get**
> ApiCollectionInstance instances_get(template_type_id=template_type_id, is_turned_on=is_turned_on, subregion_id=subregion_id, type_id=type_id, query=query, page_size=page_size, page_number=page_number, order_by=order_by, fields=fields)

Returns instance list

Acceptable order values are: Type, Status, CreationDate, Name.

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
api_instance = pyodk.OCIApi(pyodk.ApiClient(configuration))
template_type_id = 56 # int | Template type id eg marketplace, oci instance (optional)
is_turned_on = true # bool | Indicates wether an instance is turned on (optional)
subregion_id = 56 # int | Subregion Id (optional)
type_id = 56 # int | Type Id (optional)
query = 'query_example' # str | Query (optional)
page_size = 56 # int | Page size (optional)
page_number = 56 # int | Page number (optional)
order_by = 'order_by_example' # str | Order by (optional)
fields = 'fields_example' # str | Response fields filter (optional)

try:
    # Returns instance list
    api_response = api_instance.instances_get(template_type_id=template_type_id, is_turned_on=is_turned_on, subregion_id=subregion_id, type_id=type_id, query=query, page_size=page_size, page_number=page_number, order_by=order_by, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OCIApi->instances_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_type_id** | **int**| Template type id eg marketplace, oci instance | [optional] 
 **is_turned_on** | **bool**| Indicates wether an instance is turned on | [optional] 
 **subregion_id** | **int**| Subregion Id | [optional] 
 **type_id** | **int**| Type Id | [optional] 
 **query** | **str**| Query | [optional] 
 **page_size** | **int**| Page size | [optional] 
 **page_number** | **int**| Page number | [optional] 
 **order_by** | **str**| Order by | [optional] 
 **fields** | **str**| Response fields filter | [optional] 

### Return type

[**ApiCollectionInstance**](ApiCollectionInstance.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instances_get_0**
> Instance instances_get_0(id, fields=fields)

Returns instance by identifier

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
api_instance = pyodk.OCIApi(pyodk.ApiClient(configuration))
id = 56 # int | Instance identifier
fields = 'fields_example' # str | Response fields filter (optional)

try:
    # Returns instance by identifier
    api_response = api_instance.instances_get_0(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OCIApi->instances_get_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Instance identifier | 
 **fields** | **str**| Response fields filter | [optional] 

### Return type

[**Instance**](Instance.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instances_get_access_data**
> AccessData instances_get_access_data(id, fields=fields)

Returns instance access data

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
api_instance = pyodk.OCIApi(pyodk.ApiClient(configuration))
id = 56 # int | Instance id
fields = 'fields_example' # str | Response fields filter (optional)

try:
    # Returns instance access data
    api_response = api_instance.instances_get_access_data(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OCIApi->instances_get_access_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Instance id | 
 **fields** | **str**| Response fields filter | [optional] 

### Return type

[**AccessData**](AccessData.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instances_get_disks**
> ApiCollectionDisk instances_get_disks(id, disk_type=disk_type, query=query, page_size=page_size, page_number=page_number, order_by=order_by, fields=fields)

Returns instance disk list

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
api_instance = pyodk.OCIApi(pyodk.ApiClient(configuration))
id = 56 # int | Instance id
disk_type = 'disk_type_example' # str | Disk type (optional)
query = 'query_example' # str | Query (optional)
page_size = 56 # int | Page size (optional)
page_number = 56 # int | Page number (optional)
order_by = 'order_by_example' # str | Order by (optional)
fields = 'fields_example' # str | Response fields filter (optional)

try:
    # Returns instance disk list
    api_response = api_instance.instances_get_disks(id, disk_type=disk_type, query=query, page_size=page_size, page_number=page_number, order_by=order_by, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OCIApi->instances_get_disks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Instance id | 
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

# **instances_get_instance_init_script**
> str instances_get_instance_init_script(id, fields=fields)

Returns instance init script

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
api_instance = pyodk.OCIApi(pyodk.ApiClient(configuration))
id = 56 # int | 
fields = 'fields_example' # str | Response fields filter (optional)

try:
    # Returns instance init script
    api_response = api_instance.instances_get_instance_init_script(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OCIApi->instances_get_instance_init_script: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **fields** | **str**| Response fields filter | [optional] 

### Return type

**str**

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instances_get_instance_software**
> ApiCollectionSoftware instances_get_instance_software(id, fields=fields)

Returns instance software

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
api_instance = pyodk.OCIApi(pyodk.ApiClient(configuration))
id = 56 # int | 
fields = 'fields_example' # str | Response fields filter (optional)

try:
    # Returns instance software
    api_response = api_instance.instances_get_instance_software(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OCIApi->instances_get_instance_software: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **fields** | **str**| Response fields filter | [optional] 

### Return type

[**ApiCollectionSoftware**](ApiCollectionSoftware.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instances_get_instance_type**
> ApiCollectionInstanceType instances_get_instance_type(id, fields=fields)

Returns instance type

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
api_instance = pyodk.OCIApi(pyodk.ApiClient(configuration))
id = 56 # int | Instance type id
fields = 'fields_example' # str | Response fields filter (optional)

try:
    # Returns instance type
    api_response = api_instance.instances_get_instance_type(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OCIApi->instances_get_instance_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Instance type id | 
 **fields** | **str**| Response fields filter | [optional] 

### Return type

[**ApiCollectionInstanceType**](ApiCollectionInstanceType.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instances_get_instances_types**
> ApiCollectionInstanceType instances_get_instances_types(category_id=category_id, available_for_freemium=available_for_freemium, page_size=page_size, page_number=page_number, order_by=order_by, fields=fields)

Returns all available instances types

Acceptable order values are: Category, Cpu, Ram, Name.

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
api_instance = pyodk.OCIApi(pyodk.ApiClient(configuration))
category_id = 56 # int | Category id (optional)
available_for_freemium = true # bool | Is available for freemium (optional)
page_size = 56 # int | Page size (optional)
page_number = 56 # int | Page number (optional)
order_by = 'order_by_example' # str | Order by (optional)
fields = 'fields_example' # str | Response fields filter (optional)

try:
    # Returns all available instances types
    api_response = api_instance.instances_get_instances_types(category_id=category_id, available_for_freemium=available_for_freemium, page_size=page_size, page_number=page_number, order_by=order_by, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OCIApi->instances_get_instances_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **int**| Category id | [optional] 
 **available_for_freemium** | **bool**| Is available for freemium | [optional] 
 **page_size** | **int**| Page size | [optional] 
 **page_number** | **int**| Page number | [optional] 
 **order_by** | **str**| Order by | [optional] 
 **fields** | **str**| Response fields filter | [optional] 

### Return type

[**ApiCollectionInstanceType**](ApiCollectionInstanceType.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instances_get_screenshot**
> str instances_get_screenshot(id, width=width, height=height, fields=fields)

Returns instance screenshot

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
api_instance = pyodk.OCIApi(pyodk.ApiClient(configuration))
id = 56 # int | Instance id
width = 56 # int | The pixel width of the scaled image (optional)
height = 56 # int | The pixel height of the scaled image (optional)
fields = 'fields_example' # str | Response fields filter (optional)

try:
    # Returns instance screenshot
    api_response = api_instance.instances_get_screenshot(id, width=width, height=height, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OCIApi->instances_get_screenshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Instance id | 
 **width** | **int**| The pixel width of the scaled image | [optional] 
 **height** | **int**| The pixel height of the scaled image | [optional] 
 **fields** | **str**| Response fields filter | [optional] 

### Return type

**str**

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instances_get_software**
> ApiCollectionSoftware instances_get_software(fields=fields)

Returns software

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
api_instance = pyodk.OCIApi(pyodk.ApiClient(configuration))
fields = 'fields_example' # str | Response fields filter (optional)

try:
    # Returns software
    api_response = api_instance.instances_get_software(fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OCIApi->instances_get_software: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Response fields filter | [optional] 

### Return type

[**ApiCollectionSoftware**](ApiCollectionSoftware.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instances_get_ssh_keys**
> ApiCollectionInstanceSshKey instances_get_ssh_keys(id, fields=fields)

Returns SSH keys uploaded to instances

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
api_instance = pyodk.OCIApi(pyodk.ApiClient(configuration))
id = 56 # int | Instance id
fields = 'fields_example' # str | Response fields filter (optional)

try:
    # Returns SSH keys uploaded to instances
    api_response = api_instance.instances_get_ssh_keys(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OCIApi->instances_get_ssh_keys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Instance id | 
 **fields** | **str**| Response fields filter | [optional] 

### Return type

[**ApiCollectionInstanceSshKey**](ApiCollectionInstanceSshKey.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instances_get_vnc_connection**
> VncConnection instances_get_vnc_connection(id, fields=fields)

Returns remote console connection

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
api_instance = pyodk.OCIApi(pyodk.ApiClient(configuration))
id = 56 # int | Instance id
fields = 'fields_example' # str | Response fields filter (optional)

try:
    # Returns remote console connection
    api_response = api_instance.instances_get_vnc_connection(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OCIApi->instances_get_vnc_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Instance id | 
 **fields** | **str**| Response fields filter | [optional] 

### Return type

[**VncConnection**](VncConnection.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instances_post**
> Ticket instances_post(command)

Creates instance

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
api_instance = pyodk.OCIApi(pyodk.ApiClient(configuration))
command = pyodk.CreateInstanceCommand() # CreateInstanceCommand | Create instance command

try:
    # Creates instance
    api_response = api_instance.instances_post(command)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OCIApi->instances_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **command** | [**CreateInstanceCommand**](CreateInstanceCommand.md)| Create instance command | 

### Return type

[**Ticket**](Ticket.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instances_power_off**
> Ticket instances_power_off(id)

Power off instance

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
api_instance = pyodk.OCIApi(pyodk.ApiClient(configuration))
id = 56 # int | Instance identifier

try:
    # Power off instance
    api_response = api_instance.instances_power_off(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OCIApi->instances_power_off: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Instance identifier | 

### Return type

[**Ticket**](Ticket.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instances_power_on**
> Ticket instances_power_on(id)

Power on instance

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
api_instance = pyodk.OCIApi(pyodk.ApiClient(configuration))
id = 56 # int | Instance identifier

try:
    # Power on instance
    api_response = api_instance.instances_power_on(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OCIApi->instances_power_on: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Instance identifier | 

### Return type

[**Ticket**](Ticket.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instances_reboot**
> Ticket instances_reboot(id)

Reboot instance

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
api_instance = pyodk.OCIApi(pyodk.ApiClient(configuration))
id = 56 # int | Instance identifier

try:
    # Reboot instance
    api_response = api_instance.instances_reboot(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OCIApi->instances_reboot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Instance identifier | 

### Return type

[**Ticket**](Ticket.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instances_reset**
> Ticket instances_reset(id)

Reset instance

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
api_instance = pyodk.OCIApi(pyodk.ApiClient(configuration))
id = 56 # int | Instance identifier

try:
    # Reset instance
    api_response = api_instance.instances_reset(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OCIApi->instances_reset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Instance identifier | 

### Return type

[**Ticket**](Ticket.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instances_shutdown**
> Ticket instances_shutdown(id)

Shutdown instance

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
api_instance = pyodk.OCIApi(pyodk.ApiClient(configuration))
id = 56 # int | Instance identifier

try:
    # Shutdown instance
    api_response = api_instance.instances_shutdown(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OCIApi->instances_shutdown: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Instance identifier | 

### Return type

[**Ticket**](Ticket.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instances_update_vnc_connection**
> VncConnection instances_update_vnc_connection(id, command)

Updates remote console connection

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
api_instance = pyodk.OCIApi(pyodk.ApiClient(configuration))
id = 56 # int | Instance id
command = pyodk.CreateUpdateVncConnectionCommand() # CreateUpdateVncConnectionCommand | Update remote console connection command

try:
    # Updates remote console connection
    api_response = api_instance.instances_update_vnc_connection(id, command)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OCIApi->instances_update_vnc_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Instance id | 
 **command** | [**CreateUpdateVncConnectionCommand**](CreateUpdateVncConnectionCommand.md)| Update remote console connection command | 

### Return type

[**VncConnection**](VncConnection.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

