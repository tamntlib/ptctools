# ReleaseMaintainer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | Email is an optional email address to contact the named maintainer | [optional] 
**name** | **str** | Name is a user name or organization name | [optional] 
**url** | **str** | URL is an optional URL to an address for the named maintainer | [optional] 

## Example

```python
from openapi_client.models.release_maintainer import ReleaseMaintainer

# TODO update the JSON string below
json = "{}"
# create an instance of ReleaseMaintainer from a JSON string
release_maintainer_instance = ReleaseMaintainer.from_json(json)
# print the JSON string representation of the object
print(ReleaseMaintainer.to_json())

# convert the object into a dict
release_maintainer_dict = release_maintainer_instance.to_dict()
# create an instance of ReleaseMaintainer from a dict
release_maintainer_from_dict = ReleaseMaintainer.from_dict(release_maintainer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


