# PortainerPerformanceMetrics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpu_usage** | **float** |  | [optional] 
**memory_usage** | **float** |  | [optional] 
**network_usage** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.portainer_performance_metrics import PortainerPerformanceMetrics

# TODO update the JSON string below
json = "{}"
# create an instance of PortainerPerformanceMetrics from a JSON string
portainer_performance_metrics_instance = PortainerPerformanceMetrics.from_json(json)
# print the JSON string representation of the object
print(PortainerPerformanceMetrics.to_json())

# convert the object into a dict
portainer_performance_metrics_dict = portainer_performance_metrics_instance.to_dict()
# create an instance of PortainerPerformanceMetrics from a dict
portainer_performance_metrics_from_dict = PortainerPerformanceMetrics.from_dict(portainer_performance_metrics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


