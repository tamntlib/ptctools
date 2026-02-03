# PortainerLDAPSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**anonymous_mode** | **bool** | Enable this option if the server is configured for Anonymous access. When enabled, ReaderDN and Password will not be used | [optional] 
**auto_create_users** | **bool** | Automatically provision users and assign them to matching LDAP group names | [optional] 
**group_search_settings** | [**List[PortainerLDAPGroupSearchSettings]**](PortainerLDAPGroupSearchSettings.md) |  | [optional] 
**password** | **str** | Password of the account that will be used to search users | [optional] 
**reader_dn** | **str** | Account that will be used to search for users | [optional] 
**search_settings** | [**List[PortainerLDAPSearchSettings]**](PortainerLDAPSearchSettings.md) |  | [optional] 
**start_tls** | **bool** | Whether LDAP connection should use StartTLS | [optional] 
**tls_config** | [**PortainerTLSConfiguration**](PortainerTLSConfiguration.md) |  | [optional] 
**url** | **str** | URL or IP address of the LDAP server | [optional] 

## Example

```python
from openapi_client.models.portainer_ldap_settings import PortainerLDAPSettings

# TODO update the JSON string below
json = "{}"
# create an instance of PortainerLDAPSettings from a JSON string
portainer_ldap_settings_instance = PortainerLDAPSettings.from_json(json)
# print the JSON string representation of the object
print(PortainerLDAPSettings.to_json())

# convert the object into a dict
portainer_ldap_settings_dict = portainer_ldap_settings_instance.to_dict()
# create an instance of PortainerLDAPSettings from a dict
portainer_ldap_settings_from_dict = PortainerLDAPSettings.from_dict(portainer_ldap_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


