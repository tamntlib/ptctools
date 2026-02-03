# K8sIoApiRbacV1Subject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_group** | **str** | APIGroup holds the API group of the referenced subject. Defaults to \&quot;\&quot; for ServiceAccount subjects. Defaults to \&quot;rbac.authorization.k8s.io\&quot; for User and Group subjects. +optional | [optional] 
**kind** | **str** | Kind of object being referenced. Values defined by this API group are \&quot;User\&quot;, \&quot;Group\&quot;, and \&quot;ServiceAccount\&quot;. If the Authorizer does not recognized the kind value, the Authorizer should report an error. | [optional] 
**name** | **str** | Name of the object being referenced. | [optional] 
**namespace** | **str** | Namespace of the referenced object.  If the object kind is non-namespace, such as \&quot;User\&quot; or \&quot;Group\&quot;, and this value is not empty the Authorizer should report an error. +optional | [optional] 

## Example

```python
from openapi_client.models.k8s_io_api_rbac_v1_subject import K8sIoApiRbacV1Subject

# TODO update the JSON string below
json = "{}"
# create an instance of K8sIoApiRbacV1Subject from a JSON string
k8s_io_api_rbac_v1_subject_instance = K8sIoApiRbacV1Subject.from_json(json)
# print the JSON string representation of the object
print(K8sIoApiRbacV1Subject.to_json())

# convert the object into a dict
k8s_io_api_rbac_v1_subject_dict = k8s_io_api_rbac_v1_subject_instance.to_dict()
# create an instance of K8sIoApiRbacV1Subject from a dict
k8s_io_api_rbac_v1_subject_from_dict = K8sIoApiRbacV1Subject.from_dict(k8s_io_api_rbac_v1_subject_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


