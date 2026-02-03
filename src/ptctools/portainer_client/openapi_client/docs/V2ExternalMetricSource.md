# V2ExternalMetricSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metric** | [**V2MetricIdentifier**](V2MetricIdentifier.md) | metric identifies the target metric by name and selector | [optional] 
**target** | [**V2MetricTarget**](V2MetricTarget.md) | target specifies the target value for the given metric | [optional] 

## Example

```python
from openapi_client.models.v2_external_metric_source import V2ExternalMetricSource

# TODO update the JSON string below
json = "{}"
# create an instance of V2ExternalMetricSource from a JSON string
v2_external_metric_source_instance = V2ExternalMetricSource.from_json(json)
# print the JSON string representation of the object
print(V2ExternalMetricSource.to_json())

# convert the object into a dict
v2_external_metric_source_dict = v2_external_metric_source_instance.to_dict()
# create an instance of V2ExternalMetricSource from a dict
v2_external_metric_source_from_dict = V2ExternalMetricSource.from_dict(v2_external_metric_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


