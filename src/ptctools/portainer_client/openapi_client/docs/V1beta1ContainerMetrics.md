# V1beta1ContainerMetrics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Container name corresponding to the one from pod.spec.containers. | [optional] 
**usage** | [**Dict[str, ResourceQuantity]**](ResourceQuantity.md) | The memory usage is the memory working set. | [optional] 

## Example

```python
from openapi_client.models.v1beta1_container_metrics import V1beta1ContainerMetrics

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1ContainerMetrics from a JSON string
v1beta1_container_metrics_instance = V1beta1ContainerMetrics.from_json(json)
# print the JSON string representation of the object
print(V1beta1ContainerMetrics.to_json())

# convert the object into a dict
v1beta1_container_metrics_dict = v1beta1_container_metrics_instance.to_dict()
# create an instance of V1beta1ContainerMetrics from a dict
v1beta1_container_metrics_from_dict = V1beta1ContainerMetrics.from_dict(v1beta1_container_metrics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


