# TemplatesFileResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_content** | **str** | The requested file content | [optional] 

## Example

```python
from openapi_client.models.templates_file_response import TemplatesFileResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TemplatesFileResponse from a JSON string
templates_file_response_instance = TemplatesFileResponse.from_json(json)
# print the JSON string representation of the object
print(TemplatesFileResponse.to_json())

# convert the object into a dict
templates_file_response_dict = templates_file_response_instance.to_dict()
# create an instance of TemplatesFileResponse from a dict
templates_file_response_from_dict = TemplatesFileResponse.from_dict(templates_file_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


