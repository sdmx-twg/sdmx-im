SDMX Standards: Section 3A PART I

SDMX-ML:

Schema and Documentation

Message Namespace

Version 2.1

April 2011

© SDMX 2011

http://www.sdmx.org/

Contents
========

`1 Introduction 1 <#introduction>`__

`2 Schema Documentation 1 <#schema-documentation>`__

`2.1 Message Namespace 1 <#message-namespace>`__

`2.1.1 Summary 1 <#summary>`__

`2.1.2 Global Elements 2 <#global-elements>`__

`2.1.3 Complex Types 6 <#complex-types>`__

`2.1.4 Simple Types 43 <#simple-types>`__

`2.2 Message Footer Namespace 44 <#message-footer-namespace>`__

`2.2.1 Summary 44 <#summary-1>`__

`2.2.2 Global Elements 44 <#global-elements-1>`__

`2.2.3 Complex Types 44 <#complex-types-1>`__

`2.2.4 Simple Types 45 <#simple-types-1>`__

Introduction
============

At the core of the SDMX XML messages are the message namespaces. These
namespaces define the general structure of all messages and define the
specific messages that are available for exchange in SDMX.

There are two namespaces associated with the messages. The main
namespace schema which defines every message in SDMX is
http://www.sdmx.org/resources/sdmxml/schemas/v2_1/message. Associated
with this is another sub-namespace,
http://www.sdmx.org/resources/sdmxml/schemas/v2_1/message/footer. This
namespace defines footer level information that is available in messages
which might require non-standard payload information to be transmitted.

In general, every message in SDMX follows common format of:

-  Header

-  Payload (0..n)

-  Footer (0..1)

The header and payload elements exist in the message namespace, but the
content of the payload is defined in the namespaces that are specific
the functionality of the messages. Note that the header follows a common
construct, which is then restricted according to the requirements of the
message which is using it.

Schema Documentation
====================

Message Namespace
-----------------

**http://www.sdmx.org/resources/sdmxml/schemas/v2_1/message**

Summary
~~~~~~~

Referenced Namespaces:

============================================================================ ==========
**Namespace**                                                                **Prefix**
============================================================================ ==========
http://www.sdmx.org/resources/sdmxml/schemas/v2_1/common                     com
http://www.sdmx.org/resources/sdmxml/schemas/v2_1/data/generic               dat
http://www.sdmx.org/resources/sdmxml/schemas/v2_1/data/structurespecific     dsd
http://www.sdmx.org/resources/sdmxml/schemas/v2_1/message/footer             ftr
http://www.sdmx.org/resources/sdmxml/schemas/v2_1/metadata/generic           rep
http://www.sdmx.org/resources/sdmxml/schemas/v2_1/metadata/structurespecific msd
http://www.sdmx.org/resources/sdmxml/schemas/v2_1/query                      qry
http://www.sdmx.org/resources/sdmxml/schemas/v2_1/registry                   ref
http://www.sdmx.org/resources/sdmxml/schemas/v2_1/structure                  str
http://www.w3.org/2001/XMLSchema                                             xs
============================================================================ ==========

Contents:

| 44 Global Elements
| 56 Complex Types
| 1 Simple Type

Global Elements
~~~~~~~~~~~~~~~

**Structure (StructureType): **\ Structure is a message that contains
structural metadata. It may contain any of the following;
categorisations, category schemes, code lists, concepts (concept schemes
and stand-alone concepts), constraints (attachment and content) data
flows, hierarchical code lists, metadata flows, metadata structure
definitions, organisation schemes, processes, reporting taxonomies, and
structure sets.

**GenericData (GenericDataType): **\ GenericData is used to convey data
in a non data structure specific form. Data sets in this message will be
each have a related structure specification in the header, which states
the data structure the data conforms to and how the data is organised
(i.e. the observation dimension).

**GenericTimeSeriesData
(GenericTimeSeriesDataType): **\ GenericTimeSeriesData is a special
derivation of the generic data message which only allows for time series
oriented date (i.e. the observation dimension must be time). Although
this is a different message, the content of this message will be exactly
the same as a generic data message that specifies time as the
observation dimension; therefore no additional processing requirements
are necessary. This message is intended to only be used when it is
necessary to restrict an exchange to being only time series based data.

**StructureSpecificData
(StructureSpecificDataType): **\ StructureSpecificData is used to convey
data structure specific according to data structure definition. The
payload of this message (i.e. the data sets) will be based on XML
schemas which are specific to the data structure definition and the
orientation (i.e. the observation dimension) of the data.

**StructureSpecificTimeSeriesData
(StructureSpecificTimeSeriesDataType):** StructureSpecificTimeSeriesData
is a special derivation of the structure specific data message which
only allows for time series oriented date (i.e. the observation
dimension must be time). Although this is a different message, the
content of this message will be exactly the same as a structure specific
data message that specifies time as the observation dimension; therefore
no additional processing requirements are necessary. This message is
intended to only be used when it is necessary to restrict an exchange to
being only time series based data.

**GenericMetadata (GenericMetadataType): **\ GenericMetadata contains
reported metadata in a format which supports any metadata structure
definition.

**StructureSpecificMetadata
(StructureSpecificMetadataType): **\ StructureSpecificMetadata contains
reported metadata in a format which is specific to the metadata
structure definitions which define the structure of the metadata being
reported. This format allows for validation of the metadata against the
intended structure. Note that the each metadata set provided will be
based on a metadata structure specific schema.

**RegistryInterface (RegistryInterfaceType): **\ RegistryInterface is
used to conduct all interactions with the SDMX Registry Services.

**SubmitRegistrationsRequest
(SubmitRegistrationsRequestType): **\ SubmitRegistrationsRequest is sent
to the registry by an agency or data/metadata provider to request on or
more registrations for a data set or metadata set. The data source to be
registered must be accessible to the registry services at an indicated
URL, so that it can be processed by those services.

**SubmitRegistrationsResponse
(SubmitRegistrationsResponseType): **\ SubmitRegistrationsResponse is
sent to the agency or data/metadata provider in response to a
registration requests. It indicates the success or failure of each
registration request, and contains any error messages generated by the
registration service.

**QueryRegistrationRequest
(QueryRegistrationRequestType): **\ QueryRegistrationRequest is used to
query the contents of a registry for data sets and metadata sets. It
specifies whether the result set should include metadata sets, data
sets, or both. The search can be characterized by providing constraints
including reference periods, data regions, and data keys.

**QueryRegistrationResponse
(QueryRegistrationResponseType): **\ QueryRegistrationResponse is sent
as a response to any query of the contents of a registry. The result set
contains a set of links to data and/or metadata If the result set is
null, or there is some other problem with the query, then appropriate
error messages and statuses will be returned.

**SubmitStructureRequest
(SubmitStructureRequestType): **\ SubmitStructureRequest is used to
submit structure definitions to the repository. The structure resources
(key families, agencies, concepts and concept schemes, code lists, etc.)
to be submitted may be communicated in-line or be supplied in a
referenced SDMX-ML Structure messages external to the registry. A
response will indicate status and contain any relevant error
information.

**SubmitStructureResponse
(SubmitStructureResponseType): **\ SubmitStructureResponse is returned
by the registry when a structure submission request is received. It
indicates the status of the submission, and carries any error messages
which are generated, if relevant.

**SubmitSubscriptionsRequest
(SubmitSubscriptionsRequestType): **\ SubmitSubscriptionsRequest
contains one or more requests submitted to the registry to subscribe to
registration and change events for specific registry resources.

**SubmitSubscriptionsResponse
(SubmitSubscriptionsResponseType): **\ SubmitSubscriptionsResponse is
the response to a submit subscriptions request. It contains information
which describes the success or failure of each subscription request,
providing any error messages in the event of failure. If successful, it
returns the registry URN of the subscription, and the
subscriber-assigned ID.

**QuerySubscriptionRequest
(QuerySubscriptionRequestType): **\ QuerySubscriptionRequest is used to
query the registry for the subscriptions of a given organisation.

**QuerySubscriptionResponse
(QuerySubscriptionResponseType): **\ QuerySubscriptionResponse is sent
as a response to a subscription query. If the query is successful, the
details of all subscriptions for the requested organisation are sent.

**NotifyRegistryEvent (NotifyRegistryEventType): **\ NotifyRegistryEvent
is sent by the registry services to subscribers, to notify them of
specific registration and change events. Basic information about the
event, such as the object that triggered it, the time of the event, the
action that took place, and the subscription that triggered the
notification are always sent. Optionally, the details of the changed
object may also be provided.

**StructureSpecificDataQuery
(DataQueryType): **\ StructureSpecificDataQuery is used to query SDMX
compliant databases or web services for structure specific data.

**GenericDataQuery (GenericDataQueryType): **\ GenericDataQuery is used
to query SDMX compliant databases or web services for generic data. This
is actually a specialization of the structured data query, and therfore
can be processed in the same manner.

**GenericTimeSeriesDataQuery
(GenericTimeSeriesDataQueryType): **\ GenericTimeSeriesDataQuery is used
to query SDMX compliant databases or web services for time series only
generic data. This is actually a specialization of the generic data
query, and therfore can be processed in the same manner. This message is
intended to only be used when it is necessary to restrict an exchange to
being only time series based data.

**StructureSpecificTimeSeriesDataQuery
(StructureSpecificTimeSeriesDataQueryType):**\ StructureSpecificTimeSeriesDataQuery
is used to query SDMX compliant databases or web services for time
series only structure specific data. This is actually a specialization
of the structure specific data query, and therfore can be processed in
the same manner. This message is intended to only be used when it is
necessary to restrict an exchange to being only time series based data.

**GenericMetadataQuery (MetadataQueryType): **\ GenericMetadataQuery is
used to query SDMX compliant databases or web services for generic
format reference metadata.

**StructureSpecificMetadataQuery
(MetadataQueryType): **\ StructureSpecificMetadataQuery is used to query
SDMX compliant databases or web services for metadata structure specific
reference metadata.

**DataSchemaQuery (DataSchemaQueryType): **\ DataSchemaQuery is used to
query SDMX compliant databases or web services for data structure
specific schemas for the purpose of validating structured data.

**MetadataSchemaQuery (MetadataSchemaQueryType): **\ MetadataSchemaQuery
is used to query SDMX compliant databases or web services for metadata
structure specific schemas for the purpose of validating structured
metadata.

**StructuresQuery (StructuresQueryType): **\ StructuresQuery is used to
query SDMX compliant databases or web services for any structures based
on simple maintainable object properties (e.g. all objects maintained by
a maintenance agency).

**DataflowQuery (DataflowQueryType): **\ DataflowQuery is used to query
SDMX compliant databases or web services for dataflows.

**MetadataflowQuery (MetadataflowQueryType): **\ MetadataflowQuery is
used to query SDMX compliant databases or web services for metadata
flows.

**DataStructureQuery (DataStructureQueryType): **\ DataStructureQuery is
used to query SDMX compliant databases or web services for data
structures definitions.

**MetadataStructureQuery
(MetadataStructureQueryType): **\ MetadataStructureQuery is used to
query SDMX compliant databases or web services for metadata structure
definitions.

**CategorySchemeQuery (CategorySchemeQueryType): **\ CategorySchemeQuery
is used to query SDMX compliant databases or web services for category
schemes.

**ConceptSchemeQuery (ConceptSchemeQueryType): **\ ConceptSchemeQuery is
used to query SDMX compliant databases or web services for concept
schemes.

**CodelistQuery (CodelistQueryType): **\ CodelistQuery is used to query
SDMX compliant databases or web services for codelists.

**HierarchicalCodelistQuery
(HierarchicalCodelistQueryType): **\ HierarchicalCodelistQuery is used
to query SDMX compliant databases or web services for hierarchical
codelists.

**OrganisationSchemeQuery
(OrganisationSchemeQueryType): **\ OrganisationSchemeQuery is used to
query SDMX compliant databases or web services for organisation schemes.

**ReportingTaxonomyQuery
(ReportingTaxonomyQueryType): **\ ReportingTaxonomyQuery is used to
query SDMX compliant databases or web services for reporting taxonomies.

**StructureSetQuery (StructureSetQueryType): **\ StructureSetQuery is
used to query SDMX compliant databases or web services for structure
sets.

**ProcessQuery (ProcessQueryType): **\ ProcessQuery is used to query
SDMX compliant databases or web services for processes.

**CategorisationQuery (CategorisationQueryType): **\ CategorisationQuery
is used to query SDMX compliant databases or web services for
categorisations.

**ProvisionAgreementQuery
(ProvisionAgreementQueryType): **\ ProvisionAgreementQuery is used to
query SDMX compliant databases or web services for provision agreements.

**ConstraintQuery (ConstraintQueryType): **\ ConstraintQuery is used to
query SDMX compliant databases or web services for constraints.

**Error (ErrorType): **\ Error is used to communicate that an error has
occurred when responding to a request in an non-registry environment.
The content will be a collection of error messages.

Complex Types
~~~~~~~~~~~~~

**MessageType: **\ MessageType is an abstract type which is used by all
of the messages, to allow inheritance of common features. Every message
consists of a mandatory header, followed by optional payload (which may
occur multiple times), and finally an optional footer section for
conveying error, warning, and informational messages.

Content:

Header, {any element with namespace of
http://www.sdmx.org/resources/sdmxml/schemas/v2_1/message}*, ftr:Footer?

Element Documentation:

========== ================ =================
**Name**   **Type**         **Documentation**
========== ================ =================
Header     *BaseHeaderType*
ftr:Footer ftr:FooterType  
========== ================ =================

**StructureType: **\ StructureType defines the contents of a structure
message. The payload is optional since this message may be returned from
a web service with only information in the footer.

Derivation:

| *MessageType* (restriction) 
|    |image0|\ StructureType

Content:

Header, Structures?, ftr:Footer?

Element Documentation:

========== =================== =================
**Name**   **Type**            **Documentation**
========== =================== =================
Header     StructureHeaderType
Structures str:StructuresType 
ftr:Footer ftr:FooterType     
========== =================== =================

**GenericDataType: **\ GenericDataType defines the contents of a generic
data message.

Derivation:

| *MessageType* (restriction) 
|    |image1|\ GenericDataType

Content:

Header, DataSet*, ftr:Footer?

Element Documentation:

========== ====================== =================
**Name**   **Type**               **Documentation**
========== ====================== =================
Header     GenericDataHeaderTyp e
DataSet    dat:DataSetType       
ftr:Footer ftr:FooterType        
========== ====================== =================

**GenericTimeSeriesDataType: **\ GenericTimeSeriesDataType defines the
structure of the generic time series data message.

Derivation:

| *MessageType* (restriction) 
|    |image2|\ GenericDataType (restriction) 
|          |image3|\ GenericTimeSeriesDataType

Content:

Header, DataSet*, ftr:Footer?

Element Documentation:

========== ================================ =================
**Name**   **Type**                         **Documentation**
========== ================================ =================
Header     GenericTimeSeriesDat aHeaderType
DataSet    dat: TimeSeriesDataSetTyp e     
ftr:Footer ftr:FooterType                  
========== ================================ =================

**StructureSpecificDataType: **\ StructureSpecificDataType defines the
structure of the structure specific data message. Note that the data set
payload type is abstract, and therefore it will have to be assigned a
type in an instance. This type must be derived from the base type
referenced. This base type defines a general structure which can be
followed to allow for generic processing of the data even if the exact
details of the data structure specific format are not known.

Derivation:

| *MessageType* (restriction) 
|    |image4|\ StructureSpecificDataType

Content:

Header, DataSet*, ftr:Footer?

Element Documentation:

========== ================================ =================
**Name**   **Type**                         **Documentation**
========== ================================ =================
Header     StructureSpecificDat aHeaderType
DataSet    *dsd:DataSetType*               
ftr:Footer ftr:FooterType                  
========== ================================ =================

**StructureSpecificTimeSeriesDataType: **\ StructureSpecificTimeSeriesDataType
defines the structure of the structure specific time series data
message.

Derivation:

| *MessageType* (restriction) 
|    |image5|\ StructureSpecificDataType (restriction) 
|          |image6|\ StructureSpecificTimeSeriesDataType

Content:

Header, DataSet*, ftr:Footer?

Element Documentation:

========== =========================================== =================
**Name**   **Type**                                    **Documentation**
========== =========================================== =================
Header     StructureSpecificTim eSeriesDataHeaderTyp e
DataSet    *dsd: TimeSeriesDataSetTyp e*              
ftr:Footer ftr:FooterType                             
========== =========================================== =================

**GenericMetadataType: **\ GenericMetadataType defines the contents of a
generic metadata message.

Derivation:

| *MessageType* (restriction) 
|    |image7|\ GenericMetadataType

Content:

Header, MetadataSet*, ftr:Footer?

Element Documentation:

=========== ========================== =================
**Name**    **Type**                   **Documentation**
=========== ========================== =================
Header      GenericMetadataHeade rType
MetadataSet rep:MetadataSetType       
ftr:Footer  ftr:FooterType            
=========== ========================== =================

**StructureSpecificMetadataType: **\ StructureSpecificMetadataType
defines the structure of a structure specific metadata message. Note
that the metadata set payload type is abstract, and therefore it will
have to be assigned a type in an instance. This type must be derived
from the base type referenced. This base type defines a general
structure which can be followed to allow for generic processing of the
data even if the exact details of the data structure specific format are
not known.

Derivation:

| *MessageType* (restriction) 
|    |image8|\ StructureSpecificMetadataType

Content:

Header, MetadataSet*, ftr:Footer?

Element Documentation:

=========== ==================================== =================
**Name**    **Type**                             **Documentation**
=========== ==================================== =================
Header      StructureSpecificMet adataHeaderType
MetadataSet *msd:MetadataSetType*               
ftr:Footer  ftr:FooterType                      
=========== ==================================== =================

**RegistryInterfaceType: **\ This is a type which describes a structure
for holding all of the various dedicated registry interface message
types.

Derivation:

| *MessageType* (restriction) 
|    |image9|\ RegistryInterfaceType

Content:

Header, (SubmitRegistrationsRequest \| SubmitRegistrationsResponse \|
QueryRegistrationRequest \| QueryRegistrationResponse \|
SubmitStructureRequest \| SubmitStructureResponse \|
SubmitSubscriptionsRequest \| SubmitSubscriptionsResponse \|
QuerySubscriptionRequest \| QuerySubscriptionResponse \|
NotifyRegistryEvent)?, ftr:Footer?

Element Documentation:

============================ ===================================== =====================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                     **Type**                              **Documentation**
============================ ===================================== =====================================================================================================================================================================================================================================================================================================================================================================================================
Header                       BasicHeaderType                      
SubmitRegistrationsR equest  ref: SubmitRegistrationsR equestType  SubmitRegistrationsRequest is sent to the registry by an agency or data/metadata provider to request one or more registrations for a data set or metadata set. The data source to be registered must be accessible to the registry services at an indicated URL, so that it can be processed by those services.
SubmitRegistrationsR esponse ref: SubmitRegistrationsR esponseType SubmitRegistrationsResponse is sent to the agency or data/metadata provider in response to a submit registrations request. It indicates the success or failure of each registration request, and contains any error messages generated by the registration service.
QueryRegistrationReq uest    ref: QueryRegistrationReq uestType    QueryRegistrationRequest is used to query the contents of a registry for data sets and metadata sets. It specifies whether the result set should include metadata sets, data sets, or both. The search can be characterized by providing constraints including reference periods, data regions, and data keys.
QueryRegistrationRes ponse   ref: QueryRegistrationRes ponseType   QueryRegistrationResponse is sent as a response to any query of the contents of a registry. The result set contains a set of links to data and/or metadata If the result set is null, or there is some other problem with the query, then appropriate error messages and statuses will be returned.
SubmitStructureReque st      ref: SubmitStructureReque stType      SubmitStructureRequest is used to submit structure definitions to the repository. The structure resources (key families, agencies, concepts and concept schemes, code lists, etc.) to be submitted may be communicated in-line or be supplied in a referenced SDMX-ML Structure messages external to the registry. A response will indicate status and contain any relevant error information.
SubmitStructureRespo nse     ref: SubmitStructureRespo nseType     SubmitStructureResponse is returned by the registry when a structure submission request is received. It indicates the status of the submission, and carries any error messages which are generated, if relevant.
SubmitSubscriptionsR equest  ref: SubmitSubscriptionsR equestType  SubmitSubscriptionsRequest contains one or more requests submitted to the registry to subscribe to registration and change events for specific registry resources.
SubmitSubscriptionsR esponse ref: SubmitSubscriptionsR esponseType SubmitSubscriptionsResponse is the response to a submit subscriptions request. It contains information which describes the success or failure of each subscription request, providing any error messages in the event of failure. If successful, it returns the registry URN of the subscription, and the subscriber-assigned ID.
QuerySubscriptionReq uest    ref: QuerySubscriptionReq uestType    QuerySubscriptionRequest is used to query the registry for the subscriptions of a given organisation.
QuerySubscriptionRes ponse   ref: QuerySubscriptionRes ponseType   QuerySubscriptionResponse is sent as a response to a subscription query. If the query is successful, the details of all subscriptions for the requested organisation are sent.
NotifyRegistryEvent          ref: NotifyRegistryEventT ype         NotifyRegistryEvent is sent by the registry services to subscribers, to notify them of specific registration and change events. Basic information about the event, such as the object that triggered it, the time of the event, the action that took place, and the subscription that triggered the notification are always sent. Optionally, the details of the changed object may also be provided.
ftr:Footer                   ftr:FooterType                       
============================ ===================================== =====================================================================================================================================================================================================================================================================================================================================================================================================

**SubmitRegistrationsRequestType: **\ SubmitRegistrationsRequestType
defines the structure of a registry submit registration requests
document.

Derivation:

| *MessageType* (restriction) 
|    |image10|\ RegistryInterfaceType (restriction) 
|          |image11|\ SubmitRegistrationsRequestType

Content:

Header, SubmitRegistrationsRequest

Element Documentation:

=========================== ==================================== ===============================================================================================================================================================================================================================================================================================================
**Name**                    **Type**                             **Documentation**
=========================== ==================================== ===============================================================================================================================================================================================================================================================================================================
Header                      BasicHeaderType                     
SubmitRegistrationsR equest ref: SubmitRegistrationsR equestType SubmitRegistrationsRequest is sent to the registry by an agency or data/metadata provider to request one or more registrations for a data set or metadata set. The data source to be registered must be accessible to the registry services at an indicated URL, so that it can be processed by those services.
=========================== ==================================== ===============================================================================================================================================================================================================================================================================================================

**SubmitRegistrationsResponseType: **\ SubmitRegistrationsResponseType
defines the structure of a registry submit registration response
document.

Derivation:

| *MessageType* (restriction) 
|    |image12|\ RegistryInterfaceType (restriction) 
|          |image13|\ SubmitRegistrationsResponseType

Content:

Header, SubmitRegistrationsResponse, ftr:Footer?

Element Documentation:

============================ ===================================== ===================================================================================================================================================================================================================================================================
**Name**                     **Type**                              **Documentation**
============================ ===================================== ===================================================================================================================================================================================================================================================================
Header                       BasicHeaderType                      
SubmitRegistrationsR esponse ref: SubmitRegistrationsR esponseType SubmitRegistrationsResponse is sent to the agency or data/metadata provider in response to a submit registrations request. It indicates the success or failure of each registration request, and contains any error messages generated by the registration service.
ftr:Footer                   ftr:FooterType                       
============================ ===================================== ===================================================================================================================================================================================================================================================================

**QueryRegistrationRequestType: **\ QueryRegistrationRequestType defines
the structure of a registry query registration request document.

Derivation:

| *MessageType* (restriction) 
|    |image14|\ RegistryInterfaceType (restriction) 
|          |image15|\ QueryRegistrationRequestType

Content:

Header, QueryRegistrationRequest

Element Documentation:

========================= ================================== ==============================================================================================================================================================================================================================================================================================================
**Name**                  **Type**                           **Documentation**
========================= ================================== ==============================================================================================================================================================================================================================================================================================================
Header                    BasicHeaderType                   
QueryRegistrationReq uest ref: QueryRegistrationReq uestType QueryRegistrationRequest is used to query the contents of a registry for data sets and metadata sets. It specifies whether the result set should include metadata sets, data sets, or both. The search can be characterized by providing constraints including reference periods, data regions, and data keys.
========================= ================================== ==============================================================================================================================================================================================================================================================================================================

**QueryRegistrationResponseType: **\ SubmitRegistrationRequestType
defines the structure of a registry submit registration response
document.

Derivation:

| *MessageType* (restriction) 
|    |image16|\ RegistryInterfaceType (restriction) 
|          |image17|\ QueryRegistrationResponseType

Content:

Header, QueryRegistrationResponse, ftr:Footer?

Element Documentation:

========================== =================================== ===================================================================================================================================================================================================================================================================================================
**Name**                   **Type**                            **Documentation**
========================== =================================== ===================================================================================================================================================================================================================================================================================================
Header                     BasicHeaderType                    
QueryRegistrationRes ponse ref: QueryRegistrationRes ponseType QueryRegistrationResponse is sent as a response to any query of the contents of a registry. The result set contains a set of links to data and/or metadata If the result set is null, or there is some other problem with the query, then appropriate error messages and statuses will be returned.
ftr:Footer                 ftr:FooterType                     
========================== =================================== ===================================================================================================================================================================================================================================================================================================

**SubmitStructureRequestType: **\ SubmitStructureRequestType defines the
structure of a registry submit structure request document.

Derivation:

| *MessageType* (restriction) 
|    |image18|\ RegistryInterfaceType (restriction) 
|          |image19|\ SubmitStructureRequestType

Content:

Header, SubmitStructureRequest

Element Documentation:

======================= ================================ ==============================================================================================================================================================================================================================================================================================================================================================================================
**Name**                **Type**                         **Documentation**
======================= ================================ ==============================================================================================================================================================================================================================================================================================================================================================================================
Header                  BasicHeaderType                 
SubmitStructureReque st ref: SubmitStructureReque stType SubmitStructureRequest is used to submit structure definitions to the repository. The structure resources (key families, agencies, concepts and concept schemes, code lists, etc.) to be submitted may be communicated in-line or be supplied in a referenced SDMX-ML Structure messages external to the registry. A response will indicate status and contain any relevant error information.
======================= ================================ ==============================================================================================================================================================================================================================================================================================================================================================================================

**SubmitStructureResponseType: **\ SubmitStructureResponseType defines
the structure of a registry submit registration response document.

Derivation:

| *MessageType* (restriction) 
|    |image20|\ RegistryInterfaceType (restriction) 
|          |image21|\ SubmitStructureResponseType

Content:

Header, SubmitStructureResponse, ftr:Footer?

Element Documentation:

======================== ================================= ================================================================================================================================================================================================================
**Name**                 **Type**                          **Documentation**
======================== ================================= ================================================================================================================================================================================================================
Header                   BasicHeaderType                  
SubmitStructureRespo nse ref: SubmitStructureRespo nseType SubmitStructureResponse is returned by the registry when a structure submission request is received. It indicates the status of the submission, and carries any error messages which are generated, if relevant.
ftr:Footer               ftr:FooterType                   
======================== ================================= ================================================================================================================================================================================================================

**SubmitSubscriptionsRequestType: **\ SubmitSubscriptionsRequestType
defines the structure of a registry submit subscription request
document.

Derivation:

| *MessageType* (restriction) 
|    |image22|\ RegistryInterfaceType (restriction) 
|          |image23|\ SubmitSubscriptionsRequestType

Content:

Header, SubmitSubscriptionsRequest

Element Documentation:

=========================== ==================================== ==================================================================================================================================================================
**Name**                    **Type**                             **Documentation**
=========================== ==================================== ==================================================================================================================================================================
Header                      BasicHeaderType                     
SubmitSubscriptionsR equest ref: SubmitSubscriptionsR equestType SubmitSubscriptionsRequest contains one or more requests submitted to the registry to subscribe to registration and change events for specific registry resources.
=========================== ==================================== ==================================================================================================================================================================

**SubmitSubscriptionsResponseType: **\ SubmitSubscriptionsResponseType
defines the structure of a registry submit subscription response
document.

Derivation:

| *MessageType* (restriction) 
|    |image24|\ RegistryInterfaceType (restriction) 
|          |image25|\ SubmitSubscriptionsResponseType

Content:

Header, SubmitSubscriptionsResponse, ftr:Footer?

Element Documentation:

============================ ===================================== =================================================================================================================================================================================================================================================================================================================================
**Name**                     **Type**                              **Documentation**
============================ ===================================== =================================================================================================================================================================================================================================================================================================================================
Header                       BasicHeaderType                      
SubmitSubscriptionsR esponse ref: SubmitSubscriptionsR esponseType SubmitSubscriptionsResponse is the response to a submit subscriptions request. It contains information which describes the success or failure of each subscription request, providing any error messages in the event of failure. If successful, it returns the registry URN of the subscription, and the subscriber-assigned ID.
ftr:Footer                   ftr:FooterType                       
============================ ===================================== =================================================================================================================================================================================================================================================================================================================================

**QuerySubscriptionRequestType: **\ QuerySubscriptionRequestType defines
the structure of a registry query subscription request document.

Derivation:

| *MessageType* (restriction) 
|    |image26|\ RegistryInterfaceType (restriction) 
|          |image27|\ QuerySubscriptionRequestType

Content:

Header, QuerySubscriptionRequest

Element Documentation:

========================= ================================== =====================================================================================================
**Name**                  **Type**                           **Documentation**
========================= ================================== =====================================================================================================
Header                    BasicHeaderType                   
QuerySubscriptionReq uest ref: QuerySubscriptionReq uestType QuerySubscriptionRequest is used to query the registry for the subscriptions of a given organisation.
========================= ================================== =====================================================================================================

**QuerySubscriptionResponseType: **\ QuerySubscriptionResponseType
defines the structure of a registry query subscription response
document.

Derivation:

| *MessageType* (restriction) 
|    |image28|\ RegistryInterfaceType (restriction) 
|          |image29|\ QuerySubscriptionResponseType

Content:

Header, QuerySubscriptionResponse, ftr:Footer?

Element Documentation:

========================== =================================== ==============================================================================================================================================================================
**Name**                   **Type**                            **Documentation**
========================== =================================== ==============================================================================================================================================================================
Header                     BasicHeaderType                    
QuerySubscriptionRes ponse ref: QuerySubscriptionRes ponseType QuerySubscriptionResponse is sent as a response to a subscription query. If the query is successful, the details of all subscriptions for the requested organisation are sent.
ftr:Footer                 ftr:FooterType                     
========================== =================================== ==============================================================================================================================================================================

**NotifyRegistryEventType: **\ NotifyRegistryEventType defines the
structure of a registry notification document.

Derivation:

| *MessageType* (restriction) 
|    |image30|\ RegistryInterfaceType (restriction) 
|          |image31|\ NotifyRegistryEventType

Content:

Header, NotifyRegistryEvent

Element Documentation:

=================== ============================= =====================================================================================================================================================================================================================================================================================================================================================================================================
**Name**            **Type**                      **Documentation**
=================== ============================= =====================================================================================================================================================================================================================================================================================================================================================================================================
Header              BasicHeaderType              
NotifyRegistryEvent ref: NotifyRegistryEventT ype NotifyRegistryEvent is sent by the registry services to subscribers, to notify them of specific registration and change events. Basic information about the event, such as the object that triggered it, the time of the event, the action that took place, and the subscription that triggered the notification are always sent. Optionally, the details of the changed object may also be provided.
=================== ============================= =====================================================================================================================================================================================================================================================================================================================================================================================================

**DataQueryType: **\ DataQueryType defines the structure of a data query
message.

Derivation:

| *MessageType* (restriction) 
|    |image32|\ DataQueryType

Content:

Header, Query

Element Documentation:

======== ================= =================
**Name** **Type**          **Documentation**
======== ================= =================
Header   BasicHeaderType  
Query    qry:DataQueryType
======== ================= =================

**GenericDataQueryType: **\ DataQueryType defines the structure of a
generic data query message.

Derivation:

| *MessageType* (restriction) 
|    |image33|\ DataQueryType (restriction) 
|          |image34|\ GenericDataQueryType

Content:

Header, Query

Element Documentation:

======== ========================= =================
**Name** **Type**                  **Documentation**
======== ========================= =================
Header   BasicHeaderType          
Query    qry: GenericDataQueryType
======== ========================= =================

**GenericTimeSeriesDataQueryType: **\ GenericTimeSeriesDataQueryType
defines the structure of a time series generic data query message.

Derivation:

| *MessageType* (restriction) 
|    |image35|\ DataQueryType (restriction) 
|          |image36|\ GenericDataQueryType (restriction) 
|                |image37|\ GenericTimeSeriesDataQueryType

Content:

Header, Query

Element Documentation:

======== ==================================== =================
**Name** **Type**                             **Documentation**
======== ==================================== =================
Header   BasicHeaderType                     
Query    qry: GenericTimeSeriesDat aQueryType
======== ==================================== =================

**StructureSpecificTimeSeriesDataQueryType: **\ StructureSpecificTimeSeriesDataQueryType
defines the structure of a time series generic data query message.

Derivation:

| *MessageType* (restriction) 
|    |image38|\ DataQueryType (restriction) 
|          |image39|\ StructureSpecificTimeSeriesDataQueryType

Content:

Header, Query

Element Documentation:

======== ============================= =================
**Name** **Type**                      **Documentation**
======== ============================= =================
Header   BasicHeaderType              
Query    qry: TimeSeriesDataQueryT ype
======== ============================= =================

**MetadataQueryType: **\ MetadataQueryType defines the structure of a
reference metadata query message.

Derivation:

| *MessageType* (restriction) 
|    |image40|\ MetadataQueryType

Content:

Header, Query

Element Documentation:

======== ====================== =================
**Name** **Type**               **Documentation**
======== ====================== =================
Header   BasicHeaderType       
Query    qry: MetadataQueryType
======== ====================== =================

**DataSchemaQueryType: **\ DataSchemaQueryType defines the structure of
a data schema query message.

Derivation:

| *MessageType* (restriction) 
|    |image41|\ DataSchemaQueryType

Content:

Header, Query

Element Documentation:

======== ======================== =================
**Name** **Type**                 **Documentation**
======== ======================== =================
Header   BasicHeaderType         
Query    qry: DataSchemaQueryType
======== ======================== =================

**MetadataSchemaQueryType: **\ MetadataSchemaQueryType defines the
structure of a metadata schema query message.

Derivation:

| *MessageType* (restriction) 
|    |image42|\ MetadataSchemaQueryType

Content:

Header, Query

Element Documentation:

======== ============================= =================
**Name** **Type**                      **Documentation**
======== ============================= =================
Header   BasicHeaderType              
Query    qry: MetadataSchemaQueryT ype
======== ============================= =================

**StructuresQueryType: **\ StructuresQueryType defines the structure of
a structures query message.

Derivation:

| *MessageType* (restriction) 
|    |image43|\ StructuresQueryType

Content:

Header, Query

Element Documentation:

======== ======================== =================
**Name** **Type**                 **Documentation**
======== ======================== =================
Header   BasicHeaderType         
Query    qry: StructuresQueryType
======== ======================== =================

**DataflowQueryType: **\ DataflowQueryType defines the structure of a
dataflow query message.

Derivation:

| *MessageType* (restriction) 
|    |image44|\ DataflowQueryType

Content:

Header, Query

Element Documentation:

======== ====================== =================
**Name** **Type**               **Documentation**
======== ====================== =================
Header   BasicHeaderType       
Query    qry: DataflowQueryType
======== ====================== =================

**MetadataflowQueryType: **\ MetadataflowQueryType defines the structure
of a metadata flow query message.

Derivation:

| *MessageType* (restriction) 
|    |image45|\ MetadataflowQueryType

Content:

Header, Query

Element Documentation:

======== =========================== =================
**Name** **Type**                    **Documentation**
======== =========================== =================
Header   BasicHeaderType            
Query    qry: MetadataflowQueryTyp e
======== =========================== =================

**DataStructureQueryType: **\ KeyFamilyQueryType defines the structure
of a data structure query message.

Derivation:

| *MessageType* (restriction) 
|    |image46|\ DataStructureQueryType

Content:

Header, Query

Element Documentation:

======== ============================ =================
**Name** **Type**                     **Documentation**
======== ============================ =================
Header   BasicHeaderType             
Query    qry: DataStructureQueryTy pe
======== ============================ =================

**MetadataStructureQueryType: **\ MetadataStructureQueryType defines the
structure of a metadata structure query message.

Derivation:

| *MessageType* (restriction) 
|    |image47|\ MetadataStructureQueryType

Content:

Header, Query

Element Documentation:

======== ================================ =================
**Name** **Type**                         **Documentation**
======== ================================ =================
Header   BasicHeaderType                 
Query    qry: MetadataStructureQue ryType
======== ================================ =================

**CategorySchemeQueryType: **\ CategorySchemeQueryType defines the
structure of a category scheme query message.

Derivation:

| *MessageType* (restriction) 
|    |image48|\ CategorySchemeQueryType

Content:

Header, Query

Element Documentation:

======== ============================= =================
**Name** **Type**                      **Documentation**
======== ============================= =================
Header   BasicHeaderType              
Query    qry: CategorySchemeQueryT ype
======== ============================= =================

**ConceptSchemeQueryType: **\ ConceptSchemeQueryType defines the
structure of a concept scheme query message.

Derivation:

| *MessageType* (restriction) 
|    |image49|\ ConceptSchemeQueryType

Content:

Header, Query

Element Documentation:

======== ============================ =================
**Name** **Type**                     **Documentation**
======== ============================ =================
Header   BasicHeaderType             
Query    qry: ConceptSchemeQueryTy pe
======== ============================ =================

**CodelistQueryType: **\ CodelistQueryType defines the structure of a
codelist query message.

Derivation:

| *MessageType* (restriction) 
|    |image50|\ CodelistQueryType

Content:

Header, Query

Element Documentation:

======== ====================== =================
**Name** **Type**               **Documentation**
======== ====================== =================
Header   BasicHeaderType       
Query    qry: CodelistQueryType
======== ====================== =================

**HierarchicalCodelistQueryType: **\ HierarchicalCodelistQueryType
defines the structure of a hierarchical codelist query message.

Derivation:

| *MessageType* (restriction) 
|    |image51|\ HierarchicalCodelistQueryType

Content:

Header, Query

Element Documentation:

======== =================================== =================
**Name** **Type**                            **Documentation**
======== =================================== =================
Header   BasicHeaderType                    
Query    qry: HierarchicalCodelist QueryType
======== =================================== =================

**OrganisationSchemeQueryType: **\ OrganisationSchemeQueryType defines
the structure of an organisation scheme query message.

Derivation:

| *MessageType* (restriction) 
|    |image52|\ OrganisationSchemeQueryType

Content:

Header, Query

Element Documentation:

======== ================================= =================
**Name** **Type**                          **Documentation**
======== ================================= =================
Header   BasicHeaderType                  
Query    qry: OrganisationSchemeQu eryType
======== ================================= =================

**ReportingTaxonomyQueryType: **\ ReportingTaxonomyQueryType defines the
structure of a reporting taxonomy query message.

Derivation:

| *MessageType* (restriction) 
|    |image53|\ ReportingTaxonomyQueryType

Content:

Header, Query

Element Documentation:

======== ================================ =================
**Name** **Type**                         **Documentation**
======== ================================ =================
Header   BasicHeaderType                 
Query    qry: ReportingTaxonomyQue ryType
======== ================================ =================

**StructureSetQueryType: **\ StructureSetQueryType defines the structure
of a structure set query message.

Derivation:

| *MessageType* (restriction) 
|    |image54|\ StructureSetQueryType

Content:

Header, Query

Element Documentation:

======== =========================== =================
**Name** **Type**                    **Documentation**
======== =========================== =================
Header   BasicHeaderType            
Query    qry: StructureSetQueryTyp e
======== =========================== =================

**ProcessQueryType: **\ CategorizationQueryType defines the structure of
a categorization query message.

Derivation:

| *MessageType* (restriction) 
|    |image55|\ ProcessQueryType

Content:

Header, Query

Element Documentation:

======== ==================== =================
**Name** **Type**             **Documentation**
======== ==================== =================
Header   BasicHeaderType     
Query    qry:ProcessQueryType
======== ==================== =================

**CategorisationQueryType: **\ CategorisationQueryType defines the
structure of a categorisation query message.

Derivation:

| *MessageType* (restriction) 
|    |image56|\ CategorisationQueryType

Content:

Header, Query

Element Documentation:

======== ============================= =================
**Name** **Type**                      **Documentation**
======== ============================= =================
Header   BasicHeaderType              
Query    qry: CategorisationQueryT ype
======== ============================= =================

**ProvisionAgreementQueryType: **\ ProvisionAgreementQueryType defines
the structure of a provision agreement query message.

Derivation:

| *MessageType* (restriction) 
|    |image57|\ ProvisionAgreementQueryType

Content:

Header, Query

Element Documentation:

======== ================================= =================
**Name** **Type**                          **Documentation**
======== ================================= =================
Header   BasicHeaderType                  
Query    qry: ProvisionAgreementQu eryType
======== ================================= =================

**ConstraintQueryType: **\ ConstraintQueryType defines the structure of
a constraint query message.

Derivation:

| *MessageType* (restriction) 
|    |image58|\ ConstraintQueryType

Content:

Header, Query

Element Documentation:

======== ======================== =================
**Name** **Type**                 **Documentation**
======== ======================== =================
Header   BasicHeaderType         
Query    qry: ConstraintQueryType
======== ======================== =================

**ErrorType: **\ ErrorType describes the structure of an error response.

Content:

ErrorMessage+

Element Documentation:

============ ============================ ===========================================================================================================================================================================================================================================================================================================================================================
**Name**     **Type**                     **Documentation**
============ ============================ ===========================================================================================================================================================================================================================================================================================================================================================
ErrorMessage com: CodedStatusMessageTy pe ErrorMessage contains the error message. It can occur multiple times to communicate message for multiple errors, or to communicate the error message in parallel languages. If both messages for multiple errors and parallel language messages are used, then each error message should be given a code in order to distinguish message for unique errors.
============ ============================ ===========================================================================================================================================================================================================================================================================================================================================================

**BaseHeaderType: **\ BaseHeaderType in an abstract base type that
defines the basis for all message headers. Specific message formats will
refine this

Content:

ID, Test, Prepared, Sender, Receiver*, com:Name*, Structure*,
DataProvider?, DataSetAction?, DataSetID*, Extracted?, ReportingBegin?,
ReportingEnd?, EmbargoDate?, Source\*

Element Documentation:

============== ================================= ================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**       **Type**                          **Documentation**
============== ================================= ================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
ID             com:IDType                        ID identifies an identification for the message, assigned by the sender.
Test           xs:boolean                        Test indicates whether the message is for test purposes or not.
Prepared       HeaderTimeType                    Prepared is the date the message was prepared.
Sender         SenderType                        Sender is information about the party that is transmitting the message.
Receiver       PartyType                         Receiver is information about the party that is the intended recipient of the message.
com:Name       com:TextType                      Name provides a name for the transmission. Multiple instances allow for parallel language values.
Structure      *com: PayloadStructureType*       Structure provides a reference to the structure (either explicitly or through a structure usage reference) that describes the format of data or reference metadata. In addition to the structure, it is required to also supply the namespace of the structure specific schema that defines the format of the data/metadata. For cross sectional data, additional information is also required to state which dimension is being used at the observation level. This information will allow the structure specific schema to be generated. For generic format messages, this is used to simply reference the underlying structure. It is not mandatory in these cases and the generic data/metadata sets will require this reference explicitly.
DataProvider   com: DataProviderReferenc eType   DataProvider identifies the provider of the data for a data/reference metadata message.
DataSetAction  com:ActionType                    DataSetAction code provides a code for determining whether the enclosed message is an Update or Delete message (not to be used with the UtilityData message).
DataSetID      com:IDType                        DataSetID provides an identifier for a contained data set.
Extracted      xs:dateTime                       Extracted is a time-stamp from the system rendering the data.
ReportingBegin com: ObservationalTimePer iodType ReportingBegin provides the start of the time period covered by the message (in the case of data).
ReportingEnd   com: ObservationalTimePer iodType ReportingEnd provides the end of the time period covered by the message (in the case of data).
EmbargoDate    xs:dateTime                       EmbargoDate holds a time period before which the data included in this message is not available.
Source         com:TextType                      Source provides human-readable information about the source of the data.
============== ================================= ================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================

**StructureHeaderType: **\ StructureHeaderType defines the structure for
structural metadata messages.

Derivation:

| *BaseHeaderType* (restriction) 
|    |image59|\ StructureHeaderType

Content:

ID, Test, Prepared, Sender, Receiver*, com:Name*, Source\*

Element Documentation:

======== ============== =================================================================================================
**Name** **Type**       **Documentation**
======== ============== =================================================================================================
ID       com:IDType     ID identifies an identification for the message, assigned by the sender.
Test     xs:boolean     Test indicates whether the message is for test purposes or not.
Prepared HeaderTimeType Prepared is the date the message was prepared.
Sender   SenderType     Sender is information about the party that is transmitting the message.
Receiver PartyType      Receiver is information about the party that is the intended recipient of the message.
com:Name com:TextType   Name provides a name for the transmission. Multiple instances allow for parallel language values.
Source   com:TextType   Source provides human-readable information about the source of the data.
======== ============== =================================================================================================

**GenericDataHeaderType: **\ GenericDataHeaderType defines the header
structure for a generic data message.

Derivation:

| *BaseHeaderType* (restriction) 
|    |image60|\ GenericDataHeaderType

Content:

ID, Test, Prepared, Sender, Receiver*, com:Name*, Structure+,
DataProvider?, DataSetAction?, DataSetID*, Extracted?, ReportingBegin?,
ReportingEnd?, EmbargoDate?, Source\*

Element Documentation:

============== ================================= ================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**       **Type**                          **Documentation**
============== ================================= ================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
ID             com:IDType                        ID identifies an identification for the message, assigned by the sender.
Test           xs:boolean                        Test indicates whether the message is for test purposes or not.
Prepared       HeaderTimeType                    Prepared is the date the message was prepared.
Sender         SenderType                        Sender is information about the party that is transmitting the message.
Receiver       PartyType                         Receiver is information about the party that is the intended recipient of the message.
com:Name       com:TextType                      Name provides a name for the transmission. Multiple instances allow for parallel language values.
Structure      com: GenericDataStructure Type    Structure provides a reference to the structure (either explicitly or through a structure usage reference) that describes the format of data or reference metadata. In addition to the structure, it is required to also supply the namespace of the structure specific schema that defines the format of the data/metadata. For cross sectional data, additional information is also required to state which dimension is being used at the observation level. This information will allow the structure specific schema to be generated. For generic format messages, this is used to simply reference the underlying structure. It is not mandatory in these cases and the generic data/metadata sets will require this reference explicitly.
DataProvider   com: DataProviderReferenc eType   DataProvider identifies the provider of the data for a data/reference metadata message.
DataSetAction  com:ActionType                    DataSetAction code provides a code for determining whether the enclosed message is an Update or Delete message (not to be used with the UtilityData message).
DataSetID      com:IDType                        DataSetID provides an identifier for a contained data set.
Extracted      xs:dateTime                       Extracted is a time-stamp from the system rendering the data.
ReportingBegin com: ObservationalTimePer iodType ReportingBegin provides the start of the time period covered by the message (in the case of data).
ReportingEnd   com: ObservationalTimePer iodType ReportingEnd provides the end of the time period covered by the message (in the case of data).
EmbargoDate    xs:dateTime                       EmbargoDate holds a time period before which the data included in this message is not available.
Source         com:TextType                      Source provides human-readable information about the source of the data.
============== ================================= ================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================

**GenericTimeSeriesDataHeaderType: **\ GenericTimeSeriesDataHeaderType
defines the header structure for a time series only generic data
message.

Derivation:

| *BaseHeaderType* (restriction) 
|    |image61|\ GenericDataHeaderType (restriction) 
|          |image62|\ GenericTimeSeriesDataHeaderType

Content:

ID, Test, Prepared, Sender, Receiver*, com:Name*, Structure,
DataProvider?, DataSetAction?, DataSetID*, Extracted?, ReportingBegin?,
ReportingEnd?, EmbargoDate?, Source\*

Element Documentation:

============== ======================================== ================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**       **Type**                                 **Documentation**
============== ======================================== ================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
ID             com:IDType                               ID identifies an identification for the message, assigned by the sender.
Test           xs:boolean                               Test indicates whether the message is for test purposes or not.
Prepared       HeaderTimeType                           Prepared is the date the message was prepared.
Sender         SenderType                               Sender is information about the party that is transmitting the message.
Receiver       PartyType                                Receiver is information about the party that is the intended recipient of the message.
com:Name       com:TextType                             Name provides a name for the transmission. Multiple instances allow for parallel language values.
Structure      com: GenericTimeSeriesDat aStructureType Structure provides a reference to the structure (either explicitly or through a structure usage reference) that describes the format of data or reference metadata. In addition to the structure, it is required to also supply the namespace of the structure specific schema that defines the format of the data/metadata. For cross sectional data, additional information is also required to state which dimension is being used at the observation level. This information will allow the structure specific schema to be generated. For generic format messages, this is used to simply reference the underlying structure. It is not mandatory in these cases and the generic data/metadata sets will require this reference explicitly.
DataProvider   com: DataProviderReferenc eType          DataProvider identifies the provider of the data for a data/reference metadata message.
DataSetAction  com:ActionType                           DataSetAction code provides a code for determining whether the enclosed message is an Update or Delete message (not to be used with the UtilityData message).
DataSetID      com:IDType                               DataSetID provides an identifier for a contained data set.
Extracted      xs:dateTime                              Extracted is a time-stamp from the system rendering the data.
ReportingBegin com: ObservationalTimePer iodType        ReportingBegin provides the start of the time period covered by the message (in the case of data).
ReportingEnd   com: ObservationalTimePer iodType        ReportingEnd provides the end of the time period covered by the message (in the case of data).
EmbargoDate    xs:dateTime                              EmbargoDate holds a time period before which the data included in this message is not available.
Source         com:TextType                             Source provides human-readable information about the source of the data.
============== ======================================== ================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================

**StructureSpecificDataHeaderType: **\ StructureSpecificDataHeaderType
defines the header structure for a structure specific data message.

Derivation:

| *BaseHeaderType* (restriction) 
|    |image63|\ StructureSpecificDataHeaderType

Content:

ID, Test, Prepared, Sender, Receiver*, com:Name*, Structure+,
DataProvider?, DataSetAction?, DataSetID*, Extracted?, ReportingBegin?,
ReportingEnd?, EmbargoDate?, Source\*

Element Documentation:

============== ======================================== ================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**       **Type**                                 **Documentation**
============== ======================================== ================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
ID             com:IDType                               ID identifies an identification for the message, assigned by the sender.
Test           xs:boolean                               Test indicates whether the message is for test purposes or not.
Prepared       HeaderTimeType                           Prepared is the date the message was prepared.
Sender         SenderType                               Sender is information about the party that is transmitting the message.
Receiver       PartyType                                Receiver is information about the party that is the intended recipient of the message.
com:Name       com:TextType                             Name provides a name for the transmission. Multiple instances allow for parallel language values.
Structure      com: StructureSpecificDat aStructureType Structure provides a reference to the structure (either explicitly or through a structure usage reference) that describes the format of data or reference metadata. In addition to the structure, it is required to also supply the namespace of the structure specific schema that defines the format of the data/metadata. For cross sectional data, additional information is also required to state which dimension is being used at the observation level. This information will allow the structure specific schema to be generated. For generic format messages, this is used to simply reference the underlying structure. It is not mandatory in these cases and the generic data/metadata sets will require this reference explicitly.
DataProvider   com: DataProviderReferenc eType          DataProvider identifies the provider of the data for a data/reference metadata message.
DataSetAction  com:ActionType                           DataSetAction code provides a code for determining whether the enclosed message is an Update or Delete message (not to be used with the UtilityData message).
DataSetID      com:IDType                               DataSetID provides an identifier for a contained data set.
Extracted      xs:dateTime                              Extracted is a time-stamp from the system rendering the data.
ReportingBegin com: ObservationalTimePer iodType        ReportingBegin provides the start of the time period covered by the message (in the case of data).
ReportingEnd   com: ObservationalTimePer iodType        ReportingEnd provides the end of the time period covered by the message (in the case of data).
EmbargoDate    xs:dateTime                              EmbargoDate holds a time period before which the data included in this message is not available.
Source         com:TextType                             Source provides human-readable information about the source of the data.
============== ======================================== ================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================

**StructureSpecificTimeSeriesDataHeaderType: **\ StructureSpecificTimeSeriesDataHeaderType
defines the header structure for a time series only structure specific
data message.

Derivation:

| *BaseHeaderType* (restriction) 
|    |image64|\ StructureSpecificDataHeaderType (restriction) 
|          |image65|\ StructureSpecificTimeSeriesDataHeaderType

Content:

ID, Test, Prepared, Sender, Receiver*, com:Name*, Structure+,
DataProvider?, DataSetAction?, DataSetID*, Extracted?, ReportingBegin?,
ReportingEnd?, EmbargoDate?, Source\*

Element Documentation:

============== =================================================== ================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**       **Type**                                            **Documentation**
============== =================================================== ================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
ID             com:IDType                                          ID identifies an identification for the message, assigned by the sender.
Test           xs:boolean                                          Test indicates whether the message is for test purposes or not.
Prepared       HeaderTimeType                                      Prepared is the date the message was prepared.
Sender         SenderType                                          Sender is information about the party that is transmitting the message.
Receiver       PartyType                                           Receiver is information about the party that is the intended recipient of the message.
com:Name       com:TextType                                        Name provides a name for the transmission. Multiple instances allow for parallel language values.
Structure      com: StructureSpecificDat aTimeSeriesStructure Type Structure provides a reference to the structure (either explicitly or through a structure usage reference) that describes the format of data or reference metadata. In addition to the structure, it is required to also supply the namespace of the structure specific schema that defines the format of the data/metadata. For cross sectional data, additional information is also required to state which dimension is being used at the observation level. This information will allow the structure specific schema to be generated. For generic format messages, this is used to simply reference the underlying structure. It is not mandatory in these cases and the generic data/metadata sets will require this reference explicitly.
DataProvider   com: DataProviderReferenc eType                     DataProvider identifies the provider of the data for a data/reference metadata message.
DataSetAction  com:ActionType                                      DataSetAction code provides a code for determining whether the enclosed message is an Update or Delete message (not to be used with the UtilityData message).
DataSetID      com:IDType                                          DataSetID provides an identifier for a contained data set.
Extracted      xs:dateTime                                         Extracted is a time-stamp from the system rendering the data.
ReportingBegin com: ObservationalTimePer iodType                   ReportingBegin provides the start of the time period covered by the message (in the case of data).
ReportingEnd   com: ObservationalTimePer iodType                   ReportingEnd provides the end of the time period covered by the message (in the case of data).
EmbargoDate    xs:dateTime                                         EmbargoDate holds a time period before which the data included in this message is not available.
Source         com:TextType                                        Source provides human-readable information about the source of the data.
============== =================================================== ================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================

**GenericMetadataHeaderType: **\ GenericMetadataHeaderType defines the
header format for generic reference metadata.

Derivation:

| *BaseHeaderType* (restriction) 
|    |image66|\ GenericMetadataHeaderType

Content:

ID, Test, Prepared, Sender, Receiver*, com:Name*, Structure+,
DataProvider?, DataSetAction?, DataSetID*, Extracted?, Source\*

Element Documentation:

============= ================================== ================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**      **Type**                           **Documentation**
============= ================================== ================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
ID            com:IDType                         ID identifies an identification for the message, assigned by the sender.
Test          xs:boolean                         Test indicates whether the message is for test purposes or not.
Prepared      HeaderTimeType                     Prepared is the date the message was prepared.
Sender        SenderType                         Sender is information about the party that is transmitting the message.
Receiver      PartyType                          Receiver is information about the party that is the intended recipient of the message.
com:Name      com:TextType                       Name provides a name for the transmission. Multiple instances allow for parallel language values.
Structure     com: GenericMetadataStruc tureType Structure provides a reference to the structure (either explicitly or through a structure usage reference) that describes the format of data or reference metadata. In addition to the structure, it is required to also supply the namespace of the structure specific schema that defines the format of the data/metadata. For cross sectional data, additional information is also required to state which dimension is being used at the observation level. This information will allow the structure specific schema to be generated. For generic format messages, this is used to simply reference the underlying structure. It is not mandatory in these cases and the generic data/metadata sets will require this reference explicitly.
DataProvider  com: DataProviderReferenc eType    DataProvider identifies the provider of the data for a data/reference metadata message.
DataSetAction com:ActionType                     DataSetAction code provides a code for determining whether the enclosed message is an Update or Delete message (not to be used with the UtilityData message).
DataSetID     com:IDType                         DataSetID provides an identifier for a contained data set.
Extracted     xs:dateTime                        Extracted is a time-stamp from the system rendering the data.
Source        com:TextType                       Source provides human-readable information about the source of the data.
============= ================================== ================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================

**StructureSpecificMetadataHeaderType: **\ StructureSpecificMetadataHeaderType
defines the header format for metadata structure definition specific
reference metadata messages.

Derivation:

| *BaseHeaderType* (restriction) 
|    |image67|\ StructureSpecificMetadataHeaderType

Content:

ID, Test, Prepared, Sender, Receiver*, com:Name*, Structure+,
DataProvider?, DataSetAction?, DataSetID*, Extracted?, Source\*

Element Documentation:

============= ============================================ ================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**      **Type**                                     **Documentation**
============= ============================================ ================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
ID            com:IDType                                   ID identifies an identification for the message, assigned by the sender.
Test          xs:boolean                                   Test indicates whether the message is for test purposes or not.
Prepared      HeaderTimeType                               Prepared is the date the message was prepared.
Sender        SenderType                                   Sender is information about the party that is transmitting the message.
Receiver      PartyType                                    Receiver is information about the party that is the intended recipient of the message.
com:Name      com:TextType                                 Name provides a name for the transmission. Multiple instances allow for parallel language values.
Structure     com: StructureSpecificMet adataStructureType Structure provides a reference to the structure (either explicitly or through a structure usage reference) that describes the format of data or reference metadata. In addition to the structure, it is required to also supply the namespace of the structure specific schema that defines the format of the data/metadata. For cross sectional data, additional information is also required to state which dimension is being used at the observation level. This information will allow the structure specific schema to be generated. For generic format messages, this is used to simply reference the underlying structure. It is not mandatory in these cases and the generic data/metadata sets will require this reference explicitly.
DataProvider  com: DataProviderReferenc eType              DataProvider identifies the provider of the data for a data/reference metadata message.
DataSetAction com:ActionType                               DataSetAction code provides a code for determining whether the enclosed message is an Update or Delete message (not to be used with the UtilityData message).
DataSetID     com:IDType                                   DataSetID provides an identifier for a contained data set.
Extracted     xs:dateTime                                  Extracted is a time-stamp from the system rendering the data.
Source        com:TextType                                 Source provides human-readable information about the source of the data.
============= ============================================ ================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================

**BasicHeaderType: **\ BasicHeaderType defines the most basic header
information used in simple message exchanges.

Derivation:

| *BaseHeaderType* (restriction) 
|    |image68|\ BasicHeaderType

Content:

ID, Test, Prepared, Sender, Receiver

Element Documentation:

======== ============== ======================================================================================
**Name** **Type**       **Documentation**
======== ============== ======================================================================================
ID       com:IDType     ID identifies an identification for the message, assigned by the sender.
Test     xs:boolean     Test indicates whether the message is for test purposes or not.
Prepared HeaderTimeType Prepared is the date the message was prepared.
Sender   SenderType     Sender is information about the party that is transmitting the message.
Receiver PartyType      Receiver is information about the party that is the intended recipient of the message.
======== ============== ======================================================================================

**PartyType: **\ PartyType defines the information which is sent about
various parties such as senders and receivers of messages.

Attributes:

id

Content:

com:Name*, Contact\*

Attribute Documentation:

======== ========== =======================================================
**Name** **Type**   **Documentation**
======== ========== =======================================================
id       com:IDType The id attribute holds the identification of the party.
======== ========== =======================================================

Element Documentation:

======== ============ ================================================================================================
**Name** **Type**     **Documentation**
======== ============ ================================================================================================
com:Name com:TextType Name is a human-readable name of the party.
Contact  ContactType  Contact provides contact information for the party in regard to the transmission of the message.
======== ============ ================================================================================================

**SenderType: **\ SenderType extends the basic party structure to add an
optional time zone declaration.

Derivation:

| PartyType (extension) 
|    |image69|\ SenderType

Attributes:

id

Content:

com:Name*, Contact*, Timezone?

Attribute Documentation:

======== ========== =======================================================
**Name** **Type**   **Documentation**
======== ========== =======================================================
id       com:IDType The id attribute holds the identification of the party.
======== ========== =======================================================

Element Documentation:

======== ================ ========================================================================================================================================================================================================================================
**Name** **Type**         **Documentation**
======== ================ ========================================================================================================================================================================================================================================
com:Name com:TextType     Name is a human-readable name of the party.
Contact  ContactType      Contact provides contact information for the party in regard to the transmission of the message.
Timezone com:TimezoneType Timezone specifies the time zone of the sender, and if specified can be applied to all un-time zoned time values in the message. In the absence of this, any dates without time zone are implied to be in an indeterminate "local time".
======== ================ ========================================================================================================================================================================================================================================

**ContactType: **\ ContactType provides defines the contact information
about a party.

Content:

com:Name*, Department*, Role*, (Telephone \| Fax \| X400 \| URI \|
Email)\*

Element Documentation:

========== ============ ============================================================================================================================
**Name**   **Type**     **Documentation**
========== ============ ============================================================================================================================
com:Name   com:TextType Name contains a human-readable name for the contact.
Department com:TextType Department is designation of the organisational structure by a linguistic expression, within which the contact person works.
Role       com:TextType Role is the responsibility of the contact person with respect to the object for which this person is the contact.
Telephone  xs:string    Telephone holds the telephone number for the contact person.
Fax        xs:string    Fax holds the fax number for the contact person.
X400       xs:string    X400 holds the X.400 address for the contact person.
URI        xs:anyURI    URI holds an information URL for the contact person.
Email      xs:string    Email holds the email address for the contact person.
========== ============ ============================================================================================================================

Simple Types
~~~~~~~~~~~~

**HeaderTimeType: **\ Provides a union type of xs:date and xs:dateTime
for the header fields in the message.

Union of:

xs:dateTime, xs:date.

Message Footer Namespace
------------------------

**http://www.sdmx.org/resources/sdmxml/schemas/v2_1/message/footer**

.. _summary-1:

Summary
~~~~~~~

Referenced Namespaces:

======================================================== ==========
**Namespace**                                            **Prefix**
======================================================== ==========
http://www.sdmx.org/resources/sdmxml/schemas/v2_1/common com
http://www.w3.org/2001/XMLSchema                         xs
======================================================== ==========

Contents:

| 1 Global Element
| 2 Complex Types
| 1 Simple Type

.. _global-elements-1:

Global Elements
~~~~~~~~~~~~~~~

**Footer (FooterType)**: Footer is used to communicate information such
as error and warnings after the payload of a message.

.. _complex-types-1:

Complex Types
~~~~~~~~~~~~~

**FooterType**: FooterType describes the structure of a message footer.
The footer is used to convey any error, information, or warning
messages. This is to be used when the message has payload, but also
needs to communicate additional information. If an error occurs and no
payload is generated, an Error message should be returned.

Content:

Message+

Element Documentation:

======== ================= =====================================================================================================================================================================================
**Name** **Type**          **Documentation**
======== ================= =====================================================================================================================================================================================
Message  FooterMessageType Message contains a single error, information, or warning message. A code is provided along with an optional severity. The text of the message can be expressed in multiple languages.
======== ================= =====================================================================================================================================================================================

**FooterMessageType**: FooterMessageType defines the structure of a
message that is contained in the footer of a message. It is a status
message that have a severity code of Error, Information, or Warning
added to it.

Derivation:

| com:StatusMessageType (restriction) 
|    |image70|\ com:CodedStatusMessageType (extension) 
|          |image71|\ FooterMessageType

Attributes:

code, severity?

Content:

com:Text+

Attribute Documentation:

======== ================ ==============================================================================================================================================================================================================================================================================
**Name** **Type**         **Documentation**
======== ================ ==============================================================================================================================================================================================================================================================================
code     xs:string        The code attribute holds an optional code identifying the underlying error that generated the message. This should be used if parallel language descriptions of the error are supplied, to distinguish which of the multiple error messages are for the same underlying error.
severity SeverityCodeType
======== ================ ==============================================================================================================================================================================================================================================================================

Element Documentation:

======== ============ ===================================================================
**Name** **Type**     **Documentation**
======== ============ ===================================================================
com:Text com:TextType Text contains the text of the message, in parallel language values.
======== ============ ===================================================================

.. _simple-types-1:

Simple Types
~~~~~~~~~~~~

**SeverityCodeType**: 

Derived by restriction of xs:string .

.. |image0| image:: ./media-SDMX_2_1_SECTION_3A_PART_I_MESSAGE/media/image2.png
.. |image1| image:: ./media-SDMX_2_1_SECTION_3A_PART_I_MESSAGE/media/image2.png
.. |image2| image:: ./media-SDMX_2_1_SECTION_3A_PART_I_MESSAGE/media/image2.png
.. |image3| image:: ./media-SDMX_2_1_SECTION_3A_PART_I_MESSAGE/media/image2.png
.. |image4| image:: ./media-SDMX_2_1_SECTION_3A_PART_I_MESSAGE/media/image2.png
.. |image5| image:: ./media-SDMX_2_1_SECTION_3A_PART_I_MESSAGE/media/image2.png
.. |image6| image:: ./media-SDMX_2_1_SECTION_3A_PART_I_MESSAGE/media/image2.png
.. |image7| image:: ./media-SDMX_2_1_SECTION_3A_PART_I_MESSAGE/media/image2.png
.. |image8| image:: ./media-SDMX_2_1_SECTION_3A_PART_I_MESSAGE/media/image2.png
.. |image9| image:: ./media-SDMX_2_1_SECTION_3A_PART_I_MESSAGE/media/image2.png
.. |image10| image:: ./media-SDMX_2_1_SECTION_3A_PART_I_MESSAGE/media/image2.png
.. |image11| image:: ./media-SDMX_2_1_SECTION_3A_PART_I_MESSAGE/media/image2.png
.. |image12| image:: ./media-SDMX_2_1_SECTION_3A_PART_I_MESSAGE/media/image2.png
.. |image13| image:: ./media-SDMX_2_1_SECTION_3A_PART_I_MESSAGE/media/image2.png
.. |image14| image:: ./media-SDMX_2_1_SECTION_3A_PART_I_MESSAGE/media/image2.png
.. |image15| image:: ./media-SDMX_2_1_SECTION_3A_PART_I_MESSAGE/media/image2.png
.. |image16| image:: ./media-SDMX_2_1_SECTION_3A_PART_I_MESSAGE/media/image2.png
.. |image17| image:: ./media-SDMX_2_1_SECTION_3A_PART_I_MESSAGE/media/image2.png
.. |image18| image:: ./media-SDMX_2_1_SECTION_3A_PART_I_MESSAGE/media/image2.png
.. |image19| image:: ./media-SDMX_2_1_SECTION_3A_PART_I_MESSAGE/media/image2.png
.. |image20| image:: ./media-SDMX_2_1_SECTION_3A_PART_I_MESSAGE/media/image2.png
.. |image21| image:: ./media-SDMX_2_1_SECTION_3A_PART_I_MESSAGE/media/image2.png
.. |image22| image:: ./media-SDMX_2_1_SECTION_3A_PART_I_MESSAGE/media/image2.png
.. |image23| image:: ./media-SDMX_2_1_SECTION_3A_PART_I_MESSAGE/media/image2.png
.. |image24| image:: ./media-SDMX_2_1_SECTION_3A_PART_I_MESSAGE/media/image2.png
.. |image25| image:: ./media-SDMX_2_1_SECTION_3A_PART_I_MESSAGE/media/image2.png
.. |image26| image:: ./media-SDMX_2_1_SECTION_3A_PART_I_MESSAGE/media/image2.png
.. |image27| image:: ./media-SDMX_2_1_SECTION_3A_PART_I_MESSAGE/media/image2.png
.. |image28| image:: ./media-SDMX_2_1_SECTION_3A_PART_I_MESSAGE/media/image2.png
.. |image29| image:: ./media-SDMX_2_1_SECTION_3A_PART_I_MESSAGE/media/image2.png
.. |image30| image:: ./media-SDMX_2_1_SECTION_3A_PART_I_MESSAGE/media/image2.png
.. |image31| image:: ./media-SDMX_2_1_SECTION_3A_PART_I_MESSAGE/media/image2.png
.. |image32| image:: ./media-SDMX_2_1_SECTION_3A_PART_I_MESSAGE/media/image2.png
.. |image33| image:: ./media-SDMX_2_1_SECTION_3A_PART_I_MESSAGE/media/image2.png
.. |image34| image:: ./media-SDMX_2_1_SECTION_3A_PART_I_MESSAGE/media/image2.png
.. |image35| image:: ./media-SDMX_2_1_SECTION_3A_PART_I_MESSAGE/media/image2.png
.. |image36| image:: ./media-SDMX_2_1_SECTION_3A_PART_I_MESSAGE/media/image2.png
.. |image37| image:: ./media-SDMX_2_1_SECTION_3A_PART_I_MESSAGE/media/image2.png
.. |image38| image:: ./media-SDMX_2_1_SECTION_3A_PART_I_MESSAGE/media/image2.png
.. |image39| image:: ./media-SDMX_2_1_SECTION_3A_PART_I_MESSAGE/media/image2.png
.. |image40| image:: ./media-SDMX_2_1_SECTION_3A_PART_I_MESSAGE/media/image2.png
.. |image41| image:: ./media-SDMX_2_1_SECTION_3A_PART_I_MESSAGE/media/image2.png
.. |image42| image:: ./media-SDMX_2_1_SECTION_3A_PART_I_MESSAGE/media/image2.png
.. |image43| image:: ./media-SDMX_2_1_SECTION_3A_PART_I_MESSAGE/media/image2.png
.. |image44| image:: ./media-SDMX_2_1_SECTION_3A_PART_I_MESSAGE/media/image2.png
.. |image45| image:: ./media-SDMX_2_1_SECTION_3A_PART_I_MESSAGE/media/image2.png
.. |image46| image:: ./media-SDMX_2_1_SECTION_3A_PART_I_MESSAGE/media/image2.png
.. |image47| image:: ./media-SDMX_2_1_SECTION_3A_PART_I_MESSAGE/media/image2.png
.. |image48| image:: ./media-SDMX_2_1_SECTION_3A_PART_I_MESSAGE/media/image2.png
.. |image49| image:: ./media-SDMX_2_1_SECTION_3A_PART_I_MESSAGE/media/image2.png
.. |image50| image:: ./media-SDMX_2_1_SECTION_3A_PART_I_MESSAGE/media/image2.png
.. |image51| image:: ./media-SDMX_2_1_SECTION_3A_PART_I_MESSAGE/media/image2.png
.. |image52| image:: ./media-SDMX_2_1_SECTION_3A_PART_I_MESSAGE/media/image2.png
.. |image53| image:: ./media-SDMX_2_1_SECTION_3A_PART_I_MESSAGE/media/image2.png
.. |image54| image:: ./media-SDMX_2_1_SECTION_3A_PART_I_MESSAGE/media/image2.png
.. |image55| image:: ./media-SDMX_2_1_SECTION_3A_PART_I_MESSAGE/media/image2.png
.. |image56| image:: ./media-SDMX_2_1_SECTION_3A_PART_I_MESSAGE/media/image2.png
.. |image57| image:: ./media-SDMX_2_1_SECTION_3A_PART_I_MESSAGE/media/image2.png
.. |image58| image:: ./media-SDMX_2_1_SECTION_3A_PART_I_MESSAGE/media/image2.png
.. |image59| image:: ./media-SDMX_2_1_SECTION_3A_PART_I_MESSAGE/media/image2.png
.. |image60| image:: ./media-SDMX_2_1_SECTION_3A_PART_I_MESSAGE/media/image2.png
.. |image61| image:: ./media-SDMX_2_1_SECTION_3A_PART_I_MESSAGE/media/image2.png
.. |image62| image:: ./media-SDMX_2_1_SECTION_3A_PART_I_MESSAGE/media/image2.png
.. |image63| image:: ./media-SDMX_2_1_SECTION_3A_PART_I_MESSAGE/media/image2.png
.. |image64| image:: ./media-SDMX_2_1_SECTION_3A_PART_I_MESSAGE/media/image2.png
.. |image65| image:: ./media-SDMX_2_1_SECTION_3A_PART_I_MESSAGE/media/image2.png
.. |image66| image:: ./media-SDMX_2_1_SECTION_3A_PART_I_MESSAGE/media/image2.png
.. |image67| image:: ./media-SDMX_2_1_SECTION_3A_PART_I_MESSAGE/media/image2.png
.. |image68| image:: ./media-SDMX_2_1_SECTION_3A_PART_I_MESSAGE/media/image2.png
.. |image69| image:: ./media-SDMX_2_1_SECTION_3A_PART_I_MESSAGE/media/image2.png
.. |image70| image:: ./media-SDMX_2_1_SECTION_3A_PART_I_MESSAGE/media/image2.png
.. |image71| image:: ./media-SDMX_2_1_SECTION_3A_PART_I_MESSAGE/media/image2.png

