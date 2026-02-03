# openapi_client.GitopsApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**git_operation_repo_file_preview**](GitopsApi.md#git_operation_repo_file_preview) | **POST** /gitops/repo/file/preview | preview the content of target file in the git repository


# **git_operation_repo_file_preview**
> GitopsFileResponse git_operation_repo_file_preview(body)

preview the content of target file in the git repository

Retrieve the compose file content based on git repository configuration
**Access policy**: authenticated

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.gitops_file_response import GitopsFileResponse
from openapi_client.models.gitops_repository_file_preview_payload import GitopsRepositoryFilePreviewPayload
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
    api_instance = openapi_client.GitopsApi(api_client)
    body = openapi_client.GitopsRepositoryFilePreviewPayload() # GitopsRepositoryFilePreviewPayload | Template details

    try:
        # preview the content of target file in the git repository
        api_response = api_instance.git_operation_repo_file_preview(body)
        print("The response of GitopsApi->git_operation_repo_file_preview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GitopsApi->git_operation_repo_file_preview: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GitopsRepositoryFilePreviewPayload**](GitopsRepositoryFilePreviewPayload.md)| Template details | 

### Return type

[**GitopsFileResponse**](GitopsFileResponse.md)

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
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

