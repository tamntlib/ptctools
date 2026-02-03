# PortainerEdgeStackStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**details** | [**PortainerEdgeStackStatusDetails**](PortainerEdgeStackStatusDetails.md) | Deprecated | [optional] 
**error** | **str** | Deprecated | [optional] 
**ready_re_pull_image** | **bool** | ReadyRePullImage is a flag to indicate whether the auto update is trigger to re-pull image | [optional] 
**type** | [**PortainerEdgeStackStatusType**](PortainerEdgeStackStatusType.md) | Deprecated | [optional] 
**deployment_info** | [**PortainerStackDeploymentInfo**](PortainerStackDeploymentInfo.md) | EE only feature | [optional] 
**endpoint_id** | **int** |  | [optional] 
**status** | [**List[PortainerEdgeStackDeploymentStatus]**](PortainerEdgeStackDeploymentStatus.md) |  | [optional] 

## Example

```python
from openapi_client.models.portainer_edge_stack_status import PortainerEdgeStackStatus

# TODO update the JSON string below
json = "{}"
# create an instance of PortainerEdgeStackStatus from a JSON string
portainer_edge_stack_status_instance = PortainerEdgeStackStatus.from_json(json)
# print the JSON string representation of the object
print(PortainerEdgeStackStatus.to_json())

# convert the object into a dict
portainer_edge_stack_status_dict = portainer_edge_stack_status_instance.to_dict()
# create an instance of PortainerEdgeStackStatus from a dict
portainer_edge_stack_status_from_dict = PortainerEdgeStackStatus.from_dict(portainer_edge_stack_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


