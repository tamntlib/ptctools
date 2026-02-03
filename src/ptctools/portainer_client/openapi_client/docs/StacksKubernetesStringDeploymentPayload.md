# StacksKubernetesStringDeploymentPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**compose_format** | **bool** |  | [optional] 
**from_app_template** | **bool** | Whether the stack is from a app template | [optional] 
**namespace** | **str** |  | [optional] 
**stack_file_content** | **str** |  | [optional] 
**stack_name** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.stacks_kubernetes_string_deployment_payload import StacksKubernetesStringDeploymentPayload

# TODO update the JSON string below
json = "{}"
# create an instance of StacksKubernetesStringDeploymentPayload from a JSON string
stacks_kubernetes_string_deployment_payload_instance = StacksKubernetesStringDeploymentPayload.from_json(json)
# print the JSON string representation of the object
print(StacksKubernetesStringDeploymentPayload.to_json())

# convert the object into a dict
stacks_kubernetes_string_deployment_payload_dict = stacks_kubernetes_string_deployment_payload_instance.to_dict()
# create an instance of StacksKubernetesStringDeploymentPayload from a dict
stacks_kubernetes_string_deployment_payload_from_dict = StacksKubernetesStringDeploymentPayload.from_dict(stacks_kubernetes_string_deployment_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


