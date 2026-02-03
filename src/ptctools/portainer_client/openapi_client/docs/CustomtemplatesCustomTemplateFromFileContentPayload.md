# CustomtemplatesCustomTemplateFromFileContentPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of the template | 
**edge_template** | **bool** | EdgeTemplate indicates if this template purpose for Edge Stack | [optional] 
**file_content** | **str** | Content of stack file | 
**logo** | **str** | URL of the template&#39;s logo | [optional] 
**note** | **str** | A note that will be displayed in the UI. Supports HTML content | [optional] 
**platform** | [**PortainerCustomTemplatePlatform**](PortainerCustomTemplatePlatform.md) | Platform associated to the template. Valid values are: 1 - &#39;linux&#39;, 2 - &#39;windows&#39; Required for Docker stacks | [optional] 
**title** | **str** | Title of the template | 
**type** | [**PortainerStackType**](PortainerStackType.md) | Type of created stack: * 1 - swarm * 2 - compose * 3 - kubernetes | 
**variables** | [**List[PortainerCustomTemplateVariableDefinition]**](PortainerCustomTemplateVariableDefinition.md) | Definitions of variables in the stack file | [optional] 

## Example

```python
from openapi_client.models.customtemplates_custom_template_from_file_content_payload import CustomtemplatesCustomTemplateFromFileContentPayload

# TODO update the JSON string below
json = "{}"
# create an instance of CustomtemplatesCustomTemplateFromFileContentPayload from a JSON string
customtemplates_custom_template_from_file_content_payload_instance = CustomtemplatesCustomTemplateFromFileContentPayload.from_json(json)
# print the JSON string representation of the object
print(CustomtemplatesCustomTemplateFromFileContentPayload.to_json())

# convert the object into a dict
customtemplates_custom_template_from_file_content_payload_dict = customtemplates_custom_template_from_file_content_payload_instance.to_dict()
# create an instance of CustomtemplatesCustomTemplateFromFileContentPayload from a dict
customtemplates_custom_template_from_file_content_payload_from_dict = CustomtemplatesCustomTemplateFromFileContentPayload.from_dict(customtemplates_custom_template_from_file_content_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


