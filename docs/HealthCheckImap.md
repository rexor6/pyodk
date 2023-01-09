# HealthCheckImap

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**port** | **int** | Port | [optional] 
**timeout** | **int** | Timeout | [optional] 
**notification_types** | [**list[DictionaryItem]**](DictionaryItem.md) | Notification types enabled for a health check | [optional] 
**notification_event_types** | [**list[DictionaryItem]**](DictionaryItem.md) | Event types with enabled notification | [optional] 
**notification_time** | [**DictionaryItem**](DictionaryItem.md) | Time when notification is sent | [optional] 
**locations_failover_enabled** | **bool** | Use random substitute locations in case of location breakdown | [optional] 
**error_tolerance** | **int** | How many (%) locations have to report an error to consider it a breakdown | [optional] 
**id** | **int** | Id | [optional] 
**interval** | **int** | Interval | [optional] 
**name** | **str** | Name | [optional] 
**address** | **str** | Address | [optional] 
**service_type** | [**DictionaryItem**](DictionaryItem.md) | Type | [optional] 
**state** | [**DictionaryItem**](DictionaryItem.md) | State | [optional] 
**details_location** | **str** | Details url | [optional] 
**paused** | **bool** | Is paused | [optional] 
**suspended** | **bool** | Is suspended | [optional] 
**last_invalid_check** | **datetime** | Last invalid check | [optional] 
**last_valid_check** | **datetime** | Last valid check | [optional] 
**description** | **str** | Description | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


