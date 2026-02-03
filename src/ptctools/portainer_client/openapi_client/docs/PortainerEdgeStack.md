# PortainerEdgeStack


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creation_date** | **int** | StatusArray    map[EndpointID][]EdgeStackStatus &#x60;json:\&quot;StatusArray\&quot;&#x60; | [optional] 
**deployment_type** | [**PortainerEdgeStackDeploymentType**](PortainerEdgeStackDeploymentType.md) |  | [optional] 
**edge_groups** | **List[int]** |  | [optional] 
**entry_point** | **str** |  | [optional] 
**id** | **int** | EdgeStack Identifier | [optional] 
**manifest_path** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**num_deployments** | **int** |  | [optional] 
**project_path** | **str** |  | [optional] 
**status** | [**Dict[str, PortainerEdgeStackStatus]**](PortainerEdgeStackStatus.md) |  | [optional] 
**version** | **int** |  | [optional] 
**use_manifest_namespaces** | **bool** | Uses the manifest&#39;s namespaces instead of the default one | [optional] 

## Example

```python
from openapi_client.models.portainer_edge_stack import PortainerEdgeStack

# TODO update the JSON string below
json = "{}"
# create an instance of PortainerEdgeStack from a JSON string
portainer_edge_stack_instance = PortainerEdgeStack.from_json(json)
# print the JSON string representation of the object
print(PortainerEdgeStack.to_json())

# convert the object into a dict
portainer_edge_stack_dict = portainer_edge_stack_instance.to_dict()
# create an instance of PortainerEdgeStack from a dict
portainer_edge_stack_from_dict = PortainerEdgeStack.from_dict(portainer_edge_stack_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


