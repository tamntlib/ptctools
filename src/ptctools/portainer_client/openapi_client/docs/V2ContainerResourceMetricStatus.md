# V2ContainerResourceMetricStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**container** | **str** | container is the name of the container in the pods of the scaling target | [optional] 
**current** | [**V2MetricValueStatus**](V2MetricValueStatus.md) | current contains the current value for the given metric | [optional] 
**name** | [**V1ResourceName**](V1ResourceName.md) | name is the name of the resource in question. | [optional] 

## Example

```python
from openapi_client.models.v2_container_resource_metric_status import V2ContainerResourceMetricStatus

# TODO update the JSON string below
json = "{}"
# create an instance of V2ContainerResourceMetricStatus from a JSON string
v2_container_resource_metric_status_instance = V2ContainerResourceMetricStatus.from_json(json)
# print the JSON string representation of the object
print(V2ContainerResourceMetricStatus.to_json())

# convert the object into a dict
v2_container_resource_metric_status_dict = v2_container_resource_metric_status_instance.to_dict()
# create an instance of V2ContainerResourceMetricStatus from a dict
v2_container_resource_metric_status_from_dict = V2ContainerResourceMetricStatus.from_dict(v2_container_resource_metric_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


