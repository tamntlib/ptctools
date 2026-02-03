# KubernetesMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotations** | **Dict[str, str]** |  | [optional] 
**labels** | **Dict[str, str]** |  | [optional] 

## Example

```python
from openapi_client.models.kubernetes_metadata import KubernetesMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesMetadata from a JSON string
kubernetes_metadata_instance = KubernetesMetadata.from_json(json)
# print the JSON string representation of the object
print(KubernetesMetadata.to_json())

# convert the object into a dict
kubernetes_metadata_dict = kubernetes_metadata_instance.to_dict()
# create an instance of KubernetesMetadata from a dict
kubernetes_metadata_from_dict = KubernetesMetadata.from_dict(kubernetes_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


