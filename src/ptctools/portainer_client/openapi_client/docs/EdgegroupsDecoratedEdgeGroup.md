# EdgegroupsDecoratedEdgeGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dynamic** | **bool** |  | [optional] 
**endpoint_ids** | **int** | Shadow to avoid exposing in the API | [optional] 
**endpoints** | **List[int]** | Deprecated: only used for API responses | [optional] 
**has_edge_job** | **bool** |  | [optional] 
**has_edge_stack** | **bool** |  | [optional] 
**id** | **int** | EdgeGroup Identifier | [optional] 
**name** | **str** |  | [optional] 
**partial_match** | **bool** |  | [optional] 
**tag_ids** | **List[int]** |  | [optional] 
**trusted_endpoints** | **List[int]** |  | [optional] 
**endpoint_types** | [**List[PortainerEndpointType]**](PortainerEndpointType.md) |  | [optional] 

## Example

```python
from openapi_client.models.edgegroups_decorated_edge_group import EdgegroupsDecoratedEdgeGroup

# TODO update the JSON string below
json = "{}"
# create an instance of EdgegroupsDecoratedEdgeGroup from a JSON string
edgegroups_decorated_edge_group_instance = EdgegroupsDecoratedEdgeGroup.from_json(json)
# print the JSON string representation of the object
print(EdgegroupsDecoratedEdgeGroup.to_json())

# convert the object into a dict
edgegroups_decorated_edge_group_dict = edgegroups_decorated_edge_group_instance.to_dict()
# create an instance of EdgegroupsDecoratedEdgeGroup from a dict
edgegroups_decorated_edge_group_from_dict = EdgegroupsDecoratedEdgeGroup.from_dict(edgegroups_decorated_edge_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


