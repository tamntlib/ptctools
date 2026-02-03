# ReleaseFile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **List[int]** | Data is the template as byte data. | [optional] 
**name** | **str** | Name is the path-like name of the template. | [optional] 

## Example

```python
from openapi_client.models.release_file import ReleaseFile

# TODO update the JSON string below
json = "{}"
# create an instance of ReleaseFile from a JSON string
release_file_instance = ReleaseFile.from_json(json)
# print the JSON string representation of the object
print(ReleaseFile.to_json())

# convert the object into a dict
release_file_dict = release_file_instance.to_dict()
# create an instance of ReleaseFile from a dict
release_file_from_dict = ReleaseFile.from_dict(release_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


