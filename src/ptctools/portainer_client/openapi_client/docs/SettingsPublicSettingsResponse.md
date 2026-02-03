# SettingsPublicSettingsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authentication_method** | [**PortainerAuthenticationMethod**](PortainerAuthenticationMethod.md) | Active authentication method for the Portainer instance. Valid values are: 1 for internal, 2 for LDAP, or 3 for oauth | [optional] 
**enable_edge_compute_features** | **bool** | Whether edge compute features are enabled | [optional] 
**enable_telemetry** | **bool** | Whether telemetry is enabled | [optional] 
**features** | **Dict[str, bool]** | Supported feature flags | [optional] 
**global_deployment_options** | [**PortainerGlobalDeploymentOptions**](PortainerGlobalDeploymentOptions.md) | Deployment options for encouraging deployment as code | [optional] 
**is_docker_desktop_extension** | **bool** |  | [optional] 
**logo_url** | **str** | URL to a logo that will be displayed on the login page as well as on top of the sidebar. Will use default Portainer logo when value is empty string | [optional] 
**o_auth_login_uri** | **str** | The URL used for oauth login | [optional] 
**o_auth_logout_uri** | **str** | The URL used for oauth logout | [optional] 
**required_password_length** | **int** | The minimum required length for a password of any user when using internal auth mode | [optional] 
**team_sync** | **bool** | Whether team sync is enabled | [optional] 
**edge** | [**SettingsPublicSettingsResponseEdge**](SettingsPublicSettingsResponseEdge.md) |  | [optional] 
**is_amt_enabled** | **bool** | Whether AMT is enabled | [optional] 
**kubeconfig_expiry** | **str** | The expiry of a Kubeconfig | [optional] [default to '0']

## Example

```python
from openapi_client.models.settings_public_settings_response import SettingsPublicSettingsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SettingsPublicSettingsResponse from a JSON string
settings_public_settings_response_instance = SettingsPublicSettingsResponse.from_json(json)
# print the JSON string representation of the object
print(SettingsPublicSettingsResponse.to_json())

# convert the object into a dict
settings_public_settings_response_dict = settings_public_settings_response_instance.to_dict()
# create an instance of SettingsPublicSettingsResponse from a dict
settings_public_settings_response_from_dict = SettingsPublicSettingsResponse.from_dict(settings_public_settings_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


