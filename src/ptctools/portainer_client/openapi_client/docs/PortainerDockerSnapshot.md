# PortainerDockerSnapshot


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**container_count** | **int** |  | [optional] 
**diagnostics_data** | [**PortainerDiagnosticsData**](PortainerDiagnosticsData.md) |  | [optional] 
**docker_snapshot_raw** | **object** |  | [optional] 
**docker_version** | **str** |  | [optional] 
**gpu_use_all** | **bool** |  | [optional] 
**gpu_use_list** | **List[str]** |  | [optional] 
**healthy_container_count** | **int** |  | [optional] 
**image_count** | **int** |  | [optional] 
**is_podman** | **bool** |  | [optional] 
**node_count** | **int** |  | [optional] 
**performance_metrics** | [**PortainerPerformanceMetrics**](PortainerPerformanceMetrics.md) |  | [optional] 
**running_container_count** | **int** |  | [optional] 
**service_count** | **int** |  | [optional] 
**stack_count** | **int** |  | [optional] 
**stopped_container_count** | **int** |  | [optional] 
**swarm** | **bool** |  | [optional] 
**time** | **int** |  | [optional] 
**total_cpu** | **int** |  | [optional] 
**total_memory** | **int** |  | [optional] 
**unhealthy_container_count** | **int** |  | [optional] 
**volume_count** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.portainer_docker_snapshot import PortainerDockerSnapshot

# TODO update the JSON string below
json = "{}"
# create an instance of PortainerDockerSnapshot from a JSON string
portainer_docker_snapshot_instance = PortainerDockerSnapshot.from_json(json)
# print the JSON string representation of the object
print(PortainerDockerSnapshot.to_json())

# convert the object into a dict
portainer_docker_snapshot_dict = portainer_docker_snapshot_instance.to_dict()
# create an instance of PortainerDockerSnapshot from a dict
portainer_docker_snapshot_from_dict = PortainerDockerSnapshot.from_dict(portainer_docker_snapshot_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


