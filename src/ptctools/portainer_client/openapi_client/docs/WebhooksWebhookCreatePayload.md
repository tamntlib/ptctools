# WebhooksWebhookCreatePayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoint_id** | **int** |  | [optional] 
**registry_id** | **int** |  | [optional] 
**resource_id** | **str** |  | [optional] 
**webhook_type** | [**PortainerWebhookType**](PortainerWebhookType.md) | Type of webhook (1 - service) | [optional] 

## Example

```python
from openapi_client.models.webhooks_webhook_create_payload import WebhooksWebhookCreatePayload

# TODO update the JSON string below
json = "{}"
# create an instance of WebhooksWebhookCreatePayload from a JSON string
webhooks_webhook_create_payload_instance = WebhooksWebhookCreatePayload.from_json(json)
# print the JSON string representation of the object
print(WebhooksWebhookCreatePayload.to_json())

# convert the object into a dict
webhooks_webhook_create_payload_dict = webhooks_webhook_create_payload_instance.to_dict()
# create an instance of WebhooksWebhookCreatePayload from a dict
webhooks_webhook_create_payload_from_dict = WebhooksWebhookCreatePayload.from_dict(webhooks_webhook_create_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


