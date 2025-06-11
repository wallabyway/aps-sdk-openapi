# Autodesk Platform Services APIs overview

### Construction.Issues
An issue is an item that is created in ACC for tracking, managing and communicating tasks, problems and other points of concern through to resolution. You can manage different types of issues, such as design, safety, and commissioning. We currently support issues that are associated with a project.

### Account Admin
The Account Admin API automates creating and managing projects, assigning and managing project users, and managing member and partner company directories. You can also synchronize data with external systems.

### Authentication
OAuth2 token management APIs.

### Data Management API
The Data Management API provides a unified and consistent way to access data across BIM 360 Team, Fusion Team (formerly known as A360 Team), BIM 360 Docs, A360 Personal, and the Object Storage Service. With this API, you can accomplish a number of workflows, including accessing a Fusion model in Fusion Team and getting an ordered structure of items, IDs, and properties for generating a bill of materials in a 3rd-party process. Or, you might want to superimpose a Fusion model and a building model to use in the Viewer.

### Model Derivative
Use the Model Derivative API to translate designs from one CAD format to another.

### oss
The Object Storage Service (OSS) allows your application to download and upload raw files (such as PDF, XLS, DWG, or RVT) that are managed by the Data service.

### Secure Service Account (SSA)
APIs to manage Service accounts and keys. A service account is an identity that an application can use to make API requests to other services without a user authorizing the requests. A service account is identified by a unique email address and has an Oxygen ID. A service account has one or more private keys. A private key is generated through an asymmetric cryptography algorithm; the paired public key is stored by Autodesk Identity. An application can use a service account's private key to generate a JWT token. The JWT token provides proof of implicit authentication and authorization for this service account; an application can exchange it for a three-legged access token for the service service. General error response from APIs: ``` { "title:": "...", "detail": "..." } ```

### Webhooks
The Webhooks API enables applications to listen to APS events and receive notifications when they occur. When an event is triggered, the Webhooks service sends a notification to a callback URL you have defined. You can customize the types of events and resources for which you receive notifications. For example, you can set up a webhook to send notifications when files are modified or deleted in a specified hub or project. Below is quick summary of this workflow: 1. Identify the data for which you want to receive notifications. 2. Use the Webhooks API to create one or more hooks. 3. The Webhooks service will notify the webhook when there is a change in the data.



## Construction.Issues

_Generated from `Issues.yaml`_

An issue is an item that is created in ACC for tracking, managing and communicating tasks, problems and other points of concern through to resolution. You can manage different types of issues, such as design, safety, and commissioning. We currently support issues that are associated with a project.

---

### Your GET endpoint

**Endpoint:** `GET /construction/issues/v1/projects/{projectId}/users/me`
**Operation ID:** `getUserProfile`

#### Description
Returns the current user permissions.

#### Parameters
- Ref: `#/components/parameters/x-ads-region`

#### Responses
- **200**: OK
- **400**: Bad Request
- **403**: Forbidden
- **404**: Not Found
- **500**: Internal Server Error

---

### Your GET endpoint

**Endpoint:** `GET /construction/issues/v1/projects/{projectId}/issue-types`
**Operation ID:** `getIssuesTypes`

#### Description
Retrieves a project’s categories and types.

#### Parameters
- `include` in `query` (required: False) — Use include=subtypes to include the types (subtypes) for each category (type).
- `limit` in `query` (required: False) — Add limit=20 to limit the results count (together with the offset to support pagination).
- `offset` in `query` (required: False) — Add offset=20 to get partial results (together with the limit to support pagination).
- `filter[updatedAt]` in `query` (required: False) — Retrieves types that were last updated at the specified date and time, in in one of the following URL-encoded formats: YYYY-MM-DDThh:mm:ss.sz or YYYY-MM-DD. Separate multiple values with commas.
- `filter[isActive]` in `query` (required: False) — Filter types by status e.g. filter[isActive]=true will only return active types. Default value: undefined (meaning both active & inactive issue type categories will return).
- Ref: `#/components/parameters/x-ads-region`

#### Responses
- **200**: OK
- **400**: Bad Request
- **403**: Forbidden
- **404**: Not Found
- **500**: Internal Server Error

---

### Your GET endpoint

**Endpoint:** `GET /construction/issues/v1/projects/{projectId}/issue-attribute-definitions`
**Operation ID:** `getAttributeDefinitions`

#### Description
Retrieves information about issue custom attributes (custom fields) for a project, including the custom attribute title, description and type.

#### Parameters
- Ref: `#/components/parameters/x-ads-region`
- `limit` in `query` (required: False) — The number of custom attribute definitions to return in the response payload. For example, limit=2. Acceptable values: 1-200. Default value: 200.
- `offset` in `query` (required: False) — The number of custom attribute definitions you want to begin retrieving results from.
- `filter[createdAt]` in `query` (required: False) — Retrieves items that were created at the specified date and time, in one of the following URL-encoded formats: YYYY-MM-DDThh:mm:ss.sz or YYYY-MM-DD. Separate multiple values with commas.
- `filter[updatedAt]` in `query` (required: False) — Retrieves items that were last updated at the specified date and time, in one of the following URL-encoded formats: YYYY-MM-DDThh:mm:ss.sz or YYYY-MM-DD. Separate multiple values with commas.
- `filter[deletedAt]` in `query` (required: False) — Retrieves types that were deleted at the specified date and time, in one of the following URL-encoded formats: YYYY-MM-DDThh:mm:ss.sz or YYYY-MM-DD. Separate multiple values with commas.
- `filter[dataType]` in `query` (required: False) — Retrieves issue custom attribute definitions with the specified data type. Possible values: list (this corresponds to dropdown in the UI), text, paragraph, numeric. For example, filter[dataType]=text,numeric.

#### Responses
- **200**: OK
- **400**: Bad Request
- **403**: Forbidden
- **404**: Not Found
- **500**: Internal Server Error

---

### Your GET endpoint

**Endpoint:** `GET /construction/issues/v1/projects/{projectId}/issue-attribute-mappings`
**Operation ID:** `getAttributeMappings`

#### Description
Retrieves information about the issue custom attributes (custom fields) that are assigned to issue categories and issue types.

#### Parameters
- Ref: `#/components/parameters/x-ads-region`
- `limit` in `query` (required: False) — The number of custom attribute mappings to return in the response payload. For example, limit=2. Acceptable values: 1-200. Default value: 200.
- `offset` in `query` (required: False) — The number of custom attribute mappings you want to begin retrieving results from.
- `filter[createdAt]` in `query` (required: False) — Retrieves items that were created at the specified date and time, in one of the following URL-encoded formats: YYYY-MM-DDThh:mm:ss.sz or YYYY-MM-DD. Separate multiple values with commas.
- `filter[updatedAt]` in `query` (required: False) — Retrieves items that were last updated at the specified date and time, in one of the following URL-encoded formats: YYYY-MM-DDThh:mm:ss.sz or YYYY-MM-DD. Separate multiple values with commas.
- `filter[deletedAt]` in `query` (required: False) — Retrieves types that were deleted at the specified date and time, in one of the following URL-encoded formats: YYYY-MM-DDThh:mm:ss.sz or YYYY-MM-DD. Separate multiple values with commas.
- `filter[attributeDefinitionId]` in `query` (required: False) — Retrieves issue custom attribute mappings associated with the specified issue custom attribute definitions. Separate multiple values with commas. For example: filter[attributeDefinitionId]=18ee5858-cbf1-451a-a525-7c6ff8156775.
- `filter[mappedItemId]` in `query` (required: False) — Retrieves issue custom attribute mappings associated with the specified items (project, type, or subtype). Separate multiple values with commas. For example: filter[mappedItemId]=18ee5858-cbf1-451a-a525-7c6ff8156775. Note that this does not retrieve inherited custom attribute mappings or custom attribute mappings of descendants.

#### Responses
- **200**: OK

---

### Your GET endpoint

**Endpoint:** `GET /construction/issues/v1/projects/{projectId}/issue-root-cause-categories`
**Operation ID:** `getRootCauseCategories`

#### Description
Retrieves a list of supported root cause categories and root causes that you can allocate to an issue. For example, communication and coordination.

#### Parameters
- Ref: `#/components/parameters/x-ads-region`
- `include` in `query` (required: False) — Add ‘include=rootcauses’ to add the root causes for each category.
- `limit` in `query` (required: False) — Add limit=20 to limit the results count (together with the offset to support pagination).
- `offset` in `query` (required: False) — Add offset=20 to get partial results (together with the limit to support pagination)
- `filter[updatedAt]` in `query` (required: False) — Retrieves root cause categories updated at the specified date and time, in one of the following URL-encoded formats: YYYY-MM-DDThh:mm:ss.sz or YYYY-MM-DD. Separate multiple values with commas.

#### Responses
- **200**: OK
- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **500**: Internal Server Error

---

### Your GET endpoint

**Endpoint:** `GET /construction/issues/v1/projects/{projectId}/issues`
**Operation ID:** `getIssues`

#### Description
Retrieves information about all the issues in a project, including details about their associated comments and attachments.

#### Parameters
- `filter[id]` in `query` (required: False) — Filter issues by the unique issue ID. Separate multiple values with commas.
- `filter[issueTypeId]` in `query` (required: False) — Filter issues by the unique identifier of the category of the issue. Note that the API name for category is type. Separate multiple values with commas.
- `filter[issueSubtypeId]` in `query` (required: False) — Filter issues by the unique identifier of the type of the issue. Note that the API name for type is subtype. Separate multiple values with commas.
- `filter[status]` in `query` (required: False) — Filter issues by their status. Separate multiple values with commas.
- `filter[linkedDocumentUrn]` in `query` (required: False) — Retrieves pushpin issues associated with the specified files. We support all file types that are compatible with the Files tool. You need to specify the URL-encoded file item IDs.
- Ref: `#/components/parameters/x-ads-region`
- `filter[dueDate]` in `query` (required: False) — Filter issues by due date, in one of the following URL-encoded format: YYYY-MM-DD. Separate multiple values with commas.
- `filter[startDate]` in `query` (required: False) — Filter issues by start date, in one of the following URL-encoded format: YYYY-MM-DD. Separate multiple values with commas.
- `filter[createdAt]` in `query` (required: False) — Filter issues created at the specified date and time, in one of the following URL-encoded formats: YYYY-MM-DDThh:mm:ss.sz or YYYY-MM-DD. Separate multiple values with commas
- `filter[createdBy]` in `query` (required: False) — Filter issues by the unique identifier of the user who created the issue. Separate multiple values with commas.
- `filter[updatedAt]` in `query` (required: False) — Filter issues updated at the specified date and time, in one of the following URL-encoded formats: YYYY-MM-DDThh:mm:ss.sz or YYYY-MM-DD. Separate multiple values with commas.
- `filter[updatedBy]` in `query` (required: False) — Filter issues by the unique identifier of the user who updated the issue. Separate multiple values with commas.
- `filter[assignedTo]` in `query` (required: False) — Filter issues by the unique Autodesk ID of the User/Company/Role identifier of the current assignee of this issue. Separate multiple values with commas.
- `filter[rootCauseId]` in `query` (required: False) — Filter issues by the unique identifier of the type of root cause for the issue. Separate multiple values with commas.
- `filter[locationId]` in `query` (required: False) — Retrieves issues associated with the specified location but not the location’s sublocations. To also retrieve issues that relate to the locations’s sublocations use the sublocationId filter. Separate multiple values with commas.
- `filter[subLocationId]` in `query` (required: False) — Retrieves issues associated with the specified unique LBS (Location Breakdown Structure) identifier, as well as issues associated with the sub locations of the LBS identifier. Separate multiple values with commas.
- `filter[closedBy]` in `query` (required: False) — Filter issues by the unique identifier of the user who closed the issue. Separate multiple values with commas. For Example: A3RGM375QTZ7.
- `filter[closedAt]` in `query` (required: False) — Filter issues closed at the specified date and time, in one of the following URL-encoded formats: YYYY-MM-DDThh:mm:ss.sz or YYYY-MM-DD. Separate multiple values with commas.
- `filter[search]` in `query` (required: False) — Filter issues using ‘search’ criteria. this will filter both title and issues display ID. For example, use filter[search]=300
- `filter[displayId]` in `query` (required: False) — Filter issues by the chronological user-friendly identifier. Separate multiple values with commas.
- `filter[assignedToType]` in `query` (required: False) — Filter issues by the type of the current assignee of this issue. Separate multiple values with commas. Possible values: Possible values: user, company, role, null. For Example: user.
- `filter[customAttributes]` in `query` (required: False) — Filter issues by the custom attributes. Each custom attribute filter should be defined by it’s uuid. For example: filter[customAttributes][f227d940-ae9b-4722-9297-389f4411f010]=1,2,3. Separate multiple values with commas.
- `filter[valid]` in `query` (required: False) — Only return valid issues (=no empty type/subtype). Default value: undefined (meaning will return both valid & invalid issues).
- `limit` in `query` (required: False) — Return specified number of issues. Acceptable values are 1-100. Default value: 100.
- `offset` in `query` (required: False) — Return issues starting from the specified offset number. Default value: 0.
- `sortBy` in `query` (required: False) — Sort issue comments by specified fields. Separate multiple values with commas. To sort in descending order add a - (minus sign) before the sort criteria
- `fields` in `query` (required: False) — Return only specific fields in issue object. Separate multiple values with commas.

#### Responses
- **200**: OK
- **400**: Bad Request
- **403**: Forbidden
- **404**: Not Found

---

### 

**Endpoint:** `POST /construction/issues/v1/projects/{projectId}/issues`
**Operation ID:** `createIssue`

#### Description
Adds an issue to a project.

#### Parameters
- Ref: `#/components/parameters/x-ads-region`

#### Request Body
- Required: `False`
- Content-Type: `application/json`
  - Schema: `#/components/schemas/IssuePayload`

#### Responses
- **200**: OK
- **400**: Bad Request
- **403**: Forbidden
- **409**: Conflict

---

### Your GET endpoint

**Endpoint:** `GET /construction/issues/v1/projects/{projectId}/issues/{issueId}`
**Operation ID:** `getIssueDetails`

#### Description
Retrieves detailed information about a single issue. For general information about all the issues in a project.

#### Parameters
- Ref: `#/components/parameters/x-ads-region`

#### Responses
- **200**: OK
- **400**: Bad Request
- **403**: Forbidden
- **404**: Not Found

---

### 

**Endpoint:** `PATCH /construction/issues/v1/projects/{projectId}/issues/{issueId}`
**Operation ID:** `patchIssueDetails`

#### Description
Updates an issue.

To verify whether a user can update issues for a specific project, call GET users/me.

To verify which attributes the user can update, call GET issues/:id and check the permittedAttributes and permittedStatuses lists.

#### Parameters
- Ref: `#/components/parameters/x-ads-region`

#### Request Body
- Required: `False`
- Content-Type: `application/json`
  - Schema: `#/components/schemas/IssuePayload`

#### Responses
- **200**: OK
- **400**: Bad Request
- **403**: Forbidden
- **404**: Not Found

---

### Your GET endpoint

**Endpoint:** `GET /construction/issues/v1/projects/{projectId}/issues/{issueId}/comments`
**Operation ID:** `getComments`

#### Description
Get all the comments for a specific issue.

#### Parameters
- Ref: `#/components/parameters/x-ads-region`
- `limit` in `query` (required: False) — Add limit=20 to limit the results count (together with the offset to support pagination).
- `offset` in `query` (required: False) — Add offset=20 to get partial results (together with the limit to support pagination).
- `sortBy` in `query` (required: False) — Sort issue comments by specified fields. Separate multiple values with commas. To sort in descending order add a - (minus sign) before the sort criteria

#### Responses
- **200**: OK
- **400**: Bad Request
- **403**: Forbidden
- **404**: Not Found
- **500**: Internal Server Error

---

### 

**Endpoint:** `POST /construction/issues/v1/projects/{projectId}/issues/{issueId}/comments`
**Operation ID:** `CreateComments`

#### Description
Creates a new comment under a specific issue.

#### Parameters
- Ref: `#/components/parameters/x-ads-region`

#### Request Body
- Required: `False`
- Content-Type: `application/json`
  - Schema: `#/components/schemas/CommentsPayload`

#### Responses
- **201**: Created
- **400**: Bad Request
- **403**: Forbidden
- **404**: Not Found
- **409**: Conflict
- **500**: Internal Server Error

---

## Account Admin

_Generated from `admin.yaml`_

The Account Admin API automates creating and managing projects, assigning and managing project users, and managing member and partner company directories. You can also synchronize data with external systems.


---

### Get Project in account

**Endpoint:** `GET /construction/admin/v1/accounts/{accountId}/projects`
**Operation ID:** `getProjects`

#### Description
Retrieves a list of the projects in the specified account.

#### Parameters
- `Accept-Language` in `header` (required: False) — This header is not currently supported in the Account Admin API.
- `Region` in `header` (required: False) — The region where the bucket resides. Acceptable values: US, EMEA.
- `User-Id` in `header` (required: False) — Note that this header is not relevant for Account Admin GET endpoints. The ID of a user on whose behalf your API request is acting. Required if you’re using a 2-legged authentication context, which must be 2-legged OAuth2 security with user impersonation.  Your app has access to all users specified by the administrator in the SaaS integrations UI. Provide this header value to identify the user to be affected by the request.  You can use either the user’s ACC ID (id), or their Autodesk ID (autodeskId).
- `fields` in `query` (required: False) — A comma-separated list of the project fields to include in the response. Default value: all fields.
- `filter[classification]` in `query` (required: False) — A list of the classifications of projects to include in the response. Possible values: production, template, component, sample.
- `filter[platform]` in `query` (required: False) — Filter resource by platform. Possible values: acc and bim360.
- `filter[products]` in `query` (required: False) — A comma-separated list of the products that the returned projects must use. Only projects that use one or more of the listed products are returned.
- `filter[name]` in `query` (required: False) — A project name or name pattern to filter projects by. Can be a partial match based on the value of filterTextMatch that you provide; for example: filter[name]=ABCco filterTextMatch=startsWith.  Max length: 255
- `filter[type]` in `query` (required: False) — A list of project types to filter projects by. To exclude a project type from the response, prefix it with - (a hyphen); for example, -Bridge excludes bridge projects.
- `filter[status]` in `query` (required: False) — A list of the statuses of projects to include in the response. Possible values:  active pending archived suspended
- `filter[businessUnitId]` in `query` (required: False) — The ID of the business unit that returned projects must be associated with.
- `filter[jobNumber]` in `query` (required: False) — The user-defined identifier for a project to be returned. This ID was defined when the project was created. This filter accepts a partial match based on the value of filterTextMatch that you provide.
- `filter[updatedAt]` in `query` (required: False) — A range of dates during which the desired projects were updated. The range must be specified with dates in ISO 8601 format with time required. Separate multiple values with commas.
- `filterTextMatch` in `query` (required: False) — When filtering on a text-based field, this value indicates how to do the matching. Default value: contains. Possible values: contains, startsWith, endsWith and equals.
- `sort` in `query` (required: False) — A list of fields to sort the returned projects by. Multiple sort fields are applied in sequence order — each sort field produces groupings of projects with the same values of that field; the next sort field applies within the groupings produced by the previous sort field.
- `limit` in `query` (required: False) — The maximum number of records to return in a single request. Possible range: 1-200. Default value: 20.
- `offset` in `query` (required: False) — The record number that the returned page should start with. When the total number of records exceeds the value of limit, increase the offset value in subsequent requests to continue getting the remaining results.

#### Responses
- **200**: A list of requested projects.
- **400**: The request could not be understood by the server due to malformed syntax.
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Resource Not Found
- **406**: Not Acceptable
- **410**: Access to the target resource is no longer available.
- **429**: User has sent too many requests in a given amount of time.
- **500**: Internal Server Error
- **503**: Service Unavailable

---

### Create new Project

**Endpoint:** `POST /construction/admin/v1/accounts/{accountId}/projects`
**Operation ID:** `createProject`

#### Description
Creates a new project in the specified account. You can create the project directly, or clone the project from a project template.

#### Parameters
- `Accept-Language` in `header` (required: False) — This header is not currently supported in the Account Admin API.
- `Region` in `header` (required: False) — The region where the bucket resides. Acceptable values: US, EMEA.
- `User-Id` in `header` (required: False) — Note that this header is not relevant for Account Admin GET endpoints. The ID of a user on whose behalf your API request is acting. Required if you’re using a 2-legged authentication context, which must be 2-legged OAuth2 security with user impersonation.  Your app has access to all users specified by the administrator in the SaaS integrations UI. Provide this header value to identify the user to be affected by the request.  You can use either the user’s ACC ID (id), or their Autodesk ID (autodeskId).

#### Request Body
- Required: `False`
- Content-Type: `application/json`
  - Schema: `#/components/schemas/ProjectPayload`

#### Responses
- **202**: APS has received the request but not yet completed it.
- **400**: The request could not be understood by the server due to malformed syntax.
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Resource Not Found
- **406**: Not Acceptable
- **410**: Access to the target resource is no longer available.
- **415**: The server refuses to accept the request because the payload format is in an unsupported format.
- **429**: User has sent too many requests in a given amount of time.
- **500**: Internal Server Error
- **503**: Service Unavailable

---

### Get a project by ID

**Endpoint:** `GET /construction/admin/v1/projects/{projectId}`
**Operation ID:** `getProject`

#### Description
Retrieves a project specified by project ID.

#### Parameters
- `Accept-Language` in `header` (required: False) — This header is not currently supported in the Account Admin API.
- `Region` in `header` (required: False) — The region where the bucket resides. Acceptable values: US, EMEA.
- `User-Id` in `header` (required: False) — Note that this header is not relevant for Account Admin GET endpoints. The ID of a user on whose behalf your API request is acting. Required if you’re using a 2-legged authentication context, which must be 2-legged OAuth2 security with user impersonation.  Your app has access to all users specified by the administrator in the SaaS integrations UI. Provide this header value to identify the user to be affected by the request.  You can use either the user’s ACC ID (id), or their Autodesk ID (autodeskId).
- `fields` in `query` (required: False) — A comma-separated list of the project fields to include in the response. Default value: all fields.

#### Responses
- **200**: A list of requested projects.
- **400**: The request could not be understood by the server due to malformed syntax.
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Resource Not Found
- **406**: Not Acceptable
- **407**: Proxy Authentication Required
- **410**: Access to the target resource is no longer available.
- **429**: User has sent too many requests in a given amount of time.
- **500**: Internal Server Error
- **503**: Service Unavailable

---

### Create or update a project’s image

**Endpoint:** `PATCH /hq/v1/accounts/{account_id}/projects/{project_id}/image`
**Operation ID:** `createProjectImage`

#### Description
Create or update a project’s image.

#### Parameters
- `Region` in `header` (required: False) — The geographic area where the data is stored. Acceptable values: US, EMEA. By default, it is set to US.

#### Request Body
- Required: `False`
- Content-Type: `application/x-www-form-urlencoded`

#### Responses
- **200**: A list of requested projects.
- **400**: The request could not be understood by the server due to malformed syntax.
- **403**: Forbidden
- **404**: Resource Not Found
- **409**: Conflict
- **422**: The request was unable to be followed due to restrictions.
- **500**: Internal Server Error

---

### Get all companies in an account

**Endpoint:** `GET /hq/v1/accounts/{account_id}/companies`
**Operation ID:** `getCompanies`

#### Description
Query all the partner companies in a specific BIM 360 account.
Note that this endpoint is compatible with both BIM 360 and Autodesk Construction Cloud (ACC) projects.

#### Parameters
- `Region` in `header` (required: False) — The geographic area where the data is stored. Acceptable values: US, EMEA. By default, it is set to US.
- `limit` in `query` (required: False) — Response array’s size Default value: 10 Max limit: 100
- `offset` in `query` (required: False) — Offset of response array Default value: 0
- `sort` in `query` (required: False) — Comma-separated fields to sort by in ascending order  Prepending a field with - sorts in descending order Invalid fields and whitespaces will be ignored
- `field` in `query` (required: False) — Comma-separated fields to include in response  id will always be returned Invalid fields will be ignored

#### Responses
- **200**: The request has succeeded
- **400**: The request could not be understood by the server due to malformed syntax.
- **403**: Forbidden
- **404**: Resource Not Found
- **409**: The request could not be completed due to a conflict with the current state of the resource
- **422**: The request was unable to be followed due to restrictions.
- **500**: Internal Server Error

---

### Create a new partner company

**Endpoint:** `POST /hq/v1/accounts/{account_id}/companies`
**Operation ID:** `createCompany`

#### Description
Create a new partner company.
Note that this endpoint is compatible with both BIM 360 and Autodesk Construction Cloud (ACC) projects.

#### Parameters
- `Region` in `header` (required: False) — The geographic area where the data is stored. Acceptable values: US, EMEA. By default, it is set to US.

#### Request Body
- Required: `False`
- Content-Type: `application/json`
  - Schema: `#/components/schemas/CompanyPayload`

#### Responses
- **201**: A new resource has been successfully created.
- **400**: The request could not be understood by the server due to malformed syntax.
- **403**: Forbidden
- **404**: Resource Not Found
- **409**: The request could not be completed due to a conflict with the current state of the resource
- **422**: The request was unable to be followed due to restrictions.
- **500**: Internal Server Error

---

### Bulk import partner companies

**Endpoint:** `POST /hq/v1/accounts/{account_id}/companies/import`
**Operation ID:** `importCompanies`

#### Description
Bulk import partner companies to the company directory in a specific BIM 360 account. (50 companies maximum can be included in each call.)
Note that this endpoint is compatible with both BIM 360 and Autodesk Construction Cloud (ACC) projects.

#### Parameters
- `Region` in `header` (required: False) — The geographic area where the data is stored. Acceptable values: US, EMEA. By default, it is set to US.

#### Request Body
- Required: `False`
- Content-Type: `application/json`

#### Responses
- **201**: A new resource has been successfully created.
- **400**: The request could not be understood by the server due to malformed syntax.
- **403**: Forbidden
- **404**: Resource Not Found
- **409**: The request could not be completed due to a conflict with the current state of the resource
- **422**: The request was unable to be followed due to restrictions.
- **500**: Internal Server Error

---

### Get details of a company

**Endpoint:** `GET /hq/v1/accounts/{account_id}/companies/{company_id}`
**Operation ID:** `getCompany`

#### Description
Query the details of a specific partner company.

#### Parameters
- `Region` in `header` (required: False) — The geographic area where the data is stored. Acceptable values: US, EMEA. By default, it is set to US.

#### Responses
- **200**: The request has succeeded
- **400**: The request could not be understood by the server due to malformed syntax.
- **403**: Forbidden
- **404**: Resource Not Found
- **409**: The request could not be completed due to a conflict with the current state of the resource
- **422**: The request was unable to be followed due to restrictions.
- **500**: Internal Server Error

---

### Update the properties of company

**Endpoint:** `PATCH /hq/v1/accounts/{account_id}/companies/{company_id}`
**Operation ID:** `patchCompanyDetails`

#### Description
Update the properties of only the specified attributes of a specific partner company.

#### Parameters
- `Region` in `header` (required: False) — The geographic area where the data is stored. Acceptable values: US, EMEA. By default, it is set to US.

#### Request Body
- Required: `False`
- Content-Type: `application/json`
  - Schema: `#/components/schemas/CompanyPatchPayload`

#### Responses
- **200**: The request has succeeded
- **400**: The request could not be understood by the server due to malformed syntax.
- **403**: Forbidden
- **404**: Resource Not Found
- **409**: The request could not be completed due to a conflict with the current state of the resource
- **422**: The request was unable to be followed due to restrictions.
- **500**: Internal Server Error

---

### Create or update a company’s image

**Endpoint:** `PATCH /hq/v1/accounts/{account_id}/companies/{company_id}/image`
**Operation ID:** `patchCompanyImage`

#### Description
Create or update a specific partner company’s image.

#### Parameters
- `Region` in `header` (required: False) — The geographic area where the data is stored. Acceptable values: US, EMEA. By default, it is set to US.

#### Request Body
- Required: `False`
- Content-Type: `application/x-www-form-urlencoded`

#### Responses
- **200**: The request has succeeded
- **400**: The request could not be understood by the server due to malformed syntax.
- **403**: Forbidden
- **404**: Resource Not Found
- **409**: The request could not be completed due to a conflict with the current state of the resource
- **422**: The request was unable to be followed due to restrictions.
- **500**: Internal Server Error

---

### Search companies in account by name

**Endpoint:** `GET /hq/v1/accounts/{account_id}/companies/search`
**Operation ID:** `searchCompanies`

#### Description
Search partner companies in a specific BIM 360 account by name.
Note that this endpoint is compatible with both BIM 360 and Autodesk Construction Cloud (ACC) projects.

#### Parameters
- `Region` in `header` (required: False) — The geographic area where the data is stored. Acceptable values: US, EMEA. By default, it is set to US.
- `name` in `query` (required: False) — Company name to match Max length: 255
- `trade` in `query` (required: False) — Company trade to match Max length: 255
- `operator` in `query` (required: False) — Boolean operator to use: OR (default) or AND
- `partial` in `query` (required: False) — If true (default), perform a fuzzy match
- `limit` in `query` (required: False) — Response array’s size Default value: 10 Max limit: 100
- `offset` in `query` (required: False) — Offset of response array Default value: 0
- `sort` in `query` (required: False) — Comma-separated fields to sort by in ascending order
- `field` in `query` (required: False) — Comma-separated fields to include in response

#### Responses
- **200**: The request has succeeded
- **400**: The request could not be understood by the server due to malformed syntax.
- **403**: Forbidden
- **404**: Resource Not Found
- **409**: The request could not be completed due to a conflict with the current state of the resource
- **422**: The request was unable to be followed due to restrictions.
- **500**: Internal Server Error

---

### Get all companies in a project

**Endpoint:** `GET /hq/v1/accounts/{account_id}/projects/{project_id}/companies`
**Operation ID:** `getProjectCompanies`

#### Description
Query all the partner companies in a specific BIM 360 project.
Note that this endpoint is compatible with both BIM 360 and Autodesk Construction Cloud (ACC) projects.

#### Parameters
- `Region` in `header` (required: False) — The geographic area where the data is stored. Acceptable values: US, EMEA. By default, it is set to US.
- `limit` in `query` (required: False) — Response array’s size Default value: 10 Max limit: 100
- `offset` in `query` (required: False) — Offset of response array Default value: 0
- `sort` in `query` (required: False) — Comma-separated fields to sort by in ascending order
- `field` in `query` (required: False) — Comma-separated fields to include in response

#### Responses
- **200**: The request has succeeded
- **400**: The request could not be understood by the server due to malformed syntax.
- **403**: Forbidden
- **404**: Resource Not Found
- **409**: The request could not be completed due to a conflict with the current state of the resource
- **422**: The request was unable to be followed due to restrictions.
- **500**: Internal Server Error

---

### Get account users

**Endpoint:** `GET /hq/v1/accounts/{account_id}/users`
**Operation ID:** `getUsers`

#### Description
Query all the users in a specific BIM 360 account.

#### Parameters
- `Region` in `header` (required: False) — The geographic area where the data is stored. Acceptable values: US, EMEA. By default, it is set to US.
- `limit` in `query` (required: False) — Response array’s size Default value: 10 Max limit: 100
- `offset` in `query` (required: False) — Offset of response array Default value: 0
- `sort` in `query` (required: False) — Comma-separated fields to sort by in ascending order
- `field` in `query` (required: False) — Comma-separated fields to include in response

#### Responses
- **200**: The request has succeeded
- **400**: The request could not be understood by the server due to malformed syntax.
- **403**: Forbidden
- **404**: Resource Not Found
- **409**: The request could not be completed due to a conflict with the current state of the resource
- **422**: The request was unable to be followed due to restrictions.
- **500**: Internal Server Error

---

### Create User

**Endpoint:** `POST /hq/v1/accounts/{account_id}/users`
**Operation ID:** `createUser`

#### Description
Create a new user in the BIM 360 member directory.

#### Parameters
- `Region` in `header` (required: False) — The geographic area where the data is stored. Acceptable values: US, EMEA. By default, it is set to US.

#### Request Body
- Required: `False`
- Content-Type: `application/json`
  - Schema: `#/components/schemas/UserPayload`

#### Responses
- **201**: A new resource has been successfully created.
- **400**: The request could not be understood by the server due to malformed syntax.
- **403**: Forbidden
- **404**: Resource Not Found
- **409**: The request could not be completed due to a conflict with the current state of the resource
- **422**: The request was unable to be followed due to restrictions.
- **500**: Internal Server Error

---

### Bulk import users

**Endpoint:** `POST /hq/v1/accounts/{account_id}/users/import`
**Operation ID:** `importUsers`

#### Description
Bulk import users to the master member directory in a BIM 360 account. (50 users maximum can be included in each call.)

#### Parameters
- `Region` in `header` (required: False) — The geographic area where the data is stored. Acceptable values: US, EMEA. By default, it is set to US.

#### Request Body
- Required: `False`
- Content-Type: `application/json`

#### Responses
- **201**: A new resource has been successfully created.
- **400**: The request could not be understood by the server due to malformed syntax.
- **403**: Forbidden
- **404**: Resource Not Found
- **409**: The request could not be completed due to a conflict with the current state of the resource
- **422**: The request was unable to be followed due to restrictions.
- **500**: Internal Server Error

---

### Get the details of a user

**Endpoint:** `GET /hq/v1/accounts/{account_id}/users/{user_id}`
**Operation ID:** `getUser`

#### Description
Query the details of a specific user.

#### Parameters
- `Region` in `header` (required: False) — The geographic area where the data is stored. Acceptable values: US, EMEA. By default, it is set to US.

#### Responses
- **200**: The request has succeeded
- **400**: The request could not be understood by the server due to malformed syntax.
- **403**: Forbidden
- **404**: Resource Not Found
- **409**: The request could not be completed due to a conflict with the current state of the resource
- **422**: The request was unable to be followed due to restrictions.
- **500**: Internal Server Error

---

### Update User

**Endpoint:** `PATCH /hq/v1/accounts/{account_id}/users/{user_id}`
**Operation ID:** `patchUserDetails`

#### Description
Update a specific user’s status or default company.

#### Parameters
- `Region` in `header` (required: False) — The geographic area where the data is stored. Acceptable values: US, EMEA. By default, it is set to US.

#### Request Body
- Required: `False`
- Content-Type: `application/json`
  - Schema: `#/components/schemas/UserPatchPayload`

#### Responses
- **200**: The request has succeeded
- **400**: The request could not be understood by the server due to malformed syntax.
- **403**: Forbidden
- **404**: Resource Not Found
- **409**: The request could not be completed due to a conflict with the current state of the resource
- **422**: The request was unable to be followed due to restrictions.
- **500**: Internal Server Error

---

### Search Users

**Endpoint:** `GET /hq/v1/accounts/{account_id}/users/search`
**Operation ID:** `searchUsers`

#### Description
Search users in the master member directory of a specific BIM 360 account by specified fields.

#### Parameters
- `Region` in `header` (required: False) — The geographic area where the data is stored. Acceptable values: US, EMEA. By default, it is set to US.
- `name` in `query` (required: False) — User name to match Max length: 255
- `email` in `query` (required: False) — User email to match Max length: 255
- `company_name` in `query` (required: False) — User company to match Max length: 255
- `operator` in `query` (required: False) — Boolean operator to use: OR (default) or AND
- `partial` in `query` (required: False) — If true (default), perform a fuzzy match
- `limit` in `query` (required: False) — Response array’s size Default value: 10 Max limit: 100
- `offset` in `query` (required: False) — Offset of response array Default value: 0
- `sort` in `query` (required: False) — Comma-separated fields to sort by in ascending order
- `field` in `query` (required: False) — Comma-separated fields to include in response

#### Responses
- **200**: The request has succeeded
- **400**: The request could not be understood by the server due to malformed syntax.
- **403**: Forbidden
- **404**: Resource Not Found
- **409**: The request could not be completed due to a conflict with the current state of the resource
- **422**: The request was unable to be followed due to restrictions.
- **500**: Internal Server Error

---

### Get project users

**Endpoint:** `GET /construction/admin/v1/projects/{projectId}/users`
**Operation ID:** `getProjectUsers`

#### Description
Retrieves information about a filtered subset of users in the specified project.

There are two primary reasons to do this:

To verify that all users assigned to the project have been activated as members of the project.
To check other information about users, such as their project user ID, roles, and products.
Note that if you want to retrieve information about users associated with a particular Autodesk account, call the GET users endpoint.

#### Parameters
- `Accept-Language` in `header` (required: False) — This header is not currently supported in the Account Admin API.
- `Region` in `header` (required: False) — The region where the bucket resides. Acceptable values: US, EMEA.
- `User-Id` in `header` (required: False) — Note that this header is not relevant for Account Admin GET endpoints. The ID of a user on whose behalf your API request is acting. Required if you’re using a 2-legged authentication context, which must be 2-legged OAuth2 security with user impersonation.  Your app has access to all users specified by the administrator in the SaaS integrations UI. Provide this header value to identify the user to be affected by the request.  You can use either the user’s ACC ID (id), or their Autodesk ID (autodeskId).
- `filter[products]` in `query` (required: False) — A comma-separated list of the products that the returned projects must use. Only projects that use one or more of the listed products are returned.
- `filter[name]` in `query` (required: False) — A user name or name pattern to filter users by. Can be a partial match based on the value of filterTextMatch that you provide; for example: filter[name]=ABCco filterTextMatch=startsWith.  Max length: 255
- `filter[email]` in `query` (required: False) — A user email address or address pattern that the returned users must have. This can be a partial match based on the value of filterTextMatch that you provide. For example:  filter[email]=sample filterTextMatch=startsWith  Max length: 255
- `filter[status]` in `query` (required: False) — A list of statuses that the returned project users must be in. The default values are active and pending.
- `filter[accessLevels]` in `query` (required: False) — A list of user access levels that the returned users must have.
- `filter[companyId]` in `query` (required: False) — The ID of a company that the returned users must represent.
- `filter[companyName]` in `query` (required: False) — The name of a company that returned users must be associated with. Can be a partial match based on the value of filterTextMatch that you provide. For example: filter[companyName]=Sample filterTextMatch=startsWith  Max length: 255
- `filter[autodeskId]` in `query` (required: False) — A list of the Autodesk IDs of users to retrieve.
- `filter[id]` in `query` (required: False) — A list of the ACC IDs of users to retrieve.
- `filter[roleId]` in `query` (required: False) — The ID of a user role that the returned users must have. To obtain a role ID for this filter, you can inspect the roleId field in previous responses to this endpoint or to the GET projects/:projectId/users/:userId endpoint.  Max length: 255
- `filter[roleIds]` in `query` (required: False) — A list of the IDs of user roles that the returned users must have. To obtain a role ID for this filter, you can inspect the roleId field in previous responses to this endpoint or to the GET projects/:projectId/users/:userId endpoint.
- `sort` in `query` (required: False) — A list of fields to sort the returned users by. Multiple sort fields are applied in sequence order — each sort field produces groupings of projects with the same values of that field; the next sort field applies within the groupings produced by the previous sort field.
- `fields` in `query` (required: False) — A list of the project fields to include in the response. Default value: all fields.
- `orFilters` in `query` (required: False) — A list of user fields to combine with the SQL OR operator for filtering the returned project users. The OR is automatically incorporated between the fields; any one of them can produce a valid match.
- `filterTextMatch` in `query` (required: False) — When filtering on a text-based field, this value indicates how to do the matching. Default value: contains. Possible values: contains, startsWith, endsWith and equals.
- `limit` in `query` (required: False) — The maximum number of records to return in a single request. Possible range: 1-200. Default value: 20.
- `offset` in `query` (required: False) — The record number that the returned page should start with. When the total number of records exceeds the value of limit, increase the offset value in subsequent requests to continue getting the remaining results.

#### Responses
- **200**: A list of requested project users.
- **400**: The request could not be understood by the server due to malformed syntax.
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Resource Not Found
- **406**: Not Acceptable
- **410**: Access to the target resource is no longer available.
- **429**: User has sent too many requests in a given amount of time.
- **500**: Internal Server Error
- **503**: Service Unavailable

---

### Assigns a user to the specified project

**Endpoint:** `POST /construction/admin/v1/projects/{projectId}/users`
**Operation ID:** `assignProjectUser`

#### Description
Assigns a user to the specified project.

#### Parameters
- `Accept-Language` in `header` (required: False) — This header is not currently supported in the Account Admin API.
- `Region` in `header` (required: False) — The region where the bucket resides. Acceptable values: US, EMEA.
- `User-Id` in `header` (required: False) — Note that this header is not relevant for Account Admin GET endpoints. The ID of a user on whose behalf your API request is acting. Required if you’re using a 2-legged authentication context, which must be 2-legged OAuth2 security with user impersonation.  Your app has access to all users specified by the administrator in the SaaS integrations UI. Provide this header value to identify the user to be affected by the request.  You can use either the user’s ACC ID (id), or their Autodesk ID (autodeskId).

#### Request Body
- Required: `False`
- Content-Type: `application/json`
  - Schema: `#/components/schemas/ProjectUserPayload`

#### Responses
- **201**: Successfully added the user to the project.
- **400**: The request could not be understood by the server due to malformed syntax.
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Resource Not Found
- **406**: Not Acceptable
- **410**: Access to the target resource is no longer available.
- **412**: The server refuses to accept the request because a pre-condition failed.
- **415**: The server refuses to accept the request because the payload format is in an unsupported format.
- **429**: User has sent too many requests in a given amount of time.
- **500**: Internal Server Error
- **503**: Service Unavailable

---

### Assigns multiple users to a project

**Endpoint:** `POST /construction/admin/v2/projects/{projectId}/users:import`
**Operation ID:** `importProjectUsers`

#### Description
Assigns multiple users to a project at once. This endpoint can assign up to 200 users per request.

#### Parameters
- `Accept-Language` in `header` (required: False) — This header is not currently supported in the Account Admin API.
- `Region` in `header` (required: False) — The region where the bucket resides. Acceptable values: US, EMEA.
- `User-Id` in `header` (required: False) — Note that this header is not relevant for Account Admin GET endpoints. The ID of a user on whose behalf your API request is acting. Required if you’re using a 2-legged authentication context, which must be 2-legged OAuth2 security with user impersonation.  Your app has access to all users specified by the administrator in the SaaS integrations UI. Provide this header value to identify the user to be affected by the request.  You can use either the user’s ACC ID (id), or their Autodesk ID (autodeskId).

#### Request Body
- Required: `False`
- Content-Type: `application/json`
  - Schema: `#/components/schemas/ProjectUsersImportPayload`

#### Responses
- **202**: The request has been received but not yet acted upon.
- **400**: The request could not be understood by the server due to malformed syntax.
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Resource Not Found
- **406**: Not Acceptable
- **410**: Access to the target resource is no longer available.
- **412**: The server refuses to accept the request because a pre-condition failed.
- **415**: The server refuses to accept the request because the payload format is in an unsupported format.
- **429**: User has sent too many requests in a given amount of time.
- **500**: Internal Server Error
- **503**: Service Unavailable

---

### Get project user

**Endpoint:** `GET /construction/admin/v1/projects/{projectId}/users/{userId}`
**Operation ID:** `getProjectUser`

#### Description
Retrieves detailed information about the specified user in a project.

There are two primary reasons to do this:

To verify that a user assigned to the specified project has been activated as a member of the project.
To check other information about the user, such as their project user ID, roles, and products.

#### Parameters
- `Accept-Language` in `header` (required: False) — This header is not currently supported in the Account Admin API.
- `Region` in `header` (required: False) — The region where the bucket resides. Acceptable values: US, EMEA.
- `User-Id` in `header` (required: False) — Note that this header is not relevant for Account Admin GET endpoints. The ID of a user on whose behalf your API request is acting. Required if you’re using a 2-legged authentication context, which must be 2-legged OAuth2 security with user impersonation.  Your app has access to all users specified by the administrator in the SaaS integrations UI. Provide this header value to identify the user to be affected by the request.  You can use either the user’s ACC ID (id), or their Autodesk ID (autodeskId).
- `fields` in `query` (required: False) — A comma-separated list of the project fields to include in the response. Default value: all fields.

#### Responses
- **200**: Information about the requested project user.
- **400**: The request could not be understood by the server due to malformed syntax.
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Resource Not Found
- **406**: Not Acceptable
- **410**: Access to the target resource is no longer available.
- **429**: User has sent too many requests in a given amount of time.
- **500**: Internal Server Error
- **503**: Service Unavailable

---

### Update user in project

**Endpoint:** `PATCH /construction/admin/v1/projects/{projectId}/users/{userId}`
**Operation ID:** `updateProjectUser`

#### Description
Updates information about the specified user in a project.

Note that the Authorization header token can be obtained either via a three-legged OAuth flow, or via a two-legged Oauth flow with user impersonation, for which the User-Id header is also required.

#### Parameters
- `Accept-Language` in `header` (required: False) — This header is not currently supported in the Account Admin API.
- `Region` in `header` (required: False) — The region where the bucket resides. Acceptable values: US, EMEA.
- `User-Id` in `header` (required: False) — Note that this header is not relevant for Account Admin GET endpoints. The ID of a user on whose behalf your API request is acting. Required if you’re using a 2-legged authentication context, which must be 2-legged OAuth2 security with user impersonation.  Your app has access to all users specified by the administrator in the SaaS integrations UI. Provide this header value to identify the user to be affected by the request.  You can use either the user’s ACC ID (id), or their Autodesk ID (autodeskId).

#### Request Body
- Required: `False`
- Content-Type: `application/json`
  - Schema: `#/components/schemas/ProjectUsersUpdatePayload`

#### Responses
- **201**: The project user was successfully updated. The response includes only the fields being updated along with the ACC ID of the user.
- **400**: The request could not be understood by the server due to malformed syntax.
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Resource Not Found
- **406**: Not Acceptable
- **410**: Access to the target resource is no longer available.
- **412**: The server refuses to accept the request because a pre-condition failed.
- **415**: The server refuses to accept the request because the payload format is in an unsupported format.
- **429**: User has sent too many requests in a given amount of time.
- **500**: Internal Server Error
- **503**: Service Unavailable

---

### Remove Project User

**Endpoint:** `DELETE /construction/admin/v1/projects/{projectId}/users/{userId}`
**Operation ID:** `removeProjectUser`

#### Description
Removes the specified user from a project.

Note that the Authorization header token can be obtained either via a three-legged OAuth flow, or via a two-legged Oauth flow with user impersonation, for which the User-Id header is also required.

#### Parameters
- `Accept-Language` in `header` (required: False) — This header is not currently supported in the Account Admin API.
- `Region` in `header` (required: False) — The region where the bucket resides. Acceptable values: US, EMEA.
- `User-Id` in `header` (required: False) — Note that this header is not relevant for Account Admin GET endpoints. The ID of a user on whose behalf your API request is acting. Required if you’re using a 2-legged authentication context, which must be 2-legged OAuth2 security with user impersonation.  Your app has access to all users specified by the administrator in the SaaS integrations UI. Provide this header value to identify the user to be affected by the request.  You can use either the user’s ACC ID (id), or their Autodesk ID (autodeskId).

#### Responses
- **204**: The request has succeeded, no content returned.
- **400**: The request could not be understood by the server due to malformed syntax.
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Resource Not Found
- **410**: Access to the target resource is no longer available.
- **415**: The server refuses to accept the request because the payload format is in an unsupported format.
- **429**: User has sent too many requests in a given amount of time.
- **500**: Internal Server Error
- **503**: Service Unavailable

---

### Get Business Units

**Endpoint:** `GET /hq/v1/accounts/{account_id}/business_units_structure`
**Operation ID:** `getBusinessUnits`

#### Description
Query all the business units in a specific BIM 360 account.

#### Parameters
- `Region` in `header` (required: False) — The geographic area where the data is stored. Acceptable values: US, EMEA. By default, it is set to US.

#### Responses
- **200**: The request has succeeded
- **400**: The request could not be understood by the server due to malformed syntax.
- **403**: Forbidden
- **404**: Resource Not Found
- **409**: The request could not be completed due to a conflict with the current state of the resource.
- **422**: The request was unable to be followed due to restrictions
- **500**: An unexpected error occurred on the server

---

### Create Business Units

**Endpoint:** `PUT /hq/v1/accounts/{account_id}/business_units_structure`
**Operation ID:** `createBusinessUnits`

#### Description
Query all the business units in a specific BIM 360 account.

#### Parameters
- `Region` in `header` (required: False) — The geographic area where the data is stored. Acceptable values: US, EMEA. By default, it is set to US.

#### Request Body
- Required: `False`
- Content-Type: `application/json`
  - Schema: `#/components/schemas/BusinessUnitsRequestPyload`

#### Responses
- **200**: The request has succeeded
- **400**: The request could not be understood by the server due to malformed syntax.
- **403**: Forbidden
- **404**: Resource Not Found
- **409**: The request could not be completed due to a conflict with the current state of the resource.
- **422**: The request was unable to be followed due to restrictions
- **500**: An unexpected error occurred on the server

---

## Authentication

_Generated from `authentication.yaml`_

OAuth2 token management APIs.

---

### Authorize User

**Endpoint:** `GET /authentication/v2/authorize`
**Operation ID:** `authorize`

#### Description
Returns a browser URL to redirect an end user in order to acquire the user’s consent to authorize the application to access resources on their behalf.

Invoking this operation is the first step in authenticating users and retrieving an authorization code grant. The authorization code that is generated remains valid for 5 minutes, while the ID token stays valid for 60 minutes. Any access tokens you obtain are valid for 60 minutes, and refresh tokens remain valid for 15 days.

This operation has a rate limit of 500 calls per minute.

**Note:** This operation is intended for use with client-side applications only. It is not suitable for server-side applications.

#### Parameters
- `client_id` in `query` (required: True) — The Client ID of the calling application, as registered with APS.
- `response_type` in `query` (required: True) — The type of response you want to receive. Possible values are: 

-  ``code`` - Authorization code grant.
-  ``id_token`` - OpenID Connect ID token.
- `redirect_uri` in `query` (required: True) — The URI that APS redirects users to after they grant or deny access permission to the application. Must match the Callback URL for the application as registered with APS.

Must be specified as a URL-safe string. It can include query parameters or any other valid URL construct.
- `nonce` in `query` (required: False) — A random string that is sent with the request. APS passes back the same string to you so that you can verify whether you received the same string that you sent. This check mitigates token replay attacks
- `state` in `query` (required: False) — A URL-encoded random string. The authorization flow will pass the same string back to the Callback URL using the ``state`` query string parameter. This process helps ensure that the callback you receive is a response to what you originally requested. It prevents malicious actors from forging requests.

The string can only contain alphanumeric characters, commas, periods, underscores, and hyphens.
- `scope` in `query` (required: False) — A URL-encoded space-delimited list of requested scopes. See the `Developer's Guide documentation on scopes </en/docs/oauth/v2/developers_guide/scopes/>`_ for a list of valid values you can provide.

The string you specify for this parameter must not exceed 2000 characters and it cannot contain more than 50 scopes.
- `response_mode` in `query` (required: False) — Specifies how the authorization response should be returned. Valid values are:

- ``fragment`` - Encode the response parameters in the fragment of the redirect URI. A fragment in a URI is the optional part of the URI that appears after a ``#`` symbol, which refers to a specific section within a resource. For example, ``section`` in ``https://www.mysite.org/myresource#section``.
- ``form_post`` - Embed the authorization response parameter in an HTML form.
- ``query`` -  Embed the authorization response as a query string parameter of the redirect URI. 

If ``id_token`` is stated as ``response_type``,  only ``form_post`` is allowed as ``response_mode``.'
- `prompt` in `query` (required: False) — Specifies how to prompt users for authentication. Possible values are: 

- ``login`` : Always prompt the user for authentication, regardless of the state of the login session. 

**Note:** If you do not specify this parameter, the system will not prompt the user for authentication as long as a login session is active. If a login session is not active, the system will prompt the user for authentication.
- `authoptions` in `query` (required: False) — A JSON object containing options that specify how to display the sign-in page. Refer the `Developer's Guide documentation on AuthOptions </en/docs/oauth/v2/developers_guide/authoptions/>`_ for supported values.
- `code_challenge` in `query` (required: False) — A URL-encoded string derived from the code verifier sent in the authorization request with the Proof Key for Code Exchange (PKCE) grant flow.
- `code_challenge_method` in `query` (required: False) — The method used to derive the code challenge for the PKCE grant flow. Possible value is:

- ``S256``- Hashes the code verifier using the SHA-256 algorithm and then applies Base64 URL encoding.

#### Responses
- **302**: Successfully redirected to the redirect URI.

---

### Revoke Token

**Endpoint:** `POST /authentication/v2/revoke`
**Operation ID:** `revoke`

#### Description
Revokes an active access token or refresh token.

An application can only revoke its own tokens.

This operation has a rate limit of 100 calls per minute.

#### Request Body
- Required: `True`
- Content-Type: `application/x-www-form-urlencoded`
- Content-Type: `application/json`

#### Responses
- **200**: The token was successfully revoked. This operation has no response body.

---

### Get JWKS

**Endpoint:** `GET /authentication/v2/keys`
**Operation ID:** `get-keys`

#### Description
Returns a set of public keys in the JSON Web Key Set (JWKS) format.

Public keys returned by this operation can be used to validate the asymmetric JWT signature of an access token without making network calls. It can be used to validate both two-legged access tokens and three-legged access tokens. 

See the Developer's Guide topic on `Asymmetric Signing </en/docs/oauth/v2/developers_guide/asymmetric-encryption/>`_ for more information.

#### Responses
- **200**: A set of public keys in the JWKS format was returned successfully.

---

### Acquire Token

**Endpoint:** `POST /authentication/v2/token`
**Operation ID:** `fetch-token`

#### Description
Returns an access token or refresh token.

* If `grant_type` is `authorization_code`, returns a 3-legged access token for authorization code grant. 
* If `grant_type` is `client_credentials`, returns a 2-legged access token for client credentials grant.
* If `grant_type` is `refresh_token`, returns new access token using the refresh token provided in the request.

Traditional Web Apps and Server-to-Server Apps should use the ``Authorization`` header with Basic Authentication for this operation. Desktop, Mobile, and Single-Page Apps should use ``client_id`` in the form body instead.

This operation has a rate limit of 500 calls per minute.

#### Parameters
- Ref: `#/components/parameters/Authorization`

#### Request Body
- Required: `False`
- Content-Type: `application/x-www-form-urlencoded`
- Content-Type: `application/json`

#### Responses
- **200**: An access token was successfully returned.

---

### Introspect Token

**Endpoint:** `POST /authentication/v2/introspect`
**Operation ID:** `introspect_token`

#### Description
Returns metadata about the specified access token or reference token.

An application can only introspect its own tokens.

This operation has a rate limit of 500 calls per minute.

#### Parameters
- Ref: `#/components/parameters/Authorization`

#### Request Body
- Required: `False`
- Content-Type: `application/x-www-form-urlencoded`

#### Responses
- **200**: Metadata was successfully returned.

---

### Get OIDC Specification

**Endpoint:** `GET /.well-known/openid-configuration`
**Operation ID:** `get-oidc-spec`

#### Description
Returns an OpenID Connect Discovery Specification compliant JSON document. It contains a list of the OpenID/OAuth endpoints, supported scopes, claims, public keys used to sign the tokens, and other details.

#### Responses
- **200**: The OIDC specification was successfully returned.

---

### Logout

**Endpoint:** `GET /authentication/v2/logout`
**Operation ID:** `logout`

#### Description
Signs out the currently authenticated user from the APS authorization server. Thereafter, this operation redirects the user to the ``post_logout_redirect_uri``, or to the Autodesk Sign-in page when no ``post_logout_redirect_uri`` is provided.

This operation has a rate limit of 500 calls per minute.

#### Parameters
- `post_logout_redirect_uri` in `query` (required: False) — The URI to redirect your users to once logout is performed. If you do not specify this parameter your users are redirected to the Autodesk Sign-in page. 

**Note:**  You must provide a redirect URI that is pre-registered with APS. This precaution is taken to prevent unauthorized applications from hijacking the logout process.

#### Responses
- **302**: The user was successfully logged out.

---

### Get User Info

**Endpoint:** `GET /userinfo`
**Operation ID:** `get-user-info`

#### Description
Retrieves information about the authenticated user.

#### Responses
- **200**: Information about the currently logged in user was successfully returned.

---

## Data Management API

_Generated from `datamanagement.yaml`_

The Data Management API provides a unified and consistent way to access data across BIM 360 Team, Fusion Team (formerly known as A360 Team), BIM 360 Docs, A360 Personal, and the Object Storage Service.

With this API, you can accomplish a number of workflows, including accessing a Fusion model in Fusion Team and getting an ordered structure of items, IDs, and properties for generating a bill of materials in a 3rd-party process. Or, you might want to superimpose a Fusion model and a building model to use in the Viewer.

---

### List Hubs

**Endpoint:** `GET /project/v1/hubs`
**Operation ID:** `getHubs`

#### Description
Returns a collection of hubs that the user of your app can access.

The returned hubs can be BIM 360 Team hubs, Fusion Team hubs (formerly known as A360 Team hubs), A360 Personal hubs, ACC Docs (Autodesk Docs) accounts, or BIM 360 Docs accounts. Only active hubs are returned.

For BIM 360 Docs and ACC Docs, a hub ID corresponds to an Account ID. To convert a BIM 360 or ACC Account ID to a hub ID, prefix the Account ID with ``b.``. For example, an Account ID of ```c8b0c73d-3ae9``` translates to a hub ID of ``b.c8b0c73d-3ae9``.

**Note:** This operation supports Autodesk Construction Cloud (ACC) Projects. For more information, see the [ACC Platform API documentation](https://en.docs.acc.v1/overview/introduction/).

#### Parameters
- Ref: `#/components/parameters/x-user-id`
- Ref: `#/components/parameters/filter_id`
- Ref: `#/components/parameters/filter_name`
- Ref: `#/components/parameters/filter_extension_type`

#### Responses
- **200**: The list of hubs was successfully retrieved.

---

### Get a Hub

**Endpoint:** `GET /project/v1/hubs/{hub_id}`
**Operation ID:** `getHub`

#### Description
Returns the hub specified by the ``hub_id`` parameter.

For BIM 360 Docs, a hub ID corresponds to a BIM 360 account ID. To convert a BIM 360 account ID to a hub ID, prefix the account ID with ``b.``. For example, an account ID of ```c8b0c73d-3ae9``` translates to a hub ID of ``b.c8b0c73d-3ae9``.

**Note:** This operation supports Autodesk Construction Cloud (ACC) Projects. For more information, see the [ACC Platform API documentation](https://en.docs.acc.v1/overview/introduction/).

#### Parameters
- Ref: `#/components/parameters/x-user-id`

#### Responses
- **200**: The hub was successfully retrieved.

---

### Get Projects

**Endpoint:** `GET /project/v1/hubs/{hub_id}/projects`
**Operation ID:** `getHubProjects`

#### Description
Returns a collection of active projects within the specified hub. The returned projects can be Autodesk Construction Cloud (ACC), BIM 360, BIM 360 Team, Fusion Team, and A360 Personal projects. 

For BIM 360 and ACC projects a hub ID corresponds to an Account ID. To convert an Account ID to a hub ID, prefix the account ID with ``b.``. For example, a BIM 360 account ID of ```c8b0c73d-3ae9``` translates to a hub ID of ``b.c8b0c73d-3ae9``.

Similarly, to convert a BIM 360 and ACC project IDs to  Data Management project IDs prefix the BIM 360 or ACC Project ID with ``b.``. For example, a project ID of ``c8b0c73d-3ae9`` translates to a project ID of ``b.c8b0c73d-3ae9``.

**Note:** This operation supports Autodesk Construction Cloud (ACC) Projects. For more information, see the [ACC Platform API documentation](https://en.docs.acc.v1/overview/introduction/).

#### Parameters
- Ref: `#/components/parameters/x-user-id`
- Ref: `#/components/parameters/filter_id`
- Ref: `#/components/parameters/filter_extension_type`
- Ref: `#/components/parameters/page_number`
- Ref: `#/components/parameters/page_limit`

#### Responses
- **200**: The list of projects was successfully retrieved.

---

### Get a Project

**Endpoint:** `GET /project/v1/hubs/{hub_id}/projects/{project_id}`
**Operation ID:** `getProject`

#### Description
Returns the specified project from within the specified hub.

For BIM 360 Docs, a hub ID corresponds to a BIM 360 account ID. To convert a BIM 360 account ID to a hub ID, prefix the account ID with ``b.``. For example, an account ID of ```c8b0c73d-3ae9``` translates to a hub ID of ``b.c8b0c73d-3ae9``.

Similarly, to convert a BIM 360 project ID to a Data Management project ID prefix the BIM 360 Project ID with ``b.``. For example, a project ID of ``c8b0c73d-3ae9`` translates to a project ID of ``b.c8b0c73d-3ae9``.

**Note:** This operation supports Autodesk Construction Cloud (ACC) Projects. For more information, see the [ACC Platform API documentation](https://en.docs.acc.v1/overview/introduction/).

#### Parameters
- Ref: `#/components/parameters/x-user-id`

#### Responses
- **200**: The project was successfully retrieved.

---

### Get Hub for Project

**Endpoint:** `GET /project/v1/hubs/{hub_id}/projects/{project_id}/hub`
**Operation ID:** `getProjectHub`

#### Description
Returns the hub that contains the project specified by the  ``project_id`` parameter.

**Note:** This operation supports Autodesk Construction Cloud (ACC) Projects. For more information, see the [ACC Platform API documentation](https://en.docs.acc.v1/overview/introduction/).

#### Parameters
- Ref: `#/components/parameters/x-user-id`

#### Responses
- **200**: Information about the hub was successfully returned.

---

### List Top-level Project Folders

**Endpoint:** `GET /project/v1/hubs/{hub_id}/projects/{project_id}/topFolders`
**Operation ID:** `getProjectTopFolders`

#### Description
Returns the details of the highest level folders within a project that the user calling this operation has access to. The user must have at least read access to the folders.

If the user is a Project Admin, it returns all top-level folders in the project. Otherwise, it returns all the highest level folders in the folder hierarchy the user has access to.

Users with access permission to a folder has access permission to all its subfolders.

**Note:** This operation supports Autodesk Construction Cloud (ACC) Projects. For more information, see the [ACC Platform API documentation](https://en.docs.acc.v1/overview/introduction/).

#### Parameters
- Ref: `#/components/parameters/x-user-id`
- Ref: `#/components/parameters/excludeDeleted`
- Ref: `#/components/parameters/projectFilesOnly`

#### Responses
- **200**: The top-level folders of the specified project were returned successfully.

---

### Get a Folder

**Endpoint:** `GET /data/v1/projects/{project_id}/folders/{folder_id}`
**Operation ID:** `getFolder`

#### Description
Returns the folder specified by the ``folder_id`` parameter from within the project identified by the ``project_id`` parameter. All folders and subfolders within a project (including the root folder) have a unique ID.

**Note:** This operation supports Autodesk Construction Cloud (ACC) Projects. For more information, see the [ACC Platform API documentation](https://en.docs.acc.v1/overview/introduction/).

#### Parameters
- Ref: `#/components/parameters/If-Modified-Since`
- Ref: `#/components/parameters/x-user-id`

#### Responses
- **200**: The specified folder was successfully retrieved.

---

### Modify a Folder

**Endpoint:** `PATCH /data/v1/projects/{project_id}/folders/{folder_id}`
**Operation ID:** `patchFolder`

#### Description
Renames, moves, hides, or unhides a folder. Marking a BIM 360 Docs folder as hidden effectively deletes it. You can restore it by changing its ``hidden`` attribute. You can also move BIM 360 Docs folders by changing their parent folder.

You cannot permanently delete BIM 360 Docs folders. They are tagged as hidden folders and are removed from the BIM 360 Docs UI and from regular Data Management API responses. You can use the hidden filter (``filter[hidden]=true``) to get a list of deleted folders with the [List Folder Contents](/en/docs/data/v2/reference/http/projects-project_id-folders-folder_id-contents-GET/) operation.

Before you use the Data Management API to access BIM 360 Docs folders, provision your app through the BIM 360 Account Administrator portal. For details, see the [Manage Access to Docs tutorial](/en/docs/bim360/v1/tutorials/getting-started/manage-access-to-docs/).

**Note:** This operation supports Autodesk Construction Cloud (ACC) Projects. For more information, see the [ACC Platform API documentation](/en.docs.acc.v1/overview/introduction/).

#### Parameters
- Ref: `#/components/parameters/x-user-id`

#### Request Body
- Required: `False`
- Content-Type: `application/vnd.api+json`
  - Schema: `#/components/schemas/ModifyFolder`

#### Responses
- **200**: The folder was successfully modified.

---

### Get Parent of a Folder

**Endpoint:** `GET /data/v1/projects/{project_id}/folders/{folder_id}/parent`
**Operation ID:** `getFolderParent`

#### Description
Returns the parent folder of the specified folder. In a project, folders are organized in a hierarchy. Each folder except for the root folder has a parent folder.

**Note:** This operation supports Autodesk Construction Cloud (ACC) Projects. For more information, see the [ACC Platform API documentation](https://en.docs.acc.v1/overview/introduction/).

#### Parameters
- Ref: `#/components/parameters/x-user-id`

#### Responses
- **200**: The parent folder was retrieved successfully.

---

### List Folder Contents

**Endpoint:** `GET /data/v1/projects/{project_id}/folders/{folder_id}/contents`
**Operation ID:** `getFolderContents`

#### Description
Returns a list of items and folders within the specified folder. Items represent word documents, fusion design files, drawings, spreadsheets, etc.

The resources contained in the ``included`` array of the response are their tip versions.

**Note:** This operation supports Autodesk Construction Cloud (ACC) Projects. For more information, see the [ACC Platform API documentation](https://en.docs.acc.v1/overview/introduction/).

#### Parameters
- Ref: `#/components/parameters/x-user-id`
- Ref: `#/components/parameters/filter_type`
- Ref: `#/components/parameters/filter_id`
- Ref: `#/components/parameters/filter_extension_type`
- Ref: `#/components/parameters/filter_lastModifiedTimeRollup`
- Ref: `#/components/parameters/page_number`
- Ref: `#/components/parameters/page_limit`
- Ref: `#/components/parameters/includeHidden`

#### Responses
- **200**: The content of the specified folder was successfully returned.

---

### List Related Resources for a Folder

**Endpoint:** `GET /data/v1/projects/{project_id}/folders/{folder_id}/refs`
**Operation ID:** `getFolderRefs`

#### Description
Returns the resources (items, folders, and versions) that have a custom relationship with the specified folder. Custom relationships can be established between a folder and other resources within the data domain service (folders, items, and versions).

Each relationship is defined by the id of the object at the other end of the relationship, together with type, attributes, and relationships links.
Callers will typically use a filter parameter to restrict the response to the custom relationship types (``filter[meta.refType]``) they are interested in.

**Note:** This operation supports Autodesk Construction Cloud (ACC) Projects. For more information, see the [ACC Platform API documentation](https://en.docs.acc.v1/overview/introduction/).

#### Parameters
- Ref: `#/components/parameters/x-user-id`
- Ref: `#/components/parameters/filter_type_version`
- Ref: `#/components/parameters/filter_id`
- Ref: `#/components/parameters/filter_extension_type`

#### Responses
- **200**: The list of related resources was retrieved successfully.

---

### List Folder and Subfolder Contents

**Endpoint:** `GET /data/v1/projects/{project_id}/folders/{folder_id}/search`
**Operation ID:** `getFolderSearch`

#### Description
Searches the specified folder and its subfolders and returns a list of the latest versions of the items you can access.


Use the ``filter`` query string parameter to narrow down the list as appropriate. You can filter by the following properties of the version payload: 

- ``type`` property, 
- ``id`` property, 
- any of the attributes object properties. 

For example, you can filter by ``createTime`` and ``mimeType``. It returns tip versions (latest versions) of properties where the filter conditions are satisfied. To verify the properties of the attributes object for a specific version, use the [Get a Version](/en/docs/data/v2/reference/http/projects-project_id-versions-version_id-GET/) operation.

To list the immediate contents of the folder without parsing subfolders, use the [List Folder Contents](/en/docs/data/v2/reference/http/projects-project_id-folders-folder_id-contents-GET/) operation.

**Note:** This operation supports Autodesk Construction Cloud (ACC) Projects. For more information, see the [ACC Platform API documentation](https://en.docs.acc.v1/overview/introduction/).

#### Parameters
- Ref: `#/components/parameters/filter`
- Ref: `#/components/parameters/page_number`

#### Responses
- **200**: The contents of the folder and its subfolders were successfully returned.

---

### List Custom Relationships for a Folder

**Endpoint:** `GET /data/v1/projects/{project_id}/folders/{folder_id}/relationships/refs`
**Operation ID:** `getFolderRelationshipsRefs`

#### Description
Returns the custom relationships associated with the specified folder. Custom relationships can be established between a folder and other resources within the data domain service (folders, items, and versions).

Each relationship is defined by the ID of the object at the other end of the relationship, together with type, specific reference meta including extension data.
Callers will typically use a filter parameter to restrict the response to the custom relationship types (``filter[meta.refType]``) they are interested in.
The response body will have an included array that contains the resources in the relationship, which is essentially what is returned by the [List Related Resources for a Folder](/en/docs/data/v2/reference/http/projects-project_id-folders-folder_id-refs-GET/) operation.  

**Note:** This operation supports Autodesk Construction Cloud (ACC) Projects. For more information, see the [ACC Platform API documentation](https://en.docs.acc.v1/overview/introduction/).

#### Parameters
- Ref: `#/components/parameters/x-user-id`
- Ref: `#/components/parameters/filter_type_version`
- Ref: `#/components/parameters/filter_id`
- Ref: `#/components/parameters/filter_refType`
- Ref: `#/components/parameters/filter_direction`
- Ref: `#/components/parameters/filter_extension_type`

#### Responses
- **200**: The list of custom relationships was successfully retrieved.

---

### Create a Custom Relationship for a Folder

**Endpoint:** `POST /data/v1/projects/{project_id}/folders/{folder_id}/relationships/refs`
**Operation ID:** `postFolderRelationshipsRef`

#### Description
Creates a custom relationship between a folder and another resource within the data domain service (folder, item, or version).

#### Parameters
- Ref: `#/components/parameters/x-user-id`

#### Request Body
- Required: `False`
- Content-Type: `application/vnd.api+json`
  - Schema: `#/components/schemas/RelationshipRefsRequest`

#### Responses
- **204**: The reference between resources was successfully created.

---

### List Relationship Links for a Folder

**Endpoint:** `GET /data/v1/projects/{project_id}/folders/{folder_id}/relationships/links`
**Operation ID:** `getFolderRelationshipsLinks`

#### Description
Returns a list of links for the specified folder. 

Custom relationships can be established between a folder and other external resources residing outside the data domain service. A link’s ``href`` attribute defines the target URI to access a resource.

**Note:** This operation supports Autodesk Construction Cloud (ACC) Projects. For more information, see the [ACC Platform API documentation](https://en.docs.acc.v1/overview/introduction/).

#### Parameters
- Ref: `#/components/parameters/x-user-id`

#### Responses
- **200**: Successful retrieval of the links collection associated with a specific resource.

---

### Get an Item

**Endpoint:** `GET /data/v1/projects/{project_id}/items/{item_id}`
**Operation ID:** `getItem`

#### Description
Retrieves an item. Items represent Word documents, Fusion 360 design files, drawings, spreadsheets, etc.

The tip version for the item is included in the included array of the payload.
To retrieve multiple items, see the ListItems command.

**Note:** This operation supports Autodesk Construction Cloud (ACC) Projects. For more information, see the [ACC Platform API documentation](https://en.docs.acc.v1/overview/introduction/).

#### Parameters
- Ref: `#/components/parameters/x-user-id`
- Ref: `#/components/parameters/includePathInProject`

#### Responses
- **200**: The specified item was retrieved successfully.

---

### Update an Item

**Endpoint:** `PATCH /data/v1/projects/{project_id}/items/{item_id}`
**Operation ID:** `patchItem`

#### Description
Updates the ``displayName`` of the specified item. Note that updating the ``displayName`` of an item is not supported for BIM 360 Docs or ACC items.

**Note:** This operation supports Autodesk Construction Cloud (ACC) Projects. For more information, see the [ACC Platform API documentation](https://en.docs.acc.v1/overview/introduction/).

#### Parameters
- Ref: `#/components/parameters/x-user-id`

#### Request Body
- Required: `False`
- Content-Type: `application/vnd.api+json`
  - Schema: `#/components/schemas/ItemRequest`

#### Responses
- **200**: Updated the item’s properties successfully.

---

### Get Parent of an Item

**Endpoint:** `GET /data/v1/projects/{project_id}/items/{item_id}/parent`
**Operation ID:** `getItemParentFolder`

#### Description
Returns the parent folder of the specified item.

**Note:** This operation supports Autodesk Construction Cloud (ACC) Projects. For more information, see the [ACC Platform API documentation](https://en.docs.acc.v1/overview/introduction/).

#### Parameters
- Ref: `#/components/parameters/x-user-id`

#### Responses
- **200**: The parent folder was retrieved successfully.

---

### List Custom Relationships for an Item

**Endpoint:** `GET /data/v1/projects/{project_id}/items/{item_id}/relationships/refs`
**Operation ID:** `getItemRelationshipsRefs`

#### Description
Returns the custom relationships that are associated with the specified item. Custom relationships can be established between an item and other resources within the ``data`` domain service (folders, items, and versions).

Each relationship is defined by the ID of the object at the other end of the relationship, together with type, specific reference meta including extension data.
Callers will typically use a filter parameter to restrict the response to the custom relationship types (``filter[meta.refType]``) they are interested in.
The response body will have an included array that contains the resources in the relationship, which is essentially what is returned by the [List Related Resources for an Item](/en/docs/data/v2/reference/http/projects-project_id-items-item_id-refs-GET/) operation.

**Note:** This operation supports Autodesk Construction Cloud (ACC) Projects. For more information, see the [ACC Platform API documentation](https://en.docs.acc.v1/overview/introduction/).

#### Parameters
- Ref: `#/components/parameters/x-user-id`
- Ref: `#/components/parameters/filter_type_version`
- Ref: `#/components/parameters/filter_id`
- Ref: `#/components/parameters/filter_refType`
- Ref: `#/components/parameters/filter_direction`
- Ref: `#/components/parameters/filter_extension_type`

#### Responses
- **200**: The list of custom relationships was successfully retrieved.

---

### Create a Custom Relationship for an Item

**Endpoint:** `POST /data/v1/projects/{project_id}/items/{item_id}/relationships/refs`
**Operation ID:** `postItemRelationshipsRef`

#### Description
Creates a custom relationship between an item and another resource within the data domain service (folder, item, or version).

#### Parameters
- Ref: `#/components/parameters/x-user-id`

#### Request Body
- Required: `False`
- Content-Type: `application/vnd.api+json`
  - Schema: `#/components/schemas/RelationshipRefsRequest`

#### Responses
- **204**: A custom relationship for the item was successfully created.

---

### List Related Resources for an Item

**Endpoint:** `GET /data/v1/projects/{project_id}/items/{item_id}/refs`
**Operation ID:** `getItemRefs`

#### Description
Returns the resources (items, folders, and versions) that have a custom relationship with the specified item. Custom relationships can be established between an item and other resources within the data domain service (folders, items, and versions).


Each relationship is defined by the ID of the object at the other end of the relationship, together with type, attributes, and relationships links.
Callers will typically use a filter parameter to restrict the response to the custom relationship types (``filter[meta.refType]``) they are interested in.


**Note:** This operation supports Autodesk Construction Cloud (ACC) Projects. For more information, see the [ACC Platform API documentation](https://en.docs.acc.v1/overview/introduction/).

#### Parameters
- Ref: `#/components/parameters/x-user-id`
- Ref: `#/components/parameters/filter_type_version`
- Ref: `#/components/parameters/filter_id`
- Ref: `#/components/parameters/filter_extension_type`

#### Responses
- **200**: The list of related resources was successfully retrieved.
- **403**: Forbidden

---

### List Relationship Links for an Item

**Endpoint:** `GET /data/v1/projects/{project_id}/items/{item_id}/relationships/links`
**Operation ID:** `getItemRelationshipsLinks`

#### Description
Returns a list of links for the specified item. 

Custom relationships can be established between an item and other external resources residing outside the data domain service. A link’s ``href`` attribute defines the target URI to access a resource.

**Note:** This operation supports Autodesk Construction Cloud (ACC) Projects. For more information, see the [ACC Platform API documentation](https://en.docs.acc.v1/overview/introduction/).

#### Parameters
- Ref: `#/components/parameters/x-user-id`

#### Responses
- **200**: The relationship links for the item were retrieved successfully.

---

### Get Tip Version of an Item

**Endpoint:** `GET /data/v1/projects/{project_id}/items/{item_id}/tip`
**Operation ID:** `getItemTip`

#### Description
Returns the latest version of the specified item. A project can contain multiple versions of a resource item. The latest version is referred to as the tip version, which is returned by this operation.

**Note:** This operation supports Autodesk Construction Cloud (ACC) Projects. For more information, see the [ACC Platform API documentation](https://en.docs.acc.v1/overview/introduction/).

#### Parameters
- Ref: `#/components/parameters/x-user-id`

#### Responses
- **200**: The tip version of the item was retrieved successfully.

---

### List all Versions of an Item

**Endpoint:** `GET /data/v1/projects/{project_id}/items/{item_id}/versions`
**Operation ID:** `getItemVersions`

#### Description
Lists all versions of the specified item. A project can contain multiple versions of a resource item.

**Note:** This operation supports Autodesk Construction Cloud (ACC) Projects. For more information, see the [ACC Platform API documentation](https://en.docs.acc.v1/overview/introduction/).

#### Parameters
- Ref: `#/components/parameters/x-user-id`
- Ref: `#/components/parameters/filter_id`
- Ref: `#/components/parameters/filter_extension_type`
- Ref: `#/components/parameters/filter_versionNumber`
- Ref: `#/components/parameters/page_number`
- Ref: `#/components/parameters/page_limit`

#### Responses
- **200**: All versions of the specified item were successfully retrieved.

---

### Get a Version

**Endpoint:** `GET /data/v1/projects/{project_id}/versions/{version_id}`
**Operation ID:** `getVersion`

#### Description
Returns the specified version of an item.

**Note:** This operation supports Autodesk Construction Cloud (ACC) Projects. For more information, see the [ACC Platform API documentation](https://en.docs.acc.v1/overview/introduction/).

#### Parameters
- Ref: `#/components/parameters/x-user-id`

#### Responses
- **200**: The specified version was retrieved successfully.

---

### Update a Version

**Endpoint:** `PATCH /data/v1/projects/{project_id}/versions/{version_id}`
**Operation ID:** `patchVersion`

#### Description
Updates the properties of the specified version of an  item. Currently, you can only change the name of the version.

**Note:** This operation is not supported for BIM 360 and ACC. If you want to rename a version, create a new version with a new name.

#### Request Body
- Required: `False`
- Content-Type: `application/vnd.api+json`
  - Schema: `#/components/schemas/VersionRequest`

#### Responses
- **200**: The version was updated successfully.

---

### Get Item by Version

**Endpoint:** `GET /data/v1/projects/{project_id}/versions/{version_id}/item`
**Operation ID:** `getVersionItem`

#### Description
Returns the item corresponding to the specified version.

**Note:** This operation supports Autodesk Construction Cloud (ACC) Projects. For more information, see the [ACC Platform API documentation](https://en.docs.acc.v1/overview/introduction/).

#### Parameters
- Ref: `#/components/parameters/x-user-id`

#### Responses
- **200**: Successful retrieval of a specific item.

---

### List Related Resources for a Version

**Endpoint:** `GET /data/v1/projects/{project_id}/versions/{version_id}/refs`
**Operation ID:** `getVersionRefs`

#### Description
Returns the resources (items, folders, and versions) that have a custom relationship with the specified version.

Custom relationships can be established between a version of an item and other resources within the data domain service (folders, items, and versions).

- Each relationship is defined by the id of the object at the other end of the relationship, together with type, attributes, and relationships links.
- Callers will typically use a filter parameter to restrict the response to the custom relationship types (``filter[meta.refType]``) they are interested in.
- The response body will have an included array that contains the ref resources that are involved in the relationship, which is essentially the response to the [List Custom Relationships for a Version](/en/docs/data/v2/reference/http/projects-project_id-versions-version_id-relationships-refs-GET/) operation. 

**Note:** This operation supports Autodesk Construction Cloud (ACC) Projects. For more information, see the [ACC Platform API documentation](https://en.docs.acc.v1/overview/introduction/).

#### Parameters
- Ref: `#/components/parameters/x-user-id`
- Ref: `#/components/parameters/filter_type_version`
- Ref: `#/components/parameters/filter_id`
- Ref: `#/components/parameters/filter_extension_type`

#### Responses
- **200**: The list of resources was successfully returned.

---

### List Custom Relationships for a Version

**Endpoint:** `GET /data/v1/projects/{project_id}/versions/{version_id}/relationships/refs`
**Operation ID:** `getVersionRelationshipsRefs`

#### Description
Returns the custom relationships for the specified version. 

Custom relationships can be established between a version of an item and other resources within the data domain service (folders, items, and versions).

- Each relationship is defined by the id of the object at the other end of the relationship, together with type, specific reference meta including extension data.
- Callers will typically use a filter parameter to restrict the response to the custom relationship types (``filter[meta.refType]``) they are interested in.
- The response body will have an included array that contains the resources in the relationship, which is essentially the response to the [List Related Resources operation](/en/docs/data/v2/reference/http/projects-project_id-versions-version_id-relationships-refs-POST/).
- To get custom relationships for multiple versions, see the ListRefs command.

**Note:** This operation supports Autodesk Construction Cloud (ACC) Projects. For more information, see the [ACC Platform API documentation](https://en.docs.acc.v1/overview/introduction/).

#### Parameters
- Ref: `#/components/parameters/x-user-id`
- Ref: `#/components/parameters/filter_type_version`
- Ref: `#/components/parameters/filter_id`
- Ref: `#/components/parameters/filter_refType`
- Ref: `#/components/parameters/filter_direction`
- Ref: `#/components/parameters/filter_extension_type`

#### Responses
- **200**: The custom relationships for the version was returned successfully.

---

### Create a Custom Relationship for a Version

**Endpoint:** `POST /data/v1/projects/{project_id}/versions/{version_id}/relationships/refs`
**Operation ID:** `postVersionRelationshipsRef`

#### Description
Creates a custom relationship between a version of an item and another resource within the data domain service (folder, item, or version).

#### Parameters
- Ref: `#/components/parameters/x-user-id`

#### Request Body
- Required: `False`
- Content-Type: `application/vnd.api+json`
  - Schema: `#/components/schemas/RelationshipRefsRequest`

#### Responses
- **204**: The custom relationship was successfully created.

---

### List Links for a Version

**Endpoint:** `GET /projects/{project_id}/versions/{version_id}/relationships/links`
**Operation ID:** `getVersionRelationshipsLinks`

#### Description
Returns a collection of links for the specified version of an item. Custom relationships can be established between a version of an item and other external resources residing outside the data domain service. A link’s href defines the target URI to access the resource.

**Note:** This operation supports Autodesk Construction Cloud (ACC) Projects. For more information, see the [ACC Platform API documentation](https://en.docs.acc.v1/overview/introduction/).

#### Parameters
- Ref: `#/components/parameters/x-user-id`

#### Responses
- **200**: Successful retrieval of the links collection associated with a specific resource.OK

---

### Create a Storage Location in OSS

**Endpoint:** `POST /data/v1/projects/{project_id}/storage`
**Operation ID:** `postStorage`

#### Description
Creates a placeholder for an item or a version of an item in the OSS. Later, you can upload the binary content for the item or version to this storage location.

**Note:** This operation supports Autodesk Construction Cloud (ACC) Projects. For more information, see the [ACC Platform API documentation](https://en.docs.acc.v1/overview/introduction/).

#### Parameters
- Ref: `#/components/parameters/x-user-id`

#### Request Body
- Required: `False`
- Content-Type: `application/vnd.api+json`
  - Schema: `#/components/schemas/StorageRequest`

#### Responses
- **201**: The storage location was created successfully.

---

### Create a Folder

**Endpoint:** `POST /data/v1/projects/{project_id}/folders`
**Operation ID:** `postFolder`

#### Description
Creates a new folder in the specified project. Use the ``parent`` attribute in the request body to specify where in the hierarchy the new folder should be located. Folders can be nested up to 25 levels deep.

Use the `Modify a Folder </en/docs/data/v2/reference/http/projects-project_id-folders-folder_id-PATCH/>`_ operation to delete and restore folders.

Before you use the Data Management API to access BIM 360 Docs folders, provision your app through the BIM 360 Account Administrator portal. For details, see the [Manage Access to Docs tutorial](/en/docs/bim360/v1/tutorials/getting-started/manage-access-to-docs/).

**Note:** This operation supports Autodesk Construction Cloud (ACC) Projects. For more information, see the [ACC Platform API documentation](https://en.docs.acc.v1/overview/introduction/).

#### Parameters
- Ref: `#/components/parameters/x-user-id`

#### Request Body
- Required: `False`
- Content-Type: `application/vnd.api+json`
  - Schema: `#/components/schemas/CreateFolder`

#### Responses
- **201**: Successful creation of a folder.

---

### Create an Item

**Endpoint:** `POST /data/v1/projects/{project_id}/items`
**Operation ID:** `postItem`

#### Description
Creates the first version of a file (item). To create additional versions of an item, use POST versions.

Before you create the first version of an item, you must create a placeholder for the file, and upload the file to the placeholder. For more details about the workflow, see the tutorial on uploading a file.

This operation also allows you to create a new item by copying a specific version of an existing item to another folder. The copied version becomes the first version of the new item in the target folder.

**Note:** You cannot copy versions of items across different projects and accounts.

Use the [Create Version](/en/docs/data/v2/reference/http/projects-project_id-versions-POST/) operation with the ``copyFrom`` parameter if you want to create a new version of an item by copying a specific version of another item. 

Before you use the Data Management API to access BIM 360 Docs files, you must provision your app through the BIM 360 Account Administrator portal. For details, see the [Manage Access to Docs tutorial](/en/docs/bim360/v1/tutorials/getting-started/manage-access-to-docs/).

**Note:** This operation supports Autodesk Construction Cloud (ACC) Projects. For more information, see the [ACC Platform API documentation](https://en.docs.acc.v1/overview/introduction/).

#### Parameters
- Ref: `#/components/parameters/copyFrom`
- `x-user-id` in `query` (required: False) — In a two-legged authentication context, the app has access to all users specified by the administrator in the SaaS integrations UI. By providing this header, the API call will be limited to act on behalf of only the user specified.        

Note that for a three-legged OAuth flow or for a two-legged OAuth flow with user impersonation (``x-user-id``), the users of your app must have permission to upload files to the specified parent folder (``data.attributes.relationships.parent.data.id``).

For copying files, users of your app must have permission to view the source folder. 

For information about managing and verifying folder permissions for BIM 360 Docs, see the section on [Managing Folder Permissions](http://help.autodesk.com/view/BIM360D/ENU/?guid=GUID-2643FEEF-B48A-45A1-B354-797DAD628C37).'

#### Request Body
- Required: `False`
- Content-Type: `application/vnd.api+json`
  - Schema: `#/components/schemas/CreateItem`

#### Responses
- **201**: The first version of an item was successfully created.

---

### Create a Version

**Endpoint:** `POST /data/v1/projects/{project_id}/versions`
**Operation ID:** `postVersion`

#### Description
Creates a new versions of an existing item.

Before creating a new version you must create a storage location for the version in OSS, and upload the file to that location. For more details about the workflow, see the tutorial on uploading a file.

This operation also allows you to create a new version of an item by copying a specific version of an existing item from another folder within the project. The new version becomes the tip version of the item.

Use the [Create an Item](/en/docs/data/v2/reference/http/projects-project_id-items-POST/) operation to copy a specific version of an existing item as a new item in another folder.

This operation can also be used to delete files on BIM360 Document Management. For more information, please refer to the delete and restore a file tutorial.

Before you use the Data Management API to access BIM 360 Docs files, you must provision your app through the BIM 360 Account Administrator portal. For details, see the [Manage Access to Docs tutorial](/en/docs/bim360/v1/tutorials/getting-started/manage-access-to-docs/).

**Note:** This operation supports Autodesk Construction Cloud (ACC) Projects. For more information, see the [ACC Platform API documentation](https://en.docs.acc.v1/overview/introduction/).

#### Parameters
- Ref: `#/components/parameters/x-user-id`
- Ref: `#/components/parameters/copyFrom`

#### Request Body
- Required: `False`
- Content-Type: `application/vnd.api+json`
  - Schema: `#/components/schemas/CreateVersion`

#### Responses
- **201**: Successful creation of a version.
- **409**: Conflict

---

### List Supported Download Formats

**Endpoint:** `GET /data/v1/projects/{project_id}/versions/{version_id}/downloadFormats`
**Operation ID:** `getVersionDownloadFormats`

#### Description
Returns a list of file formats the specified version of an item can be downloaded as.

**Note:** This operation supports Autodesk Construction Cloud (ACC) Projects. For more information, see the [ACC Platform API documentation](https://en.docs.acc.v1/overview/introduction/).

#### Parameters
- Ref: `#/components/parameters/x-user-id`

#### Responses
- **200**: The list of file formats that the version can be downloaded as was successfully retrieved.

---

### List Available Download Formats

**Endpoint:** `GET /data/v1/projects/{project_id}/versions/{version_id}/downloads`
**Operation ID:** `getVersionDownloads`

#### Description
Returns the list of file formats of the specified version of an item currently available for download.

**Note:** This operation is not fully implemented as yet. It currently returns an empty data object.

#### Parameters
- Ref: `#/components/parameters/x-user-id`
- Ref: `#/components/parameters/filter_format_fileType`

#### Responses
- **200**: The list of available downloadformats was successfully retrieved.

---

### Get Download Details

**Endpoint:** `GET /data/v1/projects/{project_id}/downloads/{download_id}`
**Operation ID:** `getDownload`

#### Description
Returns the details of a downloadable format of a version of an item.

#### Parameters
- Ref: `#/components/parameters/x-user-id`

#### Responses
- **200**: The details of the specified download were retrieved successfully.

---

### Create Download

**Endpoint:** `POST /data/v1/projects/{project_id}/downloads`
**Operation ID:** `postDownload`

#### Description
Kicks off a job to generate the specified download format of the version. Once the job completes, the specified format becomes available for download.

#### Parameters
- Ref: `#/components/parameters/x-user-id`

#### Request Body
- Required: `False`
- Content-Type: `application/vnd.api+json`
  - Schema: `#/components/schemas/CreateDownload`

#### Responses
- **202**: A job to generate the download format was successfully started.

---

### Check Download Creation Progress

**Endpoint:** `GET /data/v1/projects/{project_id}/jobs/{job_id}`
**Operation ID:** `getDownloadJob`

#### Description
Checks the status of a job that generates a downloadable format of a version of an item. 

**Note**: If the job has finished, this operation returns a HTTP status 303, with the ``location`` return header set to the URI that returns the details of the download.

#### Parameters
- Ref: `#/components/parameters/x-user-id`

#### Responses
- **200**: Details of the specified job was returned successfully.
- **303**: The request has been redirected to a new location.

---

### Execute a Command

**Endpoint:** `POST /data/v1/projects/{project_id}/commands`
**Operation ID:** `postCommand`

#### Description
Executes the command that you specify in the request body. Commands enable you to perform general operations on multiple resources.

For example, you can check whether a user has permission to delete a collection of versions, items, and folders.

The command as well as the input data for the command are specified using the ``data`` object of the request body. 

For more information about commands see the [Commands](/en/docs/data/v2/overview/commands/) section in the Developer's Guide.

#### Parameters
- Ref: `#/components/parameters/x-user-id`

#### Request Body
- Required: `False`
- Content-Type: `application/vnd.api+json`

#### Responses
- **200**: The command was executed successfully.

---

## Model Derivative

_Generated from `modelderivative.yaml`_

Use the Model Derivative API to translate designs from one CAD format to another.

---

### List Supported Formats

**Endpoint:** `GET /modelderivative/v2/designdata/formats`
**Operation ID:** `get-formats`

#### Description
Returns an up-to-date list of supported translations. It lets you determine the types of derivatives supported for each source design file type. Furthermore, you can get it to retrieve only the translations that have been updated since a date you specify.

See the `Supported Translation Formats table </en/docs/model-derivative/v2/overview/supported-translations>`_ for more details.

**Note:** We keep adding new file formats to our supported translations list, constantly.

#### Parameters
- `If-Modified-Since` in `header` (required: False) — Specifies a date in the ``Day of the week, DD Month YYYY HH:MM:SS GMT`` format. The response will contain only the formats modified since the specified date and time. If you specify an invalid date, the response will contain all supported formats. If no changes have been made after the specified date, the service returns HTTP status ``304``, NOT MODIFIED.
- Ref: `#/components/parameters/accept-encoding`

#### Responses
- **200**: A list of supported formats was successfully returned.
- **304**: Supported formats have not changed since the date specified by the ``If-Modified-Since`` header.

---

### List Model Views

**Endpoint:** `GET /modelderivative/v2/designdata/{urn}/metadata`
**Operation ID:** `get-model-views`

#### Description
Returns a list of Model Views (Viewables) in the source design specified by the ``urn`` parameter. It also returns an ID that uniquely identifies the Model View. You can use these IDs with other metadata operations to obtain information about the objects within those Model Views.

Designs created with applications like Fusion 360 and Inventor contain only one Model View per design. Applications like Revit allow multiple Model Views per design.

**Note:** You can retrieve metadata only from a design that has already been translated to SVF or SVF2.

#### Parameters
- Ref: `#/components/parameters/accept-encoding`

#### Responses
- **200**: Success

---

### Fetch Object tree

**Endpoint:** `GET /modelderivative/v2/designdata/{urn}/metadata/{modelGuid}`
**Operation ID:** `get-object-tree`

#### Description
Retrieves the structured hierarchy of objects, known as an object tree, from the specified Model View (Viewable) within the specified source design. The object tree represents the arrangement and relationships of various objects present in that Model View.

**Note:** A design file must be translated to SVF or SVF2 before you can retrieve its object tree.  

Before you call this operation:

- Use the `List Model Views </en/docs/model-derivative/v2/reference/http/metadata/urn-metadata-GET/>`_ operation to obtain the list of Model Views in the source design.
- Pick the ID of the Model View you want to query and specify that ID as the value for the ``modelGuid``  parameter.

#### Parameters
- Ref: `#/components/parameters/accept-encoding`
- Ref: `#/components/parameters/x-ads-force`
- Ref: `#/components/parameters/x-ads-derivative-format`
- Ref: `#/components/parameters/forceget`
- `objectid` in `query` (required: False) — If specified, retrieves the sub-tree that has the specified object ID as its parent node. If this parameter is not specified, retrieves the entire object tree.
- `level` in `query` (required: False) — Specifies how many child levels of the hierarchy to return, when the ``objectid``  parameter is specified. Currently supports only ``level`` = ``1``.

#### Responses
- **200**: Success
- **202**: Request accepted but processing not complete. Call this operation iteratively until a 200 is returned.

---

### Fetch All Properties

**Endpoint:** `GET /modelderivative/v2/designdata/{urn}/metadata/{modelGuid}/properties`
**Operation ID:** `get-all-properties`

#### Description
Returns a list of properties of all objects in the  Model View specified by the ``modelGuid`` parameter. 

This operation returns properties of all objects by default. However, you can restrict the results to a specific object by specifying its ID as the ``objectid`` parameter.

Properties are returned as a flat list, ordered, by their ``objectid``. The ``objectid`` is a non-persistent ID assigned to an object when the source design is translated to the SVF or SVF2 format. This means that:

- A design file must be translated to SVF or SVF2 before you can retrieve properties.
- The ``objectid`` of an object can change if the design is translated to SVF or SVF2 again. If you require a persistent ID across translations, use ``externalId`` to reference objects, instead of ``objectid``.

Before you call this operation:

- Use the `List Model Views </en/docs/model-derivative/v2/reference/http/metadata/urn-metadata-GET/>`_ operation to obtain the list of Model Views (Viewables) in the source design. 
- Pick the ID of the Model View you want to query and specify that ID as the value for the ``modelGuid`` parameter.

**Tip**: Use `Fetch Specific Properties </en/docs/model-derivative/v2/reference/http/metadata/urn-metadata-guid-properties-GET/>`_ to retrieve only the objects and properties of interest. What’s more, the response is paginated. So, when the number of properties returned is large, responses start arriving more promptly.

#### Parameters
- Ref: `#/components/parameters/accept-encoding`
- Ref: `#/components/parameters/x-ads-force`
- Ref: `#/components/parameters/x-ads-derivative-format`
- `objectid` in `query` (required: False) — The Object ID of the object you want to restrict the response to. If you do not specify this parameter, all properties of all objects within the Model View are returned.
- Ref: `#/components/parameters/forceget`

#### Responses
- **200**: Success.
- **202**: Request accepted but processing not complete. Call this operation again, until you recieve 200 OK.

---

### Fetch Specific Properties

**Endpoint:** `POST /modelderivative/v2/designdata/{urn}/metadata/{modelGuid}/properties:query`
**Operation ID:** `fetch-specific-properties`

#### Description
Queries the objects in the Model View (Viewable) specified by the ``modelGuid`` parameter and returns the specified properties in a paginated list. You can limit the number of objects to be queried by specifying a filter using the ``query`` attribute in the request body.

**Note:** A design file must be translated to SVF or SVF2 before you can query object properties.  

Before you call this operation:

- Use the `List Model Views </en/docs/model-derivative/v2/reference/http/metadata/urn-metadata-GET/>`_ operation to obtain the list of Model Views in the source design.
- Pick the ID of the Model View you want to query and specify that ID as the value for the ``modelGuid``  parameter.

#### Parameters
- Ref: `#/components/parameters/accept-encoding`

#### Request Body
- Required: `False`
- Content-Type: `application/json`
  - Schema: `#/components/schemas/SpecificPropertiesPayload`

#### Responses
- **200**: Success
- **202**: Request accepted but processing is not complete. Call this operation again, until you receive 200 OK.

---

### Fetch Thumbnail

**Endpoint:** `GET /modelderivative/v2/designdata/{urn}/thumbnail`
**Operation ID:** `get-thumbnail`

#### Description
Downloads a thumbnail of the specified source design.

#### Parameters
- `width` in `query` (required: False) — Width of thumbnail.  

Possible values: 100, 200, 400  

If ``width`` is omitted, but ``height`` is specified, ``width`` defaults to ``height``. If both ``width`` and ``height`` are omitted, the server will return a thumbnail closest to 200, if such a thumbnail is available.
- `height` in `query` (required: False) — Height of thumbnails.

Possible values: ``100``, ``200``, ``400``.

If ``height`` is omitted, but ``width`` is specified, ``height`` defaults to ``width``.  If both ``width`` and ``height`` are omitted, the server will return a thumbnail closest to 200, if such a thumbnail is available.

#### Responses
- **200**: Success

---

### Fetch Derivative Download URL

**Endpoint:** `GET /modelderivative/v2/designdata/{urn}/manifest/{derivativeUrn}/signedcookies`
**Operation ID:** `get-derivative-url`

#### Description
Returns a download URL and a set of signed cookies, which lets you securely download the derivative specified by the `derivativeUrn` URI parameter. The signed cookies have a lifetime of 6 hours. Although you cannot use range headers for this operation, you can use range headers for the returned download URL to download the derivative in chunks, in parallel.

#### Parameters
- `minutes-expiration` in `query` (required: False) — Specifies how many minutes the signed cookies should remain valid. Default value is 360 minutes. The value you specify must be lower than the default value for this parameter. If you specify a value greater than the default value, the Model Derivative service will return an error with an HTTP status code of 400.
- `response-content-disposition` in `query` (required: False) — The value that must be returned with the download URL as the ``response-content-disposition`` query string parameter. Must begin with ``attachment``. This value defaults to the default value corresponding to the derivative/file.

#### Responses
- **200**: Success

---

### Check Derivative Details

**Endpoint:** `HEAD /modelderivative/v2/designdata/{urn}/manifest/{derivativeUrn}`
**Operation ID:** `head-check-derivative`

#### Description
Returns information about the specified derivative.

This operation returns a set of headers similar to that returned by `Download Derivative </en/docs/model-derivative/v2/reference/urn-manifest-derivativeurn-GET>`_.

You can use this operation to determine the total content length of a derivative before you download it. If the derivative is large, you can choose to download the derivative in chunks, by specifying a chunk size using the Range header parameter.

#### Responses
- **200**: Success
- **202**: Request accepted but processing not complete. Call this operation again, until getting 200 OK.

---

### Fetch Manifest

**Endpoint:** `GET /modelderivative/v2/designdata/{urn}/manifest`
**Operation ID:** `get-manifest`

#### Description
Retrieves the manifest of the specified source design.

The manifest is a JSON file containing information about all the derivatives translated from the specified source design. It contains information such as the URNs of the derivatives, the translation status of each derivative, and much more.

The first time you translate a source design, the Model Derivative service creates a manifest for that source design. Thereafter, every time you translate that source design, even to a different format, the Model Derivative service updates that manifest. It does not create a new manifest. Instead, it keeps track of all derivatives of that design.  

When the Model Derivative service starts a translation job (as a result of a request you make using `Submit Translation Job </en/docs/model-derivative/v2/reference/http/jobs/job-POST/>`_), it keeps on updating the manifest at regular intervals. So, you can use the manifest to check the status and progress of each derivative that is being generated. When multiple derivatives have been requested each derivative may complete at a different time. So, each derivative has its own ``status`` attribute. The manifest also contains an overall ``status`` attribute. The overall ``status`` becomes ``complete`` when the ``status`` of all individual derivatives become complete.

Once the translation status of a derivative is ``complete`` you can download the URN.

**Note**: You cannot download 3D SVF2 derivatives.

#### Parameters
- Ref: `#/components/parameters/accept-encoding`

#### Responses
- **200**: Success

---

### Delete Manifest

**Endpoint:** `DELETE /modelderivative/v2/designdata/{urn}/manifest`
**Operation ID:** `delete-manifest`

#### Description
Deletes the manifest of the specified source design. It also deletes all derivatives (translated output files) generated from the source design. However, it does not delete the source design.

**Note:** This operation is idempotent. So, if you call it multiple times, even when no manifest exists, will still return a successful response (200).

#### Responses
- **200**: Success.

---

### Submit Translation Job

**Endpoint:** `POST /modelderivative/v2/designdata/job`
**Operation ID:** `start-job`

#### Description
Creates a job to translate the specified source design to another format, generating derivatives of the source design. You can optionaly:

- Extract selected parts of a design and export the set of geometries in OBJ format.
- Generate different-sized thumbnails.

When the translation job runs, progress information and details of the generated derivatives are logged to a JSON file that is called a manifest. A manifest is typically created the first time you translate the source design. Thereafter the system updates the same manifest each time a translation job is executed for that source design. If necessary, you can set the ``x-ads-force`` parameter to ``true``, which deletes the existing manifest and creates a fresh manifest. However, if you do so, all derivatives generated prior to this are deleted.

#### Parameters
- Ref: `#/components/parameters/x-ads-force`
- Ref: `#/components/parameters/x-ads-derivative-format`

#### Request Body
- Required: `False`
- Content-Type: `application/json`
  - Schema: `#/components/schemas/JobPayload`

#### Responses
- **200**: Success
- **201**: The requested file type has been previously generated and has not been replaced by the new source file.

---

### Specify References

**Endpoint:** `POST /modelderivative/v2/designdata/{urn}/references`
**Operation ID:** `specify-references`

#### Description
Specifies the location of the files referenced by the specified source design.

If a source design contains references to other files, you must set  ``checkReferences`` to ``true``, when you call `Submit Translation Job </en/docs/model-derivative/v2/reference/http/job-POST>`_.  The Model Derivative service will then use the details you specify in this operation to locate and download the referenced files.

#### Request Body
- Required: `False`
- Content-Type: `application/json`

#### Responses
- **200**: Success

---

## oss

_Generated from `oss.yaml`_

The Object Storage Service (OSS) allows your application to download and upload raw files (such as PDF, XLS, DWG, or RVT) that are managed by the Data service.

---

### List Buckets

**Endpoint:** `GET /oss/v2/buckets`
**Operation ID:** `get_buckets`

#### Description
Returns a list of buckets owned by the application.

#### Parameters
- Ref: `#/components/parameters/region`
- Ref: `#/components/parameters/limit`
- Ref: `#/components/parameters/startAt`

#### Responses
- **200**: The list of buckets was successfully retrieved.

---

### Create Bucket

**Endpoint:** `POST /oss/v2/buckets`
**Operation ID:** `create_bucket`

#### Description
Creates a bucket. 

Buckets are virtual container within the Object Storage Service (OSS), which you can use to store and manage objects (files) in the cloud. The application creating the bucket is the owner of the bucket.

**Note:** Do not use this operation to create buckets for BIM360 Document Management. Use [POST projects/{project_id}/storage](/en/docs/data/v2/reference/http/projects-project_id-storage-POST>) instead. For details, see [Upload Files to BIM 360 Document Management](/en/docs/bim360/v1/tutorials/document-management/upload-document).

#### Parameters
- Ref: `#/components/parameters/x-ads-region`

#### Request Body
- Required: `True`
- Content-Type: `application/json`
  - Schema: `#/components/schemas/create_buckets_payload`

#### Responses
- **200**: Bucket was successfully created.
- **409**: The specified bucket key already exists.

---

### Delete Bucket

**Endpoint:** `DELETE /oss/v2/buckets/{bucketKey}`
**Operation ID:** `delete_bucket`

#### Description
Deletes the specified bucket. Only the application that owns the bucket can call this operation. All other applications that call this operation will receive a "403 Forbidden" error. 

The initial processing of a bucket deletion request can be time-consuming. So, we recommend only deleting buckets containing a few objects, like those typically used for acceptance testing and prototyping. 

**Note:** Bucket keys will not be immediately available for reuse.

#### Parameters
- `bucketKey` in `path` (required: True) — The bucket key of the bucket to delete.

#### Responses
- **200**: The bucket deletion request was accepted.
- **400**: BAD REQUEST, Invalid request due to malformed syntax or missing headers
- **404**: NOT FOUND, The specified ``bucketKey`` does not exist.
- **409**: CONFLICT, The specified bucket is already marked for deletion.

---

### Get Bucket Details

**Endpoint:** `GET /oss/v2/buckets/{bucketKey}/details`
**Operation ID:** `get_bucket_details`

#### Description
Returns detailed information about the specified bucket.

**Note:** Only the application that owns the bucket can call this operation. All other applications that call this operation will receive a "403 Forbidden" error.

#### Parameters
- `bucketKey` in `path` (required: True) — The bucket key of the bucket to query.

#### Responses
- **200**: Bucket details were retrieved successfully.
- **404**: NOT FOUND, Bucket does not exist.

---

### Delete Object

**Endpoint:** `DELETE /oss/v2/buckets/{bucketKey}/objects/{objectKey}`
**Operation ID:** `delete_object`

#### Description
Deletes an object from the bucket.

#### Parameters
- Ref: `#/components/parameters/bucketKey`
- Ref: `#/components/parameters/objectKey`
- `x-ads-acm-namespace` in `header` (required: False) — This header is used to let the OSS Api Proxy know if ACM is used to authorize access to the given object. If this authorization is used by your service, then you must provide the name of the namespace you want to validate access control policies against.
- `x-ads-acm-check-groups` in `header` (required: False) — Informs the OSS API Proxy know if your service requires ACM authorization to also validate against Oxygen groups. If so, you must pass this header with a value of ``true``. Otherwise, the assumption is that checking authorization against Oxygen groups is not required.
- `x-ads-acm-groups` in `header` (required: False) — Use this header to pass the Oxygen groups you want the OSS Api Proxy to use for group validation for the given user in the OAuth2 token.

#### Responses
- **200**: The object was successfully deleted.
- **404**: NOT FOUND, Bucket does not exist.

---

### List Objects

**Endpoint:** `GET /oss/v2/buckets/{bucketKey}/objects`
**Operation ID:** `get_objects`

#### Description
Returns a list objects in the specified bucket. 

Only the application that owns the bucket can call this operation. All other applications that call this operation will receive a "403 Forbidden" error.

#### Parameters
- Ref: `#/components/parameters/bucketKey`
- Ref: `#/components/parameters/limit`
- `beginsWith` in `query` (required: False) — Filters the results by the value you specify. Only the objects with their ``objectKey`` beginning with the specified string are returned.
- Ref: `#/components/parameters/startAt`

#### Responses
- **200**: The requested objects were returned successfully

---

### Get Object Details

**Endpoint:** `GET /oss/v2/buckets/{bucketKey}/objects/{objectKey}/details`
**Operation ID:** `get_object_details`

#### Description
Returns detailed information about the specified object.

#### Parameters
- Ref: `#/components/parameters/bucketKey`
- Ref: `#/components/parameters/objectKey`
- Ref: `#/components/parameters/If-Modified-Since`
- `x-ads-acm-namespace` in `header` (required: False) — This header is used to let the OSS Api Proxy know if ACM is used to authorize access to the given object. If this authorization is used by your service, then you must provide the name of the namespace you want to validate access control policies against.
- `x-ads-acm-check-groups` in `header` (required: False) — Informs the OSS Api Proxy know if your service requires ACM authorization to also validate against Oxygen groups. If so, you must pass this header with a value of ``true``. Otherwise, the assumption is that checking authorization against Oxygen groups is not required.
- `x-ads-acm-groups` in `header` (required: False) — Use this header to pass the Oxygen groups you want the OSS Api Proxy to use for group validation for the given user in the OAuth2 token.
- Ref: `#/components/parameters/with`

#### Responses
- **200**: OK, Get object details was successful.
- **304**: NOT MODIFIED, The supported formats have not been modified since the specified date.
- **404**: NOT FOUND, Object does not exist.

---

### Generate OSS Signed URL

**Endpoint:** `POST /oss/v2/buckets/{bucketKey}/objects/{objectKey}/signed`
**Operation ID:** `create_signed_resource`

#### Description
Generates a signed URL that can be used to download or upload an object within the specified expiration time. If the object the signed URL points to is deleted or expires before the signed URL expires, the signed URL will no longer be valid.

In addition to this operation that generates OSS signed URLs, OSS provides operations to generate S3 signed URLs. S3 signed URLs allow direct upload/download from S3 but are restricted to bucket owners. OSS signed URLs also allow upload/download and can be configured for access by other applications, making them suitable for sharing objects across applications.

Only the application that owns the bucket containing the object can call this operation.

#### Parameters
- Ref: `#/components/parameters/bucketKey`
- Ref: `#/components/parameters/objectKey`
- Ref: `#/components/parameters/access`
- `useCdn` in `query` (required: False) — ``true`` : Returns a Cloudfront URL to the object instead of an Autodesk URL (one that points to a location on https://developer.api.autodesk.com). Applications can interact with the Cloudfront URL exactly like with any classic public resource in OSS. They can use GET requests to download objects or PUT requests to upload objects.

``false`` : (Default) Returns an Autodesk URL (one that points to a location on https://developer.api.autodesk.com) to the object.

#### Request Body
- Required: `False`
- Content-Type: `application/json`
  - Schema: `#/components/schemas/create_signed_resource`

#### Responses
- **200**: OK, Success

---

### Download Object Using Signed URL

**Endpoint:** `GET /oss/v2/signedresources/{hash}`
**Operation ID:** `get_signed_resource`

#### Description
Downloads an object using an OSS signed URL.

**Note:** The signed URL returned by [Generate OSS Signed URL](/en/docs/data/v2/reference/http/signedresources-:id-GET/)  contains the ``hash`` URI parameter as well.

#### Parameters
- `Range` in `header` (required: False) — The byte range to download, specified in the form ``bytes=<START_BYTE>-<END_BYTE>``.
- Ref: `#/components/parameters/If-None-Match`
- Ref: `#/components/parameters/If-Modified-Since`
- `Accept-Encoding` in `header` (required: False) — The compression format your prefer to receive the data. Possible values are:

- ``gzip`` - Use the gzip format

**Note:** You cannot use ``Accept-Encoding:gzip`` with a Range header containing an end byte range. OSS will not honor the End byte range if ``Accept-Encoding: gzip`` header is used.
- Ref: `#/components/parameters/region`
- `response-content-disposition` in `query` (required: False) — The value of the Content-Disposition header you want to receive when you download the object using the signed URL. If you do not specify a value, the Content-Disposition header defaults to the value stored with OSS.
- `response-content-type` in `query` (required: False) — The value of the Content-Type header you want to receive when you download the object using the signed URL. If you do not specify a value, the Content-Type header defaults to the value stored with OSS.

#### Responses
- **206**: PARTIAL CONTENT, Partial content of the object is returned as requested.
- **416**: RANGE NOT SATISFIABLE, Request included a Range header that is not valid for this object.

---

### Replace Object Using Signed URL

**Endpoint:** `PUT /oss/v2/signedresources/{hash}`
**Operation ID:** `upload_signed_resource`

#### Description
Replaces an object that already exists on OSS, using an OSS signed URL. 

The signed URL must fulfil the following conditions:

- The signed URL is valid (it has not expired as yet).
- It was generated with ``write`` or ``readwrite`` for the ``access`` parameter.

#### Parameters
- `Content-Type` in `header` (required: False) — The MIME type of the object to upload; can be any type except 'multipart/form-data'. This can be omitted, but we recommend adding it.
- `Content-Length` in `header` (required: True) — The size of the data contained in the request body, in bytes.
- `Content-Disposition` in `header` (required: False) — The suggested file name to use when this object is downloaded as a file.
- Ref: `#/components/parameters/x-ads-region-4-object`
- `If-Match` in `header` (required: False) — The current value of the ``sha1`` attribute of the object you want to replace. OSS checks the ``If-Match`` header against the ``sha1`` attribute of the object in OSS. If they match, OSS allows the object to be overwritten. Otherwise, it means that the object on OSS has been modified since you retrieved the ``sha1`` and the request fails.

#### Request Body
- Required: `True`
- Content-Type: `application/x-www-form-urlencoded`

#### Responses
- **200**: The object was replaced successfully.
- **412**: PRECONDITION FAILED, If the value sent for the `If-Match` header is not equal to the `sha1` value stored in OSS for this object, a Precondition Failed message will be returned.

---

### Delete Object Using Signed URL

**Endpoint:** `DELETE /oss/v2/signedresources/{hash}`
**Operation ID:** `delete_signed_resource`

#### Description
Delete an object using an OSS signed URL to access it.

Only applications that own the bucket containing the object can call this operation.

#### Parameters
- Ref: `#/components/parameters/x-ads-region-4-object`

#### Responses
- **200**: The object was deleted successfully.

---

### Upload Object Using Signed URL

**Endpoint:** `PUT /oss/v2/signedresources/{hash}/resumable`
**Operation ID:** `upload_signed_resources_chunk`

#### Description
Performs a resumable upload using an OSS signed URL. Use this operation to upload an object in chunks.

**Note:** The signed URL returned by [Generate OSS Signed URL](/en/docs/data/v2/reference/http/signedresources-:id-GET/) contains the ``hash`` as a URI parameter.

#### Parameters
- `hash` in `path` (required: True) — The ID component of the signed URL.

**Note:** The signed URL returned by [Generate OSS Signed URL](/en/docs/data/v2/reference/http/signedresources-:id-GET/) contains ``hash`` as a URI parameter.
- `Content-Type` in `header` (required: False) — The MIME type of the object to upload; can be any type except 'multipart/form-data'. This can be omitted, but we recommend adding it.
- `Content-Range` in `header` (required: True) — The byte range to upload, specified in the form ``bytes=<START_BYTE>-<END_BYTE>``.
- `Content-Disposition` in `header` (required: False) — The suggested file name to use when this object is downloaded as a file.
- Ref: `#/components/parameters/x-ads-region-4-object`
- `Session-Id` in `header` (required: True) — An ID to uniquely identify the file upload session.

#### Request Body
- Required: `True`
- Content-Type: `application/x-www-form-urlencoded`

#### Responses
- **200**: Object was uploaded successfully.
- **202**: ACCEPTED, Request accepted but processing not complete. Call this operation iteratively until a 200 is returned.
- **409**: CONFLICT, The specified bucket key already exists.
- **416**: REQUEST RANGE NOT SATISFIABLE, Missing Content-Range header.

---

### Copy Object

**Endpoint:** `PUT /oss/v2/buckets/{bucketKey}/objects/{objectKey}/copyto/{newObjName}`
**Operation ID:** `copyTo`

#### Description
Creates a copy of an object within the bucket.

#### Parameters
- Ref: `#/components/parameters/bucketKey`
- Ref: `#/components/parameters/objectKey`
- `newObjName` in `path` (required: True) — A URL-encoded human friendly name to identify the copied object.
- `x-ads-acm-namespace` in `header` (required: False) — This header is used to let the OSS Api Proxy know if ACM is used to authorize access to the given object. If this authorization is used by your service, then you must provide the name of the namespace you want to validate access control policies against.
- `x-ads-acm-check-groups` in `header` (required: False) — Informs the OSS Api Proxy know if your service requires ACM authorization to also validate against Oxygen groups. If so, you must pass this header with a value of ``true``. Otherwise, the assumption is that checking authorization against Oxygen groups is not required.
- `x-ads-acm-groups` in `header` (required: False) — Use this header to pass the Oxygen groups you want the OSS Api Proxy to use for group validation for the given user in the OAuth2 token.

#### Responses
- **200**: Object was copied successfully.

---

### Generate Signed S3 Download URL

**Endpoint:** `GET /oss/v2/buckets/{bucketKey}/objects/{objectKey}/signeds3download`
**Operation ID:** `signed_s3_download`

#### Description
Gets a signed URL to download an object directly from S3, bypassing OSS servers. This signed URL expires in 2 minutes by default, but you can change this duration if needed.  You must start the download before the signed URL expires. The download itself can take longer. If the download fails after the validity period of the signed URL has elapsed, you can call this operation again to obtain a fresh signed URL.

Only applications that have read access to the object can call this operation.   

You can use range headers with the signed download URL to download the object in chunks. This ability lets you download chunks in parallel, which can result in faster downloads.

If the object you want to download was uploaded in chunks and is still assembling on OSS, you will receive multiple S3 URLs instead of just one. Each URL will point to a chunk. If you prefer to receive a single URL, set the ``public-resource-fallback`` query parameter to ``true``. This setting will make OSS fallback to returning a single signed OSS URL, if assembling is still in progress. 

In addition to this operation that generates S3 signed URLs, OSS provides an operation to generate OSS signed URLs. S3 signed URLs allow direct upload/download from S3 but are restricted to bucket owners. OSS signed URLs also allow upload/download and can be configured for access by other applications, making them suitable for sharing objects across applications.

#### Parameters
- Ref: `#/components/parameters/bucketKey`
- Ref: `#/components/parameters/objectKey`
- `If-None-Match` in `header` (required: False) — The last known ETag value of the object. OSS returns the signed URL only if the ``If-None-Match`` header differs from the ETag value of the object on S3. If not, it returns a 304 "Not Modified" HTTP status.
- `If-Modified-Since` in `header` (required: False) — A timestamp in the HTTP date format (Mon, DD Month YYYY HH:MM:SS GMT). The signed URL is returned only if the object has been modified since the specified timestamp. If not, a 304 (Not Modified) HTTP status is returned.
- `x-ads-acm-scopes` in `header` (required: False) — Optional OSS-compliant scope reference to increase bucket search performance
- `response-content-type` in `query` (required: False) — The value of the Content-Type header you want to receive when you download the object using the signed URL. If you do not specify a value, the Content-Type header defaults to the value stored with OSS.
- `response-content-disposition` in `query` (required: False) — The value of the Content-Disposition header you want to receive when you download the object using the signed URL. If you do not specify a value, the Content-Disposition header defaults to the value stored with OSS.
- `response-cache-control` in `query` (required: False) — The value of the Cache-Control header you want to receive when you download the object using the signed URL. If you do not specify a value, the Cache-Control header defaults to the value stored with OSS.
- `public-resource-fallback` in `query` (required: False) — Specifies how to return the signed URLs, in case the object was uploaded in chunks, and assembling of chunks is not yet complete.

- ``true`` : Return a single signed OSS URL.
- ``false`` : (Default) Return multiple signed S3 URLs, where each URL points to a chunk.
- `minutesExpiration` in `query` (required: False) — The time window (in minutes) the signed URL will remain usable. Acceptable values = 1-60 minutes. Default = 2 minutes.

**Tip:** Use the smallest possible time window to minimize exposure of the signed URL.
- `useCdn` in `query` (required: False) — ``true`` : Returns a URL that points to a CloudFront edge location.

``false`` : (Default) Returns a URL that points directly to the S3 object.
- `redirect` in `query` (required: False) — Generates a HTTP redirection response (Temporary Redirect 307​) using the generated URL.

#### Responses
- **200**: A signed S3 URL was successfully generated.
- **304**: NOT MODIFIED, If-None-Match header matches the object ETag or object has not been modified since the If-Modified-Since date.
- **400**: BAD REQUEST, the request has missing or malformed parameters.
- **401**: UNAUTHORIZED, Invalid authorization header.
- **404**: NOT FOUND, Object or Bucket does not exist.

---

### Batch Generate Signed S3 Upload URLs

**Endpoint:** `POST /oss/v2/buckets/{bucketKey}/objects/batchsigneds3upload`
**Operation ID:** `batch_signed_s3_upload`

#### Description
Creates and returns signed URLs to upload a set of objects directly to S3. These signed URLs expire in 2 minutes by default, but you can change this duration if needed.  You must start uploading the objects before the signed URLs expire. The upload  itself can take longer.

Only the application that owns the bucket can call this operation. All other applications that call this operation will receive a "403 Forbidden" error.

If required, you can request an array of signed URLs for each object, which lets you upload the objects in chunks. Once you upload all chunks you must call the [Complete Batch Upload to S3 Signed URL](/en/docs/data/v2/reference/http/buckets-:bucketKey-objects-:objectKey-batchcompleteupload-POST/) operation to indicate completion. This instructs OSS to assemble the chunks and reconstitute the object on OSS. You must call this operation even if you requested a single signed URL for an object.

If an upload fails after the validity period of a signed URL has elapsed, you can call this operation again to obtain fresh signed URLs. However, you must use the same ``uploadKey`` that was returned when you originally called this operation.

#### Parameters
- Ref: `#/components/parameters/bucketKey`
- `useAcceleration` in `query` (required: False) — ``true`` : (Default) Generates a faster S3 signed URL using Transfer Acceleration.

``false``: Generates a standard S3 signed URL.
- `minutesExpiration` in `query` (required: False) — The time window (in minutes) the signed URL will remain usable. Acceptable values = 1-60 minutes. Default = 2 minutes.

**Tip:** Use the smallest possible time window to minimize exposure of the signed URL.

#### Request Body
- Required: `False`
- Content-Type: `application/json`
  - Schema: `#/components/schemas/batchsigneds3upload_object`

#### Responses
- **200**: The request was successfully processed. The response body will contain objects that indicate the outcome for each object signed URLs were requested for. Objects corresponding to successful request will contain signed URLs. Objects corresponding to failed requests will contain details of the failure.
- **404**: NOT FOUND, Object or Bucket does not exist.

---

### Complete Batch Upload to S3 Signed URLs

**Endpoint:** `POST /oss/v2/buckets/{bucketKey}/objects/batchcompleteupload`
**Operation ID:** `batch_complete_upload`

#### Description
Requests OSS to start reconstituting the set of objects that were uploaded using signed S3 upload URLs. You must call this operation only after all the objects have been uploaded. 

You can specify up to 25 objects in this operation.

#### Parameters
- Ref: `#/components/parameters/bucketKey`

#### Request Body
- Required: `False`
- Content-Type: `application/json`
  - Schema: `#/components/schemas/batchcompleteupload_object`

#### Responses
- **200**: The request was successfully processed. The response body will contain objects that indicate the outcome for each uploaded object.
- **404**: Object or Bucket does not exist.

---

### Batch Generate Signed S3 Download URLs

**Endpoint:** `POST /oss/v2/buckets/{bucketKey}/objects/batchsigneds3download`
**Operation ID:** `batch_signed_s3_download`

#### Description
Creates and returns signed URLs to download a set of objects directly from S3. These signed URLs expire in 2 minutes by default, but you can change this duration if needed.  You must start download the objects before the signed URLs expire. The download itself can take longer.

Only the application that owns the bucket can call this operation. All other applications that call this operation will receive a "403 Forbidden" error.

#### Parameters
- Ref: `#/components/parameters/bucketKey`
- `public-resource-fallback` in `query` (required: False) — Specifies how to return the signed URLs, in case the object was uploaded in chunks, and assembling of chunks is not yet complete.

- ``true`` : Return a single signed OSS URL.
- ``false`` : (Default) Return multiple signed S3 URLs, where each URL points to a chunk.
- `minutesExpiration` in `query` (required: False) — The time window (in minutes) the signed URL will remain usable. Acceptable values = 1-60 minutes. Default = 2 minutes.

**Tip:** Use the smallest possible time window to minimize exposure of the signed URL.

#### Request Body
- Required: `True`
- Content-Type: `application/json`
  - Schema: `#/components/schemas/batchsigneds3download_object`

#### Responses
- **200**: The request was successfully processed. The response body will contain objects that indicate the outcome for each object signed URLs were requested for. Objects corresponding to successful request will contain signed URLs. Objects corresponding to failed requests will contain details of the failure.
- **400**: BAD REQUEST, the request has missing or malformed parameters.
- **404**: NOT FOUND, Object or Bucket does not exist.

---

### Generate Signed S3 Upload URL

**Endpoint:** `GET /oss/v2/buckets/{bucketKey}/objects/{objectKey}/signeds3upload`
**Operation ID:** `signed_s3_upload`

#### Description
Gets a signed URL to upload an object directly to S3, bypassing OSS servers. You can also request an array of signed URLs which lets you upload an object in chunks.

This signed URL expires in 2 minutes by default, but you can change this duration if needed.  You must start the upload before the signed URL expires. The upload itself can take longer. If the upload fails after the validity period of the signed URL has elapsed, you can call this operation again to obtain a fresh signed URL (or an array of signed URLs as the case may be). However, you must use the same ``uploadKey`` that was returned when you originally called this operation. 

Only applications that own the bucket can call this operation.

**Note:** Once you upload all chunks you must call the [Complete Upload to S3 Signed URL](/en/docs/data/v2/reference/http/buckets-:bucketKey-objects-:objectKey-signeds3upload-POST/) operation to indicate completion. This instructs OSS to assemble the chunks and reconstitute the object on OSS. You must call this operation even when using a single signed URL. 

In addition to this operation that generates S3 signed URLs, OSS provides an operation to generate OSS signed URLs. S3 signed URLs allow direct upload/download from S3 but are restricted to bucket owners. OSS signed URLs also allow upload/download and can be configured for access by other applications, making them suitable for sharing objects across applications.

#### Parameters
- `x-ads-acm-scopes` in `header` (required: False) — Optional OSS-compliant scope reference to increase bucket search performance
- `parts` in `query` (required: False) — The number of parts you intend to chunk the object for uploading. OSS will return that many signed URLs, one URL for each chunk. If you do not specify a value you'll get only one URL to upload the entire object.
- `firstPart` in `query` (required: False) — The index of the first chunk to be uploaded.
- `uploadKey` in `query` (required: False) — The ``uploadKey`` of a previously-initiated upload, in order to request more chunk upload URLs for the same upload. If you do not specify a value, OSS will initiate a new upload entirely.
- `minutesExpiration` in `query` (required: False) — The time window (in minutes) the signed URL will remain usable. Acceptable values = 1-60 minutes. Default = 2 minutes.

**Tip:** Use the smallest possible time window to minimize exposure of the signed URL.
- `useAcceleration` in `query` (required: False) — ``true`` : (Default) Generates a faster S3 signed URL using Transfer Acceleration.

``false``: Generates a standard S3 signed URL.

#### Responses
- **200**: Signed URLs were successfully generated.
- **404**: NOT FOUND, Bucket does not exist.

---

### Complete Upload to S3 Signed URL

**Endpoint:** `POST /oss/v2/buckets/{bucketKey}/objects/{objectKey}/signeds3upload`
**Operation ID:** `complete_signed_s3_upload`

#### Description
Requests OSS to assemble and reconstitute the object that was uploaded using signed S3 upload URL. You must call this operation only after all parts/chunks of the object has been uploaded.

#### Parameters
- `Content-Type` in `header` (required: True) — Must be ``application/json``.
- `x-ads-meta-Content-Type` in `header` (required: False) — The Content-Type value for the uploaded object to record within OSS.
- `x-ads-meta-Content-Disposition` in `header` (required: False) — The Content-Disposition value for the uploaded object to record within OSS.
- `x-ads-meta-Content-Encoding` in `header` (required: False) — The Content-Encoding value for the uploaded object to record within OSS.
- `x-ads-meta-Cache-Control` in `header` (required: False) — The Cache-Control value for the uploaded object to record within OSS.
- `x-ads-user-defined-metadata` in `header` (required: False) — Custom metadata to be stored with the object, which can be retrieved later on download or when retrieving object details. Must be a JSON object that is less than 100 bytes.

#### Request Body
- Required: `True`
- Content-Type: `application/json`
  - Schema: `#/components/schemas/completes3upload_body`

#### Responses
- **200**: Upload successfully completed
- **404**: NOT FOUND, Object or Bucket does not exist.

---

## Secure Service Account (SSA)

_Generated from `ssa.yaml`_

APIs to manage Service accounts and keys. 

A service account is an identity that an application can use to make API requests to other services without a user authorizing the requests. A service account is identified by a unique email address and has an Oxygen ID.

A service account has one or more private keys. A private key is generated through an asymmetric cryptography algorithm; the paired public key is stored by Autodesk Identity.

An application can use a service account's private key to generate a JWT token. The JWT token provides proof of implicit authentication and authorization for this service account; an application can exchange it for a three-legged access token for the service service.

General error response from APIs:
```
{
    "title:": "...",
    "detail": "..."
}
```

---

### Create Service Account

**Endpoint:** `POST /authentication/v2/service-accounts`
**Operation ID:** `create-service-account`

#### Description
This API enables a [server-to-server application](https://aps.autodesk.com/en/docs/oauth/v2/developers_guide/App-types/Machine-to-machine/) to create a service account. 
Additionally, an allowlisted Autodesk internal client can create a service account on behalf of a server-to-server application.
To allowlist the client, please reach out to Identity team at [#oxygen](https://autodesk.enterprise.slack.com/archives/C075EFGET) slack channel for assistance.

An application has up to 10 service accounts at any given time.

The API requires a two-legged bearer token with the following scope:`application:service_account:write`.


  ### Service account creation by a server-to-server application
  Request body sample

  ```json
  {
      "name": "test_service_account"
  }
  ```
  

  Errors

  | status code | title                 | detail                                             |
  |-------------|-----------------------|---------------------------------------------------------------|
  | 400         | invalid_request       | The 'name' is empty.                                      |
  | 400         | invalid_request       | The length of the 'name' should be between 5 and 64 characters.|     
  | 400         | invalid_request       | The 'name' contains invalid characters.                   |   
  | 400         | invalid_request       | The 'name' should contain at least one alpha numeric character. |  
  | 400         | invalid_request       | The 'name' already exists.                                      |
  | 401         | unauthorized          | The token has expired or is invalid.                            |                    
  | 401         | unauthorized          | The token should be a two-legged token.                         |
  | 403         | invalid_client        | The client is not allowed to create service accounts on behalf of other server-to-server applications. |
  | 403         | invalid_client        | The client is not a server-to-server application. |
  | 403         | limit_exceeded        | The number of service accounts has exceeded the limit.          |


  ### Service account creation by an allowlisted Autodesk internal client on behalf of a server-to-server application
  Request body sample

  ```json
  {
      "clientId": "BQ9teWlrzwgWetA5Eeog4bWAB5cZp2Zg"
      "name": "test_service_account"
  }
  ```
  
  The value of clientId should be set to the client ID of the server-to-server application.

  Allowlisted Autodesk internal clients are not limited to server-to-server applications.

  Errors

  | status code | title                 | detail                                             |
  |-------------|-----------------------|---------------------------------------------------------------|
  | 400         | invalid_request       | The 'clientId' does not exist.                               |
  | 400         | invalid_request       | The 'clientId' is not a server-to-server application.        |
  | 400         | invalid_request       | The 'name' is empty.                                      |
  | 400         | invalid_request       | The length of the 'name' should be between 5 and 100 characters.|     
  | 400         | invalid_request       | The 'name' contains invalid characters.                   |   
  | 400         | invalid_request       | The 'name' should contain at least one alpha numeric character. |  
  | 400         | invalid_request       | The 'name' already exists.                                      |
  | 401         | unauthorized          | The token has expired or is invalid.                            |                              
  | 401         | unauthorized          | The token should be a two-legged token.                         |
  | 403         | invalid_client        | The client is not allowed to create service accounts on behalf of other server-to-server applications. |
  | 403         | limit_exceeded        | The number of service accounts has exceeded the limit.          |


Upon a successful response, the API returns the service account ID and email. 

The email format in the response is 
```
  <serviceAccountName>@<clientID>.adskserviceaccount.autodesk.com
```

#### Request Body
- Required: `False`
- Content-Type: `application/json`
  - Schema: `#/components/schemas/create-service-account-request`

---

### Get All Service Accounts

**Endpoint:** `GET /authentication/v2/service-accounts`
**Operation ID:** `get-service-accounts`

#### Description
Retrieve all service accounts associated with an application.

If an allowlisted Autodesk internal client wants to retrieve all service accounts on behalf of another client, they should pass the clientId of the owner as a query parameter.

The API requires a two-legged bearer token with the following scope:`application:service_account:read`.

Errors:

| status code | title                 | detail                                   |
|-------------|-----------------------|-----------------------------------------------------|
| 401         | unauthorized          | The token has expired or is invalid.                |
| 401         | unauthorized          | The token should be a two-legged token.             |
| 403	        | invalid_client	      | The client is not allowed to get service accounts on behalf of other server-to-server applications.|

#### Parameters
- `clientId` in `query` (required: False) — 

---

### Get Service Account

**Endpoint:** `GET /authentication/v2/service-accounts/{serviceAccountId}`
**Operation ID:** `get-service-account`

#### Description
Retrieve the details for a service account.

The API requires a two-legged bearer token with the following scope:`application:service_account:read`.

Errors:

 status code  | title                 | detail                                    |  
|-------------|-----------------------|-----------------------------------------------------|
| 401         | unauthorized          | The token has expired or is invalid.                |
| 401         | unauthorized          | The token should be a two-legged token.             | 
| 404         | not_found             | The service account is not found.                   |

#### Parameters
- `serviceAccountId` in `path` (required: True) — The Oxygen ID of the service account

---

### Enable or Disable Service Account

**Endpoint:** `PATCH /authentication/v2/service-accounts/{serviceAccountId}`
**Operation ID:** `enable-service-account`

#### Description
This API facilitates enabling and disabling of a service account.

When a service account is disabled state, it loses its capability to manage its service account key. 
Assertions signed by the key will be treated as invalid.

This API allows to enable a service account that is in a deactivated state.

The API requires a two-legged bearer token with the following scope:`application:service_account:write`.

Errors:

 status code  | title                 | detail                                    |  
|-------------|-----------------------|-----------------------------------------------------|
| 400         | invalid_request       | The service account is already in an enabled state.  |
| 400         | invalid_request       | The service account is already in an disabled state. |
| 401         | unauthorized          | The token has expired or is invalid.                |
| 401         | unauthorized          | The token should be a two-legged token.            | 
| 404         | not_found             | The service account is not found.                   |

#### Parameters
- `serviceAccountId` in `path` (required: True) — The Oxygen ID of the service account

#### Request Body
- Required: `True`
- Content-Type: `application/json`
  - Schema: `#/components/schemas/enable-service-account-request`

---

### Delete Service Account

**Endpoint:** `DELETE /authentication/v2/service-accounts/{serviceAccountId}`
**Operation ID:** `delete-service-account`

#### Description
This API is used to delete an existing service account. When a service account is deleted, all associated keys will also be deleted.


The API requires a two-legged bearer token with the following scope:`application:service_account:write`.

Errors:

| status code | title                 | detail                                                 |
|-------------|-----------------------|-------------------------------------------------------------------|
| 401         | unauthorized          | The token has expired or is invalid.                              |
| 401         | unauthorized          | The token should be a two-legged token.                           | 
| 404         | not_found             | The service account is not found.                                 |

#### Parameters
- `serviceAccountId` in `path` (required: True) — 

---

### Create Keys

**Endpoint:** `POST /authentication/v2/service-accounts/{serviceAccountId}/keys`
**Operation ID:** `create-service-account-key`

#### Description
This API is used to create a service account key. 

A service account key is a public-private key pair, generated using RSA with a key length of 2048 bits by the Identity Authorization Service (AuthZ).

The private key is returned once during its creation. AuthZ only stores the public key.

An service account has up to 3 keys at any given time.

The API requires a two-legged bearer token with the following scope:`application:service_account_key:write`.

The API returns the key in PEM format, as shown below


```
 ----BEGIN PRIVATE KEY-----
 MIIEvgIBADANBg...
 -----END PRIVATE KEY-----
  ```

Errors:

| status code | title                 | detail                                             |
|-------------|-----------------------|---------------------------------------------------------------|
| 400         | invalid_request       | The service account is not currently in an enabled state.     |
| 401         | unauthorized          | The token has expired or is invalid.                          |
| 401         | unauthorized          | The token should be a two-legged token.                       | 
| 403         | limit_exceeded        | The number of keys has exceeded the limit.                    |
| 404         | not_found             | The service account is not found.                             |

#### Parameters
- `serviceAccountId` in `path` (required: True) — Oxgen ID of the service account

---

### Get All Keys

**Endpoint:** `GET /authentication/v2/service-accounts/{serviceAccountId}/keys`
**Operation ID:** `get-private-keys`

#### Description
Lists all keys associated with the service account. This API will only return key metadata and not private or public key.

The API requires a two-legged bearer token with the following scope:`application:service_account_key:read`.

Errors:

| status code | title                 | detail                                   |
|-------------|-----------------------|-----------------------------------------------------|
| 400         | invalid_request       | The service account is not currently in an enabled state.     |
| 401         | unauthorized          | The token has expired or is invalid.                |
| 401         | unauthorized          | The token should be a two-legged token.             | 
| 404         | not_found             | The service account is not found.                   |

#### Parameters
- `serviceAccountId` in `path` (required: True) — The Oxygen ID of the service account

---

### Enable or Disable Key

**Endpoint:** `PATCH /authentication/v2/service-accounts/{serviceAccountId}/keys/{keyId}`
**Operation ID:** `enable-disable-key`

#### Description
This API facilitates enabling and disabling of a service account key.

The API requires a two-legged bearer token with the following scope:`application:service_account_key:write`.

Errors:

 status code  | title                 | detail                                    |  
|-------------|-----------------------|-----------------------------------------------------|
| 400         | invalid_request       | The service account is not currently in an enabled state.|
| 400         | invalid_request       | The key is already in an enabled state.             |
| 400         | invalid_request       | The key is already in an disabled state.            |
| 401         | unauthorized          | The token has expired or is invalid.                |
| 401         | unauthorized          | The token should be a two-legged token.             | 
| 404         | not_found             | The service account is not found.                   |
| 404         | not_found             | The key is not found.                               |

#### Parameters
- `serviceAccountId` in `path` (required: True) — 
- `keyId` in `path` (required: True) — 

#### Request Body
- Required: `True`
- Content-Type: `application/json`
  - Schema: `#/components/schemas/enable-service-account-key-request`

#### Responses
- **204**: No response body.

---

### Delete key

**Endpoint:** `DELETE /authentication/v2/service-accounts/{serviceAccountId}/keys/{keyId}`
**Operation ID:** `delete-key`

#### Description
This API is used to delete an existing key.


The API requires a two-legged bearer token with the following scope:`application:service_account_key:write`.

Errors:
| status code | title                 | detail                                             |
|-------------|-----------------------|---------------------------------------------------------------|
| 400         | invalid_request       | The service account is not currently in an enabled state.     |
| 401         | unauthorized          | The token has expired or is invalid.                          |
| 401         | unauthorized          | The token should be a two-legged token.                       | 
| 404         | not_found             | The service account is not found.                             |
| 404         | not_found             | The key is not found.                                          |

#### Parameters
- `serviceAccountId` in `path` (required: True) — 
- `keyId` in `path` (required: True) — 

---

### Exchanging JWT assertion for token

**Endpoint:** `POST /authentication/v2/token`
**Operation ID:** `exchange-jwt-assertion`

#### Description
Exchange a JWT assertion for access token by calling OAuth2 token management endpoint.


The API is only for confidential clients, it requires Basic Authorization(clientId, client_secret), supporting the inclusion of auth information(client_id, client_secret) either in the header or the body, but not both simultaneously.

JWT token signature will be generated by using RSASSA-PKCS1-V1_5-SIGN with the SHA-256 hash function with the private key for the following input content:

{Base64url encoded header}.{Base64url encoded claim set}

JWT assertion Claims:

| claim name  | value               |
|-------------|---------------------|
| iss         | Client ID           | 
| sub         | Service Account Oxygen ID         | 
| aud         | https://developer.api.autodesk.com/authentication/v2/token         | 
| exp         | Max 5 mins from current time. The value is number containing NumericDate  value as described in [RFC 7519](https://datatracker.ietf.org/doc/html/rfc7519#section-2)          | 
| scope       | Requested Forge API scopes defined in APS scopes [docs](https://aps.autodesk.com/en/docs/oauth/v3/developers_guide/scopes/). The value of the scope parameter is a string array, containing a list of case-sensitive scope name.  Example : ["data:read", "data:write"] | 


JWT assertion headers:

| Header parameter | value               |
|-------------|---------------------|
| kid         | The ID of the key used to sign the assertion           | 
| alg         | RS256           | 



This API is compliant with [RFC7523](https://datatracker.ietf.org/doc/html/rfc7523#section-2.1)

Errors:

| status code | error               | error_description                                                                     |
|-------------|---------------------|---------------------------------------------------------------------------------------|
| 400         | invalid_request     | The token request must specify a valid 'grant_type'.                                  |
| 400         | invalid_request     | The request is missing a required parameter 'assertion'.                              |
| 400         | invalid_grant       | The service account is not currently in an enabled state.                           |
| 400         | invalid_grant       | The 'assertion' is invalid.                                                            |
| 401         | invalid_credentials | The client credentials are invalid.                                                    |

#### Request Body
- Required: `False`
- Content-Type: `application/x-www-form-urlencoded`

#### Responses
- **400**: Invalid request.
- **401**: Unauthorized

---

## Webhooks

_Generated from `webhooks.yaml`_

The Webhooks API enables applications to listen to APS events and receive notifications when they occur. When an event is triggered, the Webhooks service sends a notification to a callback URL you have defined.
You can customize the types of events and resources for which you receive notifications. For example, you can set up a webhook to send notifications when files are modified or deleted in a specified hub or project.
Below is quick summary of this workflow:
1. Identify the data for which you want to receive notifications.
2. Use the Webhooks API to create one or more hooks.
3. The Webhooks service will notify the webhook when there is a change in the data.


---

### Get details of a webhook based on its webhook ID

**Endpoint:** `GET /webhooks/v1/systems/{system}/events/{event}/hooks/{hook_id}`
**Operation ID:** `get-hook-details`

#### Description
Get details of a webhook based on its webhook ID

#### Parameters
- `x-ads-region` in `header` (required: False) — Specifies the geographical location (region) of the server that the request is executed on. Supported values are: ``EMEA``, ``US``. Default is ``US``.
- `region` in `query` (required: False) — Specifies the geographical location (region) of the server that the request is executed on. Supported values are: ``EMEA``, ``US``. Default is ``US``.

The ``x-ads-region`` header also specifies the region. If you specify both, ``x-ads-region`` has precedence.

#### Responses
- **200**: Successful.

---

### Partially update a webhook based on its webhook ID. The only fields that may be updated are: status, filter, hookAttribute, and hookExpiry.

**Endpoint:** `PATCH /webhooks/v1/systems/{system}/events/{event}/hooks/{hook_id}`
**Operation ID:** `patch-system-event-hook`

#### Description
Partially update a webhook based on its webhook ID. The only fields that may be updated are: status, filter, hookAttribute, and hookExpiry.

#### Parameters
- `x-ads-region` in `header` (required: False) — Specifies the geographical location (region) of the server that the request is executed on. Supported values are: ``EMEA``, ``US``. Default is ``US``.
- `region` in `query` (required: False) — Specifies the geographical location (region) of the server that the request is executed on. Supported values are: ``EMEA``, ``US``. Default is ``US``.

The ``x-ads-region`` header also specifies the region. If you specify both, ``x-ads-region`` has precedence.

#### Request Body
- Required: `False`
- Content-Type: `application/json`
  - Schema: `#/components/schemas/ModifyHookPayload`

#### Responses
- **200**: Successful.

---

### Deletes a webhook based on webhook ID

**Endpoint:** `DELETE /webhooks/v1/systems/{system}/events/{event}/hooks/{hook_id}`
**Operation ID:** `delete-system-event-hook`

#### Description
Deletes a webhook based on webhook ID

#### Parameters
- `x-ads-region` in `header` (required: False) — Specifies the geographical location (region) of the server that the request is executed on. Supported values are: ``EMEA``, ``US``. Default is ``US``.
- `region` in `query` (required: False) — Specifies the geographical location (region) of the server that the request is executed on. Supported values are: ``EMEA``, ``US``. Default is ``US``.

The ``x-ads-region`` header also specifies the region. If you specify both, ``x-ads-region`` has precedence.

#### Responses
- **204**: Delete operation is successful.

---

### Retrieves a paginated list of all the webhooks for a specified event. If the pageState query string is not specified, the first page is returned.

**Endpoint:** `GET /webhooks/v1/systems/{system}/events/{event}/hooks`
**Operation ID:** `get-system-event-hooks`

#### Description
Retrieves a paginated list of all the webhooks for a specified event. If the pageState query string is not specified, the first page is returned.

#### Parameters
- `x-ads-region` in `header` (required: False) — Specifies the geographical location (region) of the server that the request is executed on. Supported values are: ``EMEA``, ``US``. Default is ``US``.
- `region` in `query` (required: False) — Specifies the geographical location (region) of the server that the request is executed on. Supported values are: ``EMEA``, ``US``. Default is ``US``.

The ``x-ads-region`` header also specifies the region. If you specify both, ``x-ads-region`` has precedence.
- `scopeName` in `query` (required: False) — Scope name used to create hook. For example : folder
- Ref: `#/components/parameters/pageState`
- Ref: `#/components/parameters/status`

#### Responses
- **200**: Success.
- **204**: No webhooks exist.

---

### Add new webhook to receive the notification on a specified event.

**Endpoint:** `POST /webhooks/v1/systems/{system}/events/{event}/hooks`
**Operation ID:** `create-system-event-hook`

#### Description
Add new webhook to receive the notification on a specified event.

#### Parameters
- `region` in `query` (required: False) — Specifies the geographical location (region) of the server that the request is executed on. Supported values are: ``EMEA``, ``US``. Default is ``US``.

The ``x-ads-region`` header also specifies the region. If you specify both, ``x-ads-region`` has precedence.
- `x-ads-region` in `header` (required: False) — Specifies the geographical location (region) of the server that the request is executed on. Supported values are: ``EMEA``, ``US``. Default is ``US``.

#### Request Body
- Required: `False`
- Content-Type: `application/json`
  - Schema: `#/components/schemas/HookPayload`

#### Responses
- **201**: Successful.
- **409**: The specified hook already exists.

---

### Retrieves a paginated list of all the webhooks for a specified system. If the pageState query string is not specified, the first page is returned.

**Endpoint:** `GET /webhooks/v1/systems/{system}/hooks`
**Operation ID:** `get-system-hooks`

#### Description
Retrieves a paginated list of all the webhooks for a specified system. If the pageState query string is not specified, the first page is returned.

#### Parameters
- `x-ads-region` in `header` (required: False) — Specifies the geographical location (region) of the server that the request is executed on. Supported values are: ``EMEA``, ``US``. Default is ``US``.
- Ref: `#/components/parameters/status`
- Ref: `#/components/parameters/pageState`
- `region` in `query` (required: False) — Specifies the geographical location (region) of the server that the request is executed on. Supported values are: ``EMEA``, ``US``. Default is ``US``.

The ``x-ads-region`` header also specifies the region. If you specify both, ``x-ads-region`` has precedence.

#### Responses
- **200**: Success.
- **204**: No webhooks exist.

---

### Add new webhooks to receive the notification on all the events.

**Endpoint:** `POST /webhooks/v1/systems/{system}/hooks`
**Operation ID:** `create-system-hook`

#### Description
Add new webhooks to receive the notification on all the events.

#### Parameters
- `x-ads-region` in `header` (required: False) — Specifies the geographical location (region) of the server that the request is executed on. Supported values are: ``EMEA``, ``US``. Default is ``US``.
- `region` in `query` (required: False) — Specifies the geographical location (region) of the server that the request is executed on. Supported values are: ``EMEA``, ``US``. Default is ``US``.

The ``x-ads-region`` header also specifies the region. If you specify both, ``x-ads-region`` has precedence.

#### Request Body
- Required: `False`
- Content-Type: `application/json`
  - Schema: `#/components/schemas/HookPayload`

#### Responses
- **201**: Successful creation of one or more hooks.

---

### Retrieves a paginated list of all the webhooks. If the pageState query string is not specified, the first page is returned.

**Endpoint:** `GET /webhooks/v1/hooks`
**Operation ID:** `get-hooks`

#### Description
Retrieves a paginated list of all the webhooks. If the pageState query string is not specified, the first page is returned.

#### Parameters
- `pageState` in `query` (required: False) — Base64 encoded string used to return the next page of the list of webhooks. This can be obtained from the next field of the previous page. PagingState instances are not portable and implementation is subject to change across versions. Default page size is 200.
- `status` in `query` (required: False) — Status of the hooks. Options: ‘active’, ‘inactive’
- `region` in `query` (required: False) — Specifies the geographical location (region) of the server that the request is executed on. Supported values are: ``EMEA``, ``US``. Default is ``US``.

The ``x-ads-region`` header also specifies the region. If you specify both, ``x-ads-region`` has precedence.
- `x-ads-region` in `header` (required: False) — Specifies the geographical location (region) of the server that the request is executed on. Supported values are: EMEA, US. Default is US.

#### Responses
- **200**: Success.
- **204**: No webhooks exist.

---

### Retrieves a paginated list of webhooks created in the context of a Client or Application. This API accepts 2-legged token of the application only. If the pageState query string is not specified, the first page is returned.

**Endpoint:** `GET /webhooks/v1/app/hooks`
**Operation ID:** `get-app-hooks`

#### Description
Retrieves a paginated list of webhooks created in the context of a Client or Application. This API accepts 2-legged token of the application only. If the pageState query string is not specified, the first page is returned.

#### Parameters
- `x-ads-region` in `header` (required: False) — Specifies the geographical location (region) of the server that the request is executed on. Supported values are: ``EMEA``, ``US``. Default is ``US``.
- Ref: `#/components/parameters/pageState`
- Ref: `#/components/parameters/status`
- `sort` in `query` (required: False) — Sort order of the hooks based on last updated time. Options: ‘asc’, ‘desc’. Default is ‘desc’.
- `region` in `query` (required: False) — Specifies the geographical location (region) of the server that the request is executed on. Supported values are: ``EMEA``, ``US``. Default is ``US``.

The ``x-ads-region`` header also specifies the region. If you specify both, ``x-ads-region`` has precedence.

#### Responses
- **200**: Success.

---

### Add a new Webhook secret token

**Endpoint:** `POST /webhooks/v1/tokens`
**Operation ID:** `create-token`

#### Description
Add a new Webhook secret token

#### Parameters
- `x-ads-region` in `header` (required: False) — Specifies the geographical location (region) of the server that the request is executed on. Supported values are: ``EMEA``, ``US``. Default is ``US``.
- `region` in `query` (required: False) — Specifies the geographical location (region) of the server that the request is executed on. Supported values are: ``EMEA``, ``US``. Default is ``US``.

The ``x-ads-region`` header also specifies the region. If you specify both, ``x-ads-region`` has precedence.

#### Request Body
- Required: `False`
- Content-Type: `application/json`
  - Schema: `#/components/schemas/TokenPayload`

#### Responses
- **200**: Successful.
- **400**: The request is invalid. Secret token already exists.

---

### Update an existing Webhook secret token

**Endpoint:** `PUT /webhooks/v1/tokens/@me`
**Operation ID:** `put-token`

#### Description
Update an existing Webhook secret token

#### Parameters
- `x-ads-region` in `header` (required: False) — Specifies the geographical location (region) of the server that the request is executed on. Supported values are: ``EMEA``, ``US``. Default is ``US``.
- `region` in `query` (required: False) — Specifies the geographical location (region) of the server that the request is executed on. Supported values are: ``EMEA``, ``US``. Default is ``US``.

The ``x-ads-region`` header also specifies the region. If you specify both, ``x-ads-region`` has precedence.

#### Request Body
- Required: `False`
- Content-Type: `application/json`
  - Schema: `#/components/schemas/TokenPayload`

#### Responses
- **204**: Successful request but server is not returning any content.

---

### Delete a Webhook secret token

**Endpoint:** `DELETE /webhooks/v1/tokens/@me`
**Operation ID:** `delete-token`

#### Description
Delete a Webhook secret token

#### Parameters
- `x-ads-region` in `header` (required: False) — Specifies the geographical location (region) of the server that the request is executed on. Supported values are: ``EMEA``, ``US``. Default is ``US``.
- `region` in `query` (required: False) — Specifies the geographical location (region) of the server that the request is executed on. Supported values are: ``EMEA``, ``US``. Default is ``US``.

The ``x-ads-region`` header also specifies the region. If you specify both, ``x-ads-region`` has precedence.

#### Responses
- **204**: Successful deletion of secret token.

---


# Examples

# Autodesk Platform Services – OpenAPI REST Example code

## SSA secure service accounts Example code / Get 3LO access token, generate robot service account, alternative 3LO Authentication workflow
- [Secure Service Accounts Example for creating SA accounts, and generating 3LO access tokens in 3 languages (SSA)](https://developer.doc.autodesk.com/bPlouYTd/cloud-platform-ssa-docs-main-460369/ssa/v1/tutorials/getting-started-with-ssa/about-this-walkthrough.html)
