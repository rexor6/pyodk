# CreateUpdateInstanceSchedulerCommand

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name | 
**type_id** | **int** | Type id | 
**start_date** | **datetime** | Start date | 
**time_zone_name** | **str** | IANA Time zone. To get a list of available timezones, visit (https://momentjs.com/timezone) | 
**cycle_type_id** | **int** | Cycle type id | [optional] 
**cycle_number** | **int** | Cycle number beetwen scheduler launch | [optional] 
**action_type_id** | **int** | Action type | 
**new_instance_type_id** | **int** | New instance type. In case of \&quot;Instance type change\&quot; action type. | [optional] 
**snapshot_name** | **str** | Snapshot name. In case of \&quot;Create snapshot\&quot; action type. | [optional] 
**snapshot_description** | **str** | Snapshot description. In case of \&quot;Create snapshot\&quot; action type. | [optional] 
**snapshot_id** | **int** | Snashot. In case of \&quot;Delete snapshot\&quot; action type. | [optional] 
**clone_name** | **str** | Clone name. In case of \&quot;Clone machine\&quot; action type. | [optional] 
**storage_path** | **str** | Storage path. In case of \&quot;Create backup\&quot; action type. | [optional] 
**storage_project_id** | **str** | Storage project id. In case of \&quot;Create backup\&quot; action type. | [optional] 
**is_backups_days_limit** | **bool** | Is backups days limit set. In case of \&quot;Create backup\&quot; action type. | [optional] 
**backups_days_limit** | **int** | Backups days limit. In case of \&quot;Create backup\&quot; action type. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


