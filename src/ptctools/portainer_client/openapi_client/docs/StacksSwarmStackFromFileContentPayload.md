# StacksSwarmStackFromFileContentPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**env** | [**List[PortainerPair]**](PortainerPair.md) | A list of environment variables used during stack deployment | [optional] 
**from_app_template** | **bool** | Whether the stack is from a app template | [optional] 
**name** | **str** | Name of the stack | 
**stack_file_content** | **str** | Content of the Stack file | 
**swarm_id** | **str** | Swarm cluster identifier | 

## Example

```python
from openapi_client.models.stacks_swarm_stack_from_file_content_payload import StacksSwarmStackFromFileContentPayload

# TODO update the JSON string below
json = "{}"
# create an instance of StacksSwarmStackFromFileContentPayload from a JSON string
stacks_swarm_stack_from_file_content_payload_instance = StacksSwarmStackFromFileContentPayload.from_json(json)
# print the JSON string representation of the object
print(StacksSwarmStackFromFileContentPayload.to_json())

# convert the object into a dict
stacks_swarm_stack_from_file_content_payload_dict = stacks_swarm_stack_from_file_content_payload_instance.to_dict()
# create an instance of StacksSwarmStackFromFileContentPayload from a dict
stacks_swarm_stack_from_file_content_payload_from_dict = StacksSwarmStackFromFileContentPayload.from_dict(stacks_swarm_stack_from_file_content_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


