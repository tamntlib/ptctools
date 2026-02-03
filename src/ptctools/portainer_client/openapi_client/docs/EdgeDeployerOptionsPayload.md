# EdgeDeployerOptionsPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prune** | **bool** | Prune is a flag indicating if the agent must prune the containers or not when creating/updating an edge stack This flag drives &#x60;docker compose up --remove-orphans&#x60; and &#x60;docker stack up --prune&#x60; options Used only for EE | [optional] 
**remove_volumes** | **bool** | RemoveVolumes is a flag indicating if the agent must remove the named volumes declared in the compose file and anonymouse volumes attached to containers This flag drives &#x60;docker compose down --volumes&#x60; option Used only for EE | [optional] 

## Example

```python
from openapi_client.models.edge_deployer_options_payload import EdgeDeployerOptionsPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EdgeDeployerOptionsPayload from a JSON string
edge_deployer_options_payload_instance = EdgeDeployerOptionsPayload.from_json(json)
# print the JSON string representation of the object
print(EdgeDeployerOptionsPayload.to_json())

# convert the object into a dict
edge_deployer_options_payload_dict = edge_deployer_options_payload_instance.to_dict()
# create an instance of EdgeDeployerOptionsPayload from a dict
edge_deployer_options_payload_from_dict = EdgeDeployerOptionsPayload.from_dict(edge_deployer_options_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


