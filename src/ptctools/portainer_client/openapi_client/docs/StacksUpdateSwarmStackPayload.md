# StacksUpdateSwarmStackPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**env** | [**List[PortainerPair]**](PortainerPair.md) | A list of environment(endpoint) variables used during stack deployment | [optional] 
**prune** | **bool** | Prune services that are no longer referenced (only available for Swarm stacks) | [optional] 
**pull_image** | **bool** | Force a pulling to current image with the original tag though the image is already the latest | [optional] 
**stack_file_content** | **str** | New content of the Stack file | [optional] 

## Example

```python
from openapi_client.models.stacks_update_swarm_stack_payload import StacksUpdateSwarmStackPayload

# TODO update the JSON string below
json = "{}"
# create an instance of StacksUpdateSwarmStackPayload from a JSON string
stacks_update_swarm_stack_payload_instance = StacksUpdateSwarmStackPayload.from_json(json)
# print the JSON string representation of the object
print(StacksUpdateSwarmStackPayload.to_json())

# convert the object into a dict
stacks_update_swarm_stack_payload_dict = stacks_update_swarm_stack_payload_instance.to_dict()
# create an instance of StacksUpdateSwarmStackPayload from a dict
stacks_update_swarm_stack_payload_from_dict = StacksUpdateSwarmStackPayload.from_dict(stacks_update_swarm_stack_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


