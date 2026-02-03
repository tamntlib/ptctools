# V2ResourceMetricSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | [**V1ResourceName**](V1ResourceName.md) | name is the name of the resource in question. | [optional] 
**target** | [**V2MetricTarget**](V2MetricTarget.md) | target specifies the target value for the given metric | [optional] 

## Example

```python
from openapi_client.models.v2_resource_metric_source import V2ResourceMetricSource

# TODO update the JSON string below
json = "{}"
# create an instance of V2ResourceMetricSource from a JSON string
v2_resource_metric_source_instance = V2ResourceMetricSource.from_json(json)
# print the JSON string representation of the object
print(V2ResourceMetricSource.to_json())

# convert the object into a dict
v2_resource_metric_source_dict = v2_resource_metric_source_instance.to_dict()
# create an instance of V2ResourceMetricSource from a dict
v2_resource_metric_source_from_dict = V2ResourceMetricSource.from_dict(v2_resource_metric_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


