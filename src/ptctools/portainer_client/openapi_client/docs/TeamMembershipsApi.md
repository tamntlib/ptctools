# openapi_client.TeamMembershipsApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**team_membership_create**](TeamMembershipsApi.md#team_membership_create) | **POST** /team_memberships | Create a new team membership
[**team_membership_delete**](TeamMembershipsApi.md#team_membership_delete) | **DELETE** /team_memberships/{id} | Remove a team membership
[**team_membership_list**](TeamMembershipsApi.md#team_membership_list) | **GET** /team_memberships | List team memberships
[**team_membership_update**](TeamMembershipsApi.md#team_membership_update) | **PUT** /team_memberships/{id} | Update a team membership
[**team_memberships**](TeamMembershipsApi.md#team_memberships) | **GET** /teams/{id}/memberships | List team memberships


# **team_membership_create**
> PortainerTeamMembership team_membership_create(body)

Create a new team membership

Create a new team memberships. Access is only available to administrators leaders of the associated team.
**Access policy**: administrator

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.portainer_team_membership import PortainerTeamMembership
from openapi_client.models.teammemberships_team_membership_create_payload import TeammembershipsTeamMembershipCreatePayload
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
    api_instance = openapi_client.TeamMembershipsApi(api_client)
    body = openapi_client.TeammembershipsTeamMembershipCreatePayload() # TeammembershipsTeamMembershipCreatePayload | Team membership details

    try:
        # Create a new team membership
        api_response = api_instance.team_membership_create(body)
        print("The response of TeamMembershipsApi->team_membership_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamMembershipsApi->team_membership_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TeammembershipsTeamMembershipCreatePayload**](TeammembershipsTeamMembershipCreatePayload.md)| Team membership details | 

### Return type

[**PortainerTeamMembership**](PortainerTeamMembership.md)

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
**403** | Permission denied to manage memberships |  -  |
**409** | Team membership already registered |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_membership_delete**
> team_membership_delete(id)

Remove a team membership

Remove a team membership. Access is only available to administrators leaders of the associated team.
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
    api_instance = openapi_client.TeamMembershipsApi(api_client)
    id = 56 # int | TeamMembership identifier

    try:
        # Remove a team membership
        api_instance.team_membership_delete(id)
    except Exception as e:
        print("Exception when calling TeamMembershipsApi->team_membership_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| TeamMembership identifier | 

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
**404** | TeamMembership not found |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_membership_list**
> List[PortainerTeamMembership] team_membership_list()

List team memberships

List team memberships. Access is only available to administrators and team leaders.
**Access policy**: administrator

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.portainer_team_membership import PortainerTeamMembership
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
    api_instance = openapi_client.TeamMembershipsApi(api_client)

    try:
        # List team memberships
        api_response = api_instance.team_membership_list()
        print("The response of TeamMembershipsApi->team_membership_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamMembershipsApi->team_membership_list: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[PortainerTeamMembership]**](PortainerTeamMembership.md)

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

# **team_membership_update**
> PortainerTeamMembership team_membership_update(id, body)

Update a team membership

Update a team membership. Access is only available to administrators or leaders of the associated team.
**Access policy**: administrator or leaders of the associated team

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.portainer_team_membership import PortainerTeamMembership
from openapi_client.models.teammemberships_team_membership_update_payload import TeammembershipsTeamMembershipUpdatePayload
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
    api_instance = openapi_client.TeamMembershipsApi(api_client)
    id = 56 # int | Team membership identifier
    body = openapi_client.TeammembershipsTeamMembershipUpdatePayload() # TeammembershipsTeamMembershipUpdatePayload | Team membership details

    try:
        # Update a team membership
        api_response = api_instance.team_membership_update(id, body)
        print("The response of TeamMembershipsApi->team_membership_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamMembershipsApi->team_membership_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Team membership identifier | 
 **body** | [**TeammembershipsTeamMembershipUpdatePayload**](TeammembershipsTeamMembershipUpdatePayload.md)| Team membership details | 

### Return type

[**PortainerTeamMembership**](PortainerTeamMembership.md)

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
**404** | TeamMembership not found |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_memberships**
> List[PortainerTeamMembership] team_memberships(id)

List team memberships

List team memberships. Access is only available to administrators and team leaders.
**Access policy**: restricted

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.portainer_team_membership import PortainerTeamMembership
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
    api_instance = openapi_client.TeamMembershipsApi(api_client)
    id = 56 # int | Team Id

    try:
        # List team memberships
        api_response = api_instance.team_memberships(id)
        print("The response of TeamMembershipsApi->team_memberships:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamMembershipsApi->team_memberships: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Team Id | 

### Return type

[**List[PortainerTeamMembership]**](PortainerTeamMembership.md)

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

