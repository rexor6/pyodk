# pyodk.OCIInterfacesApi

All URIs are relative to *https://pl1-api.oktawave.com/services*

Method | HTTP request | Description
------------- | ------------- | -------------
[**instances_attach_opn**](OCIInterfacesApi.md#instances_attach_opn) | **POST** /instances/{id}/attach_opn_ticket | Attach instance to OPN
[**instances_book_new_ip**](OCIInterfacesApi.md#instances_book_new_ip) | **POST** /instances/ip_addresses | Book new IP address
[**instances_change_opn**](OCIInterfacesApi.md#instances_change_opn) | **POST** /instances/{id}/change_opn_ticket | Change OPN on network interface
[**instances_delete_ip**](OCIInterfacesApi.md#instances_delete_ip) | **DELETE** /instances/ip_addresses/{id} | Deletes IP address
[**instances_detach_from_opn**](OCIInterfacesApi.md#instances_detach_from_opn) | **POST** /instances/{id}/detach_opn_ticket | Detach instance from OPN
[**instances_get_all_network_interfaces**](OCIInterfacesApi.md#instances_get_all_network_interfaces) | **GET** /instances/interfaces | Returns all network interfaces
[**instances_get_instance_ip**](OCIInterfacesApi.md#instances_get_instance_ip) | **GET** /instances/ip_addresses/{id} | Returns IP by id
[**instances_get_instance_ips**](OCIInterfacesApi.md#instances_get_instance_ips) | **GET** /instances/{id}/ip_addresses | Returns instance public ip list
[**instances_get_instance_network_interfaces**](OCIInterfacesApi.md#instances_get_instance_network_interfaces) | **GET** /instances/{id}/interfaces | Returns instance network interfaces
[**instances_get_ips**](OCIInterfacesApi.md#instances_get_ips) | **GET** /instances/ip_addresses | Returns public ip list
[**instances_get_opns**](OCIInterfacesApi.md#instances_get_opns) | **GET** /instances/{id}/opns | Returns instance OPN&#39;s
[**instances_post_attach_ip_ticket**](OCIInterfacesApi.md#instances_post_attach_ip_ticket) | **POST** /instances/{id}/attach_ip_ticket | Attach public IP to instance
[**instances_post_detach_ip_ticket**](OCIInterfacesApi.md#instances_post_detach_ip_ticket) | **POST** /instances/{id}/detach_ip_ticket | Detach public IP from instance
[**instances_update_ip**](OCIInterfacesApi.md#instances_update_ip) | **PUT** /instances/ip_addresses/{id} | Updates IP address


# **instances_attach_opn**
> Ticket instances_attach_opn(id, command)

Attach instance to OPN

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
api_instance = pyodk.OCIInterfacesApi(pyodk.ApiClient(configuration))
id = 56 # int | Instance identifier
command = pyodk.AttachInstanceToOpnCommand() # AttachInstanceToOpnCommand | Attach instance to OPN command

try:
    # Attach instance to OPN
    api_response = api_instance.instances_attach_opn(id, command)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OCIInterfacesApi->instances_attach_opn: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Instance identifier | 
 **command** | [**AttachInstanceToOpnCommand**](AttachInstanceToOpnCommand.md)| Attach instance to OPN command | 

### Return type

[**Ticket**](Ticket.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instances_book_new_ip**
> Ip instances_book_new_ip(command)

Book new IP address

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
api_instance = pyodk.OCIInterfacesApi(pyodk.ApiClient(configuration))
command = pyodk.BookIpCommand() # BookIpCommand | 

try:
    # Book new IP address
    api_response = api_instance.instances_book_new_ip(command)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OCIInterfacesApi->instances_book_new_ip: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **command** | [**BookIpCommand**](BookIpCommand.md)|  | 

### Return type

[**Ip**](Ip.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instances_change_opn**
> Ticket instances_change_opn(id, command)

Change OPN on network interface

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
api_instance = pyodk.OCIInterfacesApi(pyodk.ApiClient(configuration))
id = 56 # int | Instance identifier
command = pyodk.ChangeOpnCommand() # ChangeOpnCommand | Change OPN command

try:
    # Change OPN on network interface
    api_response = api_instance.instances_change_opn(id, command)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OCIInterfacesApi->instances_change_opn: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Instance identifier | 
 **command** | [**ChangeOpnCommand**](ChangeOpnCommand.md)| Change OPN command | 

### Return type

[**Ticket**](Ticket.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instances_delete_ip**
> Object instances_delete_ip(id)

Deletes IP address

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
api_instance = pyodk.OCIInterfacesApi(pyodk.ApiClient(configuration))
id = 56 # int | IP address identifier

try:
    # Deletes IP address
    api_response = api_instance.instances_delete_ip(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OCIInterfacesApi->instances_delete_ip: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| IP address identifier | 

### Return type

[**Object**](Object.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instances_detach_from_opn**
> Ticket instances_detach_from_opn(id, command)

Detach instance from OPN

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
api_instance = pyodk.OCIInterfacesApi(pyodk.ApiClient(configuration))
id = 56 # int | Instance identifier
command = pyodk.DetachInstanceFromOpnCommand() # DetachInstanceFromOpnCommand | Detach instance from OPN command

try:
    # Detach instance from OPN
    api_response = api_instance.instances_detach_from_opn(id, command)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OCIInterfacesApi->instances_detach_from_opn: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Instance identifier | 
 **command** | [**DetachInstanceFromOpnCommand**](DetachInstanceFromOpnCommand.md)| Detach instance from OPN command | 

### Return type

[**Ticket**](Ticket.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instances_get_all_network_interfaces**
> NetworkInterface instances_get_all_network_interfaces(page_size=page_size, page_number=page_number, order_by=order_by, fields=fields)

Returns all network interfaces

Acceptable order values are: MacAddress, Instance, Opn, Address

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
api_instance = pyodk.OCIInterfacesApi(pyodk.ApiClient(configuration))
page_size = 56 # int | Page size (optional)
page_number = 56 # int | Page number (optional)
order_by = 'order_by_example' # str | Order by (optional)
fields = 'fields_example' # str | Response fields filter (optional)

try:
    # Returns all network interfaces
    api_response = api_instance.instances_get_all_network_interfaces(page_size=page_size, page_number=page_number, order_by=order_by, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OCIInterfacesApi->instances_get_all_network_interfaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| Page size | [optional] 
 **page_number** | **int**| Page number | [optional] 
 **order_by** | **str**| Order by | [optional] 
 **fields** | **str**| Response fields filter | [optional] 

### Return type

[**NetworkInterface**](NetworkInterface.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instances_get_instance_ip**
> Ip instances_get_instance_ip(id, fields=fields)

Returns IP by id

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
api_instance = pyodk.OCIInterfacesApi(pyodk.ApiClient(configuration))
id = 56 # int | 
fields = 'fields_example' # str | Response fields filter (optional)

try:
    # Returns IP by id
    api_response = api_instance.instances_get_instance_ip(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OCIInterfacesApi->instances_get_instance_ip: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **fields** | **str**| Response fields filter | [optional] 

### Return type

[**Ip**](Ip.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instances_get_instance_ips**
> ApiCollectionIp instances_get_instance_ips(id, page_size=page_size, page_number=page_number, order_by=order_by, fields=fields)

Returns instance public ip list

Acceptable order values are: Address, Subregion, Comment, Type

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
api_instance = pyodk.OCIInterfacesApi(pyodk.ApiClient(configuration))
id = 56 # int | Instance id
page_size = 56 # int | Page size (optional)
page_number = 56 # int | Page number (optional)
order_by = 'order_by_example' # str | Order by (optional)
fields = 'fields_example' # str | Response fields filter (optional)

try:
    # Returns instance public ip list
    api_response = api_instance.instances_get_instance_ips(id, page_size=page_size, page_number=page_number, order_by=order_by, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OCIInterfacesApi->instances_get_instance_ips: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Instance id | 
 **page_size** | **int**| Page size | [optional] 
 **page_number** | **int**| Page number | [optional] 
 **order_by** | **str**| Order by | [optional] 
 **fields** | **str**| Response fields filter | [optional] 

### Return type

[**ApiCollectionIp**](ApiCollectionIp.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instances_get_instance_network_interfaces**
> NetworkInterface instances_get_instance_network_interfaces(id, page_size=page_size, page_number=page_number, order_by=order_by, fields=fields)

Returns instance network interfaces

Acceptable order values are: MacAddress, Instance, Opn, Address

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
api_instance = pyodk.OCIInterfacesApi(pyodk.ApiClient(configuration))
id = 56 # int | Instance id
page_size = 56 # int | Page size (optional)
page_number = 56 # int | Page number (optional)
order_by = 'order_by_example' # str | Order by (optional)
fields = 'fields_example' # str | Response fields filter (optional)

try:
    # Returns instance network interfaces
    api_response = api_instance.instances_get_instance_network_interfaces(id, page_size=page_size, page_number=page_number, order_by=order_by, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OCIInterfacesApi->instances_get_instance_network_interfaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Instance id | 
 **page_size** | **int**| Page size | [optional] 
 **page_number** | **int**| Page number | [optional] 
 **order_by** | **str**| Order by | [optional] 
 **fields** | **str**| Response fields filter | [optional] 

### Return type

[**NetworkInterface**](NetworkInterface.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instances_get_ips**
> ApiCollectionIp instances_get_ips(instance_id=instance_id, only_free=only_free, page_size=page_size, page_number=page_number, order_by=order_by, fields=fields)

Returns public ip list

Acceptable order values are: Address, Subregion, Comment, Type.

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
api_instance = pyodk.OCIInterfacesApi(pyodk.ApiClient(configuration))
instance_id = 56 # int | Instance id (optional)
only_free = true # bool | Only free (optional)
page_size = 56 # int | Page size (optional)
page_number = 56 # int | Page number (optional)
order_by = 'order_by_example' # str | Order by (optional)
fields = 'fields_example' # str | Response fields filter (optional)

try:
    # Returns public ip list
    api_response = api_instance.instances_get_ips(instance_id=instance_id, only_free=only_free, page_size=page_size, page_number=page_number, order_by=order_by, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OCIInterfacesApi->instances_get_ips: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **int**| Instance id | [optional] 
 **only_free** | **bool**| Only free | [optional] 
 **page_size** | **int**| Page size | [optional] 
 **page_number** | **int**| Page number | [optional] 
 **order_by** | **str**| Order by | [optional] 
 **fields** | **str**| Response fields filter | [optional] 

### Return type

[**ApiCollectionIp**](ApiCollectionIp.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instances_get_opns**
> ApiCollectionOpn instances_get_opns(id, query=query, page_size=page_size, page_number=page_number, order_by=order_by, fields=fields)

Returns instance OPN's

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
api_instance = pyodk.OCIInterfacesApi(pyodk.ApiClient(configuration))
id = 56 # int | Instance id
query = 'query_example' # str | Query (optional)
page_size = 56 # int | Page size (optional)
page_number = 56 # int | Page number (optional)
order_by = 'order_by_example' # str | Order by (optional)
fields = 'fields_example' # str | Response fields filter (optional)

try:
    # Returns instance OPN's
    api_response = api_instance.instances_get_opns(id, query=query, page_size=page_size, page_number=page_number, order_by=order_by, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OCIInterfacesApi->instances_get_opns: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Instance id | 
 **query** | **str**| Query | [optional] 
 **page_size** | **int**| Page size | [optional] 
 **page_number** | **int**| Page number | [optional] 
 **order_by** | **str**| Order by | [optional] 
 **fields** | **str**| Response fields filter | [optional] 

### Return type

[**ApiCollectionOpn**](ApiCollectionOpn.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instances_post_attach_ip_ticket**
> Ticket instances_post_attach_ip_ticket(id, ip_id=ip_id, ip_v6=ip_v6)

Attach public IP to instance

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
api_instance = pyodk.OCIInterfacesApi(pyodk.ApiClient(configuration))
id = 56 # int | Instance identifier
ip_id = 56 # int | IP address identifier. Optional value, if null random ip will be attached. (optional)
ip_v6 = true # bool | If attach IPv6 only. Optional value, if null IPv4 and IPv6 will be attached. (optional)

try:
    # Attach public IP to instance
    api_response = api_instance.instances_post_attach_ip_ticket(id, ip_id=ip_id, ip_v6=ip_v6)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OCIInterfacesApi->instances_post_attach_ip_ticket: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Instance identifier | 
 **ip_id** | **int**| IP address identifier. Optional value, if null random ip will be attached. | [optional] 
 **ip_v6** | **bool**| If attach IPv6 only. Optional value, if null IPv4 and IPv6 will be attached. | [optional] 

### Return type

[**Ticket**](Ticket.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instances_post_detach_ip_ticket**
> Ticket instances_post_detach_ip_ticket(id, ip_id)

Detach public IP from instance

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
api_instance = pyodk.OCIInterfacesApi(pyodk.ApiClient(configuration))
id = 56 # int | Instance identifier
ip_id = 56 # int | IP address identifier

try:
    # Detach public IP from instance
    api_response = api_instance.instances_post_detach_ip_ticket(id, ip_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OCIInterfacesApi->instances_post_detach_ip_ticket: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Instance identifier | 
 **ip_id** | **int**| IP address identifier | 

### Return type

[**Ticket**](Ticket.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instances_update_ip**
> Object instances_update_ip(id, command)

Updates IP address

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
api_instance = pyodk.OCIInterfacesApi(pyodk.ApiClient(configuration))
id = 56 # int | 
command = pyodk.UpdateIpCommand() # UpdateIpCommand | 

try:
    # Updates IP address
    api_response = api_instance.instances_update_ip(id, command)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OCIInterfacesApi->instances_update_ip: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **command** | [**UpdateIpCommand**](UpdateIpCommand.md)|  | 

### Return type

[**Object**](Object.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

