# V2ContainerResourceMetricSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**container** | **str** | container is the name of the container in the pods of the scaling target | [optional] 
**name** | [**V1ResourceName**](V1ResourceName.md) | name is the name of the resource in question. | [optional] 
**target** | [**V2MetricTarget**](V2MetricTarget.md) | target specifies the target value for the given metric | [optional] 

## Example

```python
from openapi_client.models.v2_container_resource_metric_source import V2ContainerResourceMetricSource

# TODO update the JSON string below
json = "{}"
# create an instance of V2ContainerResourceMetricSource from a JSON string
v2_container_resource_metric_source_instance = V2ContainerResourceMetricSource.from_json(json)
# print the JSON string representation of the object
print(V2ContainerResourceMetricSource.to_json())

# convert the object into a dict
v2_container_resource_metric_source_dict = v2_container_resource_metric_source_instance.to_dict()
# create an instance of V2ContainerResourceMetricSource from a dict
v2_container_resource_metric_source_from_dict = V2ContainerResourceMetricSource.from_dict(v2_container_resource_metric_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


