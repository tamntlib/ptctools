# EdgestacksUpdateEdgeStackPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deployment_type** | [**PortainerEdgeStackDeploymentType**](PortainerEdgeStackDeploymentType.md) |  | [optional] 
**edge_groups** | **List[int]** |  | [optional] 
**stack_file_content** | **str** |  | [optional] 
**update_version** | **bool** |  | [optional] 
**use_manifest_namespaces** | **bool** | Uses the manifest&#39;s namespaces instead of the default one | [optional] 

## Example

```python
from openapi_client.models.edgestacks_update_edge_stack_payload import EdgestacksUpdateEdgeStackPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EdgestacksUpdateEdgeStackPayload from a JSON string
edgestacks_update_edge_stack_payload_instance = EdgestacksUpdateEdgeStackPayload.from_json(json)
# print the JSON string representation of the object
print(EdgestacksUpdateEdgeStackPayload.to_json())

# convert the object into a dict
edgestacks_update_edge_stack_payload_dict = edgestacks_update_edge_stack_payload_instance.to_dict()
# create an instance of EdgestacksUpdateEdgeStackPayload from a dict
edgestacks_update_edge_stack_payload_from_dict = EdgestacksUpdateEdgeStackPayload.from_dict(edgestacks_update_edge_stack_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


