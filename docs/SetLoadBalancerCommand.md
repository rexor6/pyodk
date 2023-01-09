# SetLoadBalancerCommand

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ssl_enabled** | **bool** | Is ssl enabled (only for \&quot;HTTP\&quot; load balancer service type) | [optional] 
**service_type** | **int** | Load balancer service type | 
**port_number** | **int** | Port number for \&quot;Port\&quot; load balancer service type | [optional] 
**target_port_number** | **int** | Port number for \&quot;TargetPort\&quot; load balancer service type | [optional] 
**ssl_target_port_number** | **int** | Ssl port number for \&quot;TargetPort\&quot; load balancer service type | [optional] 
**session_persistence_type** | **int** | Session persistence type | 
**load_balancer_algorithm** | **int** | Load balancing algorithm | 
**ip_version** | **int** | Ip version for load balancing | 
**health_check_enabled** | **bool** | Is health check enabled | [optional] 
**common_persistence_for_http_and_https_enabled** | **bool** | Is common persistence for HTTP and HTTPS enabled (only for \&quot;HTTP\&quot; load balancer service type) | [optional] 
**load_balancer_ip_id** | **int** | Public ip id for load balancer | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


