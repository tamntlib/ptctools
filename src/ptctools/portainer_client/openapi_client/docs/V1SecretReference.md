# V1SecretReference


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | name is unique within a namespace to reference a secret resource. +optional | [optional] 
**namespace** | **str** | namespace defines the space within which the secret name must be unique. +optional | [optional] 

## Example

```python
from openapi_client.models.v1_secret_reference import V1SecretReference

# TODO update the JSON string below
json = "{}"
# create an instance of V1SecretReference from a JSON string
v1_secret_reference_instance = V1SecretReference.from_json(json)
# print the JSON string representation of the object
print(V1SecretReference.to_json())

# convert the object into a dict
v1_secret_reference_dict = v1_secret_reference_instance.to_dict()
# create an instance of V1SecretReference from a dict
v1_secret_reference_from_dict = V1SecretReference.from_dict(v1_secret_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


