# CustomtemplatesCustomTemplateUpdatePayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**compose_file_path_in_repository** | **str** | Path to the Stack file inside the Git repository | [optional] [default to 'docker-compose.yml']
**description** | **str** | Description of the template | 
**edge_template** | **bool** | EdgeTemplate indicates if this template purpose for Edge Stack | [optional] 
**file_content** | **str** | Content of stack file | 
**is_compose_format** | **bool** | IsComposeFormat indicates if the Kubernetes template is created from a Docker Compose file | [optional] 
**logo** | **str** | URL of the template&#39;s logo | [optional] 
**note** | **str** | A note that will be displayed in the UI. Supports HTML content | [optional] 
**platform** | [**PortainerCustomTemplatePlatform**](PortainerCustomTemplatePlatform.md) | Platform associated to the template. Valid values are: 1 - &#39;linux&#39;, 2 - &#39;windows&#39; Required for Docker stacks | [optional] 
**repository_authentication** | **bool** | Use authentication to clone the Git repository | [optional] 
**repository_authorization_type** | [**GittypesGitCredentialAuthType**](GittypesGitCredentialAuthType.md) | RepositoryAuthorizationType is the authorization type to use | [optional] 
**repository_git_credential_id** | **int** | GitCredentialID used to identify the bound git credential. Required when RepositoryAuthentication is true and RepositoryUsername/RepositoryPassword are not provided | [optional] 
**repository_password** | **str** | Password used in basic authentication or token used in token authentication. Required when RepositoryAuthentication is true and RepositoryGitCredentialID is 0 | [optional] 
**repository_reference_name** | **str** | Reference name of a Git repository hosting the Stack file | [optional] 
**repository_url** | **str** | URL of a Git repository hosting the Stack file | 
**repository_username** | **str** | Username used in basic authentication. Required when RepositoryAuthentication is true and RepositoryGitCredentialID is 0. Ignored if RepositoryAuthType is token | [optional] 
**title** | **str** | Title of the template | 
**tlsskip_verify** | **bool** | TLSSkipVerify skips SSL verification when cloning the Git repository | [optional] 
**type** | [**PortainerStackType**](PortainerStackType.md) | Type of created stack (1 - swarm, 2 - compose, 3 - kubernetes) | 
**variables** | [**List[PortainerCustomTemplateVariableDefinition]**](PortainerCustomTemplateVariableDefinition.md) | Definitions of variables in the stack file | [optional] 

## Example

```python
from openapi_client.models.customtemplates_custom_template_update_payload import CustomtemplatesCustomTemplateUpdatePayload

# TODO update the JSON string below
json = "{}"
# create an instance of CustomtemplatesCustomTemplateUpdatePayload from a JSON string
customtemplates_custom_template_update_payload_instance = CustomtemplatesCustomTemplateUpdatePayload.from_json(json)
# print the JSON string representation of the object
print(CustomtemplatesCustomTemplateUpdatePayload.to_json())

# convert the object into a dict
customtemplates_custom_template_update_payload_dict = customtemplates_custom_template_update_payload_instance.to_dict()
# create an instance of CustomtemplatesCustomTemplateUpdatePayload from a dict
customtemplates_custom_template_update_payload_from_dict = CustomtemplatesCustomTemplateUpdatePayload.from_dict(customtemplates_custom_template_update_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


