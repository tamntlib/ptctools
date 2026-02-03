# UsersAdminInitPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** | Password for the admin user | 
**username** | **str** | Username for the admin user | 

## Example

```python
from openapi_client.models.users_admin_init_payload import UsersAdminInitPayload

# TODO update the JSON string below
json = "{}"
# create an instance of UsersAdminInitPayload from a JSON string
users_admin_init_payload_instance = UsersAdminInitPayload.from_json(json)
# print the JSON string representation of the object
print(UsersAdminInitPayload.to_json())

# convert the object into a dict
users_admin_init_payload_dict = users_admin_init_payload_instance.to_dict()
# create an instance of UsersAdminInitPayload from a dict
users_admin_init_payload_from_dict = UsersAdminInitPayload.from_dict(users_admin_init_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


