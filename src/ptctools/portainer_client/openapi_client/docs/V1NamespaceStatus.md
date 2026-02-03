# V1NamespaceStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conditions** | [**List[V1NamespaceCondition]**](V1NamespaceCondition.md) | Represents the latest available observations of a namespace&#39;s current state. +optional +patchMergeKey&#x3D;type +patchStrategy&#x3D;merge +listType&#x3D;map +listMapKey&#x3D;type | [optional] 
**phase** | [**V1NamespacePhase**](V1NamespacePhase.md) | Phase is the current lifecycle phase of the namespace. More info: https://kubernetes.io/docs/tasks/administer-cluster/namespaces/ +optional | [optional] 

## Example

```python
from openapi_client.models.v1_namespace_status import V1NamespaceStatus

# TODO update the JSON string below
json = "{}"
# create an instance of V1NamespaceStatus from a JSON string
v1_namespace_status_instance = V1NamespaceStatus.from_json(json)
# print the JSON string representation of the object
print(V1NamespaceStatus.to_json())

# convert the object into a dict
v1_namespace_status_dict = v1_namespace_status_instance.to_dict()
# create an instance of V1NamespaceStatus from a dict
v1_namespace_status_from_dict = V1NamespaceStatus.from_dict(v1_namespace_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


