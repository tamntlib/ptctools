# ResourcecontrolsResourceControlCreatePayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**administrators_only** | **bool** | Permit access to resource only to admins | [optional] 
**public** | **bool** | Permit access to the associated resource to any user | [optional] 
**resource_id** | **str** |  | 
**sub_resource_ids** | **List[str]** | List of Docker resources that will inherit this access control | [optional] 
**teams** | **List[int]** | List of team identifiers with access to the associated resource | [optional] 
**type** | [**PortainerResourceControlType**](PortainerResourceControlType.md) | Type of Resource. Valid values are: 1 - container, 2 - service 3 - volume, 4 - network, 5 - secret, 6 - stack, 7 - config, 8 - custom template, 9 - azure-container-group | 
**users** | **List[int]** | List of user identifiers with access to the associated resource | [optional] 

## Example

```python
from openapi_client.models.resourcecontrols_resource_control_create_payload import ResourcecontrolsResourceControlCreatePayload

# TODO update the JSON string below
json = "{}"
# create an instance of ResourcecontrolsResourceControlCreatePayload from a JSON string
resourcecontrols_resource_control_create_payload_instance = ResourcecontrolsResourceControlCreatePayload.from_json(json)
# print the JSON string representation of the object
print(ResourcecontrolsResourceControlCreatePayload.to_json())

# convert the object into a dict
resourcecontrols_resource_control_create_payload_dict = resourcecontrols_resource_control_create_payload_instance.to_dict()
# create an instance of ResourcecontrolsResourceControlCreatePayload from a dict
resourcecontrols_resource_control_create_payload_from_dict = ResourcecontrolsResourceControlCreatePayload.from_dict(resourcecontrols_resource_control_create_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


