# ReleaseLock


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dependencies** | [**List[ReleaseDependency]**](ReleaseDependency.md) | Dependencies is the list of dependencies that this lock file has locked. | [optional] 
**digest** | **str** | Digest is a hash of the dependencies in Chart.yaml. | [optional] 
**generated** | **str** | Generated is the date the lock file was last generated. | [optional] 

## Example

```python
from openapi_client.models.release_lock import ReleaseLock

# TODO update the JSON string below
json = "{}"
# create an instance of ReleaseLock from a JSON string
release_lock_instance = ReleaseLock.from_json(json)
# print the JSON string representation of the object
print(ReleaseLock.to_json())

# convert the object into a dict
release_lock_dict = release_lock_instance.to_dict()
# create an instance of ReleaseLock from a dict
release_lock_from_dict = ReleaseLock.from_dict(release_lock_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


