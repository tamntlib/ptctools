# KubernetesDescribeResourceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**describe** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.kubernetes_describe_resource_response import KubernetesDescribeResourceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesDescribeResourceResponse from a JSON string
kubernetes_describe_resource_response_instance = KubernetesDescribeResourceResponse.from_json(json)
# print the JSON string representation of the object
print(KubernetesDescribeResourceResponse.to_json())

# convert the object into a dict
kubernetes_describe_resource_response_dict = kubernetes_describe_resource_response_instance.to_dict()
# create an instance of KubernetesDescribeResourceResponse from a dict
kubernetes_describe_resource_response_from_dict = KubernetesDescribeResourceResponse.from_dict(kubernetes_describe_resource_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


