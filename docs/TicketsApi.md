# pyodk.TicketsApi

All URIs are relative to *https://pl1-api.oktawave.com/services*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tickets_get**](TicketsApi.md#tickets_get) | **GET** /tickets | Returns ticket collection
[**tickets_get_0**](TicketsApi.md#tickets_get_0) | **GET** /tickets/{id} | Returns ticket by identifier


# **tickets_get**
> ApiCollectionTicket tickets_get(status_id=status_id, creation_date_from=creation_date_from, creation_date_to=creation_date_to, page_size=page_size, page_number=page_number, order_by=order_by, fields=fields)

Returns ticket collection

Acceptable order values are: CreationDate, Status, OperationType

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
api_instance = pyodk.TicketsApi(pyodk.ApiClient(configuration))
status_id = 56 # int | Tickets status id (optional)
creation_date_from = '2013-10-20T19:20:30+01:00' # datetime | Tickets creation date from (optional)
creation_date_to = '2013-10-20T19:20:30+01:00' # datetime | Tickets creation date to (optional)
page_size = 56 # int | Page size (optional)
page_number = 56 # int | Page number (optional)
order_by = 'order_by_example' # str | Order by (optional)
fields = 'fields_example' # str | Response fields filter (optional)

try:
    # Returns ticket collection
    api_response = api_instance.tickets_get(status_id=status_id, creation_date_from=creation_date_from, creation_date_to=creation_date_to, page_size=page_size, page_number=page_number, order_by=order_by, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TicketsApi->tickets_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status_id** | **int**| Tickets status id | [optional] 
 **creation_date_from** | **datetime**| Tickets creation date from | [optional] 
 **creation_date_to** | **datetime**| Tickets creation date to | [optional] 
 **page_size** | **int**| Page size | [optional] 
 **page_number** | **int**| Page number | [optional] 
 **order_by** | **str**| Order by | [optional] 
 **fields** | **str**| Response fields filter | [optional] 

### Return type

[**ApiCollectionTicket**](ApiCollectionTicket.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tickets_get_0**
> Ticket tickets_get_0(id, fields=fields)

Returns ticket by identifier

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
api_instance = pyodk.TicketsApi(pyodk.ApiClient(configuration))
id = 789 # int | Ticket identifier
fields = 'fields_example' # str | Response fields filter (optional)

try:
    # Returns ticket by identifier
    api_response = api_instance.tickets_get_0(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TicketsApi->tickets_get_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Ticket identifier | 
 **fields** | **str**| Response fields filter | [optional] 

### Return type

[**Ticket**](Ticket.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

