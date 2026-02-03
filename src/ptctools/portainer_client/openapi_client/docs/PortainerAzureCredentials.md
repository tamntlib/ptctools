# PortainerAzureCredentials


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_id** | **str** | Azure application ID | [optional] 
**authentication_key** | **str** | Azure authentication key | [optional] 
**tenant_id** | **str** | Azure tenant ID | [optional] 

## Example

```python
from openapi_client.models.portainer_azure_credentials import PortainerAzureCredentials

# TODO update the JSON string below
json = "{}"
# create an instance of PortainerAzureCredentials from a JSON string
portainer_azure_credentials_instance = PortainerAzureCredentials.from_json(json)
# print the JSON string representation of the object
print(PortainerAzureCredentials.to_json())

# convert the object into a dict
portainer_azure_credentials_dict = portainer_azure_credentials_instance.to_dict()
# create an instance of PortainerAzureCredentials from a dict
portainer_azure_credentials_from_dict = PortainerAzureCredentials.from_dict(portainer_azure_credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


