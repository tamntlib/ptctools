# PortainerKubernetesSnapshot


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**diagnostics_data** | [**PortainerDiagnosticsData**](PortainerDiagnosticsData.md) |  | [optional] 
**kubernetes_version** | **str** |  | [optional] 
**node_count** | **int** |  | [optional] 
**performance_metrics** | [**PortainerPerformanceMetrics**](PortainerPerformanceMetrics.md) |  | [optional] 
**time** | **int** |  | [optional] 
**total_cpu** | **int** |  | [optional] 
**total_memory** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.portainer_kubernetes_snapshot import PortainerKubernetesSnapshot

# TODO update the JSON string below
json = "{}"
# create an instance of PortainerKubernetesSnapshot from a JSON string
portainer_kubernetes_snapshot_instance = PortainerKubernetesSnapshot.from_json(json)
# print the JSON string representation of the object
print(PortainerKubernetesSnapshot.to_json())

# convert the object into a dict
portainer_kubernetes_snapshot_dict = portainer_kubernetes_snapshot_instance.to_dict()
# create an instance of PortainerKubernetesSnapshot from a dict
portainer_kubernetes_snapshot_from_dict = PortainerKubernetesSnapshot.from_dict(portainer_kubernetes_snapshot_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


