# openapi_client.CustomTemplatesApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**custom_template_create_file**](CustomTemplatesApi.md#custom_template_create_file) | **POST** /custom_templates/create/file | Create a custom template
[**custom_template_create_repository**](CustomTemplatesApi.md#custom_template_create_repository) | **POST** /custom_templates/create/repository | Create a custom template
[**custom_template_create_string**](CustomTemplatesApi.md#custom_template_create_string) | **POST** /custom_templates/create/string | Create a custom template
[**custom_template_delete**](CustomTemplatesApi.md#custom_template_delete) | **DELETE** /custom_templates/{id} | Remove a template
[**custom_template_file**](CustomTemplatesApi.md#custom_template_file) | **GET** /custom_templates/{id}/file | Get Template stack file content.
[**custom_template_git_fetch**](CustomTemplatesApi.md#custom_template_git_fetch) | **PUT** /custom_templates/{id}/git_fetch | Fetch the latest config file content based on custom template&#39;s git repository configuration
[**custom_template_inspect**](CustomTemplatesApi.md#custom_template_inspect) | **GET** /custom_templates/{id} | Inspect a custom template
[**custom_template_list**](CustomTemplatesApi.md#custom_template_list) | **GET** /custom_templates | List available custom templates
[**custom_template_update**](CustomTemplatesApi.md#custom_template_update) | **PUT** /custom_templates/{id} | Update a template


# **custom_template_create_file**
> PortainerCustomTemplate custom_template_create_file(title, description, note, platform, type, file, logo=logo, variables=variables)

Create a custom template

Create a custom template.
**Access policy**: authenticated

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.portainer_custom_template import PortainerCustomTemplate
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: jwt
configuration.api_key['jwt'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['jwt'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CustomTemplatesApi(api_client)
    title = 'title_example' # str | Title of the template
    description = 'description_example' # str | Description of the template
    note = 'note_example' # str | A note that will be displayed in the UI. Supports HTML content
    platform = 56 # int | Platform associated to the template (1 - 'linux', 2 - 'windows')
    type = 56 # int | Type of created stack (1 - swarm, 2 - compose, 3 - kubernetes)
    file = None # bytearray | File
    logo = 'logo_example' # str | URL of the template's logo (optional)
    variables = 'variables_example' # str | A json array of variables definitions (optional)

    try:
        # Create a custom template
        api_response = api_instance.custom_template_create_file(title, description, note, platform, type, file, logo=logo, variables=variables)
        print("The response of CustomTemplatesApi->custom_template_create_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomTemplatesApi->custom_template_create_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **title** | **str**| Title of the template | 
 **description** | **str**| Description of the template | 
 **note** | **str**| A note that will be displayed in the UI. Supports HTML content | 
 **platform** | **int**| Platform associated to the template (1 - &#39;linux&#39;, 2 - &#39;windows&#39;) | 
 **type** | **int**| Type of created stack (1 - swarm, 2 - compose, 3 - kubernetes) | 
 **file** | **bytearray**| File | 
 **logo** | **str**| URL of the template&#39;s logo | [optional] 
 **variables** | **str**| A json array of variables definitions | [optional] 

### Return type

[**PortainerCustomTemplate**](PortainerCustomTemplate.md)

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Invalid request |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_template_create_repository**
> PortainerCustomTemplate custom_template_create_repository(body)

Create a custom template

Create a custom template.
**Access policy**: authenticated

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.customtemplates_custom_template_from_git_repository_payload import CustomtemplatesCustomTemplateFromGitRepositoryPayload
from openapi_client.models.portainer_custom_template import PortainerCustomTemplate
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: jwt
configuration.api_key['jwt'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['jwt'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CustomTemplatesApi(api_client)
    body = openapi_client.CustomtemplatesCustomTemplateFromGitRepositoryPayload() # CustomtemplatesCustomTemplateFromGitRepositoryPayload | Required when using method=repository

    try:
        # Create a custom template
        api_response = api_instance.custom_template_create_repository(body)
        print("The response of CustomTemplatesApi->custom_template_create_repository:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomTemplatesApi->custom_template_create_repository: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CustomtemplatesCustomTemplateFromGitRepositoryPayload**](CustomtemplatesCustomTemplateFromGitRepositoryPayload.md)| Required when using method&#x3D;repository | 

### Return type

[**PortainerCustomTemplate**](PortainerCustomTemplate.md)

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Invalid request |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_template_create_string**
> PortainerCustomTemplate custom_template_create_string(body)

Create a custom template

Create a custom template.
**Access policy**: authenticated

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.customtemplates_custom_template_from_file_content_payload import CustomtemplatesCustomTemplateFromFileContentPayload
from openapi_client.models.portainer_custom_template import PortainerCustomTemplate
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: jwt
configuration.api_key['jwt'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['jwt'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CustomTemplatesApi(api_client)
    body = openapi_client.CustomtemplatesCustomTemplateFromFileContentPayload() # CustomtemplatesCustomTemplateFromFileContentPayload | body

    try:
        # Create a custom template
        api_response = api_instance.custom_template_create_string(body)
        print("The response of CustomTemplatesApi->custom_template_create_string:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomTemplatesApi->custom_template_create_string: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CustomtemplatesCustomTemplateFromFileContentPayload**](CustomtemplatesCustomTemplateFromFileContentPayload.md)| body | 

### Return type

[**PortainerCustomTemplate**](PortainerCustomTemplate.md)

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Invalid request |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_template_delete**
> custom_template_delete(id)

Remove a template

Remove a template.
**Access policy**: authenticated

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: jwt
configuration.api_key['jwt'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['jwt'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CustomTemplatesApi(api_client)
    id = 56 # int | Template identifier

    try:
        # Remove a template
        api_instance.custom_template_delete(id)
    except Exception as e:
        print("Exception when calling CustomTemplatesApi->custom_template_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Template identifier | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success |  -  |
**400** | Invalid request |  -  |
**403** | Access denied to resource |  -  |
**404** | Template not found |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_template_file**
> CustomtemplatesFileResponse custom_template_file(id)

Get Template stack file content.

Retrieve the content of the Stack file for the specified custom template
**Access policy**: authenticated

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.customtemplates_file_response import CustomtemplatesFileResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: jwt
configuration.api_key['jwt'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['jwt'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CustomTemplatesApi(api_client)
    id = 56 # int | Template identifier

    try:
        # Get Template stack file content.
        api_response = api_instance.custom_template_file(id)
        print("The response of CustomTemplatesApi->custom_template_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomTemplatesApi->custom_template_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Template identifier | 

### Return type

[**CustomtemplatesFileResponse**](CustomtemplatesFileResponse.md)

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid request |  -  |
**404** | Custom template not found |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_template_git_fetch**
> CustomtemplatesFileResponse custom_template_git_fetch(id)

Fetch the latest config file content based on custom template's git repository configuration

Retrieve details about a template created from git repository method.
**Access policy**: authenticated

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.customtemplates_file_response import CustomtemplatesFileResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: jwt
configuration.api_key['jwt'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['jwt'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CustomTemplatesApi(api_client)
    id = 56 # int | Template identifier

    try:
        # Fetch the latest config file content based on custom template's git repository configuration
        api_response = api_instance.custom_template_git_fetch(id)
        print("The response of CustomTemplatesApi->custom_template_git_fetch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomTemplatesApi->custom_template_git_fetch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Template identifier | 

### Return type

[**CustomtemplatesFileResponse**](CustomtemplatesFileResponse.md)

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid request |  -  |
**404** | Custom template not found |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_template_inspect**
> PortainerCustomTemplate custom_template_inspect(id)

Inspect a custom template

Retrieve details about a template.
**Access policy**: authenticated

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.portainer_custom_template import PortainerCustomTemplate
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: jwt
configuration.api_key['jwt'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['jwt'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CustomTemplatesApi(api_client)
    id = 56 # int | Template identifier

    try:
        # Inspect a custom template
        api_response = api_instance.custom_template_inspect(id)
        print("The response of CustomTemplatesApi->custom_template_inspect:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomTemplatesApi->custom_template_inspect: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Template identifier | 

### Return type

[**PortainerCustomTemplate**](PortainerCustomTemplate.md)

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid request |  -  |
**404** | Template not found |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_template_list**
> List[PortainerCustomTemplate] custom_template_list(type, edge=edge)

List available custom templates

List available custom templates.
**Access policy**: authenticated

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.portainer_custom_template import PortainerCustomTemplate
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: jwt
configuration.api_key['jwt'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['jwt'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CustomTemplatesApi(api_client)
    type = [56] # List[int] | Template types
    edge = True # bool | Filter by edge templates (optional)

    try:
        # List available custom templates
        api_response = api_instance.custom_template_list(type, edge=edge)
        print("The response of CustomTemplatesApi->custom_template_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomTemplatesApi->custom_template_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | [**List[int]**](int.md)| Template types | 
 **edge** | **bool**| Filter by edge templates | [optional] 

### Return type

[**List[PortainerCustomTemplate]**](PortainerCustomTemplate.md)

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_template_update**
> PortainerCustomTemplate custom_template_update(id, body)

Update a template

Update a template.
**Access policy**: authenticated

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.customtemplates_custom_template_update_payload import CustomtemplatesCustomTemplateUpdatePayload
from openapi_client.models.portainer_custom_template import PortainerCustomTemplate
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: jwt
configuration.api_key['jwt'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['jwt'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CustomTemplatesApi(api_client)
    id = 56 # int | Template identifier
    body = openapi_client.CustomtemplatesCustomTemplateUpdatePayload() # CustomtemplatesCustomTemplateUpdatePayload | Template details

    try:
        # Update a template
        api_response = api_instance.custom_template_update(id, body)
        print("The response of CustomTemplatesApi->custom_template_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomTemplatesApi->custom_template_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Template identifier | 
 **body** | [**CustomtemplatesCustomTemplateUpdatePayload**](CustomtemplatesCustomTemplateUpdatePayload.md)| Template details | 

### Return type

[**PortainerCustomTemplate**](PortainerCustomTemplate.md)

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid request |  -  |
**403** | Permission denied to access template |  -  |
**404** | Template not found |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

