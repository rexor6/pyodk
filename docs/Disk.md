# Disk

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Id | [optional] 
**name** | **str** | Name | [optional] 
**space_capacity** | **int** | Space capacity in GB | [optional] 
**tier** | [**DictionaryItem**](DictionaryItem.md) | Tier | [optional] 
**creation_date** | **datetime** | Creation date | [optional] 
**creation_user** | [**UserResource**](UserResource.md) | User who created the disk | [optional] 
**is_shared** | **bool** | If disk is shared | [optional] 
**shared_disk_type** | [**DictionaryItem**](DictionaryItem.md) | Shared disk type, null if disk is not shared | [optional] 
**subregion** | [**BaseResource**](BaseResource.md) | Subregion | [optional] 
**is_locked** | **bool** | If the disk is locked by a running operation | [optional] 
**locking_date** | **datetime** | Locking date | [optional] 
**connections** | [**list[DiskConnection]**](DiskConnection.md) | Connections to instances | [optional] 
**is_freemium** | **bool** | Is freemium | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


