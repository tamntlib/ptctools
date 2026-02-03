# KubernetesTLSInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hosts** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.kubernetes_tls_info import KubernetesTLSInfo

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesTLSInfo from a JSON string
kubernetes_tls_info_instance = KubernetesTLSInfo.from_json(json)
# print the JSON string representation of the object
print(KubernetesTLSInfo.to_json())

# convert the object into a dict
kubernetes_tls_info_dict = kubernetes_tls_info_instance.to_dict()
# create an instance of KubernetesTLSInfo from a dict
kubernetes_tls_info_from_dict = KubernetesTLSInfo.from_dict(kubernetes_tls_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


