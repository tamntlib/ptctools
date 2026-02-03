# PortainerStackOption


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prune** | **bool** | Prune services that are no longer referenced | [optional] 

## Example

```python
from openapi_client.models.portainer_stack_option import PortainerStackOption

# TODO update the JSON string below
json = "{}"
# create an instance of PortainerStackOption from a JSON string
portainer_stack_option_instance = PortainerStackOption.from_json(json)
# print the JSON string representation of the object
print(PortainerStackOption.to_json())

# convert the object into a dict
portainer_stack_option_dict = portainer_stack_option_instance.to_dict()
# create an instance of PortainerStackOption from a dict
portainer_stack_option_from_dict = PortainerStackOption.from_dict(portainer_stack_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


