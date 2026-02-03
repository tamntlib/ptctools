# UsersUserAccessTokenCreatePayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | 
**password** | **str** |  | 

## Example

```python
from openapi_client.models.users_user_access_token_create_payload import UsersUserAccessTokenCreatePayload

# TODO update the JSON string below
json = "{}"
# create an instance of UsersUserAccessTokenCreatePayload from a JSON string
users_user_access_token_create_payload_instance = UsersUserAccessTokenCreatePayload.from_json(json)
# print the JSON string representation of the object
print(UsersUserAccessTokenCreatePayload.to_json())

# convert the object into a dict
users_user_access_token_create_payload_dict = users_user_access_token_create_payload_instance.to_dict()
# create an instance of UsersUserAccessTokenCreatePayload from a dict
users_user_access_token_create_payload_from_dict = UsersUserAccessTokenCreatePayload.from_dict(users_user_access_token_create_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


