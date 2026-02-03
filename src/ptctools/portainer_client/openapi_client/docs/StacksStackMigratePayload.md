# StacksStackMigratePayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoint_id** | **int** | Environment(Endpoint) identifier of the target environment(endpoint) where the stack will be relocated | 
**name** | **str** | If provided will rename the migrated stack | [optional] 
**swarm_id** | **str** | Swarm cluster identifier, must match the identifier of the cluster where the stack will be relocated | [optional] 

## Example

```python
from openapi_client.models.stacks_stack_migrate_payload import StacksStackMigratePayload

# TODO update the JSON string below
json = "{}"
# create an instance of StacksStackMigratePayload from a JSON string
stacks_stack_migrate_payload_instance = StacksStackMigratePayload.from_json(json)
# print the JSON string representation of the object
print(StacksStackMigratePayload.to_json())

# convert the object into a dict
stacks_stack_migrate_payload_dict = stacks_stack_migrate_payload_instance.to_dict()
# create an instance of StacksStackMigratePayload from a dict
stacks_stack_migrate_payload_from_dict = StacksStackMigratePayload.from_dict(stacks_stack_migrate_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


