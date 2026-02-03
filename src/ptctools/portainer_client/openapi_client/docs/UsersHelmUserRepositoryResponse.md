# UsersHelmUserRepositoryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**global_repository** | **str** |  | [optional] 
**user_repositories** | [**List[PortainerHelmUserRepository]**](PortainerHelmUserRepository.md) |  | [optional] 

## Example

```python
from openapi_client.models.users_helm_user_repository_response import UsersHelmUserRepositoryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UsersHelmUserRepositoryResponse from a JSON string
users_helm_user_repository_response_instance = UsersHelmUserRepositoryResponse.from_json(json)
# print the JSON string representation of the object
print(UsersHelmUserRepositoryResponse.to_json())

# convert the object into a dict
users_helm_user_repository_response_dict = users_helm_user_repository_response_instance.to_dict()
# create an instance of UsersHelmUserRepositoryResponse from a dict
users_helm_user_repository_response_from_dict = UsersHelmUserRepositoryResponse.from_dict(users_helm_user_repository_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


