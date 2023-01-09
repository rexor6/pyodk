# LoadBalancerServer

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip_address** | **str** | Ip address | [optional] 
**port** | **int** | Port | [optional] 
**protocol** | **str** | Protocol | [optional] 
**active_services** | **int** | Active services. Null if HealthCheckEnabled in Load balancer disabled. | [optional] 
**inactive_services** | **int** | Inactive services. Null if HealthCheckEnabled in Load balancer disabled. | [optional] 
**request_rate** | **int** | Request rate | [optional] 
**response_rate** | **int** | Response rate | [optional] 
**request_rate_bytes** | **int** | Request rate in bytes | [optional] 
**response_rate_bytes** | **int** | Response rate in bytes | [optional] 
**current_client_connections** | **int** | Current client connections | [optional] 
**status** | [**DictionaryItem**](DictionaryItem.md) | Status | [optional] 
**services** | [**list[LoadBalancerService]**](LoadBalancerService.md) | Services statistics. Filled only in load balancer details. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


