# ReleaseChartReference


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chart_path** | **str** |  | [optional] 
**registry_id** | **int** |  | [optional] 
**repo_url** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.release_chart_reference import ReleaseChartReference

# TODO update the JSON string below
json = "{}"
# create an instance of ReleaseChartReference from a JSON string
release_chart_reference_instance = ReleaseChartReference.from_json(json)
# print the JSON string representation of the object
print(ReleaseChartReference.to_json())

# convert the object into a dict
release_chart_reference_dict = release_chart_reference_instance.to_dict()
# create an instance of ReleaseChartReference from a dict
release_chart_reference_from_dict = ReleaseChartReference.from_dict(release_chart_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


