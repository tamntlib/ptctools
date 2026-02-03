# ReleaseChart


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**files** | [**List[ReleaseFile]**](ReleaseFile.md) | Files are miscellaneous files in a chart archive, e.g. README, LICENSE, etc. | [optional] 
**lock** | [**ReleaseLock**](ReleaseLock.md) | Lock is the contents of Chart.lock. | [optional] 
**metadata** | [**ReleaseMetadata**](ReleaseMetadata.md) | Metadata is the contents of the Chartfile. | [optional] 
**var_schema** | **List[int]** | Schema is an optional JSON schema for imposing structure on Values | [optional] 
**templates** | [**List[ReleaseFile]**](ReleaseFile.md) | Templates for this chart. | [optional] 
**values** | **Dict[str, object]** | Values are default config for this chart. | [optional] 

## Example

```python
from openapi_client.models.release_chart import ReleaseChart

# TODO update the JSON string below
json = "{}"
# create an instance of ReleaseChart from a JSON string
release_chart_instance = ReleaseChart.from_json(json)
# print the JSON string representation of the object
print(ReleaseChart.to_json())

# convert the object into a dict
release_chart_dict = release_chart_instance.to_dict()
# create an instance of ReleaseChart from a dict
release_chart_from_dict = ReleaseChart.from_dict(release_chart_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


