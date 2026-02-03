# UsersUserUpdatePasswordPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_password** | **str** | New Password | 
**password** | **str** | Current Password | 

## Example

```python
from openapi_client.models.users_user_update_password_payload import UsersUserUpdatePasswordPayload

# TODO update the JSON string below
json = "{}"
# create an instance of UsersUserUpdatePasswordPayload from a JSON string
users_user_update_password_payload_instance = UsersUserUpdatePasswordPayload.from_json(json)
# print the JSON string representation of the object
print(UsersUserUpdatePasswordPayload.to_json())

# convert the object into a dict
users_user_update_password_payload_dict = users_user_update_password_payload_instance.to_dict()
# create an instance of UsersUserUpdatePasswordPayload from a dict
users_user_update_password_payload_from_dict = UsersUserUpdatePasswordPayload.from_dict(users_user_update_password_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


