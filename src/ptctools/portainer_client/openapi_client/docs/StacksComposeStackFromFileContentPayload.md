# StacksComposeStackFromFileContentPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**env** | [**List[PortainerPair]**](PortainerPair.md) | A list of environment variables used during stack deployment | [optional] 
**from_app_template** | **bool** | Whether the stack is from a app template | [optional] 
**name** | **str** | Name of the stack | 
**stack_file_content** | **str** | Content of the Stack file | 

## Example

```python
from openapi_client.models.stacks_compose_stack_from_file_content_payload import StacksComposeStackFromFileContentPayload

# TODO update the JSON string below
json = "{}"
# create an instance of StacksComposeStackFromFileContentPayload from a JSON string
stacks_compose_stack_from_file_content_payload_instance = StacksComposeStackFromFileContentPayload.from_json(json)
# print the JSON string representation of the object
print(StacksComposeStackFromFileContentPayload.to_json())

# convert the object into a dict
stacks_compose_stack_from_file_content_payload_dict = stacks_compose_stack_from_file_content_payload_instance.to_dict()
# create an instance of StacksComposeStackFromFileContentPayload from a dict
stacks_compose_stack_from_file_content_payload_from_dict = StacksComposeStackFromFileContentPayload.from_dict(stacks_compose_stack_from_file_content_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


