# InstanceAutoscalingParameter

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**autoscaling_parameter_type** | [**DictionaryItem**](DictionaryItem.md) | Autoscaling parameter type | [optional] 
**min_ram** | **int** | Minimum RAM capacity in megabytes | [optional] 
**max_ram** | **int** | Maximum RAM capacity in megabytes | [optional] 
**min_cpu** | **int** | Minimum CPU count | [optional] 
**max_cpu** | **int** | Maximum CPU count | [optional] 
**has_agreed_to_increase_class** | **bool** | Instance class increase agreement | [optional] 
**has_agreed_to_decrease_class** | **bool** | Instance class decrease agreement | [optional] 
**has_agreed_to_restart** | **bool** | Restart agreement | [optional] 
**restart_time_from** | [**NullableTime**](NullableTime.md) | Restart time lower limit | [optional] 
**restart_time_to** | [**NullableTime**](NullableTime.md) | Restart time upper limit | [optional] 
**time_zone_name** | **str** | Time zone name (https://www.iana.org/time-zones) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


