# CreateInstanceCommand

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authorization_method_id** | **int** | Authorization method (Password) | [optional] 
**disk_class** | **int** | Class of disk | [optional] 
**disk_size** | **int** | Size of disk in gigabytes | [optional] 
**instance_name** | **str** | Name of an instance | 
**instances_count** | **int** | Count of instances | [optional] 
**ip_address_id** | **int** | Id of ip address | [optional] 
**ssh_keys_ids** | **list[int]** | Id of ssh keys to be attached to the instance | [optional] 
**opns_ids** | **list[int]** | Id of opns where attach the instance | [optional] 
**subregion_id** | **int** | Id of target subregion | [optional] 
**template_id** | **int** | Template id | 
**type_id** | **int** | Type of an instance | [optional] 
**freemium** | **bool** | Freemium | [optional] [default to False]
**init_script** | **str** | InitScript | [optional] 
**without_public_ip** | **bool** | Freemium | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


