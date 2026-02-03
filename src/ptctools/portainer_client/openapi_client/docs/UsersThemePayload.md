# UsersThemePayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**color** | **str** | Color represents the color theme of the UI | [optional] 

## Example

```python
from openapi_client.models.users_theme_payload import UsersThemePayload

# TODO update the JSON string below
json = "{}"
# create an instance of UsersThemePayload from a JSON string
users_theme_payload_instance = UsersThemePayload.from_json(json)
# print the JSON string representation of the object
print(UsersThemePayload.to_json())

# convert the object into a dict
users_theme_payload_dict = users_theme_payload_instance.to_dict()
# create an instance of UsersThemePayload from a dict
users_theme_payload_from_dict = UsersThemePayload.from_dict(users_theme_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


