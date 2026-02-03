# UsersUserUpdatePayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_password** | **str** |  | 
**password** | **str** |  | 
**role** | **int** | User role (1 for administrator account and 2 for regular account) | 
**theme** | [**UsersThemePayload**](UsersThemePayload.md) |  | [optional] 
**use_cache** | **bool** |  | 
**username** | **str** |  | 

## Example

```python
from openapi_client.models.users_user_update_payload import UsersUserUpdatePayload

# TODO update the JSON string below
json = "{}"
# create an instance of UsersUserUpdatePayload from a JSON string
users_user_update_payload_instance = UsersUserUpdatePayload.from_json(json)
# print the JSON string representation of the object
print(UsersUserUpdatePayload.to_json())

# convert the object into a dict
users_user_update_payload_dict = users_user_update_payload_instance.to_dict()
# create an instance of UsersUserUpdatePayload from a dict
users_user_update_payload_from_dict = UsersUserUpdatePayload.from_dict(users_user_update_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


