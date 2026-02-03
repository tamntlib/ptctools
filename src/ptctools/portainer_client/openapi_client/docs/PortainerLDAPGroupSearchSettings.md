# PortainerLDAPGroupSearchSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_attribute** | **str** | LDAP attribute which denotes the group membership | [optional] 
**group_base_dn** | **str** | The distinguished name of the element from which the LDAP server will search for groups | [optional] 
**group_filter** | **str** | The LDAP search filter used to select group elements, optional | [optional] 

## Example

```python
from openapi_client.models.portainer_ldap_group_search_settings import PortainerLDAPGroupSearchSettings

# TODO update the JSON string below
json = "{}"
# create an instance of PortainerLDAPGroupSearchSettings from a JSON string
portainer_ldap_group_search_settings_instance = PortainerLDAPGroupSearchSettings.from_json(json)
# print the JSON string representation of the object
print(PortainerLDAPGroupSearchSettings.to_json())

# convert the object into a dict
portainer_ldap_group_search_settings_dict = portainer_ldap_group_search_settings_instance.to_dict()
# create an instance of PortainerLDAPGroupSearchSettings from a dict
portainer_ldap_group_search_settings_from_dict = PortainerLDAPGroupSearchSettings.from_dict(portainer_ldap_group_search_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


