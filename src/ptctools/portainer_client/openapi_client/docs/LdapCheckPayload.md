# LdapCheckPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ldapsettings** | [**PortainerLDAPSettings**](PortainerLDAPSettings.md) |  | [optional] 

## Example

```python
from openapi_client.models.ldap_check_payload import LdapCheckPayload

# TODO update the JSON string below
json = "{}"
# create an instance of LdapCheckPayload from a JSON string
ldap_check_payload_instance = LdapCheckPayload.from_json(json)
# print the JSON string representation of the object
print(LdapCheckPayload.to_json())

# convert the object into a dict
ldap_check_payload_dict = ldap_check_payload_instance.to_dict()
# create an instance of LdapCheckPayload from a dict
ldap_check_payload_from_dict = LdapCheckPayload.from_dict(ldap_check_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


