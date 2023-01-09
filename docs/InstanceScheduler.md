# InstanceScheduler

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**name** | **str** | Name | [optional] 
**instance** | [**BaseResource**](BaseResource.md) | Instance | [optional] 
**creation_date** | **datetime** | Creation date | [optional] 
**last_change_date** | **datetime** | Last change date | [optional] 
**creation_user** | [**UserResource**](UserResource.md) | User who created the scheduler | [optional] 
**type** | [**DictionaryItem**](DictionaryItem.md) | Type | [optional] 
**status** | [**DictionaryItem**](DictionaryItem.md) | Status | [optional] 
**start_date** | **datetime** | Start date | [optional] 
**time_zone_name** | **str** | Time zone name | [optional] 
**cycle_type** | [**DictionaryItem**](DictionaryItem.md) | Cycle type | [optional] 
**cycle_number** | **int** | Cycle number beetwen scheduler launch | [optional] 
**action_type** | [**DictionaryItem**](DictionaryItem.md) | Action type | [optional] 
**new_instance_type** | [**DictionaryItem**](DictionaryItem.md) | New instance type. In case of \&quot;Instance type change\&quot; action type. | [optional] 
**snapshot_name** | **str** | Snapshot name. In case of \&quot;Create snapshot\&quot; action type. | [optional] 
**snapshot_description** | **str** | Snapshot description. In case of \&quot;Create snapshot\&quot; action type. | [optional] 
**snapshot** | [**BaseResource**](BaseResource.md) | Snashot. In case of \&quot;Delete snapshot\&quot; action type. | [optional] 
**clone_name** | **str** | Clone name. In case of \&quot;Clone machine\&quot; action type. | [optional] 
**storage_path** | **str** | Storage path. In case of \&quot;Create backup\&quot; action type. | [optional] 
**storage_project_id** | **str** | Storage project id. In case of \&quot;Create backup\&quot; action type. | [optional] 
**is_backups_days_limit** | **bool** | Is backups days limit set. In case of \&quot;Create backup\&quot; action type. | [optional] 
**backups_days_limit** | **int** | Backups days limit. In case of \&quot;Create backup\&quot; action type. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


