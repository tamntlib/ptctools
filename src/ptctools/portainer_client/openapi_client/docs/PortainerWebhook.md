# PortainerWebhook


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoint_id** | **int** |  | [optional] 
**id** | **int** | Webhook Identifier | [optional] 
**registry_id** | **int** |  | [optional] 
**resource_id** | **str** |  | [optional] 
**token** | **str** |  | [optional] 
**type** | [**PortainerWebhookType**](PortainerWebhookType.md) | Type of webhook (1 - service) | [optional] 

## Example

```python
from openapi_client.models.portainer_webhook import PortainerWebhook

# TODO update the JSON string below
json = "{}"
# create an instance of PortainerWebhook from a JSON string
portainer_webhook_instance = PortainerWebhook.from_json(json)
# print the JSON string representation of the object
print(PortainerWebhook.to_json())

# convert the object into a dict
portainer_webhook_dict = portainer_webhook_instance.to_dict()
# create an instance of PortainerWebhook from a dict
portainer_webhook_from_dict = PortainerWebhook.from_dict(portainer_webhook_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


