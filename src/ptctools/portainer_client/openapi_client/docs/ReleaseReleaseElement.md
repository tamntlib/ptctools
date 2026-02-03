# ReleaseReleaseElement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_version** | **str** |  | [optional] 
**chart** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**namespace** | **str** |  | [optional] 
**revision** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**updated** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.release_release_element import ReleaseReleaseElement

# TODO update the JSON string below
json = "{}"
# create an instance of ReleaseReleaseElement from a JSON string
release_release_element_instance = ReleaseReleaseElement.from_json(json)
# print the JSON string representation of the object
print(ReleaseReleaseElement.to_json())

# convert the object into a dict
release_release_element_dict = release_release_element_instance.to_dict()
# create an instance of ReleaseReleaseElement from a dict
release_release_element_from_dict = ReleaseReleaseElement.from_dict(release_release_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


