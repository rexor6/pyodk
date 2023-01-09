# pyodk.StatisticsApi

All URIs are relative to *https://pl1-api.oktawave.com/services*

Method | HTTP request | Description
------------- | ------------- | -------------
[**statistics_get_client_statistics**](StatisticsApi.md#statistics_get_client_statistics) | **GET** /statistics/account | Gets client statistics
[**statistics_get_instance_statistics**](StatisticsApi.md#statistics_get_instance_statistics) | **GET** /statistics/instances/{id} | Gets instance statistics
[**statistics_get_statistic_intervals**](StatisticsApi.md#statistics_get_statistic_intervals) | **GET** /statistics/dictionaries/intervals | Gets statistic interval types


# **statistics_get_client_statistics**
> ApiCollectionClientStatistics statistics_get_client_statistics(date_from, date_to, statistic_types, fields=fields)

Gets client statistics

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
api_instance = pyodk.StatisticsApi(pyodk.ApiClient(configuration))
date_from = '2013-10-20T19:20:30+01:00' # datetime | Date from (utc timezone)
date_to = '2013-10-20T19:20:30+01:00' # datetime | Date to (utc timezone)
statistic_types = [56] # list[int] | Statistic types
fields = 'fields_example' # str | Response fields filter (optional)

try:
    # Gets client statistics
    api_response = api_instance.statistics_get_client_statistics(date_from, date_to, statistic_types, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatisticsApi->statistics_get_client_statistics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **date_from** | **datetime**| Date from (utc timezone) | 
 **date_to** | **datetime**| Date to (utc timezone) | 
 **statistic_types** | [**list[int]**](int.md)| Statistic types | 
 **fields** | **str**| Response fields filter | [optional] 

### Return type

[**ApiCollectionClientStatistics**](ApiCollectionClientStatistics.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **statistics_get_instance_statistics**
> ApiCollectionInstanceStatistics statistics_get_instance_statistics(id, statistic_interval, date_from, date_to, statistic_types, fields=fields)

Gets instance statistics

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
api_instance = pyodk.StatisticsApi(pyodk.ApiClient(configuration))
id = 56 # int | Id
statistic_interval = 1519 # int | Statistic interval (default to 1519)
date_from = '2013-10-20T19:20:30+01:00' # datetime | Date from (utc timezone)
date_to = '2013-10-20T19:20:30+01:00' # datetime | Date to (utc timezone)
statistic_types = [56] # list[int] | Statistic types
fields = 'fields_example' # str | Response fields filter (optional)

try:
    # Gets instance statistics
    api_response = api_instance.statistics_get_instance_statistics(id, statistic_interval, date_from, date_to, statistic_types, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatisticsApi->statistics_get_instance_statistics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id | 
 **statistic_interval** | **int**| Statistic interval | [default to 1519]
 **date_from** | **datetime**| Date from (utc timezone) | 
 **date_to** | **datetime**| Date to (utc timezone) | 
 **statistic_types** | [**list[int]**](int.md)| Statistic types | 
 **fields** | **str**| Response fields filter | [optional] 

### Return type

[**ApiCollectionInstanceStatistics**](ApiCollectionInstanceStatistics.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **statistics_get_statistic_intervals**
> ApiCollectionDictionaryItem statistics_get_statistic_intervals(fields=fields)

Gets statistic interval types

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
api_instance = pyodk.StatisticsApi(pyodk.ApiClient(configuration))
fields = 'fields_example' # str | Response fields filter (optional)

try:
    # Gets statistic interval types
    api_response = api_instance.statistics_get_statistic_intervals(fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatisticsApi->statistics_get_statistic_intervals: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Response fields filter | [optional] 

### Return type

[**ApiCollectionDictionaryItem**](ApiCollectionDictionaryItem.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

