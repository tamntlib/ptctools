# EdgestacksEdgeStackFromStringPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deployment_type** | [**PortainerEdgeStackDeploymentType**](PortainerEdgeStackDeploymentType.md) | Deployment type to deploy this stack Valid values are: 0 - &#39;compose&#39;, 1 - &#39;kubernetes&#39; compose is enabled only for docker environments kubernetes is enabled only for kubernetes environments | [optional] 
**edge_groups** | **List[int]** | List of identifiers of EdgeGroups | [optional] 
**name** | **str** | Name of the stack Max length: 255 Name must only contains lowercase characters, numbers, hyphens, or underscores Name must start with a lowercase character or number Example: stack-name or stack_123 or stackName | 
**registries** | **List[int]** | List of Registries to use for this stack | [optional] 
**stack_file_content** | **str** | Content of the Stack file | 
**use_manifest_namespaces** | **bool** | Uses the manifest&#39;s namespaces instead of the default one | [optional] 

## Example

```python
from openapi_client.models.edgestacks_edge_stack_from_string_payload import EdgestacksEdgeStackFromStringPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EdgestacksEdgeStackFromStringPayload from a JSON string
edgestacks_edge_stack_from_string_payload_instance = EdgestacksEdgeStackFromStringPayload.from_json(json)
# print the JSON string representation of the object
print(EdgestacksEdgeStackFromStringPayload.to_json())

# convert the object into a dict
edgestacks_edge_stack_from_string_payload_dict = edgestacks_edge_stack_from_string_payload_instance.to_dict()
# create an instance of EdgestacksEdgeStackFromStringPayload from a dict
edgestacks_edge_stack_from_string_payload_from_dict = EdgestacksEdgeStackFromStringPayload.from_dict(edgestacks_edge_stack_from_string_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


