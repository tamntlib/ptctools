# PortainerTag


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoint_groups** | **Dict[str, bool]** | A set of environment(endpoint) group ids that have this tag | [optional] 
**endpoints** | **Dict[str, bool]** | A set of environment(endpoint) ids that have this tag | [optional] 
**name** | **str** | Tag name | [optional] 
**id** | **int** | Tag identifier | [optional] 

## Example

```python
from openapi_client.models.portainer_tag import PortainerTag

# TODO update the JSON string below
json = "{}"
# create an instance of PortainerTag from a JSON string
portainer_tag_instance = PortainerTag.from_json(json)
# print the JSON string representation of the object
print(PortainerTag.to_json())

# convert the object into a dict
portainer_tag_dict = portainer_tag_instance.to_dict()
# create an instance of PortainerTag from a dict
portainer_tag_from_dict = PortainerTag.from_dict(portainer_tag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


