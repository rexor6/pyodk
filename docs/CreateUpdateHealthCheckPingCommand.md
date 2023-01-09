# CreateUpdateHealthCheckPingCommand

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**package_size** | **int** | Data package size [bytes] | [default to 64]
**reply_timeout** | **int** | Maximum waiting time for a response [ms] | [default to 3000]
**error_tolerance** | **int** | How many (%) locations have to report an error to consider it a breakdown | [default to 51]
**name** | **str** | Health check name | [default to '']
**address** | **str** | URL or IP address of the monitored service | [default to '']
**interval** | **int** | Time interval between health checks, in seconds | [default to 60]
**paused** | **bool** | Is paused | [default to False]
**locations_failover_enabled** | **bool** | Use random substitute locations in case of location breakdown | [default to True]
**notification_type_ids** | **list[int]** | Notification types enabled for a health check | [optional] 
**notification_event_type_ids** | **list[int]** | Event types with enabled notification | [optional] 
**notification_time_id** | **int** | Time when notification is sent | [default to 1594]
**description** | **str** | Description | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


