# UsersAddHelmRepoUrlPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.users_add_helm_repo_url_payload import UsersAddHelmRepoUrlPayload

# TODO update the JSON string below
json = "{}"
# create an instance of UsersAddHelmRepoUrlPayload from a JSON string
users_add_helm_repo_url_payload_instance = UsersAddHelmRepoUrlPayload.from_json(json)
# print the JSON string representation of the object
print(UsersAddHelmRepoUrlPayload.to_json())

# convert the object into a dict
users_add_helm_repo_url_payload_dict = users_add_helm_repo_url_payload_instance.to_dict()
# create an instance of UsersAddHelmRepoUrlPayload from a dict
users_add_helm_repo_url_payload_from_dict = UsersAddHelmRepoUrlPayload.from_dict(users_add_helm_repo_url_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


