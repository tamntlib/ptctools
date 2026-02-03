# ResourcecontrolsResourceControlUpdatePayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**administrators_only** | **bool** | Permit access to resource only to admins | [optional] 
**public** | **bool** | Permit access to the associated resource to any user | [optional] 
**teams** | **List[int]** | List of team identifiers with access to the associated resource | [optional] 
**users** | **List[int]** | List of user identifiers with access to the associated resource | [optional] 

## Example

```python
from openapi_client.models.resourcecontrols_resource_control_update_payload import ResourcecontrolsResourceControlUpdatePayload

# TODO update the JSON string below
json = "{}"
# create an instance of ResourcecontrolsResourceControlUpdatePayload from a JSON string
resourcecontrols_resource_control_update_payload_instance = ResourcecontrolsResourceControlUpdatePayload.from_json(json)
# print the JSON string representation of the object
print(ResourcecontrolsResourceControlUpdatePayload.to_json())

# convert the object into a dict
resourcecontrols_resource_control_update_payload_dict = resourcecontrols_resource_control_update_payload_instance.to_dict()
# create an instance of ResourcecontrolsResourceControlUpdatePayload from a dict
resourcecontrols_resource_control_update_payload_from_dict = ResourcecontrolsResourceControlUpdatePayload.from_dict(resourcecontrols_resource_control_update_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


