# KubernetesCustomResourceMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** |  | [optional] 
**kind** | **str** |  | [optional] 
**plural** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.kubernetes_custom_resource_metadata import KubernetesCustomResourceMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesCustomResourceMetadata from a JSON string
kubernetes_custom_resource_metadata_instance = KubernetesCustomResourceMetadata.from_json(json)
# print the JSON string representation of the object
print(KubernetesCustomResourceMetadata.to_json())

# convert the object into a dict
kubernetes_custom_resource_metadata_dict = kubernetes_custom_resource_metadata_instance.to_dict()
# create an instance of KubernetesCustomResourceMetadata from a dict
kubernetes_custom_resource_metadata_from_dict = KubernetesCustomResourceMetadata.from_dict(kubernetes_custom_resource_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


