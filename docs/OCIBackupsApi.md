# pyodk.OCIBackupsApi

All URIs are relative to *https://pl1-api.oktawave.com/services*

Method | HTTP request | Description
------------- | ------------- | -------------
[**exports_get**](OCIBackupsApi.md#exports_get) | **GET** /exports | Returns exports list
[**exports_get_0**](OCIBackupsApi.md#exports_get_0) | **GET** /exports/{id} | Gets export by identifier
[**imports_create_import**](OCIBackupsApi.md#imports_create_import) | **POST** /imports | Creates an import
[**imports_delete_import**](OCIBackupsApi.md#imports_delete_import) | **DELETE** /imports/{id} | Deletes an import
[**imports_get_import**](OCIBackupsApi.md#imports_get_import) | **GET** /imports/{id} | Returns an import
[**imports_get_import_disks**](OCIBackupsApi.md#imports_get_import_disks) | **GET** /imports/{id}/disks | Returns an import disks
[**imports_get_imports**](OCIBackupsApi.md#imports_get_imports) | **GET** /imports | Returns a list of imports
[**imports_run_import**](OCIBackupsApi.md#imports_run_import) | **POST** /imports/{id}/run_ticket | Run an import
[**instances_get_exports**](OCIBackupsApi.md#instances_get_exports) | **GET** /instances/{id}/exports | Returns instace&#39;s exports
[**instances_post_export**](OCIBackupsApi.md#instances_post_export) | **POST** /instances/{id}/exports | Create export


# **exports_get**
> ApiCollectionExport exports_get(instance_id=instance_id, status_id=status_id, page_size=page_size, page_number=page_number, order_by=order_by, fields=fields)

Returns exports list

Acceptable order values are: TotalSpaceCapacity, CreationDate, OcsLocation, Name, StartDate, Status.

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
api_instance = pyodk.OCIBackupsApi(pyodk.ApiClient(configuration))
instance_id = 56 # int | Instance id (optional)
status_id = 56 # int | Status id (optional)
page_size = 56 # int | Page size (optional)
page_number = 56 # int | Page number (optional)
order_by = 'order_by_example' # str | Order by (optional)
fields = 'fields_example' # str | Response fields filter (optional)

try:
    # Returns exports list
    api_response = api_instance.exports_get(instance_id=instance_id, status_id=status_id, page_size=page_size, page_number=page_number, order_by=order_by, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OCIBackupsApi->exports_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **int**| Instance id | [optional] 
 **status_id** | **int**| Status id | [optional] 
 **page_size** | **int**| Page size | [optional] 
 **page_number** | **int**| Page number | [optional] 
 **order_by** | **str**| Order by | [optional] 
 **fields** | **str**| Response fields filter | [optional] 

### Return type

[**ApiCollectionExport**](ApiCollectionExport.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exports_get_0**
> Export exports_get_0(id, fields=fields)

Gets export by identifier

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
api_instance = pyodk.OCIBackupsApi(pyodk.ApiClient(configuration))
id = 56 # int | Export id
fields = 'fields_example' # str | Response fields filter (optional)

try:
    # Gets export by identifier
    api_response = api_instance.exports_get_0(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OCIBackupsApi->exports_get_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Export id | 
 **fields** | **str**| Response fields filter | [optional] 

### Return type

[**Export**](Export.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **imports_create_import**
> ModelImport imports_create_import(command)

Creates an import

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
api_instance = pyodk.OCIBackupsApi(pyodk.ApiClient(configuration))
command = pyodk.CreateImportCommand() # CreateImportCommand | Create import command

try:
    # Creates an import
    api_response = api_instance.imports_create_import(command)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OCIBackupsApi->imports_create_import: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **command** | [**CreateImportCommand**](CreateImportCommand.md)| Create import command | 

### Return type

[**ModelImport**](ModelImport.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **imports_delete_import**
> imports_delete_import(id)

Deletes an import

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
api_instance = pyodk.OCIBackupsApi(pyodk.ApiClient(configuration))
id = 56 # int | Import identifier

try:
    # Deletes an import
    api_instance.imports_delete_import(id)
except ApiException as e:
    print("Exception when calling OCIBackupsApi->imports_delete_import: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Import identifier | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **imports_get_import**
> ModelImport imports_get_import(id, fields=fields)

Returns an import

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
api_instance = pyodk.OCIBackupsApi(pyodk.ApiClient(configuration))
id = 56 # int | Import identifier
fields = 'fields_example' # str | Response fields filter (optional)

try:
    # Returns an import
    api_response = api_instance.imports_get_import(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OCIBackupsApi->imports_get_import: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Import identifier | 
 **fields** | **str**| Response fields filter | [optional] 

### Return type

[**ModelImport**](ModelImport.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **imports_get_import_disks**
> ApiCollectionImportDisk imports_get_import_disks(id, fields=fields)

Returns an import disks

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
api_instance = pyodk.OCIBackupsApi(pyodk.ApiClient(configuration))
id = 56 # int | Import identifier
fields = 'fields_example' # str | Response fields filter (optional)

try:
    # Returns an import disks
    api_response = api_instance.imports_get_import_disks(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OCIBackupsApi->imports_get_import_disks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Import identifier | 
 **fields** | **str**| Response fields filter | [optional] 

### Return type

[**ApiCollectionImportDisk**](ApiCollectionImportDisk.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **imports_get_imports**
> ApiCollectionImport imports_get_imports(page_size=page_size, page_number=page_number, order_by=order_by, fields=fields)

Returns a list of imports

Acceptable order values are: Name, Status, CreationDate, DisksCount, NetworkInterfacesCount, Size

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
api_instance = pyodk.OCIBackupsApi(pyodk.ApiClient(configuration))
page_size = 56 # int | Page size (optional)
page_number = 56 # int | Page number (optional)
order_by = 'order_by_example' # str | Order by (optional)
fields = 'fields_example' # str | Response fields filter (optional)

try:
    # Returns a list of imports
    api_response = api_instance.imports_get_imports(page_size=page_size, page_number=page_number, order_by=order_by, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OCIBackupsApi->imports_get_imports: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| Page size | [optional] 
 **page_number** | **int**| Page number | [optional] 
 **order_by** | **str**| Order by | [optional] 
 **fields** | **str**| Response fields filter | [optional] 

### Return type

[**ApiCollectionImport**](ApiCollectionImport.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **imports_run_import**
> Ticket imports_run_import(id, command)

Run an import

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
api_instance = pyodk.OCIBackupsApi(pyodk.ApiClient(configuration))
id = 56 # int | Import identifier
command = pyodk.RunImportCommand() # RunImportCommand | Run import command

try:
    # Run an import
    api_response = api_instance.imports_run_import(id, command)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OCIBackupsApi->imports_run_import: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Import identifier | 
 **command** | [**RunImportCommand**](RunImportCommand.md)| Run import command | 

### Return type

[**Ticket**](Ticket.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instances_get_exports**
> ApiCollectionExport instances_get_exports(id, status_id=status_id, page_size=page_size, page_number=page_number, order_by=order_by, fields=fields)

Returns instace's exports

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
api_instance = pyodk.OCIBackupsApi(pyodk.ApiClient(configuration))
id = 56 # int | 
status_id = 56 # int | Status id (optional)
page_size = 56 # int | Page size (optional)
page_number = 56 # int | Page number (optional)
order_by = 'order_by_example' # str | Order by (optional)
fields = 'fields_example' # str | Response fields filter (optional)

try:
    # Returns instace's exports
    api_response = api_instance.instances_get_exports(id, status_id=status_id, page_size=page_size, page_number=page_number, order_by=order_by, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OCIBackupsApi->instances_get_exports: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **status_id** | **int**| Status id | [optional] 
 **page_size** | **int**| Page size | [optional] 
 **page_number** | **int**| Page number | [optional] 
 **order_by** | **str**| Order by | [optional] 
 **fields** | **str**| Response fields filter | [optional] 

### Return type

[**ApiCollectionExport**](ApiCollectionExport.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instances_post_export**
> Export instances_post_export(id, command)

Create export

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
api_instance = pyodk.OCIBackupsApi(pyodk.ApiClient(configuration))
id = 56 # int | Instance id
command = pyodk.CreateExportCommand() # CreateExportCommand | Create export command

try:
    # Create export
    api_response = api_instance.instances_post_export(id, command)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OCIBackupsApi->instances_post_export: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Instance id | 
 **command** | [**CreateExportCommand**](CreateExportCommand.md)| Create export command | 

### Return type

[**Export**](Export.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

