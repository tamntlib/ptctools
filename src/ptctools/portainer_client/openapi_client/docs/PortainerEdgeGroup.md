# PortainerEdgeGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dynamic** | **bool** |  | [optional] 
**endpoint_ids** | **object** |  | [optional] 
**endpoints** | **List[int]** | Deprecated: only used for API responses | [optional] 
**id** | **int** | EdgeGroup Identifier | [optional] 
**name** | **str** |  | [optional] 
**partial_match** | **bool** |  | [optional] 
**tag_ids** | **List[int]** |  | [optional] 

## Example

```python
from openapi_client.models.portainer_edge_group import PortainerEdgeGroup

# TODO update the JSON string below
json = "{}"
# create an instance of PortainerEdgeGroup from a JSON string
portainer_edge_group_instance = PortainerEdgeGroup.from_json(json)
# print the JSON string representation of the object
print(PortainerEdgeGroup.to_json())

# convert the object into a dict
portainer_edge_group_dict = portainer_edge_group_instance.to_dict()
# create an instance of PortainerEdgeGroup from a dict
portainer_edge_group_from_dict = PortainerEdgeGroup.from_dict(portainer_edge_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


