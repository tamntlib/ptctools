# PortainerEdge


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**async_mode** | **bool** | Deprecated 2.18 | [optional] 
**command_interval** | **int** | The command list interval for edge agent - used in edge async mode (in seconds) | [optional] 
**ping_interval** | **int** | The ping interval for edge agent - used in edge async mode (in seconds) | [optional] 
**snapshot_interval** | **int** | The snapshot interval for edge agent - used in edge async mode (in seconds) | [optional] 

## Example

```python
from openapi_client.models.portainer_edge import PortainerEdge

# TODO update the JSON string below
json = "{}"
# create an instance of PortainerEdge from a JSON string
portainer_edge_instance = PortainerEdge.from_json(json)
# print the JSON string representation of the object
print(PortainerEdge.to_json())

# convert the object into a dict
portainer_edge_dict = portainer_edge_instance.to_dict()
# create an instance of PortainerEdge from a dict
portainer_edge_from_dict = PortainerEdge.from_dict(portainer_edge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


