# openapi_client.StacksApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**stack_associate**](StacksApi.md#stack_associate) | **PUT** /stacks/{id}/associate | Associate an orphaned stack to a new environment(endpoint)
[**stack_create_docker_standalone_file**](StacksApi.md#stack_create_docker_standalone_file) | **POST** /stacks/create/standalone/file | Deploy a new compose stack from a file
[**stack_create_docker_standalone_repository**](StacksApi.md#stack_create_docker_standalone_repository) | **POST** /stacks/create/standalone/repository | Deploy a new compose stack from repository
[**stack_create_docker_standalone_string**](StacksApi.md#stack_create_docker_standalone_string) | **POST** /stacks/create/standalone/string | Deploy a new compose stack from a text
[**stack_create_docker_swarm_file**](StacksApi.md#stack_create_docker_swarm_file) | **POST** /stacks/create/swarm/file | Deploy a new swarm stack from a file
[**stack_create_docker_swarm_repository**](StacksApi.md#stack_create_docker_swarm_repository) | **POST** /stacks/create/swarm/repository | Deploy a new swarm stack from a git repository
[**stack_create_docker_swarm_string**](StacksApi.md#stack_create_docker_swarm_string) | **POST** /stacks/create/swarm/string | Deploy a new swarm stack from a text
[**stack_create_kubernetes_file**](StacksApi.md#stack_create_kubernetes_file) | **POST** /stacks/create/kubernetes/string | Deploy a new kubernetes stack from a file
[**stack_create_kubernetes_git**](StacksApi.md#stack_create_kubernetes_git) | **POST** /stacks/create/kubernetes/repository | Deploy a new kubernetes stack from a git repository
[**stack_create_kubernetes_url**](StacksApi.md#stack_create_kubernetes_url) | **POST** /stacks/create/kubernetes/url | Deploy a new kubernetes stack from a url
[**stack_delete**](StacksApi.md#stack_delete) | **DELETE** /stacks/{id} | Remove a stack
[**stack_delete_kubernetes_by_name**](StacksApi.md#stack_delete_kubernetes_by_name) | **DELETE** /stacks/name/{name} | Remove Kubernetes stacks by name
[**stack_file_inspect**](StacksApi.md#stack_file_inspect) | **GET** /stacks/{id}/file | Retrieve the content of the Stack file for the specified stack
[**stack_git_redeploy**](StacksApi.md#stack_git_redeploy) | **PUT** /stacks/{id}/git/redeploy | Redeploy a stack
[**stack_inspect**](StacksApi.md#stack_inspect) | **GET** /stacks/{id} | Inspect a stack
[**stack_list**](StacksApi.md#stack_list) | **GET** /stacks | List stacks
[**stack_migrate**](StacksApi.md#stack_migrate) | **POST** /stacks/{id}/migrate | Migrate a stack to another environment(endpoint)
[**stack_start**](StacksApi.md#stack_start) | **POST** /stacks/{id}/start | Starts a stopped Stack
[**stack_stop**](StacksApi.md#stack_stop) | **POST** /stacks/{id}/stop | Stops a stopped Stack
[**stack_update**](StacksApi.md#stack_update) | **PUT** /stacks/{id} | Update a stack
[**stack_update_git**](StacksApi.md#stack_update_git) | **POST** /stacks/{id}/git | Update a stack&#39;s Git configs
[**webhook_invoke**](StacksApi.md#webhook_invoke) | **POST** /stacks/webhooks/{webhookID} | Webhook for triggering stack updates from git


# **stack_associate**
> PortainerStack stack_associate(id, endpoint_id, swarm_id, orphaned_running)

Associate an orphaned stack to a new environment(endpoint)

**Access policy**: administrator

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.portainer_stack import PortainerStack
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
    api_instance = openapi_client.StacksApi(api_client)
    id = 56 # int | Stack identifier
    endpoint_id = 56 # int | Environment identifier
    swarm_id = 56 # int | Swarm identifier
    orphaned_running = True # bool | Indicates whether the stack is orphaned

    try:
        # Associate an orphaned stack to a new environment(endpoint)
        api_response = api_instance.stack_associate(id, endpoint_id, swarm_id, orphaned_running)
        print("The response of StacksApi->stack_associate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StacksApi->stack_associate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Stack identifier | 
 **endpoint_id** | **int**| Environment identifier | 
 **swarm_id** | **int**| Swarm identifier | 
 **orphaned_running** | **bool**| Indicates whether the stack is orphaned | 

### Return type

[**PortainerStack**](PortainerStack.md)

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
**403** | Permission denied |  -  |
**404** | Stack not found |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stack_create_docker_standalone_file**
> PortainerStack stack_create_docker_standalone_file(endpoint_id, name, env=env, file=file)

Deploy a new compose stack from a file

Deploy a new stack into a Docker environment specified via the environment identifier.
**Access policy**: authenticated

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.portainer_stack import PortainerStack
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
    api_instance = openapi_client.StacksApi(api_client)
    endpoint_id = 56 # int | Identifier of the environment that will be used to deploy the stack
    name = 'name_example' # str | Name of the stack
    env = 'env_example' # str | Environment variables passed during deployment, represented as a JSON array [{'name': 'name', 'value': 'value'}]. (optional)
    file = None # bytearray | Stack file (optional)

    try:
        # Deploy a new compose stack from a file
        api_response = api_instance.stack_create_docker_standalone_file(endpoint_id, name, env=env, file=file)
        print("The response of StacksApi->stack_create_docker_standalone_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StacksApi->stack_create_docker_standalone_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint_id** | **int**| Identifier of the environment that will be used to deploy the stack | 
 **name** | **str**| Name of the stack | 
 **env** | **str**| Environment variables passed during deployment, represented as a JSON array [{&#39;name&#39;: &#39;name&#39;, &#39;value&#39;: &#39;value&#39;}]. | [optional] 
 **file** | **bytearray**| Stack file | [optional] 

### Return type

[**PortainerStack**](PortainerStack.md)

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

# **stack_create_docker_standalone_repository**
> PortainerStack stack_create_docker_standalone_repository(endpoint_id, body)

Deploy a new compose stack from repository

Deploy a new stack into a Docker environment specified via the environment identifier.
**Access policy**: authenticated

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.portainer_stack import PortainerStack
from openapi_client.models.stacks_compose_stack_from_git_repository_payload import StacksComposeStackFromGitRepositoryPayload
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
    api_instance = openapi_client.StacksApi(api_client)
    endpoint_id = 56 # int | Identifier of the environment that will be used to deploy the stack
    body = openapi_client.StacksComposeStackFromGitRepositoryPayload() # StacksComposeStackFromGitRepositoryPayload | stack config

    try:
        # Deploy a new compose stack from repository
        api_response = api_instance.stack_create_docker_standalone_repository(endpoint_id, body)
        print("The response of StacksApi->stack_create_docker_standalone_repository:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StacksApi->stack_create_docker_standalone_repository: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint_id** | **int**| Identifier of the environment that will be used to deploy the stack | 
 **body** | [**StacksComposeStackFromGitRepositoryPayload**](StacksComposeStackFromGitRepositoryPayload.md)| stack config | 

### Return type

[**PortainerStack**](PortainerStack.md)

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
**409** | Stack name or webhook ID already exists |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stack_create_docker_standalone_string**
> PortainerStack stack_create_docker_standalone_string(endpoint_id, body)

Deploy a new compose stack from a text

Deploy a new stack into a Docker environment specified via the environment identifier.
**Access policy**: authenticated

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.portainer_stack import PortainerStack
from openapi_client.models.stacks_compose_stack_from_file_content_payload import StacksComposeStackFromFileContentPayload
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
    api_instance = openapi_client.StacksApi(api_client)
    endpoint_id = 56 # int | Identifier of the environment that will be used to deploy the stack
    body = openapi_client.StacksComposeStackFromFileContentPayload() # StacksComposeStackFromFileContentPayload | stack config

    try:
        # Deploy a new compose stack from a text
        api_response = api_instance.stack_create_docker_standalone_string(endpoint_id, body)
        print("The response of StacksApi->stack_create_docker_standalone_string:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StacksApi->stack_create_docker_standalone_string: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint_id** | **int**| Identifier of the environment that will be used to deploy the stack | 
 **body** | [**StacksComposeStackFromFileContentPayload**](StacksComposeStackFromFileContentPayload.md)| stack config | 

### Return type

[**PortainerStack**](PortainerStack.md)

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

# **stack_create_docker_swarm_file**
> PortainerStack stack_create_docker_swarm_file(endpoint_id, name=name, swarm_id=swarm_id, env=env, file=file)

Deploy a new swarm stack from a file

Deploy a new stack into a Docker environment specified via the environment identifier.
**Access policy**: authenticated

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.portainer_stack import PortainerStack
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
    api_instance = openapi_client.StacksApi(api_client)
    endpoint_id = 56 # int | Identifier of the environment that will be used to deploy the stack
    name = 'name_example' # str | Name of the stack (optional)
    swarm_id = 'swarm_id_example' # str | Swarm cluster identifier. (optional)
    env = 'env_example' # str | Environment variables passed during deployment, represented as a JSON array [{'name': 'name', 'value': 'value'}]. Optional (optional)
    file = None # bytearray | Stack file (optional)

    try:
        # Deploy a new swarm stack from a file
        api_response = api_instance.stack_create_docker_swarm_file(endpoint_id, name=name, swarm_id=swarm_id, env=env, file=file)
        print("The response of StacksApi->stack_create_docker_swarm_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StacksApi->stack_create_docker_swarm_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint_id** | **int**| Identifier of the environment that will be used to deploy the stack | 
 **name** | **str**| Name of the stack | [optional] 
 **swarm_id** | **str**| Swarm cluster identifier. | [optional] 
 **env** | **str**| Environment variables passed during deployment, represented as a JSON array [{&#39;name&#39;: &#39;name&#39;, &#39;value&#39;: &#39;value&#39;}]. Optional | [optional] 
 **file** | **bytearray**| Stack file | [optional] 

### Return type

[**PortainerStack**](PortainerStack.md)

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

# **stack_create_docker_swarm_repository**
> PortainerStack stack_create_docker_swarm_repository(endpoint_id, body)

Deploy a new swarm stack from a git repository

Deploy a new stack into a Docker environment specified via the environment identifier.
**Access policy**: authenticated

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.portainer_stack import PortainerStack
from openapi_client.models.stacks_swarm_stack_from_git_repository_payload import StacksSwarmStackFromGitRepositoryPayload
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
    api_instance = openapi_client.StacksApi(api_client)
    endpoint_id = 56 # int | Identifier of the environment that will be used to deploy the stack
    body = openapi_client.StacksSwarmStackFromGitRepositoryPayload() # StacksSwarmStackFromGitRepositoryPayload | stack config

    try:
        # Deploy a new swarm stack from a git repository
        api_response = api_instance.stack_create_docker_swarm_repository(endpoint_id, body)
        print("The response of StacksApi->stack_create_docker_swarm_repository:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StacksApi->stack_create_docker_swarm_repository: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint_id** | **int**| Identifier of the environment that will be used to deploy the stack | 
 **body** | [**StacksSwarmStackFromGitRepositoryPayload**](StacksSwarmStackFromGitRepositoryPayload.md)| stack config | 

### Return type

[**PortainerStack**](PortainerStack.md)

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
**409** | Stack name or webhook ID already exists |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stack_create_docker_swarm_string**
> PortainerStack stack_create_docker_swarm_string(endpoint_id, body)

Deploy a new swarm stack from a text

Deploy a new stack into a Docker environment specified via the environment identifier.
**Access policy**: authenticated

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.portainer_stack import PortainerStack
from openapi_client.models.stacks_swarm_stack_from_file_content_payload import StacksSwarmStackFromFileContentPayload
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
    api_instance = openapi_client.StacksApi(api_client)
    endpoint_id = 56 # int | Identifier of the environment that will be used to deploy the stack
    body = openapi_client.StacksSwarmStackFromFileContentPayload() # StacksSwarmStackFromFileContentPayload | stack config

    try:
        # Deploy a new swarm stack from a text
        api_response = api_instance.stack_create_docker_swarm_string(endpoint_id, body)
        print("The response of StacksApi->stack_create_docker_swarm_string:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StacksApi->stack_create_docker_swarm_string: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint_id** | **int**| Identifier of the environment that will be used to deploy the stack | 
 **body** | [**StacksSwarmStackFromFileContentPayload**](StacksSwarmStackFromFileContentPayload.md)| stack config | 

### Return type

[**PortainerStack**](PortainerStack.md)

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

# **stack_create_kubernetes_file**
> PortainerStack stack_create_kubernetes_file(endpoint_id, body)

Deploy a new kubernetes stack from a file

Deploy a new stack into a Docker environment specified via the environment identifier.
**Access policy**: authenticated

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.portainer_stack import PortainerStack
from openapi_client.models.stacks_kubernetes_string_deployment_payload import StacksKubernetesStringDeploymentPayload
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
    api_instance = openapi_client.StacksApi(api_client)
    endpoint_id = 56 # int | Identifier of the environment that will be used to deploy the stack
    body = openapi_client.StacksKubernetesStringDeploymentPayload() # StacksKubernetesStringDeploymentPayload | stack config

    try:
        # Deploy a new kubernetes stack from a file
        api_response = api_instance.stack_create_kubernetes_file(endpoint_id, body)
        print("The response of StacksApi->stack_create_kubernetes_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StacksApi->stack_create_kubernetes_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint_id** | **int**| Identifier of the environment that will be used to deploy the stack | 
 **body** | [**StacksKubernetesStringDeploymentPayload**](StacksKubernetesStringDeploymentPayload.md)| stack config | 

### Return type

[**PortainerStack**](PortainerStack.md)

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Invalid request |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stack_create_kubernetes_git**
> PortainerStack stack_create_kubernetes_git(endpoint_id, body)

Deploy a new kubernetes stack from a git repository

Deploy a new stack into a Docker environment specified via the environment identifier.
**Access policy**: authenticated

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.portainer_stack import PortainerStack
from openapi_client.models.stacks_kubernetes_git_deployment_payload import StacksKubernetesGitDeploymentPayload
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
    api_instance = openapi_client.StacksApi(api_client)
    endpoint_id = 56 # int | Identifier of the environment that will be used to deploy the stack
    body = openapi_client.StacksKubernetesGitDeploymentPayload() # StacksKubernetesGitDeploymentPayload | stack config

    try:
        # Deploy a new kubernetes stack from a git repository
        api_response = api_instance.stack_create_kubernetes_git(endpoint_id, body)
        print("The response of StacksApi->stack_create_kubernetes_git:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StacksApi->stack_create_kubernetes_git: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint_id** | **int**| Identifier of the environment that will be used to deploy the stack | 
 **body** | [**StacksKubernetesGitDeploymentPayload**](StacksKubernetesGitDeploymentPayload.md)| stack config | 

### Return type

[**PortainerStack**](PortainerStack.md)

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Invalid request |  -  |
**409** | Stack name or webhook ID already exists |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stack_create_kubernetes_url**
> PortainerStack stack_create_kubernetes_url(endpoint_id, body)

Deploy a new kubernetes stack from a url

Deploy a new stack into a Docker environment specified via the environment identifier.
**Access policy**: authenticated

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.portainer_stack import PortainerStack
from openapi_client.models.stacks_kubernetes_manifest_url_deployment_payload import StacksKubernetesManifestURLDeploymentPayload
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
    api_instance = openapi_client.StacksApi(api_client)
    endpoint_id = 56 # int | Identifier of the environment that will be used to deploy the stack
    body = openapi_client.StacksKubernetesManifestURLDeploymentPayload() # StacksKubernetesManifestURLDeploymentPayload | stack config

    try:
        # Deploy a new kubernetes stack from a url
        api_response = api_instance.stack_create_kubernetes_url(endpoint_id, body)
        print("The response of StacksApi->stack_create_kubernetes_url:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StacksApi->stack_create_kubernetes_url: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint_id** | **int**| Identifier of the environment that will be used to deploy the stack | 
 **body** | [**StacksKubernetesManifestURLDeploymentPayload**](StacksKubernetesManifestURLDeploymentPayload.md)| stack config | 

### Return type

[**PortainerStack**](PortainerStack.md)

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Invalid request |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stack_delete**
> stack_delete(id, endpoint_id, external=external)

Remove a stack

Remove a stack.
**Access policy**: restricted

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
    api_instance = openapi_client.StacksApi(api_client)
    id = 56 # int | Stack identifier
    endpoint_id = 56 # int | Environment identifier
    external = True # bool | Set to true to delete an external stack. Only external Swarm stacks are supported (optional)

    try:
        # Remove a stack
        api_instance.stack_delete(id, endpoint_id, external=external)
    except Exception as e:
        print("Exception when calling StacksApi->stack_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Stack identifier | 
 **endpoint_id** | **int**| Environment identifier | 
 **external** | **bool**| Set to true to delete an external stack. Only external Swarm stacks are supported | [optional] 

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
**403** | Permission denied |  -  |
**404** | Not found |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stack_delete_kubernetes_by_name**
> stack_delete_kubernetes_by_name(name, endpoint_id, external=external)

Remove Kubernetes stacks by name

Remove a stack.
**Access policy**: restricted

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
    api_instance = openapi_client.StacksApi(api_client)
    name = 'name_example' # str | Stack name
    endpoint_id = 56 # int | Environment identifier
    external = True # bool | Set to true to delete an external stack. Only external Swarm stacks are supported (optional)

    try:
        # Remove Kubernetes stacks by name
        api_instance.stack_delete_kubernetes_by_name(name, endpoint_id, external=external)
    except Exception as e:
        print("Exception when calling StacksApi->stack_delete_kubernetes_by_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Stack name | 
 **endpoint_id** | **int**| Environment identifier | 
 **external** | **bool**| Set to true to delete an external stack. Only external Swarm stacks are supported | [optional] 

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
**403** | Permission denied |  -  |
**404** | Not found |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stack_file_inspect**
> StacksStackFileResponse stack_file_inspect(id)

Retrieve the content of the Stack file for the specified stack

Get Stack file content.
**Access policy**: restricted

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.stacks_stack_file_response import StacksStackFileResponse
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
    api_instance = openapi_client.StacksApi(api_client)
    id = 56 # int | Stack identifier

    try:
        # Retrieve the content of the Stack file for the specified stack
        api_response = api_instance.stack_file_inspect(id)
        print("The response of StacksApi->stack_file_inspect:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StacksApi->stack_file_inspect: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Stack identifier | 

### Return type

[**StacksStackFileResponse**](StacksStackFileResponse.md)

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
**403** | Permission denied |  -  |
**404** | Stack not found |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stack_git_redeploy**
> PortainerStack stack_git_redeploy(id, body, endpoint_id=endpoint_id)

Redeploy a stack

Pull and redeploy a stack via Git
**Access policy**: authenticated

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.portainer_stack import PortainerStack
from openapi_client.models.stacks_stack_git_redploy_payload import StacksStackGitRedployPayload
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
    api_instance = openapi_client.StacksApi(api_client)
    id = 56 # int | Stack identifier
    body = openapi_client.StacksStackGitRedployPayload() # StacksStackGitRedployPayload | Git configs for pull and redeploy of a stack. **StackName** may only be populated for Kuberenetes stacks, and if specified with a blank string, it will be set to blank
    endpoint_id = 56 # int | Stacks created before version 1.18.0 might not have an associated environment(endpoint) identifier. Use this optional parameter to set the environment(endpoint) identifier used by the stack. (optional)

    try:
        # Redeploy a stack
        api_response = api_instance.stack_git_redeploy(id, body, endpoint_id=endpoint_id)
        print("The response of StacksApi->stack_git_redeploy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StacksApi->stack_git_redeploy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Stack identifier | 
 **body** | [**StacksStackGitRedployPayload**](StacksStackGitRedployPayload.md)| Git configs for pull and redeploy of a stack. **StackName** may only be populated for Kuberenetes stacks, and if specified with a blank string, it will be set to blank | 
 **endpoint_id** | **int**| Stacks created before version 1.18.0 might not have an associated environment(endpoint) identifier. Use this optional parameter to set the environment(endpoint) identifier used by the stack. | [optional] 

### Return type

[**PortainerStack**](PortainerStack.md)

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
**403** | Permission denied |  -  |
**404** | Not found |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stack_inspect**
> PortainerStack stack_inspect(id)

Inspect a stack

Retrieve details about a stack.
**Access policy**: restricted

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.portainer_stack import PortainerStack
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
    api_instance = openapi_client.StacksApi(api_client)
    id = 56 # int | Stack identifier

    try:
        # Inspect a stack
        api_response = api_instance.stack_inspect(id)
        print("The response of StacksApi->stack_inspect:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StacksApi->stack_inspect: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Stack identifier | 

### Return type

[**PortainerStack**](PortainerStack.md)

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
**403** | Permission denied |  -  |
**404** | Stack not found |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stack_list**
> List[PortainerStack] stack_list(filters=filters)

List stacks

List all stacks based on the current user authorizations.
Will return all stacks if using an administrator account otherwise it
will only return the list of stacks the user have access to.
Limited stacks will not be returned by this endpoint.
**Access policy**: authenticated

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.portainer_stack import PortainerStack
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
    api_instance = openapi_client.StacksApi(api_client)
    filters = 'filters_example' # str | Filters to process on the stack list. Encoded as JSON (a map[string]string). For example, {'SwarmID': 'jpofkc0i9uo9wtx1zesuk649w'} will only return stacks that are part of the specified Swarm cluster. Available filters: EndpointID, SwarmID. (optional)

    try:
        # List stacks
        api_response = api_instance.stack_list(filters=filters)
        print("The response of StacksApi->stack_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StacksApi->stack_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filters** | **str**| Filters to process on the stack list. Encoded as JSON (a map[string]string). For example, {&#39;SwarmID&#39;: &#39;jpofkc0i9uo9wtx1zesuk649w&#39;} will only return stacks that are part of the specified Swarm cluster. Available filters: EndpointID, SwarmID. | [optional] 

### Return type

[**List[PortainerStack]**](PortainerStack.md)

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**204** | Success |  -  |
**400** | Invalid request |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stack_migrate**
> PortainerStack stack_migrate(id, body, endpoint_id=endpoint_id)

Migrate a stack to another environment(endpoint)

Migrate a stack from an environment(endpoint) to another environment(endpoint). It will re-create the stack inside the target environment(endpoint) before removing the original stack.
**Access policy**: authenticated

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.portainer_stack import PortainerStack
from openapi_client.models.stacks_stack_migrate_payload import StacksStackMigratePayload
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
    api_instance = openapi_client.StacksApi(api_client)
    id = 56 # int | Stack identifier
    body = openapi_client.StacksStackMigratePayload() # StacksStackMigratePayload | Stack migration details
    endpoint_id = 56 # int | Stacks created before version 1.18.0 might not have an associated environment(endpoint) identifier. Use this optional parameter to set the environment(endpoint) identifier used by the stack. (optional)

    try:
        # Migrate a stack to another environment(endpoint)
        api_response = api_instance.stack_migrate(id, body, endpoint_id=endpoint_id)
        print("The response of StacksApi->stack_migrate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StacksApi->stack_migrate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Stack identifier | 
 **body** | [**StacksStackMigratePayload**](StacksStackMigratePayload.md)| Stack migration details | 
 **endpoint_id** | **int**| Stacks created before version 1.18.0 might not have an associated environment(endpoint) identifier. Use this optional parameter to set the environment(endpoint) identifier used by the stack. | [optional] 

### Return type

[**PortainerStack**](PortainerStack.md)

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
**403** | Permission denied |  -  |
**404** | Stack not found |  -  |
**409** | A stack with the same name is already running on the target environment(endpoint) |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stack_start**
> PortainerStack stack_start(id, endpoint_id)

Starts a stopped Stack

Starts a stopped Stack.
**Access policy**: authenticated

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.portainer_stack import PortainerStack
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
    api_instance = openapi_client.StacksApi(api_client)
    id = 56 # int | Stack identifier
    endpoint_id = 56 # int | Environment identifier

    try:
        # Starts a stopped Stack
        api_response = api_instance.stack_start(id, endpoint_id)
        print("The response of StacksApi->stack_start:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StacksApi->stack_start: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Stack identifier | 
 **endpoint_id** | **int**| Environment identifier | 

### Return type

[**PortainerStack**](PortainerStack.md)

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid request |  -  |
**403** | Permission denied |  -  |
**404** | Not found |  -  |
**409** | Stack name is not unique |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stack_stop**
> PortainerStack stack_stop(id, endpoint_id)

Stops a stopped Stack

Stops a stopped Stack.
**Access policy**: authenticated

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.portainer_stack import PortainerStack
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
    api_instance = openapi_client.StacksApi(api_client)
    id = 56 # int | Stack identifier
    endpoint_id = 56 # int | Environment identifier

    try:
        # Stops a stopped Stack
        api_response = api_instance.stack_stop(id, endpoint_id)
        print("The response of StacksApi->stack_stop:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StacksApi->stack_stop: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Stack identifier | 
 **endpoint_id** | **int**| Environment identifier | 

### Return type

[**PortainerStack**](PortainerStack.md)

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid request |  -  |
**403** | Permission denied |  -  |
**404** | Not found |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stack_update**
> PortainerStack stack_update(id, endpoint_id, body)

Update a stack

Update a stack, only for file based stacks.
**Access policy**: authenticated

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.portainer_stack import PortainerStack
from openapi_client.models.stacks_update_swarm_stack_payload import StacksUpdateSwarmStackPayload
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
    api_instance = openapi_client.StacksApi(api_client)
    id = 56 # int | Stack identifier
    endpoint_id = 56 # int | Environment identifier
    body = openapi_client.StacksUpdateSwarmStackPayload() # StacksUpdateSwarmStackPayload | Stack details

    try:
        # Update a stack
        api_response = api_instance.stack_update(id, endpoint_id, body)
        print("The response of StacksApi->stack_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StacksApi->stack_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Stack identifier | 
 **endpoint_id** | **int**| Environment identifier | 
 **body** | [**StacksUpdateSwarmStackPayload**](StacksUpdateSwarmStackPayload.md)| Stack details | 

### Return type

[**PortainerStack**](PortainerStack.md)

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
**403** | Permission denied |  -  |
**404** | Not found |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stack_update_git**
> PortainerStack stack_update_git(id, body, endpoint_id=endpoint_id)

Update a stack's Git configs

Update the Git settings in a stack, e.g., RepositoryReferenceName and AutoUpdate
**Access policy**: authenticated

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.portainer_stack import PortainerStack
from openapi_client.models.stacks_stack_git_update_payload import StacksStackGitUpdatePayload
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
    api_instance = openapi_client.StacksApi(api_client)
    id = 56 # int | Stack identifier
    body = openapi_client.StacksStackGitUpdatePayload() # StacksStackGitUpdatePayload | Git configs for pull and redeploy a stack
    endpoint_id = 56 # int | Stacks created before version 1.18.0 might not have an associated environment(endpoint) identifier. Use this optional parameter to set the environment(endpoint) identifier used by the stack. (optional)

    try:
        # Update a stack's Git configs
        api_response = api_instance.stack_update_git(id, body, endpoint_id=endpoint_id)
        print("The response of StacksApi->stack_update_git:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StacksApi->stack_update_git: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Stack identifier | 
 **body** | [**StacksStackGitUpdatePayload**](StacksStackGitUpdatePayload.md)| Git configs for pull and redeploy a stack | 
 **endpoint_id** | **int**| Stacks created before version 1.18.0 might not have an associated environment(endpoint) identifier. Use this optional parameter to set the environment(endpoint) identifier used by the stack. | [optional] 

### Return type

[**PortainerStack**](PortainerStack.md)

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
**403** | Permission denied |  -  |
**404** | Not found |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhook_invoke**
> webhook_invoke(webhook_id)

Webhook for triggering stack updates from git

**Access policy**: public

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.StacksApi(api_client)
    webhook_id = 'webhook_id_example' # str | Stack identifier

    try:
        # Webhook for triggering stack updates from git
        api_instance.webhook_invoke(webhook_id)
    except Exception as e:
        print("Exception when calling StacksApi->webhook_invoke: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **str**| Stack identifier | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid request |  -  |
**409** | Autoupdate for the stack isn&#39;t available |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

