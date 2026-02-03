# PortainerSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_secret** | **str** | Container environment parameter AGENT_SECRET | [optional] 
**allow_bind_mounts_for_regular_users** | **bool** |  | [optional] 
**allow_container_capabilities_for_regular_users** | **bool** |  | [optional] 
**allow_device_mapping_for_regular_users** | **bool** |  | [optional] 
**allow_host_namespace_for_regular_users** | **bool** |  | [optional] 
**allow_privileged_mode_for_regular_users** | **bool** |  | [optional] 
**allow_stack_management_for_regular_users** | **bool** |  | [optional] 
**allow_volume_browser_for_regular_users** | **bool** |  | [optional] 
**authentication_method** | [**PortainerAuthenticationMethod**](PortainerAuthenticationMethod.md) | Active authentication method for the Portainer instance. Valid values are: 1 for internal, 2 for LDAP, or 3 for oauth | [optional] 
**black_listed_labels** | [**List[PortainerPair]**](PortainerPair.md) | A list of label name &amp; value that will be used to hide containers when querying containers | [optional] 
**display_donation_header** | **bool** | Deprecated fields | [optional] 
**display_external_contributors** | **bool** |  | [optional] 
**edge** | [**PortainerEdge**](PortainerEdge.md) |  | [optional] 
**edge_agent_checkin_interval** | **int** | The default check in interval for edge agent (in seconds) | [optional] 
**edge_portainer_url** | **str** | EdgePortainerURL is the URL that is exposed to edge agents | [optional] 
**enable_edge_compute_features** | **bool** | Whether edge compute features are enabled | [optional] 
**enable_host_management_features** | **bool** | Deprecated fields v26 | [optional] 
**enable_telemetry** | **bool** | Whether telemetry is enabled | [optional] 
**enforce_edge_id** | **bool** | EnforceEdgeID makes Portainer store the Edge ID instead of accepting anyone | [optional] 
**feature_flag_settings** | **Dict[str, bool]** |  | [optional] 
**global_deployment_options** | [**PortainerGlobalDeploymentOptions**](PortainerGlobalDeploymentOptions.md) | Deployment options for encouraging git ops workflows | [optional] 
**helm_repository_url** | **str** | Helm repository URL, defaults to \&quot;https://charts.bitnami.com/bitnami\&quot; | [optional] 
**internal_auth_settings** | [**PortainerInternalAuthSettings**](PortainerInternalAuthSettings.md) |  | [optional] 
**is_docker_desktop_extension** | **bool** |  | [optional] 
**kubeconfig_expiry** | **str** | The expiry of a Kubeconfig | [optional] 
**kubectl_shell_image** | **str** | KubectlImage, defaults to portainer/kubectl-shell | [optional] 
**ldap_settings** | [**PortainerLDAPSettings**](PortainerLDAPSettings.md) |  | [optional] 
**logo_url** | **str** | URL to a logo that will be displayed on the login page as well as on top of the sidebar. Will use default Portainer logo when value is empty string | [optional] 
**o_auth_settings** | [**PortainerOAuthSettings**](PortainerOAuthSettings.md) |  | [optional] 
**snapshot_interval** | **str** | The interval in which environment(endpoint) snapshots are created | [optional] 
**templates_url** | **str** | URL to the templates that will be displayed in the UI when navigating to App Templates | [optional] 
**trust_on_first_connect** | **bool** | TrustOnFirstConnect makes Portainer accepting edge agent connection by default | [optional] 
**user_session_timeout** | **str** | The duration of a user session | [optional] 
**open_amt_configuration** | [**PortainerOpenAMTConfiguration**](PortainerOpenAMTConfiguration.md) |  | [optional] 

## Example

```python
from openapi_client.models.portainer_settings import PortainerSettings

# TODO update the JSON string below
json = "{}"
# create an instance of PortainerSettings from a JSON string
portainer_settings_instance = PortainerSettings.from_json(json)
# print the JSON string representation of the object
print(PortainerSettings.to_json())

# convert the object into a dict
portainer_settings_dict = portainer_settings_instance.to_dict()
# create an instance of PortainerSettings from a dict
portainer_settings_from_dict = PortainerSettings.from_dict(portainer_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


