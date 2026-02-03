# EdgegroupsEdgeGroupUpdatePayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dynamic** | **bool** |  | [optional] 
**endpoints** | **List[int]** |  | [optional] 
**name** | **str** |  | [optional] 
**partial_match** | **bool** |  | [optional] 
**tag_ids** | **List[int]** |  | [optional] 

## Example

```python
from openapi_client.models.edgegroups_edge_group_update_payload import EdgegroupsEdgeGroupUpdatePayload

# TODO update the JSON string below
json = "{}"
# create an instance of EdgegroupsEdgeGroupUpdatePayload from a JSON string
edgegroups_edge_group_update_payload_instance = EdgegroupsEdgeGroupUpdatePayload.from_json(json)
# print the JSON string representation of the object
print(EdgegroupsEdgeGroupUpdatePayload.to_json())

# convert the object into a dict
edgegroups_edge_group_update_payload_dict = edgegroups_edge_group_update_payload_instance.to_dict()
# create an instance of EdgegroupsEdgeGroupUpdatePayload from a dict
edgegroups_edge_group_update_payload_from_dict = EdgegroupsEdgeGroupUpdatePayload.from_dict(edgegroups_edge_group_update_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


