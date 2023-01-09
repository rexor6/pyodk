# pyodk.WatchApi

All URIs are relative to *https://pl1-api.oktawave.com/services*

Method | HTTP request | Description
------------- | ------------- | -------------
[**watch_add_selected_monitoring_stations**](WatchApi.md#watch_add_selected_monitoring_stations) | **POST** /watch/sensors/assignments | Add monitoring sensor
[**watch_create_dns_health_check**](WatchApi.md#watch_create_dns_health_check) | **POST** /watch/healthchecks/dns | Creates dns health check
[**watch_create_full_page_health_check**](WatchApi.md#watch_create_full_page_health_check) | **POST** /watch/healthchecks/fullpage | Creates FullPage health check
[**watch_create_full_page_https_health_check**](WatchApi.md#watch_create_full_page_https_health_check) | **POST** /watch/healthchecks/fullpagehttps | Creates FullPage Https health check
[**watch_create_health_check_notification**](WatchApi.md#watch_create_health_check_notification) | **POST** /watch/healthchecks/notifications | Creates health check notification
[**watch_create_http_health_check**](WatchApi.md#watch_create_http_health_check) | **POST** /watch/healthchecks/http | Creates http health check
[**watch_create_https_health_check**](WatchApi.md#watch_create_https_health_check) | **POST** /watch/healthchecks/https | Creates https health check
[**watch_create_imap_health_check**](WatchApi.md#watch_create_imap_health_check) | **POST** /watch/healthchecks/imap | Creates imap health check
[**watch_create_imap_ssl_health_check**](WatchApi.md#watch_create_imap_ssl_health_check) | **POST** /watch/healthchecks/imapssl | Creates imap ssl health check
[**watch_create_ping_health_check**](WatchApi.md#watch_create_ping_health_check) | **POST** /watch/healthchecks/ping | Creates ping health check
[**watch_create_sip_health_check**](WatchApi.md#watch_create_sip_health_check) | **POST** /watch/healthchecks/sip | Creates sip health check
[**watch_create_smtp_health_check**](WatchApi.md#watch_create_smtp_health_check) | **POST** /watch/healthchecks/smtp | Creates smtp health check
[**watch_create_tcp_health_check**](WatchApi.md#watch_create_tcp_health_check) | **POST** /watch/healthchecks/tcp | Creates Tcp health check
[**watch_delete_health_check**](WatchApi.md#watch_delete_health_check) | **DELETE** /watch/healthchecks/{id} | Deletes health check
[**watch_delete_health_check_notification**](WatchApi.md#watch_delete_health_check_notification) | **DELETE** /watch/healthchecks/notifications/{id} | Deletes health check notification
[**watch_delete_selected_monitoring_stations**](WatchApi.md#watch_delete_selected_monitoring_stations) | **DELETE** /watch/sensors/assignments/{id} | Remove monitoring sensor
[**watch_get_available_monitoring_stations**](WatchApi.md#watch_get_available_monitoring_stations) | **GET** /watch/sensors/all | Gets all available monitoring sensors
[**watch_get_dns_health_check**](WatchApi.md#watch_get_dns_health_check) | **GET** /watch/healthchecks/dns/{id} | Returns dns health check details
[**watch_get_full_page_health_check**](WatchApi.md#watch_get_full_page_health_check) | **GET** /watch/healthchecks/fullpage/{id} | Returns FullPage health check details
[**watch_get_full_page_https_health_check**](WatchApi.md#watch_get_full_page_https_health_check) | **GET** /watch/healthchecks/fullpagehttps/{id} | Returns FullPage Https health check details
[**watch_get_health_check**](WatchApi.md#watch_get_health_check) | **GET** /watch/healthchecks/{id} | Returns health check
[**watch_get_health_check_notification**](WatchApi.md#watch_get_health_check_notification) | **GET** /watch/healthchecks/notifications/{id} | Returns health check notification details
[**watch_get_health_check_notifications**](WatchApi.md#watch_get_health_check_notifications) | **GET** /watch/healthchecks/notifications | Returns a list of configured health check notifications
[**watch_get_health_checks**](WatchApi.md#watch_get_health_checks) | **GET** /watch/healthchecks | Returns a list of configured health checks
[**watch_get_http_health_check**](WatchApi.md#watch_get_http_health_check) | **GET** /watch/healthchecks/http/{id} | Returns http health check details
[**watch_get_https_health_check**](WatchApi.md#watch_get_https_health_check) | **GET** /watch/healthchecks/https/{id} | Returns https health check details
[**watch_get_imap_health_check**](WatchApi.md#watch_get_imap_health_check) | **GET** /watch/healthchecks/imap/{id} | Returns imap health check details
[**watch_get_imap_ssl_health_check**](WatchApi.md#watch_get_imap_ssl_health_check) | **GET** /watch/healthchecks/imapssl/{id} | Returns imap ssl health check details
[**watch_get_ping_health_check**](WatchApi.md#watch_get_ping_health_check) | **GET** /watch/healthchecks/ping/{id} | Returns ping health check details
[**watch_get_selected_monitoring_station**](WatchApi.md#watch_get_selected_monitoring_station) | **GET** /watch/sensors/assignments/{id} | Gets selected monitoring sensor
[**watch_get_selected_monitoring_stations**](WatchApi.md#watch_get_selected_monitoring_stations) | **GET** /watch/sensors/assignments | Gets selected monitoring sensors
[**watch_get_sip_health_check**](WatchApi.md#watch_get_sip_health_check) | **GET** /watch/healthchecks/sip/{id} | Returns sip health check details
[**watch_get_smtp_health_check**](WatchApi.md#watch_get_smtp_health_check) | **GET** /watch/healthchecks/smtp/{id} | Returns smtp health check details
[**watch_get_tcp_health_check**](WatchApi.md#watch_get_tcp_health_check) | **GET** /watch/healthchecks/tcp/{id} | Returns tcp health check details
[**watch_update_dns_health_check**](WatchApi.md#watch_update_dns_health_check) | **PUT** /watch/healthchecks/dns/{id} | Updates dns health check
[**watch_update_full_page_health_check**](WatchApi.md#watch_update_full_page_health_check) | **PUT** /watch/healthchecks/fullpage/{id} | Updates FullPage health check
[**watch_update_full_page_https_health_check**](WatchApi.md#watch_update_full_page_https_health_check) | **PUT** /watch/healthchecks/fullpagehttps/{id} | Updates FullPage Https health check
[**watch_update_health_check_notification**](WatchApi.md#watch_update_health_check_notification) | **PUT** /watch/healthchecks/notifications/{id} | Updates health check notification
[**watch_update_http_health_check**](WatchApi.md#watch_update_http_health_check) | **PUT** /watch/healthchecks/http/{id} | Updates http health check
[**watch_update_https_health_check**](WatchApi.md#watch_update_https_health_check) | **PUT** /watch/healthchecks/https/{id} | Updates https health check
[**watch_update_imap_health_check**](WatchApi.md#watch_update_imap_health_check) | **PUT** /watch/healthchecks/imap/{id} | Updates imap health check
[**watch_update_imap_health_check_0**](WatchApi.md#watch_update_imap_health_check_0) | **PUT** /watch/healthchecks/sip/{id} | Updates sip health check
[**watch_update_imap_ssl_health_check**](WatchApi.md#watch_update_imap_ssl_health_check) | **PUT** /watch/healthchecks/imapssl/{id} | Updates imap ssl health check
[**watch_update_ping_health_check**](WatchApi.md#watch_update_ping_health_check) | **PUT** /watch/healthchecks/ping/{id} | Updates ping health check
[**watch_update_smtp_health_check**](WatchApi.md#watch_update_smtp_health_check) | **PUT** /watch/healthchecks/smtp/{id} | Updates smtp health check
[**watch_update_tcp_health_check**](WatchApi.md#watch_update_tcp_health_check) | **PUT** /watch/healthchecks/tcp/{id} | Updates Tcp health check


# **watch_add_selected_monitoring_stations**
> MonitoringSensor watch_add_selected_monitoring_stations(station)

Add monitoring sensor

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
api_instance = pyodk.WatchApi(pyodk.ApiClient(configuration))
station = pyodk.AssignNewMonitoringSensorCommand() # AssignNewMonitoringSensorCommand | Station

try:
    # Add monitoring sensor
    api_response = api_instance.watch_add_selected_monitoring_stations(station)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WatchApi->watch_add_selected_monitoring_stations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **station** | [**AssignNewMonitoringSensorCommand**](AssignNewMonitoringSensorCommand.md)| Station | 

### Return type

[**MonitoringSensor**](MonitoringSensor.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_create_dns_health_check**
> HealthCheckDns watch_create_dns_health_check(command)

Creates dns health check

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
api_instance = pyodk.WatchApi(pyodk.ApiClient(configuration))
command = pyodk.CreateUpdateHealthCheckDnsCommand() # CreateUpdateHealthCheckDnsCommand | Create dns health check command

try:
    # Creates dns health check
    api_response = api_instance.watch_create_dns_health_check(command)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WatchApi->watch_create_dns_health_check: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **command** | [**CreateUpdateHealthCheckDnsCommand**](CreateUpdateHealthCheckDnsCommand.md)| Create dns health check command | 

### Return type

[**HealthCheckDns**](HealthCheckDns.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_create_full_page_health_check**
> HealthCheckFullPage watch_create_full_page_health_check(command)

Creates FullPage health check

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
api_instance = pyodk.WatchApi(pyodk.ApiClient(configuration))
command = pyodk.CreateUpdateHealthCheckFullPageCommand() # CreateUpdateHealthCheckFullPageCommand | Create FullPage health check command

try:
    # Creates FullPage health check
    api_response = api_instance.watch_create_full_page_health_check(command)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WatchApi->watch_create_full_page_health_check: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **command** | [**CreateUpdateHealthCheckFullPageCommand**](CreateUpdateHealthCheckFullPageCommand.md)| Create FullPage health check command | 

### Return type

[**HealthCheckFullPage**](HealthCheckFullPage.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_create_full_page_https_health_check**
> HealthCheckFullPage watch_create_full_page_https_health_check(command)

Creates FullPage Https health check

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
api_instance = pyodk.WatchApi(pyodk.ApiClient(configuration))
command = pyodk.CreateUpdateHealthCheckFullPageHttpsCommand() # CreateUpdateHealthCheckFullPageHttpsCommand | Create FullPage health check command

try:
    # Creates FullPage Https health check
    api_response = api_instance.watch_create_full_page_https_health_check(command)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WatchApi->watch_create_full_page_https_health_check: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **command** | [**CreateUpdateHealthCheckFullPageHttpsCommand**](CreateUpdateHealthCheckFullPageHttpsCommand.md)| Create FullPage health check command | 

### Return type

[**HealthCheckFullPage**](HealthCheckFullPage.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_create_health_check_notification**
> HealthCheckNotification watch_create_health_check_notification(command)

Creates health check notification

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
api_instance = pyodk.WatchApi(pyodk.ApiClient(configuration))
command = pyodk.CreateUpdateHealthCheckNotificationCommand() # CreateUpdateHealthCheckNotificationCommand | Create health check notification command

try:
    # Creates health check notification
    api_response = api_instance.watch_create_health_check_notification(command)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WatchApi->watch_create_health_check_notification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **command** | [**CreateUpdateHealthCheckNotificationCommand**](CreateUpdateHealthCheckNotificationCommand.md)| Create health check notification command | 

### Return type

[**HealthCheckNotification**](HealthCheckNotification.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_create_http_health_check**
> HealthCheckHttp watch_create_http_health_check(command)

Creates http health check

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
api_instance = pyodk.WatchApi(pyodk.ApiClient(configuration))
command = pyodk.CreateUpdateHealthCheckHttpCommand() # CreateUpdateHealthCheckHttpCommand | Create http health check command

try:
    # Creates http health check
    api_response = api_instance.watch_create_http_health_check(command)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WatchApi->watch_create_http_health_check: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **command** | [**CreateUpdateHealthCheckHttpCommand**](CreateUpdateHealthCheckHttpCommand.md)| Create http health check command | 

### Return type

[**HealthCheckHttp**](HealthCheckHttp.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_create_https_health_check**
> HealthCheckHttp watch_create_https_health_check(command)

Creates https health check

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
api_instance = pyodk.WatchApi(pyodk.ApiClient(configuration))
command = pyodk.CreateUpdateHealthCheckHttpsCommand() # CreateUpdateHealthCheckHttpsCommand | Create https health check command

try:
    # Creates https health check
    api_response = api_instance.watch_create_https_health_check(command)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WatchApi->watch_create_https_health_check: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **command** | [**CreateUpdateHealthCheckHttpsCommand**](CreateUpdateHealthCheckHttpsCommand.md)| Create https health check command | 

### Return type

[**HealthCheckHttp**](HealthCheckHttp.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_create_imap_health_check**
> HealthCheckImap watch_create_imap_health_check(command)

Creates imap health check

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
api_instance = pyodk.WatchApi(pyodk.ApiClient(configuration))
command = pyodk.CreateUpdateHealthCheckImapCommand() # CreateUpdateHealthCheckImapCommand | Create imap health check command

try:
    # Creates imap health check
    api_response = api_instance.watch_create_imap_health_check(command)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WatchApi->watch_create_imap_health_check: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **command** | [**CreateUpdateHealthCheckImapCommand**](CreateUpdateHealthCheckImapCommand.md)| Create imap health check command | 

### Return type

[**HealthCheckImap**](HealthCheckImap.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_create_imap_ssl_health_check**
> HealthCheckImap watch_create_imap_ssl_health_check(command)

Creates imap ssl health check

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
api_instance = pyodk.WatchApi(pyodk.ApiClient(configuration))
command = pyodk.CreateUpdateHealthCheckImapSslCommand() # CreateUpdateHealthCheckImapSslCommand | Create imap ssl health check command

try:
    # Creates imap ssl health check
    api_response = api_instance.watch_create_imap_ssl_health_check(command)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WatchApi->watch_create_imap_ssl_health_check: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **command** | [**CreateUpdateHealthCheckImapSslCommand**](CreateUpdateHealthCheckImapSslCommand.md)| Create imap ssl health check command | 

### Return type

[**HealthCheckImap**](HealthCheckImap.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_create_ping_health_check**
> HealthCheckPing watch_create_ping_health_check(command)

Creates ping health check

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
api_instance = pyodk.WatchApi(pyodk.ApiClient(configuration))
command = pyodk.CreateUpdateHealthCheckPingCommand() # CreateUpdateHealthCheckPingCommand | Create ping health check command

try:
    # Creates ping health check
    api_response = api_instance.watch_create_ping_health_check(command)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WatchApi->watch_create_ping_health_check: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **command** | [**CreateUpdateHealthCheckPingCommand**](CreateUpdateHealthCheckPingCommand.md)| Create ping health check command | 

### Return type

[**HealthCheckPing**](HealthCheckPing.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_create_sip_health_check**
> HealthCheckSip watch_create_sip_health_check(command)

Creates sip health check

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
api_instance = pyodk.WatchApi(pyodk.ApiClient(configuration))
command = pyodk.CreateUpdateHealthCheckSipCommand() # CreateUpdateHealthCheckSipCommand | Create sip health check command

try:
    # Creates sip health check
    api_response = api_instance.watch_create_sip_health_check(command)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WatchApi->watch_create_sip_health_check: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **command** | [**CreateUpdateHealthCheckSipCommand**](CreateUpdateHealthCheckSipCommand.md)| Create sip health check command | 

### Return type

[**HealthCheckSip**](HealthCheckSip.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_create_smtp_health_check**
> HealthCheckSmtp watch_create_smtp_health_check(command)

Creates smtp health check

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
api_instance = pyodk.WatchApi(pyodk.ApiClient(configuration))
command = pyodk.CreateUpdateHealthCheckSmtpCommand() # CreateUpdateHealthCheckSmtpCommand | Create smtp health check command

try:
    # Creates smtp health check
    api_response = api_instance.watch_create_smtp_health_check(command)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WatchApi->watch_create_smtp_health_check: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **command** | [**CreateUpdateHealthCheckSmtpCommand**](CreateUpdateHealthCheckSmtpCommand.md)| Create smtp health check command | 

### Return type

[**HealthCheckSmtp**](HealthCheckSmtp.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_create_tcp_health_check**
> HealthCheckTcp watch_create_tcp_health_check(command)

Creates Tcp health check

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
api_instance = pyodk.WatchApi(pyodk.ApiClient(configuration))
command = pyodk.CreateUpdateHealthCheckTcpCommand() # CreateUpdateHealthCheckTcpCommand | Create Tcp health check command

try:
    # Creates Tcp health check
    api_response = api_instance.watch_create_tcp_health_check(command)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WatchApi->watch_create_tcp_health_check: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **command** | [**CreateUpdateHealthCheckTcpCommand**](CreateUpdateHealthCheckTcpCommand.md)| Create Tcp health check command | 

### Return type

[**HealthCheckTcp**](HealthCheckTcp.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_delete_health_check**
> watch_delete_health_check(id)

Deletes health check

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
api_instance = pyodk.WatchApi(pyodk.ApiClient(configuration))
id = 56 # int | Id of a health check

try:
    # Deletes health check
    api_instance.watch_delete_health_check(id)
except ApiException as e:
    print("Exception when calling WatchApi->watch_delete_health_check: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of a health check | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_delete_health_check_notification**
> watch_delete_health_check_notification(id)

Deletes health check notification

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
api_instance = pyodk.WatchApi(pyodk.ApiClient(configuration))
id = 56 # int | Id of a health check notification

try:
    # Deletes health check notification
    api_instance.watch_delete_health_check_notification(id)
except ApiException as e:
    print("Exception when calling WatchApi->watch_delete_health_check_notification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of a health check notification | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_delete_selected_monitoring_stations**
> MonitoringSensor watch_delete_selected_monitoring_stations(id)

Remove monitoring sensor

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
api_instance = pyodk.WatchApi(pyodk.ApiClient(configuration))
id = 56 # int | Sensor id

try:
    # Remove monitoring sensor
    api_response = api_instance.watch_delete_selected_monitoring_stations(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WatchApi->watch_delete_selected_monitoring_stations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Sensor id | 

### Return type

[**MonitoringSensor**](MonitoringSensor.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_get_available_monitoring_stations**
> MonitoringSensor watch_get_available_monitoring_stations(fields=fields)

Gets all available monitoring sensors

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
api_instance = pyodk.WatchApi(pyodk.ApiClient(configuration))
fields = 'fields_example' # str | Response fields filter (optional)

try:
    # Gets all available monitoring sensors
    api_response = api_instance.watch_get_available_monitoring_stations(fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WatchApi->watch_get_available_monitoring_stations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Response fields filter | [optional] 

### Return type

[**MonitoringSensor**](MonitoringSensor.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_get_dns_health_check**
> HealthCheckDns watch_get_dns_health_check(id, fields=fields)

Returns dns health check details

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
api_instance = pyodk.WatchApi(pyodk.ApiClient(configuration))
id = 56 # int | Id of a health check
fields = 'fields_example' # str | Response fields filter (optional)

try:
    # Returns dns health check details
    api_response = api_instance.watch_get_dns_health_check(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WatchApi->watch_get_dns_health_check: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of a health check | 
 **fields** | **str**| Response fields filter | [optional] 

### Return type

[**HealthCheckDns**](HealthCheckDns.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_get_full_page_health_check**
> HealthCheckFullPage watch_get_full_page_health_check(id, fields=fields)

Returns FullPage health check details

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
api_instance = pyodk.WatchApi(pyodk.ApiClient(configuration))
id = 56 # int | Id of a health check
fields = 'fields_example' # str | Response fields filter (optional)

try:
    # Returns FullPage health check details
    api_response = api_instance.watch_get_full_page_health_check(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WatchApi->watch_get_full_page_health_check: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of a health check | 
 **fields** | **str**| Response fields filter | [optional] 

### Return type

[**HealthCheckFullPage**](HealthCheckFullPage.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_get_full_page_https_health_check**
> HealthCheckFullPage watch_get_full_page_https_health_check(id, fields=fields)

Returns FullPage Https health check details

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
api_instance = pyodk.WatchApi(pyodk.ApiClient(configuration))
id = 56 # int | Id of a health check
fields = 'fields_example' # str | Response fields filter (optional)

try:
    # Returns FullPage Https health check details
    api_response = api_instance.watch_get_full_page_https_health_check(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WatchApi->watch_get_full_page_https_health_check: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of a health check | 
 **fields** | **str**| Response fields filter | [optional] 

### Return type

[**HealthCheckFullPage**](HealthCheckFullPage.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_get_health_check**
> HealthCheck watch_get_health_check(id, fields=fields)

Returns health check

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
api_instance = pyodk.WatchApi(pyodk.ApiClient(configuration))
id = 56 # int | Id of a health check
fields = 'fields_example' # str | Response fields filter (optional)

try:
    # Returns health check
    api_response = api_instance.watch_get_health_check(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WatchApi->watch_get_health_check: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of a health check | 
 **fields** | **str**| Response fields filter | [optional] 

### Return type

[**HealthCheck**](HealthCheck.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_get_health_check_notification**
> HealthCheckNotification watch_get_health_check_notification(id, fields=fields)

Returns health check notification details

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
api_instance = pyodk.WatchApi(pyodk.ApiClient(configuration))
id = 56 # int | Id of a health check notification
fields = 'fields_example' # str | Response fields filter (optional)

try:
    # Returns health check notification details
    api_response = api_instance.watch_get_health_check_notification(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WatchApi->watch_get_health_check_notification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of a health check notification | 
 **fields** | **str**| Response fields filter | [optional] 

### Return type

[**HealthCheckNotification**](HealthCheckNotification.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_get_health_check_notifications**
> ApiCollectionHealthCheckNotification watch_get_health_check_notifications(page_size=page_size, page_number=page_number, order_by=order_by, fields=fields)

Returns a list of configured health check notifications

Acceptable order values are: Address, Id

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
api_instance = pyodk.WatchApi(pyodk.ApiClient(configuration))
page_size = 56 # int | Page size (optional)
page_number = 56 # int | Page number (optional)
order_by = 'order_by_example' # str | Order by (optional)
fields = 'fields_example' # str | Response fields filter (optional)

try:
    # Returns a list of configured health check notifications
    api_response = api_instance.watch_get_health_check_notifications(page_size=page_size, page_number=page_number, order_by=order_by, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WatchApi->watch_get_health_check_notifications: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| Page size | [optional] 
 **page_number** | **int**| Page number | [optional] 
 **order_by** | **str**| Order by | [optional] 
 **fields** | **str**| Response fields filter | [optional] 

### Return type

[**ApiCollectionHealthCheckNotification**](ApiCollectionHealthCheckNotification.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_get_health_checks**
> ApiCollectionHealthCheck watch_get_health_checks(page_size=page_size, page_number=page_number, order_by=order_by, fields=fields)

Returns a list of configured health checks

Acceptable order values are: Name, Type

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
api_instance = pyodk.WatchApi(pyodk.ApiClient(configuration))
page_size = 56 # int | Page size (optional)
page_number = 56 # int | Page number (optional)
order_by = 'order_by_example' # str | Order by (optional)
fields = 'fields_example' # str | Response fields filter (optional)

try:
    # Returns a list of configured health checks
    api_response = api_instance.watch_get_health_checks(page_size=page_size, page_number=page_number, order_by=order_by, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WatchApi->watch_get_health_checks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| Page size | [optional] 
 **page_number** | **int**| Page number | [optional] 
 **order_by** | **str**| Order by | [optional] 
 **fields** | **str**| Response fields filter | [optional] 

### Return type

[**ApiCollectionHealthCheck**](ApiCollectionHealthCheck.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_get_http_health_check**
> HealthCheckHttp watch_get_http_health_check(id, fields=fields)

Returns http health check details

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
api_instance = pyodk.WatchApi(pyodk.ApiClient(configuration))
id = 56 # int | Id of a health check
fields = 'fields_example' # str | Response fields filter (optional)

try:
    # Returns http health check details
    api_response = api_instance.watch_get_http_health_check(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WatchApi->watch_get_http_health_check: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of a health check | 
 **fields** | **str**| Response fields filter | [optional] 

### Return type

[**HealthCheckHttp**](HealthCheckHttp.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_get_https_health_check**
> HealthCheckHttp watch_get_https_health_check(id, fields=fields)

Returns https health check details

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
api_instance = pyodk.WatchApi(pyodk.ApiClient(configuration))
id = 56 # int | Id of a health check
fields = 'fields_example' # str | Response fields filter (optional)

try:
    # Returns https health check details
    api_response = api_instance.watch_get_https_health_check(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WatchApi->watch_get_https_health_check: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of a health check | 
 **fields** | **str**| Response fields filter | [optional] 

### Return type

[**HealthCheckHttp**](HealthCheckHttp.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_get_imap_health_check**
> HealthCheckImap watch_get_imap_health_check(id, fields=fields)

Returns imap health check details

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
api_instance = pyodk.WatchApi(pyodk.ApiClient(configuration))
id = 56 # int | Id of a health check
fields = 'fields_example' # str | Response fields filter (optional)

try:
    # Returns imap health check details
    api_response = api_instance.watch_get_imap_health_check(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WatchApi->watch_get_imap_health_check: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of a health check | 
 **fields** | **str**| Response fields filter | [optional] 

### Return type

[**HealthCheckImap**](HealthCheckImap.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_get_imap_ssl_health_check**
> HealthCheckImap watch_get_imap_ssl_health_check(id, fields=fields)

Returns imap ssl health check details

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
api_instance = pyodk.WatchApi(pyodk.ApiClient(configuration))
id = 56 # int | Id of a health check
fields = 'fields_example' # str | Response fields filter (optional)

try:
    # Returns imap ssl health check details
    api_response = api_instance.watch_get_imap_ssl_health_check(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WatchApi->watch_get_imap_ssl_health_check: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of a health check | 
 **fields** | **str**| Response fields filter | [optional] 

### Return type

[**HealthCheckImap**](HealthCheckImap.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_get_ping_health_check**
> HealthCheckPing watch_get_ping_health_check(id, fields=fields)

Returns ping health check details

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
api_instance = pyodk.WatchApi(pyodk.ApiClient(configuration))
id = 56 # int | Id of a health check
fields = 'fields_example' # str | Response fields filter (optional)

try:
    # Returns ping health check details
    api_response = api_instance.watch_get_ping_health_check(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WatchApi->watch_get_ping_health_check: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of a health check | 
 **fields** | **str**| Response fields filter | [optional] 

### Return type

[**HealthCheckPing**](HealthCheckPing.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_get_selected_monitoring_station**
> MonitoringSensor watch_get_selected_monitoring_station(id, fields=fields)

Gets selected monitoring sensor

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
api_instance = pyodk.WatchApi(pyodk.ApiClient(configuration))
id = 56 # int | 
fields = 'fields_example' # str | Response fields filter (optional)

try:
    # Gets selected monitoring sensor
    api_response = api_instance.watch_get_selected_monitoring_station(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WatchApi->watch_get_selected_monitoring_station: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **fields** | **str**| Response fields filter | [optional] 

### Return type

[**MonitoringSensor**](MonitoringSensor.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_get_selected_monitoring_stations**
> MonitoringSensor watch_get_selected_monitoring_stations(fields=fields)

Gets selected monitoring sensors

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
api_instance = pyodk.WatchApi(pyodk.ApiClient(configuration))
fields = 'fields_example' # str | Response fields filter (optional)

try:
    # Gets selected monitoring sensors
    api_response = api_instance.watch_get_selected_monitoring_stations(fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WatchApi->watch_get_selected_monitoring_stations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Response fields filter | [optional] 

### Return type

[**MonitoringSensor**](MonitoringSensor.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_get_sip_health_check**
> HealthCheckSip watch_get_sip_health_check(id, fields=fields)

Returns sip health check details

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
api_instance = pyodk.WatchApi(pyodk.ApiClient(configuration))
id = 56 # int | Id of a health check
fields = 'fields_example' # str | Response fields filter (optional)

try:
    # Returns sip health check details
    api_response = api_instance.watch_get_sip_health_check(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WatchApi->watch_get_sip_health_check: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of a health check | 
 **fields** | **str**| Response fields filter | [optional] 

### Return type

[**HealthCheckSip**](HealthCheckSip.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_get_smtp_health_check**
> HealthCheckSmtp watch_get_smtp_health_check(id, fields=fields)

Returns smtp health check details

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
api_instance = pyodk.WatchApi(pyodk.ApiClient(configuration))
id = 56 # int | Id of a health check
fields = 'fields_example' # str | Response fields filter (optional)

try:
    # Returns smtp health check details
    api_response = api_instance.watch_get_smtp_health_check(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WatchApi->watch_get_smtp_health_check: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of a health check | 
 **fields** | **str**| Response fields filter | [optional] 

### Return type

[**HealthCheckSmtp**](HealthCheckSmtp.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_get_tcp_health_check**
> HealthCheckTcp watch_get_tcp_health_check(id, fields=fields)

Returns tcp health check details

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
api_instance = pyodk.WatchApi(pyodk.ApiClient(configuration))
id = 56 # int | Id of a health check
fields = 'fields_example' # str | Response fields filter (optional)

try:
    # Returns tcp health check details
    api_response = api_instance.watch_get_tcp_health_check(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WatchApi->watch_get_tcp_health_check: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of a health check | 
 **fields** | **str**| Response fields filter | [optional] 

### Return type

[**HealthCheckTcp**](HealthCheckTcp.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_update_dns_health_check**
> HealthCheckDns watch_update_dns_health_check(id, command)

Updates dns health check

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
api_instance = pyodk.WatchApi(pyodk.ApiClient(configuration))
id = 56 # int | Health check id
command = pyodk.CreateUpdateHealthCheckDnsCommand() # CreateUpdateHealthCheckDnsCommand | Create dns health check command

try:
    # Updates dns health check
    api_response = api_instance.watch_update_dns_health_check(id, command)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WatchApi->watch_update_dns_health_check: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Health check id | 
 **command** | [**CreateUpdateHealthCheckDnsCommand**](CreateUpdateHealthCheckDnsCommand.md)| Create dns health check command | 

### Return type

[**HealthCheckDns**](HealthCheckDns.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_update_full_page_health_check**
> HealthCheckFullPage watch_update_full_page_health_check(id, command)

Updates FullPage health check

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
api_instance = pyodk.WatchApi(pyodk.ApiClient(configuration))
id = 56 # int | Health check id
command = pyodk.CreateUpdateHealthCheckFullPageCommand() # CreateUpdateHealthCheckFullPageCommand | Create FullPage health check command

try:
    # Updates FullPage health check
    api_response = api_instance.watch_update_full_page_health_check(id, command)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WatchApi->watch_update_full_page_health_check: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Health check id | 
 **command** | [**CreateUpdateHealthCheckFullPageCommand**](CreateUpdateHealthCheckFullPageCommand.md)| Create FullPage health check command | 

### Return type

[**HealthCheckFullPage**](HealthCheckFullPage.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_update_full_page_https_health_check**
> HealthCheckFullPage watch_update_full_page_https_health_check(id, command)

Updates FullPage Https health check

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
api_instance = pyodk.WatchApi(pyodk.ApiClient(configuration))
id = 56 # int | Health check id
command = pyodk.CreateUpdateHealthCheckFullPageHttpsCommand() # CreateUpdateHealthCheckFullPageHttpsCommand | Create FullPage health check command

try:
    # Updates FullPage Https health check
    api_response = api_instance.watch_update_full_page_https_health_check(id, command)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WatchApi->watch_update_full_page_https_health_check: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Health check id | 
 **command** | [**CreateUpdateHealthCheckFullPageHttpsCommand**](CreateUpdateHealthCheckFullPageHttpsCommand.md)| Create FullPage health check command | 

### Return type

[**HealthCheckFullPage**](HealthCheckFullPage.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_update_health_check_notification**
> HealthCheckNotification watch_update_health_check_notification(id, command)

Updates health check notification

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
api_instance = pyodk.WatchApi(pyodk.ApiClient(configuration))
id = 56 # int | Health check notification id
command = pyodk.CreateUpdateHealthCheckNotificationCommand() # CreateUpdateHealthCheckNotificationCommand | Create health check notification command

try:
    # Updates health check notification
    api_response = api_instance.watch_update_health_check_notification(id, command)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WatchApi->watch_update_health_check_notification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Health check notification id | 
 **command** | [**CreateUpdateHealthCheckNotificationCommand**](CreateUpdateHealthCheckNotificationCommand.md)| Create health check notification command | 

### Return type

[**HealthCheckNotification**](HealthCheckNotification.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_update_http_health_check**
> HealthCheckHttp watch_update_http_health_check(id, command)

Updates http health check

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
api_instance = pyodk.WatchApi(pyodk.ApiClient(configuration))
id = 56 # int | Health check id
command = pyodk.CreateUpdateHealthCheckHttpCommand() # CreateUpdateHealthCheckHttpCommand | Create http health check command

try:
    # Updates http health check
    api_response = api_instance.watch_update_http_health_check(id, command)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WatchApi->watch_update_http_health_check: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Health check id | 
 **command** | [**CreateUpdateHealthCheckHttpCommand**](CreateUpdateHealthCheckHttpCommand.md)| Create http health check command | 

### Return type

[**HealthCheckHttp**](HealthCheckHttp.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_update_https_health_check**
> HealthCheckHttp watch_update_https_health_check(id, command)

Updates https health check

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
api_instance = pyodk.WatchApi(pyodk.ApiClient(configuration))
id = 56 # int | Health check id
command = pyodk.CreateUpdateHealthCheckHttpsCommand() # CreateUpdateHealthCheckHttpsCommand | Create https health check command

try:
    # Updates https health check
    api_response = api_instance.watch_update_https_health_check(id, command)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WatchApi->watch_update_https_health_check: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Health check id | 
 **command** | [**CreateUpdateHealthCheckHttpsCommand**](CreateUpdateHealthCheckHttpsCommand.md)| Create https health check command | 

### Return type

[**HealthCheckHttp**](HealthCheckHttp.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_update_imap_health_check**
> HealthCheckImap watch_update_imap_health_check(id, command)

Updates imap health check

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
api_instance = pyodk.WatchApi(pyodk.ApiClient(configuration))
id = 56 # int | Health check id
command = pyodk.CreateUpdateHealthCheckImapCommand() # CreateUpdateHealthCheckImapCommand | Create imap health check command

try:
    # Updates imap health check
    api_response = api_instance.watch_update_imap_health_check(id, command)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WatchApi->watch_update_imap_health_check: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Health check id | 
 **command** | [**CreateUpdateHealthCheckImapCommand**](CreateUpdateHealthCheckImapCommand.md)| Create imap health check command | 

### Return type

[**HealthCheckImap**](HealthCheckImap.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_update_imap_health_check_0**
> HealthCheckSip watch_update_imap_health_check_0(id, command)

Updates sip health check

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
api_instance = pyodk.WatchApi(pyodk.ApiClient(configuration))
id = 56 # int | Health check id
command = pyodk.CreateUpdateHealthCheckSipCommand() # CreateUpdateHealthCheckSipCommand | Create sip health check command

try:
    # Updates sip health check
    api_response = api_instance.watch_update_imap_health_check_0(id, command)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WatchApi->watch_update_imap_health_check_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Health check id | 
 **command** | [**CreateUpdateHealthCheckSipCommand**](CreateUpdateHealthCheckSipCommand.md)| Create sip health check command | 

### Return type

[**HealthCheckSip**](HealthCheckSip.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_update_imap_ssl_health_check**
> HealthCheckImap watch_update_imap_ssl_health_check(id, command)

Updates imap ssl health check

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
api_instance = pyodk.WatchApi(pyodk.ApiClient(configuration))
id = 56 # int | Health check id
command = pyodk.CreateUpdateHealthCheckImapSslCommand() # CreateUpdateHealthCheckImapSslCommand | Create imap ssl health check command

try:
    # Updates imap ssl health check
    api_response = api_instance.watch_update_imap_ssl_health_check(id, command)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WatchApi->watch_update_imap_ssl_health_check: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Health check id | 
 **command** | [**CreateUpdateHealthCheckImapSslCommand**](CreateUpdateHealthCheckImapSslCommand.md)| Create imap ssl health check command | 

### Return type

[**HealthCheckImap**](HealthCheckImap.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_update_ping_health_check**
> HealthCheckPing watch_update_ping_health_check(id, command)

Updates ping health check

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
api_instance = pyodk.WatchApi(pyodk.ApiClient(configuration))
id = 56 # int | Health check id
command = pyodk.CreateUpdateHealthCheckPingCommand() # CreateUpdateHealthCheckPingCommand | Create ping health check command

try:
    # Updates ping health check
    api_response = api_instance.watch_update_ping_health_check(id, command)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WatchApi->watch_update_ping_health_check: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Health check id | 
 **command** | [**CreateUpdateHealthCheckPingCommand**](CreateUpdateHealthCheckPingCommand.md)| Create ping health check command | 

### Return type

[**HealthCheckPing**](HealthCheckPing.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_update_smtp_health_check**
> HealthCheckSmtp watch_update_smtp_health_check(id, command)

Updates smtp health check

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
api_instance = pyodk.WatchApi(pyodk.ApiClient(configuration))
id = 56 # int | Health check id
command = pyodk.CreateUpdateHealthCheckSmtpCommand() # CreateUpdateHealthCheckSmtpCommand | Create smtp health check command

try:
    # Updates smtp health check
    api_response = api_instance.watch_update_smtp_health_check(id, command)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WatchApi->watch_update_smtp_health_check: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Health check id | 
 **command** | [**CreateUpdateHealthCheckSmtpCommand**](CreateUpdateHealthCheckSmtpCommand.md)| Create smtp health check command | 

### Return type

[**HealthCheckSmtp**](HealthCheckSmtp.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_update_tcp_health_check**
> HealthCheckTcp watch_update_tcp_health_check(id, command)

Updates Tcp health check

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
api_instance = pyodk.WatchApi(pyodk.ApiClient(configuration))
id = 56 # int | Health check id
command = pyodk.CreateUpdateHealthCheckTcpCommand() # CreateUpdateHealthCheckTcpCommand | Create Tcp health check command

try:
    # Updates Tcp health check
    api_response = api_instance.watch_update_tcp_health_check(id, command)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WatchApi->watch_update_tcp_health_check: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Health check id | 
 **command** | [**CreateUpdateHealthCheckTcpCommand**](CreateUpdateHealthCheckTcpCommand.md)| Create Tcp health check command | 

### Return type

[**HealthCheckTcp**](HealthCheckTcp.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

