# PortainerLDAPSearchSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_dn** | **str** | The distinguished name of the element from which the LDAP server will search for users | [optional] 
**filter** | **str** | Optional LDAP search filter used to select user elements | [optional] 
**user_name_attribute** | **str** | LDAP attribute which denotes the username | [optional] 

## Example

```python
from openapi_client.models.portainer_ldap_search_settings import PortainerLDAPSearchSettings

# TODO update the JSON string below
json = "{}"
# create an instance of PortainerLDAPSearchSettings from a JSON string
portainer_ldap_search_settings_instance = PortainerLDAPSearchSettings.from_json(json)
# print the JSON string representation of the object
print(PortainerLDAPSearchSettings.to_json())

# convert the object into a dict
portainer_ldap_search_settings_dict = portainer_ldap_search_settings_instance.to_dict()
# create an instance of PortainerLDAPSearchSettings from a dict
portainer_ldap_search_settings_from_dict = PortainerLDAPSearchSettings.from_dict(portainer_ldap_search_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


