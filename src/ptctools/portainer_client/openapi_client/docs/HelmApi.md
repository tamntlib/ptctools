# openapi_client.HelmApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**helm_delete**](HelmApi.md#helm_delete) | **DELETE** /endpoints/{id}/kubernetes/helm/{release} | Delete Helm Release
[**helm_get**](HelmApi.md#helm_get) | **GET** /endpoints/{id}/kubernetes/helm/{name} | Get a helm release
[**helm_get_history**](HelmApi.md#helm_get_history) | **GET** /endpoints/{id}/kubernetes/helm/{release}/history | Get a historical list of releases
[**helm_install**](HelmApi.md#helm_install) | **POST** /endpoints/{id}/kubernetes/helm | Install Helm Chart
[**helm_list**](HelmApi.md#helm_list) | **GET** /endpoints/{id}/kubernetes/helm | List Helm Releases
[**helm_repo_search**](HelmApi.md#helm_repo_search) | **GET** /templates/helm | Search Helm Charts
[**helm_rollback**](HelmApi.md#helm_rollback) | **POST** /endpoints/{id}/kubernetes/helm/{release}/rollback | Rollback a helm release
[**helm_show**](HelmApi.md#helm_show) | **GET** /templates/helm/{command} | Show Helm Chart Information
[**helm_user_repositories_list**](HelmApi.md#helm_user_repositories_list) | **GET** /users/{id}/helm/repositories | List a users helm repositories
[**helm_user_repository_create**](HelmApi.md#helm_user_repository_create) | **POST** /users/{id}/helm/repositories | Create a user helm repository
[**helm_user_repository_delete**](HelmApi.md#helm_user_repository_delete) | **DELETE** /users/{id}/helm/repositories/{repositoryID} | Delete a users helm repositoryies


# **helm_delete**
> helm_delete(id, release, namespace=namespace)

Delete Helm Release

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
    api_instance = openapi_client.HelmApi(api_client)
    id = 56 # int | Environment(Endpoint) identifier
    release = 'release_example' # str | The name of the release/application to uninstall
    namespace = 'namespace_example' # str | An optional namespace (optional)

    try:
        # Delete Helm Release
        api_instance.helm_delete(id, release, namespace=namespace)
    except Exception as e:
        print("Exception when calling HelmApi->helm_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Environment(Endpoint) identifier | 
 **release** | **str**| The name of the release/application to uninstall | 
 **namespace** | **str**| An optional namespace | [optional] 

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
**400** | Invalid environment(endpoint) id or bad request |  -  |
**401** | Unauthorized |  -  |
**404** | Environment(Endpoint) or ServiceAccount not found |  -  |
**500** | Server error or helm error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **helm_get**
> GithubComPortainerPortainerPkgLibhelmReleaseRelease helm_get(id, name, namespace=namespace, show_resources=show_resources, revision=revision)

Get a helm release

Get details of a helm release by release name
**Access policy**: authenticated

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.github_com_portainer_portainer_pkg_libhelm_release_release import GithubComPortainerPortainerPkgLibhelmReleaseRelease
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
    api_instance = openapi_client.HelmApi(api_client)
    id = 56 # int | Environment(Endpoint) identifier
    name = 'name_example' # str | Helm release name
    namespace = 'namespace_example' # str | specify an optional namespace (optional)
    show_resources = True # bool | show resources of the release (optional)
    revision = 56 # int | specify an optional revision (optional)

    try:
        # Get a helm release
        api_response = api_instance.helm_get(id, name, namespace=namespace, show_resources=show_resources, revision=revision)
        print("The response of HelmApi->helm_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HelmApi->helm_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Environment(Endpoint) identifier | 
 **name** | **str**| Helm release name | 
 **namespace** | **str**| specify an optional namespace | [optional] 
 **show_resources** | **bool**| show resources of the release | [optional] 
 **revision** | **int**| specify an optional revision | [optional] 

### Return type

[**GithubComPortainerPortainerPkgLibhelmReleaseRelease**](GithubComPortainerPortainerPkgLibhelmReleaseRelease.md)

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid request payload, such as missing required fields or fields not meeting validation criteria. |  -  |
**401** | Unauthorized access - the user is not authenticated or does not have the necessary permissions. Ensure that you have provided a valid API key or JWT token, and that you have the required permissions. |  -  |
**403** | Permission denied - the user is authenticated but does not have the necessary permissions to access the requested resource or perform the specified operation. Check your user roles and permissions. |  -  |
**404** | Unable to find an environment with the specified identifier. |  -  |
**500** | Server error occurred while attempting to retrieve the release. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **helm_get_history**
> List[GithubComPortainerPortainerPkgLibhelmReleaseRelease] helm_get_history(id, name, namespace=namespace)

Get a historical list of releases

Get a historical list of releases by release name
**Access policy**: authenticated

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.github_com_portainer_portainer_pkg_libhelm_release_release import GithubComPortainerPortainerPkgLibhelmReleaseRelease
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
    api_instance = openapi_client.HelmApi(api_client)
    id = 56 # int | Environment(Endpoint) identifier
    name = 'name_example' # str | Helm release name
    namespace = 'namespace_example' # str | specify an optional namespace (optional)

    try:
        # Get a historical list of releases
        api_response = api_instance.helm_get_history(id, name, namespace=namespace)
        print("The response of HelmApi->helm_get_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HelmApi->helm_get_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Environment(Endpoint) identifier | 
 **name** | **str**| Helm release name | 
 **namespace** | **str**| specify an optional namespace | [optional] 

### Return type

[**List[GithubComPortainerPortainerPkgLibhelmReleaseRelease]**](GithubComPortainerPortainerPkgLibhelmReleaseRelease.md)

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid request payload, such as missing required fields or fields not meeting validation criteria. |  -  |
**401** | Unauthorized access - the user is not authenticated or does not have the necessary permissions. Ensure that you have provided a valid API key or JWT token, and that you have the required permissions. |  -  |
**403** | Permission denied - the user is authenticated but does not have the necessary permissions to access the requested resource or perform the specified operation. Check your user roles and permissions. |  -  |
**404** | Unable to find an environment with the specified identifier. |  -  |
**500** | Server error occurred while attempting to retrieve the historical list of releases. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **helm_install**
> GithubComPortainerPortainerPkgLibhelmReleaseRelease helm_install(id, payload, dry_run=dry_run)

Install Helm Chart

**Access policy**: authenticated

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.github_com_portainer_portainer_pkg_libhelm_release_release import GithubComPortainerPortainerPkgLibhelmReleaseRelease
from openapi_client.models.helm_install_chart_payload import HelmInstallChartPayload
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
    api_instance = openapi_client.HelmApi(api_client)
    id = 56 # int | Environment(Endpoint) identifier
    payload = openapi_client.HelmInstallChartPayload() # HelmInstallChartPayload | Chart details
    dry_run = True # bool | Dry run (optional)

    try:
        # Install Helm Chart
        api_response = api_instance.helm_install(id, payload, dry_run=dry_run)
        print("The response of HelmApi->helm_install:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HelmApi->helm_install: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Environment(Endpoint) identifier | 
 **payload** | [**HelmInstallChartPayload**](HelmInstallChartPayload.md)| Chart details | 
 **dry_run** | **bool**| Dry run | [optional] 

### Return type

[**GithubComPortainerPortainerPkgLibhelmReleaseRelease**](GithubComPortainerPortainerPkgLibhelmReleaseRelease.md)

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**401** | Unauthorized |  -  |
**404** | Environment(Endpoint) or ServiceAccount not found |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **helm_list**
> List[ReleaseReleaseElement] helm_list(id, namespace=namespace, filter=filter, selector=selector)

List Helm Releases

**Access policy**: authenticated

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.release_release_element import ReleaseReleaseElement
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
    api_instance = openapi_client.HelmApi(api_client)
    id = 56 # int | Environment(Endpoint) identifier
    namespace = 'namespace_example' # str | specify an optional namespace (optional)
    filter = 'filter_example' # str | specify an optional filter (optional)
    selector = 'selector_example' # str | specify an optional selector (optional)

    try:
        # List Helm Releases
        api_response = api_instance.helm_list(id, namespace=namespace, filter=filter, selector=selector)
        print("The response of HelmApi->helm_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HelmApi->helm_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Environment(Endpoint) identifier | 
 **namespace** | **str**| specify an optional namespace | [optional] 
 **filter** | **str**| specify an optional filter | [optional] 
 **selector** | **str**| specify an optional selector | [optional] 

### Return type

[**List[ReleaseReleaseElement]**](ReleaseReleaseElement.md)

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid environment(endpoint) identifier |  -  |
**401** | Unauthorized |  -  |
**404** | Environment(Endpoint) or ServiceAccount not found |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **helm_repo_search**
> str helm_repo_search(repo, chart=chart, use_cache=use_cache)

Search Helm Charts

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
    api_instance = openapi_client.HelmApi(api_client)
    repo = 'repo_example' # str | Helm repository URL
    chart = 'chart_example' # str | Helm chart name (optional)
    use_cache = 'use_cache_example' # str | If true will use cache to search (optional)

    try:
        # Search Helm Charts
        api_response = api_instance.helm_repo_search(repo, chart=chart, use_cache=use_cache)
        print("The response of HelmApi->helm_repo_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HelmApi->helm_repo_search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| Helm repository URL | 
 **chart** | **str**| Helm chart name | [optional] 
 **use_cache** | **str**| If true will use cache to search | [optional] 

### Return type

**str**

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | Not found |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **helm_rollback**
> GithubComPortainerPortainerPkgLibhelmReleaseRelease helm_rollback(id, release, namespace=namespace, revision=revision, wait=wait, wait_for_jobs=wait_for_jobs, recreate=recreate, force=force, timeout=timeout)

Rollback a helm release

Rollback a helm release to a previous revision
**Access policy**: authenticated

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.github_com_portainer_portainer_pkg_libhelm_release_release import GithubComPortainerPortainerPkgLibhelmReleaseRelease
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
    api_instance = openapi_client.HelmApi(api_client)
    id = 56 # int | Environment(Endpoint) identifier
    release = 'release_example' # str | Helm release name
    namespace = 'namespace_example' # str | specify an optional namespace (optional)
    revision = 56 # int | specify the revision to rollback to (defaults to previous revision if not specified) (optional)
    wait = True # bool | wait for resources to be ready (default: false) (optional)
    wait_for_jobs = True # bool | wait for jobs to complete before marking the release as successful (default: false) (optional)
    recreate = True # bool | performs pods restart for the resource if applicable (default: true) (optional)
    force = True # bool | force resource update through delete/recreate if needed (default: false) (optional)
    timeout = 56 # int | time to wait for any individual Kubernetes operation in seconds (default: 300) (optional)

    try:
        # Rollback a helm release
        api_response = api_instance.helm_rollback(id, release, namespace=namespace, revision=revision, wait=wait, wait_for_jobs=wait_for_jobs, recreate=recreate, force=force, timeout=timeout)
        print("The response of HelmApi->helm_rollback:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HelmApi->helm_rollback: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Environment(Endpoint) identifier | 
 **release** | **str**| Helm release name | 
 **namespace** | **str**| specify an optional namespace | [optional] 
 **revision** | **int**| specify the revision to rollback to (defaults to previous revision if not specified) | [optional] 
 **wait** | **bool**| wait for resources to be ready (default: false) | [optional] 
 **wait_for_jobs** | **bool**| wait for jobs to complete before marking the release as successful (default: false) | [optional] 
 **recreate** | **bool**| performs pods restart for the resource if applicable (default: true) | [optional] 
 **force** | **bool**| force resource update through delete/recreate if needed (default: false) | [optional] 
 **timeout** | **int**| time to wait for any individual Kubernetes operation in seconds (default: 300) | [optional] 

### Return type

[**GithubComPortainerPortainerPkgLibhelmReleaseRelease**](GithubComPortainerPortainerPkgLibhelmReleaseRelease.md)

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid request payload, such as missing required fields or fields not meeting validation criteria. |  -  |
**401** | Unauthorized access - the user is not authenticated or does not have the necessary permissions. Ensure that you have provided a valid API key or JWT token, and that you have the required permissions. |  -  |
**403** | Permission denied - the user is authenticated but does not have the necessary permissions to access the requested resource or perform the specified operation. Check your user roles and permissions. |  -  |
**404** | Unable to find an environment with the specified identifier or release name. |  -  |
**500** | Server error occurred while attempting to rollback the release. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **helm_show**
> str helm_show(repo, chart, version, command)

Show Helm Chart Information

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
    api_instance = openapi_client.HelmApi(api_client)
    repo = 'repo_example' # str | Helm repository URL
    chart = 'chart_example' # str | Chart name
    version = 'version_example' # str | Chart version
    command = 'command_example' # str | chart/values/readme

    try:
        # Show Helm Chart Information
        api_response = api_instance.helm_show(repo, chart, version, command)
        print("The response of HelmApi->helm_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HelmApi->helm_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| Helm repository URL | 
 **chart** | **str**| Chart name | 
 **version** | **str**| Chart version | 
 **command** | **str**| chart/values/readme | 

### Return type

**str**

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |
**404** | Environment(Endpoint) or ServiceAccount not found |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **helm_user_repositories_list**
> UsersHelmUserRepositoryResponse helm_user_repositories_list(id)

List a users helm repositories

Inspect a user helm repositories.
**Access policy**: authenticated

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.users_helm_user_repository_response import UsersHelmUserRepositoryResponse
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
    api_instance = openapi_client.HelmApi(api_client)
    id = 56 # int | User identifier

    try:
        # List a users helm repositories
        api_response = api_instance.helm_user_repositories_list(id)
        print("The response of HelmApi->helm_user_repositories_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HelmApi->helm_user_repositories_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| User identifier | 

### Return type

[**UsersHelmUserRepositoryResponse**](UsersHelmUserRepositoryResponse.md)

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
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **helm_user_repository_create**
> PortainerHelmUserRepository helm_user_repository_create(id, payload)

Create a user helm repository

Create a user helm repository.
**Access policy**: authenticated

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.portainer_helm_user_repository import PortainerHelmUserRepository
from openapi_client.models.users_add_helm_repo_url_payload import UsersAddHelmRepoUrlPayload
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
    api_instance = openapi_client.HelmApi(api_client)
    id = 56 # int | User identifier
    payload = openapi_client.UsersAddHelmRepoUrlPayload() # UsersAddHelmRepoUrlPayload | Helm Repository

    try:
        # Create a user helm repository
        api_response = api_instance.helm_user_repository_create(id, payload)
        print("The response of HelmApi->helm_user_repository_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HelmApi->helm_user_repository_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| User identifier | 
 **payload** | [**UsersAddHelmRepoUrlPayload**](UsersAddHelmRepoUrlPayload.md)| Helm Repository | 

### Return type

[**PortainerHelmUserRepository**](PortainerHelmUserRepository.md)

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
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **helm_user_repository_delete**
> helm_user_repository_delete(id, repository_id)

Delete a users helm repositoryies

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
    api_instance = openapi_client.HelmApi(api_client)
    id = 56 # int | User identifier
    repository_id = 56 # int | Repository identifier

    try:
        # Delete a users helm repositoryies
        api_instance.helm_user_repository_delete(id, repository_id)
    except Exception as e:
        print("Exception when calling HelmApi->helm_user_repository_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| User identifier | 
 **repository_id** | **int**| Repository identifier | 

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
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

