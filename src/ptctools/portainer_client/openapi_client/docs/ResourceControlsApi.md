# openapi_client.ResourceControlsApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**resource_control_create**](ResourceControlsApi.md#resource_control_create) | **POST** /resource_controls | Create a new resource control
[**resource_control_delete**](ResourceControlsApi.md#resource_control_delete) | **DELETE** /resource_controls/{id} | Remove a resource control
[**resource_control_update**](ResourceControlsApi.md#resource_control_update) | **PUT** /resource_controls/{id} | Update a resource control


# **resource_control_create**
> PortainerResourceControl resource_control_create(body)

Create a new resource control

Create a new resource control to restrict access to a Docker resource.
**Access policy**: administrator

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.portainer_resource_control import PortainerResourceControl
from openapi_client.models.resourcecontrols_resource_control_create_payload import ResourcecontrolsResourceControlCreatePayload
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
    api_instance = openapi_client.ResourceControlsApi(api_client)
    body = openapi_client.ResourcecontrolsResourceControlCreatePayload() # ResourcecontrolsResourceControlCreatePayload | Resource control details

    try:
        # Create a new resource control
        api_response = api_instance.resource_control_create(body)
        print("The response of ResourceControlsApi->resource_control_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceControlsApi->resource_control_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ResourcecontrolsResourceControlCreatePayload**](ResourcecontrolsResourceControlCreatePayload.md)| Resource control details | 

### Return type

[**PortainerResourceControl**](PortainerResourceControl.md)

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
**409** | A resource control is already associated to this resource |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_control_delete**
> resource_control_delete(id)

Remove a resource control

Remove a resource control.
**Access policy**: administrator

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
    api_instance = openapi_client.ResourceControlsApi(api_client)
    id = 56 # int | Resource control identifier

    try:
        # Remove a resource control
        api_instance.resource_control_delete(id)
    except Exception as e:
        print("Exception when calling ResourceControlsApi->resource_control_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Resource control identifier | 

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
**404** | Resource control not found |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_control_update**
> PortainerResourceControl resource_control_update(id, body)

Update a resource control

Update a resource control
**Access policy**: authenticated

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.portainer_resource_control import PortainerResourceControl
from openapi_client.models.resourcecontrols_resource_control_update_payload import ResourcecontrolsResourceControlUpdatePayload
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
    api_instance = openapi_client.ResourceControlsApi(api_client)
    id = 56 # int | Resource control identifier
    body = openapi_client.ResourcecontrolsResourceControlUpdatePayload() # ResourcecontrolsResourceControlUpdatePayload | Resource control details

    try:
        # Update a resource control
        api_response = api_instance.resource_control_update(id, body)
        print("The response of ResourceControlsApi->resource_control_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceControlsApi->resource_control_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Resource control identifier | 
 **body** | [**ResourcecontrolsResourceControlUpdatePayload**](ResourcecontrolsResourceControlUpdatePayload.md)| Resource control details | 

### Return type

[**PortainerResourceControl**](PortainerResourceControl.md)

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
**403** | Unauthorized |  -  |
**404** | Resource control not found |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

