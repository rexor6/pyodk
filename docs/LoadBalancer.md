# LoadBalancer

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_id** | **int** | Group id | [optional] 
**group_name** | **str** | Group name | [optional] 
**ip_address** | **str** | IPv4 address | [optional] 
**ip_v6_address** | **str** | IPv6 address | [optional] 
**service_type** | [**DictionaryItem**](DictionaryItem.md) | Service type (HTTP, SMTP, Port...) | [optional] 
**port_number** | **int** | Port number for \&quot;Port\&quot; service type | [optional] 
**target_port_number** | **int** | Port number for \&quot;TargetPort\&quot; service type | [optional] 
**ssl_target_port_number** | **int** | Ssl port number for \&quot;TargetPort\&quot; service type | [optional] 
**session_persistence_type** | [**DictionaryItem**](DictionaryItem.md) | Session persistence type | [optional] 
**algorithm** | [**DictionaryItem**](DictionaryItem.md) | Algorithm | [optional] 
**ip_version** | [**DictionaryItem**](DictionaryItem.md) | IP version | [optional] 
**health_check_enabled** | **bool** | Is health check enabled | [optional] 
**ssl_enabled** | **bool** | Is ssl enabled (only for \&quot;HTTP\&quot; service type) | [optional] 
**common_persistence_for_http_and_https_enabled** | **bool** | Is common persistence for HTTP and HTTPS enabled (only for \&quot;HTTP\&quot; service type) | [optional] 
**servers** | [**list[LoadBalancerServer]**](LoadBalancerServer.md) | Services | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


