# StacksKubernetesManifestURLDeploymentPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**compose_format** | **bool** |  | [optional] 
**manifest_url** | **str** |  | [optional] 
**namespace** | **str** |  | [optional] 
**stack_name** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.stacks_kubernetes_manifest_url_deployment_payload import StacksKubernetesManifestURLDeploymentPayload

# TODO update the JSON string below
json = "{}"
# create an instance of StacksKubernetesManifestURLDeploymentPayload from a JSON string
stacks_kubernetes_manifest_url_deployment_payload_instance = StacksKubernetesManifestURLDeploymentPayload.from_json(json)
# print the JSON string representation of the object
print(StacksKubernetesManifestURLDeploymentPayload.to_json())

# convert the object into a dict
stacks_kubernetes_manifest_url_deployment_payload_dict = stacks_kubernetes_manifest_url_deployment_payload_instance.to_dict()
# create an instance of StacksKubernetesManifestURLDeploymentPayload from a dict
stacks_kubernetes_manifest_url_deployment_payload_from_dict = StacksKubernetesManifestURLDeploymentPayload.from_dict(stacks_kubernetes_manifest_url_deployment_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


