# PortainerEdgeStackDeploymentStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** |  | [optional] 
**rollback_to** | **int** | EE only feature | [optional] 
**version** | **int** |  | [optional] 
**time** | **int** |  | [optional] 
**type** | [**PortainerEdgeStackStatusType**](PortainerEdgeStackStatusType.md) |  | [optional] 

## Example

```python
from openapi_client.models.portainer_edge_stack_deployment_status import PortainerEdgeStackDeploymentStatus

# TODO update the JSON string below
json = "{}"
# create an instance of PortainerEdgeStackDeploymentStatus from a JSON string
portainer_edge_stack_deployment_status_instance = PortainerEdgeStackDeploymentStatus.from_json(json)
# print the JSON string representation of the object
print(PortainerEdgeStackDeploymentStatus.to_json())

# convert the object into a dict
portainer_edge_stack_deployment_status_dict = portainer_edge_stack_deployment_status_instance.to_dict()
# create an instance of PortainerEdgeStackDeploymentStatus from a dict
portainer_edge_stack_deployment_status_from_dict = PortainerEdgeStackDeploymentStatus.from_dict(portainer_edge_stack_deployment_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


