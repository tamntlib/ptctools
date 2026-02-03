# UsersUserCreatePayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** |  | 
**role** | **int** | User role (1 for administrator account and 2 for regular account) | 
**username** | **str** |  | 

## Example

```python
from openapi_client.models.users_user_create_payload import UsersUserCreatePayload

# TODO update the JSON string below
json = "{}"
# create an instance of UsersUserCreatePayload from a JSON string
users_user_create_payload_instance = UsersUserCreatePayload.from_json(json)
# print the JSON string representation of the object
print(UsersUserCreatePayload.to_json())

# convert the object into a dict
users_user_create_payload_dict = users_user_create_payload_instance.to_dict()
# create an instance of UsersUserCreatePayload from a dict
users_user_create_payload_from_dict = UsersUserCreatePayload.from_dict(users_user_create_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


