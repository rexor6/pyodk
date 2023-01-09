# Template

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Id | [optional] 
**name** | **str** | Name | [optional] 
**description** | **str** | Description | [optional] 
**version** | **str** | Version | [optional] 
**creation_date** | **datetime** | Creation date | [optional] 
**last_change_date** | **datetime** | Last change date | [optional] 
**creation_user** | [**UserResource**](UserResource.md) | User who created the template | [optional] 
**default_instance_type** | [**DictionaryItem**](DictionaryItem.md) | Default instance type | [optional] 
**minimum_instance_type** | [**DictionaryItem**](DictionaryItem.md) | Minimum instance type | [optional] 
**ethernet_controllers_number** | **int** | Ethernet controllers number | [optional] 
**ethernet_controllers_type** | [**DictionaryItem**](DictionaryItem.md) | Ethernet controllers type | [optional] 
**system_category** | [**DictionaryItem**](DictionaryItem.md) | System category | [optional] 
**owner_account** | [**BaseResource**](BaseResource.md) | Owner account | [optional] 
**publication_status** | [**DictionaryItem**](DictionaryItem.md) | Publication status | [optional] 
**disks** | [**list[TemplateDisk]**](TemplateDisk.md) | Disks | [optional] 
**software** | [**list[Software]**](Software.md) | Softwares | [optional] 
**template_type** | [**DictionaryItem**](DictionaryItem.md) | Template type | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


