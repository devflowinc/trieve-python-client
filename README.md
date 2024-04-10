# trieve_py_client
Trieve OpenAPI Specification. This document describes all of the operations available through the Trieve API.

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 0.6.2
- Package version: 0.6.2
- Generator version: 7.4.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://trieve.ai](https://trieve.ai)

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import trieve_py_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import trieve_py_client
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import trieve_py_client
from trieve_py_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.trieve.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = trieve_py_client.Configuration(
    host = "https://api.trieve.ai"
)



# Enter a context with an instance of the API client
with trieve_py_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = trieve_py_client.AuthApi(api_client)

    try:
        # OpenID Connect callback
        api_response = api_instance.callback()
        print("The response of AuthApi->callback:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthApi->callback: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.trieve.ai*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AuthApi* | [**callback**](docs/AuthApi.md#callback) | **GET** /api/auth/callback | OpenID Connect callback
*AuthApi* | [**get_me**](docs/AuthApi.md#get_me) | **GET** /api/auth/me | Get Me
*AuthApi* | [**login**](docs/AuthApi.md#login) | **GET** /api/auth | Login
*AuthApi* | [**logout**](docs/AuthApi.md#logout) | **DELETE** /api/auth | Logout
*ChunkApi* | [**create_chunk**](docs/ChunkApi.md#create_chunk) | **POST** /api/chunk | Create or Upsert Chunk or Chunks
*ChunkApi* | [**create_suggested_queries_handler**](docs/ChunkApi.md#create_suggested_queries_handler) | **POST** /api/chunk/gen_suggestions | Generate suggested queries
*ChunkApi* | [**delete_chunk**](docs/ChunkApi.md#delete_chunk) | **DELETE** /api/chunk/{chunk_id} | Delete Chunk
*ChunkApi* | [**delete_chunk_by_tracking_id**](docs/ChunkApi.md#delete_chunk_by_tracking_id) | **DELETE** /api/chunk/tracking_id/{tracking_id} | Delete Chunk By Tracking Id
*ChunkApi* | [**generate_off_chunks**](docs/ChunkApi.md#generate_off_chunks) | **POST** /api/chunk/generate | RAG on Specified Chunks
*ChunkApi* | [**get_chunk_by_id**](docs/ChunkApi.md#get_chunk_by_id) | **GET** /api/chunk/{chunk_id} | Get Chunk By Id
*ChunkApi* | [**get_chunk_by_tracking_id**](docs/ChunkApi.md#get_chunk_by_tracking_id) | **GET** /api/chunk/tracking_id/{tracking_id} | Get Chunk By Tracking Id
*ChunkApi* | [**get_recommended_chunks**](docs/ChunkApi.md#get_recommended_chunks) | **POST** /api/chunk/recommend | Get Recommended Chunks
*ChunkApi* | [**search_chunk**](docs/ChunkApi.md#search_chunk) | **POST** /api/chunk/search | Search
*ChunkApi* | [**update_chunk**](docs/ChunkApi.md#update_chunk) | **PUT** /api/chunk | Update Chunk
*ChunkApi* | [**update_chunk_by_tracking_id**](docs/ChunkApi.md#update_chunk_by_tracking_id) | **PUT** /api/chunk/tracking_id/update | Update Chunk By Tracking Id
*ChunkGroupApi* | [**add_chunk_to_group**](docs/ChunkGroupApi.md#add_chunk_to_group) | **POST** /api/chunk_group/chunk/{group_id} | Add Chunk to Group
*ChunkGroupApi* | [**add_chunk_to_group_by_tracking_id**](docs/ChunkGroupApi.md#add_chunk_to_group_by_tracking_id) | **POST** /api/chunk_group/tracking_id/{tracking_id} | Add Chunk to Group by Tracking ID
*ChunkGroupApi* | [**create_chunk_group**](docs/ChunkGroupApi.md#create_chunk_group) | **POST** /api/chunk_group | Create Chunk Group
*ChunkGroupApi* | [**delete_chunk_group**](docs/ChunkGroupApi.md#delete_chunk_group) | **DELETE** /api/chunk_group/{group_id} | Delete Group
*ChunkGroupApi* | [**delete_group_by_tracking_id**](docs/ChunkGroupApi.md#delete_group_by_tracking_id) | **DELETE** /api/chunk_group/tracking_id/{tracking_id} | Delete Group by Tracking ID
*ChunkGroupApi* | [**get_chunk_group**](docs/ChunkGroupApi.md#get_chunk_group) | **GET** /api/chunk_group/{group_id} | Get Group
*ChunkGroupApi* | [**get_chunks_in_group**](docs/ChunkGroupApi.md#get_chunks_in_group) | **GET** /api/chunk_group/{group_id}/{page} | Get Chunks in Group
*ChunkGroupApi* | [**get_chunks_in_group_by_tracking_id**](docs/ChunkGroupApi.md#get_chunks_in_group_by_tracking_id) | **GET** /api/chunk_group/tracking_id/{group_tracking_id}/{page} | Get Chunks in Group by Tracking ID
*ChunkGroupApi* | [**get_group_by_tracking_id**](docs/ChunkGroupApi.md#get_group_by_tracking_id) | **GET** /api/chunk_group/tracking_id/{tracking_id} | Get Group by Tracking ID
*ChunkGroupApi* | [**get_groups_chunk_is_in**](docs/ChunkGroupApi.md#get_groups_chunk_is_in) | **POST** /api/chunk_group/chunks | Get Groups for Chunks
*ChunkGroupApi* | [**get_recommended_groups**](docs/ChunkGroupApi.md#get_recommended_groups) | **POST** /api/chunk_group/recommend | Get Recommended Groups
*ChunkGroupApi* | [**get_specific_dataset_chunk_groups**](docs/ChunkGroupApi.md#get_specific_dataset_chunk_groups) | **GET** /api/dataset/groups/{dataset_id}/{page} | Get Groups for Dataset
*ChunkGroupApi* | [**remove_chunk_from_group**](docs/ChunkGroupApi.md#remove_chunk_from_group) | **DELETE** /api/chunk_group/chunk/{group_id} | Remove Chunk from Group
*ChunkGroupApi* | [**search_over_groups**](docs/ChunkGroupApi.md#search_over_groups) | **POST** /api/chunk_group/group_oriented_search | Search Over Groups
*ChunkGroupApi* | [**search_within_group**](docs/ChunkGroupApi.md#search_within_group) | **POST** /api/chunk_group/search | Search Within Group
*ChunkGroupApi* | [**update_chunk_group**](docs/ChunkGroupApi.md#update_chunk_group) | **PUT** /api/chunk_group | Update Group
*ChunkGroupApi* | [**update_group_by_tracking_id**](docs/ChunkGroupApi.md#update_group_by_tracking_id) | **PUT** /api/chunk_group/tracking_id/{tracking_id} | Update Group by Tracking ID
*DatasetApi* | [**create_dataset**](docs/DatasetApi.md#create_dataset) | **POST** /api/dataset | Create dataset
*DatasetApi* | [**delete_dataset**](docs/DatasetApi.md#delete_dataset) | **DELETE** /api/dataset/{dataset_id} | Delete Dataset
*DatasetApi* | [**get_client_dataset_config**](docs/DatasetApi.md#get_client_dataset_config) | **GET** /api/dataset/envs | Get Client Configuration
*DatasetApi* | [**get_dataset**](docs/DatasetApi.md#get_dataset) | **GET** /api/dataset/{dataset_id} | Get Dataset
*DatasetApi* | [**get_datasets_from_organization**](docs/DatasetApi.md#get_datasets_from_organization) | **GET** /api/dataset/organization/{organization_id} | Get Datasets from Organization
*DatasetApi* | [**update_dataset**](docs/DatasetApi.md#update_dataset) | **PUT** /api/dataset | Update Dataset
*EventsApi* | [**get_events**](docs/EventsApi.md#get_events) | **POST** /api/events | Get events for the dataset
*FileApi* | [**delete_file_handler**](docs/FileApi.md#delete_file_handler) | **DELETE** /api/file/{file_id} | Delete File
*FileApi* | [**get_dataset_files_handler**](docs/FileApi.md#get_dataset_files_handler) | **GET** /api/dataset/files/{dataset_id}/{page} | Get Files for Dataset
*FileApi* | [**get_file_handler**](docs/FileApi.md#get_file_handler) | **GET** /api/file/{file_id} | Get File
*FileApi* | [**upload_file_handler**](docs/FileApi.md#upload_file_handler) | **POST** /api/file | Upload File
*HealthApi* | [**health_check**](docs/HealthApi.md#health_check) | **GET** /api/health | Health Check
*InvitationApi* | [**post_invitation**](docs/InvitationApi.md#post_invitation) | **POST** /api/invitation | Send Invitation
*MessageApi* | [**create_message_completion_handler**](docs/MessageApi.md#create_message_completion_handler) | **POST** /api/message | Create a message
*MessageApi* | [**edit_message_handler**](docs/MessageApi.md#edit_message_handler) | **PUT** /api/message | Edit a message
*MessageApi* | [**get_all_topic_messages**](docs/MessageApi.md#get_all_topic_messages) | **GET** /api/messages/{messages_topic_id} | Get all messages for a given topic
*MessageApi* | [**regenerate_message_handler**](docs/MessageApi.md#regenerate_message_handler) | **DELETE** /api/message | Regenerate message
*OrganizationApi* | [**create_organization**](docs/OrganizationApi.md#create_organization) | **POST** /api/organization | Create Organization
*OrganizationApi* | [**delete_organization_by_id**](docs/OrganizationApi.md#delete_organization_by_id) | **DELETE** /api/organization/{organization_id} | Delete Organization
*OrganizationApi* | [**get_organization_by_id**](docs/OrganizationApi.md#get_organization_by_id) | **GET** /api/organization/{organization_id} | Get Organization
*OrganizationApi* | [**get_organization_usage**](docs/OrganizationApi.md#get_organization_usage) | **GET** /api/organization/usage/{organization_id} | Get Organization Usage
*OrganizationApi* | [**get_organization_users**](docs/OrganizationApi.md#get_organization_users) | **GET** /api/organization/users/{organization_id} | Get Organization Users
*OrganizationApi* | [**update_organization**](docs/OrganizationApi.md#update_organization) | **PUT** /api/organization | Update Organization
*StripeApi* | [**cancel_subscription**](docs/StripeApi.md#cancel_subscription) | **DELETE** /api/stripe/subscription/{subscription_id} | Cancel Subscription
*StripeApi* | [**direct_to_payment_link**](docs/StripeApi.md#direct_to_payment_link) | **GET** /api/stripe/payment_link/{plan_id}/{organization_id} | Checkout
*StripeApi* | [**get_all_plans**](docs/StripeApi.md#get_all_plans) | **GET** /api/stripe/plans | Get All Plans
*StripeApi* | [**update_subscription_plan**](docs/StripeApi.md#update_subscription_plan) | **PATCH** /api/stripe/subscription_plan/{subscription_id}/{plan_id} | Update Subscription Plan
*TopicApi* | [**create_topic**](docs/TopicApi.md#create_topic) | **POST** /api/topic | Create Topic
*TopicApi* | [**delete_topic**](docs/TopicApi.md#delete_topic) | **DELETE** /api/topic/{topic_id} | Delete Topic
*TopicApi* | [**get_all_topics_for_user**](docs/TopicApi.md#get_all_topics_for_user) | **GET** /api/topic/user/{user_id} | Get All Topics for User
*TopicApi* | [**update_topic**](docs/TopicApi.md#update_topic) | **PUT** /api/topic | Update Topic
*UserApi* | [**delete_user_api_key**](docs/UserApi.md#delete_user_api_key) | **DELETE** /api/user/api_key/{api_key_id} | Delete User Api Key
*UserApi* | [**set_user_api_key**](docs/UserApi.md#set_user_api_key) | **POST** /api/user/api_key | Set User Api Key
*UserApi* | [**update_user**](docs/UserApi.md#update_user) | **PUT** /api/user | Update User


## Documentation For Models

 - [AddChunkToGroupData](docs/AddChunkToGroupData.md)
 - [ApiKeyDTO](docs/ApiKeyDTO.md)
 - [AuthQuery](docs/AuthQuery.md)
 - [BatchQueuedChunkResponse](docs/BatchQueuedChunkResponse.md)
 - [BookmarkData](docs/BookmarkData.md)
 - [BookmarkGroupResult](docs/BookmarkGroupResult.md)
 - [ChatMessageProxy](docs/ChatMessageProxy.md)
 - [ChunkData](docs/ChunkData.md)
 - [ChunkFilter](docs/ChunkFilter.md)
 - [ChunkGroup](docs/ChunkGroup.md)
 - [ChunkGroupAndFile](docs/ChunkGroupAndFile.md)
 - [ChunkMetadata](docs/ChunkMetadata.md)
 - [ChunkMetadataWithScore](docs/ChunkMetadataWithScore.md)
 - [ClientDatasetConfiguration](docs/ClientDatasetConfiguration.md)
 - [CreateChunkData](docs/CreateChunkData.md)
 - [CreateChunkGroupData](docs/CreateChunkGroupData.md)
 - [CreateDatasetRequest](docs/CreateDatasetRequest.md)
 - [CreateMessageData](docs/CreateMessageData.md)
 - [CreateOrganizationData](docs/CreateOrganizationData.md)
 - [CreateTopicData](docs/CreateTopicData.md)
 - [Dataset](docs/Dataset.md)
 - [DatasetAndUsage](docs/DatasetAndUsage.md)
 - [DatasetDTO](docs/DatasetDTO.md)
 - [DatasetUsageCount](docs/DatasetUsageCount.md)
 - [DeleteTopicData](docs/DeleteTopicData.md)
 - [DeleteUserApiKeyRequest](docs/DeleteUserApiKeyRequest.md)
 - [EditMessageData](docs/EditMessageData.md)
 - [ErrorResponseBody](docs/ErrorResponseBody.md)
 - [Event](docs/Event.md)
 - [EventReturn](docs/EventReturn.md)
 - [FieldCondition](docs/FieldCondition.md)
 - [File](docs/File.md)
 - [FileDTO](docs/FileDTO.md)
 - [GenerateChunksRequest](docs/GenerateChunksRequest.md)
 - [GetEventsData](docs/GetEventsData.md)
 - [GetGroupsForChunksData](docs/GetGroupsForChunksData.md)
 - [GroupData](docs/GroupData.md)
 - [GroupScoreChunk](docs/GroupScoreChunk.md)
 - [GroupScoreSlimChunks](docs/GroupScoreSlimChunks.md)
 - [InvitationData](docs/InvitationData.md)
 - [MatchCondition](docs/MatchCondition.md)
 - [Message](docs/Message.md)
 - [Organization](docs/Organization.md)
 - [OrganizationUsageCount](docs/OrganizationUsageCount.md)
 - [Range](docs/Range.md)
 - [RangeCondition](docs/RangeCondition.md)
 - [RecommendChunksRequest](docs/RecommendChunksRequest.md)
 - [RecommendGroupChunksRequest](docs/RecommendGroupChunksRequest.md)
 - [RegenerateMessageData](docs/RegenerateMessageData.md)
 - [ReturnQueuedChunk](docs/ReturnQueuedChunk.md)
 - [ScoreChunkDTO](docs/ScoreChunkDTO.md)
 - [ScoreSlimChunks](docs/ScoreSlimChunks.md)
 - [SearchChunkData](docs/SearchChunkData.md)
 - [SearchChunkQueryResponseBody](docs/SearchChunkQueryResponseBody.md)
 - [SearchOverGroupsData](docs/SearchOverGroupsData.md)
 - [SearchOverGroupsResults](docs/SearchOverGroupsResults.md)
 - [SearchOverGroupsSlimResults](docs/SearchOverGroupsSlimResults.md)
 - [SearchSlimChunkQueryResponseBody](docs/SearchSlimChunkQueryResponseBody.md)
 - [SearchWithinGroupData](docs/SearchWithinGroupData.md)
 - [SearchWithinGroupResults](docs/SearchWithinGroupResults.md)
 - [SearchWithinGroupSlimResults](docs/SearchWithinGroupSlimResults.md)
 - [SetUserApiKeyRequest](docs/SetUserApiKeyRequest.md)
 - [SetUserApiKeyResponse](docs/SetUserApiKeyResponse.md)
 - [SingleQueuedChunkResponse](docs/SingleQueuedChunkResponse.md)
 - [SlimChunkMetadata](docs/SlimChunkMetadata.md)
 - [SlimChunkMetadataWithScore](docs/SlimChunkMetadataWithScore.md)
 - [SlimGroup](docs/SlimGroup.md)
 - [SlimUser](docs/SlimUser.md)
 - [StripePlan](docs/StripePlan.md)
 - [SuggestedQueriesRequest](docs/SuggestedQueriesRequest.md)
 - [SuggestedQueriesResponse](docs/SuggestedQueriesResponse.md)
 - [Topic](docs/Topic.md)
 - [UpdateChunkByTrackingIdData](docs/UpdateChunkByTrackingIdData.md)
 - [UpdateChunkData](docs/UpdateChunkData.md)
 - [UpdateChunkGroupData](docs/UpdateChunkGroupData.md)
 - [UpdateDatasetRequest](docs/UpdateDatasetRequest.md)
 - [UpdateGroupByTrackingIDData](docs/UpdateGroupByTrackingIDData.md)
 - [UpdateOrganizationData](docs/UpdateOrganizationData.md)
 - [UpdateTopicData](docs/UpdateTopicData.md)
 - [UpdateUserData](docs/UpdateUserData.md)
 - [UploadFileData](docs/UploadFileData.md)
 - [UploadFileResult](docs/UploadFileResult.md)
 - [UserOrganization](docs/UserOrganization.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="ApiKey"></a>
### ApiKey

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author

developers@trieve.ai


