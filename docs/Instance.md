# Instance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**name** | **str** | Name | [optional] 
**creation_date** | **datetime** | Creation date | [optional] 
**creation_user** | [**UserResource**](UserResource.md) | User who created the instance | [optional] 
**is_locked** | **bool** | If the instance is locked by a running operation | [optional] 
**locking_date** | **datetime** | Locking date | [optional] 
**template** | [**BaseResource**](BaseResource.md) | Template from which the instance was created | [optional] 
**subregion** | [**BaseResource**](BaseResource.md) | Subregion that is running the instance | [optional] 
**type** | [**DictionaryItem**](DictionaryItem.md) | Instance type. Defines the configuration of CPU and RAM | [optional] 
**status** | [**DictionaryItem**](DictionaryItem.md) | Status | [optional] 
**system_category** | [**DictionaryItem**](DictionaryItem.md) | Operating system category installed on the instance | [optional] 
**autoscaling_type** | [**DictionaryItem**](DictionaryItem.md) | Autoscaling type | [optional] 
**vm_ware_tools_status** | [**DictionaryItem**](DictionaryItem.md) | VMware Tools status | [optional] 
**monit_status** | [**DictionaryItem**](DictionaryItem.md) | Monitoring status | [optional] 
**template_type** | [**DictionaryItem**](DictionaryItem.md) | Template type eg marketplace, oci instance | [optional] 
**ip_address** | **str** | IP address | [optional] 
**private_ip_address** | **str** | Private IP address | [optional] 
**dns_address** | **str** | DNS address | [optional] 
**total_disks_capacity** | **int** | Total disks capacity in GB | [optional] 
**payment_type** | [**DictionaryItem**](DictionaryItem.md) | Payment type | [optional] 
**health_check** | [**BaseResource**](BaseResource.md) | Health check | [optional] 
**scsi_controller_type** | [**DictionaryItem**](DictionaryItem.md) | SCSI controller type | [optional] 
**is_freemium** | **bool** | Is freemium | [optional] 
**cpu_number** | **int** | Number of CPUs | [optional] 
**ram_mb** | **int** | Memory in MB | [optional] 
**support_type** | [**Software**](Software.md) | Support type | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


