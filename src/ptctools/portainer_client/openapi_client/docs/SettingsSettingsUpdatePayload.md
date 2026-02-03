# SettingsSettingsUpdatePayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**edge_portainer_url** | **str** | EdgePortainerURL is the URL that is exposed to edge agents | [optional] 
**authentication_method** | **int** | Active authentication method for the Portainer instance. Valid values are: 1 for internal, 2 for LDAP, or 3 for oauth | [optional] 
**black_listed_labels** | [**List[PortainerPair]**](PortainerPair.md) | A list of label name &amp; value that will be used to hide containers when querying containers | [optional] 
**edge_agent_checkin_interval** | **int** |  | [optional] 
**enable_edge_compute_features** | **bool** | Whether edge compute features are enabled | [optional] 
**enable_telemetry** | **bool** | Whether telemetry is enabled | [optional] 
**enforce_edge_id** | **bool** | EnforceEdgeID makes Portainer store the Edge ID instead of accepting anyone | [optional] 
**global_deployment_options** | [**PortainerGlobalDeploymentOptions**](PortainerGlobalDeploymentOptions.md) | Deployment options for encouraging deployment as code | [optional] 
**helm_repository_url** | **str** | Helm repository URL | [optional] 
**internal_auth_settings** | [**PortainerInternalAuthSettings**](PortainerInternalAuthSettings.md) |  | [optional] 
**kubeconfig_expiry** | **str** | The expiry of a Kubeconfig | [optional] [default to '0']
**kubectl_shell_image** | **str** | Kubectl Shell Image | [optional] 
**ldapsettings** | [**PortainerLDAPSettings**](PortainerLDAPSettings.md) |  | [optional] 
**logo_url** | **str** | URL to a logo that will be displayed on the login page as well as on top of the sidebar. Will use default Portainer logo when value is empty string | [optional] 
**oauth_settings** | [**PortainerOAuthSettings**](PortainerOAuthSettings.md) |  | [optional] 
**snapshot_interval** | **str** | The interval in which environment(endpoint) snapshots are created | [optional] 
**templates_url** | **str** | URL to the templates that will be displayed in the UI when navigating to App Templates | [optional] 
**trust_on_first_connect** | **bool** | TrustOnFirstConnect makes Portainer accepting edge agent connection by default | [optional] 
**user_session_timeout** | **str** | The duration of a user session | [optional] 

## Example

```python
from openapi_client.models.settings_settings_update_payload import SettingsSettingsUpdatePayload

# TODO update the JSON string below
json = "{}"
# create an instance of SettingsSettingsUpdatePayload from a JSON string
settings_settings_update_payload_instance = SettingsSettingsUpdatePayload.from_json(json)
# print the JSON string representation of the object
print(SettingsSettingsUpdatePayload.to_json())

# convert the object into a dict
settings_settings_update_payload_dict = settings_settings_update_payload_instance.to_dict()
# create an instance of SettingsSettingsUpdatePayload from a dict
settings_settings_update_payload_from_dict = SettingsSettingsUpdatePayload.from_dict(settings_settings_update_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


