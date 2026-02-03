# PortainerOAuthSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token_uri** | **str** |  | [optional] 
**auth_style** | [**Oauth2AuthStyle**](Oauth2AuthStyle.md) |  | [optional] 
**authorization_uri** | **str** |  | [optional] 
**client_id** | **str** |  | [optional] 
**client_secret** | **str** |  | [optional] 
**default_team_id** | **int** |  | [optional] 
**kube_secret_key** | **List[int]** |  | [optional] 
**logout_uri** | **str** |  | [optional] 
**o_auth_auto_create_users** | **bool** |  | [optional] 
**redirect_uri** | **str** |  | [optional] 
**resource_uri** | **str** |  | [optional] 
**sso** | **bool** |  | [optional] 
**scopes** | **str** |  | [optional] 
**user_identifier** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.portainer_o_auth_settings import PortainerOAuthSettings

# TODO update the JSON string below
json = "{}"
# create an instance of PortainerOAuthSettings from a JSON string
portainer_o_auth_settings_instance = PortainerOAuthSettings.from_json(json)
# print the JSON string representation of the object
print(PortainerOAuthSettings.to_json())

# convert the object into a dict
portainer_o_auth_settings_dict = portainer_o_auth_settings_instance.to_dict()
# create an instance of PortainerOAuthSettings from a dict
portainer_o_auth_settings_from_dict = PortainerOAuthSettings.from_dict(portainer_o_auth_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


