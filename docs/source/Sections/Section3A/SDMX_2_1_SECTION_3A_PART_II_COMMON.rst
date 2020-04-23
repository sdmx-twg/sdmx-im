SDMX Standards: Section 3A PaRT II

SDMX-ML:

Schema and Documentation

Common Namespace

Version 2.1

April 2011

© SDMX 2011

http://www.sdmx.org/

Contents
========

`1 Introduction 1 <#introduction>`__

`2 Schema Documentation 1 <#schema-documentation>`__

`2.1 Common Namespace 1 <#common-namespace>`__

`2.1.1 Summary 1 <#summary>`__

`2.1.2 Global Elements 2 <#global-elements>`__

`2.1.3 Complex Types 6 <#complex-types>`__

`2.1.4 Simple Types 316 <#simple-types>`__

Introduction
============

The common namespace defines a collection of constructs that are reused
across the various components of SDMX. Most important of these are the
referencing mechanism. The goal of the reference construct was to define
a generic structure that could be processed uniformly regardless of the
context where the reference was used. But it was also important that
references be required to be complete whenever possible.

Any object can be referenced either explicitly with a URN or by a set of
complete reference fields. To meet the previously stated requirements,
and very general mechanism was created based on the URN structure of
SDMX objects for these reference fields.

There was also a requirement that the references be able to be refined
to meet particular needs outside of the common namespace. An example of
this is in the metadata structure specific schemas. It is a requirement
that if an target object is specified as having to come from a
particular scheme, that a type based on the reference structure be
created that enforced the requirement.

Typically, this would not have been an issues as all of the components
which make up the references are of atomic types, and therefore can be
expressed as XML attributes which are easily refined and restricted
since the XML Schema design principles in SDMX always treats attributes
as unqualified.

However, the requirement to allow both a URN and/or a complete set of
reference field necessitate that these properties be contained in
elements. The fact that they are elements typically would mean that the
only way a refinement outside of the namespace could happen was if the
element were global and allowed for substitutions. This however would
mean that every distinct type of referenced object would have a unique
set of elements. This moved away from the requirement that the structure
be easy to process regardless of context.

The solution to this problem was to deviate from the normal SDMX XML
Schema design principle of always using qualified elements and allowing
for these to be unqualified. Doing so allows other namespace to derive
from these types and place further restrictions on what can be
referenced. The deviation from this principle was justified in that it
met the all of the requirements and was not deemed to major of a shift
since these properties normally would have been expressed as unqualified
attributes if it weren't for the complete reference requirement.

Schema Documentation
====================

Common Namespace
----------------

**http://www.sdmx.org/resources/sdmxml/schemas/v2_1/common**

Summary
~~~~~~~

Referenced Namespaces:

================================ ==========
**Namespace**                    **Prefix**
================================ ==========
\                               
http://www.w3.org/1999/xhtml    
http://www.w3.org/2001/XMLSchema xs
================================ ==========

Contents:

| 69 Global Elements
| 258 Complex Types
| 76 Simple Types

Global Elements
~~~~~~~~~~~~~~~

**Name (TextType): **\ Name is a reusable element, used for providing a
human-readable name for an object.

**Description (TextType): **\ Description is a reusable element, used
for providing a longer human-readable description of an object.

**Text (TextType): **\ Text is a reusable element, used for providing a
language specific text value for general purposes (i.e. not for a name
or description).

**StructuredText (XHTMLType): **\ StructuredText is a reusable element,
used for providing a language specific text value structured as XHTML.

**Annotations (AnnotationsType): **\ Annotations is a reusable element
the provides for a collection of annotations. It has been made global so
that restrictions of types that extend AnnotatableType my reference it.

**Any (EmptyType): **\ Any is an empty element that denotes an object of
any type.

**Agency (EmptyType): **\ Agency is an empty element that denotes an
agency object.

**AgencyScheme (EmptyType): **\ AgencyScheme is an empty element that
denotes an agency scheme object.

**AttachmentConstraint (EmptyType): **\ AttachmentConstraint is an empty
element that denotes an attachment constraint object.

**Attribute (EmptyType): **\ Attribute is an empty element that denotes
an attribute object.

**AttributeDescriptor (EmptyType): **\ AttributeDescriptor is an empty
element that denotes an attribute descriptor object.

**Categorisation (EmptyType): **\ Categorisation is an empty element
that denotes a categorisation object.

**Category (EmptyType): **\ Category is an empty element that denotes a
category object.

**CategorySchemeMap (EmptyType): **\ CategorySchemeMap is an empty
element that denotes a category scheme map object.

**CategoryScheme (EmptyType): **\ CategoryScheme is an empty element
that denotes a category scheme object.

**Code (EmptyType): **\ Code is an empty element that denotes a code
object.

**CodeMap (EmptyType): **\ CodeMap is an empty element that denotes a
code map object.

**Codelist (EmptyType): **\ Codelist is an empty element that denotes a
code list object.

**CodelistMap (EmptyType): **\ CodelistMap is an empty element that
denotes a code list map object.

**ComponentMap (EmptyType): **\ ComponentMap is an empty element that
denotes a component map object.

**Concept (EmptyType): **\ Concept is an empty element that denotes a
concept object.

**ConceptMap (EmptyType): **\ ConceptMap is an empty element that
denotes a concept map object.

**ConceptScheme (EmptyType): **\ ConceptScheme is an empty element that
denotes a concept scheme object.

**ConceptSchemeMap (EmptyType): **\ ConceptSchemeMap is an empty element
that denotes a concept scheme map object.

**ConstraintTarget (EmptyType): **\ ConstraintTarget is an empty element
that denotes a constraint target object.

**ContentConstraint (EmptyType): **\ ContentConstraint is an empty
element that denotes a content constraint object.

**Dataflow (EmptyType): **\ Dataflow is an empty element that denotes a
data flow object.

**DataConsumer (EmptyType): **\ DataConsumer is an empty element that
denotes a data consumer object.

**DataConsumerScheme (EmptyType): **\ DataConsumerScheme is an empty
element that denotes a data consumer scheme object.

**DataProvider (EmptyType): **\ DataProvider is an empty element that
denotes a data provider object.

**DataProviderScheme (EmptyType): **\ DataProviderScheme is an empty
element that denotes a data provider scheme object.

**DataSetTarget (EmptyType): **\ DataSetTarget is an empty element that
denotes a data set target object.

**DataStructure (EmptyType): **\ DataStructure is an empty element that
denotes a data structure definition object.

**Dimension (EmptyType): **\ Dimension is an empty element that denotes
a dimension object.

**DimensionDescriptor (EmptyType): **\ DimensionDescriptor is an empty
element that denotes a dimension descriptor object.

**DimensionDescriptorValuesTarget
(EmptyType): **\ DimensionDescriptorValuesTarget is an empty element
that denotes a dimension descriptor values target object.

**GroupDimensionDescriptor (EmptyType): **\ GroupDimensionDescriptor is
an empty element that denotes a group dimension descriptor object.

**HierarchicalCode (EmptyType): **\ HierarchicalCode is an empty element
that denotes a hierarchical code object.

**HierarchicalCodelist (EmptyType): **\ HierarchicalCodelist is an empty
element that denotes a hierarchical codelist object.

**Hierarchy (EmptyType): **\ Hierarchy is an empty element that denotes
a hierarchy within a hiearcharchical codelist.

**HybridCodelistMap (EmptyType): **\ HybridCodelistMap is an empty
element that denotes a hybrid codelist map object.

**HybridCodeMap (EmptyType): **\ HybridCodeMap is an empty element that
denotes a hybrid code map object.

**IdentifiableObjectTarget (EmptyType): **\ IdentifiableObjectTarget is
an empty element that denotes an identifiable object target object.

**Level (EmptyType): **\ Level is an empty element that denotes a level
object.

**MeasureDescriptor (EmptyType): **\ MeasureDescriptor is an empty
element that denotes a measure descriptor object.

**MeasureDimension (EmptyType): **\ MeasureDimension is an empty element
that denotes a measure dimension object.

**Metadataflow (EmptyType): **\ Metadataflow is an empty element that
denotes a metadata flow object.

**MetadataAttribute (EmptyType): **\ MetadataAttribute is an empty
element that denotes a metadata attribute object.

**MetadataSet (EmptyType): **\ MetadataSet is an empty element that
denotes a metadata set object.

**MetadataStructure (EmptyType): **\ MetadataStructure is an empty
element that denotes a metadata structure definition object.

**MetadataTarget (EmptyType): **\ MetadataTarget is an empty element
that denotes a metadata target object.

**OrganisationMap (EmptyType): **\ OrganisationMap is an empty element
that denotes an organisation map object.

**OrganisationSchemeMap (EmptyType): **\ OrganisationSchemeMap is an
empty element that denotes an organisation scheme map object.

**OrganisationUnit (EmptyType): **\ OrganisationUnit is an empty element
that denotes an organisation unit object.

**OrganisationUnitScheme (EmptyType): **\ OrganisationUnitScheme is an
empty element that denotes an organisation unit scheme object.

**PrimaryMeasure (EmptyType): **\ PrimaryMeasure is an empty element
that denotes a primary measure object.

**Process (EmptyType): **\ Process is an empty element that denotes a
process object.

**ProcessStep (EmptyType): **\ ProcessStep is an empty element that
denotes a process step object.

**ProvisionAgreement (EmptyType): **\ ProvisionAgreement is an empty
element that denotes a provision agreement object.

**ReportingCategory (EmptyType): **\ ReportingCategory is an empty
element that denotes a reporting category object.

**ReportingCategoryMap (EmptyType): **\ ReportingCategoryMap is an empty
element that denotes a reporting category map object.

**ReportingTaxonomy (EmptyType): **\ ReportingTaxonomy is an empty
element that denotes a reporting taxonomy object.

**ReportingTaxonomyMap (EmptyType): **\ ReportingTaxonomyMap is an empty
element that denotes a reporting taxonomy map object.

**ReportPeriodTarget (EmptyType): **\ ReportPeriodTarget is an empty
element that denotes a report period target object.

**ReportStructure (EmptyType): **\ ReportStructure is an empty element
that denotes a report structure object.

**StructureMap (EmptyType): **\ StructureMap is an empty element that
denotes a structure map object.

**StructureSet (EmptyType): **\ StructureSet is an empty element that
denotes a structure set object.

**TimeDimension (EmptyType): **\ TimeDimension is an empty element that
denotes a time dimension object.

**Transition (EmptyType): **\ Transition is an empty element that
denotes a transition object.

Complex Types
~~~~~~~~~~~~~

**TextType: **\ TextType provides for a set of language-specific
alternates to be provided for any human-readable constructs in the
instance.

Derivation:

| xs:anySimpleType (restriction) 
|    |image0|\ xs:string (extension) 
|          |image1|\ TextType

Attributes:

xml:lang?

Content:

Attribute Documentation:

====================== =========== ==============================================================================================================================
**Name**               **Type**    **Documentation**
====================== =========== ==============================================================================================================================
xml:lang (default: en) xs:language The xml:lang attribute specifies a language code for the text. If not supplied, the default language is assumed to be English.
====================== =========== ==============================================================================================================================

**StatusMessageType: **\ StatusMessageType describes the structure of an
error or warning message. A message contains the text of the message, as
well as an optional language indicator and an optional code.

Attributes:

code?

Content:

Text+

Attribute Documentation:

======== ========= ==============================================================================================================================================================================================================================================================================
**Name** **Type**  **Documentation**
======== ========= ==============================================================================================================================================================================================================================================================================
code     xs:string The code attribute holds an optional code identifying the underlying error that generated the message. This should be used if parallel language descriptions of the error are supplied, to distinguish which of the multiple error messages are for the same underlying error.
======== ========= ==============================================================================================================================================================================================================================================================================

Element Documentation:

======== ======== ===================================================================
**Name** **Type** **Documentation**
======== ======== ===================================================================
Text     TextType Text contains the text of the message, in parallel language values.
======== ======== ===================================================================

**CodedStatusMessageType: **\ CodedStatusMessageType describes the
structure of an error or warning message which required a code.

Derivation:

| StatusMessageType (restriction) 
|    |image2|\ CodedStatusMessageType

Attributes:

code

Content:

Text+

Attribute Documentation:

======== ========= ==============================================================================================================================================================================================================================================================================
**Name** **Type**  **Documentation**
======== ========= ==============================================================================================================================================================================================================================================================================
code     xs:string The code attribute holds an optional code identifying the underlying error that generated the message. This should be used if parallel language descriptions of the error are supplied, to distinguish which of the multiple error messages are for the same underlying error.
======== ========= ==============================================================================================================================================================================================================================================================================

Element Documentation:

======== ======== ===================================================================
**Name** **Type** **Documentation**
======== ======== ===================================================================
Text     TextType Text contains the text of the message, in parallel language values.
======== ======== ===================================================================

**AnnotableType: **\ AnnotableType is an abstract base type used for all
annotable artefacts. Any type that provides for annotations should
extend this type.

Content:

Annotations?

Element Documentation:

=========== =============== ==================================================================================================================================================================================
**Name**    **Type**        **Documentation**
=========== =============== ==================================================================================================================================================================================
Annotations AnnotationsType Annotations is a reusable element the provides for a collection of annotations. It has been made global so that restrictions of types that extend AnnotatableType my reference it.
=========== =============== ==================================================================================================================================================================================

**AnnotationsType: **\ AnnotationsType provides for a list of
annotations to be attached to data and structure messages.

Content:

Annotation+

Element Documentation:

========== ============== =================
**Name**   **Type**       **Documentation**
========== ============== =================
Annotation AnnotationType
========== ============== =================

**AnnotationType: **\ AnnotationType provides for non-documentation
notes and annotations to be embedded in data and structure messages. It
provides optional fields for providing a title, a type description, a
URI, and the text of the annotation.

Attributes:

id?

Content:

AnnotationTitle?, AnnotationType?, AnnotationURL?, AnnotationText\*

Attribute Documentation:

======== ========= =====================================================================================================================
**Name** **Type**  **Documentation**
======== ========= =====================================================================================================================
id       xs:string The id attribute provides a non-standard identification of an annotation. It can be used to disambiguate annotations.
======== ========= =====================================================================================================================

Element Documentation:

=============== ========= =================================================================================================================================================================================================================================================================================
**Name**        **Type**  **Documentation**
=============== ========= =================================================================================================================================================================================================================================================================================
AnnotationTitle xs:string AnnotationTitle provides a title for the annotation.
AnnotationType  xs:string AnnotationType is used to distinguish between annotations designed to support various uses. The types are not enumerated, as these can be specified by the user or creator of the annotations. The definitions and use of annotation types should be documented by their creator.
AnnotationURL   xs:anyURI AnnotationURL is a URI - typically a URL - which points to an external resource which may contain or supplement the annotation. If a specific behavior is desired, an annotation type should be defined which specifies the use of this field more exactly.
AnnotationText  TextType  AnnotationText holds a language-specific string containing the text of the annotation.
=============== ========= =================================================================================================================================================================================================================================================================================

**ReferencePeriodType: **\ Specifies the inclusive start and end times.

Attributes:

startTime, endTime

Content:

{Empty}

Attribute Documentation:

========= =========== ====================================================================================
**Name**  **Type**    **Documentation**
========= =========== ====================================================================================
startTime xs:dateTime The startTime attributes contains the inclusive start date for the reference period.
endTime   xs:dateTime The endTime attributes contains the inclusive end date for the reference period.
========= =========== ====================================================================================

**QueryableDataSourceType: **\ QueryableDataSourceType describes a data
source which is accepts an standard SDMX Query message and responds
appropriately.

Attributes:

isRESTDatasource, isWebServiceDatasource

Content:

DataURL, WSDLURL?, WADLURL?

Attribute Documentation:

====================== ========== =================================================================================================================================
**Name**               **Type**   **Documentation**
====================== ========== =================================================================================================================================
isRESTDatasource       xs:boolean The isRESTDatasource attribute indicates, if true, that the queryable data source is accessible via the REST protocol.
isWebServiceDatasource xs:boolean The isWebServiceDatasource attribute indicates, if true, that the queryable data source is accessible via Web Services protocols.
====================== ========== =================================================================================================================================

Element Documentation:

======== ========= ================================================================================================================================
**Name** **Type**  **Documentation**
======== ========= ================================================================================================================================
DataURL  xs:anyURI DataURL contains the URL of the data source.
WSDLURL  xs:anyURI WSDLURL provides the location of a WSDL instance on the internet which describes the queryable data source.
WADLURL  xs:anyURI WADLURL provides the location of a WADL instance on the internet which describes the REST protocol of the queryable data source.
======== ========= ================================================================================================================================

**XHTMLType: **\ XHTMLType allows for mixed content of text and XHTML
tags. When using this type, one will have to provide a reference to the
XHTML schema, since the processing of the tags within this type is
strict, meaning that they are validated against the XHTML schema
provided.

Attributes:

xml:lang?

Content:

{text} x {any element with namespace of http://www.w3.org/1999/xhtml}\*

Attribute Documentation:

====================== =========== =================
**Name**               **Type**    **Documentation**
====================== =========== =================
xml:lang (default: en) xs:language
====================== =========== =================

**RegionType: **\ RegionType is an abstract type which defines a generic
constraint region. This type can be refined to define regions for data
or metadata sets. A region is defined by a collection of key values -
each of which a collection of values for a component which disambiguates
data or metadata (i.e. dimensions or the target objects of a metadata
target). For each region, as collection of attribute values can be
provided. Taken together, the key values and attributes serve to
identify or describe a subset of a data or metadata set. Finally, the
region can flagged as being included or excluded, although this flag
only makes sense when the region is used in a particular context.

Attributes:

include?

Content:

KeyValue*, Attribute\*

Attribute Documentation:

======================= ========== ==============================================================================================================================================================================================================================================================================
**Name**                **Type**   **Documentation**
======================= ========== ==============================================================================================================================================================================================================================================================================
include (default: true) xs:boolean The include attribute indicates that the region is to be included or excluded within the context in which it is defined. For example, if the regions is defined as part of a content constraint, the exclude flag would mean the data identified by the region is not present.
======================= ========== ==============================================================================================================================================================================================================================================================================

Element Documentation:

========= ======================== =============================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**  **Type**                 **Documentation**
========= ======================== =============================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
KeyValue  *ComponentValueSetTyp e* KeyValue contains a reference to a component which disambiguates the data or metadata (i.e. a dimension or target object) and provides a collection of values for the component. The collection of values can be flagged as being inclusive or exclusive to the region being defined. Any key component that is not included is assumed to be wild carded, which is to say that the cube includes all possible values for the un-referenced key components. Further, this assumption applies to the values of the components as well. The values for any given component can only be sub-setted in the region by explicit inclusion or exclusion. For example, a dimension X which has the possible values of 1, 2, 3 is assumed to have all of these values if a key value is not defined. If a key value is defined with an inclusion attribute of true and the values of 1 and 2, the only the values of 1 and 2 for dimension X are included in the definition of the region. If the key value is defined with an inclusion attribute of false and the value of 1, then the values of 2 and 3 for dimension X are included in the definition of the region. Note that any given key component must only be referenced once in the region.
Attribute *ComponentValueSetTyp e* Attributes contains a reference to an attribute component (data or metadata) and provides a collection of values for the referenced attribute. This serves to state that for the key which defines the region, the attributes that are specified here have or do not have (depending to the include attribute of the value set) the values provided. It is possible to provide and attribute reference without specifying values, for the purpose of stating the attribute is absent (include = false) or present with an unbounded set of values. As opposed to key components, which are assumed to be wild carded if absent, no assumptions are made about the absence of an attribute. Only attributes which are explicitly stated to be present or absent from the region will be know. All unstated attributes for the set cannot be assumed to absent or present.
========= ======================== =============================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================

**ComponentValueSetType: **\ ComponentValueSetType is an abstract base
type which is used to provide a set of value for a referenced component.
Implementations of this type will be based on a particular component
type and refine the allowed values to reflect the types of values that
are possible for that type of component.

Attributes:

id, include?

Content:

(Value+ \| DataSet+ \| DataKey+ \| Object+ \| TimeRange)?

Attribute Documentation:

======================= ================== ==========================================================================================================================================================================================================================================================================================================================================================================
**Name**                **Type**           **Documentation**
======================= ================== ==========================================================================================================================================================================================================================================================================================================================================================================
id                      NestedNCNameIDType The id attribute provides the identifier for the component for which values are being provided. This base type allows for a nested identifier to be provided, for the purpose of referencing a nested component (i.e. a metadata attribute). However, specific implementations will restrict this representation to only allow single level identifiers where appropriate.
include (default: true) xs:boolean         The include attribute indicates whether the values provided for the referenced component are to be included are excluded from the region in which they are defined.
======================= ================== ==========================================================================================================================================================================================================================================================================================================================================================================

Element Documentation:

========= =================== ==============================================================================================================================================================================================================================================================================================================================================
**Name**  **Type**            **Documentation**
========= =================== ==============================================================================================================================================================================================================================================================================================================================================
Value     SimpleValueType     Value provides a simple value for the component, such as a coded, numeric, or simple text value. This type of component value is applicable for dimensions and attributes.
DataSet   SetReferenceType    DataSet provides a reference to a data set and is used to state a value for the data set target component in a metadata target.
DataKey   DataKeyType         DataKey provides a set of dimension references and value, which form a full or partial data key. This is used to state a value for the key descriptor values target component in a metadata target.
Object    ObjectReferenceType Object provides a reference to an Identifiable object in the SDMX Information Model. This is used to state a value for an identifiable target component in a metadata target.
TimeRange TimeRangeValueType  TimeValue provides a value for a component which has a time representation. This is repeatable to allow for a range to be specified, although a single value can also be provided. An operator is available on this to indicate whether the specified value indicates an exact value or the beginning/end of a range (inclusive or exclusive).
========= =================== ==============================================================================================================================================================================================================================================================================================================================================

**DistinctKeyType: **\ DistinctKeyType is an abstract base type which is
a special type of region that only defines a distinct region of data or
metadata. For each component defined in the region, only a single values
is provided. However, the same rules that apply to the general region
about unstated components being wild carded apply here as well. Thus,
this type can define a distinct full or partial key for data or
metadata.

Derivation:

| *RegionType* (restriction) 
|    |image3|\ *DistinctKeyType*

Attributes:

include?

Content:

KeyValue+

Attribute Documentation:

===================== ========== =============================================================================================================================================
**Name**              **Type**   **Documentation**
===================== ========== =============================================================================================================================================
include (fixed: true) xs:boolean The include attribute has a fixed value of true for a distinct key, since such a key is always assumed to identify existing data or metadata.
===================== ========== =============================================================================================================================================

Element Documentation:

======== ======================== =============================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name** **Type**                 **Documentation**
======== ======================== =============================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
KeyValue *DinstinctKeyValueTyp e* KeyValue contains a reference to a component which disambiguates the data or metadata (i.e. a dimension or target object) and provides a collection of values for the component. The collection of values can be flagged as being inclusive or exclusive to the region being defined. Any key component that is not included is assumed to be wild carded, which is to say that the cube includes all possible values for the un-referenced key components. Further, this assumption applies to the values of the components as well. The values for any given component can only be sub-setted in the region by explicit inclusion or exclusion. For example, a dimension X which has the possible values of 1, 2, 3 is assumed to have all of these values if a key value is not defined. If a key value is defined with an inclusion attribute of true and the values of 1 and 2, the only the values of 1 and 2 for dimension X are included in the definition of the region. If the key value is defined with an inclusion attribute of false and the value of 1, then the values of 2 and 3 for dimension X are included in the definition of the region. Note that any given key component must only be referenced once in the region.
======== ======================== =============================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================

**DinstinctKeyValueType: **\ DinstinctKeyValueType is an abstract base
type which defines a singular, required value for a key component.

Derivation:

| *ComponentValueSetType* (restriction) 
|    |image4|\ *DinstinctKeyValueType*

Attributes:

id, include?

Content:

(Value \| DataSet \| DataKey \| Object)

Attribute Documentation:

===================== ================== ==========================================================================================================================================================================================================================================================================================================================================================================
**Name**              **Type**           **Documentation**
===================== ================== ==========================================================================================================================================================================================================================================================================================================================================================================
id                    SingleNCNameIDType The id attribute provides the identifier for the component for which values are being provided. This base type allows for a nested identifier to be provided, for the purpose of referencing a nested component (i.e. a metadata attribute). However, specific implementations will restrict this representation to only allow single level identifiers where appropriate.
include (fixed: true) xs:boolean         The include attribute indicates whether the values provided for the referenced component are to be included are excluded from the region in which they are defined.
===================== ================== ==========================================================================================================================================================================================================================================================================================================================================================================

Element Documentation:

======== =================== ===================================================================================================================================================================================================
**Name** **Type**            **Documentation**
======== =================== ===================================================================================================================================================================================================
Value    SimpleKeyValueType  Value provides a simple value for the component, such as a coded, numeric, or simple text value. This type of component value is applicable for dimensions and attributes.
DataSet  SetReferenceType    DataSet provides a reference to a data set and is used to state a value for the data set target component in a metadata target.
DataKey  DataKeyType         DataKey provides a set of dimension references and value, which form a full or partial data key. This is used to state a value for the key descriptor values target component in a metadata target.
Object   ObjectReferenceType Object provides a reference to an Identifiable object in the SDMX Information Model. This is used to state a value for an identifiable target component in a metadata target.
======== =================== ===================================================================================================================================================================================================

**DataKeyType: **\ DataKeyType is a region which defines a distinct full
or partial data key. The key consists of a set of values, each
referencing a dimension and providing a single value for that dimension.
The purpose of the key is to define a subset of a data set (i.e. the
observed value and data attribute) which have the dimension values
provided in this definition. Any dimension not stated explicitly in this
key is assumed to be wild carded, thus allowing for the definition of
partial data keys.

Derivation:

| *RegionType* (restriction) 
|    |image5|\ *DistinctKeyType* (restriction) 
|          |image6|\ DataKeyType

Attributes:

include?

Content:

KeyValue+

Attribute Documentation:

===================== ========== =============================================================================================================================================
**Name**              **Type**   **Documentation**
===================== ========== =============================================================================================================================================
include (fixed: true) xs:boolean The include attribute has a fixed value of true for a distinct key, since such a key is always assumed to identify existing data or metadata.
===================== ========== =============================================================================================================================================

Element Documentation:

======== ================ =============================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name** **Type**         **Documentation**
======== ================ =============================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
KeyValue DataKeyValueType KeyValue contains a reference to a component which disambiguates the data or metadata (i.e. a dimension or target object) and provides a collection of values for the component. The collection of values can be flagged as being inclusive or exclusive to the region being defined. Any key component that is not included is assumed to be wild carded, which is to say that the cube includes all possible values for the un-referenced key components. Further, this assumption applies to the values of the components as well. The values for any given component can only be sub-setted in the region by explicit inclusion or exclusion. For example, a dimension X which has the possible values of 1, 2, 3 is assumed to have all of these values if a key value is not defined. If a key value is defined with an inclusion attribute of true and the values of 1 and 2, the only the values of 1 and 2 for dimension X are included in the definition of the region. If the key value is defined with an inclusion attribute of false and the value of 1, then the values of 2 and 3 for dimension X are included in the definition of the region. Note that any given key component must only be referenced once in the region.
======== ================ =============================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================

**DataKeyValueType: **\ DataKeyValueType is a type for providing a
dimension value for the purpose of defining a distinct data key. Only a
single value can be provided for the dimension.

Derivation:

| *ComponentValueSetType* (restriction) 
|    |image7|\ *DinstinctKeyValueType* (restriction) 
|          |image8|\ DataKeyValueType

Attributes:

id, include?

Content:

Value

Attribute Documentation:

===================== ================== ==========================================================================================================================================================================================================================================================================================================================================================================
**Name**              **Type**           **Documentation**
===================== ================== ==========================================================================================================================================================================================================================================================================================================================================================================
id                    SingleNCNameIDType The id attribute provides the identifier for the component for which values are being provided. This base type allows for a nested identifier to be provided, for the purpose of referencing a nested component (i.e. a metadata attribute). However, specific implementations will restrict this representation to only allow single level identifiers where appropriate.
include (fixed: true) xs:boolean         The include attribute indicates whether the values provided for the referenced component are to be included are excluded from the region in which they are defined.
===================== ================== ==========================================================================================================================================================================================================================================================================================================================================================================

Element Documentation:

======== ================== ==========================================================================================================================================================================
**Name** **Type**           **Documentation**
======== ================== ==========================================================================================================================================================================
Value    SimpleKeyValueType Value provides a simple value for the component, such as a coded, numeric, or simple text value. This type of component value is applicable for dimensions and attributes.
======== ================== ==========================================================================================================================================================================

**MetadataKeyType: **\ MetadataKeyType is a region which defines a
distinct full or partial metadata key. The key consists of a set of
values, each referencing a target object for the metadata target
referenced in the metadataTarget attribute, which must be defined in the
report structure referenced in the report attribute. Each target object
can be assigned a single value. If an target object from the reference
metadata target is not included in this key, the value of that is
assumed to be all known objects for a reference target object, all
possible keys for a key descriptor values target object, or all dates
for report period target object. The purpose of this key reference a
metadata conforming to a particular report structure for given object or
set of objects.

Derivation:

| *RegionType* (restriction) 
|    |image9|\ *DistinctKeyType* (restriction) 
|          |image10|\ MetadataKeyType

Attributes:

include?, report, metadataTarget

Content:

KeyValue+

Attribute Documentation:

===================== ========== ============================================================================================================================================================================================================================================================================================================================
**Name**              **Type**   **Documentation**
===================== ========== ============================================================================================================================================================================================================================================================================================================================
include (fixed: true) xs:boolean The include attribute has a fixed value of true for a distinct key, since such a key is always assumed to identify existing data or metadata.
report                IDType     The report attribute is required and holds the identifier of the report structure which the reference metadata being defined by this key is based on.
metadataTarget        IDType     The metadataTarget attribute is required and identifies the metadata target for the report structure which this key is based upon. Note that a report structure can have multiple metadata targets, so to properly determine the object or objects for which the key applies, the proper metadata target must be identified.
===================== ========== ============================================================================================================================================================================================================================================================================================================================

Element Documentation:

======== ==================== =============================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name** **Type**             **Documentation**
======== ==================== =============================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
KeyValue MetadataKeyValueType KeyValue contains a reference to a component which disambiguates the data or metadata (i.e. a dimension or target object) and provides a collection of values for the component. The collection of values can be flagged as being inclusive or exclusive to the region being defined. Any key component that is not included is assumed to be wild carded, which is to say that the cube includes all possible values for the un-referenced key components. Further, this assumption applies to the values of the components as well. The values for any given component can only be sub-setted in the region by explicit inclusion or exclusion. For example, a dimension X which has the possible values of 1, 2, 3 is assumed to have all of these values if a key value is not defined. If a key value is defined with an inclusion attribute of true and the values of 1 and 2, the only the values of 1 and 2 for dimension X are included in the definition of the region. If the key value is defined with an inclusion attribute of false and the value of 1, then the values of 2 and 3 for dimension X are included in the definition of the region. Note that any given key component must only be referenced once in the region.
======== ==================== =============================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================

**MetadataKeyValueType: **\ MetadataKeyValueType is a type for providing
a target object value for the purpose of defining a distinct metadata
key. Only a single value can be provided for the target object.

Derivation:

| *ComponentValueSetType* (restriction) 
|    |image11|\ *DinstinctKeyValueType* (restriction) 
|          |image12|\ MetadataKeyValueType

Attributes:

id, include?

Content:

(Value \| DataSet \| DataKey \| Object)

Attribute Documentation:

===================== ================== ==========================================================================================================================================================================================================================================================================================================================================================================
**Name**              **Type**           **Documentation**
===================== ================== ==========================================================================================================================================================================================================================================================================================================================================================================
id                    SingleNCNameIDType The id attribute provides the identifier for the component for which values are being provided. This base type allows for a nested identifier to be provided, for the purpose of referencing a nested component (i.e. a metadata attribute). However, specific implementations will restrict this representation to only allow single level identifiers where appropriate.
include (fixed: true) xs:boolean         The include attribute indicates whether the values provided for the referenced component are to be included are excluded from the region in which they are defined.
===================== ================== ==========================================================================================================================================================================================================================================================================================================================================================================

Element Documentation:

======== =================== ===================================================================================================================================================================================================
**Name** **Type**            **Documentation**
======== =================== ===================================================================================================================================================================================================
Value    SimpleKeyValueType  Value provides a simple value for the component, such as a coded, numeric, or simple text value. This type of component value is applicable for dimensions and attributes.
DataSet  SetReferenceType    DataSet provides a reference to a data set and is used to state a value for the data set target component in a metadata target.
DataKey  DataKeyType         DataKey provides a set of dimension references and value, which form a full or partial data key. This is used to state a value for the key descriptor values target component in a metadata target.
Object   ObjectReferenceType Object provides a reference to an Identifiable object in the SDMX Information Model. This is used to state a value for an identifiable target component in a metadata target.
======== =================== ===================================================================================================================================================================================================

**CubeRegionType: **\ CubeRegionType defines the structure of a data
cube region. This is based on the abstract RegionType and simply refines
the key and attribute values to conform with what is applicable for
dimensions and attributes, respectively. See the documentation of the
base type for more details on how a region is defined.

Derivation:

| *RegionType* (restriction) 
|    |image13|\ CubeRegionType

Attributes:

include?

Content:

KeyValue*, Attribute\*

Attribute Documentation:

======================= ========== ==============================================================================================================================================================================================================================================================================
**Name**                **Type**   **Documentation**
======================= ========== ==============================================================================================================================================================================================================================================================================
include (default: true) xs:boolean The include attribute indicates that the region is to be included or excluded within the context in which it is defined. For example, if the regions is defined as part of a content constraint, the exclude flag would mean the data identified by the region is not present.
======================= ========== ==============================================================================================================================================================================================================================================================================

Element Documentation:

========= ====================== =============================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**  **Type**               **Documentation**
========= ====================== =============================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
KeyValue  CubeRegionKeyType      KeyValue contains a reference to a component which disambiguates the data or metadata (i.e. a dimension or target object) and provides a collection of values for the component. The collection of values can be flagged as being inclusive or exclusive to the region being defined. Any key component that is not included is assumed to be wild carded, which is to say that the cube includes all possible values for the un-referenced key components. Further, this assumption applies to the values of the components as well. The values for any given component can only be sub-setted in the region by explicit inclusion or exclusion. For example, a dimension X which has the possible values of 1, 2, 3 is assumed to have all of these values if a key value is not defined. If a key value is defined with an inclusion attribute of true and the values of 1 and 2, the only the values of 1 and 2 for dimension X are included in the definition of the region. If the key value is defined with an inclusion attribute of false and the value of 1, then the values of 2 and 3 for dimension X are included in the definition of the region. Note that any given key component must only be referenced once in the region.
Attribute AttributeValueSetTyp e Attributes contains a reference to an attribute component (data or metadata) and provides a collection of values for the referenced attribute. This serves to state that for the key which defines the region, the attributes that are specified here have or do not have (depending to the include attribute of the value set) the values provided. It is possible to provide and attribute reference without specifying values, for the purpose of stating the attribute is absent (include = false) or present with an unbounded set of values. As opposed to key components, which are assumed to be wild carded if absent, no assumptions are made about the absence of an attribute. Only attributes which are explicitly stated to be present or absent from the region will be know. All unstated attributes for the set cannot be assumed to absent or present.
========= ====================== =============================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================

**MetadataTargetRegionType: **\ MetadataTargetRegionType defines the
structure of a metadata target region. A metadata target region must
define the report structure and the metadata target from that structure
on which the region is based. This type is based on the abstract
RegionType and simply refines the key and attribute values to conform
with what is applicable for target objects and metadata attributes,
respectively. See the documentation of the base type for more details on
how a region is defined.

Derivation:

| *RegionType* (restriction) 
|    |image14|\ MetadataTargetRegionType

Attributes:

include?, report, metadataTarget

Content:

KeyValue*, Attribute\*

Attribute Documentation:

======================= ========== ==================================================================================================================================================================================================================================================================================================================================
**Name**                **Type**   **Documentation**
======================= ========== ==================================================================================================================================================================================================================================================================================================================================
include (default: true) xs:boolean The include attribute indicates that the region is to be included or excluded within the context in which it is defined. For example, if the regions is defined as part of a content constraint, the exclude flag would mean the data identified by the region is not present.
report                  IDType     The report attribute is required and holds the identifier of the report structure which the reference metadata being defined by this region is based on.
metadataTarget          IDType     The metadataTarget attribute is required and identifies the metadata target for the report structure which this region is based upon. Note that a report structure can have multiple metadata targets, so to properly determine the object or objects for which the region applies, the proper metadata target must be identified.
======================= ========== ==================================================================================================================================================================================================================================================================================================================================

Element Documentation:

========= ============================== =============================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**  **Type**                       **Documentation**
========= ============================== =============================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
KeyValue  MetadataTargetRegion KeyType   KeyValue contains a reference to a component which disambiguates the data or metadata (i.e. a dimension or target object) and provides a collection of values for the component. The collection of values can be flagged as being inclusive or exclusive to the region being defined. Any key component that is not included is assumed to be wild carded, which is to say that the cube includes all possible values for the un-referenced key components. Further, this assumption applies to the values of the components as well. The values for any given component can only be sub-setted in the region by explicit inclusion or exclusion. For example, a dimension X which has the possible values of 1, 2, 3 is assumed to have all of these values if a key value is not defined. If a key value is defined with an inclusion attribute of true and the values of 1 and 2, the only the values of 1 and 2 for dimension X are included in the definition of the region. If the key value is defined with an inclusion attribute of false and the value of 1, then the values of 2 and 3 for dimension X are included in the definition of the region. Note that any given key component must only be referenced once in the region.
Attribute MetadataAttributeVal ueSetType Attributes contains a reference to an attribute component (data or metadata) and provides a collection of values for the referenced attribute. This serves to state that for the key which defines the region, the attributes that are specified here have or do not have (depending to the include attribute of the value set) the values provided. It is possible to provide and attribute reference without specifying values, for the purpose of stating the attribute is absent (include = false) or present with an unbounded set of values. As opposed to key components, which are assumed to be wild carded if absent, no assumptions are made about the absence of an attribute. Only attributes which are explicitly stated to be present or absent from the region will be know. All unstated attributes for the set cannot be assumed to absent or present.
========= ============================== =============================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================

**CubeRegionKeyType: **\ CubeRegionKeyType is a type for providing a set
of values for a dimension for the purpose of defining a data cube
region. A set of distinct value can be provided, or if this dimension is
represented as time, and time range can be specified.

Derivation:

| *ComponentValueSetType* (restriction) 
|    |image15|\ CubeRegionKeyType

Attributes:

id, include?

Content:

(Value+ \| TimeRange)

Attribute Documentation:

======================= ================== ==========================================================================================================================================================================================================================================================================================================================================================================
**Name**                **Type**           **Documentation**
======================= ================== ==========================================================================================================================================================================================================================================================================================================================================================================
id                      SingleNCNameIDType The id attribute provides the identifier for the component for which values are being provided. This base type allows for a nested identifier to be provided, for the purpose of referencing a nested component (i.e. a metadata attribute). However, specific implementations will restrict this representation to only allow single level identifiers where appropriate.
include (default: true) xs:boolean         The include attribute indicates whether the values provided for the referenced component are to be included are excluded from the region in which they are defined.
======================= ================== ==========================================================================================================================================================================================================================================================================================================================================================================

Element Documentation:

========= ================== ==============================================================================================================================================================================================================================================================================================================================================
**Name**  **Type**           **Documentation**
========= ================== ==============================================================================================================================================================================================================================================================================================================================================
Value     SimpleValueType    Value provides a simple value for the component, such as a coded, numeric, or simple text value. This type of component value is applicable for dimensions and attributes.
TimeRange TimeRangeValueType TimeValue provides a value for a component which has a time representation. This is repeatable to allow for a range to be specified, although a single value can also be provided. An operator is available on this to indicate whether the specified value indicates an exact value or the beginning/end of a range (inclusive or exclusive).
========= ================== ==============================================================================================================================================================================================================================================================================================================================================

**MetadataTargetRegionKeyType: **\ MetadataTargetRegionKeyType is a type
for providing a set of values for a target object in a metadata target
of a re fence metadata report. A set of values or a time range can be
provided for a report period target object. A collection of the
respective types of references can be provided for data set reference
and identifiable object reference target objects. For a key descriptor
values target object, a collection of data keys can be provided.

Derivation:

| *ComponentValueSetType* (restriction) 
|    |image16|\ MetadataTargetRegionKeyType

Attributes:

id, include?

Content:

(Value+ \| DataSet+ \| DataKey+ \| Object+ \| TimeRange)

Attribute Documentation:

======================= ================== ==========================================================================================================================================================================================================================================================================================================================================================================
**Name**                **Type**           **Documentation**
======================= ================== ==========================================================================================================================================================================================================================================================================================================================================================================
id                      SingleNCNameIDType The id attribute provides the identifier for the component for which values are being provided. This base type allows for a nested identifier to be provided, for the purpose of referencing a nested component (i.e. a metadata attribute). However, specific implementations will restrict this representation to only allow single level identifiers where appropriate.
include (default: true) xs:boolean         The include attribute indicates whether the values provided for the referenced component are to be included are excluded from the region in which they are defined.
======================= ================== ==========================================================================================================================================================================================================================================================================================================================================================================

Element Documentation:

========= =================== ==============================================================================================================================================================================================================================================================================================================================================
**Name**  **Type**            **Documentation**
========= =================== ==============================================================================================================================================================================================================================================================================================================================================
Value     SimpleKeyValueType  Value provides a simple value for the component, such as a coded, numeric, or simple text value. This type of component value is applicable for dimensions and attributes.
DataSet   SetReferenceType    DataSet provides a reference to a data set and is used to state a value for the data set target component in a metadata target.
DataKey   DataKeyType         DataKey provides a set of dimension references and value, which form a full or partial data key. This is used to state a value for the key descriptor values target component in a metadata target.
Object    ObjectReferenceType Object provides a reference to an Identifiable object in the SDMX Information Model. This is used to state a value for an identifiable target component in a metadata target.
TimeRange TimeRangeValueType  TimeValue provides a value for a component which has a time representation. This is repeatable to allow for a range to be specified, although a single value can also be provided. An operator is available on this to indicate whether the specified value indicates an exact value or the beginning/end of a range (inclusive or exclusive).
========= =================== ==============================================================================================================================================================================================================================================================================================================================================

**AttributeValueSetType: **\ AttributeValueSetType defines the structure
for providing values for a data attribute. If no values are provided,
the attribute is implied to include/excluded from the region in which it
is defined, with no regard to the value of the data attribute. Note that
for metadata attributes which occur within other metadata attributes, a
nested identifier can be provided. For example, a value of
CONTACT.ADDRESS.STREET refers to the metadata attribute with the
identifier STREET which exists in the ADDRESS metadata attribute in the
CONTACT metadata attribute, which is defined at the root of the report
structure.

Derivation:

| *ComponentValueSetType* (restriction) 
|    |image17|\ AttributeValueSetType

Attributes:

id, include?

Content:

(Value+ \| TimeRange)?

Attribute Documentation:

======================= ================== ==========================================================================================================================================================================================================================================================================================================================================================================
**Name**                **Type**           **Documentation**
======================= ================== ==========================================================================================================================================================================================================================================================================================================================================================================
id                      SingleNCNameIDType The id attribute provides the identifier for the component for which values are being provided. This base type allows for a nested identifier to be provided, for the purpose of referencing a nested component (i.e. a metadata attribute). However, specific implementations will restrict this representation to only allow single level identifiers where appropriate.
include (default: true) xs:boolean         The include attribute indicates whether the values provided for the referenced component are to be included are excluded from the region in which they are defined.
======================= ================== ==========================================================================================================================================================================================================================================================================================================================================================================

Element Documentation:

========= ================== ==============================================================================================================================================================================================================================================================================================================================================
**Name**  **Type**           **Documentation**
========= ================== ==============================================================================================================================================================================================================================================================================================================================================
Value     SimpleValueType    Value provides a simple value for the component, such as a coded, numeric, or simple text value. This type of component value is applicable for dimensions and attributes.
TimeRange TimeRangeValueType TimeValue provides a value for a component which has a time representation. This is repeatable to allow for a range to be specified, although a single value can also be provided. An operator is available on this to indicate whether the specified value indicates an exact value or the beginning/end of a range (inclusive or exclusive).
========= ================== ==============================================================================================================================================================================================================================================================================================================================================

**MetadataAttributeValueSetType: **\ MetadataAttributeValueSetType
defines the structure for providing values for a metadata attribute. If
no values are provided, the attribute is implied to include/excluded
from the region in which it is defined, with no regard to the value of
the metadata attribute.

Derivation:

| *ComponentValueSetType* (restriction) 
|    |image18|\ MetadataAttributeValueSetType

Attributes:

id, include?

Content:

(Value+ \| TimeRange)?

Attribute Documentation:

======================= ================== ==========================================================================================================================================================================================================================================================================================================================================================================
**Name**                **Type**           **Documentation**
======================= ================== ==========================================================================================================================================================================================================================================================================================================================================================================
id                      NestedNCNameIDType The id attribute provides the identifier for the component for which values are being provided. This base type allows for a nested identifier to be provided, for the purpose of referencing a nested component (i.e. a metadata attribute). However, specific implementations will restrict this representation to only allow single level identifiers where appropriate.
include (default: true) xs:boolean         The include attribute indicates whether the values provided for the referenced component are to be included are excluded from the region in which they are defined.
======================= ================== ==========================================================================================================================================================================================================================================================================================================================================================================

Element Documentation:

========= ================== ==============================================================================================================================================================================================================================================================================================================================================
**Name**  **Type**           **Documentation**
========= ================== ==============================================================================================================================================================================================================================================================================================================================================
Value     SimpleValueType    Value provides a simple value for the component, such as a coded, numeric, or simple text value. This type of component value is applicable for dimensions and attributes.
TimeRange TimeRangeValueType TimeValue provides a value for a component which has a time representation. This is repeatable to allow for a range to be specified, although a single value can also be provided. An operator is available on this to indicate whether the specified value indicates an exact value or the beginning/end of a range (inclusive or exclusive).
========= ================== ==============================================================================================================================================================================================================================================================================================================================================

**SimpleValueType: **\ SimpleValueType contains a simple value for a
component, and if that value is from a code list, the ability to
indicate that child codes in a simple hierarchy are part of the value
set of the component for the region.

Derivation:

| xs:anySimpleType (restriction) 
|    |image19|\ xs:string (extension) 
|          |image20|\ SimpleValueType

Attributes:

cascadeValues?

Content:

Attribute Documentation:

============================== ========== ======================================================================================================================================================================
**Name**                       **Type**   **Documentation**
============================== ========== ======================================================================================================================================================================
cascadeValues (default: false) xs:boolean The cascadeValues attribute, if true, indicates that if the value is taken from a code all child codes in a simple hierarchy are understood be included in the region.
============================== ========== ======================================================================================================================================================================

**SimpleKeyValueType: **\ SimpleKeyValueType derives from the
SimpleValueType, but does not allow for the cascading of value in the
hierarchy, as keys are meant to describe a distinct full or partial key.

Derivation:

| xs:anySimpleType (restriction) 
|    |image21|\ xs:string (extension) 
|          |image22|\ SimpleValueType (restriction) 
|                |image23|\ SimpleKeyValueType

Content:

**TimeRangeValueType: **\ TimeRangeValueType allows a time period value
to be expressed as a range. It can be expressed as the period before a
period, after a period, or between two periods. Each of these properties
can specify their inclusion in regards to the range.

Content:

(BeforePeriod \| AfterPeriod \| (StartPeriod, EndPeriod))

Element Documentation:

============ =================== =========================================================================================================================================
**Name**     **Type**            **Documentation**
============ =================== =========================================================================================================================================
BeforePeriod TimePeriodRangeType BeforePeriod is the period before which the period is meant to cover. This date may be inclusive or exclusive in the range.
AfterPeriod  TimePeriodRangeType AfterPeriod is the period after which the period is meant to cover. This date may be inclusive or exclusive in the range.
StartPeriod  TimePeriodRangeType StartPeriod is the start date or the range that the queried date must occur within. This date may be inclusive or exclusive in the range.
EndPeriod    TimePeriodRangeType EndPeriod is the end period of the range. This date may be inclusive or exclusive in the range.
============ =================== =========================================================================================================================================

**TimePeriodRangeType: **\ TimePeriodRangeType defines a time period,
and indicates whether it is inclusive in a range.

Derivation:

| xs:anySimpleType (restriction) 
|    |image24|\ ObservationalTimePeriodType (extension) 
|          |image25|\ TimePeriodRangeType

Attributes:

isInclusive?

Content:

Attribute Documentation:

=========================== ========== ========================================================================================================
**Name**                    **Type**   **Documentation**
=========================== ========== ========================================================================================================
isInclusive (default: true) xs:boolean The isInclusive attribute, when true, indicates that the time period specified is included in the range.
=========================== ========== ========================================================================================================

**PayloadStructureType: **\ PayloadStructureType is an abstract base
type used to define the structural information for data or metadata
sets. A reference to the structure is provided (either explicitly or
through a reference to a structure usage).

Attributes:

structureID, schemaURL?, namespace?, dimensionAtObservation?,
explicitMeasures?, serviceURL?, structureURL?

Content:

(ProvisionAgrement \| StructureUsage \| Structure)

Attribute Documentation:

====================== ========================= ====================================================================================================================================================================================================================================================================================
**Name**               **Type**                  **Documentation**
====================== ========================= ====================================================================================================================================================================================================================================================================================
structureID            xs:ID                     The structureID attribute uniquely identifies the structure for the purpose of referencing it from the payload. This is only used in structure specific formats. Although it is required, it is only useful when more than one data set is present in the message.
schemaURL              xs:anyURI                 The schemaURL attribute provides a location from which the structure specific schema can be located.
namespace              xs:anyURI                 The namespace attribute is used to provide the namespace for structure-specific formats. By communicating this information in the header, it is possible to generate the structure specific schema while processing the message.
dimensionAtObservation ObservationDimension Type The dimensionAtObservation is used to reference the dimension at the observation level for data messages. This can also be given the explicit value of "AllDimensions" which denotes that the cross sectional data is in the flat format.
explicitMeasures       xs:boolean                The explicitMeasures indicates whether explicit measures are used in the cross sectional format. This is only applicable for the measure dimension as the dimension at the observation level or the flat structure.
serviceURL             xs:anyURI                 The serviceURL attribute indicates the URL of an SDMX SOAP web service from which the details of the object can be retrieved. Note that this can be a registry or and SDMX structural metadata repository, as they both implement that same web service interface.
structureURL           xs:anyURI                 The structureURL attribute indicates the URL of a SDMX-ML structure message (in the same version as the source document) in which the externally referenced object is contained. Note that this may be a URL of an SDMX RESTful web service which will return the referenced object.
====================== ========================= ====================================================================================================================================================================================================================================================================================

Element Documentation:

================= ================================== ===================================================================================================
**Name**          **Type**                           **Documentation**
================= ================================== ===================================================================================================
ProvisionAgrement ProvisionAgreementRe ferenceType   ProvisionAgreement references a provision agreement which the data or metadata is reported against.
StructureUsage    *StructureUsageRefere nceBaseType* StructureUsage references a flow which the data or metadata is reported against.
Structure         *StructureReferenceBa seType*      Structure references the structure which defines the structure of the data or metadata set.
================= ================================== ===================================================================================================

**DataStructureType: **\ DataStructureType is an abstract base type the
forms the basis for the structural information for a data set.

Derivation:

| *PayloadStructureType* (restriction) 
|    |image26|\ *DataStructureType*

Attributes:

structureID, schemaURL?, namespace?, dimensionAtObservation?,
explicitMeasures?, serviceURL?, structureURL?

Content:

(ProvisionAgrement \| StructureUsage \| Structure)

Attribute Documentation:

====================== ========================= ====================================================================================================================================================================================================================================================================================
**Name**               **Type**                  **Documentation**
====================== ========================= ====================================================================================================================================================================================================================================================================================
structureID            xs:ID                     The structureID attribute uniquely identifies the structure for the purpose of referencing it from the payload. This is only used in structure specific formats. Although it is required, it is only useful when more than one data set is present in the message.
schemaURL              xs:anyURI                 The schemaURL attribute provides a location from which the structure specific schema can be located.
namespace              xs:anyURI                 The namespace attribute is used to provide the namespace for structure-specific formats. By communicating this information in the header, it is possible to generate the structure specific schema while processing the message.
dimensionAtObservation ObservationDimension Type The dimensionAtObservation is used to reference the dimension at the observation level for data messages. This can also be given the explicit value of "AllDimensions" which denotes that the cross sectional data is in the flat format.
explicitMeasures       xs:boolean                The explicitMeasures indicates whether explicit measures are used in the cross sectional format. This is only applicable for the measure dimension as the dimension at the observation level or the flat structure.
serviceURL             xs:anyURI                 The serviceURL attribute indicates the URL of an SDMX SOAP web service from which the details of the object can be retrieved. Note that this can be a registry or and SDMX structural metadata repository, as they both implement that same web service interface.
structureURL           xs:anyURI                 The structureURL attribute indicates the URL of a SDMX-ML structure message (in the same version as the source document) in which the externally referenced object is contained. Note that this may be a URL of an SDMX RESTful web service which will return the referenced object.
====================== ========================= ====================================================================================================================================================================================================================================================================================

Element Documentation:

================= ================================ ===========================================================================================
**Name**          **Type**                         **Documentation**
================= ================================ ===========================================================================================
ProvisionAgrement ProvisionAgreementRe ferenceType ProvisionAgreement references a provision agreement which the data is reported against.
StructureUsage    DataflowReferenceTyp e           StructureUsage references a dataflow which the data is reported against.
Structure         DataStructureReferen ceType      Structure references the data structure definition which defines the structure of the data.
================= ================================ ===========================================================================================

**DataStructureRequestType: **\ DataStructureRequestType is a variation
of a the DataStructureType for querying purposes. Only the observation
dimension and the explicit measures flag are allowed.

Derivation:

| *PayloadStructureType* (restriction) 
|    |image27|\ *DataStructureType* (restriction) 
|          |image28|\ DataStructureRequestType

Attributes:

structureID, dimensionAtObservation, explicitMeasures?, serviceURL?,
structureURL?

Content:

(ProvisionAgrement \| StructureUsage \| Structure)

Attribute Documentation:

================================= ========================= ====================================================================================================================================================================================================================================================================================
**Name**                          **Type**                  **Documentation**
================================= ========================= ====================================================================================================================================================================================================================================================================================
structureID                       xs:ID                     The structureID attribute uniquely identifies the structure for the purpose of referencing it from the payload. This is only used in structure specific formats. Although it is required, it is only useful when more than one data set is present in the message.
dimensionAtObservation            ObservationDimension Type The dimensionAtObservation is used to reference the dimension at the observation level for data messages. This can also be given the explicit value of "AllDimensions" which denotes that the cross sectional data is in the flat format.
explicitMeasures (default: false) xs:boolean                The explicitMeasures indicates whether explicit measures are used in the cross sectional format. This is only applicable for the measure dimension as the dimension at the observation level or the flat structure.
serviceURL                        xs:anyURI                 The serviceURL attribute indicates the URL of an SDMX SOAP web service from which the details of the object can be retrieved. Note that this can be a registry or and SDMX structural metadata repository, as they both implement that same web service interface.
structureURL                      xs:anyURI                 The structureURL attribute indicates the URL of a SDMX-ML structure message (in the same version as the source document) in which the externally referenced object is contained. Note that this may be a URL of an SDMX RESTful web service which will return the referenced object.
================================= ========================= ====================================================================================================================================================================================================================================================================================

Element Documentation:

================= ================================ ===========================================================================================
**Name**          **Type**                         **Documentation**
================= ================================ ===========================================================================================
ProvisionAgrement ProvisionAgreementRe ferenceType ProvisionAgreement references a provision agreement which the data is reported against.
StructureUsage    DataflowReferenceTyp e           StructureUsage references a dataflow which the data is reported against.
Structure         DataStructureReferen ceType      Structure references the data structure definition which defines the structure of the data.
================= ================================ ===========================================================================================

**GenericDataStructureRequestType: **\ GenericDataStructureRequestType
is a variation of a the DataStructureRequestType for querying purposes.
The explicit measure flag in not allowed.

Derivation:

| *PayloadStructureType* (restriction) 
|    |image29|\ *DataStructureType* (restriction) 
|          |image30|\ DataStructureRequestType (restriction) 
|                |image31|\ GenericDataStructureRequestType

Attributes:

structureID, dimensionAtObservation, serviceURL?, structureURL?

Content:

(ProvisionAgrement \| StructureUsage \| Structure)

Attribute Documentation:

====================== ========================= ====================================================================================================================================================================================================================================================================================
**Name**               **Type**                  **Documentation**
====================== ========================= ====================================================================================================================================================================================================================================================================================
structureID            xs:ID                     The structureID attribute uniquely identifies the structure for the purpose of referencing it from the payload. This is only used in structure specific formats. Although it is required, it is only useful when more than one data set is present in the message.
dimensionAtObservation ObservationDimension Type The dimensionAtObservation is used to reference the dimension at the observation level for data messages. This can also be given the explicit value of "AllDimensions" which denotes that the cross sectional data is in the flat format.
serviceURL             xs:anyURI                 The serviceURL attribute indicates the URL of an SDMX SOAP web service from which the details of the object can be retrieved. Note that this can be a registry or and SDMX structural metadata repository, as they both implement that same web service interface.
structureURL           xs:anyURI                 The structureURL attribute indicates the URL of a SDMX-ML structure message (in the same version as the source document) in which the externally referenced object is contained. Note that this may be a URL of an SDMX RESTful web service which will return the referenced object.
====================== ========================= ====================================================================================================================================================================================================================================================================================

Element Documentation:

================= ================================ ===========================================================================================
**Name**          **Type**                         **Documentation**
================= ================================ ===========================================================================================
ProvisionAgrement ProvisionAgreementRe ferenceType ProvisionAgreement references a provision agreement which the data is reported against.
StructureUsage    DataflowReferenceTyp e           StructureUsage references a dataflow which the data is reported against.
Structure         DataStructureReferen ceType      Structure references the data structure definition which defines the structure of the data.
================= ================================ ===========================================================================================

**TimeSeriesDataStructureRequestType: **\ TimeSeriesDataStructureRequestType
is a variation of a the DataStructureRequestType for querying purposes.
The observation dimension is fixed to TIME_PERIOD

Derivation:

| *PayloadStructureType* (restriction) 
|    |image32|\ *DataStructureType* (restriction) 
|          |image33|\ DataStructureRequestType (restriction) 
|                |image34|\ TimeSeriesDataStructureRequestType

Attributes:

structureID, dimensionAtObservation, explicitMeasures?, serviceURL?,
structureURL?

Content:

(ProvisionAgrement \| StructureUsage \| Structure)

Attribute Documentation:

=========================================== ========================= ====================================================================================================================================================================================================================================================================================
**Name**                                    **Type**                  **Documentation**
=========================================== ========================= ====================================================================================================================================================================================================================================================================================
structureID                                 xs:ID                     The structureID attribute uniquely identifies the structure for the purpose of referencing it from the payload. This is only used in structure specific formats. Although it is required, it is only useful when more than one data set is present in the message.
dimensionAtObservation (fixed: TIME_PERIOD) ObservationDimension Type The dimensionAtObservation is used to reference the dimension at the observation level for data messages. This can also be given the explicit value of "AllDimensions" which denotes that the cross sectional data is in the flat format.
explicitMeasures (default: false)           xs:boolean                The explicitMeasures indicates whether explicit measures are used in the cross sectional format. This is only applicable for the measure dimension as the dimension at the observation level or the flat structure.
serviceURL                                  xs:anyURI                 The serviceURL attribute indicates the URL of an SDMX SOAP web service from which the details of the object can be retrieved. Note that this can be a registry or and SDMX structural metadata repository, as they both implement that same web service interface.
structureURL                                xs:anyURI                 The structureURL attribute indicates the URL of a SDMX-ML structure message (in the same version as the source document) in which the externally referenced object is contained. Note that this may be a URL of an SDMX RESTful web service which will return the referenced object.
=========================================== ========================= ====================================================================================================================================================================================================================================================================================

Element Documentation:

================= ================================ ===========================================================================================
**Name**          **Type**                         **Documentation**
================= ================================ ===========================================================================================
ProvisionAgrement ProvisionAgreementRe ferenceType ProvisionAgreement references a provision agreement which the data is reported against.
StructureUsage    DataflowReferenceTyp e           StructureUsage references a dataflow which the data is reported against.
Structure         DataStructureReferen ceType      Structure references the data structure definition which defines the structure of the data.
================= ================================ ===========================================================================================

**TimeSeriesGenericDataStructureRequestType: **\ TimeSeriesGenericDataStructureRequestType
is a variation of a the GenericDataStructureRequestType for querying
purposes. The observation dimension is fixed to TIME_PERIOD.

Derivation:

| *PayloadStructureType* (restriction) 
|    |image35|\ *DataStructureType* (restriction) 
|          |image36|\ DataStructureRequestType (restriction) 
|                |image37|\ GenericDataStructureRequestType
  (restriction) 
|                      |image38|\ TimeSeriesGenericDataStructureRequestType

Attributes:

structureID, dimensionAtObservation, serviceURL?, structureURL?

Content:

(ProvisionAgrement \| StructureUsage \| Structure)

Attribute Documentation:

=========================================== ========================= ====================================================================================================================================================================================================================================================================================
**Name**                                    **Type**                  **Documentation**
=========================================== ========================= ====================================================================================================================================================================================================================================================================================
structureID                                 xs:ID                     The structureID attribute uniquely identifies the structure for the purpose of referencing it from the payload. This is only used in structure specific formats. Although it is required, it is only useful when more than one data set is present in the message.
dimensionAtObservation (fixed: TIME_PERIOD) ObservationDimension Type The dimensionAtObservation is used to reference the dimension at the observation level for data messages. This can also be given the explicit value of "AllDimensions" which denotes that the cross sectional data is in the flat format.
serviceURL                                  xs:anyURI                 The serviceURL attribute indicates the URL of an SDMX SOAP web service from which the details of the object can be retrieved. Note that this can be a registry or and SDMX structural metadata repository, as they both implement that same web service interface.
structureURL                                xs:anyURI                 The structureURL attribute indicates the URL of a SDMX-ML structure message (in the same version as the source document) in which the externally referenced object is contained. Note that this may be a URL of an SDMX RESTful web service which will return the referenced object.
=========================================== ========================= ====================================================================================================================================================================================================================================================================================

Element Documentation:

================= ================================ ===========================================================================================
**Name**          **Type**                         **Documentation**
================= ================================ ===========================================================================================
ProvisionAgrement ProvisionAgreementRe ferenceType ProvisionAgreement references a provision agreement which the data is reported against.
StructureUsage    DataflowReferenceTyp e           StructureUsage references a dataflow which the data is reported against.
Structure         DataStructureReferen ceType      Structure references the data structure definition which defines the structure of the data.
================= ================================ ===========================================================================================

**GenericDataStructureType: **\ GenericDataStructureType defines the
structural information for a generic data set. A reference to the
structure, either explicitly or through a dataflow or provision
agreement is required as well as the dimension which occurs at the
observation level.

Derivation:

| *PayloadStructureType* (restriction) 
|    |image39|\ *DataStructureType* (restriction) 
|          |image40|\ GenericDataStructureType

Attributes:

structureID, dimensionAtObservation, serviceURL?, structureURL?

Content:

(ProvisionAgrement \| StructureUsage \| Structure)

Attribute Documentation:

====================== ========================= ====================================================================================================================================================================================================================================================================================
**Name**               **Type**                  **Documentation**
====================== ========================= ====================================================================================================================================================================================================================================================================================
structureID            xs:ID                     The structureID attribute uniquely identifies the structure for the purpose of referencing it from the payload. This is only used in structure specific formats. Although it is required, it is only useful when more than one data set is present in the message.
dimensionAtObservation ObservationDimension Type The dimensionAtObservation is used to reference the dimension at the observation level for data messages. This can also be given the explicit value of "AllDimensions" which denotes that the cross sectional data is in the flat format.
serviceURL             xs:anyURI                 The serviceURL attribute indicates the URL of an SDMX SOAP web service from which the details of the object can be retrieved. Note that this can be a registry or and SDMX structural metadata repository, as they both implement that same web service interface.
structureURL           xs:anyURI                 The structureURL attribute indicates the URL of a SDMX-ML structure message (in the same version as the source document) in which the externally referenced object is contained. Note that this may be a URL of an SDMX RESTful web service which will return the referenced object.
====================== ========================= ====================================================================================================================================================================================================================================================================================

Element Documentation:

================= ================================ ===========================================================================================
**Name**          **Type**                         **Documentation**
================= ================================ ===========================================================================================
ProvisionAgrement ProvisionAgreementRe ferenceType ProvisionAgreement references a provision agreement which the data is reported against.
StructureUsage    DataflowReferenceTyp e           StructureUsage references a dataflow which the data is reported against.
Structure         DataStructureReferen ceType      Structure references the data structure definition which defines the structure of the data.
================= ================================ ===========================================================================================

**GenericTimeSeriesDataStructureType: **\ GenericTimeSeriesDataStructureType
defines the structural information for a generic time series based data
set. The dimension at the observation level is fixed to be TIME_PERIOD.

Derivation:

| *PayloadStructureType* (restriction) 
|    |image41|\ *DataStructureType* (restriction) 
|          |image42|\ GenericDataStructureType (restriction) 
|                |image43|\ GenericTimeSeriesDataStructureType

Attributes:

structureID, dimensionAtObservation, serviceURL?, structureURL?

Content:

(ProvisionAgrement \| StructureUsage \| Structure)

Attribute Documentation:

=========================================== ========================= ====================================================================================================================================================================================================================================================================================
**Name**                                    **Type**                  **Documentation**
=========================================== ========================= ====================================================================================================================================================================================================================================================================================
structureID                                 xs:ID                     The structureID attribute uniquely identifies the structure for the purpose of referencing it from the payload. This is only used in structure specific formats. Although it is required, it is only useful when more than one data set is present in the message.
dimensionAtObservation (fixed: TIME_PERIOD) ObservationDimension Type The dimensionAtObservation is used to reference the dimension at the observation level for data messages. This can also be given the explicit value of "AllDimensions" which denotes that the cross sectional data is in the flat format.
serviceURL                                  xs:anyURI                 The serviceURL attribute indicates the URL of an SDMX SOAP web service from which the details of the object can be retrieved. Note that this can be a registry or and SDMX structural metadata repository, as they both implement that same web service interface.
structureURL                                xs:anyURI                 The structureURL attribute indicates the URL of a SDMX-ML structure message (in the same version as the source document) in which the externally referenced object is contained. Note that this may be a URL of an SDMX RESTful web service which will return the referenced object.
=========================================== ========================= ====================================================================================================================================================================================================================================================================================

Element Documentation:

================= ================================ ===========================================================================================
**Name**          **Type**                         **Documentation**
================= ================================ ===========================================================================================
ProvisionAgrement ProvisionAgreementRe ferenceType ProvisionAgreement references a provision agreement which the data is reported against.
StructureUsage    DataflowReferenceTyp e           StructureUsage references a dataflow which the data is reported against.
Structure         DataStructureReferen ceType      Structure references the data structure definition which defines the structure of the data.
================= ================================ ===========================================================================================

**StructureSpecificDataStructureType: **\ StructureSpecificDataStructureType
defines the structural information for a structured data set. In
addition to referencing the data structure or dataflow which defines the
structure of the data, the namespace for the data structure specific
schema as well as which dimension is used at the observation level must
be provided. It is also necessary to state whether the format uses
explicit measures, although this is technically only applicable is the
dimension at the observation level is the measure dimension or the flat
data format is used.

Derivation:

| *PayloadStructureType* (restriction) 
|    |image44|\ *DataStructureType* (restriction) 
|          |image45|\ StructureSpecificDataStructureType

Attributes:

structureID, schemaURL?, namespace, dimensionAtObservation,
explicitMeasures?, serviceURL?, structureURL?

Content:

(ProvisionAgrement \| StructureUsage \| Structure)

Attribute Documentation:

================================= ========================= ====================================================================================================================================================================================================================================================================================
**Name**                          **Type**                  **Documentation**
================================= ========================= ====================================================================================================================================================================================================================================================================================
structureID                       xs:ID                     The structureID attribute uniquely identifies the structure for the purpose of referencing it from the payload. This is only used in structure specific formats. Although it is required, it is only useful when more than one data set is present in the message.
schemaURL                         xs:anyURI                 The schemaURL attribute provides a location from which the structure specific schema can be located.
namespace                         xs:anyURI                 The namespace attribute is used to provide the namespace for structure-specific formats. By communicating this information in the header, it is possible to generate the structure specific schema while processing the message.
dimensionAtObservation            ObservationDimension Type The dimensionAtObservation is used to reference the dimension at the observation level for data messages. This can also be given the explicit value of "AllDimensions" which denotes that the cross sectional data is in the flat format.
explicitMeasures (default: false) xs:boolean                The explicitMeasures indicates whether explicit measures are used in the cross sectional format. This is only applicable for the measure dimension as the dimension at the observation level or the flat structure.
serviceURL                        xs:anyURI                 The serviceURL attribute indicates the URL of an SDMX SOAP web service from which the details of the object can be retrieved. Note that this can be a registry or and SDMX structural metadata repository, as they both implement that same web service interface.
structureURL                      xs:anyURI                 The structureURL attribute indicates the URL of a SDMX-ML structure message (in the same version as the source document) in which the externally referenced object is contained. Note that this may be a URL of an SDMX RESTful web service which will return the referenced object.
================================= ========================= ====================================================================================================================================================================================================================================================================================

Element Documentation:

================= ================================ ===========================================================================================
**Name**          **Type**                         **Documentation**
================= ================================ ===========================================================================================
ProvisionAgrement ProvisionAgreementRe ferenceType ProvisionAgreement references a provision agreement which the data is reported against.
StructureUsage    DataflowReferenceTyp e           StructureUsage references a dataflow which the data is reported against.
Structure         DataStructureReferen ceType      Structure references the data structure definition which defines the structure of the data.
================= ================================ ===========================================================================================

**StructureSpecificDataTimeSeriesStructureType: **\ StructureSpecificDataTimeSeriesStructureType
defines the structural information for a structure definition specific
time series data set. The dimension at the observation level is fixed to
be TIME_PERIOD.

Derivation:

| *PayloadStructureType* (restriction) 
|    |image46|\ *DataStructureType* (restriction) 
|          |image47|\ StructureSpecificDataStructureType (restriction) 
|                |image48|\ StructureSpecificDataTimeSeriesStructureType

Attributes:

structureID, schemaURL?, namespace, dimensionAtObservation, serviceURL?,
structureURL?

Content:

(ProvisionAgrement \| StructureUsage \| Structure)

Attribute Documentation:

=========================================== ========================= ====================================================================================================================================================================================================================================================================================
**Name**                                    **Type**                  **Documentation**
=========================================== ========================= ====================================================================================================================================================================================================================================================================================
structureID                                 xs:ID                     The structureID attribute uniquely identifies the structure for the purpose of referencing it from the payload. This is only used in structure specific formats. Although it is required, it is only useful when more than one data set is present in the message.
schemaURL                                   xs:anyURI                 The schemaURL attribute provides a location from which the structure specific schema can be located.
namespace                                   xs:anyURI                 The namespace attribute is used to provide the namespace for structure-specific formats. By communicating this information in the header, it is possible to generate the structure specific schema while processing the message.
dimensionAtObservation (fixed: TIME_PERIOD) ObservationDimension Type The dimensionAtObservation is used to reference the dimension at the observation level for data messages. This can also be given the explicit value of "AllDimensions" which denotes that the cross sectional data is in the flat format.
serviceURL                                  xs:anyURI                 The serviceURL attribute indicates the URL of an SDMX SOAP web service from which the details of the object can be retrieved. Note that this can be a registry or and SDMX structural metadata repository, as they both implement that same web service interface.
structureURL                                xs:anyURI                 The structureURL attribute indicates the URL of a SDMX-ML structure message (in the same version as the source document) in which the externally referenced object is contained. Note that this may be a URL of an SDMX RESTful web service which will return the referenced object.
=========================================== ========================= ====================================================================================================================================================================================================================================================================================

Element Documentation:

================= ================================ ===========================================================================================
**Name**          **Type**                         **Documentation**
================= ================================ ===========================================================================================
ProvisionAgrement ProvisionAgreementRe ferenceType ProvisionAgreement references a provision agreement which the data is reported against.
StructureUsage    DataflowReferenceTyp e           StructureUsage references a dataflow which the data is reported against.
Structure         DataStructureReferen ceType      Structure references the data structure definition which defines the structure of the data.
================= ================================ ===========================================================================================

**MetadataStructureType: **\ MetadataStructureType is an abstract base
type the forms the basis of the structural information for any metadata
message. A reference to the metadata structure definition or a
metadataflow must be provided. This can be used to determine the
structure of the message.

Derivation:

| *PayloadStructureType* (restriction) 
|    |image49|\ *MetadataStructureType*

Attributes:

structureID, schemaURL?, namespace?, serviceURL?, structureURL?

Content:

(ProvisionAgrement \| StructureUsage \| Structure)

Attribute Documentation:

============ ========= ====================================================================================================================================================================================================================================================================================
**Name**     **Type**  **Documentation**
============ ========= ====================================================================================================================================================================================================================================================================================
structureID  xs:ID     The structureID attribute uniquely identifies the structure for the purpose of referencing it from the payload. This is only used in structure specific formats. Although it is required, it is only useful when more than one data set is present in the message.
schemaURL    xs:anyURI The schemaURL attribute provides a location from which the structure specific schema can be located.
namespace    xs:anyURI The namespace attribute is used to provide the namespace for structure-specific formats. By communicating this information in the header, it is possible to generate the structure specific schema while processing the message.
serviceURL   xs:anyURI The serviceURL attribute indicates the URL of an SDMX SOAP web service from which the details of the object can be retrieved. Note that this can be a registry or and SDMX structural metadata repository, as they both implement that same web service interface.
structureURL xs:anyURI The structureURL attribute indicates the URL of a SDMX-ML structure message (in the same version as the source document) in which the externally referenced object is contained. Note that this may be a URL of an SDMX RESTful web service which will return the referenced object.
============ ========= ====================================================================================================================================================================================================================================================================================

Element Documentation:

================= ================================ ===================================================================================================
**Name**          **Type**                         **Documentation**
================= ================================ ===================================================================================================
ProvisionAgrement ProvisionAgreementRe ferenceType ProvisionAgreement references a provision agreement which the metadata is reported against.
StructureUsage    MetadataflowReferenc eType       StructureUsage references a metadataflow which the metadata is reported against.
Structure         MetadataStructureRef erenceType  Structure references the metadata structure definition which defines the structure of the metadata.
================= ================================ ===================================================================================================

**StructureSpecificMetadataStructureType: **\ StructureSpecificMetadataStructureType
defines the structural information for a structured metadata message.

Derivation:

| *PayloadStructureType* (restriction) 
|    |image50|\ *MetadataStructureType* (restriction) 
|          |image51|\ StructureSpecificMetadataStructureType

Attributes:

structureID, schemaURL?, namespace, serviceURL?, structureURL?

Content:

(ProvisionAgrement \| StructureUsage \| Structure)

Attribute Documentation:

============ ========= ====================================================================================================================================================================================================================================================================================
**Name**     **Type**  **Documentation**
============ ========= ====================================================================================================================================================================================================================================================================================
structureID  xs:ID     The structureID attribute uniquely identifies the structure for the purpose of referencing it from the payload. This is only used in structure specific formats. Although it is required, it is only useful when more than one data set is present in the message.
schemaURL    xs:anyURI The schemaURL attribute provides a location from which the structure specific schema can be located.
namespace    xs:anyURI The namespace attribute is used to provide the namespace for structure-specific formats. By communicating this information in the header, it is possible to generate the structure specific schema while processing the message.
serviceURL   xs:anyURI The serviceURL attribute indicates the URL of an SDMX SOAP web service from which the details of the object can be retrieved. Note that this can be a registry or and SDMX structural metadata repository, as they both implement that same web service interface.
structureURL xs:anyURI The structureURL attribute indicates the URL of a SDMX-ML structure message (in the same version as the source document) in which the externally referenced object is contained. Note that this may be a URL of an SDMX RESTful web service which will return the referenced object.
============ ========= ====================================================================================================================================================================================================================================================================================

Element Documentation:

================= ================================ ===================================================================================================
**Name**          **Type**                         **Documentation**
================= ================================ ===================================================================================================
ProvisionAgrement ProvisionAgreementRe ferenceType ProvisionAgreement references a provision agreement which the metadata is reported against.
StructureUsage    MetadataflowReferenc eType       StructureUsage references a metadataflow which the metadata is reported against.
Structure         MetadataStructureRef erenceType  Structure references the metadata structure definition which defines the structure of the metadata.
================= ================================ ===================================================================================================

**GenericMetadataStructureType: **\ GenericMetadataStructureType defines
the structural information for a generic metadata message.

Derivation:

| *PayloadStructureType* (restriction) 
|    |image52|\ *MetadataStructureType* (restriction) 
|          |image53|\ GenericMetadataStructureType

Attributes:

structureID, schemaURL?, serviceURL?, structureURL?

Content:

(ProvisionAgrement \| StructureUsage \| Structure)

Attribute Documentation:

============ ========= ====================================================================================================================================================================================================================================================================================
**Name**     **Type**  **Documentation**
============ ========= ====================================================================================================================================================================================================================================================================================
structureID  xs:ID     The structureID attribute uniquely identifies the structure for the purpose of referencing it from the payload. This is only used in structure specific formats. Although it is required, it is only useful when more than one data set is present in the message.
schemaURL    xs:anyURI The schemaURL attribute provides a location from which the structure specific schema can be located.
serviceURL   xs:anyURI The serviceURL attribute indicates the URL of an SDMX SOAP web service from which the details of the object can be retrieved. Note that this can be a registry or and SDMX structural metadata repository, as they both implement that same web service interface.
structureURL xs:anyURI The structureURL attribute indicates the URL of a SDMX-ML structure message (in the same version as the source document) in which the externally referenced object is contained. Note that this may be a URL of an SDMX RESTful web service which will return the referenced object.
============ ========= ====================================================================================================================================================================================================================================================================================

Element Documentation:

================= ================================ ===================================================================================================
**Name**          **Type**                         **Documentation**
================= ================================ ===================================================================================================
ProvisionAgrement ProvisionAgreementRe ferenceType ProvisionAgreement references a provision agreement which the metadata is reported against.
StructureUsage    MetadataflowReferenc eType       StructureUsage references a metadataflow which the metadata is reported against.
Structure         MetadataStructureRef erenceType  Structure references the metadata structure definition which defines the structure of the metadata.
================= ================================ ===================================================================================================

**EmptyType: **\ EmptyType is an empty complex type for elements where
the presence of the tag indicates all that is necessary.

Content:

{Empty}

**ReferenceType: **\ ReferenceType is an abstract base type. It is used
as the basis for all references, to all for a top level generic object
reference that can be substituted with an explicit reference to any
object. Any reference can consist of a Ref (which contains all required
reference fields separately) and/or a URN. These must result in the
identification of the same object. Note that the Ref and URN elements
are local and unqualified in order to allow for refinement of this
structure outside of the namespace. This allows any reference to further
refined by a different namespace. For example, a metadata structure
definition specific metadata set might wish to restrict the URN to only
allow for a value from an enumerated list. The general URN structure,
for the purpose of mapping the reference fields is as follows:
urn:sdmx:org.package-name.class-name=agency-id:(maintainable-parent-object-id[maintainable-parent-object-version].)?(container-object-id.)?object-id([object-version])?.

Content:

( (Ref, URN?) \| URN)

Element Documentation:

======== ============= =============================================================================================================================================================================================================
**Name** **Type**      **Documentation**
======== ============= =============================================================================================================================================================================================================
Ref      *RefBaseType* Ref is used to provide a complete set of reference fields. Derived reference types will restrict the RefType so that the content of the Ref element requires exactly what is needed for a complete reference.
URN      xs:anyURI     URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
URN      xs:anyURI     URN is used to hold the URN of the referenced object.
======== ============= =============================================================================================================================================================================================================

**RefBaseType: **\ RefBaseType is an abstract base type the defines the
basis for any set of complete reference fields. This should be refined
by derived types so that only the necessary fields are available and
required as necessary. This can be used for both full and local
references (when some of the values are implied from another context). A
local reference is indicated with the local attribute. The values in
this type correspond directly to the components of the URN structure,
and thus can be used to compose a URN when the local attribute value is
false. As this is the case, any reference components which are not part
of the URN structure should not be present in the derived types.

Attributes:

agencyID?, maintainableParentID?, maintainableParentVersion?,
containerID?, id, version?, local?, class?, package?

Content:

{Empty}

Attribute Documentation:

========================= ======================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                  **Type**                 **Documentation**
========================= ======================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
agencyID                  NestedNCNameIDType       The agencyID attribute identifies the maintenance agency for the object being referenced (agency-id in the URN structure). This is optional to allow for local references (where the other reference fields are inferred from another context), but all complete references will require this.
maintainableParentID      IDType                   The maintainableParentID attribute identifies the maintainable object in which the referenced object is defined, if applicable (maintainable-parent-object-id in the URN structure). This is only used in references where the referenced object is not itself maintainable.
maintainableParentVersion VersionType              The maintainableParentVersion attribute identifies the version of the maintainable object in which the referenced object is defined (maintainable-parent-object-version in the URN structure). This is only used in references where the referenced object is not itself maintainable. This should only be used when the maintainableParentID is present. If this is available, a default of 1.0 will always apply.
containerID               NestedIDType             The containerID attribute identifies the object within a maintainable object in which the referenced object is defined (container-object-id in the URN structure). This is only used in references where the referenced object is not contained directly within a maintainable object (e.g. a Component within a ComponentList, within a maintainable Structure). If the container has a fixed identifier, this attribute will not be present.
id                        NestedIDType             The id attribute identifies the object being referenced, and is therefore always required.
version                   VersionType              The version attribute identifies the version of the object being reference, if applicable. If this is available, a default value of 1.0 will always apply.
local                     xs:boolean               The local attribute indicates whether this set of reference fields is meant for local referencing, in which case some of the reference fields will be implied from another context. Concrete instances of this class will always fix this value to either true or false, depending on their intended usage. If the value is fixed to true, then the complete set of reference fields will be required and a URN can be fully composed from the values.
class                     ObjectTypeCodelistTy pe  The class attribute indicates the class name of the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
package                   PackageTypeCodelistT ype The package attribute indicates the package name for the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
========================= ======================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================

**ObjectReferenceType: **\ ObjectReferenceType is a generic reference
which allows for any object to be referenced. The type of object
actually referenced can be determined from the URN or from the class
attribute of the full set of reference fields.

Derivation:

| *ReferenceType* (restriction) 
|    |image54|\ ObjectReferenceType

Content:

( (Ref, URN?) \| URN)

Element Documentation:

======== ============= =============================================================================================================================================================================================================
**Name** **Type**      **Documentation**
======== ============= =============================================================================================================================================================================================================
Ref      ObjectRefType Ref is used to provide a complete set of reference fields. Derived reference types will restrict the RefType so that the content of the Ref element requires exactly what is needed for a complete reference.
URN      xs:anyURI     URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
URN      xs:anyURI     URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
======== ============= =============================================================================================================================================================================================================

**ObjectRefType: **\ ObjectRefType contains a set of reference fields
for the purpose of referencing any object. This cannot be a local
reference, therefore the agency identifier is required. It is also
required that the class and package be supplied for the referenced
object such that a complete URN reference can be built from the values
provided. Note that this is not capable of fully validating that all
necessary fields are supplied for a given object type.

Derivation:

| *RefBaseType* (restriction) 
|    |image55|\ ObjectRefType

Attributes:

agencyID, maintainableParentID?, maintainableParentVersion?,
containerID?, id, version?, local?, class, package

Content:

{Empty}

Attribute Documentation:

========================= ======================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                  **Type**                 **Documentation**
========================= ======================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
agencyID                  NestedNCNameIDType       The agencyID attribute identifies the maintenance agency for the object being referenced (agency-id in the URN structure). This is optional to allow for local references (where the other reference fields are inferred from another context), but all complete references will require this.
maintainableParentID      IDType                   The maintainableParentID attribute identifies the maintainable object in which the referenced object is defined, if applicable (maintainable-parent-object-id in the URN structure). This is only used in references where the referenced object is not itself maintainable.
maintainableParentVersion VersionType              The maintainableParentVersion attribute identifies the version of the maintainable object in which the referenced object is defined (maintainable-parent-object-version in the URN structure). This is only used in references where the referenced object is not itself maintainable. This should only be used when the maintainableParentID is present. If this is available, a default of 1.0 will always apply.
containerID               NestedIDType             The containerID attribute identifies the object within a maintainable object in which the referenced object is defined (container-object-id in the URN structure). This is only used in references where the referenced object is not contained directly within a maintainable object (e.g. a Component within a ComponentList, within a maintainable Structure). If the container has a fixed identifier, this attribute will not be present.
id                        NestedIDType             The id attribute identifies the object being referenced, and is therefore always required.
version                   VersionType              The version attribute identifies the version of the object being reference, if applicable. If this is available, a default value of 1.0 will always apply.
local (fixed: false)      xs:boolean               The local attribute indicates whether this set of reference fields is meant for local referencing, in which case some of the reference fields will be implied from another context. Concrete instances of this class will always fix this value to either true or false, depending on their intended usage. If the value is fixed to true, then the complete set of reference fields will be required and a URN can be fully composed from the values.
class                     ObjectTypeCodelistTy pe  The class attribute indicates the class name of the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
package                   PackageTypeCodelistT ype The package attribute indicates the package name for the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
========================= ======================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================

**MaintainableRefBaseType: **\ MaintainableRefBaseType is an abstract
base type for referencing a maintainable object.

Derivation:

| *RefBaseType* (restriction) 
|    |image56|\ *MaintainableRefBaseType*

Attributes:

agencyID, id, version?, local?, class?, package?

Content:

{Empty}

Attribute Documentation:

====================== ============================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**               **Type**                      **Documentation**
====================== ============================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
agencyID               NestedNCNameIDType            The agencyID attribute identifies the maintenance agency for the object being referenced (agency-id in the URN structure). This is optional to allow for local references (where the other reference fields are inferred from another context), but all complete references will require this.
id                     IDType                        The id attribute identifies the object being referenced, and is therefore always required.
version (default: 1.0) VersionType                   The version attribute identifies the version of the object being reference, if applicable. If this is available, a default value of 1.0 will always apply.
local (fixed: false)   xs:boolean                    The local attribute indicates whether this set of reference fields is meant for local referencing, in which case some of the reference fields will be implied from another context. Concrete instances of this class will always fix this value to either true or false, depending on their intended usage. If the value is fixed to true, then the complete set of reference fields will be required and a URN can be fully composed from the values.
class                  MaintainableTypeCode listType The class attribute indicates the class name of the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
package                PackageTypeCodelistT ype      The package attribute indicates the package name for the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
====================== ============================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================

**MaintainableRefType: **\ MaintainableRefType contains a complete set
of reference fields for referencing any maintainable object.

Derivation:

| *RefBaseType* (restriction) 
|    |image57|\ *MaintainableRefBaseType* (restriction) 
|          |image58|\ MaintainableRefType

Attributes:

agencyID, id, version?, local?, class, package

Content:

{Empty}

Attribute Documentation:

====================== ===================================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**               **Type**                              **Documentation**
====================== ===================================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
agencyID               NestedNCNameIDType                    The agencyID attribute identifies the maintenance agency for the object being referenced (agency-id in the URN structure). This is optional to allow for local references (where the other reference fields are inferred from another context), but all complete references will require this.
id                     IDType                                The id attribute identifies the object being referenced, and is therefore always required.
version (default: 1.0) VersionType                           The version attribute identifies the version of the object being reference, if applicable. If this is available, a default value of 1.0 will always apply.
local (fixed: false)   xs:boolean                            The local attribute indicates whether this set of reference fields is meant for local referencing, in which case some of the reference fields will be implied from another context. Concrete instances of this class will always fix this value to either true or false, depending on their intended usage. If the value is fixed to true, then the complete set of reference fields will be required and a URN can be fully composed from the values.
class                  ConcreteMaintainable TypeCodelistType The class attribute indicates the class name of the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
package                PackageTypeCodelistT ype              The package attribute indicates the package name for the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
====================== ===================================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================

**ItemSchemeRefBaseType: **\ ItemSchemeRefBaseType is an abstract base
type for referencing an item scheme.

Derivation:

| *RefBaseType* (restriction) 
|    |image59|\ *MaintainableRefBaseType* (restriction) 
|          |image60|\ *ItemSchemeRefBaseType*

Attributes:

agencyID, id, version?, local?, class?, package?

Content:

{Empty}

Attribute Documentation:

====================== ================================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**               **Type**                           **Documentation**
====================== ================================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
agencyID               NestedNCNameIDType                 The agencyID attribute identifies the maintenance agency for the object being referenced (agency-id in the URN structure). This is optional to allow for local references (where the other reference fields are inferred from another context), but all complete references will require this.
id                     IDType                             The id attribute identifies the object being referenced, and is therefore always required.
version (default: 1.0) VersionType                        The version attribute identifies the version of the object being reference, if applicable. If this is available, a default value of 1.0 will always apply.
local (fixed: false)   xs:boolean                         The local attribute indicates whether this set of reference fields is meant for local referencing, in which case some of the reference fields will be implied from another context. Concrete instances of this class will always fix this value to either true or false, depending on their intended usage. If the value is fixed to true, then the complete set of reference fields will be required and a URN can be fully composed from the values.
class                  ItemSchemeTypeCodeli stType        The class attribute indicates the class name of the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
package                ItemSchemePackageTyp eCodelistType The package attribute indicates the package name for the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
====================== ================================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================

**ItemSchemeRefType: **\ ItemSchemeRefType contains a complete set of
reference fields for referencing any item scheme. The class and package
a required so that the reference is explicit as to the exact object
being referenced.

Derivation:

| *RefBaseType* (restriction) 
|    |image61|\ *MaintainableRefBaseType* (restriction) 
|          |image62|\ *ItemSchemeRefBaseType* (restriction) 
|                |image63|\ ItemSchemeRefType

Attributes:

agencyID, id, version?, local?, class, package

Content:

{Empty}

Attribute Documentation:

====================== ================================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**               **Type**                           **Documentation**
====================== ================================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
agencyID               NestedNCNameIDType                 The agencyID attribute identifies the maintenance agency for the object being referenced (agency-id in the URN structure). This is optional to allow for local references (where the other reference fields are inferred from another context), but all complete references will require this.
id                     IDType                             The id attribute identifies the object being referenced, and is therefore always required.
version (default: 1.0) VersionType                        The version attribute identifies the version of the object being reference, if applicable. If this is available, a default value of 1.0 will always apply.
local (fixed: false)   xs:boolean                         The local attribute indicates whether this set of reference fields is meant for local referencing, in which case some of the reference fields will be implied from another context. Concrete instances of this class will always fix this value to either true or false, depending on their intended usage. If the value is fixed to true, then the complete set of reference fields will be required and a URN can be fully composed from the values.
class                  ItemSchemeTypeCodeli stType        The class attribute indicates the class name of the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
package                ItemSchemePackageTyp eCodelistType The package attribute indicates the package name for the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
====================== ================================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================

**StructureOrUsageRefBaseType: **\ StructureOrUsageRefBaseType is an
abstract base type for referencing a structure or structure usage.

Derivation:

| *RefBaseType* (restriction) 
|    |image64|\ *MaintainableRefBaseType* (restriction) 
|          |image65|\ *StructureOrUsageRefBaseType*

Attributes:

agencyID, id, version?, local?, class?, package?

Content:

{Empty}

Attribute Documentation:

====================== ================================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**               **Type**                          **Documentation**
====================== ================================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
agencyID               NestedNCNameIDType                The agencyID attribute identifies the maintenance agency for the object being referenced (agency-id in the URN structure). This is optional to allow for local references (where the other reference fields are inferred from another context), but all complete references will require this.
id                     IDType                            The id attribute identifies the object being referenced, and is therefore always required.
version (default: 1.0) VersionType                       The version attribute identifies the version of the object being reference, if applicable. If this is available, a default value of 1.0 will always apply.
local (fixed: false)   xs:boolean                        The local attribute indicates whether this set of reference fields is meant for local referencing, in which case some of the reference fields will be implied from another context. Concrete instances of this class will always fix this value to either true or false, depending on their intended usage. If the value is fixed to true, then the complete set of reference fields will be required and a URN can be fully composed from the values.
class                  StructureOrUsageType CodelistType The class attribute indicates the class name of the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
package                StructurePackageType CodelistType The package attribute indicates the package name for the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
====================== ================================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================

**StructureRefBaseType: **\ StructureRefBaseType is an abstract base
type for referencing a structure.

Derivation:

| *RefBaseType* (restriction) 
|    |image66|\ *MaintainableRefBaseType* (restriction) 
|          |image67|\ *StructureOrUsageRefBaseType* (restriction) 
|                |image68|\ *StructureRefBaseType*

Attributes:

agencyID, id, version?, local?, class?, package?

Content:

{Empty}

Attribute Documentation:

====================== ================================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**               **Type**                          **Documentation**
====================== ================================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
agencyID               NestedNCNameIDType                The agencyID attribute identifies the maintenance agency for the object being referenced (agency-id in the URN structure). This is optional to allow for local references (where the other reference fields are inferred from another context), but all complete references will require this.
id                     IDType                            The id attribute identifies the object being referenced, and is therefore always required.
version (default: 1.0) VersionType                       The version attribute identifies the version of the object being reference, if applicable. If this is available, a default value of 1.0 will always apply.
local (fixed: false)   xs:boolean                        The local attribute indicates whether this set of reference fields is meant for local referencing, in which case some of the reference fields will be implied from another context. Concrete instances of this class will always fix this value to either true or false, depending on their intended usage. If the value is fixed to true, then the complete set of reference fields will be required and a URN can be fully composed from the values.
class                  StructureTypeCodelis tType        The class attribute indicates the class name of the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
package                StructurePackageType CodelistType The package attribute indicates the package name for the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
====================== ================================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================

**StructureRefType: **\ StructureRefType contains a set of reference
fields for referencing any structure.

Derivation:

| *RefBaseType* (restriction) 
|    |image69|\ *MaintainableRefBaseType* (restriction) 
|          |image70|\ *StructureOrUsageRefBaseType* (restriction) 
|                |image71|\ *StructureRefBaseType* (restriction) 
|                      |image72|\ StructureRefType

Attributes:

agencyID, id, version?, local?, class, package

Content:

{Empty}

Attribute Documentation:

====================== ================================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**               **Type**                          **Documentation**
====================== ================================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
agencyID               NestedNCNameIDType                The agencyID attribute identifies the maintenance agency for the object being referenced (agency-id in the URN structure). This is optional to allow for local references (where the other reference fields are inferred from another context), but all complete references will require this.
id                     IDType                            The id attribute identifies the object being referenced, and is therefore always required.
version (default: 1.0) VersionType                       The version attribute identifies the version of the object being reference, if applicable. If this is available, a default value of 1.0 will always apply.
local (fixed: false)   xs:boolean                        The local attribute indicates whether this set of reference fields is meant for local referencing, in which case some of the reference fields will be implied from another context. Concrete instances of this class will always fix this value to either true or false, depending on their intended usage. If the value is fixed to true, then the complete set of reference fields will be required and a URN can be fully composed from the values.
class                  StructureTypeCodelis tType        The class attribute indicates the class name of the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
package                StructurePackageType CodelistType The package attribute indicates the package name for the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
====================== ================================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================

**StructureUsageRefBaseType: **\ StructureUsageRefBaseType is an
abstract base type for referencing a structure usage.

Derivation:

| *RefBaseType* (restriction) 
|    |image73|\ *MaintainableRefBaseType* (restriction) 
|          |image74|\ *StructureOrUsageRefBaseType* (restriction) 
|                |image75|\ *StructureUsageRefBaseType*

Attributes:

agencyID, id, version?, local?, class?, package?

Content:

{Empty}

Attribute Documentation:

====================== ================================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**               **Type**                          **Documentation**
====================== ================================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
agencyID               NestedNCNameIDType                The agencyID attribute identifies the maintenance agency for the object being referenced (agency-id in the URN structure). This is optional to allow for local references (where the other reference fields are inferred from another context), but all complete references will require this.
id                     IDType                            The id attribute identifies the object being referenced, and is therefore always required.
version (default: 1.0) VersionType                       The version attribute identifies the version of the object being reference, if applicable. If this is available, a default value of 1.0 will always apply.
local (fixed: false)   xs:boolean                        The local attribute indicates whether this set of reference fields is meant for local referencing, in which case some of the reference fields will be implied from another context. Concrete instances of this class will always fix this value to either true or false, depending on their intended usage. If the value is fixed to true, then the complete set of reference fields will be required and a URN can be fully composed from the values.
class                  StructureUsageTypeCo delistType   The class attribute indicates the class name of the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
package                StructurePackageType CodelistType The package attribute indicates the package name for the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
====================== ================================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================

**StructureUsageRefType: **\ StructureUsageRefType contains a set of
reference fields for referencing any structure usage.

Derivation:

| *RefBaseType* (restriction) 
|    |image76|\ *MaintainableRefBaseType* (restriction) 
|          |image77|\ *StructureOrUsageRefBaseType* (restriction) 
|                |image78|\ *StructureUsageRefBaseType* (restriction) 
|                      |image79|\ StructureUsageRefType

Attributes:

agencyID, id, version?, local?, class, package

Content:

{Empty}

Attribute Documentation:

====================== ================================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**               **Type**                          **Documentation**
====================== ================================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
agencyID               NestedNCNameIDType                The agencyID attribute identifies the maintenance agency for the object being referenced (agency-id in the URN structure). This is optional to allow for local references (where the other reference fields are inferred from another context), but all complete references will require this.
id                     IDType                            The id attribute identifies the object being referenced, and is therefore always required.
version (default: 1.0) VersionType                       The version attribute identifies the version of the object being reference, if applicable. If this is available, a default value of 1.0 will always apply.
local (fixed: false)   xs:boolean                        The local attribute indicates whether this set of reference fields is meant for local referencing, in which case some of the reference fields will be implied from another context. Concrete instances of this class will always fix this value to either true or false, depending on their intended usage. If the value is fixed to true, then the complete set of reference fields will be required and a URN can be fully composed from the values.
class                  StructureUsageTypeCo delistType   The class attribute indicates the class name of the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
package                StructurePackageType CodelistType The package attribute indicates the package name for the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
====================== ================================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================

**ChildObjectRefBaseType: **\ ChildObjectRefBaseType is an abstract base
type for referencing any child object defined directly within a
maintainable object.

Derivation:

| *RefBaseType* (restriction) 
|    |image80|\ *ChildObjectRefBaseType*

Attributes:

agencyID, maintainableParentID, maintainableParentVersion?, id, local?,
class?, package?

Content:

{Empty}

Attribute Documentation:

======================================== ======================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                                 **Type**                 **Documentation**
======================================== ======================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
agencyID                                 NestedNCNameIDType       The agencyID attribute identifies the maintenance agency for the object being referenced (agency-id in the URN structure). This is optional to allow for local references (where the other reference fields are inferred from another context), but all complete references will require this.
maintainableParentID                     IDType                   The maintainableParentID attribute identifies the maintainable object in which the referenced object is defined, if applicable (maintainable-parent-object-id in the URN structure). This is only used in references where the referenced object is not itself maintainable.
maintainableParentVersion (default: 1.0) VersionType              The maintainableParentVersion attribute identifies the version of the maintainable object in which the referenced object is defined (maintainable-parent-object-version in the URN structure). This is only used in references where the referenced object is not itself maintainable. This should only be used when the maintainableParentID is present. If this is available, a default of 1.0 will always apply.
id                                       NestedIDType             The id attribute identifies the object being referenced, and is therefore always required.
local (fixed: false)                     xs:boolean               The local attribute indicates whether this set of reference fields is meant for local referencing, in which case some of the reference fields will be implied from another context. Concrete instances of this class will always fix this value to either true or false, depending on their intended usage. If the value is fixed to true, then the complete set of reference fields will be required and a URN can be fully composed from the values.
class                                    ObjectTypeCodelistTy pe  The class attribute indicates the class name of the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
package                                  PackageTypeCodelistT ype The package attribute indicates the package name for the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
======================================== ======================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================

**ContainerChildObjectRefBaseType: **\ ContainerChildObjectRefBaseType
is an abstract base type for referencing any child object within
container defined in a maintainable object.

Derivation:

| *RefBaseType* (restriction) 
|    |image81|\ *ContainerChildObjectRefBaseType*

Attributes:

agencyID, maintainableParentID, maintainableParentVersion?,
containerID?, id, version?, local?, class?, package?

Content:

{Empty}

Attribute Documentation:

======================================== ======================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                                 **Type**                 **Documentation**
======================================== ======================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
agencyID                                 NestedNCNameIDType       The agencyID attribute identifies the maintenance agency for the object being referenced (agency-id in the URN structure). This is optional to allow for local references (where the other reference fields are inferred from another context), but all complete references will require this.
maintainableParentID                     IDType                   The maintainableParentID attribute identifies the maintainable object in which the referenced object is defined, if applicable (maintainable-parent-object-id in the URN structure). This is only used in references where the referenced object is not itself maintainable.
maintainableParentVersion (default: 1.0) VersionType              The maintainableParentVersion attribute identifies the version of the maintainable object in which the referenced object is defined (maintainable-parent-object-version in the URN structure). This is only used in references where the referenced object is not itself maintainable. This should only be used when the maintainableParentID is present. If this is available, a default of 1.0 will always apply.
containerID                              NestedIDType             The containerID attribute identifies the object within a maintainable object in which the referenced object is defined (container-object-id in the URN structure). This is only used in references where the referenced object is not contained directly within a maintainable object (e.g. a Component within a ComponentList, within a maintainable Structure). If the container has a fixed identifier, this attribute will not be present.
id                                       NestedIDType             The id attribute identifies the object being referenced, and is therefore always required.
version                                  VersionType              The version attribute identifies the version of the object being reference, if applicable. If this is available, a default value of 1.0 will always apply.
local (fixed: false)                     xs:boolean               The local attribute indicates whether this set of reference fields is meant for local referencing, in which case some of the reference fields will be implied from another context. Concrete instances of this class will always fix this value to either true or false, depending on their intended usage. If the value is fixed to true, then the complete set of reference fields will be required and a URN can be fully composed from the values.
class                                    ObjectTypeCodelistTy pe  The class attribute indicates the class name of the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
package                                  PackageTypeCodelistT ype The package attribute indicates the package name for the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
======================================== ======================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================

**ItemRefBaseType: **\ ItemRefBaseType is an abstract base type for
referencing an item within an item scheme.

Derivation:

| *RefBaseType* (restriction) 
|    |image82|\ *ChildObjectRefBaseType* (restriction) 
|          |image83|\ *ItemRefBaseType*

Attributes:

agencyID, maintainableParentID, maintainableParentVersion?, id, local?,
class?, package?

Content:

{Empty}

Attribute Documentation:

======================================== ================================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                                 **Type**                           **Documentation**
======================================== ================================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
agencyID                                 NestedNCNameIDType                 The agencyID attribute identifies the maintenance agency for the object being referenced (agency-id in the URN structure). This is optional to allow for local references (where the other reference fields are inferred from another context), but all complete references will require this.
maintainableParentID                     IDType                             The maintainableParentID references the item scheme in which the item being referenced is defined.
maintainableParentVersion (default: 1.0) VersionType                        The maintainableParentVersion attribute references the version of the item scheme in which the item being referenced is defined. If not supplied, a default value of 1.0 is assumed.
id                                       NestedIDType                       The id attribute identifies the object being referenced, and is therefore always required.
local (fixed: false)                     xs:boolean                         The local attribute indicates whether this set of reference fields is meant for local referencing, in which case some of the reference fields will be implied from another context. Concrete instances of this class will always fix this value to either true or false, depending on their intended usage. If the value is fixed to true, then the complete set of reference fields will be required and a URN can be fully composed from the values.
class                                    ItemTypeCodelistType               The class attribute indicates the class name of the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
package                                  ItemSchemePackageTyp eCodelistType The package attribute indicates the package name for the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
======================================== ================================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================

**ComponentListRefBaseType: **\ ComponentListRefBaseType is an abstract
base type for referencing a component list within a structure.

Derivation:

| *RefBaseType* (restriction) 
|    |image84|\ *ChildObjectRefBaseType* (restriction) 
|          |image85|\ *ComponentListRefBaseType*

Attributes:

agencyID, maintainableParentID, maintainableParentVersion?, id, local?,
class?, package?

Content:

{Empty}

Attribute Documentation:

======================================== ================================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                                 **Type**                          **Documentation**
======================================== ================================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
agencyID                                 NestedNCNameIDType                The agencyID attribute identifies the maintenance agency for the object being referenced (agency-id in the URN structure). This is optional to allow for local references (where the other reference fields are inferred from another context), but all complete references will require this.
maintainableParentID                     IDType                            The maintainableParentID references the structure in which the component list being referenced is defined.
maintainableParentVersion (default: 1.0) VersionType                       The maintainableParentVersion attribute references the version of the structure in which the component list being referenced is defined. If not supplied, a default value of 1.0 is assumed.
id                                       IDType                            The id attribute identifies the object being referenced, and is therefore always required.
local (fixed: false)                     xs:boolean                        The local attribute indicates whether this set of reference fields is meant for local referencing, in which case some of the reference fields will be implied from another context. Concrete instances of this class will always fix this value to either true or false, depending on their intended usage. If the value is fixed to true, then the complete set of reference fields will be required and a URN can be fully composed from the values.
class                                    ComponentListTypeCod elistType    The class attribute indicates the class name of the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
package                                  StructurePackageType CodelistType The package attribute indicates the package name for the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
======================================== ================================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================

**ComponentRefBaseType: **\ ComponentRefBaseType is an abstract base
type for referencing a component contained in a component list within a
structure.

Derivation:

| *RefBaseType* (restriction) 
|    |image86|\ *ContainerChildObjectRefBaseType* (restriction) 
|          |image87|\ *ComponentRefBaseType*

Attributes:

agencyID, maintainableParentID, maintainableParentVersion?,
containerID?, id, version?, local?, class?, package?

Content:

{Empty}

Attribute Documentation:

======================================== ================================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                                 **Type**                          **Documentation**
======================================== ================================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
agencyID                                 NestedNCNameIDType                The agencyID attribute identifies the maintenance agency for the object being referenced (agency-id in the URN structure). This is optional to allow for local references (where the other reference fields are inferred from another context), but all complete references will require this.
maintainableParentID                     IDType                            The maintainableParentID references the structure in which the component being referenced is defined.
maintainableParentVersion (default: 1.0) VersionType                       The maintainableParentVersion attribute references the version of the structure in which the component being referenced is defined. If not supplied, a default value of 1.0 is assumed.
containerID                              NestedIDType                      The containerID attribute references the component list of that contains the component being referenced. It is optional for the cases where the component list has a fixed identifier. Specific implementations of this will prohibit or require this accordingly.
id                                       NestedIDType                      The id attribute identifies the object being referenced, and is therefore always required.
version                                  VersionType                       The version attribute identifies the version of the object being reference, if applicable. If this is available, a default value of 1.0 will always apply.
local (fixed: false)                     xs:boolean                        The local attribute indicates whether this set of reference fields is meant for local referencing, in which case some of the reference fields will be implied from another context. Concrete instances of this class will always fix this value to either true or false, depending on their intended usage. If the value is fixed to true, then the complete set of reference fields will be required and a URN can be fully composed from the values.
class                                    ComponentTypeCodelis tType        The class attribute indicates the class name of the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
package                                  StructurePackageType CodelistType The package attribute indicates the package name for the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
======================================== ================================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================

**AnyCodelistRefType: **\ AnyCodelistRefType is a type for referencing
any codelist object (either a codelist or a hierarchical codelist).

Derivation:

| *RefBaseType* (restriction) 
|    |image88|\ *MaintainableRefBaseType* (restriction) 
|          |image89|\ AnyCodelistRefType

Attributes:

agencyID, id, version?, local?, class, package?

Content:

{Empty}

Attribute Documentation:

========================= ========================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                  **Type**                  **Documentation**
========================= ========================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
agencyID                  NestedNCNameIDType        The agencyID attribute identifies the maintenance agency for the object being referenced (agency-id in the URN structure). This is optional to allow for local references (where the other reference fields are inferred from another context), but all complete references will require this.
id                        IDType                    The id attribute identifies the object being referenced, and is therefore always required.
version (default: 1.0)    VersionType               The version attribute identifies the version of the object being reference, if applicable. If this is available, a default value of 1.0 will always apply.
local (fixed: false)      xs:boolean                The local attribute indicates whether this set of reference fields is meant for local referencing, in which case some of the reference fields will be implied from another context. Concrete instances of this class will always fix this value to either true or false, depending on their intended usage. If the value is fixed to true, then the complete set of reference fields will be required and a URN can be fully composed from the values.
class                     CodelistTypeCodelist Type The class attribute indicates the class name of the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
package (fixed: codelist) PackageTypeCodelistT ype  The package attribute indicates the package name for the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
========================= ========================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================

**StructureOrUsageRefType: **\ StructureOrUsageRefType is a type for
referencing a structure or structure usage.

Derivation:

| *RefBaseType* (restriction) 
|    |image90|\ *MaintainableRefBaseType* (restriction) 
|          |image91|\ *StructureOrUsageRefBaseType* (restriction) 
|                |image92|\ StructureOrUsageRefType

Attributes:

agencyID, id, version?, local?, class, package

Content:

{Empty}

Attribute Documentation:

====================== ================================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**               **Type**                          **Documentation**
====================== ================================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
agencyID               NestedNCNameIDType                The agencyID attribute identifies the maintenance agency for the object being referenced (agency-id in the URN structure). This is optional to allow for local references (where the other reference fields are inferred from another context), but all complete references will require this.
id                     IDType                            The id attribute identifies the object being referenced, and is therefore always required.
version (default: 1.0) VersionType                       The version attribute identifies the version of the object being reference, if applicable. If this is available, a default value of 1.0 will always apply.
local (fixed: false)   xs:boolean                        The local attribute indicates whether this set of reference fields is meant for local referencing, in which case some of the reference fields will be implied from another context. Concrete instances of this class will always fix this value to either true or false, depending on their intended usage. If the value is fixed to true, then the complete set of reference fields will be required and a URN can be fully composed from the values.
class                  StructureOrUsageType CodelistType The class attribute indicates the class name of the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
package                StructurePackageType CodelistType The package attribute indicates the package name for the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
====================== ================================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================

**LocalIdentifiableRefBaseType: **\ LocalIdentifiableRefBaseType is an
abstract base type which provides a local reference to any identifiable
object.

Derivation:

| *RefBaseType* (restriction) 
|    |image93|\ *LocalIdentifiableRefBaseType*

Attributes:

containerID?, id, local?, class?, package?

Content:

{Empty}

Attribute Documentation:

=================== ======================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**            **Type**                 **Documentation**
=================== ======================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
containerID         NestedIDType             The containerID attribute identifies the object within a maintainable object in which the referenced object is defined (container-object-id in the URN structure). This is only used in references where the referenced object is not contained directly within a maintainable object (e.g. a Component within a ComponentList, within a maintainable Structure). If the container has a fixed identifier, this attribute will not be present.
id                  NestedIDType             The id attribute identifies the object being referenced, and is therefore always required.
local (fixed: true) xs:boolean               The local attribute indicates whether this set of reference fields is meant for local referencing, in which case some of the reference fields will be implied from another context. Concrete instances of this class will always fix this value to either true or false, depending on their intended usage. If the value is fixed to true, then the complete set of reference fields will be required and a URN can be fully composed from the values.
class               ObjectTypeCodelistTy pe  The class attribute indicates the class name of the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
package             PackageTypeCodelistT ype The package attribute indicates the package name for the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
=================== ======================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================

**LocalItemRefBaseType: **\ LocalItemRefBaseType is an abstract base
type which provides a local reference to a item object.

Derivation:

| *RefBaseType* (restriction) 
|    |image94|\ *LocalIdentifiableRefBaseType* (restriction) 
|          |image95|\ *LocalItemRefBaseType*

Attributes:

id, local?, class?, package?

Content:

{Empty}

Attribute Documentation:

=================== ================================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**            **Type**                           **Documentation**
=================== ================================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
id                  NestedIDType                       The id attribute identifies the object being referenced, and is therefore always required.
local (fixed: true) xs:boolean                         The local attribute indicates whether this set of reference fields is meant for local referencing, in which case some of the reference fields will be implied from another context. Concrete instances of this class will always fix this value to either true or false, depending on their intended usage. If the value is fixed to true, then the complete set of reference fields will be required and a URN can be fully composed from the values.
class               ItemTypeCodelistType               The class attribute indicates the class name of the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
package             ItemSchemePackageTyp eCodelistType The package attribute indicates the package name for the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
=================== ================================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================

**LocalComponentListRefBaseType: **\ LocalComponentListRefBaseType is an
abstract base type which provides a local reference to a component list
object.

Derivation:

| *RefBaseType* (restriction) 
|    |image96|\ *LocalIdentifiableRefBaseType* (restriction) 
|          |image97|\ *LocalComponentListRefBaseType*

Attributes:

id, local?, class?, package?

Content:

{Empty}

Attribute Documentation:

=================== ================================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**            **Type**                          **Documentation**
=================== ================================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
id                  NestedIDType                      The id attribute identifies the object being referenced, and is therefore always required.
local (fixed: true) xs:boolean                        The local attribute indicates whether this set of reference fields is meant for local referencing, in which case some of the reference fields will be implied from another context. Concrete instances of this class will always fix this value to either true or false, depending on their intended usage. If the value is fixed to true, then the complete set of reference fields will be required and a URN can be fully composed from the values.
class               ComponentListTypeCod elistType    The class attribute indicates the class name of the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
package             StructurePackageType CodelistType The package attribute indicates the package name for the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
=================== ================================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================

**LocalComponentListComponentRefBaseType: **\ LocalComponentRefBaseType
is an abstract base type which provides a local reference to a component
object.

Derivation:

| *RefBaseType* (restriction) 
|    |image98|\ *LocalIdentifiableRefBaseType* (restriction) 
|          |image99|\ *LocalComponentListComponentRefBaseType*

Attributes:

containerID?, id, local?, class?, package?

Content:

{Empty}

Attribute Documentation:

=================== ======================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**            **Type**                 **Documentation**
=================== ======================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
containerID         IDType                   The containerID attribute identifies the object within a maintainable object in which the referenced object is defined (container-object-id in the URN structure). This is only used in references where the referenced object is not contained directly within a maintainable object (e.g. a Component within a ComponentList, within a maintainable Structure). If the container has a fixed identifier, this attribute will not be present.
id                  NestedIDType             The id attribute identifies the object being referenced, and is therefore always required.
local (fixed: true) xs:boolean               The local attribute indicates whether this set of reference fields is meant for local referencing, in which case some of the reference fields will be implied from another context. Concrete instances of this class will always fix this value to either true or false, depending on their intended usage. If the value is fixed to true, then the complete set of reference fields will be required and a URN can be fully composed from the values.
class               ObjectTypeCodelistTy pe  The class attribute indicates the class name of the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
package             PackageTypeCodelistT ype The package attribute indicates the package name for the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
=================== ======================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================

**LocalComponentListComponentRefType: **\ LocalComponentListComponentRefType
provides a local reference to any component object within a specific
component list. References for both of these are required as well as an
indication of which type of type of component is being referenced via
the class attribute.

Derivation:

| *RefBaseType* (restriction) 
|    |image100|\ *LocalIdentifiableRefBaseType* (restriction) 
|          |image101|\ *LocalComponentListComponentRefBaseType* (restriction) 
|                |image102|\ LocalComponentListComponentRefType

Attributes:

containerID, id, local?, class, package

Content:

{Empty}

Attribute Documentation:

=================== ================================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**            **Type**                          **Documentation**
=================== ================================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
containerID         IDType                            The containerID attribute identifies the object within a maintainable object in which the referenced object is defined (container-object-id in the URN structure). This is only used in references where the referenced object is not contained directly within a maintainable object (e.g. a Component within a ComponentList, within a maintainable Structure). If the container has a fixed identifier, this attribute will not be present.
id                  NestedIDType                      The id attribute identifies the object being referenced, and is therefore always required.
local (fixed: true) xs:boolean                        The local attribute indicates whether this set of reference fields is meant for local referencing, in which case some of the reference fields will be implied from another context. Concrete instances of this class will always fix this value to either true or false, depending on their intended usage. If the value is fixed to true, then the complete set of reference fields will be required and a URN can be fully composed from the values.
class               ComponentTypeCodelis tType        The class attribute indicates the class name of the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
package             StructurePackageType CodelistType The package attribute indicates the package name for the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
=================== ================================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================

**LocalComponentRefBaseType: **\ LocalComponentRefBaseType is an
abstract base type which provides a local reference to a component
object.

Derivation:

| *RefBaseType* (restriction) 
|    |image103|\ *LocalIdentifiableRefBaseType* (restriction) 
|          |image104|\ *LocalComponentListComponentRefBaseType* (restriction) 
|                |image105|\ *LocalComponentRefBaseType*

Attributes:

id, local?, class?, package?

Content:

{Empty}

Attribute Documentation:

=================== ======================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**            **Type**                 **Documentation**
=================== ======================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
id                  NestedIDType             The id attribute identifies the object being referenced, and is therefore always required.
local (fixed: true) xs:boolean               The local attribute indicates whether this set of reference fields is meant for local referencing, in which case some of the reference fields will be implied from another context. Concrete instances of this class will always fix this value to either true or false, depending on their intended usage. If the value is fixed to true, then the complete set of reference fields will be required and a URN can be fully composed from the values.
class               ObjectTypeCodelistTy pe  The class attribute indicates the class name of the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
package             PackageTypeCodelistT ype The package attribute indicates the package name for the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
=================== ======================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================

**LocalComponentRefType: **\ LocalComponentRefType provides a local
reference to any type component object.

Derivation:

| *RefBaseType* (restriction) 
|    |image106|\ *LocalIdentifiableRefBaseType* (restriction) 
|          |image107|\ *LocalComponentListComponentRefBaseType* (restriction) 
|                |image108|\ *LocalComponentRefBaseType* (restriction) 
|                      |image109|\ LocalComponentRefType

Attributes:

id, local?, class, package

Content:

{Empty}

Attribute Documentation:

=================== ================================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**            **Type**                          **Documentation**
=================== ================================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
id                  NestedIDType                      The id attribute identifies the object being referenced, and is therefore always required.
local (fixed: true) xs:boolean                        The local attribute indicates whether this set of reference fields is meant for local referencing, in which case some of the reference fields will be implied from another context. Concrete instances of this class will always fix this value to either true or false, depending on their intended usage. If the value is fixed to true, then the complete set of reference fields will be required and a URN can be fully composed from the values.
class               ComponentTypeCodelis tType        The class attribute indicates the class name of the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
package             StructurePackageType CodelistType The package attribute indicates the package name for the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
=================== ================================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================

**AnyLocalCodeRefType: **\ AnyLocalCodeRefType provides a local
reference to any code object.

Derivation:

| *RefBaseType* (restriction) 
|    |image110|\ AnyLocalCodeRefType

Attributes:

containerID?, id, version?, local?, class?, package?

Content:

{Empty}

Attribute Documentation:

========================= ======================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                  **Type**                 **Documentation**
========================= ======================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
containerID               IDType                   The containerID attribute references the hierarchy which defines the hierarchical code in the case that this reference is for a hierarchical code.
id                        NestedIDType             The id attribute identifies the object being referenced, and is therefore always required.
version                   VersionType              The version attribute identifies the version of the object being reference, if applicable. If this is available, a default value of 1.0 will always apply.
local (fixed: true)       xs:boolean               The local attribute indicates whether this set of reference fields is meant for local referencing, in which case some of the reference fields will be implied from another context. Concrete instances of this class will always fix this value to either true or false, depending on their intended usage. If the value is fixed to true, then the complete set of reference fields will be required and a URN can be fully composed from the values.
class                     CodeTypeCodelistType     The class attribute indicates the class name of the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
package (fixed: codelist) PackageTypeCodelistT ype The package attribute indicates the package name for the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
========================= ======================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================

**URNReferenceType: **\ URNReferenceType is a type referencing any
object via its URN. The exact type of object is not specified, although
it can be determined from the URN value.

Derivation:

| *ReferenceType* (restriction) 
|    |image111|\ URNReferenceType

Content:

URN

Element Documentation:

======== ========= ========================================================================================================================================================
**Name** **Type**  **Documentation**
======== ========= ========================================================================================================================================================
URN      xs:anyURI URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
======== ========= ========================================================================================================================================================

**MaintainableReferenceBaseType: **\ MaintainableReferenceBaseType is an
abstract base type for referencing a maintainable object. It consists of
a URN and/or a complete set of reference fields; agency, id, and
version.

Derivation:

| *ReferenceType* (restriction) 
|    |image112|\ *MaintainableReferenceBaseType*

Content:

( (Ref, URN?) \| URN)

Element Documentation:

======== ========================== =============================================================================================================================================================================================================
**Name** **Type**                   **Documentation**
======== ========================== =============================================================================================================================================================================================================
Ref      *MaintainableRefBaseT ype* Ref is used to provide a complete set of reference fields. Derived reference types will restrict the RefType so that the content of the Ref element requires exactly what is needed for a complete reference.
URN      xs:anyURI                  URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
URN      xs:anyURI                  URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
======== ========================== =============================================================================================================================================================================================================

**MaintainableReferenceType: **\ MaintainableReferenceType is a type for
referencing any maintainable object. It consists of a URN and/or a
complete set of reference fields; agency, id, and version.

Derivation:

| *ReferenceType* (restriction) 
|    |image113|\ *MaintainableReferenceBaseType* (restriction) 
|          |image114|\ MaintainableReferenceType

Content:

( (Ref, URN?) \| URN)

Element Documentation:

======== =================== =============================================================================================================================================================================================================
**Name** **Type**            **Documentation**
======== =================== =============================================================================================================================================================================================================
Ref      MaintainableRefType Ref is used to provide a complete set of reference fields. Derived reference types will restrict the RefType so that the content of the Ref element requires exactly what is needed for a complete reference.
URN      xs:anyURI           URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
URN      xs:anyURI           URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
======== =================== =============================================================================================================================================================================================================

**LocalIdentifiableReferenceType: **\ LocalIdentifiableReferenceType is
an abstract base type for referencing an identifiable object locally,
where the maintainable object in which it is defined is referenced in
another context..

Derivation:

| *ReferenceType* (restriction) 
|    |image115|\ *LocalIdentifiableReferenceType*

Content:

Ref

Element Documentation:

======== =============================== =============================================================================================================================================================================================================
**Name** **Type**                        **Documentation**
======== =============================== =============================================================================================================================================================================================================
Ref      *LocalIdentifiableRef BaseType* Ref is used to provide a complete set of reference fields. Derived reference types will restrict the RefType so that the content of the Ref element requires exactly what is needed for a complete reference.
======== =============================== =============================================================================================================================================================================================================

**StructureReferenceBaseType: **\ StructureReferneceBaseType is a
specific type of MaintainableReference that is used for referencing
structure definitions. It consists of a URN and/or a complete set of
reference fields; agency, id, and version.

Derivation:

| *ReferenceType* (restriction) 
|    |image116|\ *MaintainableReferenceBaseType* (restriction) 
|          |image117|\ *StructureReferenceBaseType*

Content:

( (Ref, URN?) \| URN)

Element Documentation:

======== ====================== =============================================================================================================================================================================================================
**Name** **Type**               **Documentation**
======== ====================== =============================================================================================================================================================================================================
Ref      *StructureRefBaseType* Ref is used to provide a complete set of reference fields. Derived reference types will restrict the RefType so that the content of the Ref element requires exactly what is needed for a complete reference.
URN      xs:anyURI              URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
URN      xs:anyURI              URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
======== ====================== =============================================================================================================================================================================================================

**StructureReferenceType: **\ StructureReferenceType is a specific type
of MaintainableReference that is used for referencing any structure. It
consists of a URN and/or a complete set of reference fields; agency, id,
and version.

Derivation:

| *ReferenceType* (restriction) 
|    |image118|\ *MaintainableReferenceBaseType* (restriction) 
|          |image119|\ *StructureReferenceBaseType* (restriction) 
|                |image120|\ StructureReferenceType

Content:

( (Ref, URN?) \| URN)

Element Documentation:

======== ================ =============================================================================================================================================================================================================
**Name** **Type**         **Documentation**
======== ================ =============================================================================================================================================================================================================
Ref      StructureRefType Ref is used to provide a complete set of reference fields. Derived reference types will restrict the RefType so that the content of the Ref element requires exactly what is needed for a complete reference.
URN      xs:anyURI        URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
URN      xs:anyURI        URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
======== ================ =============================================================================================================================================================================================================

**StructureUsageReferenceBaseType: **\ StructureUsageReferenceBaseType
is a specific type of MaintainableReference that is used for referencing
structure usages. It consists of a URN and/or a complete set of
reference fields; agency, id, and version.

Derivation:

| *ReferenceType* (restriction) 
|    |image121|\ *MaintainableReferenceBaseType* (restriction) 
|          |image122|\ *StructureUsageReferenceBaseType*

Content:

( (Ref, URN?) \| URN)

Element Documentation:

======== ============================ =============================================================================================================================================================================================================
**Name** **Type**                     **Documentation**
======== ============================ =============================================================================================================================================================================================================
Ref      *StructureUsageRefBas eType* Ref is used to provide a complete set of reference fields. Derived reference types will restrict the RefType so that the content of the Ref element requires exactly what is needed for a complete reference.
URN      xs:anyURI                    URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
URN      xs:anyURI                    URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
======== ============================ =============================================================================================================================================================================================================

**StructureUsageReferenceType: **\ StructureUsageReferenceType is a
specific type of MaintainableReference that is used for referencing any
structure usages. It consists of a URN and/or a complete set of
reference fields; agency, id, and version.

Derivation:

| *ReferenceType* (restriction) 
|    |image123|\ *MaintainableReferenceBaseType* (restriction) 
|          |image124|\ *StructureUsageReferenceBaseType* (restriction) 
|                |image125|\ StructureUsageReferenceType

Content:

( (Ref, URN?) \| URN)

Element Documentation:

======== ====================== =============================================================================================================================================================================================================
**Name** **Type**               **Documentation**
======== ====================== =============================================================================================================================================================================================================
Ref      StructureUsageRefTyp e Ref is used to provide a complete set of reference fields. Derived reference types will restrict the RefType so that the content of the Ref element requires exactly what is needed for a complete reference.
URN      xs:anyURI              URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
URN      xs:anyURI              URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
======== ====================== =============================================================================================================================================================================================================

**ItemSchemeReferenceBaseType: **\ ItemSchemeReferenceBaseType is a
specific type of MaintainableReference that is used for referencing item
schemes. It consists of a URN and/or a complete set of reference fields;
agency, id, and version.

Derivation:

| *ReferenceType* (restriction) 
|    |image126|\ *MaintainableReferenceBaseType* (restriction) 
|          |image127|\ *ItemSchemeReferenceBaseType*

Content:

( (Ref, URN?) \| URN)

Element Documentation:

======== ======================== =============================================================================================================================================================================================================
**Name** **Type**                 **Documentation**
======== ======================== =============================================================================================================================================================================================================
Ref      *ItemSchemeRefBaseTyp e* Ref is used to provide a complete set of reference fields. Derived reference types will restrict the RefType so that the content of the Ref element requires exactly what is needed for a complete reference.
URN      xs:anyURI                URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
URN      xs:anyURI                URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
======== ======================== =============================================================================================================================================================================================================

**ItemSchemeReferenceType: **\ ItemSchemeReferenceType is a reference
that is used for referencing any type of item scheme. It consists of a
URN and/or a complete set of reference fields; agency, id, and version.

Derivation:

| *ReferenceType* (restriction) 
|    |image128|\ *MaintainableReferenceBaseType* (restriction) 
|          |image129|\ *ItemSchemeReferenceBaseType* (restriction) 
|                |image130|\ ItemSchemeReferenceType

Content:

( (Ref, URN?) \| URN)

Element Documentation:

======== ================= =============================================================================================================================================================================================================
**Name** **Type**          **Documentation**
======== ================= =============================================================================================================================================================================================================
Ref      ItemSchemeRefType Ref is used to provide a complete set of reference fields. Derived reference types will restrict the RefType so that the content of the Ref element requires exactly what is needed for a complete reference.
URN      xs:anyURI         URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
URN      xs:anyURI         URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
======== ================= =============================================================================================================================================================================================================

**ChildObjectReferenceType: **\ ChildObjectReferenceType is an abstract
base type used for referencing a particular object defined directly
within a maintainable object. It consists of a URN and/or a complete set
of reference fields; agency, maintainable id (maintainableParentID),
maintainable version (maintainableParentVersion), the object id (which
can be nested), and optionally the object version (if applicable).

Derivation:

| *ReferenceType* (restriction) 
|    |image131|\ *ChildObjectReferenceType*

Content:

( (Ref, URN?) \| URN)

Element Documentation:

======== ========================= =============================================================================================================================================================================================================
**Name** **Type**                  **Documentation**
======== ========================= =============================================================================================================================================================================================================
Ref      *ChildObjectRefBaseTy pe* Ref is used to provide a complete set of reference fields. Derived reference types will restrict the RefType so that the content of the Ref element requires exactly what is needed for a complete reference.
URN      xs:anyURI                 URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
URN      xs:anyURI                 URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
======== ========================= =============================================================================================================================================================================================================

**ContainerChildObjectReferenceType: **\ ContainerChildObjectReferenceType
is an abstract base type used for referencing a particular object
defined in a container object within a maintainable object. It consists
of a URN and/or a complete set of reference fields; agency, maintainable
id (maintainableParentID), maintainable version
(maintainableParentVersion), container id (which is optional in order to
allow for containers with fixed values to be omitted), container version
(if applicable), the object id (which can be nested), and optionally the
object version (if applicable).

Derivation:

| *ReferenceType* (restriction) 
|    |image132|\ *ContainerChildObjectReferenceType*

Content:

( (Ref, URN?) \| URN)

Element Documentation:

======== ================================== =============================================================================================================================================================================================================
**Name** **Type**                           **Documentation**
======== ================================== =============================================================================================================================================================================================================
Ref      *ContainerChildObject RefBaseType* Ref is used to provide a complete set of reference fields. Derived reference types will restrict the RefType so that the content of the Ref element requires exactly what is needed for a complete reference.
URN      xs:anyURI                          URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
URN      xs:anyURI                          URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
======== ================================== =============================================================================================================================================================================================================

**ItemReferenceType: **\ ItemReferenceType is an abstract base type used
for referencing a particular item within an item scheme. Note that this
reference also has the ability to reference items contained within other
items inside of the item scheme. It consists of a URN and/or a complete
set of reference fields; agency, scheme id (maintainableParentID),
scheme version (maintainableParentVersion), and item id (which can be
nested).

Derivation:

| *ReferenceType* (restriction) 
|    |image133|\ *ChildObjectReferenceType* (restriction) 
|          |image134|\ *ItemReferenceType*

Content:

( (Ref, URN?) \| URN)

Element Documentation:

======== ================= =============================================================================================================================================================================================================
**Name** **Type**          **Documentation**
======== ================= =============================================================================================================================================================================================================
Ref      *ItemRefBaseType* Ref is used to provide a complete set of reference fields. Derived reference types will restrict the RefType so that the content of the Ref element requires exactly what is needed for a complete reference.
URN      xs:anyURI         URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
URN      xs:anyURI         URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
======== ================= =============================================================================================================================================================================================================

**ComponentListReferenceType: **\ ComponentListReferenceType is an
abstract base type used for referencing component lists within a
structure. It consists of a URN and/or a complete set of reference
fields (structure agency, structure id, structure version, and component
list id).

Derivation:

| *ReferenceType* (restriction) 
|    |image135|\ *ChildObjectReferenceType* (restriction) 
|          |image136|\ *ComponentListReferenceType*

Content:

( (Ref, URN?) \| URN)

Element Documentation:

======== =========================== =============================================================================================================================================================================================================
**Name** **Type**                    **Documentation**
======== =========================== =============================================================================================================================================================================================================
Ref      *ComponentListRefBase Type* Ref is used to provide a complete set of reference fields. Derived reference types will restrict the RefType so that the content of the Ref element requires exactly what is needed for a complete reference.
URN      xs:anyURI                   URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
URN      xs:anyURI                   URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
======== =========================== =============================================================================================================================================================================================================

**ComponentReferenceType: **\ ComponentReferenceType is an abstract base
type used for referencing components within a structure definition. It
consists of a URN and/or a complete set of reference fields (structure
agency, structure id, structure version, component list id, and
component id).

Derivation:

| *ReferenceType* (restriction) 
|    |image137|\ *ContainerChildObjectReferenceType* (restriction) 
|          |image138|\ *ComponentReferenceType*

Content:

( (Ref, URN?) \| URN)

Element Documentation:

======== ====================== =============================================================================================================================================================================================================
**Name** **Type**               **Documentation**
======== ====================== =============================================================================================================================================================================================================
Ref      *ComponentRefBaseType* Ref is used to provide a complete set of reference fields. Derived reference types will restrict the RefType so that the content of the Ref element requires exactly what is needed for a complete reference.
URN      xs:anyURI              URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
URN      xs:anyURI              URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
======== ====================== =============================================================================================================================================================================================================

**LocalItemReferenceType: **\ LocalItemReferenceType is an abstract base
type which provides a simple reference to an item where the reference to
the item scheme which defines it are provided in another context.

Derivation:

| *ReferenceType* (restriction) 
|    |image139|\ *LocalItemReferenceType*

Content:

Ref

Element Documentation:

======== ====================== =============================================================================================================================================================================================================
**Name** **Type**               **Documentation**
======== ====================== =============================================================================================================================================================================================================
Ref      *LocalItemRefBaseType* Ref is used to provide a complete set of reference fields. Derived reference types will restrict the RefType so that the content of the Ref element requires exactly what is needed for a complete reference.
======== ====================== =============================================================================================================================================================================================================

**LocalComponentListReferenceType: **\ LocalComponentListReferenceType
is an abstract base type which provides a simple reference to a
component list where the reference to the structure which defines it is
provided in another context.

Derivation:

| *ReferenceType* (restriction) 
|    |image140|\ *LocalComponentListReferenceType*

Content:

Ref

Element Documentation:

======== ================================ =============================================================================================================================================================================================================
**Name** **Type**                         **Documentation**
======== ================================ =============================================================================================================================================================================================================
Ref      *LocalComponentListRe fBaseType* Ref is used to provide a complete set of reference fields. Derived reference types will restrict the RefType so that the content of the Ref element requires exactly what is needed for a complete reference.
======== ================================ =============================================================================================================================================================================================================

**LocalComponentListComponentReferenceBaseType:**\ LocalComponentListComponentReferenceBaseType
is an abstract base type which provides a simple reference to any type
of component in a specific component list where the reference to the
structure which defines it are provided in another context, and the
component list may or may not be defined in another context.

Derivation:

| *ReferenceType* (restriction) 
|    |image141|\ *LocalComponentListComponentReferenceBaseType*

Content:

Ref

Element Documentation:

======== ========================================= =============================================================================================================================================================================================================
**Name** **Type**                                  **Documentation**
======== ========================================= =============================================================================================================================================================================================================
Ref      *LocalComponentListCo mponentRefBaseType* Ref is used to provide a complete set of reference fields. Derived reference types will restrict the RefType so that the content of the Ref element requires exactly what is needed for a complete reference.
======== ========================================= =============================================================================================================================================================================================================

**LocalComponentListComponentReferenceType: **\ LocalComponentListComponentReferenceType
provides a simple reference to any type of component in a specific
component list where the reference to the structure which defines it are
provided in another context.

Derivation:

| *ReferenceType* (restriction) 
|    |image142|\ *LocalComponentListComponentReferenceBaseType*\ (restriction) 
|          |image143|\ LocalComponentListComponentReferenceType

Content:

Ref

Element Documentation:

======== =================================== =============================================================================================================================================================================================================
**Name** **Type**                            **Documentation**
======== =================================== =============================================================================================================================================================================================================
Ref      LocalComponentListCo mponentRefType Ref is used to provide a complete set of reference fields. Derived reference types will restrict the RefType so that the content of the Ref element requires exactly what is needed for a complete reference.
======== =================================== =============================================================================================================================================================================================================

**LocalComponentReferenceBaseType: **\ LocalComponentReferenceBaseType
is an abstract base type which provides a simple reference to a
component where the references to the component list which contains it
and the structure which defines it are provided in another context.

Derivation:

| *ReferenceType* (restriction) 
|    |image144|\ *LocalComponentListComponentReferenceBaseType*\ (restriction) 
|          |image145|\ *LocalComponentReferenceBaseType*

Content:

Ref

Element Documentation:

======== ============================ =============================================================================================================================================================================================================
**Name** **Type**                     **Documentation**
======== ============================ =============================================================================================================================================================================================================
Ref      *LocalComponentRefBas eType* Ref is used to provide a complete set of reference fields. Derived reference types will restrict the RefType so that the content of the Ref element requires exactly what is needed for a complete reference.
======== ============================ =============================================================================================================================================================================================================

**LocalComponentReferenceType: **\ LocalComponentReferenceType provides
a simple reference to any type of component in a component list where
the references to the component list and the structure which defines
them are provided in another context.

Derivation:

| *ReferenceType* (restriction) 
|    |image146|\ *LocalComponentListComponentReferenceBaseType*\ (restriction) 
|          |image147|\ LocalComponentReferenceType

Content:

Ref

Element Documentation:

======== ====================== =============================================================================================================================================================================================================
**Name** **Type**               **Documentation**
======== ====================== =============================================================================================================================================================================================================
Ref      LocalComponentRefTyp e Ref is used to provide a complete set of reference fields. Derived reference types will restrict the RefType so that the content of the Ref element requires exactly what is needed for a complete reference.
======== ====================== =============================================================================================================================================================================================================

**StructureOrUsageReferenceType: **\ StructureOrUsageReferenceType is a
specific type of a reference for referencing either a structure or a
structure usage. It consists of a URN and/or a complete set of reference
fields; agency, id and version. If the complete set of reference fields
is used, it is required that a class and package be provided so that the
type of object referenced is clear.

Derivation:

| *ReferenceType* (restriction) 
|    |image148|\ *MaintainableReferenceBaseType* (restriction) 
|          |image149|\ StructureOrUsageReferenceType

Content:

( (Ref, URN?) \| URN)

Element Documentation:

======== ======================== =============================================================================================================================================================================================================
**Name** **Type**                 **Documentation**
======== ======================== =============================================================================================================================================================================================================
Ref      StructureOrUsageRefT ype Ref is used to provide a complete set of reference fields. Derived reference types will restrict the RefType so that the content of the Ref element requires exactly what is needed for a complete reference.
URN      xs:anyURI                URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
URN      xs:anyURI                URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
======== ======================== =============================================================================================================================================================================================================

**CategorisationReferenceType: **\ CategorisationReferenceType is a type
for referencing a categorisation object. It consists of a URN and/or a
complete set of reference fields.

Derivation:

| *ReferenceType* (restriction) 
|    |image150|\ *MaintainableReferenceBaseType* (restriction) 
|          |image151|\ CategorisationReferenceType

Content:

( (Ref, URN?) \| URN)

Element Documentation:

======== ====================== =============================================================================================================================================================================================================
**Name** **Type**               **Documentation**
======== ====================== =============================================================================================================================================================================================================
Ref      CategorisationRefTyp e Ref is used to provide a complete set of reference fields. Derived reference types will restrict the RefType so that the content of the Ref element requires exactly what is needed for a complete reference.
URN      xs:anyURI              URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
URN      xs:anyURI              URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
======== ====================== =============================================================================================================================================================================================================

**CategorisationRefType: **\ CategorisationRefType provides a reference
to a categorisation via a complete set of reference fields.

Derivation:

| *RefBaseType* (restriction) 
|    |image152|\ *MaintainableRefBaseType* (restriction) 
|          |image153|\ CategorisationRefType

Attributes:

agencyID, id, version?, local?, class?, package?

Content:

{Empty}

Attribute Documentation:

=============================== ============================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                        **Type**                      **Documentation**
=============================== ============================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
agencyID                        NestedNCNameIDType            The agencyID attribute identifies the maintenance agency for the object being referenced (agency-id in the URN structure). This is optional to allow for local references (where the other reference fields are inferred from another context), but all complete references will require this.
id                              IDType                        The id attribute identifies the object being referenced, and is therefore always required.
version (default: 1.0)          VersionType                   The version attribute identifies the version of the object being reference, if applicable. If this is available, a default value of 1.0 will always apply.
local (fixed: false)            xs:boolean                    The local attribute indicates whether this set of reference fields is meant for local referencing, in which case some of the reference fields will be implied from another context. Concrete instances of this class will always fix this value to either true or false, depending on their intended usage. If the value is fixed to true, then the complete set of reference fields will be required and a URN can be fully composed from the values.
class (fixed: Categorisation)   MaintainableTypeCode listType The class attribute indicates the class name of the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
package (fixed: categoryscheme) PackageTypeCodelistT ype      The package attribute indicates the package name for the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
=============================== ============================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================

**CategorySchemeReferenceType: **\ CategorySchemeReferenceType is a type
for referencing a category scheme object. It consists of a URN and/or a
complete set of reference fields.

Derivation:

| *ReferenceType* (restriction) 
|    |image154|\ *MaintainableReferenceBaseType* (restriction) 
|          |image155|\ *ItemSchemeReferenceBaseType* (restriction) 
|                |image156|\ CategorySchemeReferenceType

Content:

( (Ref, URN?) \| URN)

Element Documentation:

======== ====================== =============================================================================================================================================================================================================
**Name** **Type**               **Documentation**
======== ====================== =============================================================================================================================================================================================================
Ref      CategorySchemeRefTyp e Ref is used to provide a complete set of reference fields. Derived reference types will restrict the RefType so that the content of the Ref element requires exactly what is needed for a complete reference.
URN      xs:anyURI              URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
URN      xs:anyURI              URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
======== ====================== =============================================================================================================================================================================================================

**CategorySchemeRefType: **\ CategorySchemeRefType provides a reference
to a category scheme via a complete set of reference fields.

Derivation:

| *RefBaseType* (restriction) 
|    |image157|\ *MaintainableRefBaseType* (restriction) 
|          |image158|\ *ItemSchemeRefBaseType* (restriction) 
|                |image159|\ CategorySchemeRefType

Attributes:

agencyID, id, version?, local?, class?, package?

Content:

{Empty}

Attribute Documentation:

=============================== ================================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                        **Type**                           **Documentation**
=============================== ================================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
agencyID                        NestedNCNameIDType                 The agencyID attribute identifies the maintenance agency for the object being referenced (agency-id in the URN structure). This is optional to allow for local references (where the other reference fields are inferred from another context), but all complete references will require this.
id                              IDType                             The id attribute identifies the object being referenced, and is therefore always required.
version (default: 1.0)          VersionType                        The version attribute identifies the version of the object being reference, if applicable. If this is available, a default value of 1.0 will always apply.
local (fixed: false)            xs:boolean                         The local attribute indicates whether this set of reference fields is meant for local referencing, in which case some of the reference fields will be implied from another context. Concrete instances of this class will always fix this value to either true or false, depending on their intended usage. If the value is fixed to true, then the complete set of reference fields will be required and a URN can be fully composed from the values.
class (fixed: CategoryScheme)   ItemSchemeTypeCodeli stType        The class attribute indicates the class name of the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
package (fixed: categoryscheme) ItemSchemePackageTyp eCodelistType The package attribute indicates the package name for the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
=============================== ================================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================

**CategoryReferenceType: **\ CategoryReferenceType is a type for
referencing a category object. It consists of a URN and/or a complete
set of reference fields.

Derivation:

| *ReferenceType* (restriction) 
|    |image160|\ *ChildObjectReferenceType* (restriction) 
|          |image161|\ *ItemReferenceType* (restriction) 
|                |image162|\ CategoryReferenceType

Content:

( (Ref, URN?) \| URN)

Element Documentation:

======== =============== =============================================================================================================================================================================================================
**Name** **Type**        **Documentation**
======== =============== =============================================================================================================================================================================================================
Ref      CategoryRefType Ref is used to provide a complete set of reference fields. Derived reference types will restrict the RefType so that the content of the Ref element requires exactly what is needed for a complete reference.
URN      xs:anyURI       URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
URN      xs:anyURI       URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
======== =============== =============================================================================================================================================================================================================

**CategoryRefType: **\ CategoryRefType references a category from within
a category scheme. Reference fields are required for both the scheme and
the item.

Derivation:

| *RefBaseType* (restriction) 
|    |image163|\ *ChildObjectRefBaseType* (restriction) 
|          |image164|\ *ItemRefBaseType* (restriction) 
|                |image165|\ CategoryRefType

Attributes:

agencyID, maintainableParentID, maintainableParentVersion?, id, local?,
class?, package?

Content:

{Empty}

Attribute Documentation:

======================================== ================================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                                 **Type**                           **Documentation**
======================================== ================================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
agencyID                                 NestedNCNameIDType                 The agencyID attribute identifies the maintenance agency for the object being referenced (agency-id in the URN structure). This is optional to allow for local references (where the other reference fields are inferred from another context), but all complete references will require this.
maintainableParentID                     IDType                             The maintainableParentID references the category scheme in which the category being referenced is defined.
maintainableParentVersion (default: 1.0) VersionType                        The maintainableParentVersion attribute references the version of the category scheme in which the category being referenced is defined. If not supplied, a default value of 1.0 is assumed.
id                                       NestedIDType                       The id attribute identifies the object being referenced, and is therefore always required.
local (fixed: false)                     xs:boolean                         The local attribute indicates whether this set of reference fields is meant for local referencing, in which case some of the reference fields will be implied from another context. Concrete instances of this class will always fix this value to either true or false, depending on their intended usage. If the value is fixed to true, then the complete set of reference fields will be required and a URN can be fully composed from the values.
class (fixed: Category)                  ItemTypeCodelistType               The class attribute indicates the class name of the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
package (fixed: categoryscheme)          ItemSchemePackageTyp eCodelistType The package attribute indicates the package name for the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
======================================== ================================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================

**LocalCategoryReferenceType: **\ LocalCategoryReferenceType provides a
simple references to a category where the identification of the category
scheme which defines it is contained in another context.

Derivation:

| *ReferenceType* (restriction) 
|    |image166|\ *LocalItemReferenceType* (restriction) 
|          |image167|\ LocalCategoryReferenceType

Content:

Ref

Element Documentation:

======== ==================== =============================================================================================================================================================================================================
**Name** **Type**             **Documentation**
======== ==================== =============================================================================================================================================================================================================
Ref      LocalCategoryRefType Ref is used to provide a complete set of reference fields. Derived reference types will restrict the RefType so that the content of the Ref element requires exactly what is needed for a complete reference.
======== ==================== =============================================================================================================================================================================================================

**LocalCategoryRefType: **\ LocalCategoryRefType references a category
locally where the references to the category scheme which defines it is
provided elsewhere.

Derivation:

| *RefBaseType* (restriction) 
|    |image168|\ *LocalIdentifiableRefBaseType* (restriction) 
|          |image169|\ *LocalItemRefBaseType* (restriction) 
|                |image170|\ LocalCategoryRefType

Attributes:

id, local?, class?, package?

Content:

{Empty}

Attribute Documentation:

=============================== ================================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                        **Type**                           **Documentation**
=============================== ================================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
id                              NestedIDType                       The id attribute identifies the object being referenced, and is therefore always required.
local (fixed: true)             xs:boolean                         The local attribute indicates whether this set of reference fields is meant for local referencing, in which case some of the reference fields will be implied from another context. Concrete instances of this class will always fix this value to either true or false, depending on their intended usage. If the value is fixed to true, then the complete set of reference fields will be required and a URN can be fully composed from the values.
class (fixed: Category)         ItemTypeCodelistType               The class attribute indicates the class name of the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
package (fixed: categoryscheme) ItemSchemePackageTyp eCodelistType The package attribute indicates the package name for the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
=============================== ================================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================

**CodelistReferenceType: **\ CodelistReferenceType is a type for
referencing a codelist object. It consists of a URN and/or a complete
set of reference fields.

Derivation:

| *ReferenceType* (restriction) 
|    |image171|\ *MaintainableReferenceBaseType* (restriction) 
|          |image172|\ *ItemSchemeReferenceBaseType* (restriction) 
|                |image173|\ CodelistReferenceType

Content:

( (Ref, URN?) \| URN)

Element Documentation:

======== =============== =============================================================================================================================================================================================================
**Name** **Type**        **Documentation**
======== =============== =============================================================================================================================================================================================================
Ref      CodelistRefType Ref is used to provide a complete set of reference fields. Derived reference types will restrict the RefType so that the content of the Ref element requires exactly what is needed for a complete reference.
URN      xs:anyURI       URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
URN      xs:anyURI       URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
======== =============== =============================================================================================================================================================================================================

**CodelistRefType: **\ CodelistRefType provides a reference to a
codelist via a complete set of reference fields.

Derivation:

| *RefBaseType* (restriction) 
|    |image174|\ *MaintainableRefBaseType* (restriction) 
|          |image175|\ *ItemSchemeRefBaseType* (restriction) 
|                |image176|\ CodelistRefType

Attributes:

agencyID, id, version?, local?, class?, package?

Content:

{Empty}

Attribute Documentation:

========================= ================================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                  **Type**                           **Documentation**
========================= ================================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
agencyID                  NestedNCNameIDType                 The agencyID attribute identifies the maintenance agency for the object being referenced (agency-id in the URN structure). This is optional to allow for local references (where the other reference fields are inferred from another context), but all complete references will require this.
id                        IDType                             The id attribute identifies the object being referenced, and is therefore always required.
version (default: 1.0)    VersionType                        The version attribute identifies the version of the object being reference, if applicable. If this is available, a default value of 1.0 will always apply.
local (fixed: false)      xs:boolean                         The local attribute indicates whether this set of reference fields is meant for local referencing, in which case some of the reference fields will be implied from another context. Concrete instances of this class will always fix this value to either true or false, depending on their intended usage. If the value is fixed to true, then the complete set of reference fields will be required and a URN can be fully composed from the values.
class (fixed: Codelist)   ItemSchemeTypeCodeli stType        The class attribute indicates the class name of the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
package (fixed: codelist) ItemSchemePackageTyp eCodelistType The package attribute indicates the package name for the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
========================= ================================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================

**CodeReferenceType: **\ CodeReferenceType is a type for referencing a
code object. It consists of a URN and/or a complete set of reference
fields.

Derivation:

| *ReferenceType* (restriction) 
|    |image177|\ *ChildObjectReferenceType* (restriction) 
|          |image178|\ *ItemReferenceType* (restriction) 
|                |image179|\ CodeReferenceType

Content:

( (Ref, URN?) \| URN)

Element Documentation:

======== =========== =============================================================================================================================================================================================================
**Name** **Type**    **Documentation**
======== =========== =============================================================================================================================================================================================================
Ref      CodeRefType Ref is used to provide a complete set of reference fields. Derived reference types will restrict the RefType so that the content of the Ref element requires exactly what is needed for a complete reference.
URN      xs:anyURI   URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
URN      xs:anyURI   URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
======== =========== =============================================================================================================================================================================================================

**CodeRefType: **\ CodeRefType references a code from within a codelist.
Reference fields are required for both the scheme and the item.

Derivation:

| *RefBaseType* (restriction) 
|    |image180|\ *ChildObjectRefBaseType* (restriction) 
|          |image181|\ *ItemRefBaseType* (restriction) 
|                |image182|\ CodeRefType

Attributes:

agencyID, maintainableParentID, maintainableParentVersion?, id, local?,
class?, package?

Content:

{Empty}

Attribute Documentation:

======================================== ================================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                                 **Type**                           **Documentation**
======================================== ================================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
agencyID                                 NestedNCNameIDType                 The agencyID attribute identifies the maintenance agency for the object being referenced (agency-id in the URN structure). This is optional to allow for local references (where the other reference fields are inferred from another context), but all complete references will require this.
maintainableParentID                     IDType                             The maintainableParentID references the codelist in which the code being referenced is defined.
maintainableParentVersion (default: 1.0) VersionType                        The maintainableParentVersion attribute references the version of the codelist in which the code being referenced is defined. If not supplied, a default value of 1.0 is assumed.
id                                       IDType                             The id attribute identifies the object being referenced, and is therefore always required.
local (fixed: false)                     xs:boolean                         The local attribute indicates whether this set of reference fields is meant for local referencing, in which case some of the reference fields will be implied from another context. Concrete instances of this class will always fix this value to either true or false, depending on their intended usage. If the value is fixed to true, then the complete set of reference fields will be required and a URN can be fully composed from the values.
class (fixed: Code)                      ItemTypeCodelistType               The class attribute indicates the class name of the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
package (fixed: codelist)                ItemSchemePackageTyp eCodelistType The package attribute indicates the package name for the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
======================================== ================================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================

**LocalCodeReferenceType: **\ LocalCodeReferenceType provides a simple
references to a code where the identification of the codelist which
defines it is contained in another context.

Derivation:

| *ReferenceType* (restriction) 
|    |image183|\ *LocalItemReferenceType* (restriction) 
|          |image184|\ LocalCodeReferenceType

Content:

Ref

Element Documentation:

======== ================ =============================================================================================================================================================================================================
**Name** **Type**         **Documentation**
======== ================ =============================================================================================================================================================================================================
Ref      LocalCodeRefType Ref is used to provide a complete set of reference fields. Derived reference types will restrict the RefType so that the content of the Ref element requires exactly what is needed for a complete reference.
======== ================ =============================================================================================================================================================================================================

**LocalCodeRefType: **\ LocalCodeRefType references a code locally where
the references to the codelist which defines it is provided elsewhere.

Derivation:

| *RefBaseType* (restriction) 
|    |image185|\ *LocalIdentifiableRefBaseType* (restriction) 
|          |image186|\ *LocalItemRefBaseType* (restriction) 
|                |image187|\ LocalCodeRefType

Attributes:

id, local?, class?, package?

Content:

{Empty}

Attribute Documentation:

========================= ================================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                  **Type**                           **Documentation**
========================= ================================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
id                        IDType                             The id attribute identifies the object being referenced, and is therefore always required.
local (fixed: true)       xs:boolean                         The local attribute indicates whether this set of reference fields is meant for local referencing, in which case some of the reference fields will be implied from another context. Concrete instances of this class will always fix this value to either true or false, depending on their intended usage. If the value is fixed to true, then the complete set of reference fields will be required and a URN can be fully composed from the values.
class (fixed: Code)       ItemTypeCodelistType               The class attribute indicates the class name of the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
package (fixed: codelist) ItemSchemePackageTyp eCodelistType The package attribute indicates the package name for the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
========================= ================================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================

**AnyCodelistReferenceType: **\ AnyCodelistReferenceType is a specific
type of a reference for referencing either a codelist or a hierarchical
codelist usage. It consists of a URN and/or a complete set of reference
fields; agency, id and version. If the complete set of reference fields
is used, it is required that a class be provided so that the type of
object referenced is clear.

Derivation:

| *ReferenceType* (restriction) 
|    |image188|\ *MaintainableReferenceBaseType* (restriction) 
|          |image189|\ AnyCodelistReferenceType

Content:

( (Ref, URN?) \| URN)

Element Documentation:

======== ================== =============================================================================================================================================================================================================
**Name** **Type**           **Documentation**
======== ================== =============================================================================================================================================================================================================
Ref      AnyCodelistRefType Ref is used to provide a complete set of reference fields. Derived reference types will restrict the RefType so that the content of the Ref element requires exactly what is needed for a complete reference.
URN      xs:anyURI          URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
URN      xs:anyURI          URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
======== ================== =============================================================================================================================================================================================================

**AnyLocalCodeReferenceType: **\ AnyLocalCodeReferenceType provides a
simple references to any code or hierarchical code where the
identification of the codelist or hierarchical codelist which defines it
is contained in another context.

Derivation:

| *ReferenceType* (restriction) 
|    |image190|\ AnyLocalCodeReferenceType

Content:

( (Ref, URN?) \| URN)

Element Documentation:

======== =================== =============================================================================================================================================================================================================
**Name** **Type**            **Documentation**
======== =================== =============================================================================================================================================================================================================
Ref      AnyLocalCodeRefType Ref is used to provide a complete set of reference fields. Derived reference types will restrict the RefType so that the content of the Ref element requires exactly what is needed for a complete reference.
URN      xs:anyURI           URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
URN      xs:anyURI           URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
======== =================== =============================================================================================================================================================================================================

**ConceptSchemeReferenceType: **\ ConceptSchemeReferenceType is a type
for referencing a concept scheme object. It consists of a URN and/or a
complete set of reference fields.

Derivation:

| *ReferenceType* (restriction) 
|    |image191|\ *MaintainableReferenceBaseType* (restriction) 
|          |image192|\ *ItemSchemeReferenceBaseType* (restriction) 
|                |image193|\ ConceptSchemeReferenceType

Content:

( (Ref, URN?) \| URN)

Element Documentation:

======== ==================== =============================================================================================================================================================================================================
**Name** **Type**             **Documentation**
======== ==================== =============================================================================================================================================================================================================
Ref      ConceptSchemeRefType Ref is used to provide a complete set of reference fields. Derived reference types will restrict the RefType so that the content of the Ref element requires exactly what is needed for a complete reference.
URN      xs:anyURI            URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
URN      xs:anyURI            URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
======== ==================== =============================================================================================================================================================================================================

**ConceptSchemeRefType: **\ ConceptSchemeRefType provides a reference to
a concept scheme via a complete set of reference fields.

Derivation:

| *RefBaseType* (restriction) 
|    |image194|\ *MaintainableRefBaseType* (restriction) 
|          |image195|\ *ItemSchemeRefBaseType* (restriction) 
|                |image196|\ ConceptSchemeRefType

Attributes:

agencyID, id, version?, local?, class?, package?

Content:

{Empty}

Attribute Documentation:

============================== ================================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                       **Type**                           **Documentation**
============================== ================================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
agencyID                       NestedNCNameIDType                 The agencyID attribute identifies the maintenance agency for the object being referenced (agency-id in the URN structure). This is optional to allow for local references (where the other reference fields are inferred from another context), but all complete references will require this.
id                             IDType                             The id attribute identifies the object being referenced, and is therefore always required.
version (default: 1.0)         VersionType                        The version attribute identifies the version of the object being reference, if applicable. If this is available, a default value of 1.0 will always apply.
local (fixed: false)           xs:boolean                         The local attribute indicates whether this set of reference fields is meant for local referencing, in which case some of the reference fields will be implied from another context. Concrete instances of this class will always fix this value to either true or false, depending on their intended usage. If the value is fixed to true, then the complete set of reference fields will be required and a URN can be fully composed from the values.
class (fixed: ConceptScheme)   ItemSchemeTypeCodeli stType        The class attribute indicates the class name of the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
package (fixed: conceptscheme) ItemSchemePackageTyp eCodelistType The package attribute indicates the package name for the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
============================== ================================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================

**ConceptReferenceType: **\ ConceptReferenceType is a type for
referencing a concept object. It consists of a URN and/or a complete set
of reference fields.

Derivation:

| *ReferenceType* (restriction) 
|    |image197|\ *ChildObjectReferenceType* (restriction) 
|          |image198|\ *ItemReferenceType* (restriction) 
|                |image199|\ ConceptReferenceType

Content:

( (Ref, URN?) \| URN)

Element Documentation:

======== ============== =============================================================================================================================================================================================================
**Name** **Type**       **Documentation**
======== ============== =============================================================================================================================================================================================================
Ref      ConceptRefType Ref is used to provide a complete set of reference fields. Derived reference types will restrict the RefType so that the content of the Ref element requires exactly what is needed for a complete reference.
URN      xs:anyURI      URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
URN      xs:anyURI      URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
======== ============== =============================================================================================================================================================================================================

**ConceptRefType: **\ ConceptRefType references a concept from within a
concept scheme. Reference fields are required for both the scheme and
the item.

Derivation:

| *RefBaseType* (restriction) 
|    |image200|\ *ChildObjectRefBaseType* (restriction) 
|          |image201|\ *ItemRefBaseType* (restriction) 
|                |image202|\ ConceptRefType

Attributes:

agencyID, maintainableParentID, maintainableParentVersion?, id, local?,
class?, package?

Content:

{Empty}

Attribute Documentation:

======================================== ================================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                                 **Type**                           **Documentation**
======================================== ================================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
agencyID                                 NestedNCNameIDType                 The agencyID attribute identifies the maintenance agency for the object being referenced (agency-id in the URN structure). This is optional to allow for local references (where the other reference fields are inferred from another context), but all complete references will require this.
maintainableParentID                     IDType                             The maintainableParentID references the concept scheme in which the concept being referenced is defined.
maintainableParentVersion (default: 1.0) VersionType                        The maintainableParentVersion attribute references the version of the concept scheme in which the concept being referenced is defined. If not supplied, a default value of 1.0 is assumed.
id                                       IDType                             The id attribute identifies the object being referenced, and is therefore always required.
local (fixed: false)                     xs:boolean                         The local attribute indicates whether this set of reference fields is meant for local referencing, in which case some of the reference fields will be implied from another context. Concrete instances of this class will always fix this value to either true or false, depending on their intended usage. If the value is fixed to true, then the complete set of reference fields will be required and a URN can be fully composed from the values.
class (fixed: Concept)                   ItemTypeCodelistType               The class attribute indicates the class name of the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
package (fixed: conceptscheme)           ItemSchemePackageTyp eCodelistType The package attribute indicates the package name for the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
======================================== ================================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================

**LocalConceptReferenceType: **\ LocalConceptReferenceType provides a
simple references to a concept where the identification of the concept
scheme which defines it is contained in another context.

Derivation:

| *ReferenceType* (restriction) 
|    |image203|\ *LocalItemReferenceType* (restriction) 
|          |image204|\ LocalConceptReferenceType

Content:

Ref

Element Documentation:

======== =================== =============================================================================================================================================================================================================
**Name** **Type**            **Documentation**
======== =================== =============================================================================================================================================================================================================
Ref      LocalConceptRefType Ref is used to provide a complete set of reference fields. Derived reference types will restrict the RefType so that the content of the Ref element requires exactly what is needed for a complete reference.
======== =================== =============================================================================================================================================================================================================

**LocalConceptRefType: **\ LocalConceptRefType references a concept
locally where the references to the concept scheme which defines it is
provided elsewhere.

Derivation:

| *RefBaseType* (restriction) 
|    |image205|\ *LocalIdentifiableRefBaseType* (restriction) 
|          |image206|\ *LocalItemRefBaseType* (restriction) 
|                |image207|\ LocalConceptRefType

Attributes:

id, local?, class?, package?

Content:

{Empty}

Attribute Documentation:

============================== ================================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                       **Type**                           **Documentation**
============================== ================================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
id                             IDType                             The id attribute identifies the object being referenced, and is therefore always required.
local (fixed: true)            xs:boolean                         The local attribute indicates whether this set of reference fields is meant for local referencing, in which case some of the reference fields will be implied from another context. Concrete instances of this class will always fix this value to either true or false, depending on their intended usage. If the value is fixed to true, then the complete set of reference fields will be required and a URN can be fully composed from the values.
class (fixed: Concept)         ItemTypeCodelistType               The class attribute indicates the class name of the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
package (fixed: conceptscheme) ItemSchemePackageTyp eCodelistType The package attribute indicates the package name for the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
============================== ================================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================

**OrganisationSchemeReferenceBaseType: **\ OrganisationSchemeReferenceBaseType
is a type for referencing a organisation scheme object. It consists of a
URN and/or a complete set of reference fields.

Derivation:

| *ReferenceType* (restriction) 
|    |image208|\ *MaintainableReferenceBaseType* (restriction) 
|          |image209|\ *ItemSchemeReferenceBaseType* (restriction) 
|                |image210|\ *OrganisationSchemeReferenceBaseType*

Content:

( (Ref, URN?) \| URN)

Element Documentation:

======== ================================ =============================================================================================================================================================================================================
**Name** **Type**                         **Documentation**
======== ================================ =============================================================================================================================================================================================================
Ref      *OrganisationSchemeRe fBaseType* Ref is used to provide a complete set of reference fields. Derived reference types will restrict the RefType so that the content of the Ref element requires exactly what is needed for a complete reference.
URN      xs:anyURI                        URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
URN      xs:anyURI                        URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
======== ================================ =============================================================================================================================================================================================================

**OrganisationSchemeRefBaseType: **\ OrganisationSchemeRefBaseType
contains a set of reference fields for an organisation scheme.

Derivation:

| *RefBaseType* (restriction) 
|    |image211|\ *MaintainableRefBaseType* (restriction) 
|          |image212|\ *ItemSchemeRefBaseType* (restriction) 
|                |image213|\ *OrganisationSchemeRefBaseType*

Attributes:

agencyID, id, version?, local?, class?, package?

Content:

{Empty}

Attribute Documentation:

====================== =================================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**               **Type**                            **Documentation**
====================== =================================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
agencyID               NestedNCNameIDType                  The agencyID attribute identifies the maintenance agency for the object being referenced (agency-id in the URN structure). This is optional to allow for local references (where the other reference fields are inferred from another context), but all complete references will require this.
id                     IDType                              The id attribute identifies the object being referenced, and is therefore always required.
version (default: 1.0) VersionType                         The version attribute identifies the version of the object being reference, if applicable. If this is available, a default value of 1.0 will always apply.
local (fixed: false)   xs:boolean                          The local attribute indicates whether this set of reference fields is meant for local referencing, in which case some of the reference fields will be implied from another context. Concrete instances of this class will always fix this value to either true or false, depending on their intended usage. If the value is fixed to true, then the complete set of reference fields will be required and a URN can be fully composed from the values.
class                  OrganisationSchemeTy peCodelistType The class attribute indicates the class name of the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
package (fixed: base)  ItemSchemePackageTyp eCodelistType  The package attribute indicates the package name for the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
====================== =================================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================

**OrganisationSchemeReferenceType: **\ OrganisationSchemeReferenceType
references an organisation scheme regardless of the specific type. It
consists of a URN and/or a complete set of reference fields.

Derivation:

| *ReferenceType* (restriction) 
|    |image214|\ *MaintainableReferenceBaseType* (restriction) 
|          |image215|\ *ItemSchemeReferenceBaseType* (restriction) 
|                |image216|\ *OrganisationSchemeReferenceBaseType* (restriction) 
|                      |image217|\ OrganisationSchemeReferenceType

Content:

( (Ref, URN?) \| URN)

Element Documentation:

======== ========================== =============================================================================================================================================================================================================
**Name** **Type**                   **Documentation**
======== ========================== =============================================================================================================================================================================================================
Ref      OrganisationSchemeRe fType Ref is used to provide a complete set of reference fields. Derived reference types will restrict the RefType so that the content of the Ref element requires exactly what is needed for a complete reference.
URN      xs:anyURI                  URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
URN      xs:anyURI                  URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
======== ========================== =============================================================================================================================================================================================================

**OrganisationSchemeRefType: **\ OrganisationSchemeRefType provides a
reference to an organisation scheme via a complete set of reference
fields. It is required that the class (i.e. the type) of organisation
scheme being referenced be specified.

Derivation:

| *RefBaseType* (restriction) 
|    |image218|\ *MaintainableRefBaseType* (restriction) 
|          |image219|\ *ItemSchemeRefBaseType* (restriction) 
|                |image220|\ *OrganisationSchemeRefBaseType* (restriction) 
|                      |image221|\ OrganisationSchemeRefType

Attributes:

agencyID, id, version?, local?, class, package?

Content:

{Empty}

Attribute Documentation:

====================== =================================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**               **Type**                            **Documentation**
====================== =================================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
agencyID               NestedNCNameIDType                  The agencyID attribute identifies the maintenance agency for the object being referenced (agency-id in the URN structure). This is optional to allow for local references (where the other reference fields are inferred from another context), but all complete references will require this.
id                     IDType                              The id attribute identifies the object being referenced, and is therefore always required.
version (default: 1.0) VersionType                         The version attribute identifies the version of the object being reference, if applicable. If this is available, a default value of 1.0 will always apply.
local (fixed: false)   xs:boolean                          The local attribute indicates whether this set of reference fields is meant for local referencing, in which case some of the reference fields will be implied from another context. Concrete instances of this class will always fix this value to either true or false, depending on their intended usage. If the value is fixed to true, then the complete set of reference fields will be required and a URN can be fully composed from the values.
class                  OrganisationSchemeTy peCodelistType The class attribute indicates the class name of the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
package (fixed: base)  ItemSchemePackageTyp eCodelistType  The package attribute indicates the package name for the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
====================== =================================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================

**OrganisationReferenceBaseType: **\ OrganisationReferenceBaseType is a
type for referencing any organisation object, regardless of its type. It
consists of a URN and/or a complete set of reference fields.

Derivation:

| *ReferenceType* (restriction) 
|    |image222|\ *ChildObjectReferenceType* (restriction) 
|          |image223|\ *ItemReferenceType* (restriction) 
|                |image224|\ *OrganisationReferenceBaseType*

Content:

( (Ref, URN?) \| URN)

Element Documentation:

======== ========================== =============================================================================================================================================================================================================
**Name** **Type**                   **Documentation**
======== ========================== =============================================================================================================================================================================================================
Ref      *OrganisationRefBaseT ype* Ref is used to provide a complete set of reference fields. Derived reference types will restrict the RefType so that the content of the Ref element requires exactly what is needed for a complete reference.
URN      xs:anyURI                  URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
URN      xs:anyURI                  URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
======== ========================== =============================================================================================================================================================================================================

**OrganisationRefBaseType: **\ OrganisationRefBaseType is an abstract
base type which references an organisation from within a organisation
scheme. Reference fields are required for both the scheme and the
organisation.

Derivation:

| *RefBaseType* (restriction) 
|    |image225|\ *ChildObjectRefBaseType* (restriction) 
|          |image226|\ *ItemRefBaseType* (restriction) 
|                |image227|\ *OrganisationRefBaseType*

Attributes:

agencyID, maintainableParentID, maintainableParentVersion?, id, local?,
class?, package?

Content:

{Empty}

Attribute Documentation:

======================================== ================================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                                 **Type**                           **Documentation**
======================================== ================================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
agencyID                                 NestedNCNameIDType                 The agencyID attribute identifies the maintenance agency for the object being referenced (agency-id in the URN structure). This is optional to allow for local references (where the other reference fields are inferred from another context), but all complete references will require this.
maintainableParentID                     IDType                             The maintainableParentID references the organisation scheme in which the organisation being referenced is defined.
maintainableParentVersion (default: 1.0) VersionType                        The maintainableParentVersion attribute references the version of the organisation scheme in which the organisation being referenced is defined. If not supplied, a default value of 1.0 is assumed.
id                                       IDType                             The id attribute identifies the object being referenced, and is therefore always required.
local (fixed: false)                     xs:boolean                         The local attribute indicates whether this set of reference fields is meant for local referencing, in which case some of the reference fields will be implied from another context. Concrete instances of this class will always fix this value to either true or false, depending on their intended usage. If the value is fixed to true, then the complete set of reference fields will be required and a URN can be fully composed from the values.
class                                    OrganisationTypeCode listType      The class attribute indicates the class name of the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
package (fixed: base)                    ItemSchemePackageTyp eCodelistType The package attribute indicates the package name for the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
======================================== ================================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================

**OrganisationReferenceType: **\ OrganisationReferenceType references an
organisation regardless of the specific type. It consists of a URN
and/or a complete set of reference fields.

Derivation:

| *ReferenceType* (restriction) 
|    |image228|\ *ChildObjectReferenceType* (restriction) 
|          |image229|\ *ItemReferenceType* (restriction) 
|                |image230|\ *OrganisationReferenceBaseType* (restriction) 
|                      |image231|\ OrganisationReferenceType

Content:

( (Ref, URN?) \| URN)

Element Documentation:

======== ========================== =============================================================================================================================================================================================================
**Name** **Type**                   **Documentation**
======== ========================== =============================================================================================================================================================================================================
Ref      *OrganisationRefBaseT ype* Ref is used to provide a complete set of reference fields. Derived reference types will restrict the RefType so that the content of the Ref element requires exactly what is needed for a complete reference.
URN      xs:anyURI                  URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
URN      xs:anyURI                  URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
======== ========================== =============================================================================================================================================================================================================

**OrganisationRefType: **\ OrganisationRefType provides a reference to
any organisation via a complete set of reference fields. It is required
that the class (i.e. the type) of organisation being referenced be
specified.

Derivation:

| *RefBaseType* (restriction) 
|    |image232|\ *ChildObjectRefBaseType* (restriction) 
|          |image233|\ *ItemRefBaseType* (restriction) 
|                |image234|\ *OrganisationRefBaseType* (restriction) 
|                      |image235|\ OrganisationRefType

Attributes:

agencyID, maintainableParentID, maintainableParentVersion?, id, local?,
class, package?

Content:

{Empty}

Attribute Documentation:

======================================== ================================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                                 **Type**                           **Documentation**
======================================== ================================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
agencyID                                 NestedNCNameIDType                 The agencyID attribute identifies the maintenance agency for the object being referenced (agency-id in the URN structure). This is optional to allow for local references (where the other reference fields are inferred from another context), but all complete references will require this.
maintainableParentID                     IDType                             The maintainableParentID references the organisation scheme in which the organisation being referenced is defined.
maintainableParentVersion (default: 1.0) VersionType                        The maintainableParentVersion attribute references the version of the organisation scheme in which the organisation being referenced is defined. If not supplied, a default value of 1.0 is assumed.
id                                       IDType                             The id attribute identifies the object being referenced, and is therefore always required.
local (fixed: false)                     xs:boolean                         The local attribute indicates whether this set of reference fields is meant for local referencing, in which case some of the reference fields will be implied from another context. Concrete instances of this class will always fix this value to either true or false, depending on their intended usage. If the value is fixed to true, then the complete set of reference fields will be required and a URN can be fully composed from the values.
class                                    OrganisationTypeCode listType      The class attribute indicates the class name of the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
package (fixed: base)                    ItemSchemePackageTyp eCodelistType The package attribute indicates the package name for the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
======================================== ================================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================

**LocalOrganisationReferenceBaseType: **\ LocalOrganisationReferenceBaseType
is an abstract base type which provides a simple references to an
organisation, regardless of type, where the identification of the
organisation scheme which defines it is contained in another context.

Derivation:

| *ReferenceType* (restriction) 
|    |image236|\ *LocalItemReferenceType* (restriction) 
|          |image237|\ *LocalOrganisationReferenceBaseType*

Content:

Ref

Element Documentation:

======== =============================== =============================================================================================================================================================================================================
**Name** **Type**                        **Documentation**
======== =============================== =============================================================================================================================================================================================================
Ref      *LocalOrganisationRef BaseType* Ref is used to provide a complete set of reference fields. Derived reference types will restrict the RefType so that the content of the Ref element requires exactly what is needed for a complete reference.
======== =============================== =============================================================================================================================================================================================================

**LocalOrganisationRefBaseType: **\ LocalOrganisationRefBaseType is an
abstract base type that references an organisation locally where the
reference to the organisation scheme which defines it is provided
elsewhere.

Derivation:

| *RefBaseType* (restriction) 
|    |image238|\ *LocalIdentifiableRefBaseType* (restriction) 
|          |image239|\ *LocalItemRefBaseType* (restriction) 
|                |image240|\ *LocalOrganisationRefBaseType*

Attributes:

id, local?, class?, package?

Content:

{Empty}

Attribute Documentation:

===================== ================================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**              **Type**                           **Documentation**
===================== ================================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
id                    IDType                             The id attribute identifies the object being referenced, and is therefore always required.
local (fixed: true)   xs:boolean                         The local attribute indicates whether this set of reference fields is meant for local referencing, in which case some of the reference fields will be implied from another context. Concrete instances of this class will always fix this value to either true or false, depending on their intended usage. If the value is fixed to true, then the complete set of reference fields will be required and a URN can be fully composed from the values.
class                 OrganisationTypeCode listType      The class attribute indicates the class name of the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
package (fixed: base) ItemSchemePackageTyp eCodelistType The package attribute indicates the package name for the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
===================== ================================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================

**LocalOrganisationReferenceType: **\ LocalOrganisationReferenceType
provides a simple reference to an organisation, regardless of type,
where the identification of the organisation scheme which defines it is
contained in another context.

Derivation:

| *ReferenceType* (restriction) 
|    |image241|\ *LocalItemReferenceType* (restriction) 
|          |image242|\ *LocalOrganisationReferenceBaseType* (restriction) 
|                |image243|\ LocalOrganisationReferenceType

Content:

Ref

Element Documentation:

======== ========================= =============================================================================================================================================================================================================
**Name** **Type**                  **Documentation**
======== ========================= =============================================================================================================================================================================================================
Ref      LocalOrganisationRef Type Ref is used to provide a complete set of reference fields. Derived reference types will restrict the RefType so that the content of the Ref element requires exactly what is needed for a complete reference.
======== ========================= =============================================================================================================================================================================================================

**LocalOrganisationRefType: **\ LocalOrganisationRefType references an
organisation locally where the reference to the organisation scheme
which defines it is provided elsewhere. The reference requires that the
class (i.e. the type) or the organisation being reference be provided.

Derivation:

| *RefBaseType* (restriction) 
|    |image244|\ *LocalIdentifiableRefBaseType* (restriction) 
|          |image245|\ *LocalItemRefBaseType* (restriction) 
|                |image246|\ *LocalOrganisationRefBaseType* (restriction) 
|                      |image247|\ LocalOrganisationRefType

Attributes:

id, local?, class?, package?

Content:

{Empty}

Attribute Documentation:

===================== ================================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**              **Type**                           **Documentation**
===================== ================================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
id                    IDType                             The id attribute identifies the object being referenced, and is therefore always required.
local (fixed: true)   xs:boolean                         The local attribute indicates whether this set of reference fields is meant for local referencing, in which case some of the reference fields will be implied from another context. Concrete instances of this class will always fix this value to either true or false, depending on their intended usage. If the value is fixed to true, then the complete set of reference fields will be required and a URN can be fully composed from the values.
class                 OrganisationTypeCode listType      The class attribute indicates the class name of the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
package (fixed: base) ItemSchemePackageTyp eCodelistType The package attribute indicates the package name for the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
===================== ================================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================

**OrganisationUnitSchemeReferenceType: **\ OrganisationUnitSchemeReferenceType
is a type for referencing an organisation unit scheme object. It
consists of a URN and/or a complete set of reference fields.

Derivation:

| *ReferenceType* (restriction) 
|    |image248|\ *MaintainableReferenceBaseType* (restriction) 
|          |image249|\ *ItemSchemeReferenceBaseType* (restriction) 
|                |image250|\ *OrganisationSchemeReferenceBaseType* (restriction) 
|                      |image251|\ OrganisationUnitSchemeReferenceType

Content:

( (Ref, URN?) \| URN)

Element Documentation:

======== ============================== =============================================================================================================================================================================================================
**Name** **Type**                       **Documentation**
======== ============================== =============================================================================================================================================================================================================
Ref      OrganisationUnitSche meRefType Ref is used to provide a complete set of reference fields. Derived reference types will restrict the RefType so that the content of the Ref element requires exactly what is needed for a complete reference.
URN      xs:anyURI                      URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
URN      xs:anyURI                      URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
======== ============================== =============================================================================================================================================================================================================

**OrganisationUnitSchemeRefType: **\ OrganisationUnitSchemeRefType
contains a set of reference fields for an organisation unit scheme.

Derivation:

| *RefBaseType* (restriction) 
|    |image252|\ *MaintainableRefBaseType* (restriction) 
|          |image253|\ *ItemSchemeRefBaseType* (restriction) 
|                |image254|\ *OrganisationSchemeRefBaseType* (restriction) 
|                      |image255|\ OrganisationUnitSchemeRefType

Attributes:

agencyID, id, version?, local?, class?, package?

Content:

{Empty}

Attribute Documentation:

===================================== =================================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                              **Type**                            **Documentation**
===================================== =================================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
agencyID                              NestedNCNameIDType                  The agencyID attribute identifies the maintenance agency for the object being referenced (agency-id in the URN structure). This is optional to allow for local references (where the other reference fields are inferred from another context), but all complete references will require this.
id                                    IDType                              The id attribute identifies the object being referenced, and is therefore always required.
version (default: 1.0)                VersionType                         The version attribute identifies the version of the object being reference, if applicable. If this is available, a default value of 1.0 will always apply.
local (fixed: false)                  xs:boolean                          The local attribute indicates whether this set of reference fields is meant for local referencing, in which case some of the reference fields will be implied from another context. Concrete instances of this class will always fix this value to either true or false, depending on their intended usage. If the value is fixed to true, then the complete set of reference fields will be required and a URN can be fully composed from the values.
class (fixed: OrganisationUnitScheme) OrganisationSchemeTy peCodelistType The class attribute indicates the class name of the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
package (fixed: base)                 ItemSchemePackageTyp eCodelistType  The package attribute indicates the package name for the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
===================================== =================================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================

**OrganisationUnitReferenceType: **\ OrganisationUnitReferenceType is a
type for referencing an organisation unit. It consists of a URN and/or a
complete set of reference fields.

Derivation:

| *ReferenceType* (restriction) 
|    |image256|\ *ChildObjectReferenceType* (restriction) 
|          |image257|\ *ItemReferenceType* (restriction) 
|                |image258|\ *OrganisationReferenceBaseType* (restriction) 
|                      |image259|\ OrganisationUnitReferenceType

Content:

( (Ref, URN?) \| URN)

Element Documentation:

======== ======================== =============================================================================================================================================================================================================
**Name** **Type**                 **Documentation**
======== ======================== =============================================================================================================================================================================================================
Ref      OrganisationUnitRefT ype Ref is used to provide a complete set of reference fields. Derived reference types will restrict the RefType so that the content of the Ref element requires exactly what is needed for a complete reference.
URN      xs:anyURI                URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
URN      xs:anyURI                URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
======== ======================== =============================================================================================================================================================================================================

**OrganisationUnitRefType: **\ OrganisationUnitRefType contains a set of
reference fields for referencing an organisation unit within an
organisation unit scheme.

Derivation:

| *RefBaseType* (restriction) 
|    |image260|\ *ChildObjectRefBaseType* (restriction) 
|          |image261|\ *ItemRefBaseType* (restriction) 
|                |image262|\ *OrganisationRefBaseType* (restriction) 
|                      |image263|\ OrganisationUnitRefType

Attributes:

agencyID, maintainableParentID, maintainableParentVersion?, id, local?,
class?, package?

Content:

{Empty}

Attribute Documentation:

======================================== ================================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                                 **Type**                           **Documentation**
======================================== ================================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
agencyID                                 NestedNCNameIDType                 The agencyID attribute identifies the maintenance agency for the object being referenced (agency-id in the URN structure). This is optional to allow for local references (where the other reference fields are inferred from another context), but all complete references will require this.
maintainableParentID                     IDType                             The maintainableParentID references the organisation scheme in which the organisation being referenced is defined.
maintainableParentVersion (default: 1.0) VersionType                        The maintainableParentVersion attribute references the version of the organisation scheme in which the organisation being referenced is defined. If not supplied, a default value of 1.0 is assumed.
id                                       IDType                             The id attribute identifies the object being referenced, and is therefore always required.
local (fixed: false)                     xs:boolean                         The local attribute indicates whether this set of reference fields is meant for local referencing, in which case some of the reference fields will be implied from another context. Concrete instances of this class will always fix this value to either true or false, depending on their intended usage. If the value is fixed to true, then the complete set of reference fields will be required and a URN can be fully composed from the values.
class (fixed: OrganisationUnit)          OrganisationTypeCode listType      The class attribute indicates the class name of the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
package (fixed: base)                    ItemSchemePackageTyp eCodelistType The package attribute indicates the package name for the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
======================================== ================================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================

**LocalOrganisationUnitReferenceType: **\ LocalOrganisationUnitReferenceType
provides a simple reference to an organisation unit, where the reference
to the organisation unit scheme which defines it is provided in another
context.

Derivation:

| *ReferenceType* (restriction) 
|    |image264|\ *LocalItemReferenceType* (restriction) 
|          |image265|\ *LocalOrganisationReferenceBaseType* (restriction) 
|                |image266|\ LocalOrganisationUnitReferenceType

Content:

Ref

Element Documentation:

======== ============================= =============================================================================================================================================================================================================
**Name** **Type**                      **Documentation**
======== ============================= =============================================================================================================================================================================================================
Ref      LocalOrganisationUni tRefType Ref is used to provide a complete set of reference fields. Derived reference types will restrict the RefType so that the content of the Ref element requires exactly what is needed for a complete reference.
======== ============================= =============================================================================================================================================================================================================

**LocalOrganisationUnitRefType: **\ LocalOrganisationUnitRefType
references an organisation unit locally where the reference to the
organisation unit scheme which defines it is provided elsewhere.

Derivation:

| *RefBaseType* (restriction) 
|    |image267|\ *LocalIdentifiableRefBaseType* (restriction) 
|          |image268|\ *LocalItemRefBaseType* (restriction) 
|                |image269|\ *LocalOrganisationRefBaseType* (restriction) 
|                      |image270|\ LocalOrganisationUnitRefType

Attributes:

id, local?, class?, package?

Content:

{Empty}

Attribute Documentation:

=============================== ================================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                        **Type**                           **Documentation**
=============================== ================================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
id                              IDType                             The id attribute identifies the object being referenced, and is therefore always required.
local (fixed: true)             xs:boolean                         The local attribute indicates whether this set of reference fields is meant for local referencing, in which case some of the reference fields will be implied from another context. Concrete instances of this class will always fix this value to either true or false, depending on their intended usage. If the value is fixed to true, then the complete set of reference fields will be required and a URN can be fully composed from the values.
class (fixed: OrganisationUnit) OrganisationTypeCode listType      The class attribute indicates the class name of the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
package (fixed: base)           ItemSchemePackageTyp eCodelistType The package attribute indicates the package name for the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
=============================== ================================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================

**AgencySchemeReferenceType: **\ AgencySchemeReferenceType is a type for
referencing an agency scheme object. It consists of a URN and/or a
complete set of reference fields.

Derivation:

| *ReferenceType* (restriction) 
|    |image271|\ *MaintainableReferenceBaseType* (restriction) 
|          |image272|\ *ItemSchemeReferenceBaseType* (restriction) 
|                |image273|\ *OrganisationSchemeReferenceBaseType* (restriction) 
|                      |image274|\ AgencySchemeReferenceType

Content:

( (Ref, URN?) \| URN)

Element Documentation:

======== =================== =============================================================================================================================================================================================================
**Name** **Type**            **Documentation**
======== =================== =============================================================================================================================================================================================================
Ref      AgencySchemeRefType Ref is used to provide a complete set of reference fields. Derived reference types will restrict the RefType so that the content of the Ref element requires exactly what is needed for a complete reference.
URN      xs:anyURI           URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
URN      xs:anyURI           URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
======== =================== =============================================================================================================================================================================================================

**AgencySchemeRefType: **\ AgencySchemeRefType contains a set of
reference fields for an agency scheme.

Derivation:

| *RefBaseType* (restriction) 
|    |image275|\ *MaintainableRefBaseType* (restriction) 
|          |image276|\ *ItemSchemeRefBaseType* (restriction) 
|                |image277|\ *OrganisationSchemeRefBaseType* (restriction) 
|                      |image278|\ AgencySchemeRefType

Attributes:

agencyID, id, version?, local?, class?, package?

Content:

{Empty}

Attribute Documentation:

=========================== =================================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                    **Type**                            **Documentation**
=========================== =================================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
agencyID                    NestedNCNameIDType                  The agencyID attribute identifies the maintenance agency for the object being referenced (agency-id in the URN structure). This is optional to allow for local references (where the other reference fields are inferred from another context), but all complete references will require this.
id                          IDType                              The id attribute identifies the object being referenced, and is therefore always required.
version (default: 1.0)      VersionType                         The version attribute identifies the version of the object being reference, if applicable. If this is available, a default value of 1.0 will always apply.
local (fixed: false)        xs:boolean                          The local attribute indicates whether this set of reference fields is meant for local referencing, in which case some of the reference fields will be implied from another context. Concrete instances of this class will always fix this value to either true or false, depending on their intended usage. If the value is fixed to true, then the complete set of reference fields will be required and a URN can be fully composed from the values.
class (fixed: AgencyScheme) OrganisationSchemeTy peCodelistType The class attribute indicates the class name of the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
package (fixed: base)       ItemSchemePackageTyp eCodelistType  The package attribute indicates the package name for the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
=========================== =================================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================

**AgencyReferenceType: **\ AgencyReferenceType is a type for referencing
an agency. It consists of a URN and/or a complete set of reference
fields.

Derivation:

| *ReferenceType* (restriction) 
|    |image279|\ *ChildObjectReferenceType* (restriction) 
|          |image280|\ *ItemReferenceType* (restriction) 
|                |image281|\ *OrganisationReferenceBaseType* (restriction) 
|                      |image282|\ AgencyReferenceType

Content:

( (Ref, URN?) \| URN)

Element Documentation:

======== ============= =============================================================================================================================================================================================================
**Name** **Type**      **Documentation**
======== ============= =============================================================================================================================================================================================================
Ref      AgencyRefType Ref is used to provide a complete set of reference fields. Derived reference types will restrict the RefType so that the content of the Ref element requires exactly what is needed for a complete reference.
URN      xs:anyURI     URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
URN      xs:anyURI     URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
======== ============= =============================================================================================================================================================================================================

**AgencyRefType: **\ AgencyRefType contains a set of reference fields
for referencing an agency within an agency scheme.

Derivation:

| *RefBaseType* (restriction) 
|    |image283|\ *ChildObjectRefBaseType* (restriction) 
|          |image284|\ *ItemRefBaseType* (restriction) 
|                |image285|\ *OrganisationRefBaseType* (restriction) 
|                      |image286|\ AgencyRefType

Attributes:

agencyID, maintainableParentID, maintainableParentVersion?, id, local?,
class?, package?

Content:

{Empty}

Attribute Documentation:

======================================== ================================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                                 **Type**                           **Documentation**
======================================== ================================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
agencyID                                 NestedNCNameIDType                 The agencyID attribute identifies the maintenance agency for the object being referenced (agency-id in the URN structure). This is optional to allow for local references (where the other reference fields are inferred from another context), but all complete references will require this.
maintainableParentID                     IDType                             The maintainableParentID references the organisation scheme in which the organisation being referenced is defined.
maintainableParentVersion (default: 1.0) VersionType                        The maintainableParentVersion attribute references the version of the organisation scheme in which the organisation being referenced is defined. If not supplied, a default value of 1.0 is assumed.
id                                       IDType                             The id attribute identifies the object being referenced, and is therefore always required.
local (fixed: false)                     xs:boolean                         The local attribute indicates whether this set of reference fields is meant for local referencing, in which case some of the reference fields will be implied from another context. Concrete instances of this class will always fix this value to either true or false, depending on their intended usage. If the value is fixed to true, then the complete set of reference fields will be required and a URN can be fully composed from the values.
class (fixed: Agency)                    OrganisationTypeCode listType      The class attribute indicates the class name of the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
package (fixed: base)                    ItemSchemePackageTyp eCodelistType The package attribute indicates the package name for the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
======================================== ================================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================

**LocalAgencyReferenceType: **\ LocalAgencyReferenceType provides a
simple reference to an agency, where the reference to the agency scheme
which defines it is provided in another context.

Derivation:

| *ReferenceType* (restriction) 
|    |image287|\ *LocalItemReferenceType* (restriction) 
|          |image288|\ *LocalOrganisationReferenceBaseType* (restriction) 
|                |image289|\ LocalAgencyReferenceType

Content:

Ref

Element Documentation:

======== ================== =============================================================================================================================================================================================================
**Name** **Type**           **Documentation**
======== ================== =============================================================================================================================================================================================================
Ref      LocalAgencyRefType Ref is used to provide a complete set of reference fields. Derived reference types will restrict the RefType so that the content of the Ref element requires exactly what is needed for a complete reference.
======== ================== =============================================================================================================================================================================================================

**LocalAgencyRefType: **\ LocalAgencyRefType references an agency
locally where the reference to the agency scheme which defines it is
provided elsewhere.

Derivation:

| *RefBaseType* (restriction) 
|    |image290|\ *LocalIdentifiableRefBaseType* (restriction) 
|          |image291|\ *LocalItemRefBaseType* (restriction) 
|                |image292|\ *LocalOrganisationRefBaseType* (restriction) 
|                      |image293|\ LocalAgencyRefType

Attributes:

id, local?, class?, package?

Content:

{Empty}

Attribute Documentation:

===================== ================================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**              **Type**                           **Documentation**
===================== ================================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
id                    IDType                             The id attribute identifies the object being referenced, and is therefore always required.
local (fixed: true)   xs:boolean                         The local attribute indicates whether this set of reference fields is meant for local referencing, in which case some of the reference fields will be implied from another context. Concrete instances of this class will always fix this value to either true or false, depending on their intended usage. If the value is fixed to true, then the complete set of reference fields will be required and a URN can be fully composed from the values.
class (fixed: Agency) OrganisationTypeCode listType      The class attribute indicates the class name of the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
package (fixed: base) ItemSchemePackageTyp eCodelistType The package attribute indicates the package name for the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
===================== ================================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================

**DataConsumerSchemeReferenceType: **\ DataConsumerSchemeReferenceType
is a type for referencing a data consumer scheme object. It consists of
a URN and/or a complete set of reference fields.

Derivation:

| *ReferenceType* (restriction) 
|    |image294|\ *MaintainableReferenceBaseType* (restriction) 
|          |image295|\ *ItemSchemeReferenceBaseType* (restriction) 
|                |image296|\ *OrganisationSchemeReferenceBaseType* (restriction) 
|                      |image297|\ DataConsumerSchemeReferenceType

Content:

( (Ref, URN?) \| URN)

Element Documentation:

======== ========================== =============================================================================================================================================================================================================
**Name** **Type**                   **Documentation**
======== ========================== =============================================================================================================================================================================================================
Ref      DataConsumerSchemeRe fType Ref is used to provide a complete set of reference fields. Derived reference types will restrict the RefType so that the content of the Ref element requires exactly what is needed for a complete reference.
URN      xs:anyURI                  URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
URN      xs:anyURI                  URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
======== ========================== =============================================================================================================================================================================================================

**DataConsumerSchemeRefType: **\ DataConsumerSchemeRefType contains a
set of reference fields for a data consumer scheme.

Derivation:

| *RefBaseType* (restriction) 
|    |image298|\ *MaintainableRefBaseType* (restriction) 
|          |image299|\ *ItemSchemeRefBaseType* (restriction) 
|                |image300|\ *OrganisationSchemeRefBaseType* (restriction) 
|                      |image301|\ DataConsumerSchemeRefType

Attributes:

agencyID, id, version?, local?, class?, package?

Content:

{Empty}

Attribute Documentation:

================================= =================================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                          **Type**                            **Documentation**
================================= =================================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
agencyID                          NestedNCNameIDType                  The agencyID attribute identifies the maintenance agency for the object being referenced (agency-id in the URN structure). This is optional to allow for local references (where the other reference fields are inferred from another context), but all complete references will require this.
id                                IDType                              The id attribute identifies the object being referenced, and is therefore always required.
version (default: 1.0)            VersionType                         The version attribute identifies the version of the object being reference, if applicable. If this is available, a default value of 1.0 will always apply.
local (fixed: false)              xs:boolean                          The local attribute indicates whether this set of reference fields is meant for local referencing, in which case some of the reference fields will be implied from another context. Concrete instances of this class will always fix this value to either true or false, depending on their intended usage. If the value is fixed to true, then the complete set of reference fields will be required and a URN can be fully composed from the values.
class (fixed: DataConsumerScheme) OrganisationSchemeTy peCodelistType The class attribute indicates the class name of the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
package (fixed: base)             ItemSchemePackageTyp eCodelistType  The package attribute indicates the package name for the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
================================= =================================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================

**DataConsumerReferenceType: **\ DataConsumerReferenceType is a type for
referencing a data consumer. It consists of a URN and/or a complete set
of reference fields.

Derivation:

| *ReferenceType* (restriction) 
|    |image302|\ *ChildObjectReferenceType* (restriction) 
|          |image303|\ *ItemReferenceType* (restriction) 
|                |image304|\ *OrganisationReferenceBaseType* (restriction) 
|                      |image305|\ DataConsumerReferenceType

Content:

( (Ref, URN?) \| URN)

Element Documentation:

======== =================== =============================================================================================================================================================================================================
**Name** **Type**            **Documentation**
======== =================== =============================================================================================================================================================================================================
Ref      DataConsumerRefType Ref is used to provide a complete set of reference fields. Derived reference types will restrict the RefType so that the content of the Ref element requires exactly what is needed for a complete reference.
URN      xs:anyURI           URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
URN      xs:anyURI           URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
======== =================== =============================================================================================================================================================================================================

**DataConsumerRefType: **\ DataConsumerRefType contains a set of
reference fields for referencing a data consumer within a data consumer
scheme.

Derivation:

| *RefBaseType* (restriction) 
|    |image306|\ *ChildObjectRefBaseType* (restriction) 
|          |image307|\ *ItemRefBaseType* (restriction) 
|                |image308|\ *OrganisationRefBaseType* (restriction) 
|                      |image309|\ DataConsumerRefType

Attributes:

agencyID, maintainableParentID, maintainableParentVersion?, id, local?,
class?, package?

Content:

{Empty}

Attribute Documentation:

======================================== ================================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                                 **Type**                           **Documentation**
======================================== ================================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
agencyID                                 NestedNCNameIDType                 The agencyID attribute identifies the maintenance agency for the object being referenced (agency-id in the URN structure). This is optional to allow for local references (where the other reference fields are inferred from another context), but all complete references will require this.
maintainableParentID                     IDType                             The maintainableParentID references the organisation scheme in which the organisation being referenced is defined.
maintainableParentVersion (default: 1.0) VersionType                        The maintainableParentVersion attribute references the version of the organisation scheme in which the organisation being referenced is defined. If not supplied, a default value of 1.0 is assumed.
id                                       IDType                             The id attribute identifies the object being referenced, and is therefore always required.
local (fixed: false)                     xs:boolean                         The local attribute indicates whether this set of reference fields is meant for local referencing, in which case some of the reference fields will be implied from another context. Concrete instances of this class will always fix this value to either true or false, depending on their intended usage. If the value is fixed to true, then the complete set of reference fields will be required and a URN can be fully composed from the values.
class (fixed: DataConsumer)              OrganisationTypeCode listType      The class attribute indicates the class name of the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
package (fixed: base)                    ItemSchemePackageTyp eCodelistType The package attribute indicates the package name for the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
======================================== ================================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================

**LocalDataConsumerReferenceType: **\ LocalDataConsumerReferenceType
provides a simple reference to a data consumer, where the reference to
the data consumer scheme which defines it is provided in another
context.

Derivation:

| *ReferenceType* (restriction) 
|    |image310|\ *LocalItemReferenceType* (restriction) 
|          |image311|\ *LocalOrganisationReferenceBaseType* (restriction) 
|                |image312|\ LocalDataConsumerReferenceType

Content:

Ref

Element Documentation:

======== ========================= =============================================================================================================================================================================================================
**Name** **Type**                  **Documentation**
======== ========================= =============================================================================================================================================================================================================
Ref      LocalDataConsumerRef Type Ref is used to provide a complete set of reference fields. Derived reference types will restrict the RefType so that the content of the Ref element requires exactly what is needed for a complete reference.
======== ========================= =============================================================================================================================================================================================================

**LocalDataConsumerRefType: **\ LocalDataConsumerRefType references a
data consumer locally where the reference to the data consumer scheme
which defines it is provided elsewhere.

Derivation:

| *RefBaseType* (restriction) 
|    |image313|\ *LocalIdentifiableRefBaseType* (restriction) 
|          |image314|\ *LocalItemRefBaseType* (restriction) 
|                |image315|\ *LocalOrganisationRefBaseType* (restriction) 
|                      |image316|\ LocalDataConsumerRefType

Attributes:

id, local?, class?, package?

Content:

{Empty}

Attribute Documentation:

=========================== ================================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                    **Type**                           **Documentation**
=========================== ================================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
id                          IDType                             The id attribute identifies the object being referenced, and is therefore always required.
local (fixed: true)         xs:boolean                         The local attribute indicates whether this set of reference fields is meant for local referencing, in which case some of the reference fields will be implied from another context. Concrete instances of this class will always fix this value to either true or false, depending on their intended usage. If the value is fixed to true, then the complete set of reference fields will be required and a URN can be fully composed from the values.
class (fixed: DataConsumer) OrganisationTypeCode listType      The class attribute indicates the class name of the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
package (fixed: base)       ItemSchemePackageTyp eCodelistType The package attribute indicates the package name for the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
=========================== ================================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================

**DataProviderSchemeReferenceType: **\ DataProviderSchemeReferenceType
is a type for referencing a data provider scheme object. It consists of
a URN and/or a complete set of reference fields.

Derivation:

| *ReferenceType* (restriction) 
|    |image317|\ *MaintainableReferenceBaseType* (restriction) 
|          |image318|\ *ItemSchemeReferenceBaseType* (restriction) 
|                |image319|\ *OrganisationSchemeReferenceBaseType* (restriction) 
|                      |image320|\ DataProviderSchemeReferenceType

Content:

( (Ref, URN?) \| URN)

Element Documentation:

======== ========================== =============================================================================================================================================================================================================
**Name** **Type**                   **Documentation**
======== ========================== =============================================================================================================================================================================================================
Ref      DataProviderSchemeRe fType Ref is used to provide a complete set of reference fields. Derived reference types will restrict the RefType so that the content of the Ref element requires exactly what is needed for a complete reference.
URN      xs:anyURI                  URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
URN      xs:anyURI                  URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
======== ========================== =============================================================================================================================================================================================================

**DataProviderSchemeRefType: **\ DataProviderSchemeRefType contains a
set of reference fields for a data provider scheme.

Derivation:

| *RefBaseType* (restriction) 
|    |image321|\ *MaintainableRefBaseType* (restriction) 
|          |image322|\ *ItemSchemeRefBaseType* (restriction) 
|                |image323|\ *OrganisationSchemeRefBaseType* (restriction) 
|                      |image324|\ DataProviderSchemeRefType

Attributes:

agencyID, id, version?, local?, class?, package?

Content:

{Empty}

Attribute Documentation:

================================= =================================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                          **Type**                            **Documentation**
================================= =================================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
agencyID                          NestedNCNameIDType                  The agencyID attribute identifies the maintenance agency for the object being referenced (agency-id in the URN structure). This is optional to allow for local references (where the other reference fields are inferred from another context), but all complete references will require this.
id                                IDType                              The id attribute identifies the object being referenced, and is therefore always required.
version (default: 1.0)            VersionType                         The version attribute identifies the version of the object being reference, if applicable. If this is available, a default value of 1.0 will always apply.
local (fixed: false)              xs:boolean                          The local attribute indicates whether this set of reference fields is meant for local referencing, in which case some of the reference fields will be implied from another context. Concrete instances of this class will always fix this value to either true or false, depending on their intended usage. If the value is fixed to true, then the complete set of reference fields will be required and a URN can be fully composed from the values.
class (fixed: DataProviderScheme) OrganisationSchemeTy peCodelistType The class attribute indicates the class name of the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
package (fixed: base)             ItemSchemePackageTyp eCodelistType  The package attribute indicates the package name for the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
================================= =================================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================

**DataProviderReferenceType: **\ DataProviderReferenceType is a type for
referencing a data provider. It consists of a URN and/or a complete set
of reference fields.

Derivation:

| *ReferenceType* (restriction) 
|    |image325|\ *ChildObjectReferenceType* (restriction) 
|          |image326|\ *ItemReferenceType* (restriction) 
|                |image327|\ *OrganisationReferenceBaseType* (restriction) 
|                      |image328|\ DataProviderReferenceType

Content:

( (Ref, URN?) \| URN)

Element Documentation:

======== =================== =============================================================================================================================================================================================================
**Name** **Type**            **Documentation**
======== =================== =============================================================================================================================================================================================================
Ref      DataProviderRefType Ref is used to provide a complete set of reference fields. Derived reference types will restrict the RefType so that the content of the Ref element requires exactly what is needed for a complete reference.
URN      xs:anyURI           URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
URN      xs:anyURI           URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
======== =================== =============================================================================================================================================================================================================

**DataProviderRefType: **\ DataProviderRefType contains a set of
reference fields for referencing a data provider within a data provider
scheme.

Derivation:

| *RefBaseType* (restriction) 
|    |image329|\ *ChildObjectRefBaseType* (restriction) 
|          |image330|\ *ItemRefBaseType* (restriction) 
|                |image331|\ *OrganisationRefBaseType* (restriction) 
|                      |image332|\ DataProviderRefType

Attributes:

agencyID, maintainableParentID, maintainableParentVersion?, id, local?,
class?, package?

Content:

{Empty}

Attribute Documentation:

======================================== ================================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                                 **Type**                           **Documentation**
======================================== ================================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
agencyID                                 NestedNCNameIDType                 The agencyID attribute identifies the maintenance agency for the object being referenced (agency-id in the URN structure). This is optional to allow for local references (where the other reference fields are inferred from another context), but all complete references will require this.
maintainableParentID                     IDType                             The maintainableParentID references the organisation scheme in which the organisation being referenced is defined.
maintainableParentVersion (default: 1.0) VersionType                        The maintainableParentVersion attribute references the version of the organisation scheme in which the organisation being referenced is defined. If not supplied, a default value of 1.0 is assumed.
id                                       IDType                             The id attribute identifies the object being referenced, and is therefore always required.
local (fixed: false)                     xs:boolean                         The local attribute indicates whether this set of reference fields is meant for local referencing, in which case some of the reference fields will be implied from another context. Concrete instances of this class will always fix this value to either true or false, depending on their intended usage. If the value is fixed to true, then the complete set of reference fields will be required and a URN can be fully composed from the values.
class (fixed: DataProvider)              OrganisationTypeCode listType      The class attribute indicates the class name of the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
package (fixed: base)                    ItemSchemePackageTyp eCodelistType The package attribute indicates the package name for the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
======================================== ================================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================

**LocalDataProviderReferenceType: **\ LocalDataProviderReferenceType
provides a simple reference to a data provider, where the reference to
the data provider scheme which defines it is provided in another
context.

Derivation:

| *ReferenceType* (restriction) 
|    |image333|\ *LocalItemReferenceType* (restriction) 
|          |image334|\ *LocalOrganisationReferenceBaseType* (restriction) 
|                |image335|\ LocalDataProviderReferenceType

Content:

Ref

Element Documentation:

======== ========================= =============================================================================================================================================================================================================
**Name** **Type**                  **Documentation**
======== ========================= =============================================================================================================================================================================================================
Ref      LocalDataProviderRef Type Ref is used to provide a complete set of reference fields. Derived reference types will restrict the RefType so that the content of the Ref element requires exactly what is needed for a complete reference.
======== ========================= =============================================================================================================================================================================================================

**LocalDataProviderRefType: **\ LocalDataProviderRefType references a
data provider locally where the reference to the data provider scheme
which defines it is provided elsewhere.

Derivation:

| *RefBaseType* (restriction) 
|    |image336|\ *LocalIdentifiableRefBaseType* (restriction) 
|          |image337|\ *LocalItemRefBaseType* (restriction) 
|                |image338|\ *LocalOrganisationRefBaseType* (restriction) 
|                      |image339|\ LocalDataProviderRefType

Attributes:

id, local?, class?, package?

Content:

{Empty}

Attribute Documentation:

=========================== ================================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                    **Type**                           **Documentation**
=========================== ================================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
id                          IDType                             The id attribute identifies the object being referenced, and is therefore always required.
local (fixed: true)         xs:boolean                         The local attribute indicates whether this set of reference fields is meant for local referencing, in which case some of the reference fields will be implied from another context. Concrete instances of this class will always fix this value to either true or false, depending on their intended usage. If the value is fixed to true, then the complete set of reference fields will be required and a URN can be fully composed from the values.
class (fixed: DataProvider) OrganisationTypeCode listType      The class attribute indicates the class name of the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
package (fixed: base)       ItemSchemePackageTyp eCodelistType The package attribute indicates the package name for the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
=========================== ================================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================

**ReportingTaxonomyReferenceType: **\ ReportingTaxonomyReferenceType is
a type for referencing a reporting taxonomy object. It consists of a URN
and/or a complete set of reference fields.

Derivation:

| *ReferenceType* (restriction) 
|    |image340|\ *MaintainableReferenceBaseType* (restriction) 
|          |image341|\ *ItemSchemeReferenceBaseType* (restriction) 
|                |image342|\ ReportingTaxonomyReferenceType

Content:

( (Ref, URN?) \| URN)

Element Documentation:

======== ========================= =============================================================================================================================================================================================================
**Name** **Type**                  **Documentation**
======== ========================= =============================================================================================================================================================================================================
Ref      ReportingTaxonomyRef Type Ref is used to provide a complete set of reference fields. Derived reference types will restrict the RefType so that the content of the Ref element requires exactly what is needed for a complete reference.
URN      xs:anyURI                 URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
URN      xs:anyURI                 URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
======== ========================= =============================================================================================================================================================================================================

**ReportingTaxonomyRefType: **\ ReportingTaxonomyRefType provides a
reference to a reporting taxonomy via a complete set of reference
fields.

Derivation:

| *RefBaseType* (restriction) 
|    |image343|\ *MaintainableRefBaseType* (restriction) 
|          |image344|\ *ItemSchemeRefBaseType* (restriction) 
|                |image345|\ ReportingTaxonomyRefType

Attributes:

agencyID, id, version?, local?, class?, package?

Content:

{Empty}

Attribute Documentation:

================================ ================================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                         **Type**                           **Documentation**
================================ ================================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
agencyID                         NestedNCNameIDType                 The agencyID attribute identifies the maintenance agency for the object being referenced (agency-id in the URN structure). This is optional to allow for local references (where the other reference fields are inferred from another context), but all complete references will require this.
id                               IDType                             The id attribute identifies the object being referenced, and is therefore always required.
version (default: 1.0)           VersionType                        The version attribute identifies the version of the object being reference, if applicable. If this is available, a default value of 1.0 will always apply.
local (fixed: false)             xs:boolean                         The local attribute indicates whether this set of reference fields is meant for local referencing, in which case some of the reference fields will be implied from another context. Concrete instances of this class will always fix this value to either true or false, depending on their intended usage. If the value is fixed to true, then the complete set of reference fields will be required and a URN can be fully composed from the values.
class (fixed: ReportingTaxonomy) ItemSchemeTypeCodeli stType        The class attribute indicates the class name of the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
package (fixed: categoryscheme)  ItemSchemePackageTyp eCodelistType The package attribute indicates the package name for the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
================================ ================================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================

**ReportingCategoryReferenceType: **\ ReportingCategoryReferenceType is
a type for referencing a reporting category object. It consists of a URN
and/or a complete set of reference fields.

Derivation:

| *ReferenceType* (restriction) 
|    |image346|\ *ChildObjectReferenceType* (restriction) 
|          |image347|\ *ItemReferenceType* (restriction) 
|                |image348|\ ReportingCategoryReferenceType

Content:

( (Ref, URN?) \| URN)

Element Documentation:

======== ====================== =============================================================================================================================================================================================================
**Name** **Type**               **Documentation**
======== ====================== =============================================================================================================================================================================================================
Ref      ReportCategoryRefTyp e Ref is used to provide a complete set of reference fields. Derived reference types will restrict the RefType so that the content of the Ref element requires exactly what is needed for a complete reference.
URN      xs:anyURI              URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
URN      xs:anyURI              URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
======== ====================== =============================================================================================================================================================================================================

**ReportCategoryRefType: **\ ReportCategoryRefType contains a set of
fields for referencing a reporting category within a reporting taxonomy.

Derivation:

| *RefBaseType* (restriction) 
|    |image349|\ *ChildObjectRefBaseType* (restriction) 
|          |image350|\ *ItemRefBaseType* (restriction) 
|                |image351|\ ReportCategoryRefType

Attributes:

agencyID, maintainableParentID, maintainableParentVersion?, id, local?,
class?, package?

Content:

{Empty}

Attribute Documentation:

======================================== ================================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                                 **Type**                           **Documentation**
======================================== ================================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
agencyID                                 NestedNCNameIDType                 The agencyID attribute identifies the maintenance agency for the object being referenced (agency-id in the URN structure). This is optional to allow for local references (where the other reference fields are inferred from another context), but all complete references will require this.
maintainableParentID                     IDType                             The maintainableParentID references the reporting taxonomy in which the reporting category being referenced is defined.
maintainableParentVersion (default: 1.0) VersionType                        The maintainableParentVersion attribute references the version of the reporting taxonomy in which the reporting category being referenced is defined. If not supplied, a default value of 1.0 is assumed.
id                                       NestedIDType                       The id attribute identifies the object being referenced, and is therefore always required.
local (fixed: false)                     xs:boolean                         The local attribute indicates whether this set of reference fields is meant for local referencing, in which case some of the reference fields will be implied from another context. Concrete instances of this class will always fix this value to either true or false, depending on their intended usage. If the value is fixed to true, then the complete set of reference fields will be required and a URN can be fully composed from the values.
class (fixed: ReportingCategory)         ItemTypeCodelistType               The class attribute indicates the class name of the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
package (fixed: categoryscheme)          ItemSchemePackageTyp eCodelistType The package attribute indicates the package name for the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
======================================== ================================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================

**LocalReportingCategoryReferenceType: **\ LocalReportingCategoryReferenceType
provides a simple references to a reporting category where the
identification of the reporting taxonomy which defines it is contained
in another context.

Derivation:

| *ReferenceType* (restriction) 
|    |image352|\ *LocalItemReferenceType* (restriction) 
|          |image353|\ LocalReportingCategoryReferenceType

Content:

Ref

Element Documentation:

======== ============================== =============================================================================================================================================================================================================
**Name** **Type**                       **Documentation**
======== ============================== =============================================================================================================================================================================================================
Ref      LocalReportingCatego ryRefType Ref is used to provide a complete set of reference fields. Derived reference types will restrict the RefType so that the content of the Ref element requires exactly what is needed for a complete reference.
======== ============================== =============================================================================================================================================================================================================

**LocalReportingCategoryRefType: **\ LocalReportingCategoryRefType
references a reporting category locally where the references to the
reporting taxonomy which defines it is provided elsewhere.

Derivation:

| *RefBaseType* (restriction) 
|    |image354|\ *LocalIdentifiableRefBaseType* (restriction) 
|          |image355|\ *LocalItemRefBaseType* (restriction) 
|                |image356|\ LocalReportingCategoryRefType

Attributes:

id, local?, class?, package?

Content:

{Empty}

Attribute Documentation:

================================ ================================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                         **Type**                           **Documentation**
================================ ================================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
id                               NestedIDType                       The id attribute identifies the object being referenced, and is therefore always required.
local (fixed: true)              xs:boolean                         The local attribute indicates whether this set of reference fields is meant for local referencing, in which case some of the reference fields will be implied from another context. Concrete instances of this class will always fix this value to either true or false, depending on their intended usage. If the value is fixed to true, then the complete set of reference fields will be required and a URN can be fully composed from the values.
class (fixed: ReportingCategory) ItemTypeCodelistType               The class attribute indicates the class name of the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
package (fixed: categoryscheme)  ItemSchemePackageTyp eCodelistType The package attribute indicates the package name for the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
================================ ================================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================

**HierarchicalCodelistReferenceType: **\ HierarchicalCodelistReferenceType
is a type for referencing a hierarchical codelist object. It consists of
a URN and/or a complete set of reference fields.

Derivation:

| *ReferenceType* (restriction) 
|    |image357|\ *MaintainableReferenceBaseType* (restriction) 
|          |image358|\ HierarchicalCodelistReferenceType

Content:

( (Ref, URN?) \| URN)

Element Documentation:

======== ============================ =============================================================================================================================================================================================================
**Name** **Type**                     **Documentation**
======== ============================ =============================================================================================================================================================================================================
Ref      HierarchicalCodelist RefType Ref is used to provide a complete set of reference fields. Derived reference types will restrict the RefType so that the content of the Ref element requires exactly what is needed for a complete reference.
URN      xs:anyURI                    URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
URN      xs:anyURI                    URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
======== ============================ =============================================================================================================================================================================================================

**HierarchicalCodelistRefType: **\ HierarchicalCodelistRefType contains
a set of reference fields for a hierarchical codelist.

Derivation:

| *RefBaseType* (restriction) 
|    |image359|\ *MaintainableRefBaseType* (restriction) 
|          |image360|\ HierarchicalCodelistRefType

Attributes:

agencyID, id, version?, local?, class?, package?

Content:

{Empty}

Attribute Documentation:

=================================== ================================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                            **Type**                           **Documentation**
=================================== ================================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
agencyID                            NestedNCNameIDType                 The agencyID attribute identifies the maintenance agency for the object being referenced (agency-id in the URN structure). This is optional to allow for local references (where the other reference fields are inferred from another context), but all complete references will require this.
id                                  IDType                             The id attribute identifies the object being referenced, and is therefore always required.
version (default: 1.0)              VersionType                        The version attribute identifies the version of the object being reference, if applicable. If this is available, a default value of 1.0 will always apply.
local (fixed: false)                xs:boolean                         The local attribute indicates whether this set of reference fields is meant for local referencing, in which case some of the reference fields will be implied from another context. Concrete instances of this class will always fix this value to either true or false, depending on their intended usage. If the value is fixed to true, then the complete set of reference fields will be required and a URN can be fully composed from the values.
class (fixed: HierarchicalCodelist) MaintainableTypeCode listType      The class attribute indicates the class name of the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
package (fixed: codelist)           ItemSchemePackageTyp eCodelistType The package attribute indicates the package name for the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
=================================== ================================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================

**HierarchyReferenceType: **\ HierarchyReferenceType is a type for
referencing a hierarchy within a hierarchical codelist.

Derivation:

| *ReferenceType* (restriction) 
|    |image361|\ *ChildObjectReferenceType* (restriction) 
|          |image362|\ HierarchyReferenceType

Content:

( (Ref, URN?) \| URN)

Element Documentation:

======== ================ =============================================================================================================================================================================================================
**Name** **Type**         **Documentation**
======== ================ =============================================================================================================================================================================================================
Ref      HierarchyRefType Ref is used to provide a complete set of reference fields. Derived reference types will restrict the RefType so that the content of the Ref element requires exactly what is needed for a complete reference.
URN      xs:anyURI        URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
URN      xs:anyURI        URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
======== ================ =============================================================================================================================================================================================================

**HierarchyRefType: **\ HierarchyRefType is type which references a
hierarchy from within a hierarchical codelist. Reference fields are
required for both the hierarchy and the codelist.

Derivation:

| *RefBaseType* (restriction) 
|    |image363|\ *ChildObjectRefBaseType* (restriction) 
|          |image364|\ HierarchyRefType

Attributes:

agencyID, maintainableParentID, maintainableParentVersion?, id, local?,
class?, package?

Content:

{Empty}

Attribute Documentation:

======================================== ======================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                                 **Type**                 **Documentation**
======================================== ======================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
agencyID                                 NestedNCNameIDType       The agencyID attribute identifies the maintenance agency for the object being referenced (agency-id in the URN structure). This is optional to allow for local references (where the other reference fields are inferred from another context), but all complete references will require this.
maintainableParentID                     IDType                   The maintainableParentID attribute identifies the maintainable object in which the referenced object is defined, if applicable (maintainable-parent-object-id in the URN structure). This is only used in references where the referenced object is not itself maintainable.
maintainableParentVersion (default: 1.0) VersionType              The maintainableParentVersion attribute identifies the version of the maintainable object in which the referenced object is defined (maintainable-parent-object-version in the URN structure). This is only used in references where the referenced object is not itself maintainable. This should only be used when the maintainableParentID is present. If this is available, a default of 1.0 will always apply.
id                                       IDType                   The id attribute identifies the object being referenced, and is therefore always required.
local (fixed: false)                     xs:boolean               The local attribute indicates whether this set of reference fields is meant for local referencing, in which case some of the reference fields will be implied from another context. Concrete instances of this class will always fix this value to either true or false, depending on their intended usage. If the value is fixed to true, then the complete set of reference fields will be required and a URN can be fully composed from the values.
class (fixed: Hierarchy)                 ObjectTypeCodelistTy pe  The class attribute indicates the class name of the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
package (fixed: codelist)                PackageTypeCodelistT ype The package attribute indicates the package name for the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
======================================== ======================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================

**LevelReferenceType: **\ LevelReferenceType is a type for referencing a
level object. It consists of a URN and/or a complete set of reference
fields.

Derivation:

| *ReferenceType* (restriction) 
|    |image365|\ *ChildObjectReferenceType* (restriction) 
|          |image366|\ LevelReferenceType

Content:

( (Ref, URN?) \| URN)

Element Documentation:

======== ============ =============================================================================================================================================================================================================
**Name** **Type**     **Documentation**
======== ============ =============================================================================================================================================================================================================
Ref      LevelRefType Ref is used to provide a complete set of reference fields. Derived reference types will restrict the RefType so that the content of the Ref element requires exactly what is needed for a complete reference.
URN      xs:anyURI    URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
URN      xs:anyURI    URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
======== ============ =============================================================================================================================================================================================================

**LevelRefType: **\ LevelRefType references a level from within a
hierarchical codelist. Reference fields are required for both the level
and the codelist.

Derivation:

| *RefBaseType* (restriction) 
|    |image367|\ *ChildObjectRefBaseType* (restriction) 
|          |image368|\ LevelRefType

Attributes:

agencyID, maintainableParentID, maintainableParentVersion?, id, local?,
class?, package?

Content:

{Empty}

Attribute Documentation:

======================================== ======================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                                 **Type**                 **Documentation**
======================================== ======================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
agencyID                                 NestedNCNameIDType       The agencyID attribute identifies the maintenance agency for the object being referenced (agency-id in the URN structure). This is optional to allow for local references (where the other reference fields are inferred from another context), but all complete references will require this.
maintainableParentID                     IDType                   The maintainableParentID attribute identifies the maintainable object in which the referenced object is defined, if applicable (maintainable-parent-object-id in the URN structure). This is only used in references where the referenced object is not itself maintainable.
maintainableParentVersion (default: 1.0) VersionType              The maintainableParentVersion attribute identifies the version of the maintainable object in which the referenced object is defined (maintainable-parent-object-version in the URN structure). This is only used in references where the referenced object is not itself maintainable. This should only be used when the maintainableParentID is present. If this is available, a default of 1.0 will always apply.
id                                       IDType                   The id attribute identifies the object being referenced, and is therefore always required.
local (fixed: false)                     xs:boolean               The local attribute indicates whether this set of reference fields is meant for local referencing, in which case some of the reference fields will be implied from another context. Concrete instances of this class will always fix this value to either true or false, depending on their intended usage. If the value is fixed to true, then the complete set of reference fields will be required and a URN can be fully composed from the values.
class (fixed: Level)                     ObjectTypeCodelistTy pe  The class attribute indicates the class name of the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
package (fixed: codelist)                PackageTypeCodelistT ype The package attribute indicates the package name for the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
======================================== ======================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================

**LocalLevelReferenceType: **\ LocalLevelReferenceType is a type for
referencing a level object where the reference to the hierarchical
codelist and the hierarchy in which it is defined is provided in another
context (e.g. is inferred from the hierarchy in which the reference is
defined).

Derivation:

| *ReferenceType* (restriction) 
|    |image369|\ LocalLevelReferenceType

Content:

Ref

Element Documentation:

======== ================= =============================================================================================================================================================================================================
**Name** **Type**          **Documentation**
======== ================= =============================================================================================================================================================================================================
Ref      LocalLevelRefType Ref is used to provide a complete set of reference fields. Derived reference types will restrict the RefType so that the content of the Ref element requires exactly what is needed for a complete reference.
======== ================= =============================================================================================================================================================================================================

**LocalLevelRefType: **\ LocalLevelRefType references a level object
where the reference to the hierarchy in which it is contained and the
hierarchical codelist which define it are provided in another context.

Derivation:

| *RefBaseType* (restriction) 
|    |image370|\ *LocalIdentifiableRefBaseType* (restriction) 
|          |image371|\ LocalLevelRefType

Attributes:

containerID?, id, local?, class?, package?

Content:

{Empty}

Attribute Documentation:

==================== ======================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**             **Type**                 **Documentation**
==================== ======================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
containerID          NestedIDType             The containerID attribute identifies the object within a maintainable object in which the referenced object is defined (container-object-id in the URN structure). This is only used in references where the referenced object is not contained directly within a maintainable object (e.g. a Component within a ComponentList, within a maintainable Structure). If the container has a fixed identifier, this attribute will not be present.
id                   NestedIDType             The id attribute identifies the object being referenced, and is therefore always required.
local (fixed: true)  xs:boolean               The local attribute indicates whether this set of reference fields is meant for local referencing, in which case some of the reference fields will be implied from another context. Concrete instances of this class will always fix this value to either true or false, depending on their intended usage. If the value is fixed to true, then the complete set of reference fields will be required and a URN can be fully composed from the values.
class (fixed: Level) ObjectTypeCodelistTy pe  The class attribute indicates the class name of the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
package              PackageTypeCodelistT ype The package attribute indicates the package name for the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
==================== ======================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================

**HierarchicalCodeReferenceType: **\ HierarchicalCodeReferenceType is a
type for referencing a hierarchical code object. It consists of a URN
and/or a complete set of reference fields.

Derivation:

| *ReferenceType* (restriction) 
|    |image372|\ *ContainerChildObjectReferenceType* (restriction) 
|          |image373|\ HierarchicalCodeReferenceType

Content:

( (Ref, URN?) \| URN)

Element Documentation:

======== ======================== =============================================================================================================================================================================================================
**Name** **Type**                 **Documentation**
======== ======================== =============================================================================================================================================================================================================
Ref      HierarchicalCodeRefT ype Ref is used to provide a complete set of reference fields. Derived reference types will restrict the RefType so that the content of the Ref element requires exactly what is needed for a complete reference.
URN      xs:anyURI                URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
URN      xs:anyURI                URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
======== ======================== =============================================================================================================================================================================================================

**HierarchicalCodeRefType: **\ HierarchicalCodeRefType references a code
from within a hierarchical codelist. Reference fields are required for
both the code and the codelist.

Derivation:

| *RefBaseType* (restriction) 
|    |image374|\ *ContainerChildObjectRefBaseType* (restriction) 
|          |image375|\ HierarchicalCodeRefType

Attributes:

agencyID, maintainableParentID, maintainableParentVersion?, containerID,
id, version?, local?, class?, package?

Content:

{Empty}

Attribute Documentation:

======================================== ======================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                                 **Type**                 **Documentation**
======================================== ======================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
agencyID                                 NestedNCNameIDType       The agencyID attribute identifies the maintenance agency for the object being referenced (agency-id in the URN structure). This is optional to allow for local references (where the other reference fields are inferred from another context), but all complete references will require this.
maintainableParentID                     IDType                   The maintainableParentID references the hierarchical codelist in which the code being referenced is defined.
maintainableParentVersion (default: 1.0) VersionType              The maintainableParentVersion attribute references the version of the hierarchical codelist in which the code being referenced is defined. If not supplied, a default value of 1.0 is assumed.
containerID                              IDType                   The containerID references the hierarchy which contains the code being referenced is defined.
id                                       NestedIDType             The id attribute identifies the object being referenced, and is therefore always required.
version                                  VersionType              The version attribute identifies the version of the object being reference, if applicable. If this is available, a default value of 1.0 will always apply.
local (fixed: false)                     xs:boolean               The local attribute indicates whether this set of reference fields is meant for local referencing, in which case some of the reference fields will be implied from another context. Concrete instances of this class will always fix this value to either true or false, depending on their intended usage. If the value is fixed to true, then the complete set of reference fields will be required and a URN can be fully composed from the values.
class (fixed: HierarchicalCode)          ObjectTypeCodelistTy pe  The class attribute indicates the class name of the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
package (fixed: codelist)                PackageTypeCodelistT ype The package attribute indicates the package name for the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
======================================== ======================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================

**ConstraintReferenceType: **\ ConstraintReferenceType is a type for
referencing a constraint object. It consists of a URN and/or a complete
set of reference fields.

Derivation:

| *ReferenceType* (restriction) 
|    |image376|\ *MaintainableReferenceBaseType* (restriction) 
|          |image377|\ ConstraintReferenceType

Content:

( (Ref, URN?) \| URN)

Element Documentation:

======== =================== =============================================================================================================================================================================================================
**Name** **Type**            **Documentation**
======== =================== =============================================================================================================================================================================================================
Ref      *ConstraintRefType* Ref is used to provide a complete set of reference fields. Derived reference types will restrict the RefType so that the content of the Ref element requires exactly what is needed for a complete reference.
URN      xs:anyURI           URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
URN      xs:anyURI           URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
======== =================== =============================================================================================================================================================================================================

**ConstraintRefType: **\ ConstraintRefType contains a set of reference
fields for a constraint.

Derivation:

| *RefBaseType* (restriction) 
|    |image378|\ *MaintainableRefBaseType* (restriction) 
|          |image379|\ *ConstraintRefType*

Attributes:

agencyID, id, version?, local?, class?, package?

Content:

{Empty}

Attribute Documentation:

========================= =========================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                  **Type**                    **Documentation**
========================= =========================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
agencyID                  NestedNCNameIDType          The agencyID attribute identifies the maintenance agency for the object being referenced (agency-id in the URN structure). This is optional to allow for local references (where the other reference fields are inferred from another context), but all complete references will require this.
id                        IDType                      The id attribute identifies the object being referenced, and is therefore always required.
version (default: 1.0)    VersionType                 The version attribute identifies the version of the object being reference, if applicable. If this is available, a default value of 1.0 will always apply.
local (fixed: false)      xs:boolean                  The local attribute indicates whether this set of reference fields is meant for local referencing, in which case some of the reference fields will be implied from another context. Concrete instances of this class will always fix this value to either true or false, depending on their intended usage. If the value is fixed to true, then the complete set of reference fields will be required and a URN can be fully composed from the values.
class                     ConstraintTypeCodeli stType The class attribute indicates the class name of the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
package (fixed: registry) PackageTypeCodelistT ype    The package attribute indicates the package name for the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
========================= =========================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================

**AttachmentConstraintReferenceType: **\ AttachmentConstraintReferenceType
is a type for referencing a attachment constraint object. It consists of
a URN and/or a complete set of reference fields.

Derivation:

| *ReferenceType* (restriction) 
|    |image380|\ *MaintainableReferenceBaseType* (restriction) 
|          |image381|\ ConstraintReferenceType (restriction) 
|                |image382|\ AttachmentConstraintReferenceType

Content:

( (Ref, URN?) \| URN)

Element Documentation:

======== ============================ =============================================================================================================================================================================================================
**Name** **Type**                     **Documentation**
======== ============================ =============================================================================================================================================================================================================
Ref      AttachmentConstraint RefType Ref is used to provide a complete set of reference fields. Derived reference types will restrict the RefType so that the content of the Ref element requires exactly what is needed for a complete reference.
URN      xs:anyURI                    URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
URN      xs:anyURI                    URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
======== ============================ =============================================================================================================================================================================================================

**AttachmentConstraintRefType: **\ AttachmentConstraintRefType contains
a set of reference fields for an attachment constraint.

Derivation:

| *RefBaseType* (restriction) 
|    |image383|\ *MaintainableRefBaseType* (restriction) 
|          |image384|\ *ConstraintRefType* (restriction) 
|                |image385|\ AttachmentConstraintRefType

Attributes:

agencyID, id, version?, local?, class?, package?

Content:

{Empty}

Attribute Documentation:

=================================== =========================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                            **Type**                    **Documentation**
=================================== =========================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
agencyID                            NestedNCNameIDType          The agencyID attribute identifies the maintenance agency for the object being referenced (agency-id in the URN structure). This is optional to allow for local references (where the other reference fields are inferred from another context), but all complete references will require this.
id                                  IDType                      The id attribute identifies the object being referenced, and is therefore always required.
version (default: 1.0)              VersionType                 The version attribute identifies the version of the object being reference, if applicable. If this is available, a default value of 1.0 will always apply.
local (fixed: false)                xs:boolean                  The local attribute indicates whether this set of reference fields is meant for local referencing, in which case some of the reference fields will be implied from another context. Concrete instances of this class will always fix this value to either true or false, depending on their intended usage. If the value is fixed to true, then the complete set of reference fields will be required and a URN can be fully composed from the values.
class (fixed: AttachmentConstraint) ConstraintTypeCodeli stType The class attribute indicates the class name of the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
package (fixed: registry)           PackageTypeCodelistT ype    The package attribute indicates the package name for the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
=================================== =========================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================

**ContentConstraintReferenceType: **\ ContentConstraintReferenceType is
a type for referencing a content constraint object. It consists of a URN
and/or a complete set of reference fields.

Derivation:

| *ReferenceType* (restriction) 
|    |image386|\ *MaintainableReferenceBaseType* (restriction) 
|          |image387|\ ConstraintReferenceType (restriction) 
|                |image388|\ ContentConstraintReferenceType

Content:

( (Ref, URN?) \| URN)

Element Documentation:

======== ========================= =============================================================================================================================================================================================================
**Name** **Type**                  **Documentation**
======== ========================= =============================================================================================================================================================================================================
Ref      ContentConstraintRef Type Ref is used to provide a complete set of reference fields. Derived reference types will restrict the RefType so that the content of the Ref element requires exactly what is needed for a complete reference.
URN      xs:anyURI                 URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
URN      xs:anyURI                 URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
======== ========================= =============================================================================================================================================================================================================

**ContentConstraintRefType: **\ ContentConstraintRefType contains a set
of reference fields for a content constraint.

Derivation:

| *RefBaseType* (restriction) 
|    |image389|\ *MaintainableRefBaseType* (restriction) 
|          |image390|\ *ConstraintRefType* (restriction) 
|                |image391|\ ContentConstraintRefType

Attributes:

agencyID, id, version?, local?, class?, package?

Content:

{Empty}

Attribute Documentation:

================================ =========================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                         **Type**                    **Documentation**
================================ =========================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
agencyID                         NestedNCNameIDType          The agencyID attribute identifies the maintenance agency for the object being referenced (agency-id in the URN structure). This is optional to allow for local references (where the other reference fields are inferred from another context), but all complete references will require this.
id                               IDType                      The id attribute identifies the object being referenced, and is therefore always required.
version (default: 1.0)           VersionType                 The version attribute identifies the version of the object being reference, if applicable. If this is available, a default value of 1.0 will always apply.
local (fixed: false)             xs:boolean                  The local attribute indicates whether this set of reference fields is meant for local referencing, in which case some of the reference fields will be implied from another context. Concrete instances of this class will always fix this value to either true or false, depending on their intended usage. If the value is fixed to true, then the complete set of reference fields will be required and a URN can be fully composed from the values.
class (fixed: ContentConstraint) ConstraintTypeCodeli stType The class attribute indicates the class name of the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
package (fixed: registry)        PackageTypeCodelistT ype    The package attribute indicates the package name for the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
================================ =========================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================

**DataflowReferenceType: **\ DataflowReferenceType is a type for
referencing a dataflow object. It consists of a URN and/or a complete
set of reference fields.

Derivation:

| *ReferenceType* (restriction) 
|    |image392|\ *MaintainableReferenceBaseType* (restriction) 
|          |image393|\ *StructureUsageReferenceBaseType* (restriction) 
|                |image394|\ DataflowReferenceType

Content:

( (Ref, URN?) \| URN)

Element Documentation:

======== =============== =============================================================================================================================================================================================================
**Name** **Type**        **Documentation**
======== =============== =============================================================================================================================================================================================================
Ref      DataflowRefType Ref is used to provide a complete set of reference fields. Derived reference types will restrict the RefType so that the content of the Ref element requires exactly what is needed for a complete reference.
URN      xs:anyURI       URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
URN      xs:anyURI       URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
======== =============== =============================================================================================================================================================================================================

**DataflowRefType: **\ DataflowRefType contains a set of reference
fields for a data flow.

Derivation:

| *RefBaseType* (restriction) 
|    |image395|\ *MaintainableRefBaseType* (restriction) 
|          |image396|\ *StructureOrUsageRefBaseType* (restriction) 
|                |image397|\ *StructureUsageRefBaseType* (restriction) 
|                      |image398|\ DataflowRefType

Attributes:

agencyID, id, version?, local?, class?, package?

Content:

{Empty}

Attribute Documentation:

============================== ================================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                       **Type**                          **Documentation**
============================== ================================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
agencyID                       NestedNCNameIDType                The agencyID attribute identifies the maintenance agency for the object being referenced (agency-id in the URN structure). This is optional to allow for local references (where the other reference fields are inferred from another context), but all complete references will require this.
id                             IDType                            The id attribute identifies the object being referenced, and is therefore always required.
version (default: 1.0)         VersionType                       The version attribute identifies the version of the object being reference, if applicable. If this is available, a default value of 1.0 will always apply.
local (fixed: false)           xs:boolean                        The local attribute indicates whether this set of reference fields is meant for local referencing, in which case some of the reference fields will be implied from another context. Concrete instances of this class will always fix this value to either true or false, depending on their intended usage. If the value is fixed to true, then the complete set of reference fields will be required and a URN can be fully composed from the values.
class (fixed: Dataflow)        StructureUsageTypeCo delistType   The class attribute indicates the class name of the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
package (fixed: datastructure) StructurePackageType CodelistType The package attribute indicates the package name for the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
============================== ================================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================

**MetadataflowReferenceType: **\ MetadataflowReferenceType is a type for
referencing a metadata flow object. It consists of a URN and/or a
complete set of reference fields.

Derivation:

| *ReferenceType* (restriction) 
|    |image399|\ *MaintainableReferenceBaseType* (restriction) 
|          |image400|\ *StructureUsageReferenceBaseType* (restriction) 
|                |image401|\ MetadataflowReferenceType

Content:

( (Ref, URN?) \| URN)

Element Documentation:

======== =================== =============================================================================================================================================================================================================
**Name** **Type**            **Documentation**
======== =================== =============================================================================================================================================================================================================
Ref      MetadataflowRefType Ref is used to provide a complete set of reference fields. Derived reference types will restrict the RefType so that the content of the Ref element requires exactly what is needed for a complete reference.
URN      xs:anyURI           URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
URN      xs:anyURI           URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
======== =================== =============================================================================================================================================================================================================

**MetadataflowRefType: **\ MetadataflowRefType contains a set of
reference fields for a metadata flow.

Derivation:

| *RefBaseType* (restriction) 
|    |image402|\ *MaintainableRefBaseType* (restriction) 
|          |image403|\ *StructureOrUsageRefBaseType* (restriction) 
|                |image404|\ *StructureUsageRefBaseType* (restriction) 
|                      |image405|\ MetadataflowRefType

Attributes:

agencyID, id, version?, local?, class?, package?

Content:

{Empty}

Attribute Documentation:

================================== ================================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                           **Type**                          **Documentation**
================================== ================================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
agencyID                           NestedNCNameIDType                The agencyID attribute identifies the maintenance agency for the object being referenced (agency-id in the URN structure). This is optional to allow for local references (where the other reference fields are inferred from another context), but all complete references will require this.
id                                 IDType                            The id attribute identifies the object being referenced, and is therefore always required.
version (default: 1.0)             VersionType                       The version attribute identifies the version of the object being reference, if applicable. If this is available, a default value of 1.0 will always apply.
local (fixed: false)               xs:boolean                        The local attribute indicates whether this set of reference fields is meant for local referencing, in which case some of the reference fields will be implied from another context. Concrete instances of this class will always fix this value to either true or false, depending on their intended usage. If the value is fixed to true, then the complete set of reference fields will be required and a URN can be fully composed from the values.
class (fixed: Metadataflow)        StructureUsageTypeCo delistType   The class attribute indicates the class name of the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
package (fixed: metadatastructure) StructurePackageType CodelistType The package attribute indicates the package name for the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
================================== ================================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================

**DataStructureReferenceType: **\ DataStructureReferenceType is a type
for referencing a data structure definition object. It consists of a URN
and/or a complete set of reference fields.

Derivation:

| *ReferenceType* (restriction) 
|    |image406|\ *MaintainableReferenceBaseType* (restriction) 
|          |image407|\ *StructureReferenceBaseType* (restriction) 
|                |image408|\ DataStructureReferenceType

Content:

( (Ref, URN?) \| URN)

Element Documentation:

======== ==================== =============================================================================================================================================================================================================
**Name** **Type**             **Documentation**
======== ==================== =============================================================================================================================================================================================================
Ref      DataStructureRefType Ref is used to provide a complete set of reference fields. Derived reference types will restrict the RefType so that the content of the Ref element requires exactly what is needed for a complete reference.
URN      xs:anyURI            URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
URN      xs:anyURI            URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
======== ==================== =============================================================================================================================================================================================================

**DataStructureRefType: **\ DataStructureRefType contains a set of
reference fields for a data structure definition.

Derivation:

| *RefBaseType* (restriction) 
|    |image409|\ *MaintainableRefBaseType* (restriction) 
|          |image410|\ *StructureOrUsageRefBaseType* (restriction) 
|                |image411|\ *StructureRefBaseType* (restriction) 
|                      |image412|\ DataStructureRefType

Attributes:

agencyID, id, version?, local?, class?, package?

Content:

{Empty}

Attribute Documentation:

============================== ================================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                       **Type**                          **Documentation**
============================== ================================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
agencyID                       NestedNCNameIDType                The agencyID attribute identifies the maintenance agency for the object being referenced (agency-id in the URN structure). This is optional to allow for local references (where the other reference fields are inferred from another context), but all complete references will require this.
id                             IDType                            The id attribute identifies the object being referenced, and is therefore always required.
version (default: 1.0)         VersionType                       The version attribute identifies the version of the object being reference, if applicable. If this is available, a default value of 1.0 will always apply.
local (fixed: false)           xs:boolean                        The local attribute indicates whether this set of reference fields is meant for local referencing, in which case some of the reference fields will be implied from another context. Concrete instances of this class will always fix this value to either true or false, depending on their intended usage. If the value is fixed to true, then the complete set of reference fields will be required and a URN can be fully composed from the values.
class (fixed: DataStructure)   StructureTypeCodelis tType        The class attribute indicates the class name of the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
package (fixed: datastructure) StructurePackageType CodelistType The package attribute indicates the package name for the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
============================== ================================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================

**KeyDescriptorReferenceType: **\ KeyDescriptorReferenceType is a type
for referencing a key descriptor object. It consists of a URN and/or a
complete set of reference fields.

Derivation:

| *ReferenceType* (restriction) 
|    |image413|\ *ChildObjectReferenceType* (restriction) 
|          |image414|\ *ComponentListReferenceType* (restriction) 
|                |image415|\ KeyDescriptorReferenceType

Content:

( (Ref, URN?) \| URN)

Element Documentation:

======== ==================== =============================================================================================================================================================================================================
**Name** **Type**             **Documentation**
======== ==================== =============================================================================================================================================================================================================
Ref      KeyDescriptorRefType Ref is used to provide a complete set of reference fields. Derived reference types will restrict the RefType so that the content of the Ref element requires exactly what is needed for a complete reference.
URN      xs:anyURI            URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
URN      xs:anyURI            URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
======== ==================== =============================================================================================================================================================================================================

**KeyDescriptorRefType: **\ KeyDescriptorRefType contains a reference to
the key descriptor within a data structure definition.

Derivation:

| *RefBaseType* (restriction) 
|    |image416|\ *ChildObjectRefBaseType* (restriction) 
|          |image417|\ *ComponentListRefBaseType* (restriction) 
|                |image418|\ KeyDescriptorRefType

Attributes:

agencyID, maintainableParentID, maintainableParentVersion?, id, local?,
class?, package?

Content:

{Empty}

Attribute Documentation:

======================================== ================================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                                 **Type**                          **Documentation**
======================================== ================================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
agencyID                                 NestedNCNameIDType                The agencyID attribute identifies the maintenance agency for the object being referenced (agency-id in the URN structure). This is optional to allow for local references (where the other reference fields are inferred from another context), but all complete references will require this.
maintainableParentID                     IDType                            The maintainableParentID references the structure in which the component list being referenced is defined.
maintainableParentVersion (default: 1.0) VersionType                       The maintainableParentVersion attribute references the version of the structure in which the component list being referenced is defined. If not supplied, a default value of 1.0 is assumed.
id (fixed: DIMENSION_DESCRIPTOR)         IDType                            The id attribute identifies the object being referenced, and is therefore always required.
local (fixed: false)                     xs:boolean                        The local attribute indicates whether this set of reference fields is meant for local referencing, in which case some of the reference fields will be implied from another context. Concrete instances of this class will always fix this value to either true or false, depending on their intended usage. If the value is fixed to true, then the complete set of reference fields will be required and a URN can be fully composed from the values.
class (fixed: DimensionDescriptor)       ComponentListTypeCod elistType    The class attribute indicates the class name of the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
package (fixed: datastructure)           StructurePackageType CodelistType The package attribute indicates the package name for the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
======================================== ================================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================

**AttributeDescriptorReferenceType: **\ AttributeDescriptorReferenceType
is a type for referencing an attribute descriptor object. It consists of
a URN and/or a complete set of reference fields.

Derivation:

| *ReferenceType* (restriction) 
|    |image419|\ *ChildObjectReferenceType* (restriction) 
|          |image420|\ *ComponentListReferenceType* (restriction) 
|                |image421|\ AttributeDescriptorReferenceType

Content:

( (Ref, URN?) \| URN)

Element Documentation:

======== =========================== =============================================================================================================================================================================================================
**Name** **Type**                    **Documentation**
======== =========================== =============================================================================================================================================================================================================
Ref      AttributeDescriptorR efType Ref is used to provide a complete set of reference fields. Derived reference types will restrict the RefType so that the content of the Ref element requires exactly what is needed for a complete reference.
URN      xs:anyURI                   URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
URN      xs:anyURI                   URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
======== =========================== =============================================================================================================================================================================================================

**AttributeDescriptorRefType: **\ AttributeDescriptorRefType contains a
reference to the attribute descriptor within a data structure
definition.

Derivation:

| *RefBaseType* (restriction) 
|    |image422|\ *ChildObjectRefBaseType* (restriction) 
|          |image423|\ *ComponentListRefBaseType* (restriction) 
|                |image424|\ AttributeDescriptorRefType

Attributes:

agencyID, maintainableParentID, maintainableParentVersion?, id, local?,
class?, package?

Content:

{Empty}

Attribute Documentation:

======================================== ================================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                                 **Type**                          **Documentation**
======================================== ================================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
agencyID                                 NestedNCNameIDType                The agencyID attribute identifies the maintenance agency for the object being referenced (agency-id in the URN structure). This is optional to allow for local references (where the other reference fields are inferred from another context), but all complete references will require this.
maintainableParentID                     IDType                            The maintainableParentID references the structure in which the component list being referenced is defined.
maintainableParentVersion (default: 1.0) VersionType                       The maintainableParentVersion attribute references the version of the structure in which the component list being referenced is defined. If not supplied, a default value of 1.0 is assumed.
id (fixed: ATTRIBUTE_DESCRIPTOR)         IDType                            The id attribute identifies the object being referenced, and is therefore always required.
local (fixed: false)                     xs:boolean                        The local attribute indicates whether this set of reference fields is meant for local referencing, in which case some of the reference fields will be implied from another context. Concrete instances of this class will always fix this value to either true or false, depending on their intended usage. If the value is fixed to true, then the complete set of reference fields will be required and a URN can be fully composed from the values.
class (fixed: AttributeDescriptor)       ComponentListTypeCod elistType    The class attribute indicates the class name of the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
package (fixed: datastructure)           StructurePackageType CodelistType The package attribute indicates the package name for the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
======================================== ================================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================

**MeasureDescriptorReferenceType: **\ MeasureDescriptorReferenceType is
a type for referencing a measure descriptor object. It consists of a URN
and/or a complete set of reference fields.

Derivation:

| *ReferenceType* (restriction) 
|    |image425|\ *ChildObjectReferenceType* (restriction) 
|          |image426|\ *ComponentListReferenceType* (restriction) 
|                |image427|\ MeasureDescriptorReferenceType

Content:

( (Ref, URN?) \| URN)

Element Documentation:

======== ========================= =============================================================================================================================================================================================================
**Name** **Type**                  **Documentation**
======== ========================= =============================================================================================================================================================================================================
Ref      MeasureDescriptorRef Type Ref is used to provide a complete set of reference fields. Derived reference types will restrict the RefType so that the content of the Ref element requires exactly what is needed for a complete reference.
URN      xs:anyURI                 URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
URN      xs:anyURI                 URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
======== ========================= =============================================================================================================================================================================================================

**MeasureDescriptorRefType: **\ MeasureDescriptorRefType contains a
reference to the measure descriptor within a data structure definition.

Derivation:

| *RefBaseType* (restriction) 
|    |image428|\ *ChildObjectRefBaseType* (restriction) 
|          |image429|\ *ComponentListRefBaseType* (restriction) 
|                |image430|\ MeasureDescriptorRefType

Attributes:

agencyID, maintainableParentID, maintainableParentVersion?, id, local?,
class?, package?

Content:

{Empty}

Attribute Documentation:

======================================== ================================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                                 **Type**                          **Documentation**
======================================== ================================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
agencyID                                 NestedNCNameIDType                The agencyID attribute identifies the maintenance agency for the object being referenced (agency-id in the URN structure). This is optional to allow for local references (where the other reference fields are inferred from another context), but all complete references will require this.
maintainableParentID                     IDType                            The maintainableParentID references the structure in which the component list being referenced is defined.
maintainableParentVersion (default: 1.0) VersionType                       The maintainableParentVersion attribute references the version of the structure in which the component list being referenced is defined. If not supplied, a default value of 1.0 is assumed.
id (fixed: MEASURE_DESCRIPTOR)           IDType                            The id attribute identifies the object being referenced, and is therefore always required.
local (fixed: false)                     xs:boolean                        The local attribute indicates whether this set of reference fields is meant for local referencing, in which case some of the reference fields will be implied from another context. Concrete instances of this class will always fix this value to either true or false, depending on their intended usage. If the value is fixed to true, then the complete set of reference fields will be required and a URN can be fully composed from the values.
class (fixed: MeasureDescriptor)         ComponentListTypeCod elistType    The class attribute indicates the class name of the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
package (fixed: datastructure)           StructurePackageType CodelistType The package attribute indicates the package name for the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
======================================== ================================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================

**GroupKeyDescriptorReferenceType: **\ GroupKeyDescriptorReferenceType
is a type for referencing a group key descriptor object. It consists of
a URN and/or a complete set of reference fields.

Derivation:

| *ReferenceType* (restriction) 
|    |image431|\ *ChildObjectReferenceType* (restriction) 
|          |image432|\ *ComponentListReferenceType* (restriction) 
|                |image433|\ GroupKeyDescriptorReferenceType

Content:

( (Ref, URN?) \| URN)

Element Documentation:

======== ========================== =============================================================================================================================================================================================================
**Name** **Type**                   **Documentation**
======== ========================== =============================================================================================================================================================================================================
Ref      GroupKeyDescriptorRe fType Ref is used to provide a complete set of reference fields. Derived reference types will restrict the RefType so that the content of the Ref element requires exactly what is needed for a complete reference.
URN      xs:anyURI                  URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
URN      xs:anyURI                  URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
======== ========================== =============================================================================================================================================================================================================

**GroupKeyDescriptorRefType: **\ GroupKeyDescriptorRefType contains a
reference to a group key descriptor within a data structure definition.

Derivation:

| *RefBaseType* (restriction) 
|    |image434|\ *ChildObjectRefBaseType* (restriction) 
|          |image435|\ *ComponentListRefBaseType* (restriction) 
|                |image436|\ GroupKeyDescriptorRefType

Attributes:

agencyID, maintainableParentID, maintainableParentVersion?, id, local?,
class?, package?

Content:

{Empty}

Attribute Documentation:

======================================== ================================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                                 **Type**                          **Documentation**
======================================== ================================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
agencyID                                 NestedNCNameIDType                The agencyID attribute identifies the maintenance agency for the object being referenced (agency-id in the URN structure). This is optional to allow for local references (where the other reference fields are inferred from another context), but all complete references will require this.
maintainableParentID                     IDType                            The maintainableParentID references the structure in which the component list being referenced is defined.
maintainableParentVersion (default: 1.0) VersionType                       The maintainableParentVersion attribute references the version of the structure in which the component list being referenced is defined. If not supplied, a default value of 1.0 is assumed.
id                                       IDType                            The id attribute identifies the object being referenced, and is therefore always required.
local (fixed: false)                     xs:boolean                        The local attribute indicates whether this set of reference fields is meant for local referencing, in which case some of the reference fields will be implied from another context. Concrete instances of this class will always fix this value to either true or false, depending on their intended usage. If the value is fixed to true, then the complete set of reference fields will be required and a URN can be fully composed from the values.
class (fixed: GroupDimensionDescriptor)  ComponentListTypeCod elistType    The class attribute indicates the class name of the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
package (fixed: datastructure)           StructurePackageType CodelistType The package attribute indicates the package name for the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
======================================== ================================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================

**LocalGroupKeyDescriptorReferenceType: **\ LocalGroupKeyDescriptorReferenceType
is a type for referencing a group key descriptor locally, where the
reference to the data structure definition which defines it is provided
in another context (for example the data structure definition in which
the reference occurs).

Derivation:

| *ReferenceType* (restriction) 
|    |image437|\ *LocalComponentListReferenceType* (restriction) 
|          |image438|\ LocalGroupKeyDescriptorReferenceType

Content:

Ref

Element Documentation:

======== =============================== =============================================================================================================================================================================================================
**Name** **Type**                        **Documentation**
======== =============================== =============================================================================================================================================================================================================
Ref      LocalGroupKeyDescrip torRefType Ref is used to provide a complete set of reference fields. Derived reference types will restrict the RefType so that the content of the Ref element requires exactly what is needed for a complete reference.
======== =============================== =============================================================================================================================================================================================================

**LocalGroupKeyDescriptorRefType: **\ LocalGroupKeyDescriptorRefType
contains a local reference to a group key descriptor.

Derivation:

| *RefBaseType* (restriction) 
|    |image439|\ *LocalIdentifiableRefBaseType* (restriction) 
|          |image440|\ *LocalComponentListRefBaseType* (restriction) 
|                |image441|\ LocalGroupKeyDescriptorRefType

Attributes:

id, local?, class?, package?

Content:

{Empty}

Attribute Documentation:

======================================= ================================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                                **Type**                          **Documentation**
======================================= ================================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
id                                      NestedIDType                      The id attribute identifies the object being referenced, and is therefore always required.
local (fixed: true)                     xs:boolean                        The local attribute indicates whether this set of reference fields is meant for local referencing, in which case some of the reference fields will be implied from another context. Concrete instances of this class will always fix this value to either true or false, depending on their intended usage. If the value is fixed to true, then the complete set of reference fields will be required and a URN can be fully composed from the values.
class (fixed: GroupDimensionDescriptor) ComponentListTypeCod elistType    The class attribute indicates the class name of the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
package (fixed: datastructure)          StructurePackageType CodelistType The package attribute indicates the package name for the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
======================================= ================================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================

**DimensionReferenceType: **\ DimensionReferenceType is a type for
referencing a dimension object. It consists of a URN and/or a complete
set of reference fields.

Derivation:

| *ReferenceType* (restriction) 
|    |image442|\ *ContainerChildObjectReferenceType* (restriction) 
|          |image443|\ *ComponentReferenceType* (restriction) 
|                |image444|\ DimensionReferenceType

Content:

( (Ref, URN?) \| URN)

Element Documentation:

======== ================ =============================================================================================================================================================================================================
**Name** **Type**         **Documentation**
======== ================ =============================================================================================================================================================================================================
Ref      DimensionRefType Ref is used to provide a complete set of reference fields. Derived reference types will restrict the RefType so that the content of the Ref element requires exactly what is needed for a complete reference.
URN      xs:anyURI        URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
URN      xs:anyURI        URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
======== ================ =============================================================================================================================================================================================================

**DimensionRefType: **\ DimensionRefType contains a reference to a
dimension within a data structure definition. Note that since there is
only one key descriptor, the container reference fields are prohibited.

Derivation:

| *RefBaseType* (restriction) 
|    |image445|\ *ContainerChildObjectRefBaseType* (restriction) 
|          |image446|\ *ComponentRefBaseType* (restriction) 
|                |image447|\ DimensionRefType

Attributes:

agencyID, maintainableParentID, maintainableParentVersion?, id,
version?, local?, class?, package?

Content:

{Empty}

Attribute Documentation:

======================================== ================================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                                 **Type**                          **Documentation**
======================================== ================================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
agencyID                                 NestedNCNameIDType                The agencyID attribute identifies the maintenance agency for the object being referenced (agency-id in the URN structure). This is optional to allow for local references (where the other reference fields are inferred from another context), but all complete references will require this.
maintainableParentID                     IDType                            The maintainableParentID references the structure in which the component being referenced is defined.
maintainableParentVersion (default: 1.0) VersionType                       The maintainableParentVersion attribute references the version of the structure in which the component being referenced is defined. If not supplied, a default value of 1.0 is assumed.
id                                       IDType                            The id attribute identifies the object being referenced, and is therefore always required.
version                                  VersionType                       The version attribute identifies the version of the object being reference, if applicable. If this is available, a default value of 1.0 will always apply.
local (fixed: false)                     xs:boolean                        The local attribute indicates whether this set of reference fields is meant for local referencing, in which case some of the reference fields will be implied from another context. Concrete instances of this class will always fix this value to either true or false, depending on their intended usage. If the value is fixed to true, then the complete set of reference fields will be required and a URN can be fully composed from the values.
class (fixed: Dimension)                 DimensionTypeCodelis tType        The class attribute indicates the class name of the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
package (fixed: datastructure)           StructurePackageType CodelistType The package attribute indicates the package name for the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
======================================== ================================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================

**MeasureDimensionReferenceType: **\ MeasureDimensionReferenceType is a
type for referencing a measure dimension object. It consists of a URN
and/or a complete set of reference fields.

Derivation:

| *ReferenceType* (restriction) 
|    |image448|\ *ContainerChildObjectReferenceType* (restriction) 
|          |image449|\ *ComponentReferenceType* (restriction) 
|                |image450|\ MeasureDimensionReferenceType

Content:

( (Ref, URN?) \| URN)

Element Documentation:

======== ======================== =============================================================================================================================================================================================================
**Name** **Type**                 **Documentation**
======== ======================== =============================================================================================================================================================================================================
Ref      MeasureDimensionRefT ype Ref is used to provide a complete set of reference fields. Derived reference types will restrict the RefType so that the content of the Ref element requires exactly what is needed for a complete reference.
URN      xs:anyURI                URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
URN      xs:anyURI                URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
======== ======================== =============================================================================================================================================================================================================

**MeasureDimensionRefType: **\ MeasureDimensionRefType contains a
reference to the measure dimension within a data structure definition.
Note that since there is only one key descriptor, the container
reference fields are prohibited.

Derivation:

| *RefBaseType* (restriction) 
|    |image451|\ *ContainerChildObjectRefBaseType* (restriction) 
|          |image452|\ *ComponentRefBaseType* (restriction) 
|                |image453|\ MeasureDimensionRefType

Attributes:

agencyID, maintainableParentID, maintainableParentVersion?, id,
version?, local?, class?, package?

Content:

{Empty}

Attribute Documentation:

======================================== ================================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                                 **Type**                          **Documentation**
======================================== ================================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
agencyID                                 NestedNCNameIDType                The agencyID attribute identifies the maintenance agency for the object being referenced (agency-id in the URN structure). This is optional to allow for local references (where the other reference fields are inferred from another context), but all complete references will require this.
maintainableParentID                     IDType                            The maintainableParentID references the structure in which the component being referenced is defined.
maintainableParentVersion (default: 1.0) VersionType                       The maintainableParentVersion attribute references the version of the structure in which the component being referenced is defined. If not supplied, a default value of 1.0 is assumed.
id                                       IDType                            The id attribute identifies the object being referenced, and is therefore always required.
version                                  VersionType                       The version attribute identifies the version of the object being reference, if applicable. If this is available, a default value of 1.0 will always apply.
local (fixed: false)                     xs:boolean                        The local attribute indicates whether this set of reference fields is meant for local referencing, in which case some of the reference fields will be implied from another context. Concrete instances of this class will always fix this value to either true or false, depending on their intended usage. If the value is fixed to true, then the complete set of reference fields will be required and a URN can be fully composed from the values.
class (fixed: MeasureDimension)          DimensionTypeCodelis tType        The class attribute indicates the class name of the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
package (fixed: datastructure)           StructurePackageType CodelistType The package attribute indicates the package name for the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
======================================== ================================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================

**TimeDimensionReferenceType: **\ TimeDimensionReferenceType is a type
for referencing a time dimension object. It consists of a URN and/or a
complete set of reference fields.

Derivation:

| *ReferenceType* (restriction) 
|    |image454|\ *ContainerChildObjectReferenceType* (restriction) 
|          |image455|\ *ComponentReferenceType* (restriction) 
|                |image456|\ TimeDimensionReferenceType

Content:

( (Ref, URN?) \| URN)

Element Documentation:

======== ==================== =============================================================================================================================================================================================================
**Name** **Type**             **Documentation**
======== ==================== =============================================================================================================================================================================================================
Ref      TimeDimensionRefType Ref is used to provide a complete set of reference fields. Derived reference types will restrict the RefType so that the content of the Ref element requires exactly what is needed for a complete reference.
URN      xs:anyURI            URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
URN      xs:anyURI            URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
======== ==================== =============================================================================================================================================================================================================

**TimeDimensionRefType: **\ TimeDimensionRefType contains a reference to
the time dimension within a data structure definition. Note that since
there is only one key descriptor, the container reference fields are
prohibited.

Derivation:

| *RefBaseType* (restriction) 
|    |image457|\ *ContainerChildObjectRefBaseType* (restriction) 
|          |image458|\ *ComponentRefBaseType* (restriction) 
|                |image459|\ TimeDimensionRefType

Attributes:

agencyID, maintainableParentID, maintainableParentVersion?, id,
version?, local?, class?, package?

Content:

{Empty}

Attribute Documentation:

======================================== ================================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                                 **Type**                          **Documentation**
======================================== ================================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
agencyID                                 NestedNCNameIDType                The agencyID attribute identifies the maintenance agency for the object being referenced (agency-id in the URN structure). This is optional to allow for local references (where the other reference fields are inferred from another context), but all complete references will require this.
maintainableParentID                     IDType                            The maintainableParentID references the structure in which the component being referenced is defined.
maintainableParentVersion (default: 1.0) VersionType                       The maintainableParentVersion attribute references the version of the structure in which the component being referenced is defined. If not supplied, a default value of 1.0 is assumed.
id (fixed: TIME_PERIOD)                  IDType                            The id attribute identifies the object being referenced, and is therefore always required.
version                                  VersionType                       The version attribute identifies the version of the object being reference, if applicable. If this is available, a default value of 1.0 will always apply.
local (fixed: false)                     xs:boolean                        The local attribute indicates whether this set of reference fields is meant for local referencing, in which case some of the reference fields will be implied from another context. Concrete instances of this class will always fix this value to either true or false, depending on their intended usage. If the value is fixed to true, then the complete set of reference fields will be required and a URN can be fully composed from the values.
class (fixed: TimeDimension)             DimensionTypeCodelis tType        The class attribute indicates the class name of the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
package (fixed: datastructure)           StructurePackageType CodelistType The package attribute indicates the package name for the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
======================================== ================================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================

**LocalDimensionReferenceType: **\ LocalDimensionReferenceType is a type
for referencing any type of dimension locally, where the reference to
the data structure definition which defines the dimension is provided in
another context (for example the data structure definition in which the
reference occurs).

Derivation:

| *ReferenceType* (restriction) 
|    |image460|\ *LocalComponentListComponentReferenceBaseType*\ (restriction) 
|          |image461|\ *LocalComponentReferenceBaseType* (restriction) 
|                |image462|\ LocalDimensionReferenceType

Content:

Ref

Element Documentation:

======== ====================== =============================================================================================================================================================================================================
**Name** **Type**               **Documentation**
======== ====================== =============================================================================================================================================================================================================
Ref      LocalDimensionRefTyp e Ref is used to provide a complete set of reference fields. Derived reference types will restrict the RefType so that the content of the Ref element requires exactly what is needed for a complete reference.
======== ====================== =============================================================================================================================================================================================================

**LocalDimensionRefType: **\ LocalDimensionRefType contains the
reference fields for referencing a dimension locally.

Derivation:

| *RefBaseType* (restriction) 
|    |image463|\ *LocalIdentifiableRefBaseType* (restriction) 
|          |image464|\ *LocalComponentListComponentRefBaseType* (restriction) 
|                |image465|\ *LocalComponentRefBaseType* (restriction) 
|                      |image466|\ LocalDimensionRefType

Attributes:

id, local?, class?, package?

Content:

{Empty}

Attribute Documentation:

============================== ================================= ===========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                       **Type**                          **Documentation**
============================== ================================= ===========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
id                             IDType                            The id attribute identifies the object being referenced, and is therefore always required.
local (fixed: true)            xs:boolean                        The local attribute indicates whether this set of reference fields is meant for local referencing, in which case some of the reference fields will be implied from another context. Concrete instances of this class will always fix this value to either true or false, depending on their intended usage. If the value is fixed to true, then the complete set of reference fields will be required and a URN can be fully composed from the values.
class (default: Dimension)     DimensionTypeCodelis tType        The class attribute is optional and provided a default value of Dimension. It is strongly recommended that if the time or measure dimension is referenced, that the proper value be set for this field. However, this is not absolutely necessary since all data structure definition components must have a unique identifier within the scope of the entire data structure. It does, however, allow systems which will treat such a reference as a URN to easily construct the URN without having to verify the object class of the referenced dimension.
package (fixed: datastructure) StructurePackageType CodelistType The package attribute indicates the package name for the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
============================== ================================= ===========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================

**AttributeReferenceType: **\ AttributeReferenceType is a type for
referencing an attribute object. It consists of a URN and/or a complete
set of reference fields.

Derivation:

| *ReferenceType* (restriction) 
|    |image467|\ *ContainerChildObjectReferenceType* (restriction) 
|          |image468|\ *ComponentReferenceType* (restriction) 
|                |image469|\ AttributeReferenceType

Content:

( (Ref, URN?) \| URN)

Element Documentation:

======== ================ =============================================================================================================================================================================================================
**Name** **Type**         **Documentation**
======== ================ =============================================================================================================================================================================================================
Ref      AttributeRefType Ref is used to provide a complete set of reference fields. Derived reference types will restrict the RefType so that the content of the Ref element requires exactly what is needed for a complete reference.
URN      xs:anyURI        URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
URN      xs:anyURI        URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
======== ================ =============================================================================================================================================================================================================

**AttributeRefType: **\ AttributeRefType contains a reference to an
attribute within a data structure definition. Note that since there is
only one attribute descriptor, the container reference fields are
prohibited.

Derivation:

| *RefBaseType* (restriction) 
|    |image470|\ *ContainerChildObjectRefBaseType* (restriction) 
|          |image471|\ *ComponentRefBaseType* (restriction) 
|                |image472|\ AttributeRefType

Attributes:

agencyID, maintainableParentID, maintainableParentVersion?, id,
version?, local?, class?, package?

Content:

{Empty}

Attribute Documentation:

======================================== ================================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                                 **Type**                          **Documentation**
======================================== ================================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
agencyID                                 NestedNCNameIDType                The agencyID attribute identifies the maintenance agency for the object being referenced (agency-id in the URN structure). This is optional to allow for local references (where the other reference fields are inferred from another context), but all complete references will require this.
maintainableParentID                     IDType                            The maintainableParentID references the structure in which the component being referenced is defined.
maintainableParentVersion (default: 1.0) VersionType                       The maintainableParentVersion attribute references the version of the structure in which the component being referenced is defined. If not supplied, a default value of 1.0 is assumed.
id                                       IDType                            The id attribute identifies the object being referenced, and is therefore always required.
version                                  VersionType                       The version attribute identifies the version of the object being reference, if applicable. If this is available, a default value of 1.0 will always apply.
local (fixed: false)                     xs:boolean                        The local attribute indicates whether this set of reference fields is meant for local referencing, in which case some of the reference fields will be implied from another context. Concrete instances of this class will always fix this value to either true or false, depending on their intended usage. If the value is fixed to true, then the complete set of reference fields will be required and a URN can be fully composed from the values.
class (fixed: Attribute)                 ComponentTypeCodelis tType        The class attribute indicates the class name of the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
package (fixed: datastructure)           StructurePackageType CodelistType The package attribute indicates the package name for the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
======================================== ================================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================

**PrimaryMeasureReferenceType: **\ PrimaryMeasureReferenceType is a type
for referencing a primary measure object. It consists of a URN and/or a
complete set of reference fields.

Derivation:

| *ReferenceType* (restriction) 
|    |image473|\ *ContainerChildObjectReferenceType* (restriction) 
|          |image474|\ *ComponentReferenceType* (restriction) 
|                |image475|\ PrimaryMeasureReferenceType

Content:

( (Ref, URN?) \| URN)

Element Documentation:

======== ====================== =============================================================================================================================================================================================================
**Name** **Type**               **Documentation**
======== ====================== =============================================================================================================================================================================================================
Ref      PrimaryMeasureRefTyp e Ref is used to provide a complete set of reference fields. Derived reference types will restrict the RefType so that the content of the Ref element requires exactly what is needed for a complete reference.
URN      xs:anyURI              URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
URN      xs:anyURI              URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
======== ====================== =============================================================================================================================================================================================================

**PrimaryMeasureRefType: **\ PrimaryMeasureRefType contains a reference
to the primary measure within a data structure definition. Note that
since there is only one key descriptor, the container reference fields
are prohibited.

Derivation:

| *RefBaseType* (restriction) 
|    |image476|\ *ContainerChildObjectRefBaseType* (restriction) 
|          |image477|\ *ComponentRefBaseType* (restriction) 
|                |image478|\ PrimaryMeasureRefType

Attributes:

agencyID, maintainableParentID, maintainableParentVersion?, id,
version?, local?, class?, package?

Content:

{Empty}

Attribute Documentation:

======================================== ================================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                                 **Type**                          **Documentation**
======================================== ================================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
agencyID                                 NestedNCNameIDType                The agencyID attribute identifies the maintenance agency for the object being referenced (agency-id in the URN structure). This is optional to allow for local references (where the other reference fields are inferred from another context), but all complete references will require this.
maintainableParentID                     IDType                            The maintainableParentID references the structure in which the component being referenced is defined.
maintainableParentVersion (default: 1.0) VersionType                       The maintainableParentVersion attribute references the version of the structure in which the component being referenced is defined. If not supplied, a default value of 1.0 is assumed.
id (fixed: OBS_VALUE)                    IDType                            The id attribute identifies the object being referenced, and is therefore always required.
version                                  VersionType                       The version attribute identifies the version of the object being reference, if applicable. If this is available, a default value of 1.0 will always apply.
local (fixed: false)                     xs:boolean                        The local attribute indicates whether this set of reference fields is meant for local referencing, in which case some of the reference fields will be implied from another context. Concrete instances of this class will always fix this value to either true or false, depending on their intended usage. If the value is fixed to true, then the complete set of reference fields will be required and a URN can be fully composed from the values.
class (fixed: PrimaryMeasure)            ComponentTypeCodelis tType        The class attribute indicates the class name of the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
package (fixed: datastructure)           StructurePackageType CodelistType The package attribute indicates the package name for the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
======================================== ================================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================

**LocalPrimaryMeasureReferenceType: **\ LocalPrimaryMeasureReferenceType
is a type for referencing a primary measure locally, where the reference
to the data structure definition which defines the primary measure is
provided in another context (for example the data structure definition
in which the reference occurs).

Derivation:

| *ReferenceType* (restriction) 
|    |image479|\ *LocalComponentListComponentReferenceBaseType*\ (restriction) 
|          |image480|\ *LocalComponentReferenceBaseType* (restriction) 
|                |image481|\ LocalPrimaryMeasureReferenceType

Content:

Ref

Element Documentation:

======== =========================== =============================================================================================================================================================================================================
**Name** **Type**                    **Documentation**
======== =========================== =============================================================================================================================================================================================================
Ref      LocalPrimaryMeasureR efType Ref is used to provide a complete set of reference fields. Derived reference types will restrict the RefType so that the content of the Ref element requires exactly what is needed for a complete reference.
======== =========================== =============================================================================================================================================================================================================

**LocalPrimaryMeasureRefType: **\ LocalPrimaryMeasureRefType contains
the reference fields for referencing a primary measure locally.

Derivation:

| *RefBaseType* (restriction) 
|    |image482|\ *LocalIdentifiableRefBaseType* (restriction) 
|          |image483|\ *LocalComponentListComponentRefBaseType* (restriction) 
|                |image484|\ *LocalComponentRefBaseType* (restriction) 
|                      |image485|\ LocalPrimaryMeasureRefType

Attributes:

id, local?, class?, package?

Content:

{Empty}

Attribute Documentation:

============================== ================================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                       **Type**                          **Documentation**
============================== ================================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
id (fixed: OBS_VALUE)          IDType                            The id attribute identifies the object being referenced, and is therefore always required.
local (fixed: true)            xs:boolean                        The local attribute indicates whether this set of reference fields is meant for local referencing, in which case some of the reference fields will be implied from another context. Concrete instances of this class will always fix this value to either true or false, depending on their intended usage. If the value is fixed to true, then the complete set of reference fields will be required and a URN can be fully composed from the values.
class (fixed: PrimaryMeasure)  ComponentTypeCodelis tType        The class attribute indicates the class name of the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
package (fixed: datastructure) StructurePackageType CodelistType The package attribute indicates the package name for the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
============================== ================================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================

**LocalDataStructureComponentReferenceType: **\ LocalDataStructureComponentReferenceType
is a type for referencing any type of data structure component locally,
where the reference for the data structure definition which defines the
components is available in another context.

Derivation:

| *ReferenceType* (restriction) 
|    |image486|\ *LocalComponentListComponentReferenceBaseType*\ (restriction) 
|          |image487|\ LocalDataStructureComponentReferenceType

Content:

Ref

Element Documentation:

======== =================================== =============================================================================================================================================================================================================
**Name** **Type**                            **Documentation**
======== =================================== =============================================================================================================================================================================================================
Ref      LocalDataStructureCo mponentRefType Ref is used to provide a complete set of reference fields. Derived reference types will restrict the RefType so that the content of the Ref element requires exactly what is needed for a complete reference.
======== =================================== =============================================================================================================================================================================================================

**LocalDataStructureComponentRefType: **\ LocalDataStructureComponentRefType
contains the reference fields for referencing any data structure
component locally. This reference must specify the class of the
component being referenced.

Derivation:

| *RefBaseType* (restriction) 
|    |image488|\ *LocalIdentifiableRefBaseType* (restriction) 
|          |image489|\ *LocalComponentListComponentRefBaseType* (restriction) 
|                |image490|\ LocalDataStructureComponentRefType

Attributes:

id, local?, class, package?

Content:

{Empty}

Attribute Documentation:

============================== ======================================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                       **Type**                                **Documentation**
============================== ======================================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
id                             IDType                                  The id attribute identifies the object being referenced, and is therefore always required.
local (fixed: true)            xs:boolean                              The local attribute indicates whether this set of reference fields is meant for local referencing, in which case some of the reference fields will be implied from another context. Concrete instances of this class will always fix this value to either true or false, depending on their intended usage. If the value is fixed to true, then the complete set of reference fields will be required and a URN can be fully composed from the values.
class                          DataStructureCompone ntTypeCodelistType The class attribute indicates the class name of the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
package (fixed: datastructure) StructurePackageType CodelistType       The package attribute indicates the package name for the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
============================== ======================================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================

**DataStructureEnumerationSchemeReferenceType: **\ DataStructureEnumerationSchemeReferenceType
is a type for referencing any type of item scheme that is allowable as
the enumeration of the representation of a data structure definition
component. It consists of a URN and/or a complete set of reference
fields.

Derivation:

| *ReferenceType* (restriction) 
|    |image491|\ *MaintainableReferenceBaseType* (restriction) 
|          |image492|\ *ItemSchemeReferenceBaseType* (restriction) 
|                |image493|\ ItemSchemeReferenceType (restriction) 
|                      |image494|\ DataStructureEnumerationSchemeReferenceType

Content:

( (Ref, URN?) \| URN)

Element Documentation:

======== ====================================== =============================================================================================================================================================================================================
**Name** **Type**                               **Documentation**
======== ====================================== =============================================================================================================================================================================================================
Ref      DataStructureEnumera tionSchemeRefType Ref is used to provide a complete set of reference fields. Derived reference types will restrict the RefType so that the content of the Ref element requires exactly what is needed for a complete reference.
URN      xs:anyURI                              URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
URN      xs:anyURI                              URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
======== ====================================== =============================================================================================================================================================================================================

**DataStructureEnumerationSchemeRefType: **\ DataStructureEnumerationSchemeRefType
contains the reference fields for referencing any item scheme that is
allowable as the enumeration of the representation of a data structure
definition component.

Derivation:

| *RefBaseType* (restriction) 
|    |image495|\ *MaintainableRefBaseType* (restriction) 
|          |image496|\ *ItemSchemeRefBaseType* (restriction) 
|                |image497|\ ItemSchemeRefType (restriction) 
|                      |image498|\ DataStructureEnumerationSchemeRefType

Attributes:

agencyID, id, version?, local?, class, package

Content:

{Empty}

Attribute Documentation:

====================== =========================================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**               **Type**                                    **Documentation**
====================== =========================================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
agencyID               NestedNCNameIDType                          The agencyID attribute identifies the maintenance agency for the object being referenced (agency-id in the URN structure). This is optional to allow for local references (where the other reference fields are inferred from another context), but all complete references will require this.
id                     IDType                                      The id attribute identifies the object being referenced, and is therefore always required.
version (default: 1.0) VersionType                                 The version attribute identifies the version of the object being reference, if applicable. If this is available, a default value of 1.0 will always apply.
local (fixed: false)   xs:boolean                                  The local attribute indicates whether this set of reference fields is meant for local referencing, in which case some of the reference fields will be implied from another context. Concrete instances of this class will always fix this value to either true or false, depending on their intended usage. If the value is fixed to true, then the complete set of reference fields will be required and a URN can be fully composed from the values.
class                  DimensionEumerationS chemeTypeCodelistTyp e The class attribute indicates the class name of the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
package                ItemSchemePackageTyp eCodelistType          The package attribute indicates the package name for the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
====================== =========================================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================

**MetadataStructureReferenceType: **\ MetadataStructureReferenceType is
a type for referencing a metadata structure definition object. It
consists of a URN and/or a complete set of reference fields.

Derivation:

| *ReferenceType* (restriction) 
|    |image499|\ *MaintainableReferenceBaseType* (restriction) 
|          |image500|\ *StructureReferenceBaseType* (restriction) 
|                |image501|\ MetadataStructureReferenceType

Content:

( (Ref, URN?) \| URN)

Element Documentation:

======== ========================= =============================================================================================================================================================================================================
**Name** **Type**                  **Documentation**
======== ========================= =============================================================================================================================================================================================================
Ref      MetadataStructureRef Type Ref is used to provide a complete set of reference fields. Derived reference types will restrict the RefType so that the content of the Ref element requires exactly what is needed for a complete reference.
URN      xs:anyURI                 URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
URN      xs:anyURI                 URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
======== ========================= =============================================================================================================================================================================================================

**MetadataStructureRefType: **\ MetadataStructureRefType contains a set
of reference fields for a metadata structure definition.

Derivation:

| *RefBaseType* (restriction) 
|    |image502|\ *MaintainableRefBaseType* (restriction) 
|          |image503|\ *StructureOrUsageRefBaseType* (restriction) 
|                |image504|\ *StructureRefBaseType* (restriction) 
|                      |image505|\ MetadataStructureRefType

Attributes:

agencyID, id, version?, local?, class?, package?

Content:

{Empty}

Attribute Documentation:

================================== ================================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                           **Type**                          **Documentation**
================================== ================================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
agencyID                           NestedNCNameIDType                The agencyID attribute identifies the maintenance agency for the object being referenced (agency-id in the URN structure). This is optional to allow for local references (where the other reference fields are inferred from another context), but all complete references will require this.
id                                 IDType                            The id attribute identifies the object being referenced, and is therefore always required.
version (default: 1.0)             VersionType                       The version attribute identifies the version of the object being reference, if applicable. If this is available, a default value of 1.0 will always apply.
local (fixed: false)               xs:boolean                        The local attribute indicates whether this set of reference fields is meant for local referencing, in which case some of the reference fields will be implied from another context. Concrete instances of this class will always fix this value to either true or false, depending on their intended usage. If the value is fixed to true, then the complete set of reference fields will be required and a URN can be fully composed from the values.
class (fixed: MetadataStructure)   StructureTypeCodelis tType        The class attribute indicates the class name of the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
package (fixed: metadatastructure) StructurePackageType CodelistType The package attribute indicates the package name for the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
================================== ================================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================

**MetadataTargetReferenceType: **\ MetadataTargetReferenceType is a type
for referencing a metadata target object. It consists of a URN and/or a
complete set of reference fields.

Derivation:

| *ReferenceType* (restriction) 
|    |image506|\ *ChildObjectReferenceType* (restriction) 
|          |image507|\ *ComponentListReferenceType* (restriction) 
|                |image508|\ MetadataTargetReferenceType

Content:

( (Ref, URN?) \| URN)

Element Documentation:

======== ====================== =============================================================================================================================================================================================================
**Name** **Type**               **Documentation**
======== ====================== =============================================================================================================================================================================================================
Ref      MetadataTargetRefTyp e Ref is used to provide a complete set of reference fields. Derived reference types will restrict the RefType so that the content of the Ref element requires exactly what is needed for a complete reference.
URN      xs:anyURI              URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
URN      xs:anyURI              URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
======== ====================== =============================================================================================================================================================================================================

**MetadataTargetRefType: **\ MetadataTargetRefType contains a reference
to a metadata target within a metadata structure definition.

Derivation:

| *RefBaseType* (restriction) 
|    |image509|\ *ChildObjectRefBaseType* (restriction) 
|          |image510|\ *ComponentListRefBaseType* (restriction) 
|                |image511|\ MetadataTargetRefType

Attributes:

agencyID, maintainableParentID, maintainableParentVersion?, id, local?,
class?, package?

Content:

{Empty}

Attribute Documentation:

======================================== ================================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                                 **Type**                          **Documentation**
======================================== ================================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
agencyID                                 NestedNCNameIDType                The agencyID attribute identifies the maintenance agency for the object being referenced (agency-id in the URN structure). This is optional to allow for local references (where the other reference fields are inferred from another context), but all complete references will require this.
maintainableParentID                     IDType                            The maintainableParentID references the structure in which the component list being referenced is defined.
maintainableParentVersion (default: 1.0) VersionType                       The maintainableParentVersion attribute references the version of the structure in which the component list being referenced is defined. If not supplied, a default value of 1.0 is assumed.
id                                       IDType                            The id attribute identifies the object being referenced, and is therefore always required.
local (fixed: false)                     xs:boolean                        The local attribute indicates whether this set of reference fields is meant for local referencing, in which case some of the reference fields will be implied from another context. Concrete instances of this class will always fix this value to either true or false, depending on their intended usage. If the value is fixed to true, then the complete set of reference fields will be required and a URN can be fully composed from the values.
class (fixed: MetadataTarget)            ComponentListTypeCod elistType    The class attribute indicates the class name of the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
package (fixed: metadatastructure)       StructurePackageType CodelistType The package attribute indicates the package name for the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
======================================== ================================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================

**LocalMetadataTargetReferenceType: **\ LocalMetadataTargetReferenceType
is a type for referencing a metadata target locally, where the reference
to the metadata structure definition which defines it is provided in
another context (for example the metadata structure definition in which
the reference occurs).

Derivation:

| *ReferenceType* (restriction) 
|    |image512|\ *LocalComponentListReferenceType* (restriction) 
|          |image513|\ LocalMetadataTargetReferenceType

Content:

Ref

Element Documentation:

======== =========================== =============================================================================================================================================================================================================
**Name** **Type**                    **Documentation**
======== =========================== =============================================================================================================================================================================================================
Ref      LocalMetadataTargetR efType Ref is used to provide a complete set of reference fields. Derived reference types will restrict the RefType so that the content of the Ref element requires exactly what is needed for a complete reference.
======== =========================== =============================================================================================================================================================================================================

**LocalMetadataTargetRefType: **\ LocalMetadataTargetRefType contains a
local reference to a metadata target object.

Derivation:

| *RefBaseType* (restriction) 
|    |image514|\ *LocalIdentifiableRefBaseType* (restriction) 
|          |image515|\ *LocalComponentListRefBaseType* (restriction) 
|                |image516|\ LocalMetadataTargetRefType

Attributes:

id, local?, class?, package?

Content:

{Empty}

Attribute Documentation:

================================== ================================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                           **Type**                          **Documentation**
================================== ================================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
id                                 NestedIDType                      The id attribute identifies the object being referenced, and is therefore always required.
local (fixed: true)                xs:boolean                        The local attribute indicates whether this set of reference fields is meant for local referencing, in which case some of the reference fields will be implied from another context. Concrete instances of this class will always fix this value to either true or false, depending on their intended usage. If the value is fixed to true, then the complete set of reference fields will be required and a URN can be fully composed from the values.
class (fixed: MetadataTarget)      ComponentListTypeCod elistType    The class attribute indicates the class name of the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
package (fixed: metadatastructure) StructurePackageType CodelistType The package attribute indicates the package name for the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
================================== ================================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================

**ConstraintTargetReferenceType: **\ ConstraintTargetReferenceType is a
type for referencing a constraint target object. It consists of a URN
and/or a complete set of reference fields.

Derivation:

| *ReferenceType* (restriction) 
|    |image517|\ *ContainerChildObjectReferenceType* (restriction) 
|          |image518|\ *ComponentReferenceType* (restriction) 
|                |image519|\ ConstraintTargetReferenceType

Content:

( (Ref, URN?) \| URN)

Element Documentation:

======== ======================== =============================================================================================================================================================================================================
**Name** **Type**                 **Documentation**
======== ======================== =============================================================================================================================================================================================================
Ref      ConstraintTargetRefT ype Ref is used to provide a complete set of reference fields. Derived reference types will restrict the RefType so that the content of the Ref element requires exactly what is needed for a complete reference.
URN      xs:anyURI                URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
URN      xs:anyURI                URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
======== ======================== =============================================================================================================================================================================================================

**ConstraintTargetRefType: **\ ConstraintTargetRefType contains a
reference to a constraint target within a metadata target of a data
structure definition.

Derivation:

| *RefBaseType* (restriction) 
|    |image520|\ *ContainerChildObjectRefBaseType* (restriction) 
|          |image521|\ *ComponentRefBaseType* (restriction) 
|                |image522|\ ConstraintTargetRefType

Attributes:

agencyID, maintainableParentID, maintainableParentVersion?, containerID,
id, version?, local?, class?, package?

Content:

{Empty}

Attribute Documentation:

======================================== ================================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                                 **Type**                          **Documentation**
======================================== ================================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
agencyID                                 NestedNCNameIDType                The agencyID attribute identifies the maintenance agency for the object being referenced (agency-id in the URN structure). This is optional to allow for local references (where the other reference fields are inferred from another context), but all complete references will require this.
maintainableParentID                     IDType                            The maintainableParentID references the structure in which the component being referenced is defined.
maintainableParentVersion (default: 1.0) VersionType                       The maintainableParentVersion attribute references the version of the structure in which the component being referenced is defined. If not supplied, a default value of 1.0 is assumed.
containerID                              IDType                            The containerID attribute references the component list of that contains the component being referenced. It is optional for the cases where the component list has a fixed identifier. Specific implementations of this will prohibit or require this accordingly.
id (fixed: CONSTRAINT_TARGET)            IDType                            The id attribute identifies the object being referenced, and is therefore always required.
version                                  VersionType                       The version attribute identifies the version of the object being reference, if applicable. If this is available, a default value of 1.0 will always apply.
local (fixed: false)                     xs:boolean                        The local attribute indicates whether this set of reference fields is meant for local referencing, in which case some of the reference fields will be implied from another context. Concrete instances of this class will always fix this value to either true or false, depending on their intended usage. If the value is fixed to true, then the complete set of reference fields will be required and a URN can be fully composed from the values.
class (fixed: ConstraintTarget)          ComponentTypeCodelis tType        The class attribute indicates the class name of the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
package (fixed: metadatastructure)       StructurePackageType CodelistType The package attribute indicates the package name for the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
======================================== ================================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================

**DataSetTargetReferenceType: **\ DataSetTargetReferenceType is a type
for referencing a data set target object. It consists of a URN and/or a
complete set of reference fields.

Derivation:

| *ReferenceType* (restriction) 
|    |image523|\ *ContainerChildObjectReferenceType* (restriction) 
|          |image524|\ *ComponentReferenceType* (restriction) 
|                |image525|\ DataSetTargetReferenceType

Content:

( (Ref, URN?) \| URN)

Element Documentation:

======== ==================== =============================================================================================================================================================================================================
**Name** **Type**             **Documentation**
======== ==================== =============================================================================================================================================================================================================
Ref      DataSetTargetRefType Ref is used to provide a complete set of reference fields. Derived reference types will restrict the RefType so that the content of the Ref element requires exactly what is needed for a complete reference.
URN      xs:anyURI            URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
URN      xs:anyURI            URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
======== ==================== =============================================================================================================================================================================================================

**DataSetTargetRefType: **\ DataSetTargetRefType contains a reference to
a data set target within a metadata target of a data structure
definition.

Derivation:

| *RefBaseType* (restriction) 
|    |image526|\ *ContainerChildObjectRefBaseType* (restriction) 
|          |image527|\ *ComponentRefBaseType* (restriction) 
|                |image528|\ DataSetTargetRefType

Attributes:

agencyID, maintainableParentID, maintainableParentVersion?, containerID,
id, version?, local?, class?, package?

Content:

{Empty}

Attribute Documentation:

======================================== ================================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                                 **Type**                          **Documentation**
======================================== ================================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
agencyID                                 NestedNCNameIDType                The agencyID attribute identifies the maintenance agency for the object being referenced (agency-id in the URN structure). This is optional to allow for local references (where the other reference fields are inferred from another context), but all complete references will require this.
maintainableParentID                     IDType                            The maintainableParentID references the structure in which the component being referenced is defined.
maintainableParentVersion (default: 1.0) VersionType                       The maintainableParentVersion attribute references the version of the structure in which the component being referenced is defined. If not supplied, a default value of 1.0 is assumed.
containerID                              IDType                            The containerID attribute references the component list of that contains the component being referenced. It is optional for the cases where the component list has a fixed identifier. Specific implementations of this will prohibit or require this accordingly.
id (fixed: DATA_SET_TARGET)              IDType                            The id attribute identifies the object being referenced, and is therefore always required.
version                                  VersionType                       The version attribute identifies the version of the object being reference, if applicable. If this is available, a default value of 1.0 will always apply.
local (fixed: false)                     xs:boolean                        The local attribute indicates whether this set of reference fields is meant for local referencing, in which case some of the reference fields will be implied from another context. Concrete instances of this class will always fix this value to either true or false, depending on their intended usage. If the value is fixed to true, then the complete set of reference fields will be required and a URN can be fully composed from the values.
class (fixed: DataSetTarget)             ComponentTypeCodelis tType        The class attribute indicates the class name of the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
package (fixed: metadatastructure)       StructurePackageType CodelistType The package attribute indicates the package name for the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
======================================== ================================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================

**KeyDescriptorValuesTargetReferenceType: **\ KeyDescriptorValuesTargetType
is a type for referencing a key descriptor values target object. It
consists of a URN and/or a complete set of reference fields.

Derivation:

| *ReferenceType* (restriction) 
|    |image529|\ *ContainerChildObjectReferenceType* (restriction) 
|          |image530|\ *ComponentReferenceType* (restriction) 
|                |image531|\ KeyDescriptorValuesTargetReferenceType

Content:

( (Ref, URN?) \| URN)

Element Documentation:

======== ================================= =============================================================================================================================================================================================================
**Name** **Type**                          **Documentation**
======== ================================= =============================================================================================================================================================================================================
Ref      KeyDescriptorValuesT argetRefType Ref is used to provide a complete set of reference fields. Derived reference types will restrict the RefType so that the content of the Ref element requires exactly what is needed for a complete reference.
URN      xs:anyURI                         URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
URN      xs:anyURI                         URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
======== ================================= =============================================================================================================================================================================================================

**KeyDescriptorValuesTargetRefType: **\ KeyDescriptorValuesTargetRefType
contains a reference to a key descriptor values target within a metadata
target of a data structure definition.

Derivation:

| *RefBaseType* (restriction) 
|    |image532|\ *ContainerChildObjectRefBaseType* (restriction) 
|          |image533|\ *ComponentRefBaseType* (restriction) 
|                |image534|\ KeyDescriptorValuesTargetRefType

Attributes:

agencyID, maintainableParentID, maintainableParentVersion?, containerID,
id, version?, local?, class?, package?

Content:

{Empty}

Attribute Documentation:

============================================== ================================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                                       **Type**                          **Documentation**
============================================== ================================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
agencyID                                       NestedNCNameIDType                The agencyID attribute identifies the maintenance agency for the object being referenced (agency-id in the URN structure). This is optional to allow for local references (where the other reference fields are inferred from another context), but all complete references will require this.
maintainableParentID                           IDType                            The maintainableParentID references the structure in which the component being referenced is defined.
maintainableParentVersion (default: 1.0)       VersionType                       The maintainableParentVersion attribute references the version of the structure in which the component being referenced is defined. If not supplied, a default value of 1.0 is assumed.
containerID                                    IDType                            The containerID attribute references the component list of that contains the component being referenced. It is optional for the cases where the component list has a fixed identifier. Specific implementations of this will prohibit or require this accordingly.
id (fixed: DIMENSION_DESCRIPTOR_VALUES_TARGET) IDType                            The id attribute identifies the object being referenced, and is therefore always required.
version                                        VersionType                       The version attribute identifies the version of the object being reference, if applicable. If this is available, a default value of 1.0 will always apply.
local (fixed: false)                           xs:boolean                        The local attribute indicates whether this set of reference fields is meant for local referencing, in which case some of the reference fields will be implied from another context. Concrete instances of this class will always fix this value to either true or false, depending on their intended usage. If the value is fixed to true, then the complete set of reference fields will be required and a URN can be fully composed from the values.
class (fixed: DimensionDescriptorValuesTarget) ComponentTypeCodelis tType        The class attribute indicates the class name of the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
package (fixed: metadatastructure)             StructurePackageType CodelistType The package attribute indicates the package name for the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
============================================== ================================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================

**ReportPeriodTargetReferenceType: **\ ReportPeriodTargetReferenceType
is a type for referencing a report period target object. It consists of
a URN and/or a complete set of reference fields.

Derivation:

| *ReferenceType* (restriction) 
|    |image535|\ *ContainerChildObjectReferenceType* (restriction) 
|          |image536|\ *ComponentReferenceType* (restriction) 
|                |image537|\ ReportPeriodTargetReferenceType

Content:

( (Ref, URN?) \| URN)

Element Documentation:

======== ========================== =============================================================================================================================================================================================================
**Name** **Type**                   **Documentation**
======== ========================== =============================================================================================================================================================================================================
Ref      ReportPeriodTargetRe fType Ref is used to provide a complete set of reference fields. Derived reference types will restrict the RefType so that the content of the Ref element requires exactly what is needed for a complete reference.
URN      xs:anyURI                  URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
URN      xs:anyURI                  URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
======== ========================== =============================================================================================================================================================================================================

**ReportPeriodTargetRefType: **\ ReportPeriodTargetRefType contains a
reference to a report period target within a metadata target of a data
structure definition.

Derivation:

| *RefBaseType* (restriction) 
|    |image538|\ *ContainerChildObjectRefBaseType* (restriction) 
|          |image539|\ *ComponentRefBaseType* (restriction) 
|                |image540|\ ReportPeriodTargetRefType

Attributes:

agencyID, maintainableParentID, maintainableParentVersion?, containerID,
id, version?, local?, class?, package?

Content:

{Empty}

Attribute Documentation:

======================================== ================================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                                 **Type**                          **Documentation**
======================================== ================================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
agencyID                                 NestedNCNameIDType                The agencyID attribute identifies the maintenance agency for the object being referenced (agency-id in the URN structure). This is optional to allow for local references (where the other reference fields are inferred from another context), but all complete references will require this.
maintainableParentID                     IDType                            The maintainableParentID references the structure in which the component being referenced is defined.
maintainableParentVersion (default: 1.0) VersionType                       The maintainableParentVersion attribute references the version of the structure in which the component being referenced is defined. If not supplied, a default value of 1.0 is assumed.
containerID                              IDType                            The containerID attribute references the component list of that contains the component being referenced. It is optional for the cases where the component list has a fixed identifier. Specific implementations of this will prohibit or require this accordingly.
id (fixed: REPORT_PERIOD_TARGET)         IDType                            The id attribute identifies the object being referenced, and is therefore always required.
version                                  VersionType                       The version attribute identifies the version of the object being reference, if applicable. If this is available, a default value of 1.0 will always apply.
local (fixed: false)                     xs:boolean                        The local attribute indicates whether this set of reference fields is meant for local referencing, in which case some of the reference fields will be implied from another context. Concrete instances of this class will always fix this value to either true or false, depending on their intended usage. If the value is fixed to true, then the complete set of reference fields will be required and a URN can be fully composed from the values.
class (fixed: ReportPeriodTarget)        ComponentTypeCodelis tType        The class attribute indicates the class name of the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
package (fixed: metadatastructure)       StructurePackageType CodelistType The package attribute indicates the package name for the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
======================================== ================================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================

**IdentifiableObjectTargetReferenceType: **\ IdentifiableObjectTargetReferenceType
is a type for referencing an identifiable object target object. It
consists of a URN and/or a complete set of reference fields.

Derivation:

| *ReferenceType* (restriction) 
|    |image541|\ *ContainerChildObjectReferenceType* (restriction) 
|          |image542|\ *ComponentReferenceType* (restriction) 
|                |image543|\ IdentifiableObjectTargetReferenceType

Content:

( (Ref, URN?) \| URN)

Element Documentation:

======== ================================ =============================================================================================================================================================================================================
**Name** **Type**                         **Documentation**
======== ================================ =============================================================================================================================================================================================================
Ref      IdentifiableObjectTa rgetRefType Ref is used to provide a complete set of reference fields. Derived reference types will restrict the RefType so that the content of the Ref element requires exactly what is needed for a complete reference.
URN      xs:anyURI                        URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
URN      xs:anyURI                        URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
======== ================================ =============================================================================================================================================================================================================

**IdentifiableObjectTargetRefType: **\ IdentifiableObjectTargetRefType
contains a reference to an identifiable object target within a metadata
target of a data structure definition.

Derivation:

| *RefBaseType* (restriction) 
|    |image544|\ *ContainerChildObjectRefBaseType* (restriction) 
|          |image545|\ *ComponentRefBaseType* (restriction) 
|                |image546|\ IdentifiableObjectTargetRefType

Attributes:

agencyID, maintainableParentID, maintainableParentVersion?,
containerID?, id, version?, local?, class?, package?

Content:

{Empty}

Attribute Documentation:

======================================== ================================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                                 **Type**                          **Documentation**
======================================== ================================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
agencyID                                 NestedNCNameIDType                The agencyID attribute identifies the maintenance agency for the object being referenced (agency-id in the URN structure). This is optional to allow for local references (where the other reference fields are inferred from another context), but all complete references will require this.
maintainableParentID                     IDType                            The maintainableParentID references the structure in which the component being referenced is defined.
maintainableParentVersion (default: 1.0) VersionType                       The maintainableParentVersion attribute references the version of the structure in which the component being referenced is defined. If not supplied, a default value of 1.0 is assumed.
containerID                              NestedIDType                      The containerID attribute references the component list of that contains the component being referenced. It is optional for the cases where the component list has a fixed identifier. Specific implementations of this will prohibit or require this accordingly.
id                                       IDType                            The id attribute identifies the object being referenced, and is therefore always required.
version                                  VersionType                       The version attribute identifies the version of the object being reference, if applicable. If this is available, a default value of 1.0 will always apply.
local (fixed: false)                     xs:boolean                        The local attribute indicates whether this set of reference fields is meant for local referencing, in which case some of the reference fields will be implied from another context. Concrete instances of this class will always fix this value to either true or false, depending on their intended usage. If the value is fixed to true, then the complete set of reference fields will be required and a URN can be fully composed from the values.
class (fixed: IdentifiableObjectTarget)  ComponentTypeCodelis tType        The class attribute indicates the class name of the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
package (fixed: metadatastructure)       StructurePackageType CodelistType The package attribute indicates the package name for the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
======================================== ================================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================

**LocalTargetObjectReferenceType: **\ LocalTargetObjectReferenceType is
a type for referencing any type of target object within a metadata
target locally, where the references to the metadata target and the
metadata structure definition which defines the target reference are
provided in another context.

Derivation:

| *ReferenceType* (restriction) 
|    |image547|\ *LocalComponentListComponentReferenceBaseType*\ (restriction) 
|          |image548|\ *LocalComponentReferenceBaseType* (restriction) 
|                |image549|\ LocalTargetObjectReferenceType

Content:

Ref

Element Documentation:

======== ========================= =============================================================================================================================================================================================================
**Name** **Type**                  **Documentation**
======== ========================= =============================================================================================================================================================================================================
Ref      LocalTargetObjectRef Type Ref is used to provide a complete set of reference fields. Derived reference types will restrict the RefType so that the content of the Ref element requires exactly what is needed for a complete reference.
======== ========================= =============================================================================================================================================================================================================

**LocalTargetObjectRefType: **\ LocalTargetObjectRefType contains the
reference fields for referencing a target object locally.

Derivation:

| *RefBaseType* (restriction) 
|    |image550|\ *LocalIdentifiableRefBaseType* (restriction) 
|          |image551|\ *LocalComponentListComponentRefBaseType* (restriction) 
|                |image552|\ *LocalComponentRefBaseType* (restriction) 
|                      |image553|\ LocalTargetObjectRefType

Attributes:

id, local?, class, package?

Content:

{Empty}

Attribute Documentation:

================================== ================================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                           **Type**                          **Documentation**
================================== ================================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
id                                 NestedIDType                      The id attribute identifies the object being referenced, and is therefore always required.
local (fixed: true)                xs:boolean                        The local attribute indicates whether this set of reference fields is meant for local referencing, in which case some of the reference fields will be implied from another context. Concrete instances of this class will always fix this value to either true or false, depending on their intended usage. If the value is fixed to true, then the complete set of reference fields will be required and a URN can be fully composed from the values.
class                              TargetObjectTypeCode listType     The class attribute indicates the class name of the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
package (fixed: metadatastructure) StructurePackageType CodelistType The package attribute indicates the package name for the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
================================== ================================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================

**ReportStructureReferenceType: **\ ReportStructureReferenceType is a
type for referencing a report structure object. It consists of a URN
and/or a complete set of reference fields.

Derivation:

| *ReferenceType* (restriction) 
|    |image554|\ *ChildObjectReferenceType* (restriction) 
|          |image555|\ *ComponentListReferenceType* (restriction) 
|                |image556|\ ReportStructureReferenceType

Content:

( (Ref, URN?) \| URN)

Element Documentation:

======== ======================= =============================================================================================================================================================================================================
**Name** **Type**                **Documentation**
======== ======================= =============================================================================================================================================================================================================
Ref      ReportStructureRefTy pe Ref is used to provide a complete set of reference fields. Derived reference types will restrict the RefType so that the content of the Ref element requires exactly what is needed for a complete reference.
URN      xs:anyURI               URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
URN      xs:anyURI               URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
======== ======================= =============================================================================================================================================================================================================

**ReportStructureRefType: **\ ReportStructureRefType contains a
reference to a report structure within a metadata structure definition.

Derivation:

| *RefBaseType* (restriction) 
|    |image557|\ *ChildObjectRefBaseType* (restriction) 
|          |image558|\ *ComponentListRefBaseType* (restriction) 
|                |image559|\ ReportStructureRefType

Attributes:

agencyID, maintainableParentID, maintainableParentVersion?, id, local?,
class?, package?

Content:

{Empty}

Attribute Documentation:

======================================== ================================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                                 **Type**                          **Documentation**
======================================== ================================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
agencyID                                 NestedNCNameIDType                The agencyID attribute identifies the maintenance agency for the object being referenced (agency-id in the URN structure). This is optional to allow for local references (where the other reference fields are inferred from another context), but all complete references will require this.
maintainableParentID                     IDType                            The maintainableParentID references the structure in which the component list being referenced is defined.
maintainableParentVersion (default: 1.0) VersionType                       The maintainableParentVersion attribute references the version of the structure in which the component list being referenced is defined. If not supplied, a default value of 1.0 is assumed.
id                                       IDType                            The id attribute identifies the object being referenced, and is therefore always required.
local (fixed: false)                     xs:boolean                        The local attribute indicates whether this set of reference fields is meant for local referencing, in which case some of the reference fields will be implied from another context. Concrete instances of this class will always fix this value to either true or false, depending on their intended usage. If the value is fixed to true, then the complete set of reference fields will be required and a URN can be fully composed from the values.
class (fixed: ReportStructure)           ComponentListTypeCod elistType    The class attribute indicates the class name of the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
package (fixed: metadatastructure)       StructurePackageType CodelistType The package attribute indicates the package name for the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
======================================== ================================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================

**LocalReportStructureReferenceType: **\ LocalReportStructureReferenceType
is a type for referencing a report structure locally, where the
reference to the metadata structure definition which defines it is
provided in another context (for example the metadata structure
definition in which the reference occurs).

Derivation:

| *ReferenceType* (restriction) 
|    |image560|\ *LocalComponentListReferenceType* (restriction) 
|          |image561|\ LocalReportStructureReferenceType

Content:

Ref

Element Documentation:

======== ============================ =============================================================================================================================================================================================================
**Name** **Type**                     **Documentation**
======== ============================ =============================================================================================================================================================================================================
Ref      LocalReportStructure RefType Ref is used to provide a complete set of reference fields. Derived reference types will restrict the RefType so that the content of the Ref element requires exactly what is needed for a complete reference.
======== ============================ =============================================================================================================================================================================================================

**LocalReportStructureRefType: **\ LocalReportStructureRefType contains
a local reference to a report structure object.

Derivation:

| *RefBaseType* (restriction) 
|    |image562|\ *LocalIdentifiableRefBaseType* (restriction) 
|          |image563|\ *LocalComponentListRefBaseType* (restriction) 
|                |image564|\ LocalReportStructureRefType

Attributes:

id, local?, class?, package?

Content:

{Empty}

Attribute Documentation:

================================== ================================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                           **Type**                          **Documentation**
================================== ================================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
id                                 NestedIDType                      The id attribute identifies the object being referenced, and is therefore always required.
local (fixed: true)                xs:boolean                        The local attribute indicates whether this set of reference fields is meant for local referencing, in which case some of the reference fields will be implied from another context. Concrete instances of this class will always fix this value to either true or false, depending on their intended usage. If the value is fixed to true, then the complete set of reference fields will be required and a URN can be fully composed from the values.
class (fixed: ReportStructure)     ComponentListTypeCod elistType    The class attribute indicates the class name of the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
package (fixed: metadatastructure) StructurePackageType CodelistType The package attribute indicates the package name for the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
================================== ================================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================

**MetadataAttributeReferenceType: **\ MetadataAttributeReferenceType is
a type for referencing a metadata attribute object. It consists of a URN
and/or a complete set of reference fields.

Derivation:

| *ReferenceType* (restriction) 
|    |image565|\ *ContainerChildObjectReferenceType* (restriction) 
|          |image566|\ *ComponentReferenceType* (restriction) 
|                |image567|\ MetadataAttributeReferenceType

Content:

( (Ref, URN?) \| URN)

Element Documentation:

======== ========================= =============================================================================================================================================================================================================
**Name** **Type**                  **Documentation**
======== ========================= =============================================================================================================================================================================================================
Ref      MetadataAttributeRef Type Ref is used to provide a complete set of reference fields. Derived reference types will restrict the RefType so that the content of the Ref element requires exactly what is needed for a complete reference.
URN      xs:anyURI                 URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
URN      xs:anyURI                 URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
======== ========================= =============================================================================================================================================================================================================

**MetadataAttributeRefType: **\ MetadataAttributeRefType contains a
reference to a metadata attribute within a report structure in a
metadata structure definition.

Derivation:

| *RefBaseType* (restriction) 
|    |image568|\ *ContainerChildObjectRefBaseType* (restriction) 
|          |image569|\ *ComponentRefBaseType* (restriction) 
|                |image570|\ MetadataAttributeRefType

Attributes:

agencyID, maintainableParentID, maintainableParentVersion?, containerID,
id, version?, local?, class?, package?

Content:

{Empty}

Attribute Documentation:

======================================== ================================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                                 **Type**                          **Documentation**
======================================== ================================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
agencyID                                 NestedNCNameIDType                The agencyID attribute identifies the maintenance agency for the object being referenced (agency-id in the URN structure). This is optional to allow for local references (where the other reference fields are inferred from another context), but all complete references will require this.
maintainableParentID                     IDType                            The maintainableParentID references the structure in which the component being referenced is defined.
maintainableParentVersion (default: 1.0) VersionType                       The maintainableParentVersion attribute references the version of the structure in which the component being referenced is defined. If not supplied, a default value of 1.0 is assumed.
containerID                              IDType                            The containerID attribute references the component list of that contains the component being referenced. It is optional for the cases where the component list has a fixed identifier. Specific implementations of this will prohibit or require this accordingly.
id                                       NestedIDType                      The id attribute identifies the object being referenced, and is therefore always required.
version                                  VersionType                       The version attribute identifies the version of the object being reference, if applicable. If this is available, a default value of 1.0 will always apply.
local (fixed: false)                     xs:boolean                        The local attribute indicates whether this set of reference fields is meant for local referencing, in which case some of the reference fields will be implied from another context. Concrete instances of this class will always fix this value to either true or false, depending on their intended usage. If the value is fixed to true, then the complete set of reference fields will be required and a URN can be fully composed from the values.
class (fixed: MetadataAttribute)         ComponentTypeCodelis tType        The class attribute indicates the class name of the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
package (fixed: metadatastructure)       StructurePackageType CodelistType The package attribute indicates the package name for the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
======================================== ================================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================

**LocalMetadataStructureComponentReferenceType: **\ LocalMetadataStructureComponentReferenceType
is a type for referencing any type of metadata structure component
locally, where the reference for the metadata structure definition which
defines the components is available in another context.

Derivation:

| *ReferenceType* (restriction) 
|    |image571|\ *LocalComponentListComponentReferenceBaseType*\ (restriction) 
|          |image572|\ LocalMetadataStructureComponentReferenceType

Content:

Ref

Element Documentation:

======== ======================================= =============================================================================================================================================================================================================
**Name** **Type**                                **Documentation**
======== ======================================= =============================================================================================================================================================================================================
Ref      LocalMetadataStructu reComponentRefType Ref is used to provide a complete set of reference fields. Derived reference types will restrict the RefType so that the content of the Ref element requires exactly what is needed for a complete reference.
======== ======================================= =============================================================================================================================================================================================================

**LocalMetadataStructureComponentRefType: **\ LocalMetadataStructureComponentRefType
contains the reference fields for referencing any metadata structure
component locally. This reference must specify the class of the
component being referenced.

Derivation:

| *RefBaseType* (restriction) 
|    |image573|\ *LocalIdentifiableRefBaseType* (restriction) 
|          |image574|\ *LocalComponentListComponentRefBaseType* (restriction) 
|                |image575|\ LocalMetadataStructureComponentRefType

Attributes:

containerID, id, local?, class, package?

Content:

{Empty}

Attribute Documentation:

================================== ============================================ ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                           **Type**                                     **Documentation**
================================== ============================================ ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
containerID                        IDType                                       The containerID attribute identifies the object within a maintainable object in which the referenced object is defined (container-object-id in the URN structure). This is only used in references where the referenced object is not contained directly within a maintainable object (e.g. a Component within a ComponentList, within a maintainable Structure). If the container has a fixed identifier, this attribute will not be present.
id                                 NestedIDType                                 The id attribute identifies the object being referenced, and is therefore always required.
local (fixed: true)                xs:boolean                                   The local attribute indicates whether this set of reference fields is meant for local referencing, in which case some of the reference fields will be implied from another context. Concrete instances of this class will always fix this value to either true or false, depending on their intended usage. If the value is fixed to true, then the complete set of reference fields will be required and a URN can be fully composed from the values.
class                              MetadataStructureCom ponentTypeCodelistTy pe The class attribute indicates the class name of the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
package (fixed: metadatastructure) StructurePackageType CodelistType            The package attribute indicates the package name for the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
================================== ============================================ ======================================================================================================================================================================================================================================================================================================================================================================================================================================================

**ProvisionAgreementReferenceType: **\ ProvisionAgreementReferenceType
is a type for referencing a provision agreement. It consists of a URN
and/or a complete set of reference fields.

Derivation:

| *ReferenceType* (restriction) 
|    |image576|\ *MaintainableReferenceBaseType* (restriction) 
|          |image577|\ ProvisionAgreementReferenceType

Content:

( (Ref, URN?) \| URN)

Element Documentation:

======== ========================== =============================================================================================================================================================================================================
**Name** **Type**                   **Documentation**
======== ========================== =============================================================================================================================================================================================================
Ref      ProvisionAgreementRe fType Ref is used to provide a complete set of reference fields. Derived reference types will restrict the RefType so that the content of the Ref element requires exactly what is needed for a complete reference.
URN      xs:anyURI                  URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
URN      xs:anyURI                  URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
======== ========================== =============================================================================================================================================================================================================

**ProvisionAgreementRefType: **\ ProvisionAgreementRefType contains a
set of reference fields for a provision agreement.

Derivation:

| *RefBaseType* (restriction) 
|    |image578|\ *MaintainableRefBaseType* (restriction) 
|          |image579|\ ProvisionAgreementRefType

Attributes:

agencyID, id, version?, local?, class?, package?

Content:

{Empty}

Attribute Documentation:

================================= ============================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                          **Type**                      **Documentation**
================================= ============================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
agencyID                          NestedNCNameIDType            The agencyID attribute identifies the maintenance agency for the object being referenced (agency-id in the URN structure). This is optional to allow for local references (where the other reference fields are inferred from another context), but all complete references will require this.
id                                IDType                        The id attribute identifies the object being referenced, and is therefore always required.
version (default: 1.0)            VersionType                   The version attribute identifies the version of the object being reference, if applicable. If this is available, a default value of 1.0 will always apply.
local (fixed: false)              xs:boolean                    The local attribute indicates whether this set of reference fields is meant for local referencing, in which case some of the reference fields will be implied from another context. Concrete instances of this class will always fix this value to either true or false, depending on their intended usage. If the value is fixed to true, then the complete set of reference fields will be required and a URN can be fully composed from the values.
class (fixed: ProvisionAgreement) MaintainableTypeCode listType The class attribute indicates the class name of the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
package (fixed: registry)         PackageTypeCodelistT ype      The package attribute indicates the package name for the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
================================= ============================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================

**ProcessReferenceType: **\ ProcessReferenceType is a type for
referencing a process object. It consists of a URN and/or a complete set
of reference fields.

Derivation:

| *ReferenceType* (restriction) 
|    |image580|\ *MaintainableReferenceBaseType* (restriction) 
|          |image581|\ ProcessReferenceType

Content:

( (Ref, URN?) \| URN)

Element Documentation:

======== ============== =============================================================================================================================================================================================================
**Name** **Type**       **Documentation**
======== ============== =============================================================================================================================================================================================================
Ref      ProcessRefType Ref is used to provide a complete set of reference fields. Derived reference types will restrict the RefType so that the content of the Ref element requires exactly what is needed for a complete reference.
URN      xs:anyURI      URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
URN      xs:anyURI      URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
======== ============== =============================================================================================================================================================================================================

**ProcessRefType: **\ ProcessRefType contains a set of reference fields
for a process.

Derivation:

| *RefBaseType* (restriction) 
|    |image582|\ *MaintainableRefBaseType* (restriction) 
|          |image583|\ ProcessRefType

Attributes:

agencyID, id, version?, local?, class?, package?

Content:

{Empty}

Attribute Documentation:

======================== ============================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                 **Type**                      **Documentation**
======================== ============================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
agencyID                 NestedNCNameIDType            The agencyID attribute identifies the maintenance agency for the object being referenced (agency-id in the URN structure). This is optional to allow for local references (where the other reference fields are inferred from another context), but all complete references will require this.
id                       IDType                        The id attribute identifies the object being referenced, and is therefore always required.
version (default: 1.0)   VersionType                   The version attribute identifies the version of the object being reference, if applicable. If this is available, a default value of 1.0 will always apply.
local (fixed: false)     xs:boolean                    The local attribute indicates whether this set of reference fields is meant for local referencing, in which case some of the reference fields will be implied from another context. Concrete instances of this class will always fix this value to either true or false, depending on their intended usage. If the value is fixed to true, then the complete set of reference fields will be required and a URN can be fully composed from the values.
class (fixed: Process)   MaintainableTypeCode listType The class attribute indicates the class name of the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
package (fixed: process) PackageTypeCodelistT ype      The package attribute indicates the package name for the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
======================== ============================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================

**ProcessStepReferenceType: **\ ProcessStepReferenceType is a type for
referencing a process step object. It consists of a URN and/or a
complete set of reference fields.

Derivation:

| *ReferenceType* (restriction) 
|    |image584|\ *ChildObjectReferenceType* (restriction) 
|          |image585|\ ProcessStepReferenceType

Content:

( (Ref, URN?) \| URN)

Element Documentation:

======== ================== =============================================================================================================================================================================================================
**Name** **Type**           **Documentation**
======== ================== =============================================================================================================================================================================================================
Ref      ProcessStepRefType Ref is used to provide a complete set of reference fields. Derived reference types will restrict the RefType so that the content of the Ref element requires exactly what is needed for a complete reference.
URN      xs:anyURI          URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
URN      xs:anyURI          URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
======== ================== =============================================================================================================================================================================================================

**ProcessStepRefType: **\ ProcessStepRefType provides for a reference to
a process step through its id. Support for referencing nested process
steps is provided through a nested identifier.

Derivation:

| *RefBaseType* (restriction) 
|    |image586|\ *ChildObjectRefBaseType* (restriction) 
|          |image587|\ ProcessStepRefType

Attributes:

agencyID, maintainableParentID, maintainableParentVersion?, id, local?,
class?, package?

Content:

{Empty}

Attribute Documentation:

======================================== ======================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                                 **Type**                 **Documentation**
======================================== ======================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
agencyID                                 NestedNCNameIDType       The agencyID attribute identifies the maintenance agency for the object being referenced (agency-id in the URN structure). This is optional to allow for local references (where the other reference fields are inferred from another context), but all complete references will require this.
maintainableParentID                     IDType                   The maintainableParentID attribute identifies the maintainable object in which the referenced object is defined, if applicable (maintainable-parent-object-id in the URN structure). This is only used in references where the referenced object is not itself maintainable.
maintainableParentVersion (default: 1.0) VersionType              The maintainableParentVersion attribute identifies the version of the maintainable object in which the referenced object is defined (maintainable-parent-object-version in the URN structure). This is only used in references where the referenced object is not itself maintainable. This should only be used when the maintainableParentID is present. If this is available, a default of 1.0 will always apply.
id                                       NestedIDType             The id attribute identifies the object being referenced, and is therefore always required.
local (fixed: false)                     xs:boolean               The local attribute indicates whether this set of reference fields is meant for local referencing, in which case some of the reference fields will be implied from another context. Concrete instances of this class will always fix this value to either true or false, depending on their intended usage. If the value is fixed to true, then the complete set of reference fields will be required and a URN can be fully composed from the values.
class (fixed: ProcessStep)               ObjectTypeCodelistTy pe  The class attribute indicates the class name of the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
package (fixed: process)                 PackageTypeCodelistT ype The package attribute indicates the package name for the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
======================================== ======================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================

**LocalProcessStepReferenceType: **\ LocalProcessStepReferenceType is a
type for referencing a process step locally, where the reference to the
process which defines it is provided in another context (for example the
metadata structure definition in which the reference occurs).

Derivation:

| *ReferenceType* (restriction) 
|    |image588|\ *LocalIdentifiableReferenceType* (restriction) 
|          |image589|\ LocalProcessStepReferenceType

Content:

Ref

Element Documentation:

======== ======================== =============================================================================================================================================================================================================
**Name** **Type**                 **Documentation**
======== ======================== =============================================================================================================================================================================================================
Ref      LocalProcessStepRefT ype Ref is used to provide a complete set of reference fields. Derived reference types will restrict the RefType so that the content of the Ref element requires exactly what is needed for a complete reference.
======== ======================== =============================================================================================================================================================================================================

**LocalProcessStepRefType: **\ LocalProcessStepRefType contains a local
reference to a process step object.

Derivation:

| *RefBaseType* (restriction) 
|    |image590|\ *LocalIdentifiableRefBaseType* (restriction) 
|          |image591|\ LocalProcessStepRefType

Attributes:

containerID?, id, local?, class?, package?

Content:

{Empty}

Attribute Documentation:

========================== ======================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                   **Type**                 **Documentation**
========================== ======================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
containerID                NestedIDType             The containerID attribute identifies the object within a maintainable object in which the referenced object is defined (container-object-id in the URN structure). This is only used in references where the referenced object is not contained directly within a maintainable object (e.g. a Component within a ComponentList, within a maintainable Structure). If the container has a fixed identifier, this attribute will not be present.
id                         NestedIDType             The id attribute identifies the object being referenced, and is therefore always required.
local (fixed: true)        xs:boolean               The local attribute indicates whether this set of reference fields is meant for local referencing, in which case some of the reference fields will be implied from another context. Concrete instances of this class will always fix this value to either true or false, depending on their intended usage. If the value is fixed to true, then the complete set of reference fields will be required and a URN can be fully composed from the values.
class (fixed: ProcessStep) ObjectTypeCodelistTy pe  The class attribute indicates the class name of the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
package (fixed: process)   PackageTypeCodelistT ype The package attribute indicates the package name for the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
========================== ======================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================

**TransitionReferenceType: **\ TransiationReferenceType is a type for
referencing a process step object. It consists of a URN and/or a
complete set of reference fields.

Derivation:

| *ReferenceType* (restriction) 
|    |image592|\ *ContainerChildObjectReferenceType* (restriction) 
|          |image593|\ TransitionReferenceType

Content:

( (Ref, URN?) \| URN)

Element Documentation:

======== ================= =============================================================================================================================================================================================================
**Name** **Type**          **Documentation**
======== ================= =============================================================================================================================================================================================================
Ref      TransitionRefType Ref is used to provide a complete set of reference fields. Derived reference types will restrict the RefType so that the content of the Ref element requires exactly what is needed for a complete reference.
URN      xs:anyURI         URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
URN      xs:anyURI         URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
======== ================= =============================================================================================================================================================================================================

**TransitionRefType: **\ TransitionRefType provides for a reference to a
transition definition in process step through its id.

Derivation:

| *RefBaseType* (restriction) 
|    |image594|\ *ContainerChildObjectRefBaseType* (restriction) 
|          |image595|\ TransitionRefType

Attributes:

agencyID, maintainableParentID, maintainableParentVersion?, containerID,
id, version?, local?, class?, package?

Content:

{Empty}

Attribute Documentation:

======================================== ======================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                                 **Type**                 **Documentation**
======================================== ======================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
agencyID                                 NestedNCNameIDType       The agencyID attribute identifies the maintenance agency for the object being referenced (agency-id in the URN structure). This is optional to allow for local references (where the other reference fields are inferred from another context), but all complete references will require this.
maintainableParentID                     IDType                   The maintainableParentID attribute identifies the maintainable object in which the referenced object is defined, if applicable (maintainable-parent-object-id in the URN structure). This is only used in references where the referenced object is not itself maintainable.
maintainableParentVersion (default: 1.0) VersionType              The maintainableParentVersion attribute identifies the version of the maintainable object in which the referenced object is defined (maintainable-parent-object-version in the URN structure). This is only used in references where the referenced object is not itself maintainable. This should only be used when the maintainableParentID is present. If this is available, a default of 1.0 will always apply.
containerID                              NestedIDType             The containerID attribute identifies the object within a maintainable object in which the referenced object is defined (container-object-id in the URN structure). This is only used in references where the referenced object is not contained directly within a maintainable object (e.g. a Component within a ComponentList, within a maintainable Structure). If the container has a fixed identifier, this attribute will not be present.
id                                       NestedIDType             The id attribute identifies the object being referenced, and is therefore always required.
version                                  VersionType              The version attribute identifies the version of the object being reference, if applicable. If this is available, a default value of 1.0 will always apply.
local (fixed: false)                     xs:boolean               The local attribute indicates whether this set of reference fields is meant for local referencing, in which case some of the reference fields will be implied from another context. Concrete instances of this class will always fix this value to either true or false, depending on their intended usage. If the value is fixed to true, then the complete set of reference fields will be required and a URN can be fully composed from the values.
class (fixed: Transition)                ObjectTypeCodelistTy pe  The class attribute indicates the class name of the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
package (fixed: process)                 PackageTypeCodelistT ype The package attribute indicates the package name for the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
======================================== ======================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================

**StructureSetReferenceType: **\ StructureSetReferenceType is a type for
referencing a structure set object. It consists of a URN and/or a
complete set of reference fields.

Derivation:

| *ReferenceType* (restriction) 
|    |image596|\ *MaintainableReferenceBaseType* (restriction) 
|          |image597|\ StructureSetReferenceType

Content:

( (Ref, URN?) \| URN)

Element Documentation:

======== =================== =============================================================================================================================================================================================================
**Name** **Type**            **Documentation**
======== =================== =============================================================================================================================================================================================================
Ref      StructureSetRefType Ref is used to provide a complete set of reference fields. Derived reference types will restrict the RefType so that the content of the Ref element requires exactly what is needed for a complete reference.
URN      xs:anyURI           URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
URN      xs:anyURI           URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
======== =================== =============================================================================================================================================================================================================

**StructureSetRefType: **\ StructureSetRefType contains a set of
reference fields for a structure set.

Derivation:

| *RefBaseType* (restriction) 
|    |image598|\ *MaintainableRefBaseType* (restriction) 
|          |image599|\ StructureSetRefType

Attributes:

agencyID, id, version?, local?, class?, package?

Content:

{Empty}

Attribute Documentation:

=========================== ============================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                    **Type**                      **Documentation**
=========================== ============================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
agencyID                    NestedNCNameIDType            The agencyID attribute identifies the maintenance agency for the object being referenced (agency-id in the URN structure). This is optional to allow for local references (where the other reference fields are inferred from another context), but all complete references will require this.
id                          IDType                        The id attribute identifies the object being referenced, and is therefore always required.
version (default: 1.0)      VersionType                   The version attribute identifies the version of the object being reference, if applicable. If this is available, a default value of 1.0 will always apply.
local (fixed: false)        xs:boolean                    The local attribute indicates whether this set of reference fields is meant for local referencing, in which case some of the reference fields will be implied from another context. Concrete instances of this class will always fix this value to either true or false, depending on their intended usage. If the value is fixed to true, then the complete set of reference fields will be required and a URN can be fully composed from the values.
class (fixed: StructureSet) MaintainableTypeCode listType The class attribute indicates the class name of the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
package (fixed: mapping)    PackageTypeCodelistT ype      The package attribute indicates the package name for the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
=========================== ============================= ======================================================================================================================================================================================================================================================================================================================================================================================================================================================

**StructureMapReferenceType: **\ StructureMapReferenceType is a type for
referencing a structure map object. It consists of a URN and/or a
complete set of reference fields.

Derivation:

| *ReferenceType* (restriction) 
|    |image600|\ *ChildObjectReferenceType* (restriction) 
|          |image601|\ StructureMapReferenceType

Content:

( (Ref, URN?) \| URN)

Element Documentation:

======== =================== =============================================================================================================================================================================================================
**Name** **Type**            **Documentation**
======== =================== =============================================================================================================================================================================================================
Ref      StructureMapRefType Ref is used to provide a complete set of reference fields. Derived reference types will restrict the RefType so that the content of the Ref element requires exactly what is needed for a complete reference.
URN      xs:anyURI           URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
URN      xs:anyURI           URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
======== =================== =============================================================================================================================================================================================================

**StructureMapRefType: **\ StructureMapRefType contains fields for
referencing a structure map within a structure set.

Derivation:

| *RefBaseType* (restriction) 
|    |image602|\ *ChildObjectRefBaseType* (restriction) 
|          |image603|\ StructureMapRefType

Attributes:

agencyID, maintainableParentID, maintainableParentVersion?, id, local?,
class?, package?

Content:

{Empty}

Attribute Documentation:

======================================== ======================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                                 **Type**                 **Documentation**
======================================== ======================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
agencyID                                 NestedNCNameIDType       The agencyID attribute identifies the maintenance agency for the object being referenced (agency-id in the URN structure). This is optional to allow for local references (where the other reference fields are inferred from another context), but all complete references will require this.
maintainableParentID                     IDType                   The maintainableParentID attribute identifies the maintainable object in which the referenced object is defined, if applicable (maintainable-parent-object-id in the URN structure). This is only used in references where the referenced object is not itself maintainable.
maintainableParentVersion (default: 1.0) VersionType              The maintainableParentVersion attribute identifies the version of the maintainable object in which the referenced object is defined (maintainable-parent-object-version in the URN structure). This is only used in references where the referenced object is not itself maintainable. This should only be used when the maintainableParentID is present. If this is available, a default of 1.0 will always apply.
id                                       IDType                   The id attribute identifies the object being referenced, and is therefore always required.
local (fixed: false)                     xs:boolean               The local attribute indicates whether this set of reference fields is meant for local referencing, in which case some of the reference fields will be implied from another context. Concrete instances of this class will always fix this value to either true or false, depending on their intended usage. If the value is fixed to true, then the complete set of reference fields will be required and a URN can be fully composed from the values.
class (fixed: StructureMap)              ObjectTypeCodelistTy pe  The class attribute indicates the class name of the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
package (fixed: mapping)                 PackageTypeCodelistT ype The package attribute indicates the package name for the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
======================================== ======================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================

**CategorySchemeMapReferenceType: **\ CategorySchemeMapReferenceType is
a type for referencing a category scheme map object. It consists of a
URN and/or a complete set of reference fields.

Derivation:

| *ReferenceType* (restriction) 
|    |image604|\ *ChildObjectReferenceType* (restriction) 
|          |image605|\ CategorySchemeMapReferenceType

Content:

( (Ref, URN?) \| URN)

Element Documentation:

======== ========================= =============================================================================================================================================================================================================
**Name** **Type**                  **Documentation**
======== ========================= =============================================================================================================================================================================================================
Ref      CategorySchemeMapRef Type Ref is used to provide a complete set of reference fields. Derived reference types will restrict the RefType so that the content of the Ref element requires exactly what is needed for a complete reference.
URN      xs:anyURI                 URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
URN      xs:anyURI                 URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
======== ========================= =============================================================================================================================================================================================================

**CategorySchemeMapRefType: **\ CategorySchemeMapRefType contains a set
of reference fields for a category scheme map.

Derivation:

| *RefBaseType* (restriction) 
|    |image606|\ *ChildObjectRefBaseType* (restriction) 
|          |image607|\ CategorySchemeMapRefType

Attributes:

agencyID, maintainableParentID, maintainableParentVersion?, id, local?,
class?, package?

Content:

{Empty}

Attribute Documentation:

======================================== ======================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                                 **Type**                 **Documentation**
======================================== ======================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
agencyID                                 NestedNCNameIDType       The agencyID attribute identifies the maintenance agency for the object being referenced (agency-id in the URN structure). This is optional to allow for local references (where the other reference fields are inferred from another context), but all complete references will require this.
maintainableParentID                     IDType                   The maintainableParentID attribute identifies the maintainable object in which the referenced object is defined, if applicable (maintainable-parent-object-id in the URN structure). This is only used in references where the referenced object is not itself maintainable.
maintainableParentVersion (default: 1.0) VersionType              The maintainableParentVersion attribute identifies the version of the maintainable object in which the referenced object is defined (maintainable-parent-object-version in the URN structure). This is only used in references where the referenced object is not itself maintainable. This should only be used when the maintainableParentID is present. If this is available, a default of 1.0 will always apply.
id                                       IDType                   The id attribute identifies the object being referenced, and is therefore always required.
local (fixed: false)                     xs:boolean               The local attribute indicates whether this set of reference fields is meant for local referencing, in which case some of the reference fields will be implied from another context. Concrete instances of this class will always fix this value to either true or false, depending on their intended usage. If the value is fixed to true, then the complete set of reference fields will be required and a URN can be fully composed from the values.
class (fixed: CategorySchemeMap)         ObjectTypeCodelistTy pe  The class attribute indicates the class name of the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
package (fixed: mapping)                 PackageTypeCodelistT ype The package attribute indicates the package name for the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
======================================== ======================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================

**CodelistMapReferenceType: **\ CodelistMapReferenceType is a type for
referencing a codelist map object. It consists of a URN and/or a
complete set of reference fields.

Derivation:

| *ReferenceType* (restriction) 
|    |image608|\ *ChildObjectReferenceType* (restriction) 
|          |image609|\ CodelistMapReferenceType

Content:

( (Ref, URN?) \| URN)

Element Documentation:

======== ================== =============================================================================================================================================================================================================
**Name** **Type**           **Documentation**
======== ================== =============================================================================================================================================================================================================
Ref      CodelistMapRefType Ref is used to provide a complete set of reference fields. Derived reference types will restrict the RefType so that the content of the Ref element requires exactly what is needed for a complete reference.
URN      xs:anyURI          URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
URN      xs:anyURI          URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
======== ================== =============================================================================================================================================================================================================

**CodelistMapRefType: **\ CodelistMapRefType contains a set of reference
fields for a codelist map.

Derivation:

| *RefBaseType* (restriction) 
|    |image610|\ *ChildObjectRefBaseType* (restriction) 
|          |image611|\ CodelistMapRefType

Attributes:

agencyID, maintainableParentID, maintainableParentVersion?, id, local?,
class?, package?

Content:

{Empty}

Attribute Documentation:

======================================== ======================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                                 **Type**                 **Documentation**
======================================== ======================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
agencyID                                 NestedNCNameIDType       The agencyID attribute identifies the maintenance agency for the object being referenced (agency-id in the URN structure). This is optional to allow for local references (where the other reference fields are inferred from another context), but all complete references will require this.
maintainableParentID                     IDType                   The maintainableParentID attribute identifies the maintainable object in which the referenced object is defined, if applicable (maintainable-parent-object-id in the URN structure). This is only used in references where the referenced object is not itself maintainable.
maintainableParentVersion (default: 1.0) VersionType              The maintainableParentVersion attribute identifies the version of the maintainable object in which the referenced object is defined (maintainable-parent-object-version in the URN structure). This is only used in references where the referenced object is not itself maintainable. This should only be used when the maintainableParentID is present. If this is available, a default of 1.0 will always apply.
id                                       IDType                   The id attribute identifies the object being referenced, and is therefore always required.
local (fixed: false)                     xs:boolean               The local attribute indicates whether this set of reference fields is meant for local referencing, in which case some of the reference fields will be implied from another context. Concrete instances of this class will always fix this value to either true or false, depending on their intended usage. If the value is fixed to true, then the complete set of reference fields will be required and a URN can be fully composed from the values.
class (fixed: CodelistMap)               ObjectTypeCodelistTy pe  The class attribute indicates the class name of the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
package (fixed: mapping)                 PackageTypeCodelistT ype The package attribute indicates the package name for the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
======================================== ======================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================

**LocalCodelistMapReferenceType: **\ LocalCodelistMapReferenceType is a
type for referencing a codelist map object where the reference to the
structure set which defines it is provided in another context (e.g. the
structure set in which this reference occurs).

Derivation:

| *ReferenceType* (restriction) 
|    |image612|\ LocalCodelistMapReferenceType

Content:

Ref

Element Documentation:

======== ======================== =============================================================================================================================================================================================================
**Name** **Type**                 **Documentation**
======== ======================== =============================================================================================================================================================================================================
Ref      LocalCodelistMapRefT ype Ref is used to provide a complete set of reference fields. Derived reference types will restrict the RefType so that the content of the Ref element requires exactly what is needed for a complete reference.
======== ======================== =============================================================================================================================================================================================================

**LocalCodelistMapRefType: **\ LocalCodelistMapRefType contains a set of
reference fields for a codelist map locally.

Derivation:

| *RefBaseType* (restriction) 
|    |image613|\ *LocalIdentifiableRefBaseType* (restriction) 
|          |image614|\ LocalCodelistMapRefType

Attributes:

id, local?, class?, package?

Content:

{Empty}

Attribute Documentation:

========================== ======================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                   **Type**                 **Documentation**
========================== ======================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
id                         NestedIDType             The id attribute identifies the object being referenced, and is therefore always required.
local (fixed: true)        xs:boolean               The local attribute indicates whether this set of reference fields is meant for local referencing, in which case some of the reference fields will be implied from another context. Concrete instances of this class will always fix this value to either true or false, depending on their intended usage. If the value is fixed to true, then the complete set of reference fields will be required and a URN can be fully composed from the values.
class (fixed: CodelistMap) ObjectTypeCodelistTy pe  The class attribute indicates the class name of the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
package (fixed: mapping)   PackageTypeCodelistT ype The package attribute indicates the package name for the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
========================== ======================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================

**ConceptSchemeMapReferenceType: **\ ConceptSchemeMapReferenceType is a
type for referencing a concept scheme map object. It consists of a URN
and/or a complete set of reference fields.

Derivation:

| *ReferenceType* (restriction) 
|    |image615|\ *ChildObjectReferenceType* (restriction) 
|          |image616|\ ConceptSchemeMapReferenceType

Content:

( (Ref, URN?) \| URN)

Element Documentation:

======== ======================== =============================================================================================================================================================================================================
**Name** **Type**                 **Documentation**
======== ======================== =============================================================================================================================================================================================================
Ref      ConceptSchemeMapRefT ype Ref is used to provide a complete set of reference fields. Derived reference types will restrict the RefType so that the content of the Ref element requires exactly what is needed for a complete reference.
URN      xs:anyURI                URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
URN      xs:anyURI                URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
======== ======================== =============================================================================================================================================================================================================

**ConceptSchemeMapRefType: **\ ConceptSchemeMapRefType contains a set of
reference fields for a concept scheme map.

Derivation:

| *RefBaseType* (restriction) 
|    |image617|\ *ChildObjectRefBaseType* (restriction) 
|          |image618|\ ConceptSchemeMapRefType

Attributes:

agencyID, maintainableParentID, maintainableParentVersion?, id, local?,
class?, package?

Content:

{Empty}

Attribute Documentation:

======================================== ======================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                                 **Type**                 **Documentation**
======================================== ======================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
agencyID                                 NestedNCNameIDType       The agencyID attribute identifies the maintenance agency for the object being referenced (agency-id in the URN structure). This is optional to allow for local references (where the other reference fields are inferred from another context), but all complete references will require this.
maintainableParentID                     IDType                   The maintainableParentID attribute identifies the maintainable object in which the referenced object is defined, if applicable (maintainable-parent-object-id in the URN structure). This is only used in references where the referenced object is not itself maintainable.
maintainableParentVersion (default: 1.0) VersionType              The maintainableParentVersion attribute identifies the version of the maintainable object in which the referenced object is defined (maintainable-parent-object-version in the URN structure). This is only used in references where the referenced object is not itself maintainable. This should only be used when the maintainableParentID is present. If this is available, a default of 1.0 will always apply.
id                                       IDType                   The id attribute identifies the object being referenced, and is therefore always required.
local (fixed: false)                     xs:boolean               The local attribute indicates whether this set of reference fields is meant for local referencing, in which case some of the reference fields will be implied from another context. Concrete instances of this class will always fix this value to either true or false, depending on their intended usage. If the value is fixed to true, then the complete set of reference fields will be required and a URN can be fully composed from the values.
class (fixed: ConceptSchemeMap)          ObjectTypeCodelistTy pe  The class attribute indicates the class name of the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
package (fixed: mapping)                 PackageTypeCodelistT ype The package attribute indicates the package name for the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
======================================== ======================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================

**OrganisationSchemeMapReferenceType: **\ OrganisationSchemeMapReferenceType
is a type for referencing a organisation scheme map object. It consists
of a URN and/or a complete set of reference fields.

Derivation:

| *ReferenceType* (restriction) 
|    |image619|\ *ChildObjectReferenceType* (restriction) 
|          |image620|\ OrganisationSchemeMapReferenceType

Content:

( (Ref, URN?) \| URN)

Element Documentation:

======== ============================= =============================================================================================================================================================================================================
**Name** **Type**                      **Documentation**
======== ============================= =============================================================================================================================================================================================================
Ref      OrganisationSchemeMa pRefType Ref is used to provide a complete set of reference fields. Derived reference types will restrict the RefType so that the content of the Ref element requires exactly what is needed for a complete reference.
URN      xs:anyURI                     URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
URN      xs:anyURI                     URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
======== ============================= =============================================================================================================================================================================================================

**OrganisationSchemeMapRefType: **\ OrganisationSchemeMapRefType
contains a set of reference fields for an organisation scheme map.

Derivation:

| *RefBaseType* (restriction) 
|    |image621|\ *ChildObjectRefBaseType* (restriction) 
|          |image622|\ OrganisationSchemeMapRefType

Attributes:

agencyID, maintainableParentID, maintainableParentVersion?, id, local?,
class?, package?

Content:

{Empty}

Attribute Documentation:

======================================== ======================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                                 **Type**                 **Documentation**
======================================== ======================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================
agencyID                                 NestedNCNameIDType       The agencyID attribute identifies the maintenance agency for the object being referenced (agency-id in the URN structure). This is optional to allow for local references (where the other reference fields are inferred from another context), but all complete references will require this.
maintainableParentID                     IDType                   The maintainableParentID attribute identifies the maintainable object in which the referenced object is defined, if applicable (maintainable-parent-object-id in the URN structure). This is only used in references where the referenced object is not itself maintainable.
maintainableParentVersion (default: 1.0) VersionType              The maintainableParentVersion attribute identifies the version of the maintainable object in which the referenced object is defined (maintainable-parent-object-version in the URN structure). This is only used in references where the referenced object is not itself maintainable. This should only be used when the maintainableParentID is present. If this is available, a default of 1.0 will always apply.
id                                       IDType                   The id attribute identifies the object being referenced, and is therefore always required.
local (fixed: false)                     xs:boolean               The local attribute indicates whether this set of reference fields is meant for local referencing, in which case some of the reference fields will be implied from another context. Concrete instances of this class will always fix this value to either true or false, depending on their intended usage. If the value is fixed to true, then the complete set of reference fields will be required and a URN can be fully composed from the values.
class (fixed: OrganisationSchemeMap)     ObjectTypeCodelistTy pe  The class attribute indicates the class name of the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
package (fixed: mapping)                 PackageTypeCodelistT ype The package attribute indicates the package name for the object being referenced. This attribute allows any reference to be processed generically from this definition. References derived from this should fix the value of this attribute to indicate the type of object that is being referenced, or in the case that a reference which allows specific types of fields, the representation should be sub-setted to the appropriate values.
======================================== ======================== ======================================================================================================================================================================================================================================================================================================================================================================================================================================================

**SetReferenceType: **\ SetReferenceType defines the structure of a
reference to a data/metadata set. A full reference to a data provider
and the identifier for the data set must be provided. Note that this is
not derived from the base reference structure since data/metadata sets
are not technically identifiable.

Content:

DataProvider, ID

Element Documentation:

============ ========================== ==================================================================================================================================
**Name**     **Type**                   **Documentation**
============ ========================== ==================================================================================================================================
DataProvider DataProviderReferenc eType DataProvider references a the provider of the data/metadata set. A URN and/or a complete set of reference fields must be provided.
ID           IDType                     ID contains the identifier of the data/metadata set being referenced.
============ ========================== ==================================================================================================================================

**ObjectTypeListType: **\ ObjectTypeListType provides a means for
enumerating object types.

Content:

(Any?, Agency?, AgencyScheme?, AttachmentConstraint?, Attribute?,
AttributeDescriptor?, Categorisation?, Category?, CategorySchemeMap?,
CategoryScheme?, Code?, CodeMap?, Codelist?, CodelistMap?,
ComponentMap?, Concept?, ConceptMap?, ConceptScheme?, ConceptSchemeMap?,
ContentConstraint?, Dataflow?, DataConsumer?, DataConsumerScheme?,
DataProvider?, DataProviderScheme?, DataSetTarget?, DataStructure?,
Dimension?, DimensionDescriptor?, DimensionDescriptorValuesTarget?,
GroupDimensionDescriptor?, HierarchicalCode?, HierarchicalCodelist?,
Hierarchy?, HybridCodelistMap?, HybridCodeMap?,
IdentifiableObjectTarget?, Level?, MeasureDescriptor?,
MeasureDimension?, Metadataflow?, MetadataAttribute?, MetadataSet?,
MetadataStructure?, MetadataTarget?, OrganisationMap?,
OrganisationSchemeMap?, OrganisationUnit?, OrganisationUnitScheme?,
PrimaryMeasure?, Process?, ProcessStep?, ProvisionAgreement?,
ReportingCategory?, ReportingCategoryMap?, ReportingTaxonomy?,
ReportingTaxonomyMap?, ReportPeriodTarget?, ReportStructure?,
StructureMap?, StructureSet?, TimeDimension?, Transition?)

Element Documentation:

================================ ========= =============================================================================================================
**Name**                         **Type**  **Documentation**
================================ ========= =============================================================================================================
Any                              EmptyType Any is an empty element that denotes an object of any type.
Agency                           EmptyType Agency is an empty element that denotes an agency object.
AgencyScheme                     EmptyType AgencyScheme is an empty element that denotes an agency scheme object.
AttachmentConstraint             EmptyType AttachmentConstraint is an empty element that denotes an attachment constraint object.
Attribute                        EmptyType Attribute is an empty element that denotes an attribute object.
AttributeDescriptor              EmptyType AttributeDescriptor is an empty element that denotes an attribute descriptor object.
Categorisation                   EmptyType Categorisation is an empty element that denotes a categorisation object.
Category                         EmptyType Category is an empty element that denotes a category object.
CategorySchemeMap                EmptyType CategorySchemeMap is an empty element that denotes a category scheme map object.
CategoryScheme                   EmptyType CategoryScheme is an empty element that denotes a category scheme object.
Code                             EmptyType Code is an empty element that denotes a code object.
CodeMap                          EmptyType CodeMap is an empty element that denotes a code map object.
Codelist                         EmptyType Codelist is an empty element that denotes a code list object.
CodelistMap                      EmptyType CodelistMap is an empty element that denotes a code list map object.
ComponentMap                     EmptyType ComponentMap is an empty element that denotes a component map object.
Concept                          EmptyType Concept is an empty element that denotes a concept object.
ConceptMap                       EmptyType ConceptMap is an empty element that denotes a concept map object.
ConceptScheme                    EmptyType ConceptScheme is an empty element that denotes a concept scheme object.
ConceptSchemeMap                 EmptyType ConceptSchemeMap is an empty element that denotes a concept scheme map object.
ContentConstraint                EmptyType ContentConstraint is an empty element that denotes a content constraint object.
Dataflow                         EmptyType Dataflow is an empty element that denotes a data flow object.
DataConsumer                     EmptyType DataConsumer is an empty element that denotes a data consumer object.
DataConsumerScheme               EmptyType DataConsumerScheme is an empty element that denotes a data consumer scheme object.
DataProvider                     EmptyType DataProvider is an empty element that denotes a data provider object.
DataProviderScheme               EmptyType DataProviderScheme is an empty element that denotes a data provider scheme object.
DataSetTarget                    EmptyType DataSetTarget is an empty element that denotes a data set target object.
DataStructure                    EmptyType DataStructure is an empty element that denotes a data structure definition object.
Dimension                        EmptyType Dimension is an empty element that denotes a dimension object.
DimensionDescriptor              EmptyType DimensionDescriptor is an empty element that denotes a dimension descriptor object.
DimensionDescriptorV aluesTarget EmptyType DimensionDescriptorValuesTarget is an empty element that denotes a dimension descriptor values target object.
GroupDimensionDescri ptor        EmptyType GroupDimensionDescriptor is an empty element that denotes a group dimension descriptor object.
HierarchicalCode                 EmptyType HierarchicalCode is an empty element that denotes a hierarchical code object.
HierarchicalCodelist             EmptyType HierarchicalCodelist is an empty element that denotes a hierarchical codelist object.
Hierarchy                        EmptyType Hierarchy is an empty element that denotes a hierarchy within a hiearcharchical codelist.
HybridCodelistMap                EmptyType HybridCodelistMap is an empty element that denotes a hybrid codelist map object.
HybridCodeMap                    EmptyType HybridCodeMap is an empty element that denotes a hybrid code map object.
IdentifiableObjectTa rget        EmptyType IdentifiableObjectTarget is an empty element that denotes an identifiable object target object.
Level                            EmptyType Level is an empty element that denotes a level object.
MeasureDescriptor                EmptyType MeasureDescriptor is an empty element that denotes a measure descriptor object.
MeasureDimension                 EmptyType MeasureDimension is an empty element that denotes a measure dimension object.
Metadataflow                     EmptyType Metadataflow is an empty element that denotes a metadata flow object.
MetadataAttribute                EmptyType MetadataAttribute is an empty element that denotes a metadata attribute object.
MetadataSet                      EmptyType MetadataSet is an empty element that denotes a metadata set object.
MetadataStructure                EmptyType MetadataStructure is an empty element that denotes a metadata structure definition object.
MetadataTarget                   EmptyType MetadataTarget is an empty element that denotes a metadata target object.
OrganisationMap                  EmptyType OrganisationMap is an empty element that denotes an organisation map object.
OrganisationSchemeMa p           EmptyType OrganisationSchemeMap is an empty element that denotes an organisation scheme map object.
OrganisationUnit                 EmptyType OrganisationUnit is an empty element that denotes an organisation unit object.
OrganisationUnitSche me          EmptyType OrganisationUnitScheme is an empty element that denotes an organisation unit scheme object.
PrimaryMeasure                   EmptyType PrimaryMeasure is an empty element that denotes a primary measure object.
Process                          EmptyType Process is an empty element that denotes a process object.
ProcessStep                      EmptyType ProcessStep is an empty element that denotes a process step object.
ProvisionAgreement               EmptyType ProvisionAgreement is an empty element that denotes a provision agreement object.
ReportingCategory                EmptyType ReportingCategory is an empty element that denotes a reporting category object.
ReportingCategoryMap             EmptyType ReportingCategoryMap is an empty element that denotes a reporting category map object.
ReportingTaxonomy                EmptyType ReportingTaxonomy is an empty element that denotes a reporting taxonomy object.
ReportingTaxonomyMap             EmptyType ReportingTaxonomyMap is an empty element that denotes a reporting taxonomy map object.
ReportPeriodTarget               EmptyType ReportPeriodTarget is an empty element that denotes a report period target object.
ReportStructure                  EmptyType ReportStructure is an empty element that denotes a report structure object.
StructureMap                     EmptyType StructureMap is an empty element that denotes a structure map object.
StructureSet                     EmptyType StructureSet is an empty element that denotes a structure set object.
TimeDimension                    EmptyType TimeDimension is an empty element that denotes a time dimension object.
Transition                       EmptyType Transition is an empty element that denotes a transition object.
================================ ========= =============================================================================================================

**MaintainableObjectTypeListType: **\ MaintainableObjectTypeListType
provides a means for enumerating maintainable object types.

Derivation:

| ObjectTypeListType (restriction) 
|    |image623|\ MaintainableObjectTypeListType

Content:

(AgencyScheme?, AttachmentConstraint?, Categorisation?, CategoryScheme?,
Codelist?, ConceptScheme?, ContentConstraint?, Dataflow?,
DataConsumerScheme?, DataProviderScheme?, DataStructure?,
HierarchicalCodelist?, Metadataflow?, MetadataStructure?,
OrganisationUnitScheme?, Process?, ProvisionAgreement?,
ReportingTaxonomy?, StructureSet?)

Element Documentation:

======================= ========= ===========================================================================================
**Name**                **Type**  **Documentation**
======================= ========= ===========================================================================================
AgencyScheme            EmptyType AgencyScheme is an empty element that denotes an agency scheme object.
AttachmentConstraint    EmptyType AttachmentConstraint is an empty element that denotes an attachment constraint object.
Categorisation          EmptyType Categorisation is an empty element that denotes a categorisation object.
CategoryScheme          EmptyType CategoryScheme is an empty element that denotes a category scheme object.
Codelist                EmptyType Codelist is an empty element that denotes a code list object.
ConceptScheme           EmptyType ConceptScheme is an empty element that denotes a concept scheme object.
ContentConstraint       EmptyType ContentConstraint is an empty element that denotes a content constraint object.
Dataflow                EmptyType Dataflow is an empty element that denotes a data flow object.
DataConsumerScheme      EmptyType DataConsumerScheme is an empty element that denotes a data consumer scheme object.
DataProviderScheme      EmptyType DataProviderScheme is an empty element that denotes a data provider scheme object.
DataStructure           EmptyType DataStructure is an empty element that denotes a data structure definition object.
HierarchicalCodelist    EmptyType HierarchicalCodelist is an empty element that denotes a hierarchical codelist object.
Metadataflow            EmptyType Metadataflow is an empty element that denotes a metadata flow object.
MetadataStructure       EmptyType MetadataStructure is an empty element that denotes a metadata structure definition object.
OrganisationUnitSche me EmptyType OrganisationUnitScheme is an empty element that denotes an organisation unit scheme object.
Process                 EmptyType Process is an empty element that denotes a process object.
ProvisionAgreement      EmptyType ProvisionAgreement is an empty element that denotes a provision agreement object.
ReportingTaxonomy       EmptyType ReportingTaxonomy is an empty element that denotes a reporting taxonomy object.
StructureSet            EmptyType StructureSet is an empty element that denotes a structure set object.
======================= ========= ===========================================================================================

Simple Types
~~~~~~~~~~~~

**AlphaNumericType: **\ AlphaNumericType is a reusable simple type that
allows for only mixed-case alphabetical and numeric characters.

| Derived by restriction of xs:string .
| Regular Expression Pattern: [A-z0-9]+

**AlphaType: **\ AlphaType is a reusable simple type that allows for
only mixed-case alphabetical characters. This is derived from the
AlphaNumericType.

| Derived by restriction of AlphaNumericType .
| Regular Expression Pattern: [A-z]+

**NumericType: **\ NumericType is a reusable simple type that allows for
only numeric characters. This is not to be confused with an integer, as
this may be used to numeric strings which have leading zeros. These
leading zeros are not ignored. This is derived from the
AlphaNumericType.

| Derived by restriction of AlphaNumericType .
| Regular Expression Pattern: [0-9]+

**ObservationalTimePeriodType: **\ ObservationalTimePeriodType specifies
a distinct time period or point in time in SDMX. The time period can
either be a Gregorian calendar period, a standard reporting period, a
distinct point in time, or a time range with a specific date and
duration.

Union of:

xs:gYear, xs:gYearMonth, xs:date, xs:dateTime, ReportingYearType,
ReportingSemesterType, ReportingTrimesterType, ReportingQuarterType,
ReportingMonthType, ReportingWeekType, ReportingDayType, TimeRangeType.

**StandardTimePeriodType: **\ StandardTimePeriodType defines the set of
standard time periods in SDMX. This includes the reporting time periods
and the basic date type (i.e. the calendar time periods and the dateTime
format).

Union of:

xs:gYear, xs:gYearMonth, xs:date, xs:dateTime, ReportingYearType,
ReportingSemesterType, ReportingTrimesterType, ReportingQuarterType,
ReportingMonthType, ReportingWeekType, ReportingDayType.

**BasicTimePeriodType: **\ BasicTimePeriodType contains the basic dates
and calendar periods. It is a combination of the Gregorian time periods
and the date time type..

Union of:

xs:gYear, xs:gYearMonth, xs:date, xs:dateTime.

**GregorianTimePeriodType: **\ GregorianTimePeriodType defines the set
of standard calendar periods in SDMX.

Union of:

xs:gYear, xs:gYearMonth, xs:date.

**ReportingTimePeriodType: **\ ReportingTimePeriodType defines standard
reporting periods in SDMX, which are all in relation to the start day
(day-month) of a reporting year which is specified in the specialized
reporting year start day attribute. If the reporting year start day is
not defined, a day of January 1 is assumed. The reporting year must be
epxressed as the year at the beginning of the period. Therfore, if the
reproting year runs from April to March, any given reporting year is
expressed as the year for April. The general format of a report period
can be described as [year]-[period][time zone]?, where the type of
period is designated with a single character followed by a number
representing the period. Note that all periods allow for an optional
time zone offset. See the details of each member type for the specifics
of its format.

Union of:

ReportingYearType, ReportingSemesterType, ReportingTrimesterType,
ReportingQuarterType, ReportingMonthType, ReportingWeekType,
ReportingDayType.

**BaseReportPeriodType: **\ BaseReportPeriodType is a simple type which
frames the general pattern of a reporting period for validation
purposes. This regular expression is only a general validation which is
meant to validate the following structure [year]-[period][time zone]?.
This type is meant to be derived from for further validation.

| Derived by restriction of xs:string .
| Regular Expression
  Pattern: \d{4}\-([ASTQ]\d{1}|[MW]\d{2}|[D]\d{3})(Z|((\+|\-)\d{2}:\d{2}))?

**ReportPeriodValidTimeZoneType: **\ ReportPeriodValidTimeZoneType is a
derivation of the BaseReportPeriodType which validates that the time
zone provided in the base type is valid. The base type will have
provided basic validation already. The patterns below validate that the
time zone is "Z" or that it is between -14:00 and +14:00, or that there
is no time zone provided. This type is meant to be derived from for
further validation.

| Derived by restriction of BaseReportPeriodType .
| Regular Expression
  Pattern: .+Z.{5}.*(\+|\-)(14:00|((0[0-9]|1[0-3]):[0-5][0-9])).{5}[^\+\-Z]+

**ReportingYearType: **\ ReportingYearType defines a time period of 1
year (P1Y) in relation to a reporting year which has a start day
(day-month) specified in the specialized reporting year start day
attribute. In the absence of a start day for the reporting year, a day
of January 1 is assumed. In this case a reporting year will coincide
with a calendar year. The format of a reporting year is YYYY-A1 (e.g.
2000-A1). Note that the period value of 1 is fixed.

| Derived by restriction of ReportPeriodValidTimeZoneType .
| Regular Expression Pattern: .{5}A1.\*

**ReportingSemesterType: **\ ReportingSemesterType defines a time period
of 6 months (P6M) in relation to a reporting year which has a start day
(day-month) specified in the specialized reporting year start day
attribute. In the absence of a start day for the reporting year, a day
of January 1 is assumed. The format of a reporting semester is YYYY-Ss
(e.g. 2000-S1), where s is either 1 or 2.

| Derived by restriction of ReportPeriodValidTimeZoneType .
| Regular Expression Pattern: .{5}S[1-2].\*

**ReportingTrimesterType: **\ ReportingTrimesterType defines a time
period of 4 months (P4M) in relation to a reporting year which has a
start day (day-month) specified in the specialized reporting year start
day attribute. In the absence of a start day for the reporting year, a
day of January 1 is assumed. The format of a reporting trimester is
YYYY-Tt (e.g. 2000-T1), where s is either 1, 2, or 3.

| Derived by restriction of ReportPeriodValidTimeZoneType .
| Regular Expression Pattern: .{5}T[1-3].\*

**ReportingQuarterType: **\ ReportingQuarterType defines a time period
of 3 months (P3M) in relation to a reporting year which has a start day
(day-month) specified in the specialized reporting year start day
attribute. In the absence of a start day for the reporting year, a day
of January 1 is assumed. The format of a reporting quarter is YYYY-Qq
(e.g. 2000-Q1), where q is a value between 1 and 4.

| Derived by restriction of ReportPeriodValidTimeZoneType .
| Regular Expression Pattern: .{5}Q[1-4].\*

**ReportingMonthType: **\ ReportingMonthType defines a time period of 1
month (P1M) in relation to a reporting year which has a start day
(day-month) specified in the specialized reporting year start day
attribute. In the absence of a start day for the reporting year, a day
of January 1 is assumed. In this case a reporting month will coincide
with a calendar month. The format of a reporting month is YYYY-Mmm (e.g.
2000-M01), where mm is a two digit month (i.e. 01-12).

| Derived by restriction of ReportPeriodValidTimeZoneType .
| Regular Expression Pattern: .{5}M(0[1-9]|1[0-2]).\*

**ReportingWeekType: **\ ReportingWeekType defines a time period of 7
days (P7D) in relation to a reporting year which has a start day
(day-month) specified in the specialized reporting year start day
attribute. A standard reporting week is based on the ISO 8601 defintion
of a week date, in relation to the reporting period start day. The first
week is defined as the week with the first Thursday on or after the
reporting year start day. An equivalent definition is the week starting
with the Monday nearest in time to the reporting year start day. There
are other equivalent defintions, all of which should be adjusted based
on the reporting year start day. In the absence of a start day for the
reporting year, a day of January 1 is assumed. The format of a reporting
week is YYYY-Www (e.g. 2000-W01), where mm is a two digit week (i.e.
01-53).

| Derived by restriction of ReportPeriodValidTimeZoneType .
| Regular Expression Pattern: .{5}W(0[1-9]|[1-4][0-9]|5[0-3]).\*

**ReportingDayType: **\ ReportingDayType defines a time period of 1 day
(P1D) in relation to a reporting year which has a start day (day-month)
specified in the specialized reporting year start day attribute. In the
absence of a start day for the reporting year, a day of January 1 is
assumed. The format of a reporting day is YYYY-Dddd (e.g. 2000-D001),
where ddd is a three digit day (i.e. 001-366).

| Derived by restriction of ReportPeriodValidTimeZoneType .
| Regular Expression
  Pattern: .{5}D(0[0-9][1-9]|[1-2][0-9][0-9]|3[0-5][0-9]|36[0-6]).\*

**BaseTimeRangeType: **\ BaseTimeRangeType is a simple type which frames
the general pattern for a time range in SDMX. A time range pattern is
generally described as [xs:date or xs:dateTime]\[xs:duration], where the
referenced types are defined by XML Schema. This type is meant to be
derived from for further validation.

| Derived by restriction of xs:string .
| Regular Expression
  Pattern: \d{4}\-\d{2}\-\d{2}(T\d{2}:\d{2}:\d{2}(\.\d+)?)?(Z|((\+|\-)\d{2}:\d{2}))?/P.+

**RangeValidMonthDayType: **\ RangeValidMonthDayType is a derivation of
the BaseTimeRangeType which validates that the day provided is valid for
the month, without regard to leap years. The base type will have
provided basic validation already. The patterns below validate that
there are up to 29 days in February, up to 30 days in April, June,
September, and November and up to 31 days in January, March, May, July,
August, October, and December. This type is meant to be derived from for
further validation.

| Derived by restriction of BaseTimeRangeType .
| Regular Expression
  Pattern: .{5}02\-(0[1-9]|[1-2][0-9]).+.{5}(04|06|09|11)\-(0[1-9]|[1-2][0-9]|30).+.{5}(01|03|05|07|08|10|12)\-(0[1-9]|[1-2][0-9]|3[0-1]).+

**RangeValidLeapYearType: **\ RangeValidLeapYearType is a derivation of
the RangeValidMonthDayType which validates that a date of February 29
occurs in a valid leap year (i.e. if the year is divisible 4 and not by
100, unless it is also divisible by 400). This type is meant to be
derived from for further validation.

| Derived by restriction of RangeValidMonthDayType .
| Regular Expression
  Pattern: ((\d{2}(04|08|12|16|20|24|28|32|36|40|44|48|52|56|60|64|68|72|76|80|84|88|92|96))|((00|04|08|12|16|20|24|28|32|36|40|44|48|52|56|60|64|68|72|76|80|84|88|92|96)00))\-02\-29.+.{5}02\-(([0-1][0-9])|(2[^9])).+.{5}((0[1,3-9])|1[0-2]).+

**RangeValidTimeType: **\ RangeValidTimeType is a derivation of the
RangeValidLeapYearType which validates that the time (if provided) is
validly formatted. The base type will have provided basic validation
already. The patterns below validate that the time falls between
00:00:00 and 24:00:00. Note that as the XML dateTime type does, seconds
are required. It is also permissible to have fractions of seconds, but
only within the boundaries of the range specified. This type is meant to
be derived from for further validation.

| Derived by restriction of RangeValidLeapYearType .
| Regular Expression
  Pattern: .{10}T(24:00:00(\.[0]+)?|((([0-1][0-9])|(2[0-3])):[0-5][0-9]:[0-5][0-9](\.\d+)?))(/|Z|\+|\-).+[^T]+/.+

**RangeValidTimeZoneType: **\ RangeValidMonthDayType is a derivation of
the RangeValidTimeType which validates that the time zone provided in
the base type is valid. The base type will have provided basic
validation already. The patterns below validate that the time zone is
"Z" or that it is between -14:00 and +14:00, or that there is no time
zone provided. This type is meant to be derived from for further
validation.

| Derived by restriction of RangeValidTimeType .
| Regular Expression
  Pattern: .+Z/.+.{10}.*(\+|\-)(14:00|((0[0-9]|1[0-3]):[0-5][0-9]))/.+.{10}[^\+\-Z]+

**TimeRangeValidDateDurationType: **\ TimeRangeValidDateDurationType is
an abstract derivation of the RangeValidTimeType which validates that
duration provided is generally valid, up to the time component.

| Derived by restriction of RangeValidTimeZoneType .
| Regular Expression Pattern: .+/P(\d+Y)?(\d+M)?(\d+D)?(T.+)?

**TimeRangeType: **\ TimeRangeType defines the structure of a time range
in SDMX. The pattern of a time range can be generally described as
[start date]\[duration], where start date is an date or dateTime type as
defined in XML Schema and duration is a time duration as defined in XML
Schema. Note that it is permissible for a time zone offset to be
provided on the date or date time.

| Derived by restriction of TimeRangeValidDateDurationType .
| Regular Expression
  Pattern: .+/P.*T(\d+H)?(\d+M)?(\d+(.\d+)?S)?.+/P[^T]+

**TimezoneType: **\ TimezoneType defines the pattern for a time zone. An
offset of -14:00 to +14:00 or Z can be specified.

| Derived by restriction of xs:string .
| Regular Expression
  Pattern: Z(\+|\-)(14:00|((0[0-9]|1[0-3]):[0-5][0-9]))

**OccurenceType: **\ OccurenceType is used to express the maximum
occurrence of an object. It combines an integer, greater than 1, and the
literal text, "unbounded", for objects which have no upper limit on its
occurrence.

Union of:

MaxOccursNumberType, UnboundedCodeType.

**MaxOccursNumberType: **\ MaxOccursNumberType is a base type used to
restrict an integer to be greater than 1, for the purpose of expressing
the maximum number of occurrences of an object.

| Derived by restriction of xs:nonNegativeInteger .
| Minimum (inclusive): 1
| Fraction Digits: 0

**UnboundedCodeType: **\ UnboundedCodeType provides single textual value
of "unbounded", for use in OccurentType.

Derived by restriction of xs:string .

Enumerations:

========= =========================================
**Value** **Documentation**
========= =========================================
unbounded Object has no upper limit on occurrences.
========= =========================================

**ActionType: **\ ActionType provides a list of actions, describing the
intention of the data transmission from the sender's side. Each action
provided at the data or metadata set level applies to the entire data
set for which it is given. Note that the actions indicated in the
Message Header are optional, and used to summarize specific actions
indicated with this data type for all registry interactions. The
"Informational" value is used when the message contains information in
response to a query, rather than being used to invoke a maintenance
activity.

Derived by restriction of xs:NMTOKEN .

Enumerations:

=========== =======================================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Value**   **Documentation**
=========== =======================================================================================================================================================================================================================================================================================================================================================================================================================================================================
Append      Append - this is an incremental update for an existing data/metadata set or the provision of new data or documentation (attribute values) formerly absent. If any of the supplied data or metadata is already present, it will not replace that data or metadata. This corresponds to the "Update" value found in version 1.0 of the SDMX Technical Standards.
Replace     Replace - data/metadata is to be replaced, and may also include additional data/metadata to be appended. The replacement occurs at the level of the observation - that is, it is not possible to replace an entire series.
Delete      Delete - data/metadata is to be deleted. Deletion occurs at the lowest level object. For instance, if a delete data message contains a series with no observations, then the entire series will be deleted. If the series contains observations, then only those observations specified will be deleted. The same basic concept applies for attributes. If a series or observation in a delete message contains attributes, then only those attributes will be deleted.
Information Informational - data/metadata is being exchanged for informational purposes only, and not meant to update a system.
=========== =======================================================================================================================================================================================================================================================================================================================================================================================================================================================================

**WildCardValueType: **\ WildCardValueType is a single value code list,
used to include the '%' character - indicating that an entire field is
wild carded.

Derived by restriction of xs:string .

Enumerations:

========= ============================
**Value** **Documentation**
========= ============================
%         Indicates a wild card value.
========= ============================

**DimensionTypeType: **\ DimensionTypeType enumerates the sub-classes of
a dimension.

Derived by restriction of xs:string .

Enumerations:

================ ======================
**Value**        **Documentation**
================ ======================
Dimension        An ordinary dimension.
MeasureDimension A measure dimension.
TimeDimension    The time dimension.
================ ======================

**ContentConstraintTypeCodeType: **\ ContentConstraintTypeCodeType
defines a list of types for a content constraint. A content constraint
can state which data is present or which content is allowed for the
constraint attachment.

Derived by restriction of xs:string .

Enumerations:

========= ===========================================================================
**Value** **Documentation**
========= ===========================================================================
Allowed   The constraint contains the allowed values for attachable object.
Actual    The constraints contains the actual data present for the attachable object.
========= ===========================================================================

**SimpleOperatorType: **\ SimpleOperatorType provides an enumeration of
simple operators to be applied to any value.

Derived by restriction of xs:string .

Enumerations:

========= ========================================================
**Value** **Documentation**
========= ========================================================
notEqual  (!=) - value must not be equal to the value supplied.
equal     (=) - value must be exactly equal to the value supplied.
========= ========================================================

**RangeOperatorType: **\ RangeOperatorType provides an enumeration of
range operators to be applied to an ordered value.

Derived by restriction of xs:string .

Enumerations:

================== =================================================================
**Value**          **Documentation**
================== =================================================================
greaterThanOrEqual (>=) - value must be greater than or equal to the value supplied.
lessThanOrEqual    (<=) - value must be less than or equal to the value supplied.
greaterThan        (>) - value must be greater than the value supplied.
lessThan           (<) - value must be less than the value supplied.
================== =================================================================

**TextSearchOperatorType: **\ TextSearchOperatorType provides an
enumeration of text search operators.

Derived by restriction of xs:string .

Enumerations:

================ ============================================================
**Value**        **Documentation**
================ ============================================================
contains         The text being searched must contain the supplied text.
startsWith       The text being searched must start with the supplied text.
endsWith         The text being searched must end with the supplied text.
doesNotContain   The text being searched cannot contain the supplied text.
doesNotStartWith The text being searched cannot start with the supplied text.
doesNotEndWith   The text being searched cannot end with the supplied text.
================ ============================================================

**OrderedOperatorType: **\ OrderedOperatorType combines the
SimpleOperatorType and the RangeOperatorType to provide a full range or
operators for any ordered value.

Union of:

SimpleOperatorType, RangeOperatorType.

**TextOperatorType: **

Union of:

SimpleOperatorType, TextSearchOperatorType.

**TimeOperatorType: **\ TimeOperatorType derives from the
OrderedOperatorType to remove the notEqual operator.

Derived by restriction of OrderedOperatorType .

Enumerations:

================== =================
**Value**          **Documentation**
================== =================
equal             
greaterThanOrEqual
lessThanOrEqual   
greaterThan       
lessThan          
================== =================

**ObservationDimensionType: **\ ObservationDimensionType allows for the
dimension at the observation level to be specified by either providing
the dimension identifier or using the explicit value "AllDimensions".

Union of:

NCNameIDType, ObsDimensionsCodeType.

**ObsDimensionsCodeType: **\ ObsDimensionsCodeType is an enumeration
containing the values "TimeDimension" and "AllDimensions"

Derived by restriction of xs:string .

Enumerations:

============= =======================================================================================================================================
**Value**     **Documentation**
============= =======================================================================================================================================
AllDimensions AllDimensions notes that the cross sectional format shall be flat; that is all dimensions should be contained at the observation level.
TIME_PERIOD   TIME_PERIOD refers to the fixed identifier for the time dimension.
============= =======================================================================================================================================

**DataType: **\ DataTypeType provides an enumerated list of the types of
data formats allowed as the for the representation of an object.

Derived by restriction of xs:NMTOKEN .

Enumerations:

============================= =======================================================================================================================================================================================================================================================================================================
**Value**                     **Documentation**
============================= =======================================================================================================================================================================================================================================================================================================
String                        A string datatype corresponding to W3C XML Schema's xs:string datatype.
Alpha                         A string datatype which only allows for the simple aplhabetic charcter set of A-z.
AlphaNumeric                  A string datatype which only allows for the simple alphabetic character set of A-z plus the simple numeric character set of 0-9.
Numeric                       A string datatype which only allows for the simple numeric character set of 0-9. This format is not treated as an integer, and therefore can having leading zeros.
BigInteger                    An integer datatype corresponding to W3C XML Schema's xs:integer datatype.
Integer                       An integer datatype corresponding to W3C XML Schema's xs:int datatype.
Long                          A numeric datatype corresponding to W3C XML Schema's xs:long datatype.
Short                         A numeric datatype corresponding to W3C XML Schema's xs:short datatype.
Decimal                       A numeric datatype corresponding to W3C XML Schema's xs:decimal datatype.
Float                         A numeric datatype corresponding to W3C XML Schema's xs:float datatype.
Double                        A numeric datatype corresponding to W3C XML Schema's xs:double datatype.
Boolean                       A datatype corresponding to W3C XML Schema's xs:boolean datatype.
URI                           A datatype corresponding to W3C XML Schema's xs:anyURI datatype.
Count                         A simple incrementing Integer type. The isSequence facet must be set to true, and the interval facet must be set to "1".
InclusiveValueRange           This value indicates that the startValue and endValue attributes provide the inclusive boundaries of a numeric range of type xs:decimal.
ExclusiveValueRange           This value indicates that the startValue and endValue attributes provide the exclusive boundaries of a numeric range, of type xs:decimal.
Incremental                   This value indicates that the value increments according to the value provided in the interval facet, and has a true value for the isSequence facet.
ObservationalTimePeriod       Observational time periods are the superset of all time periods in SDMX. It is the union of the standard time periods (i.e. Gregorian time periods, the reporting time periods, and date time) and a time range.
StandardTimePeriod            Standard time periods is a superset of distinct time period in SDMX. It is the union of the basic time periods (i.e. the Gregorian time periods and date time) and the reporting time periods.
BasicTimePeriod               BasicTimePeriod time periods is a superset of the Gregorian time periods and a date time.
GregorianTimePeriod           Gregorian time periods correspond to calendar periods and are represented in ISO-8601 formats. This is the union of the year, year month, and date formats.
GregorianYear                 A Gregorian time period corresponding to W3C XML Schema's xs:gYear datatype, which is based on ISO-8601.
GregorianYearMonth            A time datatype corresponding to W3C XML Schema's xs:gYearMonth datatype, which is based on ISO-8601.
GregorianDay                  A time datatype corresponding to W3C XML Schema's xs:date datatype, which is based on ISO-8601.
ReportingTimePeriod           Reporting time periods represent periods of a standard length within a reporting year, where to start of the year (defined as a month and day) must be defined elsewhere or it is assumed to be January 1. This is the union of the reporting year, semester, trimester, quarter, month, week, and day.
ReportingYear                 A reporting year represents a period of 1 year (P1Y) from the start date of the reporting year. This is expressed as using the SDMX specific ReportingYearType.
ReportingSemester             A reporting semester represents a period of 6 months (P6M) from the start date of the reporting year. This is expressed as using the SDMX specific ReportingSemesterType.
ReportingTrimester            A reporting trimester represents a period of 4 months (P4M) from the start date of the reporting year. This is expressed as using the SDMX specific ReportingTrimesterType.
ReportingQuarter              A reporting quarter represents a period of 3 months (P3M) from the start date of the reporting year. This is expressed as using the SDMX specific ReportingQuarterType.
ReportingMonth                A reporting month represents a period of 1 month (P1M) from the start date of the reporting year. This is expressed as using the SDMX specific ReportingMonthType.
ReportingWeek                 A reporting week represents a period of 7 days (P7D) from the start date of the reporting year. This is expressed as using the SDMX specific ReportingWeekType.
ReportingDay                  A reporting day represents a period of 1 day (P1D) from the start date of the reporting year. This is expressed as using the SDMX specific ReportingDayType.
DateTime                      A time datatype corresponding to W3C XML Schema's xs:dateTime datatype.
TimeRange                     TimeRange defines a time period by providing a distinct start (date or date time) and a duration.
Month                         A time datatype corresponding to W3C XML Schema's xs:gMonth datatype.
MonthDay                      A time datatype corresponding to W3C XML Schema's xs:gMonthDay datatype.
Day                           A time datatype corresponding to W3C XML Schema's xs:gDay datatype.
Time                          A time datatype corresponding to W3C XML Schema's xs:time datatype.
Duration                      A time datatype corresponding to W3C XML Schema's xs:duration datatype.
XHTML                         This value indicates that the content of the component can contain XHTML markup.
KeyValues                     This value indicates that the content of the component will be data key (a set of dimension references and values for the dimensions).
IdentifiableReference         This value indicates that the content of the component will be complete reference (either URN or full set of reference fields) to an Identifiable object in the SDMX Information Model.
DataSetReference              This value indicates that the content of the component will be reference to a data provider, which is actually a formal reference to a data provider and a data set identifier value.
AttachmentConstraintReference This value indicates that the content of the component will be reference to an attachment constraint, which is actually a combination of a collection of full or partial key values and a reference to a data set or data structure, usage, or provision agreement.
============================= =======================================================================================================================================================================================================================================================================================================

**BasicComponentDataType: **\ BasicComponentDataType provides an
enumerated list of the types of characters allowed in the textType
attribute for all non-target object components.

Derived by restriction of DataType .

Enumerations:

======================= =======================================================================================================================================================================================================================================================================================================
**Value**               **Documentation**
======================= =======================================================================================================================================================================================================================================================================================================
String                  A string datatype corresponding to W3C XML Schema's xs:string datatype.
Alpha                   A string datatype which only allows for the simple aplhabetic charcter set of A-z.
AlphaNumeric            A string datatype which only allows for the simple alphabetic character set of A-z plus the simple numeric character set of 0-9.
Numeric                 A string datatype which only allows for the simple numeric character set of 0-9. This format is not treated as an integer, and therefore can having leading zeros.
BigInteger              An integer datatype corresponding to W3C XML Schema's xs:integer datatype.
Integer                 An integer datatype corresponding to W3C XML Schema's xs:int datatype.
Long                    A numeric datatype corresponding to W3C XML Schema's xs:long datatype.
Short                   A numeric datatype corresponding to W3C XML Schema's xs:short datatype.
Decimal                 A numeric datatype corresponding to W3C XML Schema's xs:decimal datatype.
Float                   A numeric datatype corresponding to W3C XML Schema's xs:float datatype.
Double                  A numeric datatype corresponding to W3C XML Schema's xs:double datatype.
Boolean                 A datatype corresponding to W3C XML Schema's xs:boolean datatype.
URI                     A datatype corresponding to W3C XML Schema's xs:anyURI datatype.
Count                   A simple incrementing Integer type. The isSequence facet must be set to true, and the interval facet must be set to "1".
InclusiveValueRange     This value indicates that the startValue and endValue attributes provide the inclusive boundaries of a numeric range of type xs:decimal.
ExclusiveValueRange     This value indicates that the startValue and endValue attributes provide the exclusive boundaries of a numeric range, of type xs:decimal.
Incremental             This value indicates that the value increments according to the value provided in the interval facet, and has a true value for the isSequence facet.
ObservationalTimePeriod Observational time periods are the superset of all time periods in SDMX. It is the union of the standard time periods (i.e. Gregorian time periods, the reporting time periods, and date time) and a time range.
StandardTimePeriod      Standard time periods is a superset of distinct time period in SDMX. It is the union of the basic time periods (i.e. the Gregorian time periods and date time) and the reporting time periods.
BasicTimePeriod         BasicTimePeriod time periods is a superset of the Gregorian time periods and a date time.
GregorianTimePeriod     Gregorian time periods correspond to calendar periods and are represented in ISO-8601 formats. This is the union of the year, year month, and date formats.
GregorianYear           A Gregorian time period corresponding to W3C XML Schema's xs:gYear datatype, which is based on ISO-8601.
GregorianYearMonth      A time datatype corresponding to W3C XML Schema's xs:gYearMonth datatype, which is based on ISO-8601.
GregorianDay            A time datatype corresponding to W3C XML Schema's xs:date datatype, which is based on ISO-8601.
ReportingTimePeriod     Reporting time periods represent periods of a standard length within a reporting year, where to start of the year (defined as a month and day) must be defined elsewhere or it is assumed to be January 1. This is the union of the reporting year, semester, trimester, quarter, month, week, and day.
ReportingYear           A reporting year represents a period of 1 year (P1Y) from the start date of the reporting year. This is expressed as using the SDMX specific ReportingYearType.
ReportingSemester       A reporting semester represents a period of 6 months (P6M) from the start date of the reporting year. This is expressed as using the SDMX specific ReportingSemesterType.
ReportingTrimester      A reporting trimester represents a period of 4 months (P4M) from the start date of the reporting year. This is expressed as using the SDMX specific ReportingTrimesterType.
ReportingQuarter        A reporting quarter represents a period of 3 months (P3M) from the start date of the reporting year. This is expressed as using the SDMX specific ReportingQuarterType.
ReportingMonth          A reporting month represents a period of 1 month (P1M) from the start date of the reporting year. This is expressed as using the SDMX specific ReportingMonthType.
ReportingWeek           A reporting week represents a period of 7 days (P7D) from the start date of the reporting year. This is expressed as using the SDMX specific ReportingWeekType.
ReportingDay            A reporting day represents a period of 1 day (P1D) from the start date of the reporting year. This is expressed as using the SDMX specific ReportingDayType.
DateTime                A time datatype corresponding to W3C XML Schema's xs:dateTime datatype.
TimeRange               TimeRange defines a time period by providing a distinct start (date or date time) and a duration.
Month                   A time datatype corresponding to W3C XML Schema's xs:gMonth datatype.
MonthDay                A time datatype corresponding to W3C XML Schema's xs:gMonthDay datatype.
Day                     A time datatype corresponding to W3C XML Schema's xs:gDay datatype.
Time                    A time datatype corresponding to W3C XML Schema's xs:time datatype.
Duration                A time datatype corresponding to W3C XML Schema's xs:duration datatype.
XHTML                   This value indicates that the content of the component can contain XHTML markup.
======================= =======================================================================================================================================================================================================================================================================================================

**SimpleDataType: **\ SimpleDataType restricts BasicComponentDataType to
specify the allowable data types for a data structure definition
component. The XHTML representation is removed as a possible type.

Derived by restriction of BasicComponentDataType .

Enumerations:

======================= =======================================================================================================================================================================================================================================================================================================
**Value**               **Documentation**
======================= =======================================================================================================================================================================================================================================================================================================
String                  A string datatype corresponding to W3C XML Schema's xs:string datatype.
Alpha                   A string datatype which only allows for the simple aplhabetic charcter set of A-z.
AlphaNumeric            A string datatype which only allows for the simple alphabetic character set of A-z plus the simple numeric character set of 0-9.
Numeric                 A string datatype which only allows for the simple numeric character set of 0-9. This format is not treated as an integer, and therefore can having leading zeros.
BigInteger              An integer datatype corresponding to W3C XML Schema's xs:integer datatype.
Integer                 An integer datatype corresponding to W3C XML Schema's xs:int datatype.
Long                    A numeric datatype corresponding to W3C XML Schema's xs:long datatype.
Short                   A numeric datatype corresponding to W3C XML Schema's xs:short datatype.
Decimal                 A numeric datatype corresponding to W3C XML Schema's xs:decimal datatype.
Float                   A numeric datatype corresponding to W3C XML Schema's xs:float datatype.
Double                  A numeric datatype corresponding to W3C XML Schema's xs:double datatype.
Boolean                 A datatype corresponding to W3C XML Schema's xs:boolean datatype.
URI                     A datatype corresponding to W3C XML Schema's xs:anyURI datatype.
Count                   A simple incrementing Integer type. The isSequence facet must be set to true, and the interval facet must be set to "1".
InclusiveValueRange     This value indicates that the startValue and endValue attributes provide the inclusive boundaries of a numeric range of type xs:decimal.
ExclusiveValueRange     This value indicates that the startValue and endValue attributes provide the exclusive boundaries of a numeric range, of type xs:decimal.
Incremental             This value indicates that the value increments according to the value provided in the interval facet, and has a true value for the isSequence facet.
ObservationalTimePeriod Observational time periods are the superset of all time periods in SDMX. It is the union of the standard time periods (i.e. Gregorian time periods, the reporting time periods, and date time) and a time range.
StandardTimePeriod      Standard time periods is a superset of distinct time period in SDMX. It is the union of the basic time periods (i.e. the Gregorian time periods and date time) and the reporting time periods.
BasicTimePeriod         BasicTimePeriod time periods is a superset of the Gregorian time periods and a date time.
GregorianTimePeriod     Gregorian time periods correspond to calendar periods and are represented in ISO-8601 formats. This is the union of the year, year month, and date formats.
GregorianYear           A Gregorian time period corresponding to W3C XML Schema's xs:gYear datatype, which is based on ISO-8601.
GregorianYearMonth      A time datatype corresponding to W3C XML Schema's xs:gYearMonth datatype, which is based on ISO-8601.
GregorianDay            A time datatype corresponding to W3C XML Schema's xs:date datatype, which is based on ISO-8601.
ReportingTimePeriod     Reporting time periods represent periods of a standard length within a reporting year, where to start of the year (defined as a month and day) must be defined elsewhere or it is assumed to be January 1. This is the union of the reporting year, semester, trimester, quarter, month, week, and day.
ReportingYear           A reporting year represents a period of 1 year (P1Y) from the start date of the reporting year. This is expressed as using the SDMX specific ReportingYearType.
ReportingSemester       A reporting semester represents a period of 6 months (P6M) from the start date of the reporting year. This is expressed as using the SDMX specific ReportingSemesterType.
ReportingTrimester      A reporting trimester represents a period of 4 months (P4M) from the start date of the reporting year. This is expressed as using the SDMX specific ReportingTrimesterType.
ReportingQuarter        A reporting quarter represents a period of 3 months (P3M) from the start date of the reporting year. This is expressed as using the SDMX specific ReportingQuarterType.
ReportingMonth          A reporting month represents a period of 1 month (P1M) from the start date of the reporting year. This is expressed as using the SDMX specific ReportingMonthType.
ReportingWeek           A reporting week represents a period of 7 days (P7D) from the start date of the reporting year. This is expressed as using the SDMX specific ReportingWeekType.
ReportingDay            A reporting day represents a period of 1 day (P1D) from the start date of the reporting year. This is expressed as using the SDMX specific ReportingDayType.
DateTime                A time datatype corresponding to W3C XML Schema's xs:dateTime datatype.
TimeRange               TimeRange defines a time period by providing a distinct start (date or date time) and a duration.
Month                   A time datatype corresponding to W3C XML Schema's xs:gMonth datatype.
MonthDay                A time datatype corresponding to W3C XML Schema's xs:gMonthDay datatype.
Day                     A time datatype corresponding to W3C XML Schema's xs:gDay datatype.
Time                    A time datatype corresponding to W3C XML Schema's xs:time datatype.
Duration                A time datatype corresponding to W3C XML Schema's xs:duration datatype.
======================= =======================================================================================================================================================================================================================================================================================================

**TimeDataType: **\ TimeDataType restricts SimpleDataType to specify the
allowable data types for representing a time value.

Derived by restriction of SimpleDataType .

Enumerations:

======================= =======================================================================================================================================================================================================================================================================================================
**Value**               **Documentation**
======================= =======================================================================================================================================================================================================================================================================================================
ObservationalTimePeriod Observational time periods are the superset of all time periods in SDMX. It is the union of the standard time periods (i.e. Gregorian time periods, the reporting time periods, and date time) and a time range.
StandardTimePeriod      Standard time periods is a superset of distinct time period in SDMX. It is the union of the basic time periods (i.e. the Gregorian time periods and date time) and the reporting time periods.
BasicTimePeriod         BasicTimePeriod time periods is a superset of the Gregorian time periods and a date time.
GregorianTimePeriod     Gregorian time periods correspond to calendar periods and are represented in ISO-8601 formats. This is the union of the year, year month, and date formats.
GregorianYear           A Gregorian time period corresponding to W3C XML Schema's xs:gYear datatype, which is based on ISO-8601.
GregorianYearMonth      A time datatype corresponding to W3C XML Schema's xs:gYearMonth datatype, which is based on ISO-8601.
GregorianDay            A time datatype corresponding to W3C XML Schema's xs:date datatype, which is based on ISO-8601.
ReportingTimePeriod     Reporting time periods represent periods of a standard length within a reporting year, where to start of the year (defined as a month and day) must be defined elsewhere or it is assumed to be January 1. This is the union of the reporting year, semester, trimester, quarter, month, week, and day.
ReportingYear           A reporting year represents a period of 1 year (P1Y) from the start date of the reporting year. This is expressed as using the SDMX specific ReportingYearType.
ReportingSemester       A reporting semester represents a period of 6 months (P6M) from the start date of the reporting year. This is expressed as using the SDMX specific ReportingSemesterType.
ReportingTrimester      A reporting trimester represents a period of 4 months (P4M) from the start date of the reporting year. This is expressed as using the SDMX specific ReportingTrimesterType.
ReportingQuarter        A reporting quarter represents a period of 3 months (P3M) from the start date of the reporting year. This is expressed as using the SDMX specific ReportingQuarterType.
ReportingMonth          A reporting month represents a period of 1 month (P1M) from the start date of the reporting year. This is expressed as using the SDMX specific ReportingMonthType.
ReportingWeek           A reporting week represents a period of 7 days (P7D) from the start date of the reporting year. This is expressed as using the SDMX specific ReportingWeekType.
ReportingDay            A reporting day represents a period of 1 day (P1D) from the start date of the reporting year. This is expressed as using the SDMX specific ReportingDayType.
DateTime                A time datatype corresponding to W3C XML Schema's xs:dateTime datatype.
TimeRange               TimeRange defines a time period by providing a distinct start (date or date time) and a duration.
======================= =======================================================================================================================================================================================================================================================================================================

**NestedIDType: **\ NestedIDType is the least restrictive form of an
identifier used throughout all SDMX-ML messages. It allows for a
hierarchical identifier, with each portion separated by the '.'
character. For the identifier portions, valid characters include A-Z,
a-z, @, 0-9, \_, -, $.

| Derived by restriction of xs:string .
| Regular Expression Pattern: [A-z0-9_@$\-]+(\.[A-z0-9_@$\-]+)\*

**TwoLevelIDType: **\ TwoLevelIDType defines an identifier with exactly
two levels.

| Derived by restriction of NestedIDType .
| Regular Expression Pattern: [A-z0-9_@$\-]+\.[A-z0-9_@$\-]+

**IDType: **\ IDType provides a type which is used for restricting the
characters in codes and IDs throughout all SDMX-ML messages. Valid
characters include A-Z, a-z, @, 0-9, \_, -, $.

| Derived by restriction of NestedIDType .
| Regular Expression Pattern: [A-z0-9_@$\-]+

**NCNameIDType: **\ NCNameIDType restricts the IDType, so that the id
may be used to generate valid XML components. IDs created from this type
conform to the W3C XML Schema NCNAME type, and therefore can be used as
element or attribute names.

| Derived by restriction of IDType .
| Regular Expression Pattern: [A-z][A-z0-9_\-]\*

**NestedNCNameIDType: **\ NestedNCNameIDType restricts the NestedIDType,
so that the id may be used to generate valid XML components. IDs created
from this type conform to the W3C XML Schema NCNAME type, and therefore
can be used as element or attribute names.

| Derived by restriction of NestedIDType .
| Regular Expression Pattern: [A-z][A-z0-9_\-]*(\.[A-z][A-z0-9_\-]*)\*

**SingleNCNameIDType: **\ SingleNCNameIDType restricts the
NestedNCNameIDType to allow only one level. Note that this is the same
pattern as the NCNameIDType, but can be used when the base type to be
restricted is a nested NCNameIDType (where as the NCNameIDType could
only restrict the IDType).

| Derived by restriction of NestedNCNameIDType .
| Regular Expression Pattern: [A-z][A-z0-9_\-]\*

**VersionType: **\ VersionType is used to communicate version
information. The format is restricted to allow for simple incrementing
and sorting of version number. The version consists of an unlimited set
of numeric components, separated by the '.' character. When processing
version, each numeric component (the number preceding and following any
'.' character) should be parsed as an integer. Thus, a version of 1.3
and 1.03 would be equivalent, as both the '3' component and the '03'
component would parse to an integer value of 3.

| Derived by restriction of xs:string .
| Regular Expression Pattern: [0-9]+(\.[0-9]+)\*

**VersionQueryType: **\ VersionQueryType combines the VersionType and
LateBoundVersionType to allow one to query for either a specific version
of an object, or the latest version by specifying the '*' value.

Union of:

VersionType, LateBoundVersionType.

**LateBoundVersionType: **\ LateBoundVersionType is a single value code
list, used to include the '*' character - indicating that the latest
version of an object is required.

Derived by restriction of xs:string .

Enumerations:

========= ============================================================
**Value** **Documentation**
========= ============================================================
\*        Indicates that the latest version of an object is requested.
========= ============================================================

**PackageTypeCodelistType: **\ PackageTypeCodelistType provides an
enumeration of all SDMX package names.

Derived by restriction of xs:string .

Enumerations:

================= =================
**Value**         **Documentation**
================= =================
base             
datastructure    
metadatastructure
process          
registry         
mapping          
codelist         
categoryscheme   
conceptscheme    
================= =================

**ItemSchemePackageTypeCodelistType: **\ ItemSchemePackageTypeCodelistType
provides an enumeration of all SDMX packages which contain item schemes.

Derived by restriction of PackageTypeCodelistType .

Enumerations:

============== =================
**Value**      **Documentation**
============== =================
base          
codelist      
categoryscheme
conceptscheme 
============== =================

**StructurePackageTypeCodelistType: **\ StructurePackageTypeCodelistType
provides an enumeration of all SDMX packages which contain structure and
structure usages.

Derived by restriction of PackageTypeCodelistType .

Enumerations:

================= =================
**Value**         **Documentation**
================= =================
datastructure    
metadatastructure
================= =================

**ObjectTypeCodelistType: **\ ObjectTypeCodelistType provides an
enumeration of all objects outside of the base infomration model class.
This includes some abstract object types such as Organsiation and
Constraint.

Derived by restriction of xs:string .

Enumerations:

=============================== =================
**Value**                       **Documentation**
=============================== =================
Any                            
Agency                         
AgencyScheme                   
AttachmentConstraint           
Attribute                      
AttributeDescriptor            
Categorisation                 
Category                       
CategorySchemeMap              
CategoryScheme                 
Code                           
CodeMap                        
Codelist                       
CodelistMap                    
ComponentMap                   
Concept                        
ConceptMap                     
ConceptScheme                  
ConceptSchemeMap               
Constraint                     
ConstraintTarget               
ContentConstraint              
Dataflow                       
DataConsumer                   
DataConsumerScheme             
DataProvider                   
DataProviderScheme             
DataSetTarget                  
DataStructure                  
Dimension                      
DimensionDescriptor            
DimensionDescriptorValuesTarget
GroupDimensionDescriptor       
HierarchicalCode               
HierarchicalCodelist           
Hierarchy                      
HybridCodelistMap              
HybridCodeMap                  
IdentifiableObjectTarget       
Level                          
MeasureDescriptor              
MeasureDimension               
Metadataflow                   
MetadataAttribute              
MetadataSet                    
MetadataStructure              
MetadataTarget                 
Organisation                   
OrganisationMap                
OrganisationScheme             
OrganisationSchemeMap          
OrganisationUnit               
OrganisationUnitScheme         
PrimaryMeasure                 
Process                        
ProcessStep                    
ProvisionAgreement             
ReportingCategory              
ReportingCategoryMap           
ReportingTaxonomy              
ReportingTaxonomyMap           
ReportingYearStartDay          
ReportPeriodTarget             
ReportStructure                
StructureMap                   
StructureSet                   
TimeDimension                  
Transition                     
=============================== =================

**MaintainableTypeCodelistType: **\ MaintainableTypeCodelistType
provides an enumeration of all maintainable objects.

Derived by restriction of ObjectTypeCodelistType .

Enumerations:

====================== =================
**Value**              **Documentation**
====================== =================
Any                   
AgencyScheme          
AttachmentConstraint  
Categorisation        
CategoryScheme        
Codelist              
ConceptScheme         
Constraint            
ContentConstraint     
Dataflow              
DataConsumerScheme    
DataProviderScheme    
DataStructure         
HierarchicalCodelist  
Metadataflow          
MetadataStructure     
OrganisationScheme    
OrganisationUnitScheme
Process               
ProvisionAgreement    
ReportingTaxonomy     
StructureSet          
====================== =================

**ConcreteMaintainableTypeCodelistType: **\ ConcreteMaintainableTypeCodelistType
provides an enumeration of all concrete maintainable objects.

Derived by restriction of MaintainableTypeCodelistType .

Enumerations:

====================== =================
**Value**              **Documentation**
====================== =================
AgencyScheme          
AttachmentConstraint  
Categorisation        
CategoryScheme        
Codelist              
ConceptScheme         
ContentConstraint     
Dataflow              
DataConsumerScheme    
DataProviderScheme    
DataStructure         
HierarchicalCodelist  
Metadataflow          
MetadataStructure     
OrganisationUnitScheme
Process               
ProvisionAgreement    
ReportingTaxonomy     
StructureSet          
====================== =================

**CodelistTypeCodelistType: **\ CodelistTypeCodelistType provides an
enumeration of all codelist objects.

Derived by restriction of MaintainableTypeCodelistType .

Enumerations:

==================== =================
**Value**            **Documentation**
==================== =================
Codelist            
HierarchicalCodelist
==================== =================

**CodeTypeCodelistType: **\ CodeTypeCodelistType provides an enumeration
of all code objects.

Derived by restriction of ObjectTypeCodelistType .

Enumerations:

================ =================
**Value**        **Documentation**
================ =================
Code            
HierarchicalCode
================ =================

**ConstraintTypeCodelistType: **\ ConstraintTypeCodelistType provides an
enumeration of all constraint objects.

Derived by restriction of MaintainableTypeCodelistType .

Enumerations:

==================== =================
**Value**            **Documentation**
==================== =================
AttachmentConstraint
ContentConstraint   
==================== =================

**ItemSchemeTypeCodelistType: **\ ItemSchemeTypeCodelistType provides an
enumeration of all item scheme objects.

Derived by restriction of MaintainableTypeCodelistType .

Enumerations:

====================== =================
**Value**              **Documentation**
====================== =================
AgencyScheme          
CategoryScheme        
Codelist              
ConceptScheme         
DataConsumerScheme    
DataProviderScheme    
OrganisationUnitScheme
ReportingTaxonomy     
====================== =================

**OrganisationSchemeTypeCodelistType: **\ OrganisationSchemeTypeCodelistType
provides an enumeration of all organisation scheme objects.

Derived by restriction of ItemSchemeTypeCodelistType .

Enumerations:

====================== =================
**Value**              **Documentation**
====================== =================
AgencyScheme          
DataConsumerScheme    
DataProviderScheme    
OrganisationUnitScheme
====================== =================

**OrganisationTypeCodelistType: **\ OrganisationTypeCodelistType
provides an enumeration of all organisation objects.

Derived by restriction of ItemTypeCodelistType .

Enumerations:

================ =================
**Value**        **Documentation**
================ =================
Agency          
DataConsumer    
DataProvider    
OrganisationUnit
================ =================

**StructureOrUsageTypeCodelistType: **\ StructureOrUsageTypeCodelistType
provides an enumeration all structure and structure usage objects

Derived by restriction of MaintainableTypeCodelistType .

Enumerations:

================= =================
**Value**         **Documentation**
================= =================
Dataflow         
DataStructure    
Metadataflow     
MetadataStructure
================= =================

**StructureTypeCodelistType: **\ StructureTypeCodelistType provides an
enumeration all structure objects

Derived by restriction of StructureOrUsageTypeCodelistType .

Enumerations:

================= =================
**Value**         **Documentation**
================= =================
DataStructure    
MetadataStructure
================= =================

**StructureUsageTypeCodelistType: **\ StructureUsageTypeCodelistType
provides an enumeration all structure usage objects

Derived by restriction of StructureOrUsageTypeCodelistType .

Enumerations:

============ =================
**Value**    **Documentation**
============ =================
Dataflow    
Metadataflow
============ =================

**ItemTypeCodelistType: **\ ItemTypeCodelistType provides an enumeration
of all item objects.

Derived by restriction of ObjectTypeCodelistType .

Enumerations:

================= =================
**Value**         **Documentation**
================= =================
Agency           
Category         
Code             
Concept          
DataConsumer     
DataProvider     
OrganisationUnit 
ReportingCategory
================= =================

**ComponentListTypeCodelistType: **\ ComponentListTypeCodelistType
provides an enumeration of all component list objects.

Derived by restriction of ObjectTypeCodelistType .

Enumerations:

======================== =================
**Value**                **Documentation**
======================== =================
AttributeDescriptor     
DimensionDescriptor     
GroupDimensionDescriptor
MeasureDescriptor       
MetadataTarget          
ReportStructure         
======================== =================

**ComponentTypeCodelistType: **\ ComponentTypeCodelistType provides an
enumeration of all component objects.

Derived by restriction of ObjectTypeCodelistType .

Enumerations:

=============================== =================
**Value**                       **Documentation**
=============================== =================
Attribute                      
ConstraintTarget               
DataSetTarget                  
Dimension                      
IdentifiableObjectTarget       
DimensionDescriptorValuesTarget
MeasureDimension               
MetadataAttribute              
PrimaryMeasure                 
ReportingYearStartDay          
ReportPeriodTarget             
TimeDimension                  
=============================== =================

**DataStructureComponentTypeCodelistType: **\ DataStructureComponentTypeCodelistType
provides an enumeration of all data structure component objects, except
for the primary measure.

Derived by restriction of ComponentTypeCodelistType .

Enumerations:

===================== =================
**Value**             **Documentation**
===================== =================
Attribute            
Dimension            
MeasureDimension     
PrimaryMeasure       
ReportingYearStartDay
TimeDimension        
===================== =================

**DimensionEumerationSchemeTypeCodelistType: **\ DimensionEumerationSchemeTypeCodelistType
provides an enumeration of all item schemes which are allowable as the
representation of a data structure definition component.

Derived by restriction of ItemSchemeTypeCodelistType .

Enumerations:

============= =================
**Value**     **Documentation**
============= =================
Codelist     
ConceptScheme
============= =================

**MetadataStructureComponentTypeCodelistType: **\ MetadataStructureComponentTypeCodelistType
provides an enumeration of all metadata structure component objects.

Derived by restriction of ComponentTypeCodelistType .

Enumerations:

=============================== =================
**Value**                       **Documentation**
=============================== =================
ConstraintTarget               
DataSetTarget                  
IdentifiableObjectTarget       
DimensionDescriptorValuesTarget
MetadataAttribute              
ReportPeriodTarget             
=============================== =================

**DimensionTypeCodelistType: **\ DimensionTypeCodelistType provides an
enumeration of all dimension objects.

Derived by restriction of ComponentTypeCodelistType .

Enumerations:

================ =================
**Value**        **Documentation**
================ =================
Dimension       
MeasureDimension
TimeDimension   
================ =================

**TargetObjectTypeCodelistType: **\ TargetObjectTypeCodelistType
provides an enumeration of all target object objects.

Derived by restriction of ComponentTypeCodelistType .

Enumerations:

=============================== =================
**Value**                       **Documentation**
=============================== =================
ConstraintTarget               
DataSetTarget                  
IdentifiableObjectTarget       
DimensionDescriptorValuesTarget
ReportPeriodTarget             
=============================== =================

.. _section-1:

.. |image0| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image1| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image2| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image3| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image4| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image5| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image6| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image7| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image8| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image9| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image10| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image11| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image12| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image13| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image14| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image15| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image16| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image17| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image18| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image19| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image20| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image21| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image22| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image23| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image24| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image25| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image26| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image27| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image28| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image29| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image30| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image31| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image32| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image33| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image34| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image35| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image36| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image37| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image38| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image39| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image40| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image41| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image42| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image43| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image44| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image45| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image46| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image47| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image48| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image49| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image50| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image51| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image52| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image53| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image54| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image55| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image56| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image57| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image58| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image59| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image60| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image61| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image62| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image63| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image64| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image65| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image66| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image67| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image68| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image69| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image70| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image71| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image72| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image73| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image74| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image75| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image76| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image77| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image78| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image79| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image80| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image81| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image82| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image83| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image84| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image85| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image86| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image87| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image88| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image89| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image90| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image91| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image92| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image93| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image94| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image95| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image96| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image97| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image98| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image99| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image100| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image101| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image102| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image103| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image104| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image105| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image106| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image107| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image108| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image109| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image110| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image111| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image112| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image113| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image114| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image115| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image116| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image117| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image118| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image119| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image120| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image121| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image122| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image123| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image124| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image125| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image126| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image127| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image128| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image129| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image130| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image131| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image132| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image133| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image134| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image135| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image136| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image137| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image138| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image139| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image140| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image141| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image142| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image143| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image144| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image145| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image146| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image147| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image148| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image149| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image150| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image151| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image152| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image153| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image154| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image155| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image156| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image157| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image158| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image159| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image160| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image161| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image162| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image163| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image164| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image165| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image166| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image167| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image168| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image169| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image170| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image171| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image172| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image173| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image174| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image175| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image176| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image177| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image178| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image179| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image180| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image181| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image182| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image183| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image184| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image185| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image186| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image187| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image188| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image189| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image190| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image191| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image192| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image193| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image194| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image195| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image196| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image197| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image198| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image199| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image200| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image201| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image202| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image203| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image204| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image205| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image206| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image207| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image208| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image209| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image210| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image211| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image212| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image213| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image214| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image215| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image216| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image217| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image218| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image219| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image220| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image221| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image222| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image223| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image224| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image225| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image226| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image227| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image228| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image229| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image230| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image231| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image232| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image233| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image234| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image235| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image236| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image237| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image238| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image239| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image240| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image241| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image242| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image243| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image244| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image245| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image246| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image247| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image248| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image249| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image250| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image251| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image252| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image253| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image254| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image255| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image256| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image257| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image258| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image259| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image260| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image261| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image262| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image263| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image264| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image265| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image266| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image267| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image268| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image269| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image270| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image271| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image272| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image273| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image274| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image275| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image276| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image277| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image278| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image279| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image280| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image281| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image282| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image283| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image284| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image285| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image286| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image287| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image288| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image289| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image290| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image291| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image292| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image293| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image294| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image295| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image296| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image297| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image298| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image299| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image300| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image301| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image302| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image303| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image304| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image305| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image306| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image307| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image308| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image309| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image310| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image311| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image312| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image313| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image314| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image315| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image316| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image317| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image318| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image319| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image320| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image321| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image322| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image323| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image324| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image325| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image326| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image327| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image328| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image329| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image330| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image331| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image332| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image333| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image334| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image335| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image336| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image337| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image338| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image339| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image340| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image341| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image342| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image343| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image344| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image345| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image346| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image347| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image348| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image349| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image350| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image351| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image352| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image353| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image354| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image355| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image356| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image357| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image358| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image359| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image360| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image361| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image362| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image363| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image364| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image365| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image366| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image367| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image368| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image369| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image370| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image371| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image372| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image373| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image374| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image375| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image376| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image377| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image378| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image379| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image380| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image381| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image382| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image383| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image384| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image385| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image386| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image387| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image388| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image389| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image390| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image391| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image392| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image393| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image394| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image395| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image396| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image397| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image398| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image399| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image400| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image401| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image402| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image403| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image404| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image405| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image406| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image407| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image408| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image409| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image410| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image411| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image412| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image413| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image414| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image415| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image416| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image417| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image418| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image419| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image420| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image421| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image422| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image423| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image424| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image425| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image426| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image427| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image428| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image429| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image430| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image431| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image432| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image433| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image434| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image435| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image436| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image437| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image438| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image439| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image440| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image441| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image442| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image443| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image444| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image445| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image446| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image447| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image448| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image449| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image450| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image451| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image452| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image453| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image454| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image455| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image456| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image457| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image458| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image459| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image460| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image461| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image462| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image463| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image464| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image465| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image466| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image467| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image468| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image469| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image470| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image471| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image472| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image473| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image474| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image475| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image476| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image477| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image478| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image479| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image480| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image481| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image482| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image483| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image484| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image485| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image486| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image487| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image488| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image489| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image490| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image491| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image492| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image493| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image494| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image495| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image496| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image497| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image498| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image499| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image500| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image501| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image502| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image503| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image504| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image505| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image506| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image507| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image508| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image509| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image510| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image511| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image512| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image513| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image514| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image515| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image516| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image517| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image518| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image519| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image520| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image521| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image522| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image523| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image524| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image525| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image526| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image527| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image528| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image529| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image530| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image531| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image532| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image533| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image534| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image535| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image536| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image537| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image538| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image539| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image540| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image541| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image542| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image543| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image544| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image545| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image546| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image547| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image548| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image549| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image550| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image551| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image552| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image553| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image554| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image555| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image556| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image557| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image558| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image559| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image560| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image561| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image562| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image563| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image564| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image565| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image566| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image567| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image568| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image569| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image570| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image571| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image572| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image573| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image574| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image575| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image576| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image577| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image578| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image579| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image580| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image581| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image582| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image583| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image584| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image585| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image586| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image587| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image588| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image589| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image590| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image591| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image592| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image593| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image594| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image595| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image596| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image597| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image598| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image599| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image600| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image601| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image602| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image603| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image604| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image605| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image606| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image607| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image608| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image609| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image610| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image611| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image612| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image613| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image614| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image615| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image616| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image617| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image618| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image619| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image620| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image621| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image622| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png
.. |image623| image:: ./media-SDMX_2_1_SECTION_3A_PART_II_COMMON/media/image2.png

