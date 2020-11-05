SDMX Standards: Section 3a PaRT III

SDMX-ML:

Schema and Documentation

Structure Namespace

Version 2.1

April 2011

© SDMX 2011

http://www.sdmx.org/

Contents
========

`1 Introduction 1 <#introduction>`__

`2 Schema Documentation 1 <#schema-documentation>`__

`2.1 Structure Namespace 1 <#structure-namespace>`__

`2.1.1 Summary 1 <#summary>`__

`2.1.2 Global Elements 1 <#global-elements>`__

`2.1.3 Complex Types 7 <#complex-types>`__

`2.1.4 Simple Types 266 <#simple-types>`__

Introduction
============

The structure namespace contains the definition of all structural
metadata constructs. These constructs are intended to be very tightly
coupled with the information model to ease the burden of implementers on
translating the information from the XML messages into objects based on
the information model.

The conformance with the information was achieved through derivation by
extensions, restrictions, and substitutions. Because of some the
limitations of XML Schema in these areas, it was often necessary to
create intermediate type which formed the basis of the final types which
make up the information that is actually exchanged in SDMX messages. The
intermediate types are all abstract, so they are not explicitly used in
a message. They do however serve the purpose of creating a strong
relation of the schemas to the information model.

Schema Documentation
====================

Structure Namespace
-------------------

**http://www.sdmx.org/resources/sdmxml/schemas/v2_1/structure**

Summary
~~~~~~~

Referenced Namespaces:

======================================================== ==========
**Namespace**                                            **Prefix**
======================================================== ==========
\                                                       
http://www.sdmx.org/resources/sdmxml/schemas/v2_1/common com
http://www.w3.org/2001/XMLSchema                         xs
======================================================== ==========

Contents:

| 41 Global Elements
| 173 Complex Types
| 5 Simple Types

Global Elements
~~~~~~~~~~~~~~~

**Structures (StructuresType): **\ Structures contains constructs for
all structural metadata components.

**Item (ItemType): **\ Item is an abstract element that serves as a
substitution head for all items in an item scheme, including those items
nested within other items. Concrete instances of this must use a
concrete instance of ItemType.

Substitutions: Category, Code, Concept, \ *Organisation*, Agency, DataConsumer,DataProvider, OrganisationUnit, ReportingCategory

**Grouping (GroupingType): **\ Grouping is an abstract element that
serves as a substitution head for all structure groupings. Groupings
contain a collection of component lists for a structure. Concrete
instances of this must use a concrete instance of GroupingType.

Substitutions: DataStructureComponents, MetadataStructureComponents

**ComponentList (ComponentListType): **\ ComponentList is an abstract
element that serves as a substitution head for all component lists.
Concrete instances of this must use a concrete instance of
ComponentListType.

Substitutions: AttributeList, DimensionList, Group, MeasureList,MetadataTarget, ReportStructure

**Component (ComponentType): **\ Component is an abstract element that
serves as a substitution head for all components. Concrete instances of
this must use a concrete instance of ComponentType.

Substitutions: Attribute, ReportingYearStartDay, Dimension, TimeDimension,MeasureDimension, GroupDimension, PrimaryMeasure,KeyDescriptorValuesTarget, DataSetTarget, ConstraintContentTarget,ReportPeriodTarget, IdentifiableObjectTarget, MetadataAttribute

**Category (CategoryType): **\ Category represents a set of nested
categories which describe a simple classification hierarchy.

Substitution For: \ *Item*

**Code (CodeType): **\ Code describes a code in a codelist. In addition
to the identification and description of the code, basic presentational
information is also available. Presentational information not present
may be added through the use of annotations.

Substitution For: \ *Item*

**Concept (ConceptType): **\ Concept describes the details of a concept
within a concept scheme.

Substitution For: \ *Item*

**DataStructureComponents
(DataStructureComponentsType): **\ DataStructureComponents defines the
grouping of the sets of metadata concepts that have a defined structural
role in the data structure definition. Note that for any component or
group defined in a data structure definition, its id must be unique.
This applies to the identifiers explicitly defined by the components as
well as those inherited from the concept identity of a component. For
example, if two dimensions take their identity from concepts with same
identity (regardless of whether the concepts exist in different schemes)
one of the dimensions must be provided a different explicit identifier.
Although there are XML schema constraints to help enforce this, these
only apply to explicitly assigned identifiers. Identifiers inherited
from a concept from which a component takes its identity cannot be
validated against this constraint. Therefore, systems processing data
structure definitions will have to perform this check outside of the XML
validation. There are also three reserved identifiers in a data
structure definition; OBS_VALUE, TIME_PERIOD, and
REPORTING_PERIOD_START_DAY. These identifiers may not be used outside of
their respective defintions (PrimaryMeasure, TimeDimension, and
ReportingYearStartDay). This applies to both the explicit identifiers
that can be assigned to the components or groups as well as an
identifier inherited by a component from its concept identity. For
example, if an ordinary dimension (i.e. not the time dimension) takes
its concept identity from a concept with the identifier TIME_PERIOD,
that dimension must provide a different explicit identifier.

Substitution For: \ *Grouping*

**AttributeList (AttributeListType): **\ AttributeList describes the
attribute descriptor for the data structure definition. It is a
collection of metadata concepts that define the attributes of the data
structure definition.

Substitution For: \ *ComponentList*

**Attribute (AttributeType): **\ Attribute describes the definition of a
data attribute, which is defined as a characteristic of an object or
entity.

Substitution For: \ *Component*

**ReportingYearStartDay
(ReportingYearStartDayType): **\ ReportingYearStartDay is a specialized
data attribute which provides important context to the time dimension.
If the value of the time dimension is one of the standard reporting
periods (see common:ReportingTimePeriodType) then this attribute is used
to state the month and day that the reporting year begins. This provides
a reference point from which the actual calendar dates covered by these
periods can be determined. If this attribute does not occur in a data
set, then the reporting year start day will be assumed to be January 1.

Substitution For: \ *Component*

**DimensionList (DimensionListType): **\ DimensionList describes the key
descriptor for the data structure definition. It is an ordered set of
metadata concepts that, combined, classify a statistical series, such as
a time series, and whose values, when combined (the key) in an instance
such as a data set, uniquely identify a specific series.

Substitution For: \ *ComponentList*

**Dimension (DimensionType): **\ Dimension describes the structure of a
dimension, which is defined as a statistical concept used (most probably
together with other statistical concepts) to identify a statistical
series, such as a time series, e.g. a statistical concept indicating
certain economic activity or a geographical reference area.

Substitution For: \ *Component*

**TimeDimension (TimeDimensionType): **\ TimeDimension is a special
dimension which designates the period in time in which the data
identified by the full series key applies.

Substitution For: \ *Component*

**MeasureDimension (MeasureDimensionType): **\ MeasureDimension is a
special type of dimension which defines multiple measures in a key
family. This is represented as any other dimension in a unless it is the
observation dimension. It takes it representation from a concept scheme,
and this scheme defines the measures and their representations. When
data is formatted with this as the observation dimension, these measures
can be made explicit or the value of the dimension can be treated as any
other dimension. If the measures are explicit, the representation of the
observation will be specific to the core representation for each concept
in the representation concept scheme. Note that it is necessary that
these representations are compliant (the same or derived from) with that
of the primary measure.

Substitution For: \ *Component*

**Group (GroupType): **\ Group describes a group descriptor in a data
structure definition. It is a set metadata concepts (and possibly their
values) that define a partial key derived from the key descriptor in a
data structure definition.

Substitution For: \ *ComponentList*

**GroupDimension (GroupDimensionType): **\ GroupDimension is a component
which contains only a reference to a dimension in the key descriptor
(DimensionList). Although it is conventional to declare dimensions in
the same order as they are declared in the ordered key, there is no
requirement to do so - the ordering of the values of the key are taken
from the order in which the dimensions are declared. Note that the id of
a dimension may be inherited from its underlying concept - therefore
this reference value may actually be the id of the concept.

Substitution For: \ *Component*

**MeasureList (MeasureListType): **\ MeasureList describes the measure
descriptor for a key family. It contains a single metadata concepts that
define the primary measures of a data structure.

Substitution For: \ *ComponentList*

**PrimaryMeasure (PrimaryMeasureType): **\ PrimaryMeasure defines the
structure of the primary measure, which is the concept that is the value
of the phenomenon to be measured in a data set. Although this may take
its semantic from any concept, this is provided a fixed identifier
(OBS_VALUE) so that it may be easily distinguished in data messages.

Substitution For: \ *Component*

**MetadataStructureComponents
(MetadataStructureComponentsType): **\ MetadataStructureComponents
defines the grouping of the sets of the components that make up the
metadata structure definition. All components and component list (target
identifiers, identifier components, report structures, and metadata
attributes) in the structure definition must have a unique
identification.

Substitution For: \ *Grouping*

**MetadataTarget (MetadataTargetType): **\ MetadataTarget is a
collection of target objects which when taken together describe a
structure which defines the key of an object type to which metadata may
be attached and serve to disambiguate reference metadata set reports.

Substitution For: \ *ComponentList*

**KeyDescriptorValuesTarget
(KeyDescriptorValuesTargetType): **\ KeyDescriptorValuesTarget is target
object which references a data key for the purpose of attach reference
metadata to portions of data. A data key is a set of dimension
references and values for those dimension. This component on its own is
not of much use, as the data key only has local references to the
dimensions. Therefore it is typical that this is used in combination
with some sort of reference to the data (either a data set reference or
a reference to the underlying structure, structure usage, or provision
agreement of the data.

Substitution For: \ *Component*

**DataSetTarget (DataSetTargetType): **\ DataSetTarget is target object
which references a data set for the purpose of attaching reference
metadata data. A data set reference is a full reference to a data
provider and an identifier for the data set.

Substitution For: \ *Component*

**ConstraintContentTarget
(ConstraintContentTargetType): **\ ConstraintContentTarget is target
object which references an attachment constraint for the purpose of
attaching reference metadata data to data key sets or cube regions
defined by the constraint.

Substitution For: \ *Component*

**ReportPeriodTarget (ReportPeriodTargetType): **\ ReportPeriodTarget is
target object which specifies a reporting period to which a metadata
report applies.

Substitution For: \ *Component*

**IdentifiableObjectTarget
(IdentifiableObjectTargetType): **\ IdentifiableObjectTarget is target
object which references an Identifiable object as defined in the SDMX
Information Model. The reference must be complete (i.e. a URN or a
complete set of reference fields). For an item object, it is possible to
define a local representation of an item scheme from which the item must
be referenced.

Substitution For: \ *Component*

**ReportStructure (ReportStructureType): **\ ReportStructure defines a
report structure, which comprises a set of metadata attributes that can
be defined as a hierarchy, for reporting reference metadata about a
target object. The identification of metadata attributes must be unique
at any given level of the report structure. Although there are XML
schema constraints to help enforce this, these only apply to explicitly
assigned identifiers. Identifiers inherited from a concept from which a
metadata attribute takes its identity cannot be validated against this
constraint. Therefore, systems processing metadata structure definitions
will have to perform this check outside of the XML validation.

Substitution For: \ *ComponentList*

**MetadataAttribute (MetadataAttributeType): **\ MetadataAttribute
defines the a metadata attribute, which is the value of an attribute,
such as the instance of a coded or uncoded attribute in a metadata
structure definition.

Substitution For: \ *Component*

**Organisation (OrganisationType): **\ Organisation is an abstract
substitution head for a generic organisation.

Substitution For: \ *Item*

Substitutions: Agency, DataConsumer, DataProvider, OrganisationUnit

**Agency (AgencyType): **\ Agency is an organisation which maintains
structural metadata such as statistical classifications, glossaries, key
family structural definitions, and metadata structure definitions..

Substitution For: \ *Organisation*

**DataConsumer (DataConsumerType): **\ DataConsumer describes an
organisation using data as input for further processing.

Substitution For: \ *Organisation*

**DataProvider (DataProviderType): **\ DataProvider describes an
organisation that produces data or reference metadata.

Substitution For: \ *Organisation*

**OrganisationUnit (OrganisationUnitType): **\ OrganisationUnit
describes a generic organisation, which serves not predefined role in
SDMX.

Substitution For: \ *Organisation*

**ReportingCategory (ReportingCategoryType): **\ ReportingCateogry
defines a reporting category, which is used to group structure usages
into useful sub-packages.

Substitution For: \ *Item*

**ItemAssociation (ItemAssociationType): **\ ItemAssociation is an
abstract description of the relation between two items for the purpose
of mapping.

Substitutions: OrganisationMap, CategoryMap, CodeMap, ConceptMap,ReportingCategoryMap

**OrganisationMap (OrganisationMapType): **\ OrganisationMap relates a
source organisation to a target organisation.

Substitution For: \ *ItemAssociation*

**CategoryMap (CategoryMapType): **\ CategoryMap defines the structure
of a map which identifies relationships between categories in different
category schemes.

Substitution For: \ *ItemAssociation*

**CodeMap (CodeMapType): **\ CodeMap defines the structure of a map
which identifies relationships between codes in different codelists.

Substitution For: \ *ItemAssociation*

**ConceptMap (ConceptMapType): **\ ConceptMap defines the structure of a
map which identifies relationships between concepts in different concept
schemes.

Substitution For: \ *ItemAssociation*

**ReportingCategoryMap
(ReportingCategoryMapType): **\ ReportingCategoryMap defines the
structure of a map which identifies relationships between reporting
categories in different reporting taxonomies.

Substitution For: \ *ItemAssociation*

Complex Types
~~~~~~~~~~~~~

**StructuresType: **\ StructuresType describes the structure of the
container for all structural metadata components. The structural
components may be explicitly detailed, or referenced from an external
structure document or registry service. Best practices dictate that, at
a minimum, any structural component that is referenced by another
structural component be included by reference.

Content:

OrganisationSchemes?, Dataflows?, Metadataflows?, CategorySchemes?,
Categorisations?, Codelists?, HierarchicalCodelists?, Concepts?,
MetadataStructures?, DataStructures?, StructureSets?,
ReportingTaxonomies?, Processes?, Constraints?, ProvisionAgreements?

Element Documentation:

====================== ========================== =====================================================================================================================================================================================================================================================================
**Name**               **Type**                   **Documentation**
====================== ========================== =====================================================================================================================================================================================================================================================================
OrganisationSchemes    OrganisationSchemesT ype   OrganisationSchemes contains a collection of organisation scheme descriptions. The organisation schemes may be detailed in full, or referenced from an external structure document or registry service.
Dataflows              DataflowsType              Dataflows contains a collection of data flow descriptions. The data flows may be detailed in full, or referenced from an external structure document or registry service.
Metadataflows          MetadataflowsType          Metadataflows contains a collection of metadata flow descriptions. The metadata flows may be detailed in full, or referenced from an external structure document or registry service.
CategorySchemes        CategorySchemesType        CategorySchemes contains a collection of category scheme descriptions. The category schemes may be detailed in full, or referenced from an external structure document or registry service.
Categorisations        CategorisationsType        Categorisations contains a collection of structural object categorisations. This container may contain categorisations for many types of objects. The categorisations may be detailed in full, or referenced from an external structure document or registry service.
Codelists              CodelistsType              Codelists contains a collection of code list descriptions. The code lists may be detailed in full, or referenced from an external structure document or registry service.
HierarchicalCodelist s HierarchicalCodelist sType HierarchicalCodelists contains a collection of hierarchical code list descriptions. The hierarchical code lists may be detailed in full, or referenced from an external structure document or registry service.
Concepts               ConceptsType               Concepts contains a collection of concept descriptions. The concepts described may be both stand-alone concepts and concepts contained within schemes. The concepts may be detailed in full, or referenced from an external structure document or registry service.
MetadataStructures     MetadataStructuresTy pe    MetadataStructures contains a collection of metadata structure definition descriptions. The metadata structure definitions may be detailed in full, or referenced from an external structure document or registry service.
DataStructures         DataStructuresType         DataStructures contains a collection of data structure definitions. The data structure definitions may be detailed in full, or referenced from an external structure document or registry service.
StructureSets          StructureSetsType          StructureSets contains a collection of structure set descriptions. The structure sets may be detailed in full, or referenced from an external structure document or registry service.
ReportingTaxonomies    ReportingTaxonomiesT ype   ReportingTaxonomies contains a collection of reporting taxonomy descriptions. The reporting taxonomies may be detailed in full, or referenced from an external structure document or registry service.
Processes              ProcessesType              Processes contains a collection of process descriptions. The processes may be detailed in full, or referenced from an external structure document or registry service.
Constraints            ConstraintsType            Constraints contains a collection of constraint descriptions. This container may contain both attachment and content constraints. The constraints may be detailed in full, or referenced from an external structure document or registry service.
ProvisionAgreements    ProvisionAgreementsT ype   ProvisionAgreements contains a collection of provision agreements. The provision agreements may be detailed in full, or referenced from an external structure document or registry service.
====================== ========================== =====================================================================================================================================================================================================================================================================

**OrganisationSchemesType: **\ OrganisationSchemesType describes the
structure of the organisation schemes container. It contains one or more
organisation scheme, which can be explicitly detailed or referenced from
an external structure document or registry service.

Content:

(AgencyScheme \| DataConsumerScheme \| DataProviderScheme \|
OrganisationUnitScheme)+

Element Documentation:

======================= =========================== ======================================================================================================================
**Name**                **Type**                    **Documentation**
======================= =========================== ======================================================================================================================
AgencyScheme            AgencySchemeType            AgencyScheme provides the details of an agency scheme, in which agencies are described.
DataConsumerScheme      DataConsumerSchemeTy pe     DataConsumerScheme provides the details of an data consumer scheme, in which data consumers are described.
DataProviderScheme      DataProviderSchemeTy pe     DataProviderScheme provides the details of an data provider scheme, in which data providers are described.
OrganisationUnitSche me OrganisationUnitSche meType OrganisationUnitScheme provides the details of an organisation unit scheme, in which organisation units are described.
======================= =========================== ======================================================================================================================

**DataflowsType: **\ DataflowsType describes the structure of the data
flows container. It contains one or more data flow, which can be
explicitly detailed or referenced from an external structure document or
registry service.

Content:

Dataflow+

Element Documentation:

======== ============ ==============================================================================================================================================
**Name** **Type**     **Documentation**
======== ============ ==============================================================================================================================================
Dataflow DataflowType Dataflow provides the details of a data flow, which is defined as the structure of data that will be provided for different reference periods.
======== ============ ==============================================================================================================================================

**MetadataflowsType: **\ MetadataflowsType describes the structure of
the metadata flows container. It contains one or more metadata flow,
which can be explicitly detailed or referenced from an external
structure document or registry service.

Content:

Metadataflow+

Element Documentation:

============ ================ ===================================================================================================================================================================
**Name**     **Type**         **Documentation**
============ ================ ===================================================================================================================================================================
Metadataflow MetadataflowType Metadataflow provides the details of a metadata flow, which is defined as the structure of reference metadata that will be provided for different reference periods
============ ================ ===================================================================================================================================================================

**CategorySchemesType: **\ CategorySchemesType describes the structure
of the category schemes container. It contains one or more category
scheme, which can be explicitly detailed or referenced from an external
structure document or registry service.

Content:

CategoryScheme+

Element Documentation:

============== ================== ================================================================================================================================================================================================================================================================================
**Name**       **Type**           **Documentation**
============== ================== ================================================================================================================================================================================================================================================================================
CategoryScheme CategorySchemeType CategoryScheme provides the details of a category scheme, which is the descriptive information for an arrangement or division of categories into groups based on characteristics, which the objects have in common. This provides for a simple, leveled hierarchy or categories.
============== ================== ================================================================================================================================================================================================================================================================================

**CategorisationsType: **\ CategorisationsType describes the structure
of the categorisations container. It contains one or more categorisation
of a specific object type, which can be explicitly detailed or
referenced from an external structure document or registry service. This
container may contain categorisations for multiple types of structural
objects.

Content:

Categorisation+

Element Documentation:

============== ================== ====================================================================================================================================================================================================================================================================================================================================================================
**Name**       **Type**           **Documentation**
============== ================== ====================================================================================================================================================================================================================================================================================================================================================================
Categorisation CategorisationType Categorisation allows for the association of an identifiable object to a category, providing for the classifications of the reference identifiable object. This must either contain the full details of the categorisation, or provide a name and identification information and reference the full details from an external structure document or registry service.
============== ================== ====================================================================================================================================================================================================================================================================================================================================================================

**CodelistsType: **\ CodelistsType describes the structure of the code
lists container. It contains one or more code list, which can be
explicitly detailed or referenced from an external structure document or
registry service.

Content:

Codelist+

Element Documentation:

======== ============ =================================================================================================================================================
**Name** **Type**     **Documentation**
======== ============ =================================================================================================================================================
Codelist CodelistType Codelist provides the details of a code list, which is defined as a list from which some statistical concepts (coded concepts) take their values.
======== ============ =================================================================================================================================================

**HierarchicalCodelistsType: **\ HierarchicalCodelistsType describes the
structure of the hierarchical code lists container. It contains one or
more hierarchical code list, which can be explicitly detailed or
referenced from an external structure document or registry service.

Content:

HierarchicalCodelist+

Element Documentation:

==================== ========================= ==================================================================================================================================================================================================================================================================
**Name**             **Type**                  **Documentation**
==================== ========================= ==================================================================================================================================================================================================================================================================
HierarchicalCodelist HierarchicalCodelist Type HierarchicalCodelist provides the details of a hierarchical code list, which is defined as an organised collection of codes that may participate in many parent/child relationships with other codes in the list, as defined by one or more hierarchy of the list.
==================== ========================= ==================================================================================================================================================================================================================================================================

**ConceptsType: **\ ConceptsType describes the structure of the concepts
container. It contains one or more stand-alone concept or concept
scheme, which can be explicitly detailed or referenced from an external
structure document or registry service. This container may contain a mix
of both stand-alone concepts and concept schemes.

Content:

ConceptScheme\*

Element Documentation:

============= ================= ============================================================================================================================================================================================================================================================================================================
**Name**      **Type**          **Documentation**
============= ================= ============================================================================================================================================================================================================================================================================================================
ConceptScheme ConceptSchemeType ConceptScheme provides the details of a concept scheme, which is the descriptive information for an arrangement or division of concepts into groups based on characteristics, which the objects have in common. It contains a collection of concept definitions, that may be arranged in simple hierarchies.
============= ================= ============================================================================================================================================================================================================================================================================================================

**MetadataStructuresType: **\ MetadataStructuresType describes the
structure of the metadata structure definitions container. It contains
one or more metadata structure definition, which can be explicitly
detailed or referenced from an external structure document or registry
service.

Content:

MetadataStructure+

Element Documentation:

================= ====================== ==============================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**          **Type**               **Documentation**
================= ====================== ==============================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
MetadataStructure MetadataStructureTyp e MetadataStructure provides the details of a metadata structure definition, which is defined as a collection of metadata concepts, their structure and usage when used to collect or disseminate reference metadata. A metadata structure definition performs several functions: it groups sets of objects into "targets" against which reference metadata may be reported. Targets define the structure of the reference metadata "keys" which identify specific types of reported metadata, and describe the valid values for populating the keys. Also, metadata structure definitions provide a presentational organization of concepts for reporting purposes. The structure of a reference metadata report is derived from this presentational structure.
================= ====================== ==============================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================

**DataStructuresType: **\ DataStructuresType describes the structure of
the data structure definitions container. It contains one or more data
structure definition, which can be explicitly detailed or referenced
from an external structure document or registry service.

Content:

DataStructure+

Element Documentation:

============= ================= =============================================================================================================================================================================================
**Name**      **Type**          **Documentation**
============= ================= =============================================================================================================================================================================================
DataStructure DataStructureType DataStructure provides the details of a data structure definition, which is defined as a collection of metadata concepts, their structure and usage when used to collect or disseminate data.
============= ================= =============================================================================================================================================================================================

**StructureSetsType: **\ StructureSetsType describes the structure of
the structure sets container. It contains one or more structure set,
which can be explicitly detailed or referenced from an external
structure document or registry service.

Content:

StructureSet+

Element Documentation:

============ ================ ============================================================================================================================================================================================================
**Name**     **Type**         **Documentation**
============ ================ ============================================================================================================================================================================================================
StructureSet StructureSetType StructureSet provides the details or a structure set, which allows components in one structure, structure usage, or item scheme to be mapped to components in another structural component of the same type.
============ ================ ============================================================================================================================================================================================================

**ReportingTaxonomiesType: **\ ReportingTaxonomiesType describes the
structure of the reporting taxonomies container. It contains one or more
reporting taxonomy, which can be explicitly detailed or referenced from
an external structure document or registry service.

Content:

ReportingTaxonomy+

Element Documentation:

================= ====================== ====================================================================================================================================================================================================================================
**Name**          **Type**               **Documentation**
================= ====================== ====================================================================================================================================================================================================================================
ReportingTaxonomy ReportingTaxonomyTyp e ReportingTaxonomy provides the details of a reporting taxonomy, which is a scheme which defines the composition structure of a data report where each component can be described by an independent data or metadata flow definition.
================= ====================== ====================================================================================================================================================================================================================================

**ProcessesType: **\ ProcessesType describes the structure of the
processes container. It contains one or more process, which can be
explicitly detailed or referenced from an external structure document or
registry service.

Content:

Process+

Element Documentation:

======== =========== ========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name** **Type**    **Documentation**
======== =========== ========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
Process  ProcessType Process provides the details of a process, which is a scheme which defines or documents the operations performed on data in order to validate data or to derive new information according to a given set of rules. It is not meant to support process automation, but serves as a description of how processes occur. The primary use for this structural mechanism is the attachment of reference metadata regarding statistical processing. This must either contain the full details of the category scheme, or provide a name and identification information and reference the full details from an external structure document or registry service.
======== =========== ========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================

**ConstraintsType: **\ ConstraintsType describes the structure of the
constraints container. It contains one or more constraint, which can be
explicitly detailed or referenced from an external structure document or
registry service. This container may contain both attachment and content
constraints.

Content:

(AttachmentConstraint \| ContentConstraint)+

Element Documentation:

==================== ========================= ============================================================================================================================================================================================================================================================
**Name**             **Type**                  **Documentation**
==================== ========================= ============================================================================================================================================================================================================================================================
AttachmentConstraint AttachmentConstraint Type AttachmentConstraint describes sub sets of the content of a data or metadata set in terms of the content regions or in terms of the set of key combinations to which attributes or reference metadata (as defined by structure definitions) may be attached.
ContentConstraint    ContentConstraintTyp e    ContentConstraint specifies a sub set of the definition of the allowable or available content of a data or metadata set in terms of the content or in terms of the set of key combinations.
==================== ========================= ============================================================================================================================================================================================================================================================

**ProvisionAgreementsType: **\ ProvisionAgreementsType describes the
structure of the provision agreements container. It contains one or more
provision agreement, which can be explicitly detailed or referenced from
an external structure document or registry service.

Content:

ProvisionAgreement+

Element Documentation:

================== ======================= ================================================================================================================================================================
**Name**           **Type**                **Documentation**
================== ======================= ================================================================================================================================================================
ProvisionAgreement ProvisionAgreementTy pe ProvisionAgreement provides the details of a provision agreement, which is an agreement for a data provider to report data or reference metadata against a flow.
================== ======================= ================================================================================================================================================================

**IdentifiableType: **\ IdentifiableType is an abstract base type for
all identifiable objects.

Derivation:

| *com:AnnotableType* (extension) 
|    |image0|\ *IdentifiableType*

Attributes:

id?, urn?, uri?

Content:

com:Annotations?

Attribute Documentation:

======== ========== ==================================================================================================================================================================
**Name** **Type**   **Documentation**
======== ========== ==================================================================================================================================================================
id       com:IDType The id is the identifier for the object.
urn      xs:anyURI  The urn attribute holds a valid SDMX Registry URN (see SDMX Registry Specification for details).
uri      xs:anyURI  The uri attribute holds a URI that contains a link to a resource with additional information about the object, such as a web page. This uri is not a SDMX message.
======== ========== ==================================================================================================================================================================

Element Documentation:

=============== =================== ==================================================================================================================================================================================
**Name**        **Type**            **Documentation**
=============== =================== ==================================================================================================================================================================================
com:Annotations com:AnnotationsType Annotations is a reusable element the provides for a collection of annotations. It has been made global so that restrictions of types that extend AnnotatableType my reference it.
=============== =================== ==================================================================================================================================================================================

**NameableType: **\ NameableType is an abstract base type for all
nameable objects.

Derivation:

| *com:AnnotableType* (extension) 
|    |image1|\ *IdentifiableType* (extension) 
|          |image2|\ *NameableType*

Attributes:

id?, urn?, uri?

Content:

com:Annotations?, com:Name+, com:Description\*

Attribute Documentation:

======== ========== ==================================================================================================================================================================
**Name** **Type**   **Documentation**
======== ========== ==================================================================================================================================================================
id       com:IDType The id is the identifier for the object.
urn      xs:anyURI  The urn attribute holds a valid SDMX Registry URN (see SDMX Registry Specification for details).
uri      xs:anyURI  The uri attribute holds a URI that contains a link to a resource with additional information about the object, such as a web page. This uri is not a SDMX message.
======== ========== ==================================================================================================================================================================

Element Documentation:

=============== =================== ==================================================================================================================================================================================
**Name**        **Type**            **Documentation**
=============== =================== ==================================================================================================================================================================================
com:Annotations com:AnnotationsType Annotations is a reusable element the provides for a collection of annotations. It has been made global so that restrictions of types that extend AnnotatableType my reference it.
com:Name        com:TextType        Name provides for a human-readable name for the object. This may be provided in multiple, parallel language-equivalent forms.
com:Description com:TextType        Description provides for a longer human-readable description of the object. This may be provided in multiple, parallel language-equivalent forms.
=============== =================== ==================================================================================================================================================================================

**VersionableType: **\ VersionableType is an abstract base type for all
versionable objects.

Derivation:

| *com:AnnotableType* (extension) 
|    |image3|\ *IdentifiableType* (extension) 
|          |image4|\ *NameableType* (extension) 
|                |image5|\ *VersionableType*

Attributes:

id?, urn?, uri?, version?, validFrom?, validTo?

Content:

com:Annotations?, com:Name+, com:Description\*

Attribute Documentation:

====================== =============== ===============================================================================================================================================================================
**Name**               **Type**        **Documentation**
====================== =============== ===============================================================================================================================================================================
id                     com:IDType      The id is the identifier for the object.
urn                    xs:anyURI       The urn attribute holds a valid SDMX Registry URN (see SDMX Registry Specification for details).
uri                    xs:anyURI       The uri attribute holds a URI that contains a link to a resource with additional information about the object, such as a web page. This uri is not a SDMX message.
version (default: 1.0) com:VersionType This version attribute holds a version number in the format of #[.#]+ (see common:VersionType definition for details). If not supplied, the version number is defaulted to 1.0.
validFrom              xs:dateTime     The validFrom attribute provides the inclusive start date for providing supplemental validity information about the version.
validTo                xs:dateTime     The validTo attribute provides the inclusive end date for providing supplemental validity information about the version.
====================== =============== ===============================================================================================================================================================================

Element Documentation:

=============== =================== ==================================================================================================================================================================================
**Name**        **Type**            **Documentation**
=============== =================== ==================================================================================================================================================================================
com:Annotations com:AnnotationsType Annotations is a reusable element the provides for a collection of annotations. It has been made global so that restrictions of types that extend AnnotatableType my reference it.
com:Name        com:TextType        Name provides for a human-readable name for the object. This may be provided in multiple, parallel language-equivalent forms.
com:Description com:TextType        Description provides for a longer human-readable description of the object. This may be provided in multiple, parallel language-equivalent forms.
=============== =================== ==================================================================================================================================================================================

**MaintainableBaseType: **\ MaintainableBaseType is an abstract type
that only serves the purpose of forming the base for the actual
MaintainableType. The purpose of this type is to restrict the
VersionableType to require the id attribute.

Derivation:

| *com:AnnotableType* (extension) 
|    |image6|\ *IdentifiableType* (extension) 
|          |image7|\ *NameableType* (extension) 
|                |image8|\ *VersionableType* (restriction) 
|                      |image9|\ *MaintainableBaseType*

Attributes:

id, urn?, uri?, version?, validFrom?, validTo?

Content:

com:Annotations?, com:Name+, com:Description\*

Attribute Documentation:

====================== =============== ===============================================================================================================================================================================
**Name**               **Type**        **Documentation**
====================== =============== ===============================================================================================================================================================================
id                     com:IDType      The id is the identifier for the object.
urn                    xs:anyURI       The urn attribute holds a valid SDMX Registry URN (see SDMX Registry Specification for details).
uri                    xs:anyURI       The uri attribute holds a URI that contains a link to a resource with additional information about the object, such as a web page. This uri is not a SDMX message.
version (default: 1.0) com:VersionType This version attribute holds a version number in the format of #[.#]+ (see common:VersionType definition for details). If not supplied, the version number is defaulted to 1.0.
validFrom              xs:dateTime     The validFrom attribute provides the inclusive start date for providing supplemental validity information about the version.
validTo                xs:dateTime     The validTo attribute provides the inclusive end date for providing supplemental validity information about the version.
====================== =============== ===============================================================================================================================================================================

Element Documentation:

=============== =================== ==================================================================================================================================================================================
**Name**        **Type**            **Documentation**
=============== =================== ==================================================================================================================================================================================
com:Annotations com:AnnotationsType Annotations is a reusable element the provides for a collection of annotations. It has been made global so that restrictions of types that extend AnnotatableType my reference it.
com:Name        com:TextType        Name provides for a human-readable name for the object. This may be provided in multiple, parallel language-equivalent forms.
com:Description com:TextType        Description provides for a longer human-readable description of the object. This may be provided in multiple, parallel language-equivalent forms.
=============== =================== ==================================================================================================================================================================================

**MaintainableType: **\ MaintainableType is an abstract base type for
all maintainable objects.

Derivation:

| *com:AnnotableType* (extension) 
|    |image10|\ *IdentifiableType* (extension) 
|          |image11|\ *NameableType* (extension) 
|                |image12|\ *VersionableType* (restriction) 
|                      |image13|\ *MaintainableBaseType* (extension) 
|                            |image14|\ *MaintainableType*

Attributes:

id, urn?, uri?, version?, validFrom?, validTo?, agencyID, isFinal?,
isExternalReference?, serviceURL?, structureURL?

Content:

com:Annotations?, com:Name+, com:Description\*

Attribute Documentation:

==================================== ======================= ==========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                             **Type**                **Documentation**
==================================== ======================= ==========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
id                                   com:IDType              The id is the identifier for the object.
urn                                  xs:anyURI               The urn attribute holds a valid SDMX Registry URN (see SDMX Registry Specification for details).
uri                                  xs:anyURI               The uri attribute holds a URI that contains a link to a resource with additional information about the object, such as a web page. This uri is not a SDMX message.
version (default: 1.0)               com:VersionType         This version attribute holds a version number in the format of #[.#]+ (see common:VersionType definition for details). If not supplied, the version number is defaulted to 1.0.
validFrom                            xs:dateTime             The validFrom attribute provides the inclusive start date for providing supplemental validity information about the version.
validTo                              xs:dateTime             The validTo attribute provides the inclusive end date for providing supplemental validity information about the version.
agencyID                             com: NestedNCNameIDType The agencyID must be provided, and identifies the maintenance agency of the object.
isFinal (default: false)             xs:boolean              The isFinal attribute indicates whether the object is unchangeable without versioning. If the value is true, the object must be versioned upon change. If the final attribute is not supplied, then the object is assumed not to be final. Note that all production objects must be final.
isExternalReference (default: false) xs:boolean              The isExternalReference attribute, if true, indicates that the actual object is not defined the corresponding element, rather its full details are defined elsewhere - indicated by either the registryURL, the repositoryURL, or the structureURL. The purpose of this is so that each structure message does not have to redefine object that are already defined elsewhere. If the isExternalReference attribute is not set, then it is assumed to be false, and the object should contain the full definition of its contents. If more than one of the registryURL, the repositoryURL, and the structureURL are supplied, then the application processing the object can choose the method it finds best suited to retrieve the details of the object.
serviceURL                           xs:anyURI               The serviceURL attribute indicates the URL of an SDMX SOAP web service from which the details of the object can be retrieved. Note that this can be a registry or and SDMX structural metadata repository, as they both implement that same web service interface.
structureURL                         xs:anyURI               The structureURL attribute indicates the URL of a SDMX-ML structure message (in the same version as the source document) in which the externally referenced object is contained. Note that this may be a URL of an SDMX RESTful web service which will return the referenced object.
==================================== ======================= ==========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================

Element Documentation:

=============== =================== ==================================================================================================================================================================================
**Name**        **Type**            **Documentation**
=============== =================== ==================================================================================================================================================================================
com:Annotations com:AnnotationsType Annotations is a reusable element the provides for a collection of annotations. It has been made global so that restrictions of types that extend AnnotatableType my reference it.
com:Name        com:TextType        Name provides for a human-readable name for the object. This may be provided in multiple, parallel language-equivalent forms.
com:Description com:TextType        Description provides for a longer human-readable description of the object. This may be provided in multiple, parallel language-equivalent forms.
=============== =================== ==================================================================================================================================================================================

**ItemSchemeType: **\ ItemSchemeType is an abstract base type for all
item scheme objects. It contains a collection of items. Concrete
instances of this type should restrict the actual types of items allowed
within the scheme.

Derivation:

| *com:AnnotableType* (extension) 
|    |image15|\ *IdentifiableType* (extension) 
|          |image16|\ *NameableType* (extension) 
|                |image17|\ *VersionableType* (restriction) 
|                      |image18|\ *MaintainableBaseType* (extension) 
|                            |image19|\ *MaintainableType* (extension) 
|                                  |image20|\ *ItemSchemeType*

Attributes:

id, urn?, uri?, version?, validFrom?, validTo?, agencyID, isFinal?,
isExternalReference?, serviceURL?, structureURL?, isPartial?

Content:

com:Annotations?, com:Name+, com:Description*, \ *Item\**

Attribute Documentation:

==================================== ======================= ==========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                             **Type**                **Documentation**
==================================== ======================= ==========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
id                                   com:IDType              The id is the identifier for the object.
urn                                  xs:anyURI               The urn attribute holds a valid SDMX Registry URN (see SDMX Registry Specification for details).
uri                                  xs:anyURI               The uri attribute holds a URI that contains a link to a resource with additional information about the object, such as a web page. This uri is not a SDMX message.
version (default: 1.0)               com:VersionType         This version attribute holds a version number in the format of #[.#]+ (see common:VersionType definition for details). If not supplied, the version number is defaulted to 1.0.
validFrom                            xs:dateTime             The validFrom attribute provides the inclusive start date for providing supplemental validity information about the version.
validTo                              xs:dateTime             The validTo attribute provides the inclusive end date for providing supplemental validity information about the version.
agencyID                             com: NestedNCNameIDType The agencyID must be provided, and identifies the maintenance agency of the object.
isFinal (default: false)             xs:boolean              The isFinal attribute indicates whether the object is unchangeable without versioning. If the value is true, the object must be versioned upon change. If the final attribute is not supplied, then the object is assumed not to be final. Note that all production objects must be final.
isExternalReference (default: false) xs:boolean              The isExternalReference attribute, if true, indicates that the actual object is not defined the corresponding element, rather its full details are defined elsewhere - indicated by either the registryURL, the repositoryURL, or the structureURL. The purpose of this is so that each structure message does not have to redefine object that are already defined elsewhere. If the isExternalReference attribute is not set, then it is assumed to be false, and the object should contain the full definition of its contents. If more than one of the registryURL, the repositoryURL, and the structureURL are supplied, then the application processing the object can choose the method it finds best suited to retrieve the details of the object.
serviceURL                           xs:anyURI               The serviceURL attribute indicates the URL of an SDMX SOAP web service from which the details of the object can be retrieved. Note that this can be a registry or and SDMX structural metadata repository, as they both implement that same web service interface.
structureURL                         xs:anyURI               The structureURL attribute indicates the URL of a SDMX-ML structure message (in the same version as the source document) in which the externally referenced object is contained. Note that this may be a URL of an SDMX RESTful web service which will return the referenced object.
isPartial (default: false)           xs:boolean              The isPartial, if true, indicates that only the relevant portion of the item scheme is being communicated. This is used in cases where a codelist is returned for a key family in the context of a constraint.
==================================== ======================= ==========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================

Element Documentation:

=============== =================== =====================================================================================================================================================================================================================
**Name**        **Type**            **Documentation**
=============== =================== =====================================================================================================================================================================================================================
com:Annotations com:AnnotationsType Annotations is a reusable element the provides for a collection of annotations. It has been made global so that restrictions of types that extend AnnotatableType my reference it.
com:Name        com:TextType        Name provides for a human-readable name for the object. This may be provided in multiple, parallel language-equivalent forms.
com:Description com:TextType        Description provides for a longer human-readable description of the object. This may be provided in multiple, parallel language-equivalent forms.
*Item*          *ItemType*          Item is an abstract element that serves as a substitution head for all items in an item scheme, including those items nested within other items. Concrete instances of this must use a concrete instance of ItemType.
=============== =================== =====================================================================================================================================================================================================================

**ItemBaseType: **\ ItemBaseType is an abstract base type that forms the
basis for the ItemType. It requires that at least an id be supplied for
an item.

Derivation:

| *com:AnnotableType* (extension) 
|    |image21|\ *IdentifiableType* (extension) 
|          |image22|\ *NameableType* (restriction) 
|                |image23|\ *ItemBaseType*

Attributes:

id, urn?, uri?

Content:

com:Annotations?, com:Name+, com:Description\*

Attribute Documentation:

======== ========== ==================================================================================================================================================================
**Name** **Type**   **Documentation**
======== ========== ==================================================================================================================================================================
id       com:IDType The id is the identifier for the object.
urn      xs:anyURI  The urn attribute holds a valid SDMX Registry URN (see SDMX Registry Specification for details).
uri      xs:anyURI  The uri attribute holds a URI that contains a link to a resource with additional information about the object, such as a web page. This uri is not a SDMX message.
======== ========== ==================================================================================================================================================================

Element Documentation:

=============== =================== ==================================================================================================================================================================================
**Name**        **Type**            **Documentation**
=============== =================== ==================================================================================================================================================================================
com:Annotations com:AnnotationsType Annotations is a reusable element the provides for a collection of annotations. It has been made global so that restrictions of types that extend AnnotatableType my reference it.
com:Name        com:TextType        Name provides for a human-readable name for the object. This may be provided in multiple, parallel language-equivalent forms.
com:Description com:TextType        Description provides for a longer human-readable description of the object. This may be provided in multiple, parallel language-equivalent forms.
=============== =================== ==================================================================================================================================================================================

**ItemType: **\ ItemType is an abstract base type for all items with in
an item scheme. Concrete instances of this type may or may not utilize
the nested item, but if so should restrict the actual types of item
allowed.

Derivation:

| *com:AnnotableType* (extension) 
|    |image24|\ *IdentifiableType* (extension) 
|          |image25|\ *NameableType* (restriction) 
|                |image26|\ *ItemBaseType* (extension) 
|                      |image27|\ *ItemType*

Attributes:

id, urn?, uri?

Content:

com:Annotations?, com:Name+, com:Description*, (Parent \|\ *Item+*)?

Attribute Documentation:

======== ========== ==================================================================================================================================================================
**Name** **Type**   **Documentation**
======== ========== ==================================================================================================================================================================
id       com:IDType The id is the identifier for the object.
urn      xs:anyURI  The urn attribute holds a valid SDMX Registry URN (see SDMX Registry Specification for details).
uri      xs:anyURI  The uri attribute holds a URI that contains a link to a resource with additional information about the object, such as a web page. This uri is not a SDMX message.
======== ========== ==================================================================================================================================================================

Element Documentation:

=============== ============================== =====================================================================================================================================================================================================================
**Name**        **Type**                       **Documentation**
=============== ============================== =====================================================================================================================================================================================================================
com:Annotations com:AnnotationsType            Annotations is a reusable element the provides for a collection of annotations. It has been made global so that restrictions of types that extend AnnotatableType my reference it.
com:Name        com:TextType                   Name provides for a human-readable name for the object. This may be provided in multiple, parallel language-equivalent forms.
com:Description com:TextType                   Description provides for a longer human-readable description of the object. This may be provided in multiple, parallel language-equivalent forms.
Parent          *com: LocalItemReferenceTy pe*
*Item*          *ItemType*                     Item is an abstract element that serves as a substitution head for all items in an item scheme, including those items nested within other items. Concrete instances of this must use a concrete instance of ItemType.
=============== ============================== =====================================================================================================================================================================================================================

**StructureType: **\ StructureType is an abstract base type for all
structure objects. Concrete instances of this should restrict to a
concrete grouping.

Derivation:

| *com:AnnotableType* (extension) 
|    |image28|\ *IdentifiableType* (extension) 
|          |image29|\ *NameableType* (extension) 
|                |image30|\ *VersionableType* (restriction) 
|                      |image31|\ *MaintainableBaseType* (extension) 
|                            |image32|\ *MaintainableType* (extension) 
|                                  |image33|\ *StructureType*

Attributes:

id, urn?, uri?, version?, validFrom?, validTo?, agencyID, isFinal?,
isExternalReference?, serviceURL?, structureURL?

Content:

com:Annotations?, com:Name+, com:Description*, \ *Grouping?*

Attribute Documentation:

==================================== ======================= ==========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                             **Type**                **Documentation**
==================================== ======================= ==========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
id                                   com:IDType              The id is the identifier for the object.
urn                                  xs:anyURI               The urn attribute holds a valid SDMX Registry URN (see SDMX Registry Specification for details).
uri                                  xs:anyURI               The uri attribute holds a URI that contains a link to a resource with additional information about the object, such as a web page. This uri is not a SDMX message.
version (default: 1.0)               com:VersionType         This version attribute holds a version number in the format of #[.#]+ (see common:VersionType definition for details). If not supplied, the version number is defaulted to 1.0.
validFrom                            xs:dateTime             The validFrom attribute provides the inclusive start date for providing supplemental validity information about the version.
validTo                              xs:dateTime             The validTo attribute provides the inclusive end date for providing supplemental validity information about the version.
agencyID                             com: NestedNCNameIDType The agencyID must be provided, and identifies the maintenance agency of the object.
isFinal (default: false)             xs:boolean              The isFinal attribute indicates whether the object is unchangeable without versioning. If the value is true, the object must be versioned upon change. If the final attribute is not supplied, then the object is assumed not to be final. Note that all production objects must be final.
isExternalReference (default: false) xs:boolean              The isExternalReference attribute, if true, indicates that the actual object is not defined the corresponding element, rather its full details are defined elsewhere - indicated by either the registryURL, the repositoryURL, or the structureURL. The purpose of this is so that each structure message does not have to redefine object that are already defined elsewhere. If the isExternalReference attribute is not set, then it is assumed to be false, and the object should contain the full definition of its contents. If more than one of the registryURL, the repositoryURL, and the structureURL are supplied, then the application processing the object can choose the method it finds best suited to retrieve the details of the object.
serviceURL                           xs:anyURI               The serviceURL attribute indicates the URL of an SDMX SOAP web service from which the details of the object can be retrieved. Note that this can be a registry or and SDMX structural metadata repository, as they both implement that same web service interface.
structureURL                         xs:anyURI               The structureURL attribute indicates the URL of a SDMX-ML structure message (in the same version as the source document) in which the externally referenced object is contained. Note that this may be a URL of an SDMX RESTful web service which will return the referenced object.
==================================== ======================= ==========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================

Element Documentation:

=============== =================== ===========================================================================================================================================================================================================================================
**Name**        **Type**            **Documentation**
=============== =================== ===========================================================================================================================================================================================================================================
com:Annotations com:AnnotationsType Annotations is a reusable element the provides for a collection of annotations. It has been made global so that restrictions of types that extend AnnotatableType my reference it.
com:Name        com:TextType        Name provides for a human-readable name for the object. This may be provided in multiple, parallel language-equivalent forms.
com:Description com:TextType        Description provides for a longer human-readable description of the object. This may be provided in multiple, parallel language-equivalent forms.
*Grouping*      *GroupingType*      Grouping is an abstract element that serves as a substitution head for all structure groupings. Groupings contain a collection of component lists for a structure. Concrete instances of this must use a concrete instance of GroupingType.
=============== =================== ===========================================================================================================================================================================================================================================

**GroupingType: **\ GroupType is an abstract base type for specific
structure groupings. It contains a collection of component lists.
Concrete instances of this should restrict to specific concrete
component lists.

Content:

*ComponentList\**

Element Documentation:

=============== =================== ==============================================================================================================================================================================
**Name**        **Type**            **Documentation**
=============== =================== ==============================================================================================================================================================================
*ComponentList* *ComponentListType* ComponentList is an abstract element that serves as a substitution head for all component lists. Concrete instances of this must use a concrete instance of ComponentListType.
=============== =================== ==============================================================================================================================================================================

**ComponentListType: **\ ComponentListType is an abstract base type for
all component lists. It contains a collection of components. Concrete
types should restrict this to specific concrete components.

Derivation:

| *com:AnnotableType* (extension) 
|    |image34|\ *IdentifiableType* (extension) 
|          |image35|\ *ComponentListType*

Attributes:

id?, urn?, uri?

Content:

com:Annotations?, \ *Component\**

Attribute Documentation:

======== ========== ==================================================================================================================================================================
**Name** **Type**   **Documentation**
======== ========== ==================================================================================================================================================================
id       com:IDType The id is the identifier for the object.
urn      xs:anyURI  The urn attribute holds a valid SDMX Registry URN (see SDMX Registry Specification for details).
uri      xs:anyURI  The uri attribute holds a URI that contains a link to a resource with additional information about the object, such as a web page. This uri is not a SDMX message.
======== ========== ==================================================================================================================================================================

Element Documentation:

=============== =================== ==================================================================================================================================================================================
**Name**        **Type**            **Documentation**
=============== =================== ==================================================================================================================================================================================
com:Annotations com:AnnotationsType Annotations is a reusable element the provides for a collection of annotations. It has been made global so that restrictions of types that extend AnnotatableType my reference it.
*Component*     *ComponentType*     Component is an abstract element that serves as a substitution head for all components. Concrete instances of this must use a concrete instance of ComponentType.
=============== =================== ==================================================================================================================================================================================

**ComponentBaseType: **\ ComponentBaseType is an abstract type that only
serves the purpose of forming the base for the actual ComponentType. It
only restricts the format of the id attribute to the NCNameIDType.

Derivation:

| *com:AnnotableType* (extension) 
|    |image36|\ *IdentifiableType* (restriction) 
|          |image37|\ *ComponentBaseType*

Attributes:

id?, urn?, uri?

Content:

com:Annotations?

Attribute Documentation:

======== ================ ================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name** **Type**         **Documentation**
======== ================ ================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
id       com:NCNameIDType The id attribute holds an explicit identification of the component. If this identifier is not supplied, then it is assumed to be the same as the identifier of the concept referenced from the concept identity. Because structures require that every component be given a unique identifier, it may be necessary to assign an explicit identifier when more than one component in a structure reference concepts with same identifier. It is important to note that this applies strictly to the identifier of concept and not the URN. Therefore if two concepts with the same identifier from different concept schemes are referenced in the same structure, one of the components will have to provide a unique explicit identifier. The type of this identifier is restricted to the common:NCNameIDType. This is necessary, since component identifiers are used to create XML elements and attributes in data and metadata structure specific schemas and therefore must be compliant with the NCName type in XML Schema (see common:NCNameIDType for further details).
urn      xs:anyURI        The urn attribute holds a valid SDMX Registry URN (see SDMX Registry Specification for details).
uri      xs:anyURI        The uri attribute holds a URI that contains a link to a resource with additional information about the object, such as a web page. This uri is not a SDMX message.
======== ================ ================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================

Element Documentation:

=============== =================== ==================================================================================================================================================================================
**Name**        **Type**            **Documentation**
=============== =================== ==================================================================================================================================================================================
com:Annotations com:AnnotationsType Annotations is a reusable element the provides for a collection of annotations. It has been made global so that restrictions of types that extend AnnotatableType my reference it.
=============== =================== ==================================================================================================================================================================================

**ComponentType: **\ ComponentType is an abstract base type for all
components. It contains information pertaining to a component, including
an optional reference to a concept, an optional role played by the
concept, an optional text format description, and an optional local
representation.

Derivation:

| *com:AnnotableType* (extension) 
|    |image38|\ *IdentifiableType* (restriction) 
|          |image39|\ *ComponentBaseType* (extension) 
|                |image40|\ *ComponentType*

Attributes:

id?, urn?, uri?

Content:

com:Annotations?, ConceptIdentity?, LocalRepresentation?

Attribute Documentation:

======== ================ ================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name** **Type**         **Documentation**
======== ================ ================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
id       com:NCNameIDType The id attribute holds an explicit identification of the component. If this identifier is not supplied, then it is assumed to be the same as the identifier of the concept referenced from the concept identity. Because structures require that every component be given a unique identifier, it may be necessary to assign an explicit identifier when more than one component in a structure reference concepts with same identifier. It is important to note that this applies strictly to the identifier of concept and not the URN. Therefore if two concepts with the same identifier from different concept schemes are referenced in the same structure, one of the components will have to provide a unique explicit identifier. The type of this identifier is restricted to the common:NCNameIDType. This is necessary, since component identifiers are used to create XML elements and attributes in data and metadata structure specific schemas and therefore must be compliant with the NCName type in XML Schema (see common:NCNameIDType for further details).
urn      xs:anyURI        The urn attribute holds a valid SDMX Registry URN (see SDMX Registry Specification for details).
uri      xs:anyURI        The uri attribute holds a URI that contains a link to a resource with additional information about the object, such as a web page. This uri is not a SDMX message.
======== ================ ================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================

Element Documentation:

=================== ========================= ==============================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**            **Type**                  **Documentation**
=================== ========================= ==============================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
com:Annotations     com:AnnotationsType       Annotations is a reusable element the provides for a collection of annotations. It has been made global so that restrictions of types that extend AnnotatableType my reference it.
ConceptIdentity     com: ConceptReferenceType ConceptIdentity allows for the referencing of a concept in a concept scheme. The component takes its semantic from this concept, and if an id is not specified, it takes its identification as well. If a representation (LocalRepresentation) is not supplied, then the representation of the component is also inherited from the concept. Note that in the case of the component representation being inherited from the concept, the allowable representations for the component still apply. Therefore, if a component references a concept with a core representation that is not allowed for the concept, that representation must be locally overridden. For components which can specify a concept role, it is implied that the concept which is referenced also identifies a role for the component.
LocalRepresentation *RepresentationType*      LocalRepresentation references item schemes that may be used to create the representation of a component. The type of this must be refined such that a concrete item scheme reference is used.
=================== ========================= ==============================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================

**StructureUsageType: **\ StructureUsageType is an abstract base type
for all structure usages. It contains a reference to a structure.
Concrete instances of this type should restrict the type of structure
referenced.

Derivation:

| *com:AnnotableType* (extension) 
|    |image41|\ *IdentifiableType* (extension) 
|          |image42|\ *NameableType* (extension) 
|                |image43|\ *VersionableType* (restriction) 
|                      |image44|\ *MaintainableBaseType* (extension) 
|                            |image45|\ *MaintainableType* (extension) 
|                                  |image46|\ *StructureUsageType*

Attributes:

id, urn?, uri?, version?, validFrom?, validTo?, agencyID, isFinal?,
isExternalReference?, serviceURL?, structureURL?

Content:

com:Annotations?, com:Name+, com:Description*, Structure?

Attribute Documentation:

==================================== ======================= ==========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                             **Type**                **Documentation**
==================================== ======================= ==========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
id                                   com:IDType              The id is the identifier for the object.
urn                                  xs:anyURI               The urn attribute holds a valid SDMX Registry URN (see SDMX Registry Specification for details).
uri                                  xs:anyURI               The uri attribute holds a URI that contains a link to a resource with additional information about the object, such as a web page. This uri is not a SDMX message.
version (default: 1.0)               com:VersionType         This version attribute holds a version number in the format of #[.#]+ (see common:VersionType definition for details). If not supplied, the version number is defaulted to 1.0.
validFrom                            xs:dateTime             The validFrom attribute provides the inclusive start date for providing supplemental validity information about the version.
validTo                              xs:dateTime             The validTo attribute provides the inclusive end date for providing supplemental validity information about the version.
agencyID                             com: NestedNCNameIDType The agencyID must be provided, and identifies the maintenance agency of the object.
isFinal (default: false)             xs:boolean              The isFinal attribute indicates whether the object is unchangeable without versioning. If the value is true, the object must be versioned upon change. If the final attribute is not supplied, then the object is assumed not to be final. Note that all production objects must be final.
isExternalReference (default: false) xs:boolean              The isExternalReference attribute, if true, indicates that the actual object is not defined the corresponding element, rather its full details are defined elsewhere - indicated by either the registryURL, the repositoryURL, or the structureURL. The purpose of this is so that each structure message does not have to redefine object that are already defined elsewhere. If the isExternalReference attribute is not set, then it is assumed to be false, and the object should contain the full definition of its contents. If more than one of the registryURL, the repositoryURL, and the structureURL are supplied, then the application processing the object can choose the method it finds best suited to retrieve the details of the object.
serviceURL                           xs:anyURI               The serviceURL attribute indicates the URL of an SDMX SOAP web service from which the details of the object can be retrieved. Note that this can be a registry or and SDMX structural metadata repository, as they both implement that same web service interface.
structureURL                         xs:anyURI               The structureURL attribute indicates the URL of a SDMX-ML structure message (in the same version as the source document) in which the externally referenced object is contained. Note that this may be a URL of an SDMX RESTful web service which will return the referenced object.
==================================== ======================= ==========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================

Element Documentation:

=============== ================================== ===========================================================================================================================================================================================================================================================================================
**Name**        **Type**                           **Documentation**
=============== ================================== ===========================================================================================================================================================================================================================================================================================
com:Annotations com:AnnotationsType                Annotations is a reusable element the provides for a collection of annotations. It has been made global so that restrictions of types that extend AnnotatableType my reference it.
com:Name        com:TextType                       Name provides for a human-readable name for the object. This may be provided in multiple, parallel language-equivalent forms.
com:Description com:TextType                       Description provides for a longer human-readable description of the object. This may be provided in multiple, parallel language-equivalent forms.
Structure       *com: StructureReferenceBa seType* Structure references the structure (data structure or metadata structure definition) which the structure usage is based upon. Implementations will have to refine the type to use a concrete structure reference (i.e. either a data structure or metadata structure definition reference).
=============== ================================== ===========================================================================================================================================================================================================================================================================================

**RepresentationType: **\ RepresentationType is an abstract type that
defines a representation. Because the type of item schemes that are
allowed as the an enumeration vary based on the object in which this is
defined, this type is abstract to force that the enumeration reference
be restricted to the proper type of item scheme reference.

Content:

(TextFormat \| (Enumeration, EnumerationFormat?))

Element Documentation:

================= =================================== ================================================================================================================
**Name**          **Type**                            **Documentation**
================= =================================== ================================================================================================================
TextFormat        TextFormatType                      TextFormat describes an uncoded textual format.
Enumeration       *com: ItemSchemeReferenceB aseType* Enumeration references an item scheme that enumerates the allowable values for this representation.
EnumerationFormat CodededTextFormatTyp e              EnumerationFormat describes the facets of the item scheme enumeration. This is for the most part, informational.
================= =================================== ================================================================================================================

**TextFormatType: **\ TextFormatType defines the information for
describing a full range of text formats and may place restrictions on
the values of the other attributes, referred to as "facets".

Attributes:

textType?, isSequence?, interval?, startValue?, endValue?,
timeInterval?, startTime?, endTime?, minLength?, maxLength?, minValue?,
maxValue?, decimals?, pattern?, isMultiLingual?

Content:

{Empty}

Attribute Documentation:

============================== ============================ =====================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                       **Type**                     **Documentation**
============================== ============================ =====================================================================================================================================================================================================================================================================================================================================================================================================================
textType (default: String)     com:DataType                 The textType attribute provides a description of the datatype. If it is not specified, any valid characters may be included in the text field (it corresponds to the xs:string datatype of W3C XML Schema) within the constraints of the facets.
isSequence                     xs:boolean                   The isSequence attribute indicates whether the values are intended to be ordered, and it may work in combination with the interval, startValue, and endValue attributes or the timeInterval, startTime, and endTime, attributes. If this attribute holds a value of true, a start value or time and a numeric or time interval must supplied. If an end value is not given, then the sequence continues indefinitely.
interval                       xs:decimal                   The interval attribute specifies the permitted interval (increment) in a sequence. In order for this to be used, the isSequence attribute must have a value of true.
startValue                     xs:decimal                   The startValue attribute is used in conjunction with the isSequence and interval attributes (which must be set in order to use this attribute). This attribute is used for a numeric sequence, and indicates the starting point of the sequence. This value is mandatory for a numeric sequence to be expressed.
endValue                       xs:decimal                   The endValue attribute is used in conjunction with the isSequence and interval attributes (which must be set in order to use this attribute). This attribute is used for a numeric sequence, and indicates that ending point (if any) of the sequence.
timeInterval                   xs:duration                  The timeInterval attribute indicates the permitted duration in a time sequence. In order for this to be used, the isSequence attribute must have a value of true.
startTime                      com: StandardTimePeriodTy pe The startTime attribute is used in conjunction with the isSequence and timeInterval attributes (which must be set in order to use this attribute). This attribute is used for a time sequence, and indicates the start time of the sequence. This value is mandatory for a time sequence to be expressed.
endTime                        com: StandardTimePeriodTy pe The endTime attribute is used in conjunction with the isSequence and timeInterval attributes (which must be set in order to use this attribute). This attribute is used for a time sequence, and indicates that ending point (if any) of the sequence.
minLength                      xs:positiveInteger           The minLength attribute specifies the minimum and length of the value in characters.
maxLength                      xs:positiveInteger           The maxLength attribute specifies the maximum length of the value in characters.
minValue                       xs:decimal                   The minValue attribute is used for inclusive and exclusive ranges, indicating what the lower bound of the range is. If this is used with an inclusive range, a valid value will be greater than or equal to the value specified here. If the inclusive and exclusive data type is not specified (e.g. this facet is used with an integer data type), the value is assumed to be inclusive.
maxValue                       xs:decimal                   The maxValue attribute is used for inclusive and exclusive ranges, indicating what the upper bound of the range is. If this is used with an inclusive range, a valid value will be less than or equal to the value specified here. If the inclusive and exclusive data type is not specified (e.g. this facet is used with an integer data type), the value is assumed to be inclusive.
decimals                       xs:positiveInteger           The decimals attribute indicates the number of characters allowed after the decimal separator.
pattern                        xs:string                    The pattern attribute holds any regular expression permitted in the similar facet in W3C XML Schema.
isMultiLingual (default: true) xs:boolean                   The isMultiLingual attribute indicates for a text format of type "string", whether the value should allow for multiple values in different languages.
============================== ============================ =====================================================================================================================================================================================================================================================================================================================================================================================================================

**BasicComponentTextFormatType: **\ BasicComponentTextFormatType is a
restricted version of the TextFormatType that restricts the text type to
the representations allowed for all components except for target
objects.

Derivation:

| TextFormatType (restriction) 
|    |image47|\ BasicComponentTextFormatType

Attributes:

textType?, isSequence?, interval?, startValue?, endValue?,
timeInterval?, startTime?, endTime?, minLength?, maxLength?, minValue?,
maxValue?, decimals?, pattern?, isMultiLingual?

Content:

{Empty}

Attribute Documentation:

============================== ============================ =====================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                       **Type**                     **Documentation**
============================== ============================ =====================================================================================================================================================================================================================================================================================================================================================================================================================
textType (default: String)     com: BasicComponentDataTy pe The textType attribute provides a description of the datatype. If it is not specified, any valid characters may be included in the text field (it corresponds to the xs:string datatype of W3C XML Schema) within the constraints of the facets.
isSequence                     xs:boolean                   The isSequence attribute indicates whether the values are intended to be ordered, and it may work in combination with the interval, startValue, and endValue attributes or the timeInterval, startTime, and endTime, attributes. If this attribute holds a value of true, a start value or time and a numeric or time interval must supplied. If an end value is not given, then the sequence continues indefinitely.
interval                       xs:decimal                   The interval attribute specifies the permitted interval (increment) in a sequence. In order for this to be used, the isSequence attribute must have a value of true.
startValue                     xs:decimal                   The startValue attribute is used in conjunction with the isSequence and interval attributes (which must be set in order to use this attribute). This attribute is used for a numeric sequence, and indicates the starting point of the sequence. This value is mandatory for a numeric sequence to be expressed.
endValue                       xs:decimal                   The endValue attribute is used in conjunction with the isSequence and interval attributes (which must be set in order to use this attribute). This attribute is used for a numeric sequence, and indicates that ending point (if any) of the sequence.
timeInterval                   xs:duration                  The timeInterval attribute indicates the permitted duration in a time sequence. In order for this to be used, the isSequence attribute must have a value of true.
startTime                      com: StandardTimePeriodTy pe The startTime attribute is used in conjunction with the isSequence and timeInterval attributes (which must be set in order to use this attribute). This attribute is used for a time sequence, and indicates the start time of the sequence. This value is mandatory for a time sequence to be expressed.
endTime                        com: StandardTimePeriodTy pe The endTime attribute is used in conjunction with the isSequence and timeInterval attributes (which must be set in order to use this attribute). This attribute is used for a time sequence, and indicates that ending point (if any) of the sequence.
minLength                      xs:positiveInteger           The minLength attribute specifies the minimum and length of the value in characters.
maxLength                      xs:positiveInteger           The maxLength attribute specifies the maximum length of the value in characters.
minValue                       xs:decimal                   The minValue attribute is used for inclusive and exclusive ranges, indicating what the lower bound of the range is. If this is used with an inclusive range, a valid value will be greater than or equal to the value specified here. If the inclusive and exclusive data type is not specified (e.g. this facet is used with an integer data type), the value is assumed to be inclusive.
maxValue                       xs:decimal                   The maxValue attribute is used for inclusive and exclusive ranges, indicating what the upper bound of the range is. If this is used with an inclusive range, a valid value will be less than or equal to the value specified here. If the inclusive and exclusive data type is not specified (e.g. this facet is used with an integer data type), the value is assumed to be inclusive.
decimals                       xs:positiveInteger           The decimals attribute indicates the number of characters allowed after the decimal separator.
pattern                        xs:string                    The pattern attribute holds any regular expression permitted in the similar facet in W3C XML Schema.
isMultiLingual (default: true) xs:boolean                   The isMultiLingual attribute indicates for a text format of type "string", whether the value should allow for multiple values in different languages.
============================== ============================ =====================================================================================================================================================================================================================================================================================================================================================================================================================

**SimpleComponentTextFormatType: **\ SimpleComponentTextFormatType is a
restricted version of the BasicComponentTextFormatType that does not
allow for multi-lingual values.

Derivation:

| TextFormatType (restriction) 
|    |image48|\ BasicComponentTextFormatType (restriction) 
|          |image49|\ SimpleComponentTextFormatType

Attributes:

textType?, isSequence?, interval?, startValue?, endValue?,
timeInterval?, startTime?, endTime?, minLength?, maxLength?, minValue?,
maxValue?, decimals?, pattern?

Content:

{Empty}

Attribute Documentation:

========================== ============================ =====================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                   **Type**                     **Documentation**
========================== ============================ =====================================================================================================================================================================================================================================================================================================================================================================================================================
textType (default: String) com:SimpleDataType           The textType attribute provides a description of the datatype. If it is not specified, any valid characters may be included in the text field (it corresponds to the xs:string datatype of W3C XML Schema) within the constraints of the facets.
isSequence                 xs:boolean                   The isSequence attribute indicates whether the values are intended to be ordered, and it may work in combination with the interval, startValue, and endValue attributes or the timeInterval, startTime, and endTime, attributes. If this attribute holds a value of true, a start value or time and a numeric or time interval must supplied. If an end value is not given, then the sequence continues indefinitely.
interval                   xs:decimal                   The interval attribute specifies the permitted interval (increment) in a sequence. In order for this to be used, the isSequence attribute must have a value of true.
startValue                 xs:decimal                   The startValue attribute is used in conjunction with the isSequence and interval attributes (which must be set in order to use this attribute). This attribute is used for a numeric sequence, and indicates the starting point of the sequence. This value is mandatory for a numeric sequence to be expressed.
endValue                   xs:decimal                   The endValue attribute is used in conjunction with the isSequence and interval attributes (which must be set in order to use this attribute). This attribute is used for a numeric sequence, and indicates that ending point (if any) of the sequence.
timeInterval               xs:duration                  The timeInterval attribute indicates the permitted duration in a time sequence. In order for this to be used, the isSequence attribute must have a value of true.
startTime                  com: StandardTimePeriodTy pe The startTime attribute is used in conjunction with the isSequence and timeInterval attributes (which must be set in order to use this attribute). This attribute is used for a time sequence, and indicates the start time of the sequence. This value is mandatory for a time sequence to be expressed.
endTime                    com: StandardTimePeriodTy pe The endTime attribute is used in conjunction with the isSequence and timeInterval attributes (which must be set in order to use this attribute). This attribute is used for a time sequence, and indicates that ending point (if any) of the sequence.
minLength                  xs:positiveInteger           The minLength attribute specifies the minimum and length of the value in characters.
maxLength                  xs:positiveInteger           The maxLength attribute specifies the maximum length of the value in characters.
minValue                   xs:decimal                   The minValue attribute is used for inclusive and exclusive ranges, indicating what the lower bound of the range is. If this is used with an inclusive range, a valid value will be greater than or equal to the value specified here. If the inclusive and exclusive data type is not specified (e.g. this facet is used with an integer data type), the value is assumed to be inclusive.
maxValue                   xs:decimal                   The maxValue attribute is used for inclusive and exclusive ranges, indicating what the upper bound of the range is. If this is used with an inclusive range, a valid value will be less than or equal to the value specified here. If the inclusive and exclusive data type is not specified (e.g. this facet is used with an integer data type), the value is assumed to be inclusive.
decimals                   xs:positiveInteger           The decimals attribute indicates the number of characters allowed after the decimal separator.
pattern                    xs:string                    The pattern attribute holds any regular expression permitted in the similar facet in W3C XML Schema.
========================== ============================ =====================================================================================================================================================================================================================================================================================================================================================================================================================

**CodededTextFormatType: **\ CodededTextFormatType is a restricted
version of the SimpleComponentTextFormatType that only allows factets
and text types applicable to codes. Although the time facets permit any
value, an actual code identifier does not support the necessary
characters for time. Therefore these facets should not contain time in
their values.

Derivation:

| TextFormatType (restriction) 
|    |image50|\ BasicComponentTextFormatType (restriction) 
|          |image51|\ SimpleComponentTextFormatType (restriction) 
|                |image52|\ CodededTextFormatType

Attributes:

textType?, isSequence?, interval?, startValue?, endValue?,
timeInterval?, startTime?, endTime?, minLength?, maxLength?, minValue?,
maxValue?, pattern?

Content:

{Empty}

Attribute Documentation:

============ ============================ =====================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**     **Type**                     **Documentation**
============ ============================ =====================================================================================================================================================================================================================================================================================================================================================================================================================
textType     CodeDataType                 The textType attribute provides a description of the datatype. If it is not specified, any valid characters may be included in the text field (it corresponds to the xs:string datatype of W3C XML Schema) within the constraints of the facets.
isSequence   xs:boolean                   The isSequence attribute indicates whether the values are intended to be ordered, and it may work in combination with the interval, startValue, and endValue attributes or the timeInterval, startTime, and endTime, attributes. If this attribute holds a value of true, a start value or time and a numeric or time interval must supplied. If an end value is not given, then the sequence continues indefinitely.
interval     xs:integer                   The interval attribute specifies the permitted interval (increment) in a sequence. In order for this to be used, the isSequence attribute must have a value of true.
startValue   xs:integer                   The startValue attribute is used in conjunction with the isSequence and interval attributes (which must be set in order to use this attribute). This attribute is used for a numeric sequence, and indicates the starting point of the sequence. This value is mandatory for a numeric sequence to be expressed.
endValue     xs:integer                   The endValue attribute is used in conjunction with the isSequence and interval attributes (which must be set in order to use this attribute). This attribute is used for a numeric sequence, and indicates that ending point (if any) of the sequence.
timeInterval xs:duration                  The timeInterval attribute indicates the permitted duration in a time sequence. In order for this to be used, the isSequence attribute must have a value of true.
startTime    com: StandardTimePeriodTy pe The startTime attribute is used in conjunction with the isSequence and timeInterval attributes (which must be set in order to use this attribute). This attribute is used for a time sequence, and indicates the start time of the sequence. This value is mandatory for a time sequence to be expressed.
endTime      com: StandardTimePeriodTy pe The endTime attribute is used in conjunction with the isSequence and timeInterval attributes (which must be set in order to use this attribute). This attribute is used for a time sequence, and indicates that ending point (if any) of the sequence.
minLength    xs:positiveInteger           The minLength attribute specifies the minimum and length of the value in characters.
maxLength    xs:positiveInteger           The maxLength attribute specifies the maximum length of the value in characters.
minValue     xs:integer                   The minValue attribute is used for inclusive and exclusive ranges, indicating what the lower bound of the range is. If this is used with an inclusive range, a valid value will be greater than or equal to the value specified here. If the inclusive and exclusive data type is not specified (e.g. this facet is used with an integer data type), the value is assumed to be inclusive.
maxValue     xs:integer                   The maxValue attribute is used for inclusive and exclusive ranges, indicating what the upper bound of the range is. If this is used with an inclusive range, a valid value will be less than or equal to the value specified here. If the inclusive and exclusive data type is not specified (e.g. this facet is used with an integer data type), the value is assumed to be inclusive.
pattern      xs:string                    The pattern attribute holds any regular expression permitted in the similar facet in W3C XML Schema.
============ ============================ =====================================================================================================================================================================================================================================================================================================================================================================================================================

**NonFacetedTextFormatType: **\ NonFacetedTextFormatType is a restricted
version of the SimpleComponentTextFormatType that does not allow for any
facets.

Derivation:

| TextFormatType (restriction) 
|    |image53|\ BasicComponentTextFormatType (restriction) 
|          |image54|\ SimpleComponentTextFormatType (restriction) 
|                |image55|\ NonFacetedTextFormatType

Attributes:

textType?

Content:

{Empty}

Attribute Documentation:

======== ================== ================================================================================================================================================================================================================================================
**Name** **Type**           **Documentation**
======== ================== ================================================================================================================================================================================================================================================
textType com:SimpleDataType The textType attribute provides a description of the datatype. If it is not specified, any valid characters may be included in the text field (it corresponds to the xs:string datatype of W3C XML Schema) within the constraints of the facets.
======== ================== ================================================================================================================================================================================================================================================

**TimeTextFormatType: **\ TimeTextFormat is a restricted version of the
SimpleComponentTextFormatType that only allows time based format and
specifies a default ObservationalTimePeriod representation and facets of
a start and end time.

Derivation:

| TextFormatType (restriction) 
|    |image56|\ BasicComponentTextFormatType (restriction) 
|          |image57|\ SimpleComponentTextFormatType (restriction) 
|                |image58|\ TimeTextFormatType

Attributes:

textType?, startTime?, endTime?

Content:

{Empty}

Attribute Documentation:

=========================================== ============================ =========================================================================================================================================================================================================================================================================================================
**Name**                                    **Type**                     **Documentation**
=========================================== ============================ =========================================================================================================================================================================================================================================================================================================
textType (default: ObservationalTimePeriod) com:TimeDataType             The textType attribute provides a description of the datatype. If it is not specified, any valid characters may be included in the text field (it corresponds to the xs:string datatype of W3C XML Schema) within the constraints of the facets.
startTime                                   com: StandardTimePeriodTy pe The startTime attribute is used in conjunction with the isSequence and timeInterval attributes (which must be set in order to use this attribute). This attribute is used for a time sequence, and indicates the start time of the sequence. This value is mandatory for a time sequence to be expressed.
endTime                                     com: StandardTimePeriodTy pe The endTime attribute is used in conjunction with the isSequence and timeInterval attributes (which must be set in order to use this attribute). This attribute is used for a time sequence, and indicates that ending point (if any) of the sequence.
=========================================== ============================ =========================================================================================================================================================================================================================================================================================================

**CategorisationType: **\ CategorisationType is defines the structure
for a categorisation. A source object is referenced via an object
reference and the target category is referenced via the target category.

Derivation:

| *com:AnnotableType* (extension) 
|    |image59|\ *IdentifiableType* (extension) 
|          |image60|\ *NameableType* (extension) 
|                |image61|\ *VersionableType* (restriction) 
|                      |image62|\ *MaintainableBaseType* (extension) 
|                            |image63|\ *MaintainableType* (extension) 
|                                  |image64|\ CategorisationType

Attributes:

id, urn?, uri?, version?, validFrom?, validTo?, agencyID, isFinal?,
isExternalReference?, serviceURL?, structureURL?

Content:

com:Annotations?, com:Name+, com:Description*, (Source, Target)?

Attribute Documentation:

==================================== ======================= ==========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                             **Type**                **Documentation**
==================================== ======================= ==========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
id                                   com:IDType              The id is the identifier for the object.
urn                                  xs:anyURI               The urn attribute holds a valid SDMX Registry URN (see SDMX Registry Specification for details).
uri                                  xs:anyURI               The uri attribute holds a URI that contains a link to a resource with additional information about the object, such as a web page. This uri is not a SDMX message.
version (default: 1.0)               com:VersionType         This version attribute holds a version number in the format of #[.#]+ (see common:VersionType definition for details). If not supplied, the version number is defaulted to 1.0.
validFrom                            xs:dateTime             The validFrom attribute provides the inclusive start date for providing supplemental validity information about the version.
validTo                              xs:dateTime             The validTo attribute provides the inclusive end date for providing supplemental validity information about the version.
agencyID                             com: NestedNCNameIDType The agencyID must be provided, and identifies the maintenance agency of the object.
isFinal (default: false)             xs:boolean              The isFinal attribute indicates whether the object is unchangeable without versioning. If the value is true, the object must be versioned upon change. If the final attribute is not supplied, then the object is assumed not to be final. Note that all production objects must be final.
isExternalReference (default: false) xs:boolean              The isExternalReference attribute, if true, indicates that the actual object is not defined the corresponding element, rather its full details are defined elsewhere - indicated by either the registryURL, the repositoryURL, or the structureURL. The purpose of this is so that each structure message does not have to redefine object that are already defined elsewhere. If the isExternalReference attribute is not set, then it is assumed to be false, and the object should contain the full definition of its contents. If more than one of the registryURL, the repositoryURL, and the structureURL are supplied, then the application processing the object can choose the method it finds best suited to retrieve the details of the object.
serviceURL                           xs:anyURI               The serviceURL attribute indicates the URL of an SDMX SOAP web service from which the details of the object can be retrieved. Note that this can be a registry or and SDMX structural metadata repository, as they both implement that same web service interface.
structureURL                         xs:anyURI               The structureURL attribute indicates the URL of a SDMX-ML structure message (in the same version as the source document) in which the externally referenced object is contained. Note that this may be a URL of an SDMX RESTful web service which will return the referenced object.
==================================== ======================= ==========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================

Element Documentation:

=============== =========================== ==================================================================================================================================================================================
**Name**        **Type**                    **Documentation**
=============== =========================== ==================================================================================================================================================================================
com:Annotations com:AnnotationsType         Annotations is a reusable element the provides for a collection of annotations. It has been made global so that restrictions of types that extend AnnotatableType my reference it.
com:Name        com:TextType                Name provides for a human-readable name for the object. This may be provided in multiple, parallel language-equivalent forms.
com:Description com:TextType                Description provides for a longer human-readable description of the object. This may be provided in multiple, parallel language-equivalent forms.
Source          com: ObjectReferenceType    Source is a reference to an object to be categorized.
Target          com: CategoryReferenceTyp e Target is reference to the category that the referenced object is to be mapped to.
=============== =========================== ==================================================================================================================================================================================

**CategorySchemeType: **\ CategorySchemeType describes the structure of
a category scheme. A category scheme is the descriptive information for
an arrangement or division of categories into groups based on
characteristics, which the objects have in common. This provides for a
simple, leveled hierarchy or categories.

Derivation:

| *com:AnnotableType* (extension) 
|    |image65|\ *IdentifiableType* (extension) 
|          |image66|\ *NameableType* (extension) 
|                |image67|\ *VersionableType* (restriction) 
|                      |image68|\ *MaintainableBaseType* (extension) 
|                            |image69|\ *MaintainableType* (extension) 
|                                  |image70|\ *ItemSchemeType* (restriction) 
|                                        |image71|\ CategorySchemeType

Attributes:

id, urn?, uri?, version?, validFrom?, validTo?, agencyID, isFinal?,
isExternalReference?, serviceURL?, structureURL?, isPartial?

Content:

com:Annotations?, com:Name+, com:Description*, Category\*

Attribute Documentation:

==================================== ======================= ==========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                             **Type**                **Documentation**
==================================== ======================= ==========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
id                                   com:NCNameIDType        The id attribute holds the identification of the category scheme. The type of this id is restricted to the common:NCNNameIDType. This is necessary, since the category scheme may be used to create simple types in data and metadata structure specific schemas and therefore must be compliant with the NCName type in XML Schema (see common:NCNameIDType for further details).
urn                                  xs:anyURI               The urn attribute holds a valid SDMX Registry URN (see SDMX Registry Specification for details).
uri                                  xs:anyURI               The uri attribute holds a URI that contains a link to a resource with additional information about the object, such as a web page. This uri is not a SDMX message.
version (default: 1.0)               com:VersionType         This version attribute holds a version number in the format of #[.#]+ (see common:VersionType definition for details). If not supplied, the version number is defaulted to 1.0.
validFrom                            xs:dateTime             The validFrom attribute provides the inclusive start date for providing supplemental validity information about the version.
validTo                              xs:dateTime             The validTo attribute provides the inclusive end date for providing supplemental validity information about the version.
agencyID                             com: NestedNCNameIDType The agencyID must be provided, and identifies the maintenance agency of the object.
isFinal (default: false)             xs:boolean              The isFinal attribute indicates whether the object is unchangeable without versioning. If the value is true, the object must be versioned upon change. If the final attribute is not supplied, then the object is assumed not to be final. Note that all production objects must be final.
isExternalReference (default: false) xs:boolean              The isExternalReference attribute, if true, indicates that the actual object is not defined the corresponding element, rather its full details are defined elsewhere - indicated by either the registryURL, the repositoryURL, or the structureURL. The purpose of this is so that each structure message does not have to redefine object that are already defined elsewhere. If the isExternalReference attribute is not set, then it is assumed to be false, and the object should contain the full definition of its contents. If more than one of the registryURL, the repositoryURL, and the structureURL are supplied, then the application processing the object can choose the method it finds best suited to retrieve the details of the object.
serviceURL                           xs:anyURI               The serviceURL attribute indicates the URL of an SDMX SOAP web service from which the details of the object can be retrieved. Note that this can be a registry or and SDMX structural metadata repository, as they both implement that same web service interface.
structureURL                         xs:anyURI               The structureURL attribute indicates the URL of a SDMX-ML structure message (in the same version as the source document) in which the externally referenced object is contained. Note that this may be a URL of an SDMX RESTful web service which will return the referenced object.
isPartial (default: false)           xs:boolean              The isPartial, if true, indicates that only the relevant portion of the item scheme is being communicated. This is used in cases where a codelist is returned for a key family in the context of a constraint.
==================================== ======================= ==========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================

Element Documentation:

=============== =================== ==================================================================================================================================================================================
**Name**        **Type**            **Documentation**
=============== =================== ==================================================================================================================================================================================
com:Annotations com:AnnotationsType Annotations is a reusable element the provides for a collection of annotations. It has been made global so that restrictions of types that extend AnnotatableType my reference it.
com:Name        com:TextType        Name provides for a human-readable name for the object. This may be provided in multiple, parallel language-equivalent forms.
com:Description com:TextType        Description provides for a longer human-readable description of the object. This may be provided in multiple, parallel language-equivalent forms.
Category        CategoryType        Category represents a set of nested categories which describe a simple classification hierarchy.
=============== =================== ==================================================================================================================================================================================

**CategoryType: **\ CategoryType describes the details of a category. A
category is defined as an item at any level in a classification. The
Category element represents a set of nested categories which are child
categories.

Derivation:

| *com:AnnotableType* (extension) 
|    |image72|\ *IdentifiableType* (extension) 
|          |image73|\ *NameableType* (restriction) 
|                |image74|\ *ItemBaseType* (extension) 
|                      |image75|\ *ItemType* (restriction) 
|                            |image76|\ CategoryType

Attributes:

id, urn?, uri?

Content:

com:Annotations?, com:Name+, com:Description*, Category\*

Attribute Documentation:

======== ========== ==================================================================================================================================================================
**Name** **Type**   **Documentation**
======== ========== ==================================================================================================================================================================
id       com:IDType The id is the identifier for the object.
urn      xs:anyURI  The urn attribute holds a valid SDMX Registry URN (see SDMX Registry Specification for details).
uri      xs:anyURI  The uri attribute holds a URI that contains a link to a resource with additional information about the object, such as a web page. This uri is not a SDMX message.
======== ========== ==================================================================================================================================================================

Element Documentation:

=============== =================== ==================================================================================================================================================================================
**Name**        **Type**            **Documentation**
=============== =================== ==================================================================================================================================================================================
com:Annotations com:AnnotationsType Annotations is a reusable element the provides for a collection of annotations. It has been made global so that restrictions of types that extend AnnotatableType my reference it.
com:Name        com:TextType        Name provides for a human-readable name for the object. This may be provided in multiple, parallel language-equivalent forms.
com:Description com:TextType        Description provides for a longer human-readable description of the object. This may be provided in multiple, parallel language-equivalent forms.
Category        CategoryType        Category represents a set of nested categories which describe a simple classification hierarchy.
=============== =================== ==================================================================================================================================================================================

**CodelistType: **\ CodelistType defines the structure of a codelist. A
codelist is defined as a list from which some statistical concepts
(coded concepts) take their values.

Derivation:

| *com:AnnotableType* (extension) 
|    |image77|\ *IdentifiableType* (extension) 
|          |image78|\ *NameableType* (extension) 
|                |image79|\ *VersionableType* (restriction) 
|                      |image80|\ *MaintainableBaseType* (extension) 
|                            |image81|\ *MaintainableType* (extension) 
|                                  |image82|\ *ItemSchemeType* (restriction) 
|                                        |image83|\ CodelistType

Attributes:

id, urn?, uri?, version?, validFrom?, validTo?, agencyID, isFinal?,
isExternalReference?, serviceURL?, structureURL?, isPartial?

Content:

com:Annotations?, com:Name+, com:Description*, Code\*

Attribute Documentation:

==================================== ======================= ==========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                             **Type**                **Documentation**
==================================== ======================= ==========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
id                                   com:NCNameIDType        The id attribute holds the identification of the code list. The type of this id is restricted to the common:NCNNameIDType. This is necessary, since the code list may be used to create simple types in data and metadata structure specific schemas and therefore must be compliant with the NCName type in XML Schema (see common:NCNameIDType for further details).
urn                                  xs:anyURI               The urn attribute holds a valid SDMX Registry URN (see SDMX Registry Specification for details).
uri                                  xs:anyURI               The uri attribute holds a URI that contains a link to a resource with additional information about the object, such as a web page. This uri is not a SDMX message.
version (default: 1.0)               com:VersionType         This version attribute holds a version number in the format of #[.#]+ (see common:VersionType definition for details). If not supplied, the version number is defaulted to 1.0.
validFrom                            xs:dateTime             The validFrom attribute provides the inclusive start date for providing supplemental validity information about the version.
validTo                              xs:dateTime             The validTo attribute provides the inclusive end date for providing supplemental validity information about the version.
agencyID                             com: NestedNCNameIDType The agencyID must be provided, and identifies the maintenance agency of the object.
isFinal (default: false)             xs:boolean              The isFinal attribute indicates whether the object is unchangeable without versioning. If the value is true, the object must be versioned upon change. If the final attribute is not supplied, then the object is assumed not to be final. Note that all production objects must be final.
isExternalReference (default: false) xs:boolean              The isExternalReference attribute, if true, indicates that the actual object is not defined the corresponding element, rather its full details are defined elsewhere - indicated by either the registryURL, the repositoryURL, or the structureURL. The purpose of this is so that each structure message does not have to redefine object that are already defined elsewhere. If the isExternalReference attribute is not set, then it is assumed to be false, and the object should contain the full definition of its contents. If more than one of the registryURL, the repositoryURL, and the structureURL are supplied, then the application processing the object can choose the method it finds best suited to retrieve the details of the object.
serviceURL                           xs:anyURI               The serviceURL attribute indicates the URL of an SDMX SOAP web service from which the details of the object can be retrieved. Note that this can be a registry or and SDMX structural metadata repository, as they both implement that same web service interface.
structureURL                         xs:anyURI               The structureURL attribute indicates the URL of a SDMX-ML structure message (in the same version as the source document) in which the externally referenced object is contained. Note that this may be a URL of an SDMX RESTful web service which will return the referenced object.
isPartial (default: false)           xs:boolean              The isPartial, if true, indicates that only the relevant portion of the item scheme is being communicated. This is used in cases where a codelist is returned for a key family in the context of a constraint.
==================================== ======================= ==========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================

Element Documentation:

=============== =================== ===========================================================================================================================================================================================================================================
**Name**        **Type**            **Documentation**
=============== =================== ===========================================================================================================================================================================================================================================
com:Annotations com:AnnotationsType Annotations is a reusable element the provides for a collection of annotations. It has been made global so that restrictions of types that extend AnnotatableType my reference it.
com:Name        com:TextType        Name provides for a human-readable name for the object. This may be provided in multiple, parallel language-equivalent forms.
com:Description com:TextType        Description provides for a longer human-readable description of the object. This may be provided in multiple, parallel language-equivalent forms.
Code            CodeType            Code describes a code in a codelist. In addition to the identification and description of the code, basic presentational information is also available. Presentational information not present may be added through the use of annotations.
=============== =================== ===========================================================================================================================================================================================================================================

**CodeType: **\ CodeType describes the structure of a code. A code is
defined as a language independent set of letters, numbers or symbols
that represent a concept whose meaning is described in a natural
language. Presentational information not present may be added through
the use of annotations.

Derivation:

| *com:AnnotableType* (extension) 
|    |image84|\ *IdentifiableType* (extension) 
|          |image85|\ *NameableType* (restriction) 
|                |image86|\ *ItemBaseType* (extension) 
|                      |image87|\ *ItemType* (restriction) 
|                            |image88|\ CodeType

Attributes:

id, urn?, uri?

Content:

com:Annotations?, com:Name+, com:Description*, Parent?

Attribute Documentation:

======== ========== ==================================================================================================================================================================
**Name** **Type**   **Documentation**
======== ========== ==================================================================================================================================================================
id       com:IDType The id is the identifier for the object.
urn      xs:anyURI  The urn attribute holds a valid SDMX Registry URN (see SDMX Registry Specification for details).
uri      xs:anyURI  The uri attribute holds a URI that contains a link to a resource with additional information about the object, such as a web page. This uri is not a SDMX message.
======== ========== ==================================================================================================================================================================

Element Documentation:

=============== ============================ ==================================================================================================================================================================================
**Name**        **Type**                     **Documentation**
=============== ============================ ==================================================================================================================================================================================
com:Annotations com:AnnotationsType          Annotations is a reusable element the provides for a collection of annotations. It has been made global so that restrictions of types that extend AnnotatableType my reference it.
com:Name        com:TextType                 Name provides for a human-readable name for the object. This may be provided in multiple, parallel language-equivalent forms. It may be used in place of a short description.
com:Description com:TextType                 Description provides a plain text, human-readable description of the code. This may be provided in multiple, parallel language-equivalent forms.
Parent          com: LocalCodeReferenceTy pe Parent provides the ability to describe simple hierarchies within a single codelist, by referencing the id value of another code in the same codelist.
=============== ============================ ==================================================================================================================================================================================

**ConceptSchemeType: **\ onceptSchemeType describes the structure of a
concept scheme. A concept scheme is the descriptive information for an
arrangement or division of concepts into groups based on
characteristics, which the objects have in common. It contains a
collection of concept definitions, that may be arranged in simple
hierarchies.

Derivation:

| *com:AnnotableType* (extension) 
|    |image89|\ *IdentifiableType* (extension) 
|          |image90|\ *NameableType* (extension) 
|                |image91|\ *VersionableType* (restriction) 
|                      |image92|\ *MaintainableBaseType* (extension) 
|                            |image93|\ *MaintainableType* (extension) 
|                                  |image94|\ *ItemSchemeType* (restriction) 
|                                        |image95|\ ConceptSchemeType

Attributes:

id, urn?, uri?, version?, validFrom?, validTo?, agencyID, isFinal?,
isExternalReference?, serviceURL?, structureURL?, isPartial?

Content:

com:Annotations?, com:Name+, com:Description*, Concept\*

Attribute Documentation:

==================================== ======================= ==========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                             **Type**                **Documentation**
==================================== ======================= ==========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
id                                   com:NCNameIDType        The id attribute holds the identification of the concept scheme. The type of this id is restricted to the common:NCNNameIDType. This is necessary, since the concept scheme may be used to create simple types in data and metadata structure specific schemas and therefore must be compliant with the NCName type in XML Schema (see common:NCNameIDType for further details).
urn                                  xs:anyURI               The urn attribute holds a valid SDMX Registry URN (see SDMX Registry Specification for details).
uri                                  xs:anyURI               The uri attribute holds a URI that contains a link to a resource with additional information about the object, such as a web page. This uri is not a SDMX message.
version (default: 1.0)               com:VersionType         This version attribute holds a version number in the format of #[.#]+ (see common:VersionType definition for details). If not supplied, the version number is defaulted to 1.0.
validFrom                            xs:dateTime             The validFrom attribute provides the inclusive start date for providing supplemental validity information about the version.
validTo                              xs:dateTime             The validTo attribute provides the inclusive end date for providing supplemental validity information about the version.
agencyID                             com: NestedNCNameIDType The agencyID must be provided, and identifies the maintenance agency of the object.
isFinal (default: false)             xs:boolean              The isFinal attribute indicates whether the object is unchangeable without versioning. If the value is true, the object must be versioned upon change. If the final attribute is not supplied, then the object is assumed not to be final. Note that all production objects must be final.
isExternalReference (default: false) xs:boolean              The isExternalReference attribute, if true, indicates that the actual object is not defined the corresponding element, rather its full details are defined elsewhere - indicated by either the registryURL, the repositoryURL, or the structureURL. The purpose of this is so that each structure message does not have to redefine object that are already defined elsewhere. If the isExternalReference attribute is not set, then it is assumed to be false, and the object should contain the full definition of its contents. If more than one of the registryURL, the repositoryURL, and the structureURL are supplied, then the application processing the object can choose the method it finds best suited to retrieve the details of the object.
serviceURL                           xs:anyURI               The serviceURL attribute indicates the URL of an SDMX SOAP web service from which the details of the object can be retrieved. Note that this can be a registry or and SDMX structural metadata repository, as they both implement that same web service interface.
structureURL                         xs:anyURI               The structureURL attribute indicates the URL of a SDMX-ML structure message (in the same version as the source document) in which the externally referenced object is contained. Note that this may be a URL of an SDMX RESTful web service which will return the referenced object.
isPartial (default: false)           xs:boolean              The isPartial, if true, indicates that only the relevant portion of the item scheme is being communicated. This is used in cases where a codelist is returned for a key family in the context of a constraint.
==================================== ======================= ==========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================

Element Documentation:

=============== =================== ==================================================================================================================================================================================
**Name**        **Type**            **Documentation**
=============== =================== ==================================================================================================================================================================================
com:Annotations com:AnnotationsType Annotations is a reusable element the provides for a collection of annotations. It has been made global so that restrictions of types that extend AnnotatableType my reference it.
com:Name        com:TextType        Name provides for a human-readable name for the object. This may be provided in multiple, parallel language-equivalent forms.
com:Description com:TextType        Description provides for a longer human-readable description of the object. This may be provided in multiple, parallel language-equivalent forms.
Concept         ConceptType         Concept describes the details of a concept within a concept scheme.
=============== =================== ==================================================================================================================================================================================

**ConceptBaseType: **\ ConceptBaseType is an abstract base type the
forms the basis of the ConceptType by requiring a name and id, and
restricting the content of the id.

Derivation:

| *com:AnnotableType* (extension) 
|    |image96|\ *IdentifiableType* (extension) 
|          |image97|\ *NameableType* (restriction) 
|                |image98|\ *ItemBaseType* (extension) 
|                      |image99|\ *ItemType* (restriction) 
|                            |image100|\ *ConceptBaseType*

Attributes:

id, urn?, uri?

Content:

com:Annotations?, com:Name+, com:Description*, Parent?

Attribute Documentation:

======== ================ ================================================================================================================================================================================================================================================================================================================================================================================
**Name** **Type**         **Documentation**
======== ================ ================================================================================================================================================================================================================================================================================================================================================================================
id       com:NCNameIDType The id attribute holds the identification of the concept. The type of this id is restricted to the common:NCNNameIDType. This is necessary, since concept id may be used to create XML elements and attributes in data and metadata structure specific schemas and therefore must be compliant with the NCName type in XML Schema (see common:NCNameIDType for further details).
urn      xs:anyURI        The urn attribute holds a valid SDMX Registry URN (see SDMX Registry Specification for details).
uri      xs:anyURI        The uri attribute holds a URI that contains a link to a resource with additional information about the object, such as a web page. This uri is not a SDMX message.
======== ================ ================================================================================================================================================================================================================================================================================================================================================================================

Element Documentation:

=============== =============================== =========================================================================================================================================================================================================================
**Name**        **Type**                        **Documentation**
=============== =============================== =========================================================================================================================================================================================================================
com:Annotations com:AnnotationsType             Annotations is a reusable element the provides for a collection of annotations. It has been made global so that restrictions of types that extend AnnotatableType my reference it.
com:Name        com:TextType                    Name provides for a human-readable name for the object. This may be provided in multiple, parallel language-equivalent forms.
com:Description com:TextType                    Description provides for a longer human-readable description of the object. This may be provided in multiple, parallel language-equivalent forms.
Parent          com: LocalConceptReferenc eType Parent captures the semantic relationships between concepts which occur within a single concept scheme. This identifies the concept of which the current concept is a qualification (in the ISO 11179 sense) or subclass.
=============== =============================== =========================================================================================================================================================================================================================

**ConceptType: **\ ConceptType describes the details of a concept. A
concept is defined as a unit of knowledge created by a unique
combination of characteristics. If a concept does not specify a
TextFormat or a core representation, then the representation of the
concept is assumed to be represented by any set of valid characters
(corresponding to the xs:string datatype of W3C XML Schema).

Derivation:

| *com:AnnotableType* (extension) 
|    |image101|\ *IdentifiableType* (extension) 
|          |image102|\ *NameableType* (restriction) 
|                |image103|\ *ItemBaseType* (extension) 
|                      |image104|\ *ItemType* (restriction) 
|                            |image105|\ *ConceptBaseType* (extension) 
|                                  |image106|\ ConceptType

Attributes:

id, urn?, uri?

Content:

com:Annotations?, com:Name+, com:Description*, Parent?,
CoreRepresentation?, ISOConceptReference?

Attribute Documentation:

======== ================ ================================================================================================================================================================================================================================================================================================================================================================================
**Name** **Type**         **Documentation**
======== ================ ================================================================================================================================================================================================================================================================================================================================================================================
id       com:NCNameIDType The id attribute holds the identification of the concept. The type of this id is restricted to the common:NCNNameIDType. This is necessary, since concept id may be used to create XML elements and attributes in data and metadata structure specific schemas and therefore must be compliant with the NCName type in XML Schema (see common:NCNameIDType for further details).
urn      xs:anyURI        The urn attribute holds a valid SDMX Registry URN (see SDMX Registry Specification for details).
uri      xs:anyURI        The uri attribute holds a URI that contains a link to a resource with additional information about the object, such as a web page. This uri is not a SDMX message.
======== ================ ================================================================================================================================================================================================================================================================================================================================================================================

Element Documentation:

=================== =============================== =========================================================================================================================================================================================================================
**Name**            **Type**                        **Documentation**
=================== =============================== =========================================================================================================================================================================================================================
com:Annotations     com:AnnotationsType             Annotations is a reusable element the provides for a collection of annotations. It has been made global so that restrictions of types that extend AnnotatableType my reference it.
com:Name            com:TextType                    Name provides for a human-readable name for the object. This may be provided in multiple, parallel language-equivalent forms.
com:Description     com:TextType                    Description provides for a longer human-readable description of the object. This may be provided in multiple, parallel language-equivalent forms.
Parent              com: LocalConceptReferenc eType Parent captures the semantic relationships between concepts which occur within a single concept scheme. This identifies the concept of which the current concept is a qualification (in the ISO 11179 sense) or subclass.
CoreRepresentation  ConceptRepresentatio n         
ISOConceptReference ISOConceptReferenceT ype        Provides a reference to an ISO 11179 concept.
=================== =============================== =========================================================================================================================================================================================================================

**ConceptRepresentation: **\ ConceptRepresentation defines the core
representation that are allowed for a concept. The text format allowed
for a concept is that which is allowed for any non-target object
component.

Derivation:

| *RepresentationType* (restriction) 
|    |image107|\ ConceptRepresentation

Content:

(TextFormat \| (Enumeration, EnumerationFormat?))

Element Documentation:

================= ============================= ==============================================================================================================================
**Name**          **Type**                      **Documentation**
================= ============================= ==============================================================================================================================
TextFormat        BasicComponentTextFo rmatType TextFormat describes an uncoded textual format.
Enumeration       com: CodelistReferenceTyp e   Enumeration references a codelist which enumerates the possible values that can be used as the representation of this concept.
EnumerationFormat CodededTextFormatTyp e        EnumerationFormat describes the facets of the item scheme enumeration. This is for the most part, informational.
================= ============================= ==============================================================================================================================

**ISOConceptReferenceType: **\ ISOConceptReferenceType provides a
reference to and ISO 11179 concept.

Content:

ConceptAgency, ConceptSchemeID, ConceptID

Element Documentation:

=============== ========= =================
**Name**        **Type**  **Documentation**
=============== ========= =================
ConceptAgency   xs:string
ConceptSchemeID xs:string
ConceptID       xs:string
=============== ========= =================

**ConstraintBaseType: **\ ConstraintBaseType is an abstract base type
that forms the basis of the main abstract ConstraintType. It requires
that a name be provided.

Derivation:

| *com:AnnotableType* (extension) 
|    |image108|\ *IdentifiableType* (extension) 
|          |image109|\ *NameableType* (extension) 
|                |image110|\ *VersionableType* (restriction) 
|                      |image111|\ *MaintainableBaseType* (extension) 
|                            |image112|\ *MaintainableType* (restriction) 
|                                  |image113|\ *ConstraintBaseType*

Attributes:

id, urn?, uri?, version?, validFrom?, validTo?, agencyID, isFinal?,
isExternalReference?, serviceURL?, structureURL?

Content:

com:Annotations?, com:Name+, com:Description\*

Attribute Documentation:

==================================== ======================= ==========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                             **Type**                **Documentation**
==================================== ======================= ==========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
id                                   com:IDType              The id is the identifier for the object.
urn                                  xs:anyURI               The urn attribute holds a valid SDMX Registry URN (see SDMX Registry Specification for details).
uri                                  xs:anyURI               The uri attribute holds a URI that contains a link to a resource with additional information about the object, such as a web page. This uri is not a SDMX message.
version (default: 1.0)               com:VersionType         This version attribute holds a version number in the format of #[.#]+ (see common:VersionType definition for details). If not supplied, the version number is defaulted to 1.0.
validFrom                            xs:dateTime             The validFrom attribute provides the inclusive start date for providing supplemental validity information about the version.
validTo                              xs:dateTime             The validTo attribute provides the inclusive end date for providing supplemental validity information about the version.
agencyID                             com: NestedNCNameIDType The agencyID must be provided, and identifies the maintenance agency of the object.
isFinal (default: false)             xs:boolean              The isFinal attribute indicates whether the object is unchangeable without versioning. If the value is true, the object must be versioned upon change. If the final attribute is not supplied, then the object is assumed not to be final. Note that all production objects must be final.
isExternalReference (default: false) xs:boolean              The isExternalReference attribute, if true, indicates that the actual object is not defined the corresponding element, rather its full details are defined elsewhere - indicated by either the registryURL, the repositoryURL, or the structureURL. The purpose of this is so that each structure message does not have to redefine object that are already defined elsewhere. If the isExternalReference attribute is not set, then it is assumed to be false, and the object should contain the full definition of its contents. If more than one of the registryURL, the repositoryURL, and the structureURL are supplied, then the application processing the object can choose the method it finds best suited to retrieve the details of the object.
serviceURL                           xs:anyURI               The serviceURL attribute indicates the URL of an SDMX SOAP web service from which the details of the object can be retrieved. Note that this can be a registry or and SDMX structural metadata repository, as they both implement that same web service interface.
structureURL                         xs:anyURI               The structureURL attribute indicates the URL of a SDMX-ML structure message (in the same version as the source document) in which the externally referenced object is contained. Note that this may be a URL of an SDMX RESTful web service which will return the referenced object.
==================================== ======================= ==========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================

Element Documentation:

=============== =================== ==================================================================================================================================================================================
**Name**        **Type**            **Documentation**
=============== =================== ==================================================================================================================================================================================
com:Annotations com:AnnotationsType Annotations is a reusable element the provides for a collection of annotations. It has been made global so that restrictions of types that extend AnnotatableType my reference it.
com:Name        com:TextType        Name provides for a human-readable name for the object. This may be provided in multiple, parallel language-equivalent forms.
com:Description com:TextType        Description provides for a longer human-readable description of the object. This may be provided in multiple, parallel language-equivalent forms.
=============== =================== ==================================================================================================================================================================================

**ConstraintType: **\ ConstraintType is an abstract base type that
specific types of constraints (content and attachment) restrict and
extend to describe their details. The inclusion of a key or region in a
constraint is determined by first processing the included key sets, and
then removing those keys defined in the excluded key sets. If no
included key sets are defined, then it is assumed the all possible keys
or regions are included, and any excluded key or regions are removed
from this complete set.

Derivation:

| *com:AnnotableType* (extension) 
|    |image114|\ *IdentifiableType* (extension) 
|          |image115|\ *NameableType* (extension) 
|                |image116|\ *VersionableType* (restriction) 
|                      |image117|\ *MaintainableBaseType* (extension) 
|                            |image118|\ *MaintainableType* (restriction) 
|                                  |image119|\ *ConstraintBaseType* (extension) 
|                                        |image120|\ *ConstraintType*

Attributes:

id, urn?, uri?, version?, validFrom?, validTo?, agencyID, isFinal?,
isExternalReference?, serviceURL?, structureURL?

Content:

com:Annotations?, com:Name+, com:Description*, ConstraintAttachment?,
(DataKeySet \| MetadataKeySet \| CubeRegion \| MetadataTargetRegion)\*

Attribute Documentation:

==================================== ======================= ==========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                             **Type**                **Documentation**
==================================== ======================= ==========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
id                                   com:IDType              The id is the identifier for the object.
urn                                  xs:anyURI               The urn attribute holds a valid SDMX Registry URN (see SDMX Registry Specification for details).
uri                                  xs:anyURI               The uri attribute holds a URI that contains a link to a resource with additional information about the object, such as a web page. This uri is not a SDMX message.
version (default: 1.0)               com:VersionType         This version attribute holds a version number in the format of #[.#]+ (see common:VersionType definition for details). If not supplied, the version number is defaulted to 1.0.
validFrom                            xs:dateTime             The validFrom attribute provides the inclusive start date for providing supplemental validity information about the version.
validTo                              xs:dateTime             The validTo attribute provides the inclusive end date for providing supplemental validity information about the version.
agencyID                             com: NestedNCNameIDType The agencyID must be provided, and identifies the maintenance agency of the object.
isFinal (default: false)             xs:boolean              The isFinal attribute indicates whether the object is unchangeable without versioning. If the value is true, the object must be versioned upon change. If the final attribute is not supplied, then the object is assumed not to be final. Note that all production objects must be final.
isExternalReference (default: false) xs:boolean              The isExternalReference attribute, if true, indicates that the actual object is not defined the corresponding element, rather its full details are defined elsewhere - indicated by either the registryURL, the repositoryURL, or the structureURL. The purpose of this is so that each structure message does not have to redefine object that are already defined elsewhere. If the isExternalReference attribute is not set, then it is assumed to be false, and the object should contain the full definition of its contents. If more than one of the registryURL, the repositoryURL, and the structureURL are supplied, then the application processing the object can choose the method it finds best suited to retrieve the details of the object.
serviceURL                           xs:anyURI               The serviceURL attribute indicates the URL of an SDMX SOAP web service from which the details of the object can be retrieved. Note that this can be a registry or and SDMX structural metadata repository, as they both implement that same web service interface.
structureURL                         xs:anyURI               The structureURL attribute indicates the URL of a SDMX-ML structure message (in the same version as the source document) in which the externally referenced object is contained. Note that this may be a URL of an SDMX RESTful web service which will return the referenced object.
==================================== ======================= ==========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================

Element Documentation:

==================== ============================== ==================================================================================================================================================================================
**Name**             **Type**                       **Documentation**
==================== ============================== ==================================================================================================================================================================================
com:Annotations      com:AnnotationsType            Annotations is a reusable element the provides for a collection of annotations. It has been made global so that restrictions of types that extend AnnotatableType my reference it.
com:Name             com:TextType                   Name provides for a human-readable name for the object. This may be provided in multiple, parallel language-equivalent forms.
com:Description      com:TextType                   Description provides for a longer human-readable description of the object. This may be provided in multiple, parallel language-equivalent forms.
ConstraintAttachment *ConstraintAttachment Type*    ConstraintAttachment describes the collection of constrainable artefacts that the constraint is attached to.
DataKeySet           DataKeySetType                
MetadataKeySet       MetadataKeySetType            
CubeRegion           com:CubeRegionType            
MetadataTargetRegion com: MetadataTargetRegion Type
==================== ============================== ==================================================================================================================================================================================

**AttachmentConstraintType: **\ AttachmentConstraintType describes the
details of an attachment constraint by defining the data or metadata key
sets or component regions that attributes or reference metadata may be
attached in the constraint attachment objects.

Derivation:

| *com:AnnotableType* (extension) 
|    |image121|\ *IdentifiableType* (extension) 
|          |image122|\ *NameableType* (extension) 
|                |image123|\ *VersionableType* (restriction) 
|                      |image124|\ *MaintainableBaseType* (extension) 
|                            |image125|\ *MaintainableType* (restriction) 
|                                  |image126|\ *ConstraintBaseType* (extension) 
|                                        |image127|\ *ConstraintType* (restriction) 
|                                              |image128|\ AttachmentConstraintType

Attributes:

id, urn?, uri?, version?, validFrom?, validTo?, agencyID, isFinal?,
isExternalReference?, serviceURL?, structureURL?

Content:

com:Annotations?, com:Name+, com:Description*, ConstraintAttachment?,
(DataKeySet \| MetadataKeySet)\*

Attribute Documentation:

==================================== ======================= ==========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                             **Type**                **Documentation**
==================================== ======================= ==========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
id                                   com:IDType              The id is the identifier for the object.
urn                                  xs:anyURI               The urn attribute holds a valid SDMX Registry URN (see SDMX Registry Specification for details).
uri                                  xs:anyURI               The uri attribute holds a URI that contains a link to a resource with additional information about the object, such as a web page. This uri is not a SDMX message.
version (default: 1.0)               com:VersionType         This version attribute holds a version number in the format of #[.#]+ (see common:VersionType definition for details). If not supplied, the version number is defaulted to 1.0.
validFrom                            xs:dateTime             The validFrom attribute provides the inclusive start date for providing supplemental validity information about the version.
validTo                              xs:dateTime             The validTo attribute provides the inclusive end date for providing supplemental validity information about the version.
agencyID                             com: NestedNCNameIDType The agencyID must be provided, and identifies the maintenance agency of the object.
isFinal (default: false)             xs:boolean              The isFinal attribute indicates whether the object is unchangeable without versioning. If the value is true, the object must be versioned upon change. If the final attribute is not supplied, then the object is assumed not to be final. Note that all production objects must be final.
isExternalReference (default: false) xs:boolean              The isExternalReference attribute, if true, indicates that the actual object is not defined the corresponding element, rather its full details are defined elsewhere - indicated by either the registryURL, the repositoryURL, or the structureURL. The purpose of this is so that each structure message does not have to redefine object that are already defined elsewhere. If the isExternalReference attribute is not set, then it is assumed to be false, and the object should contain the full definition of its contents. If more than one of the registryURL, the repositoryURL, and the structureURL are supplied, then the application processing the object can choose the method it finds best suited to retrieve the details of the object.
serviceURL                           xs:anyURI               The serviceURL attribute indicates the URL of an SDMX SOAP web service from which the details of the object can be retrieved. Note that this can be a registry or and SDMX structural metadata repository, as they both implement that same web service interface.
structureURL                         xs:anyURI               The structureURL attribute indicates the URL of a SDMX-ML structure message (in the same version as the source document) in which the externally referenced object is contained. Note that this may be a URL of an SDMX RESTful web service which will return the referenced object.
==================================== ======================= ==========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================

Element Documentation:

==================== =================================== ==================================================================================================================================================================================
**Name**             **Type**                            **Documentation**
==================== =================================== ==================================================================================================================================================================================
com:Annotations      com:AnnotationsType                 Annotations is a reusable element the provides for a collection of annotations. It has been made global so that restrictions of types that extend AnnotatableType my reference it.
com:Name             com:TextType                        Name provides for a human-readable name for the object. This may be provided in multiple, parallel language-equivalent forms.
com:Description      com:TextType                        Description provides for a longer human-readable description of the object. This may be provided in multiple, parallel language-equivalent forms.
ConstraintAttachment AttachmentConstraint AttachmentType ConstraintAttachment describes the collection of constrainable artefacts that the constraint is attached to.
DataKeySet           DataKeySetType                     
MetadataKeySet       MetadataKeySetType                 
==================== =================================== ==================================================================================================================================================================================

**ContentConstraintBaseType: **\ ContentConstraintBaseType is an
abstract base type that forms the basis for the ContentConstraintType.

Derivation:

| *com:AnnotableType* (extension) 
|    |image129|\ *IdentifiableType* (extension) 
|          |image130|\ *NameableType* (extension) 
|                |image131|\ *VersionableType* (restriction) 
|                      |image132|\ *MaintainableBaseType* (extension) 
|                            |image133|\ *MaintainableType* (restriction) 
|                                  |image134|\ *ConstraintBaseType* (extension) 
|                                        |image135|\ *ConstraintType* (restriction) 
|                                              |image136|\ *ContentConstraintBaseType*

Attributes:

id, urn?, uri?, version?, validFrom?, validTo?, agencyID, isFinal?,
isExternalReference?, serviceURL?, structureURL?

Content:

com:Annotations?, com:Name+, com:Description*, ConstraintAttachment?,
(DataKeySet \| MetadataKeySet \| CubeRegion \| MetadataTargetRegion)\*

Attribute Documentation:

==================================== ======================= ==========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                             **Type**                **Documentation**
==================================== ======================= ==========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
id                                   com:IDType              The id is the identifier for the object.
urn                                  xs:anyURI               The urn attribute holds a valid SDMX Registry URN (see SDMX Registry Specification for details).
uri                                  xs:anyURI               The uri attribute holds a URI that contains a link to a resource with additional information about the object, such as a web page. This uri is not a SDMX message.
version (default: 1.0)               com:VersionType         This version attribute holds a version number in the format of #[.#]+ (see common:VersionType definition for details). If not supplied, the version number is defaulted to 1.0.
validFrom                            xs:dateTime             The validFrom attribute provides the inclusive start date for providing supplemental validity information about the version.
validTo                              xs:dateTime             The validTo attribute provides the inclusive end date for providing supplemental validity information about the version.
agencyID                             com: NestedNCNameIDType The agencyID must be provided, and identifies the maintenance agency of the object.
isFinal (default: false)             xs:boolean              The isFinal attribute indicates whether the object is unchangeable without versioning. If the value is true, the object must be versioned upon change. If the final attribute is not supplied, then the object is assumed not to be final. Note that all production objects must be final.
isExternalReference (default: false) xs:boolean              The isExternalReference attribute, if true, indicates that the actual object is not defined the corresponding element, rather its full details are defined elsewhere - indicated by either the registryURL, the repositoryURL, or the structureURL. The purpose of this is so that each structure message does not have to redefine object that are already defined elsewhere. If the isExternalReference attribute is not set, then it is assumed to be false, and the object should contain the full definition of its contents. If more than one of the registryURL, the repositoryURL, and the structureURL are supplied, then the application processing the object can choose the method it finds best suited to retrieve the details of the object.
serviceURL                           xs:anyURI               The serviceURL attribute indicates the URL of an SDMX SOAP web service from which the details of the object can be retrieved. Note that this can be a registry or and SDMX structural metadata repository, as they both implement that same web service interface.
structureURL                         xs:anyURI               The structureURL attribute indicates the URL of a SDMX-ML structure message (in the same version as the source document) in which the externally referenced object is contained. Note that this may be a URL of an SDMX RESTful web service which will return the referenced object.
==================================== ======================= ==========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================

Element Documentation:

==================== ================================ ==================================================================================================================================================================================================================
**Name**             **Type**                         **Documentation**
==================== ================================ ==================================================================================================================================================================================================================
com:Annotations      com:AnnotationsType              Annotations is a reusable element the provides for a collection of annotations. It has been made global so that restrictions of types that extend AnnotatableType my reference it.
com:Name             com:TextType                     Name provides for a human-readable name for the object. This may be provided in multiple, parallel language-equivalent forms.
com:Description      com:TextType                     Description provides for a longer human-readable description of the object. This may be provided in multiple, parallel language-equivalent forms.
ConstraintAttachment ContentConstraintAtt achmentType ConstraintAttachment describes the collection of constrainable artefacts that the constraint is attached to.
DataKeySet           DataKeySetType                   DataKeySet defines a collection of full or partial data keys.
MetadataKeySet       MetadataKeySetType               MetadataKeySet defines a collection of metadata keys.
CubeRegion           com:CubeRegionType               CubeRegion describes a set of dimension values which define a region and attributes which relate to the region for the purpose of describing a constraint.
MetadataTargetRegion com: MetadataTargetRegion Type   MetadataTargetRegion describes a set of target object values for a given report structure which define a region, and the metadata attribute which relate to the target for the purpose of describing a constraint.
==================== ================================ ==================================================================================================================================================================================================================

**ContentConstraintType: **\ ContentConstraintType describes the details
of a content constraint by defining the content regions, key sets, or
release information for the constraint attachment objects. Note that if
the constraint is for a data provider, then only release calendar
information is relevant, as there is no reliable way of determining
which key family is being used to frame constraints in terms of cube
regions or key sets.

Derivation:

| *com:AnnotableType* (extension) 
|    |image137|\ *IdentifiableType* (extension) 
|          |image138|\ *NameableType* (extension) 
|                |image139|\ *VersionableType* (restriction) 
|                      |image140|\ *MaintainableBaseType* (extension) 
|                            |image141|\ *MaintainableType* (restriction) 
|                                  |image142|\ *ConstraintBaseType* (extension) 
|                                        |image143|\ *ConstraintType* (restriction) 
|                                              |image144|\ *ContentConstraintBaseType* (extension) 
|                                                    |image145|\ ContentConstraintType

Attributes:

id, urn?, uri?, version?, validFrom?, validTo?, agencyID, isFinal?,
isExternalReference?, serviceURL?, structureURL?, type?

Content:

com:Annotations?, com:Name+, com:Description*, ConstraintAttachment?,
(DataKeySet \| MetadataKeySet \| CubeRegion \| MetadataTargetRegion)*,
ReleaseCalendar?, ReferencePeriod?

Attribute Documentation:

==================================== =================================== ==========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                             **Type**                            **Documentation**
==================================== =================================== ==========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
id                                   com:IDType                          The id is the identifier for the object.
urn                                  xs:anyURI                           The urn attribute holds a valid SDMX Registry URN (see SDMX Registry Specification for details).
uri                                  xs:anyURI                           The uri attribute holds a URI that contains a link to a resource with additional information about the object, such as a web page. This uri is not a SDMX message.
version (default: 1.0)               com:VersionType                     This version attribute holds a version number in the format of #[.#]+ (see common:VersionType definition for details). If not supplied, the version number is defaulted to 1.0.
validFrom                            xs:dateTime                         The validFrom attribute provides the inclusive start date for providing supplemental validity information about the version.
validTo                              xs:dateTime                         The validTo attribute provides the inclusive end date for providing supplemental validity information about the version.
agencyID                             com: NestedNCNameIDType             The agencyID must be provided, and identifies the maintenance agency of the object.
isFinal (default: false)             xs:boolean                          The isFinal attribute indicates whether the object is unchangeable without versioning. If the value is true, the object must be versioned upon change. If the final attribute is not supplied, then the object is assumed not to be final. Note that all production objects must be final.
isExternalReference (default: false) xs:boolean                          The isExternalReference attribute, if true, indicates that the actual object is not defined the corresponding element, rather its full details are defined elsewhere - indicated by either the registryURL, the repositoryURL, or the structureURL. The purpose of this is so that each structure message does not have to redefine object that are already defined elsewhere. If the isExternalReference attribute is not set, then it is assumed to be false, and the object should contain the full definition of its contents. If more than one of the registryURL, the repositoryURL, and the structureURL are supplied, then the application processing the object can choose the method it finds best suited to retrieve the details of the object.
serviceURL                           xs:anyURI                           The serviceURL attribute indicates the URL of an SDMX SOAP web service from which the details of the object can be retrieved. Note that this can be a registry or and SDMX structural metadata repository, as they both implement that same web service interface.
structureURL                         xs:anyURI                           The structureURL attribute indicates the URL of a SDMX-ML structure message (in the same version as the source document) in which the externally referenced object is contained. Note that this may be a URL of an SDMX RESTful web service which will return the referenced object.
type (default: Actual)               com: ContentConstraintTyp eCodeType The type attribute indicates whether this constraint states what data is actually present for the constraint attachment, or if it defines what content is allowed. The default value is "Actual", meaning the data actually present for the constraint attachment.
==================================== =================================== ==========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================

Element Documentation:

==================== ================================ ==================================================================================================================================================================================================================
**Name**             **Type**                         **Documentation**
==================== ================================ ==================================================================================================================================================================================================================
com:Annotations      com:AnnotationsType              Annotations is a reusable element the provides for a collection of annotations. It has been made global so that restrictions of types that extend AnnotatableType my reference it.
com:Name             com:TextType                     Name provides for a human-readable name for the object. This may be provided in multiple, parallel language-equivalent forms.
com:Description      com:TextType                     Description provides for a longer human-readable description of the object. This may be provided in multiple, parallel language-equivalent forms.
ConstraintAttachment ContentConstraintAtt achmentType ConstraintAttachment describes the collection of constrainable artefacts that the constraint is attached to.
DataKeySet           DataKeySetType                   DataKeySet defines a collection of full or partial data keys.
MetadataKeySet       MetadataKeySetType               MetadataKeySet defines a collection of metadata keys.
CubeRegion           com:CubeRegionType               CubeRegion describes a set of dimension values which define a region and attributes which relate to the region for the purpose of describing a constraint.
MetadataTargetRegion com: MetadataTargetRegion Type   MetadataTargetRegion describes a set of target object values for a given report structure which define a region, and the metadata attribute which relate to the target for the purpose of describing a constraint.
ReleaseCalendar      ReleaseCalendarType              ReleaseCalendar defines dates on which the constrained data is to be made available.
ReferencePeriod      com: ReferencePeriodType         ReferencePeriod is used to report start date and end date constraints.
==================== ================================ ==================================================================================================================================================================================================================

**ReleaseCalendarType: **\ ReleaseCalendarType describes information
about the timing of releases of the constrained data. All of these
values use the standard "P7D" - style format.

Content:

Periodicity, Offset, Tolerance

Element Documentation:

=========== ========= ===========================================================================================
**Name**    **Type**  **Documentation**
=========== ========= ===========================================================================================
Periodicity xs:string Periodicity is the period between releases of the data set.
Offset      xs:string Offset is the interval between January first and the first release of data within the year.
Tolerance   xs:string Tolerance is the period after which the release of data may be deemed late.
=========== ========= ===========================================================================================

**KeySetType: **\ KeySetType is an abstract base type for defining a
collection of keys.

Attributes:

isIncluded

Content:

Key+

Attribute Documentation:

========== ========== =========================================================================================================================
**Name**   **Type**   **Documentation**
========== ========== =========================================================================================================================
isIncluded xs:boolean The isIncluded attribute indicates whether the keys defined in this key set are inclusive or exclusive to the constraint.
========== ========== =========================================================================================================================

Element Documentation:

======== ===================== ============================================================================================================
**Name** **Type**              **Documentation**
======== ===================== ============================================================================================================
Key      *com:DistinctKeyType* Key contains a data or metadata key, which are sets of component values which identify the data or metadata.
======== ===================== ============================================================================================================

**DataKeySetType: **\ DataKeySetType defines a collection of full or
partial data keys (dimension values).

Derivation:

| *KeySetType* (restriction) 
|    |image146|\ DataKeySetType

Attributes:

isIncluded

Content:

Key+

Attribute Documentation:

========== ========== =========================================================================================================================
**Name**   **Type**   **Documentation**
========== ========== =========================================================================================================================
isIncluded xs:boolean The isIncluded attribute indicates whether the keys defined in this key set are inclusive or exclusive to the constraint.
========== ========== =========================================================================================================================

Element Documentation:

======== =============== =========================================================================
**Name** **Type**        **Documentation**
======== =============== =========================================================================
Key      com:DataKeyType Key contains a set of dimension values which identify a full set of data.
======== =============== =========================================================================

**MetadataKeySetType: **\ MetadataKeySetType defines a collection of
metadata keys (identifier component values).

Derivation:

| *KeySetType* (restriction) 
|    |image147|\ MetadataKeySetType

Attributes:

isIncluded

Content:

Key+

Attribute Documentation:

========== ========== =========================================================================================================================
**Name**   **Type**   **Documentation**
========== ========== =========================================================================================================================
isIncluded xs:boolean The isIncluded attribute indicates whether the keys defined in this key set are inclusive or exclusive to the constraint.
========== ========== =========================================================================================================================

Element Documentation:

======== =================== ==================================================================================================================================================================================================
**Name** **Type**            **Documentation**
======== =================== ==================================================================================================================================================================================================
Key      com:MetadataKeyType Key contains a set of target object values for a specified report structure which serve to identify which object reference metadata conforming to the specified report structure is available for.
======== =================== ==================================================================================================================================================================================================

**ConstraintAttachmentType: **\ ConstraintAttachmentType describes a
collection of references to constrainable artefacts.

Content:

(DataProvider \| DataSet+ \| MetadataSet+ \| SimpleDataSource+ \|
(DataStructure+, QueryableDataSource*) \| (MetadataStructure+,
QueryableDataSource*) \| (Dataflow+, QueryableDataSource*) \|
(Metadataflow+, QueryableDataSource*) \| (ProvisionAgreement+,
QueryableDataSource*))

Element Documentation:

=================== ===================================== =========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**            **Type**                              **Documentation**
=================== ===================================== =========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
DataProvider        com: DataProviderReferenc eType       DataProvider is reference to a data provider to which the constraint is attached. If this is used, then only the release calendar is relevant. The referenced is provided as a URN and/or a full set of reference fields.
DataSet             com:SetReferenceType                  DataSet is reference to a data set to which the constraint is attached. The referenced is provided as a URN and/or a full set of reference fields.
MetadataSet         com:SetReferenceType                  MetadataSet is reference to a metadata set to which the constraint is attached. The referenced is provided as a URN and/or a full set of reference fields.
SimpleDataSource    xs:anyURI                             SimpleDataSource describes a simple data source, which is a URL of a SDMX-ML data or metadata message.
DataStructure       com: DataStructureReferen ceType      DataStructure is reference to a data structure definition to which the constraint is attached. The referenced is provided as a URN and/or a full set of reference fields. A constraint which is attached to more than one data structure must only express key sets and/or cube regions where the identifiers of the dimensions are common across all structures to which the constraint is attached.
QueryableDataSource com: QueryableDataSourceT ype         QueryableDataSource describes a queryable data source to which the constraint is attached.
MetadataStructure   com: MetadataStructureRef erenceType  MetadataStructure is reference to a metadata structure definition to which the constraint is attached. The referenced is provided as a URN and/or a full set of reference fields. A constraint which is attached to more than one metadata structure must only express key sets and/or target regions where the identifiers of the target objects are common across all structures to which the constraint is attached.
QueryableDataSource com: QueryableDataSourceT ype         QueryableDataSource describes a queryable data source to which the constraint is attached.
Dataflow            com: DataflowReferenceTyp e           Dataflow is reference to a data flow to which the constraint is attached. The referenced is provided as a URN and/or a full set of reference fields. A constraint can be attached to more than one dataflow, and the dataflows do not necessarily have to be usages of the same data structure. However, a constraint which is attached to more than one data structure must only express key sets and/or cube regions where the identifiers of the dimensions are common across all structures to which the constraint is attached.
QueryableDataSource com: QueryableDataSourceT ype         QueryableDataSource describes a queryable data source to which the constraint is attached.
Metadataflow        com: MetadataflowReferenc eType       Metadataflow is reference to a metadata flow to which the constraint is attached. The referenced is provided as a URN and/or a full set of reference fields. A constraint can be attached to more than one metadataflow, and the metadataflows do not necessarily have to be usages of the same metadata structure. However, a constraint which is attached to more than one metadata structure must only express key sets and/or target regions where the identifiers of the target objects are common across all structures to which the constraint is attached.
QueryableDataSource com: QueryableDataSourceT ype         QueryableDataSource describes a queryable data source to which the constraint is attached.
ProvisionAgreement  com: ProvisionAgreementRe ferenceType ProvisionAgreementReference is reference to a provision agreement to which the constraint is attached. The referenced is provided as a URN and/or a full set of reference fields. A constraint can be attached to more than one provision aggreement, and the provision agreements do not necessarily have to be references structure usages based on the same structure. However, a constraint which is attached to more than one provision agreement must only express key sets and/or cube/target regions where the identifier of the components are common across all structures to which the constraint is attached.
QueryableDataSource com: QueryableDataSourceT ype         QueryableDataSource describes a queryable data source to which the constraint is attached.
=================== ===================================== =========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================

**AttachmentConstraintAttachmentType: **\ AttachmentConstraintAttachmentType
defines the structure for specifying the object to which an attachment
constraints applies.

Derivation:

| *ConstraintAttachmentType* (restriction) 
|    |image148|\ AttachmentConstraintAttachmentType

Content:

(DataSet+ \| MetadataSet+ \| SimpleDataSource+ \| DataStructure+ \|
MetadataStructure+ \| Dataflow+ \| Metadataflow+ \| ProvisionAgreement+)

Element Documentation:

================== ===================================== =========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**           **Type**                              **Documentation**
================== ===================================== =========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
DataSet            com:SetReferenceType                  DataSet is reference to a data set to which the constraint is attached. The referenced is provided as a URN and/or a full set of reference fields. Multiple instance can only be used if they have the same underlying structure.
MetadataSet        com:SetReferenceType                  MetadataSet is reference to a metadata set to which the constraint is attached. The referenced is provided as a URN and/or a full set of reference fields. Multiple instance can only be used if they have the same underlying structure.
SimpleDataSource   xs:anyURI                             SimpleDataSource describes a simple data source, which is a URL of a SDMX-ML data or metadata message. Multiple instance can only be used if they have the same underlying structure.
DataStructure      com: DataStructureReferen ceType      DataStructure is reference to a data structure definition to which the constraint is attached. The referenced is provided as a URN and/or a full set of reference fields. A constraint which is attached to more than one data structure must only express key sets and/or cube regions where the identifiers of the dimensions are common across all structures to which the constraint is attached.
MetadataStructure  com: MetadataStructureRef erenceType  MetadataStructure is reference to a metadata structure definition to which the constraint is attached. The referenced is provided as a URN and/or a full set of reference fields. A constraint which is attached to more than one metadata structure must only express key sets and/or target regions where the identifiers of the target objects are common across all structures to which the constraint is attached.
Dataflow           com: DataflowReferenceTyp e           Dataflow is reference to a data flow to which the constraint is attached. The referenced is provided as a URN and/or a full set of reference fields. A constraint can be attached to more than one dataflow, and the dataflows do not necessarily have to be usages of the same data structure. However, a constraint which is attached to more than one data structure must only express key sets and/or cube regions where the identifiers of the dimensions are common across all structures to which the constraint is attached.
Metadataflow       com: MetadataflowReferenc eType       Metadataflow is reference to a metadata flow to which the constraint is attached. The referenced is provided as a URN and/or a full set of reference fields. A constraint can be attached to more than one metadataflow, and the metadataflows do not necessarily have to be usages of the same metadata structure. However, a constraint which is attached to more than one metadata structure must only express key sets and/or target regions where the identifiers of the target objects are common across all structures to which the constraint is attached.
ProvisionAgreement com: ProvisionAgreementRe ferenceType ProvisionAgreementReference is reference to a provision agreement to which the constraint is attached. The referenced is provided as a URN and/or a full set of reference fields. A constraint can be attached to more than one provision aggreement, and the provision agreements do not necessarily have to be references structure usages based on the same structure. However, a constraint which is attached to more than one provision agreement must only express key sets and/or cube/target regions where the identifier of the components are common across all structures to which the constraint is attached.
================== ===================================== =========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================

**ContentConstraintAttachmentType: **\ ContentConstraintAttachmentType
defines the structure for specifying the target object(s) of a content
constraint.

Derivation:

| *ConstraintAttachmentType* (restriction) 
|    |image149|\ ContentConstraintAttachmentType

Content:

(DataProvider \| DataSet \| MetadataSet \| SimpleDataSource \|
(DataStructure+, QueryableDataSource*) \| (MetadataStructure+,
QueryableDataSource*) \| (Dataflow+, QueryableDataSource*) \|
(Metadataflow+, QueryableDataSource*) \| (ProvisionAgreement+,
QueryableDataSource*))

Element Documentation:

=================== ===================================== =========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**            **Type**                              **Documentation**
=================== ===================================== =========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
DataProvider        com: DataProviderReferenc eType       DataProvider is reference to a data provider to which the constraint is attached. If this is used, then only the release calendar is relevant. The referenced is provided as a URN and/or a full set of reference fields.
DataSet             com:SetReferenceType                  DataSet is reference to a data set to which the constraint is attached. The referenced is provided as a URN and/or a full set of reference fields.
MetadataSet         com:SetReferenceType                  MetadataSet is reference to a metadata set to which the constraint is attached. The referenced is provided as a URN and/or a full set of reference fields.
SimpleDataSource    xs:anyURI                             SimpleDataSource describes a simple data source, which is a URL of a SDMX-ML data or metadata message.
DataStructure       com: DataStructureReferen ceType      DataStructure is reference to a data structure definition to which the constraint is attached. The referenced is provided as a URN and/or a full set of reference fields. A constraint which is attached to more than one data structure must only express key sets and/or cube regions where the identifiers of the dimensions are common across all structures to which the constraint is attached.
QueryableDataSource com: QueryableDataSourceT ype         QueryableDataSource describes a queryable data source to which the constraint is attached.
MetadataStructure   com: MetadataStructureRef erenceType  MetadataStructure is reference to a metadata structure definition to which the constraint is attached. The referenced is provided as a URN and/or a full set of reference fields. A constraint which is attached to more than one metadata structure must only express key sets and/or target regions where the identifiers of the target objects are common across all structures to which the constraint is attached.
QueryableDataSource com: QueryableDataSourceT ype         QueryableDataSource describes a queryable data source to which the constraint is attached.
Dataflow            com: DataflowReferenceTyp e           Dataflow is reference to a data flow to which the constraint is attached. The referenced is provided as a URN and/or a full set of reference fields. A constraint can be attached to more than one dataflow, and the dataflows do not necessarily have to be usages of the same data structure. However, a constraint which is attached to more than one data structure must only express key sets and/or cube regions where the identifiers of the dimensions are common across all structures to which the constraint is attached.
QueryableDataSource com: QueryableDataSourceT ype         QueryableDataSource describes a queryable data source to which the constraint is attached.
Metadataflow        com: MetadataflowReferenc eType       Metadataflow is reference to a metadata flow to which the constraint is attached. The referenced is provided as a URN and/or a full set of reference fields. A constraint can be attached to more than one metadataflow, and the metadataflows do not necessarily have to be usages of the same metadata structure. However, a constraint which is attached to more than one metadata structure must only express key sets and/or target regions where the identifiers of the target objects are common across all structures to which the constraint is attached.
QueryableDataSource com: QueryableDataSourceT ype         QueryableDataSource describes a queryable data source to which the constraint is attached.
ProvisionAgreement  com: ProvisionAgreementRe ferenceType ProvisionAgreementReference is reference to a provision agreement to which the constraint is attached. The referenced is provided as a URN and/or a full set of reference fields. A constraint can be attached to more than one provision aggreement, and the provision agreements do not necessarily have to be references structure usages based on the same structure. However, a constraint which is attached to more than one provision agreement must only express key sets and/or cube/target regions where the identifier of the components are common across all structures to which the constraint is attached.
QueryableDataSource com: QueryableDataSourceT ype         QueryableDataSource describes a queryable data source to which the constraint is attached.
=================== ===================================== =========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================

**DataStructureType: **\ DataStructureType describes the structure of a
data structure definition. A data structure definition is defined as a
collection of metadata concepts, their structure and usage when used to
collect or disseminate data.

Derivation:

| *com:AnnotableType* (extension) 
|    |image150|\ *IdentifiableType* (extension) 
|          |image151|\ *NameableType* (extension) 
|                |image152|\ *VersionableType* (restriction) 
|                      |image153|\ *MaintainableBaseType* (extension) 
|                            |image154|\ *MaintainableType* (extension) 
|                                  |image155|\ *StructureType* (restriction) 
|                                        |image156|\ DataStructureType

Attributes:

id, urn?, uri?, version?, validFrom?, validTo?, agencyID, isFinal?,
isExternalReference?, serviceURL?, structureURL?

Content:

com:Annotations?, com:Name+, com:Description*, DataStructureComponents?

Attribute Documentation:

==================================== ======================= ==========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                             **Type**                **Documentation**
==================================== ======================= ==========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
id                                   com:IDType              The id is the identifier for the object.
urn                                  xs:anyURI               The urn attribute holds a valid SDMX Registry URN (see SDMX Registry Specification for details).
uri                                  xs:anyURI               The uri attribute holds a URI that contains a link to a resource with additional information about the object, such as a web page. This uri is not a SDMX message.
version (default: 1.0)               com:VersionType         This version attribute holds a version number in the format of #[.#]+ (see common:VersionType definition for details). If not supplied, the version number is defaulted to 1.0.
validFrom                            xs:dateTime             The validFrom attribute provides the inclusive start date for providing supplemental validity information about the version.
validTo                              xs:dateTime             The validTo attribute provides the inclusive end date for providing supplemental validity information about the version.
agencyID                             com: NestedNCNameIDType The agencyID must be provided, and identifies the maintenance agency of the object.
isFinal (default: false)             xs:boolean              The isFinal attribute indicates whether the object is unchangeable without versioning. If the value is true, the object must be versioned upon change. If the final attribute is not supplied, then the object is assumed not to be final. Note that all production objects must be final.
isExternalReference (default: false) xs:boolean              The isExternalReference attribute, if true, indicates that the actual object is not defined the corresponding element, rather its full details are defined elsewhere - indicated by either the registryURL, the repositoryURL, or the structureURL. The purpose of this is so that each structure message does not have to redefine object that are already defined elsewhere. If the isExternalReference attribute is not set, then it is assumed to be false, and the object should contain the full definition of its contents. If more than one of the registryURL, the repositoryURL, and the structureURL are supplied, then the application processing the object can choose the method it finds best suited to retrieve the details of the object.
serviceURL                           xs:anyURI               The serviceURL attribute indicates the URL of an SDMX SOAP web service from which the details of the object can be retrieved. Note that this can be a registry or and SDMX structural metadata repository, as they both implement that same web service interface.
structureURL                         xs:anyURI               The structureURL attribute indicates the URL of a SDMX-ML structure message (in the same version as the source document) in which the externally referenced object is contained. Note that this may be a URL of an SDMX RESTful web service which will return the referenced object.
==================================== ======================= ==========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================

Element Documentation:

======================== ============================ =====================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                 **Type**                     **Documentation**
======================== ============================ =====================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
com:Annotations          com:AnnotationsType          Annotations is a reusable element the provides for a collection of annotations. It has been made global so that restrictions of types that extend AnnotatableType my reference it.
com:Name                 com:TextType                 Name provides for a human-readable name for the object. This may be provided in multiple, parallel language-equivalent forms.
com:Description          com:TextType                 Description provides for a longer human-readable description of the object. This may be provided in multiple, parallel language-equivalent forms.
DataStructureCompone nts DataStructureCompone ntsType DataStructureComponents defines the grouping of the sets of metadata concepts that have a defined structural role in the data structure definition. Note that for any component or group defined in a data structure definition, its id must be unique. This applies to the identifiers explicitly defined by the components as well as those inherited from the concept identity of a component. For example, if two dimensions take their identity from concepts with same identity (regardless of whether the concepts exist in different schemes) one of the dimensions must be provided a different explicit identifier. Although there are XML schema constraints to help enforce this, these only apply to explicitly assigned identifiers. Identifiers inherited from a concept from which a component takes its identity cannot be validated against this constraint. Therefore, systems processing data structure definitions will have to perform this check outside of the XML validation. There are also three reserved identifiers in a data structure definition; OBS_VALUE, TIME_PERIOD, and REPORTING_PERIOD_START_DAY. These identifiers may not be used outside of their respective defintions (PrimaryMeasure, TimeDimension, and ReportingYearStartDay). This applies to both the explicit identifiers that can be assigned to the components or groups as well as an identifier inherited by a component from its concept identity. For example, if an ordinary dimension (i.e. not the time dimension) takes its concept identity from a concept with the identifier TIME_PERIOD, that dimension must provide a different explicit identifier.
======================== ============================ =====================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================

**DataStructureComponentsBaseType: **\ DataStructureComponentsBaseType
is an abstract base type the serves as the basis for the
DataStructureComponentsType. This type is necessary to allow for valid
substitutions of component lists.

Derivation:

| *GroupingType* (restriction) 
|    |image157|\ *DataStructureComponentsBaseType*

Content:

{Empty}

**DataStructureComponentsType: **\ DataStructureComponentsType describes
the structure of the grouping to the sets of metadata concepts that have
a defined structural role in the data structure definition. At a minimum
at least one dimension and a primary measure must be defined.

Derivation:

| *GroupingType* (restriction) 
|    |image158|\ *DataStructureComponentsBaseType* (extension) 
|          |image159|\ DataStructureComponentsType

Content:

DimensionList, Group*, AttributeList?, MeasureList

Element Documentation:

============= ================= ===============================================================================================================================================================================================================================================================================================================
**Name**      **Type**          **Documentation**
============= ================= ===============================================================================================================================================================================================================================================================================================================
DimensionList DimensionListType DimensionList describes the key descriptor for the data structure definition. It is an ordered set of metadata concepts that, combined, classify a statistical series, such as a time series, and whose values, when combined (the key) in an instance such as a data set, uniquely identify a specific series.
Group         GroupType         Group describes a group descriptor in a data structure definition. It is a set metadata concepts (and possibly their values) that define a partial key derived from the key descriptor in a data structure definition.
AttributeList AttributeListType AttributeList describes the attribute descriptor for the data structure definition. It is a collection of metadata concepts that define the attributes of the data structure definition.
MeasureList   MeasureListType   MeasureList describes the measure descriptor for a key family. It contains a single metadata concepts that define the primary measures of a data structure.
============= ================= ===============================================================================================================================================================================================================================================================================================================

**AttributeListBaseType: **\ AttributeListBaseType is an abstract base
type used as the basis for the AttributeListType.

Derivation:

| *com:AnnotableType* (extension) 
|    |image160|\ *IdentifiableType* (extension) 
|          |image161|\ *ComponentListType* (restriction) 
|                |image162|\ *AttributeListBaseType*

Attributes:

id?, urn?, uri?

Content:

com:Annotations?

Attribute Documentation:

=============================== ========== ==================================================================================================================================================================
**Name**                        **Type**   **Documentation**
=============================== ========== ==================================================================================================================================================================
id (fixed: AttributeDescriptor) com:IDType The id attribute is provided in this case for completeness. However, its value is fixed to AttributeDescriptor.
urn                             xs:anyURI  The urn attribute holds a valid SDMX Registry URN (see SDMX Registry Specification for details).
uri                             xs:anyURI  The uri attribute holds a URI that contains a link to a resource with additional information about the object, such as a web page. This uri is not a SDMX message.
=============================== ========== ==================================================================================================================================================================

Element Documentation:

=============== =================== ==================================================================================================================================================================================
**Name**        **Type**            **Documentation**
=============== =================== ==================================================================================================================================================================================
com:Annotations com:AnnotationsType Annotations is a reusable element the provides for a collection of annotations. It has been made global so that restrictions of types that extend AnnotatableType my reference it.
=============== =================== ==================================================================================================================================================================================

**AttributeListType: **\ AttributeListType describes the attribute
descriptor for the data structure definition.

Derivation:

| *com:AnnotableType* (extension) 
|    |image163|\ *IdentifiableType* (extension) 
|          |image164|\ *ComponentListType* (restriction) 
|                |image165|\ *AttributeListBaseType* (extension) 
|                      |image166|\ AttributeListType

Attributes:

id?, urn?, uri?

Content:

com:Annotations?, (Attribute \| ReportingYearStartDay)+

Attribute Documentation:

=============================== ========== ==================================================================================================================================================================
**Name**                        **Type**   **Documentation**
=============================== ========== ==================================================================================================================================================================
id (fixed: AttributeDescriptor) com:IDType The id attribute is provided in this case for completeness. However, its value is fixed to AttributeDescriptor.
urn                             xs:anyURI  The urn attribute holds a valid SDMX Registry URN (see SDMX Registry Specification for details).
uri                             xs:anyURI  The uri attribute holds a URI that contains a link to a resource with additional information about the object, such as a web page. This uri is not a SDMX message.
=============================== ========== ==================================================================================================================================================================

Element Documentation:

====================== ========================== =========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**               **Type**                   **Documentation**
====================== ========================== =========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
com:Annotations        com:AnnotationsType        Annotations is a reusable element the provides for a collection of annotations. It has been made global so that restrictions of types that extend AnnotatableType my reference it.
Attribute              AttributeType              Attribute describes the definition of a data attribute, which is defined as a characteristic of an object or entity.
ReportingYearStartDa y ReportingYearStartDa yType ReportingYearStartDay is a specialized data attribute which provides important context to the time dimension. If the value of the time dimension is one of the standard reporting periods (see common:ReportingTimePeriodType) then this attribute is used to state the month and day that the reporting year begins. This provides a reference point from which the actual calendar dates covered by these periods can be determined. If this attribute does not occur in a data set, then the reporting year start day will be assumed to be January 1.
====================== ========================== =========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================

**AttributeBaseType: **\ AttributeBaseType is an abstract base type that
serves as the basis for the AttributeType. It restricts the text format
base to a text format valid for data components (that does not allow for
XHTML representation). The local representation is restricted to the
values defined in codelist. The concept role is restricted to the values
valid for a data attribute.

Derivation:

| *com:AnnotableType* (extension) 
|    |image167|\ *IdentifiableType* (restriction) 
|          |image168|\ *ComponentBaseType* (extension) 
|                |image169|\ *ComponentType* (restriction) 
|                      |image170|\ *AttributeBaseType*

Attributes:

id?, urn?, uri?

Content:

com:Annotations?, ConceptIdentity, LocalRepresentation?

Attribute Documentation:

======== ================ ================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name** **Type**         **Documentation**
======== ================ ================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
id       com:NCNameIDType The id attribute holds an explicit identification of the component. If this identifier is not supplied, then it is assumed to be the same as the identifier of the concept referenced from the concept identity. Because structures require that every component be given a unique identifier, it may be necessary to assign an explicit identifier when more than one component in a structure reference concepts with same identifier. It is important to note that this applies strictly to the identifier of concept and not the URN. Therefore if two concepts with the same identifier from different concept schemes are referenced in the same structure, one of the components will have to provide a unique explicit identifier. The type of this identifier is restricted to the common:NCNameIDType. This is necessary, since component identifiers are used to create XML elements and attributes in data and metadata structure specific schemas and therefore must be compliant with the NCName type in XML Schema (see common:NCNameIDType for further details).
urn      xs:anyURI        The urn attribute holds a valid SDMX Registry URN (see SDMX Registry Specification for details).
uri      xs:anyURI        The uri attribute holds a URI that contains a link to a resource with additional information about the object, such as a web page. This uri is not a SDMX message.
======== ================ ================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================

Element Documentation:

=================== ====================================== ==============================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**            **Type**                               **Documentation**
=================== ====================================== ==============================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
com:Annotations     com:AnnotationsType                    Annotations is a reusable element the provides for a collection of annotations. It has been made global so that restrictions of types that extend AnnotatableType my reference it.
ConceptIdentity     com: ConceptReferenceType              ConceptIdentity allows for the referencing of a concept in a concept scheme. The component takes its semantic from this concept, and if an id is not specified, it takes its identification as well. If a representation (LocalRepresentation) is not supplied, then the representation of the component is also inherited from the concept. Note that in the case of the component representation being inherited from the concept, the allowable representations for the component still apply. Therefore, if a component references a concept with a core representation that is not allowed for the concept, that representation must be locally overridden. For components which can specify a concept role, it is implied that the concept which is referenced also identifies a role for the component.
LocalRepresentation SimpleDataStructureR epresentationType LocalRepresentation references item schemes that may be used to create the representation of a component. The type of this must be refined such that a concrete item scheme reference is used.
=================== ====================================== ==============================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================

**AttributeType: **\ AttributeType describes the structure of a data
attribute, which is defined as a characteristic of an object or entity.
The attribute takes its semantic, and in some cases it representation,
from its concept identity. An attribute can be coded by referencing a
code list from its coded local representation. It can also specify its
text format, which is used as the representation of the attribute if a
coded representation is not defined. Neither the coded or uncoded
representation are necessary, since the attribute may take these from
the referenced concept. An attribute specifies its relationship with
other data structure components and is given an assignment status. These
two properties dictate where in a data message the attribute will be
attached, and whether or not the attribute will be required to be given
a value. A set of roles defined in concept scheme can be assigned to the
attribute.

Derivation:

| *com:AnnotableType* (extension) 
|    |image171|\ *IdentifiableType* (restriction) 
|          |image172|\ *ComponentBaseType* (extension) 
|                |image173|\ *ComponentType* (restriction) 
|                      |image174|\ *AttributeBaseType* (extension) 
|                            |image175|\ AttributeType

Attributes:

id?, urn?, uri?, assignmentStatus

Content:

com:Annotations?, ConceptIdentity, LocalRepresentation?, ConceptRole*,
AttributeRelationship

Attribute Documentation:

================ ================ ================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**         **Type**         **Documentation**
================ ================ ================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
id               com:NCNameIDType The id attribute holds an explicit identification of the component. If this identifier is not supplied, then it is assumed to be the same as the identifier of the concept referenced from the concept identity. Because structures require that every component be given a unique identifier, it may be necessary to assign an explicit identifier when more than one component in a structure reference concepts with same identifier. It is important to note that this applies strictly to the identifier of concept and not the URN. Therefore if two concepts with the same identifier from different concept schemes are referenced in the same structure, one of the components will have to provide a unique explicit identifier. The type of this identifier is restricted to the common:NCNameIDType. This is necessary, since component identifiers are used to create XML elements and attributes in data and metadata structure specific schemas and therefore must be compliant with the NCName type in XML Schema (see common:NCNameIDType for further details).
urn              xs:anyURI        The urn attribute holds a valid SDMX Registry URN (see SDMX Registry Specification for details).
uri              xs:anyURI        The uri attribute holds a URI that contains a link to a resource with additional information about the object, such as a web page. This uri is not a SDMX message.
assignmentStatus UsageStatusType  The assignmentStatus attribute indicates whether a value must be provided for the attribute when sending documentation along with the data.
================ ================ ================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================

Element Documentation:

====================== ====================================== ==============================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**               **Type**                               **Documentation**
====================== ====================================== ==============================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
com:Annotations        com:AnnotationsType                    Annotations is a reusable element the provides for a collection of annotations. It has been made global so that restrictions of types that extend AnnotatableType my reference it.
ConceptIdentity        com: ConceptReferenceType              ConceptIdentity allows for the referencing of a concept in a concept scheme. The component takes its semantic from this concept, and if an id is not specified, it takes its identification as well. If a representation (LocalRepresentation) is not supplied, then the representation of the component is also inherited from the concept. Note that in the case of the component representation being inherited from the concept, the allowable representations for the component still apply. Therefore, if a component references a concept with a core representation that is not allowed for the concept, that representation must be locally overridden. For components which can specify a concept role, it is implied that the concept which is referenced also identifies a role for the component.
LocalRepresentation    SimpleDataStructureR epresentationType LocalRepresentation references item schemes that may be used to create the representation of a component. The type of this must be refined such that a concrete item scheme reference is used.
ConceptRole            com: ConceptReferenceType              ConceptRole references concepts which define roles which this attribute serves. If the concept from which the attribute takes its identity also defines a role the concept serves, then the isConceptRole indicator can be set to true on the concept identity rather than repeating the reference here.
AttributeRelationshi p AttributeRelationshi pType             AttributeRelationship describes how the value of this attribute varies with the values of other components. These relationships will be used to determine the attachment level of the attribute in the various data formats.
====================== ====================================== ==============================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================

**AttributeRelationshipType: **\ AttributeRelationshipType defines the
structure for stating the relationship between an attribute and other
data structure definition components.

Content:

(None \| (Dimension+, AttachmentGroup*) \| Group \| PrimaryMeasure)

Element Documentation:

=============== ========================================== =====================================================================================================================================================================================================================================================================================================================================================
**Name**        **Type**                                   **Documentation**
=============== ========================================== =====================================================================================================================================================================================================================================================================================================================================================
None            com:EmptyType                              This means that value of the attribute will not vary with any of the other key family components. This will always be treated as a data set level attribute.
Dimension       com: LocalDimensionRefere nceType          This is used to reference dimensions in the data structure definition on which the value of this attribute depends. An attribute using this relationship can be either a group, series (or section), or observation level attribute. The attachment level of the attribute will be determined by the data format and which dimensions are referenced.
AttachmentGroup com: LocalGroupKeyDescrip torReferenceType This is used to specify that the attribute should always be attached to the groups referenced here. Note that if one of the referenced dimensions is the time dimension, the groups referenced here will be ignored.
Group           com: LocalGroupKeyDescrip torReferenceType This is used as a convenience to referencing all of the dimension defined by the referenced group. The attribute will also be attached to this group.
PrimaryMeasure  com: LocalPrimaryMeasureR eferenceType     This is used to specify that the value of the attribute is dependent upon the observed value. An attribute with this relationship will always be treated as an observation level attribute.
=============== ========================================== =====================================================================================================================================================================================================================================================================================================================================================

**ReportingYearStartDayType: **\ ReportingYearStartDayType defines the
structure of the reporting year start day attribute. The reporting year
start day attribute takes its semantic from its concept identity
(usually the REPORTING_YEAR_START_DAY concept), yet is always has a
fixed identifier (REPORTING_YEAR_START_DAY). The reporting year start
day attribute always has a fixed text format, which specifies that the
format of its value is always a day and month in the ISO 8601 format of
'--MM-DD'. As with any other attribute, an attribute relationship must
be specified. this relationship should be carefully selected as it will
determin what type of data the data structure definition will allow. For
example, if an attribute relationship of none is specified, this will
mean the data sets conforming to this data structure definition can only
contain data with standard reporting periods where the all reporting
periods have the same start day. In this case, data reported as standard
reporting periods from two entities with different fiscal year start
days could not be contained in the same data set.

Derivation:

| *com:AnnotableType* (extension) 
|    |image176|\ *IdentifiableType* (restriction) 
|          |image177|\ *ComponentBaseType* (extension) 
|                |image178|\ *ComponentType* (restriction) 
|                      |image179|\ *AttributeBaseType* (extension) 
|                            |image180|\ AttributeType (restriction) 
|                                  |image181|\ ReportingYearStartDayType

Attributes:

id?, urn?, uri?, assignmentStatus

Content:

com:Annotations?, ConceptIdentity, LocalRepresentation,
AttributeRelationship

Attribute Documentation:

==================================== ================ ================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                             **Type**         **Documentation**
==================================== ================ ================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
id (fixed: REPORTING_YEAR_START_DAY) com:NCNameIDType The id attribute holds an explicit identification of the component. If this identifier is not supplied, then it is assumed to be the same as the identifier of the concept referenced from the concept identity. Because structures require that every component be given a unique identifier, it may be necessary to assign an explicit identifier when more than one component in a structure reference concepts with same identifier. It is important to note that this applies strictly to the identifier of concept and not the URN. Therefore if two concepts with the same identifier from different concept schemes are referenced in the same structure, one of the components will have to provide a unique explicit identifier. The type of this identifier is restricted to the common:NCNameIDType. This is necessary, since component identifiers are used to create XML elements and attributes in data and metadata structure specific schemas and therefore must be compliant with the NCName type in XML Schema (see common:NCNameIDType for further details).
urn                                  xs:anyURI        The urn attribute holds a valid SDMX Registry URN (see SDMX Registry Specification for details).
uri                                  xs:anyURI        The uri attribute holds a URI that contains a link to a resource with additional information about the object, such as a web page. This uri is not a SDMX message.
assignmentStatus                     UsageStatusType  The assignmentStatus attribute indicates whether a value must be provided for the attribute when sending documentation along with the data.
==================================== ================ ================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================

Element Documentation:

====================== ======================================== ==============================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**               **Type**                                 **Documentation**
====================== ======================================== ==============================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
com:Annotations        com:AnnotationsType                      Annotations is a reusable element the provides for a collection of annotations. It has been made global so that restrictions of types that extend AnnotatableType my reference it.
ConceptIdentity        com: ConceptReferenceType                ConceptIdentity allows for the referencing of a concept in a concept scheme. The component takes its semantic from this concept, and if an id is not specified, it takes its identification as well. If a representation (LocalRepresentation) is not supplied, then the representation of the component is also inherited from the concept. Note that in the case of the component representation being inherited from the concept, the allowable representations for the component still apply. Therefore, if a component references a concept with a core representation that is not allowed for the concept, that representation must be locally overridden. For components which can specify a concept role, it is implied that the concept which is referenced also identifies a role for the component.
LocalRepresentation    ReportingYearStartDa yRepresentationType LocalRepresentation references item schemes that may be used to create the representation of a component. The type of this must be refined such that a concrete item scheme reference is used.
AttributeRelationshi p AttributeRelationshi pType               AttributeRelationship describes how the value of this attribute varies with the values of other components. These relationships will be used to determine the attachment level of the attribute in the various data formats.
====================== ======================================== ==============================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================

**ReportingYearStartDayRepresentationType: **\ ReportingYearStartDayRepresentationType
defines the representation for the reporting year start day attribute.
Enumerated values are not allowed and the text format is fixed to be a
day and month in the ISO 8601 format of '--MM-DD'.

Derivation:

| *RepresentationType* (restriction) 
|    |image182|\ *DataStructureRepresentationType* (restriction) 
|          |image183|\ SimpleDataStructureRepresentationType
  (restriction) 
|                |image184|\ ReportingYearStartDayRepresentationType

Content:

TextFormat

Element Documentation:

========== ==================================== ===============================================
**Name**   **Type**                             **Documentation**
========== ==================================== ===============================================
TextFormat ReportingYearStartDa yTextFormatType TextFormat describes an uncoded textual format.
========== ==================================== ===============================================

**ReportingYearStartDayTextFormatType: **\ ReportingYearStartDayTextFormatType
is a restricted version of the NonFacetedTextFormatType that fixes the
value of the text type to be DayMonth. This type exists solely for the
purpose of fixing the representation of the reporting year start day
attribute.

Derivation:

| TextFormatType (restriction) 
|    |image185|\ BasicComponentTextFormatType (restriction) 
|          |image186|\ SimpleComponentTextFormatType (restriction) 
|                |image187|\ NonFacetedTextFormatType (restriction) 
|                      |image188|\ ReportingYearStartDayTextFormatType

Attributes:

textType?

Content:

{Empty}

Attribute Documentation:

========================== ================== ================================================================================================================================================================================================================================================
**Name**                   **Type**           **Documentation**
========================== ================== ================================================================================================================================================================================================================================================
textType (fixed: MonthDay) com:SimpleDataType The textType attribute provides a description of the datatype. If it is not specified, any valid characters may be included in the text field (it corresponds to the xs:string datatype of W3C XML Schema) within the constraints of the facets.
========================== ================== ================================================================================================================================================================================================================================================

**DimensionListBaseType: **\ DimensionListBaseType is an abstract base
type used as the basis for the DimensionListType.

Derivation:

| *com:AnnotableType* (extension) 
|    |image189|\ *IdentifiableType* (extension) 
|          |image190|\ *ComponentListType* (restriction) 
|                |image191|\ *DimensionListBaseType*

Attributes:

id?, urn?, uri?

Content:

com:Annotations?

Attribute Documentation:

=============================== ========== ==================================================================================================================================================================
**Name**                        **Type**   **Documentation**
=============================== ========== ==================================================================================================================================================================
id (fixed: DimensionDescriptor) com:IDType The id attribute is provided in this case for completeness. However, its value is fixed to DimensionDescriptor.
urn                             xs:anyURI  The urn attribute holds a valid SDMX Registry URN (see SDMX Registry Specification for details).
uri                             xs:anyURI  The uri attribute holds a URI that contains a link to a resource with additional information about the object, such as a web page. This uri is not a SDMX message.
=============================== ========== ==================================================================================================================================================================

Element Documentation:

=============== =================== ==================================================================================================================================================================================
**Name**        **Type**            **Documentation**
=============== =================== ==================================================================================================================================================================================
com:Annotations com:AnnotationsType Annotations is a reusable element the provides for a collection of annotations. It has been made global so that restrictions of types that extend AnnotatableType my reference it.
=============== =================== ==================================================================================================================================================================================

**DimensionListType: **\ DimensionListType describes the key descriptor
for a data structure definition. The order of the declaration of child
dimensions is significant: it is used to describe the order in which
they will appear in data formats for which key values are supplied in an
ordered fashion (exclusive of the time dimension, which is not
represented as a member of the ordered key). Any data structure
definition which uses the time dimension should also declare a frequency
dimension, conventionally the first dimension in the key (the set of
ordered non-time dimensions). If is not necessary to assign a time
dimension, as data can be organised in any fashion required.

Derivation:

| *com:AnnotableType* (extension) 
|    |image192|\ *IdentifiableType* (extension) 
|          |image193|\ *ComponentListType* (restriction) 
|                |image194|\ *DimensionListBaseType* (extension) 
|                      |image195|\ DimensionListType

Attributes:

id?, urn?, uri?

Content:

com:Annotations?, (Dimension \| MeasureDimension \| TimeDimension)+

Attribute Documentation:

=============================== ========== ==================================================================================================================================================================
**Name**                        **Type**   **Documentation**
=============================== ========== ==================================================================================================================================================================
id (fixed: DimensionDescriptor) com:IDType The id attribute is provided in this case for completeness. However, its value is fixed to DimensionDescriptor.
urn                             xs:anyURI  The urn attribute holds a valid SDMX Registry URN (see SDMX Registry Specification for details).
uri                             xs:anyURI  The uri attribute holds a URI that contains a link to a resource with additional information about the object, such as a web page. This uri is not a SDMX message.
=============================== ========== ==================================================================================================================================================================

Element Documentation:

================ ==================== =========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**         **Type**             **Documentation**
================ ==================== =========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
com:Annotations  com:AnnotationsType  Annotations is a reusable element the provides for a collection of annotations. It has been made global so that restrictions of types that extend AnnotatableType my reference it.
Dimension        DimensionType        Dimension describes the structure of a dimension, which is defined as a statistical concept used (most probably together with other statistical concepts) to identify a statistical series, such as a time series, e.g. a statistical concept indicating certain economic activity or a geographical reference area.
MeasureDimension MeasureDimensionType MeasureDimension is a special type of dimension which defines multiple measures in a key family. This is represented as any other dimension in a unless it is the observation dimension. It takes it representation from a concept scheme, and this scheme defines the measures and their representations. When data is formatted with this as the observation dimension, these measures can be made explicit or the value of the dimension can be treated as any other dimension. If the measures are explicit, the representation of the observation will be specific to the core representation for each concept in the representation concept scheme. Note that it is necessary that these representations are compliant (the same or derived from) with that of the primary measure.
TimeDimension    TimeDimensionType    TimeDimension is a special dimension which designates the period in time in which the data identified by the full series key applies.
================ ==================== =========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================

**BaseDimensionBaseType: **\ BaseDimensionBaseType is an abstract base
type that serves as the basis for any dimension. It restricts the text
format base to a text format valid for data components (that does not
allow for XHTML representation).

Derivation:

| *com:AnnotableType* (extension) 
|    |image196|\ *IdentifiableType* (restriction) 
|          |image197|\ *ComponentBaseType* (extension) 
|                |image198|\ *ComponentType* (restriction) 
|                      |image199|\ *BaseDimensionBaseType*

Attributes:

id?, urn?, uri?

Content:

com:Annotations?, ConceptIdentity, LocalRepresentation?

Attribute Documentation:

======== ================ ================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name** **Type**         **Documentation**
======== ================ ================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
id       com:NCNameIDType The id attribute holds an explicit identification of the component. If this identifier is not supplied, then it is assumed to be the same as the identifier of the concept referenced from the concept identity. Because structures require that every component be given a unique identifier, it may be necessary to assign an explicit identifier when more than one component in a structure reference concepts with same identifier. It is important to note that this applies strictly to the identifier of concept and not the URN. Therefore if two concepts with the same identifier from different concept schemes are referenced in the same structure, one of the components will have to provide a unique explicit identifier. The type of this identifier is restricted to the common:NCNameIDType. This is necessary, since component identifiers are used to create XML elements and attributes in data and metadata structure specific schemas and therefore must be compliant with the NCName type in XML Schema (see common:NCNameIDType for further details).
urn      xs:anyURI        The urn attribute holds a valid SDMX Registry URN (see SDMX Registry Specification for details).
uri      xs:anyURI        The uri attribute holds a URI that contains a link to a resource with additional information about the object, such as a web page. This uri is not a SDMX message.
======== ================ ================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================

Element Documentation:

=================== ================================== ==============================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**            **Type**                           **Documentation**
=================== ================================== ==============================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
com:Annotations     com:AnnotationsType                Annotations is a reusable element the provides for a collection of annotations. It has been made global so that restrictions of types that extend AnnotatableType my reference it.
ConceptIdentity     com: ConceptReferenceType          ConceptIdentity allows for the referencing of a concept in a concept scheme. The component takes its semantic from this concept, and if an id is not specified, it takes its identification as well. If a representation (LocalRepresentation) is not supplied, then the representation of the component is also inherited from the concept. Note that in the case of the component representation being inherited from the concept, the allowable representations for the component still apply. Therefore, if a component references a concept with a core representation that is not allowed for the concept, that representation must be locally overridden. For components which can specify a concept role, it is implied that the concept which is referenced also identifies a role for the component.
LocalRepresentation *DataStructureReprese ntationType* LocalRepresentation references item schemes that may be used to create the representation of a component. The type of this must be refined such that a concrete item scheme reference is used.
=================== ================================== ==============================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================

**BaseDimensionType: **\ BaseDimensionType is an abstract base type
which defines the basic structure of all dimensions.

Derivation:

| *com:AnnotableType* (extension) 
|    |image200|\ *IdentifiableType* (restriction) 
|          |image201|\ *ComponentBaseType* (extension) 
|                |image202|\ *ComponentType* (restriction) 
|                      |image203|\ *BaseDimensionBaseType* (extension) 
|                            |image204|\ *BaseDimensionType*

Attributes:

id?, urn?, uri?, position?, type?

Content:

com:Annotations?, ConceptIdentity, LocalRepresentation?, ConceptRole\*

Attribute Documentation:

======== ====================== ================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name** **Type**               **Documentation**
======== ====================== ================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
id       com:NCNameIDType       The id attribute holds an explicit identification of the component. If this identifier is not supplied, then it is assumed to be the same as the identifier of the concept referenced from the concept identity. Because structures require that every component be given a unique identifier, it may be necessary to assign an explicit identifier when more than one component in a structure reference concepts with same identifier. It is important to note that this applies strictly to the identifier of concept and not the URN. Therefore if two concepts with the same identifier from different concept schemes are referenced in the same structure, one of the components will have to provide a unique explicit identifier. The type of this identifier is restricted to the common:NCNameIDType. This is necessary, since component identifiers are used to create XML elements and attributes in data and metadata structure specific schemas and therefore must be compliant with the NCName type in XML Schema (see common:NCNameIDType for further details).
urn      xs:anyURI              The urn attribute holds a valid SDMX Registry URN (see SDMX Registry Specification for details).
uri      xs:anyURI              The uri attribute holds a URI that contains a link to a resource with additional information about the object, such as a web page. This uri is not a SDMX message.
position xs:int                 The position attribute specifies the position of the dimension in the data structure definition. It is optional an the position of the dimension in the key descriptor (DimensionList element) always takes precedence over the value supplied here. This is strictly for informational purposes only.
type     com: DimensionTypeType The type attribute identifies whether then dimension is a measure dimension, the time dimension, or a regular dimension. Although these are all apparent by the element names, this attribute allows for each dimension to be processed independent of its element as well as maintaining the restriction of only one measure and time dimension while still allowing dimension to occur in any order.
======== ====================== ================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================

Element Documentation:

=================== ================================== ==============================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**            **Type**                           **Documentation**
=================== ================================== ==============================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
com:Annotations     com:AnnotationsType                Annotations is a reusable element the provides for a collection of annotations. It has been made global so that restrictions of types that extend AnnotatableType my reference it.
ConceptIdentity     com: ConceptReferenceType          ConceptIdentity allows for the referencing of a concept in a concept scheme. The component takes its semantic from this concept, and if an id is not specified, it takes its identification as well. If a representation (LocalRepresentation) is not supplied, then the representation of the component is also inherited from the concept. Note that in the case of the component representation being inherited from the concept, the allowable representations for the component still apply. Therefore, if a component references a concept with a core representation that is not allowed for the concept, that representation must be locally overridden. For components which can specify a concept role, it is implied that the concept which is referenced also identifies a role for the component.
LocalRepresentation *DataStructureReprese ntationType* LocalRepresentation references item schemes that may be used to create the representation of a component. The type of this must be refined such that a concrete item scheme reference is used.
ConceptRole         com: ConceptReferenceType          ConceptRole references concepts which define roles which this dimension serves. If the concept from which the attribute takes its identity also defines a role the concept serves, then the isConceptRole indicator can be set to true on the concept identity rather than repeating the reference here.
=================== ================================== ==============================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================

**DimensionType: **\ DimensionType describes the structure of an
ordinary dimension, which is defined as a statistical concept used (most
probably together with other statistical concepts) to identify a
statistical series, such as a time series, e.g. a statistical concept
indicating certain economic activity or a geographical reference area.
The dimension takes its semantic, and in some cases it representation,
from its concept identity. A dimension can be coded by referencing a
code list from its coded local representation. It can also specify its
text format, which is used as the representation of the dimension if a
coded representation is not defined. Neither the coded or uncoded
representation are necessary, since the dimension may take these from
the referenced concept.

Derivation:

| *com:AnnotableType* (extension) 
|    |image205|\ *IdentifiableType* (restriction) 
|          |image206|\ *ComponentBaseType* (extension) 
|                |image207|\ *ComponentType* (restriction) 
|                      |image208|\ *BaseDimensionBaseType* (extension) 
|                            |image209|\ *BaseDimensionType* (restriction) 
|                                  |image210|\ DimensionType

Attributes:

id?, urn?, uri?, position?, type?

Content:

com:Annotations?, ConceptIdentity, LocalRepresentation?, ConceptRole\*

Attribute Documentation:

======================= ====================== ================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                **Type**               **Documentation**
======================= ====================== ================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
id                      com:NCNameIDType       The id attribute holds an explicit identification of the component. If this identifier is not supplied, then it is assumed to be the same as the identifier of the concept referenced from the concept identity. Because structures require that every component be given a unique identifier, it may be necessary to assign an explicit identifier when more than one component in a structure reference concepts with same identifier. It is important to note that this applies strictly to the identifier of concept and not the URN. Therefore if two concepts with the same identifier from different concept schemes are referenced in the same structure, one of the components will have to provide a unique explicit identifier. The type of this identifier is restricted to the common:NCNameIDType. This is necessary, since component identifiers are used to create XML elements and attributes in data and metadata structure specific schemas and therefore must be compliant with the NCName type in XML Schema (see common:NCNameIDType for further details).
urn                     xs:anyURI              The urn attribute holds a valid SDMX Registry URN (see SDMX Registry Specification for details).
uri                     xs:anyURI              The uri attribute holds a URI that contains a link to a resource with additional information about the object, such as a web page. This uri is not a SDMX message.
position                xs:int                 The position attribute specifies the position of the dimension in the data structure definition. It is optional an the position of the dimension in the key descriptor (DimensionList element) always takes precedence over the value supplied here. This is strictly for informational purposes only.
type (fixed: Dimension) com: DimensionTypeType The type attribute identifies whether then dimension is a measure dimension, the time dimension, or a regular dimension. Although these are all apparent by the element names, this attribute allows for each dimension to be processed independent of its element as well as maintaining the restriction of only one measure and time dimension while still allowing dimension to occur in any order.
======================= ====================== ================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================

Element Documentation:

=================== ====================================== ==============================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**            **Type**                               **Documentation**
=================== ====================================== ==============================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
com:Annotations     com:AnnotationsType                    Annotations is a reusable element the provides for a collection of annotations. It has been made global so that restrictions of types that extend AnnotatableType my reference it.
ConceptIdentity     com: ConceptReferenceType              ConceptIdentity allows for the referencing of a concept in a concept scheme. The component takes its semantic from this concept, and if an id is not specified, it takes its identification as well. If a representation (LocalRepresentation) is not supplied, then the representation of the component is also inherited from the concept. Note that in the case of the component representation being inherited from the concept, the allowable representations for the component still apply. Therefore, if a component references a concept with a core representation that is not allowed for the concept, that representation must be locally overridden. For components which can specify a concept role, it is implied that the concept which is referenced also identifies a role for the component.
LocalRepresentation SimpleDataStructureR epresentationType LocalRepresentation references item schemes that may be used to create the representation of a component. The type of this must be refined such that a concrete item scheme reference is used.
ConceptRole         com: ConceptReferenceType              ConceptRole references concepts which define roles which this dimension serves. If the concept from which the attribute takes its identity also defines a role the concept serves, then the isConceptRole indicator can be set to true on the concept identity rather than repeating the reference here.
=================== ====================================== ==============================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================

**TimeDimensionType: **\ TimeDimensionType describes the structure of a
time dimension. The time dimension takes its semantic from its concept
identity (usually the TIME_PERIOD concept), yet is always has a fixed
identifier (TIME_PERIOD). The time dimension always has a fixed text
format, which specifies that its format is always the in the value set
of the observational time period (see
common:ObservationalTimePeriodType). It is possible that the format may
be a sub-set of the observational time period value set. For example, it
is possible to state that the representation might always be a calendar
year. See the enumerations of the textType attribute in the
LocalRepresentation/TextFormat for more details of the possible
sub-sets. It is also possible to facet this representation with start
and end dates. The purpose of such facts is to restrict the value of the
time dimension to occur within the specified range. If the time
dimension is expected to allow for the standard reporting periods (see
common:ReportingTimePeriodType) to be used, then it is strongly
recommended that the reporting year start day attribute also be included
in the data structure definition. When the reporting year start day
attribute is used, any standard reporting period values will be assumed
to be based on the start day contained in this attribute. If the
reporting year start day attribute is not included and standard
reporting periods are used, these values will be assumed to be based on
a reporting year which begins January 1.

Derivation:

| *com:AnnotableType* (extension) 
|    |image211|\ *IdentifiableType* (restriction) 
|          |image212|\ *ComponentBaseType* (extension) 
|                |image213|\ *ComponentType* (restriction) 
|                      |image214|\ *BaseDimensionBaseType* (extension) 
|                            |image215|\ *BaseDimensionType* (restriction) 
|                                  |image216|\ TimeDimensionType

Attributes:

id?, urn?, uri?, position?, type?

Content:

com:Annotations?, ConceptIdentity, LocalRepresentation

Attribute Documentation:

=========================== ====================== ================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                    **Type**               **Documentation**
=========================== ====================== ================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
id (fixed: TIME_PERIOD)     com:NCNameIDType       The id attribute holds an explicit identification of the component. If this identifier is not supplied, then it is assumed to be the same as the identifier of the concept referenced from the concept identity. Because structures require that every component be given a unique identifier, it may be necessary to assign an explicit identifier when more than one component in a structure reference concepts with same identifier. It is important to note that this applies strictly to the identifier of concept and not the URN. Therefore if two concepts with the same identifier from different concept schemes are referenced in the same structure, one of the components will have to provide a unique explicit identifier. The type of this identifier is restricted to the common:NCNameIDType. This is necessary, since component identifiers are used to create XML elements and attributes in data and metadata structure specific schemas and therefore must be compliant with the NCName type in XML Schema (see common:NCNameIDType for further details).
urn                         xs:anyURI              The urn attribute holds a valid SDMX Registry URN (see SDMX Registry Specification for details).
uri                         xs:anyURI              The uri attribute holds a URI that contains a link to a resource with additional information about the object, such as a web page. This uri is not a SDMX message.
position                    xs:int                 The position attribute specifies the position of the dimension in the data structure definition. It is optional an the position of the dimension in the key descriptor (DimensionList element) always takes precedence over the value supplied here. This is strictly for informational purposes only.
type (fixed: TimeDimension) com: DimensionTypeType The type attribute identifies whether then dimension is a measure dimension, the time dimension, or a regular dimension. Although these are all apparent by the element names, this attribute allows for each dimension to be processed independent of its element as well as maintaining the restriction of only one measure and time dimension while still allowing dimension to occur in any order.
=========================== ====================== ================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================

Element Documentation:

=================== ================================ ==============================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**            **Type**                         **Documentation**
=================== ================================ ==============================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
com:Annotations     com:AnnotationsType              Annotations is a reusable element the provides for a collection of annotations. It has been made global so that restrictions of types that extend AnnotatableType my reference it.
ConceptIdentity     com: ConceptReferenceType        ConceptIdentity allows for the referencing of a concept in a concept scheme. The component takes its semantic from this concept, and if an id is not specified, it takes its identification as well. If a representation (LocalRepresentation) is not supplied, then the representation of the component is also inherited from the concept. Note that in the case of the component representation being inherited from the concept, the allowable representations for the component still apply. Therefore, if a component references a concept with a core representation that is not allowed for the concept, that representation must be locally overridden. For components which can specify a concept role, it is implied that the concept which is referenced also identifies a role for the component.
LocalRepresentation TimeDimensionReprese ntationType LocalRepresentation references item schemes that may be used to create the representation of a component. The type of this must be refined such that a concrete item scheme reference is used.
=================== ================================ ==============================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================

**MeasureDimensionType: **\ MeasureDimensionType defines the structure
of the measure dimension. It is derived from the base dimension
structure, but requires that a coded representation taken from a concept
scheme is given.

Derivation:

| *com:AnnotableType* (extension) 
|    |image217|\ *IdentifiableType* (restriction) 
|          |image218|\ *ComponentBaseType* (extension) 
|                |image219|\ *ComponentType* (restriction) 
|                      |image220|\ *BaseDimensionBaseType* (extension) 
|                            |image221|\ *BaseDimensionType* (restriction) 
|                                  |image222|\ MeasureDimensionType

Attributes:

id?, urn?, uri?, position?, type?

Content:

com:Annotations?, ConceptIdentity, LocalRepresentation, ConceptRole\*

Attribute Documentation:

============================== ====================== ================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                       **Type**               **Documentation**
============================== ====================== ================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
id                             com:NCNameIDType       The id attribute holds an explicit identification of the component. If this identifier is not supplied, then it is assumed to be the same as the identifier of the concept referenced from the concept identity. Because structures require that every component be given a unique identifier, it may be necessary to assign an explicit identifier when more than one component in a structure reference concepts with same identifier. It is important to note that this applies strictly to the identifier of concept and not the URN. Therefore if two concepts with the same identifier from different concept schemes are referenced in the same structure, one of the components will have to provide a unique explicit identifier. The type of this identifier is restricted to the common:NCNameIDType. This is necessary, since component identifiers are used to create XML elements and attributes in data and metadata structure specific schemas and therefore must be compliant with the NCName type in XML Schema (see common:NCNameIDType for further details).
urn                            xs:anyURI              The urn attribute holds a valid SDMX Registry URN (see SDMX Registry Specification for details).
uri                            xs:anyURI              The uri attribute holds a URI that contains a link to a resource with additional information about the object, such as a web page. This uri is not a SDMX message.
position                       xs:int                 The position attribute specifies the position of the dimension in the data structure definition. It is optional an the position of the dimension in the key descriptor (DimensionList element) always takes precedence over the value supplied here. This is strictly for informational purposes only.
type (fixed: MeasureDimension) com: DimensionTypeType The type attribute identifies whether then dimension is a measure dimension, the time dimension, or a regular dimension. Although these are all apparent by the element names, this attribute allows for each dimension to be processed independent of its element as well as maintaining the restriction of only one measure and time dimension while still allowing dimension to occur in any order.
============================== ====================== ================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================

Element Documentation:

=================== =================================== ==============================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**            **Type**                            **Documentation**
=================== =================================== ==============================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
com:Annotations     com:AnnotationsType                 Annotations is a reusable element the provides for a collection of annotations. It has been made global so that restrictions of types that extend AnnotatableType my reference it.
ConceptIdentity     com: ConceptReferenceType           ConceptIdentity allows for the referencing of a concept in a concept scheme. The component takes its semantic from this concept, and if an id is not specified, it takes its identification as well. If a representation (LocalRepresentation) is not supplied, then the representation of the component is also inherited from the concept. Note that in the case of the component representation being inherited from the concept, the allowable representations for the component still apply. Therefore, if a component references a concept with a core representation that is not allowed for the concept, that representation must be locally overridden. For components which can specify a concept role, it is implied that the concept which is referenced also identifies a role for the component.
LocalRepresentation MeasureDimensionRepr esentationType LocalRepresentation references item schemes that may be used to create the representation of a component. The type of this must be refined such that a concrete item scheme reference is used.
ConceptRole         com: ConceptReferenceType           ConceptRole references concepts which define roles which this dimension serves. If the concept from which the attribute takes its identity also defines a role the concept serves, then the isConceptRole indicator can be set to true on the concept identity rather than repeating the reference here.
=================== =================================== ==============================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================

**GroupBaseType: **\ GroupBaseType is an abstract base type that forms
the basis for the GroupType.

Derivation:

| *com:AnnotableType* (extension) 
|    |image223|\ *IdentifiableType* (extension) 
|          |image224|\ *ComponentListType* (restriction) 
|                |image225|\ *GroupBaseType*

Attributes:

id, urn?, uri?

Content:

com:Annotations?

Attribute Documentation:

======== ========== ==================================================================================================================================================================
**Name** **Type**   **Documentation**
======== ========== ==================================================================================================================================================================
id       com:IDType The id is the identifier for the object.
urn      xs:anyURI  The urn attribute holds a valid SDMX Registry URN (see SDMX Registry Specification for details).
uri      xs:anyURI  The uri attribute holds a URI that contains a link to a resource with additional information about the object, such as a web page. This uri is not a SDMX message.
======== ========== ==================================================================================================================================================================

Element Documentation:

=============== =================== ==================================================================================================================================================================================
**Name**        **Type**            **Documentation**
=============== =================== ==================================================================================================================================================================================
com:Annotations com:AnnotationsType Annotations is a reusable element the provides for a collection of annotations. It has been made global so that restrictions of types that extend AnnotatableType my reference it.
=============== =================== ==================================================================================================================================================================================

**GroupType: **\ GroupType describes the structure of a group descriptor
in a data structure definition. A group may consist of a of partial key,
or collection of distinct cube regions or key sets to which attributes
may be attached. The purpose of a group is to specify attributes values
which have the same value based on some common dimensionality. All
groups declared in the data structure must be unique - that is, you may
not have duplicate partial keys. All groups must be given unique
identifiers.

Derivation:

| *com:AnnotableType* (extension) 
|    |image226|\ *IdentifiableType* (extension) 
|          |image227|\ *ComponentListType* (restriction) 
|                |image228|\ *GroupBaseType* (extension) 
|                      |image229|\ GroupType

Attributes:

id, urn?, uri?

Content:

com:Annotations?, (GroupDimension+ \| AttachmentConstraint)

Attribute Documentation:

======== ========== ==================================================================================================================================================================
**Name** **Type**   **Documentation**
======== ========== ==================================================================================================================================================================
id       com:IDType The id is the identifier for the object.
urn      xs:anyURI  The urn attribute holds a valid SDMX Registry URN (see SDMX Registry Specification for details).
uri      xs:anyURI  The uri attribute holds a URI that contains a link to a resource with additional information about the object, such as a web page. This uri is not a SDMX message.
======== ========== ==================================================================================================================================================================

Element Documentation:

==================== ======================================= =============================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**             **Type**                                **Documentation**
==================== ======================================= =============================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
com:Annotations      com:AnnotationsType                     Annotations is a reusable element the provides for a collection of annotations. It has been made global so that restrictions of types that extend AnnotatableType my reference it.
GroupDimension       GroupDimensionType                      GroupDimension is a component which contains only a reference to a dimension in the key descriptor (DimensionList). Although it is conventional to declare dimensions in the same order as they are declared in the ordered key, there is no requirement to do so - the ordering of the values of the key are taken from the order in which the dimensions are declared. Note that the id of a dimension may be inherited from its underlying concept - therefore this reference value may actually be the id of the concept.
AttachmentConstraint com: AttachmentConstraint ReferenceType AttachmentConstraint references an attachment constraint that defines the key sets and/or cube regions that attributes may be attached to. This is an alternative to referencing the dimensions, and allows attributes to be attached to data for given values of dimensions.
==================== ======================================= =============================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================

**GroupDimensionBaseType: **\ GroupDimensionBaseType is an abstract base
type which refines the base ComponentType in order to form the basis for
the GroupDimensionType.

Derivation:

| *com:AnnotableType* (extension) 
|    |image230|\ *IdentifiableType* (restriction) 
|          |image231|\ *ComponentBaseType* (extension) 
|                |image232|\ *ComponentType* (restriction) 
|                      |image233|\ *GroupDimensionBaseType*

Content:

{Empty}

**GroupDimensionType: **\ GroupDimensionType defines a dimension
component with a group key descriptor component list. Although
technically a component, this is essentially a reference to a dimension
defined in the key descriptor. Therefore, the identification, name, and
description, concept identity and representation properties that are
typically available for a component are not allowed here, as they are
all inherited from the referenced dimension.

Derivation:

| *com:AnnotableType* (extension) 
|    |image234|\ *IdentifiableType* (restriction) 
|          |image235|\ *ComponentBaseType* (extension) 
|                |image236|\ *ComponentType* (restriction) 
|                      |image237|\ *GroupDimensionBaseType* (extension) 
|                            |image238|\ GroupDimensionType

Content:

DimensionReference

Element Documentation:

================== ================================= ====================================================================================================================================================================
**Name**           **Type**                          **Documentation**
================== ================================= ====================================================================================================================================================================
DimensionReference com: LocalDimensionRefere nceType DimensionReference provides a reference to a dimension defined in the key descriptor of the data structure definition in which this group key descriptor is defined.
================== ================================= ====================================================================================================================================================================

**MeasureListType: **\ MeasureListType describes the structure of the
measure descriptor for a data structure definition. Only a primary may
be defined.

Derivation:

| *com:AnnotableType* (extension) 
|    |image239|\ *IdentifiableType* (extension) 
|          |image240|\ *ComponentListType* (restriction) 
|                |image241|\ MeasureListType

Attributes:

id?, urn?, uri?

Content:

com:Annotations?, PrimaryMeasure

Attribute Documentation:

============================= ========== ==================================================================================================================================================================
**Name**                      **Type**   **Documentation**
============================= ========== ==================================================================================================================================================================
id (fixed: MeasureDescriptor) com:IDType The id is the identifier for the object.
urn                           xs:anyURI  The urn attribute holds a valid SDMX Registry URN (see SDMX Registry Specification for details).
uri                           xs:anyURI  The uri attribute holds a URI that contains a link to a resource with additional information about the object, such as a web page. This uri is not a SDMX message.
============================= ========== ==================================================================================================================================================================

Element Documentation:

=============== =================== ==================================================================================================================================================================================================================================================================================================================
**Name**        **Type**            **Documentation**
=============== =================== ==================================================================================================================================================================================================================================================================================================================
com:Annotations com:AnnotationsType Annotations is a reusable element the provides for a collection of annotations. It has been made global so that restrictions of types that extend AnnotatableType my reference it.
PrimaryMeasure  PrimaryMeasureType  PrimaryMeasure defines the structure of the primary measure, which is the concept that is the value of the phenomenon to be measured in a data set. Although this may take its semantic from any concept, this is provided a fixed identifier (OBS_VALUE) so that it may be easily distinguished in data messages.
=============== =================== ==================================================================================================================================================================================================================================================================================================================

**PrimaryMeasureType: **\ PrimaryMeasureType describes the structure of
the primary measure. It describes the observation values for all
presentations of the data. The primary measure takes its semantic, and
in some cases it representation, from its concept identity
(conventionally the OBS_VALUE concept). The primary measure can be coded
by referencing a code list from its coded local representation. It can
also specify its text format, which is used as the representation of the
primary measure if a coded representation is not defined. Neither the
coded or uncoded representation are necessary, since the primary measure
may take these from the referenced concept. Note that if the data
structure declares a measure dimension, the representation of this must
be a superset of all possible measure concept representations.

Derivation:

| *com:AnnotableType* (extension) 
|    |image242|\ *IdentifiableType* (restriction) 
|          |image243|\ *ComponentBaseType* (extension) 
|                |image244|\ *ComponentType* (restriction) 
|                      |image245|\ PrimaryMeasureType

Attributes:

id?, urn?, uri?

Content:

com:Annotations?, ConceptIdentity, LocalRepresentation?

Attribute Documentation:

===================== ================ ================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**              **Type**         **Documentation**
===================== ================ ================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
id (fixed: OBS_VALUE) com:NCNameIDType The id attribute holds an explicit identification of the component. If this identifier is not supplied, then it is assumed to be the same as the identifier of the concept referenced from the concept identity. Because structures require that every component be given a unique identifier, it may be necessary to assign an explicit identifier when more than one component in a structure reference concepts with same identifier. It is important to note that this applies strictly to the identifier of concept and not the URN. Therefore if two concepts with the same identifier from different concept schemes are referenced in the same structure, one of the components will have to provide a unique explicit identifier. The type of this identifier is restricted to the common:NCNameIDType. This is necessary, since component identifiers are used to create XML elements and attributes in data and metadata structure specific schemas and therefore must be compliant with the NCName type in XML Schema (see common:NCNameIDType for further details).
urn                   xs:anyURI        The urn attribute holds a valid SDMX Registry URN (see SDMX Registry Specification for details).
uri                   xs:anyURI        The uri attribute holds a URI that contains a link to a resource with additional information about the object, such as a web page. This uri is not a SDMX message.
===================== ================ ================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================

Element Documentation:

=================== ====================================== ==============================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**            **Type**                               **Documentation**
=================== ====================================== ==============================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
com:Annotations     com:AnnotationsType                    Annotations is a reusable element the provides for a collection of annotations. It has been made global so that restrictions of types that extend AnnotatableType my reference it.
ConceptIdentity     com: ConceptReferenceType              ConceptIdentity allows for the referencing of a concept in a concept scheme. The component takes its semantic from this concept, and if an id is not specified, it takes its identification as well. If a representation (LocalRepresentation) is not supplied, then the representation of the component is also inherited from the concept. Note that in the case of the component representation being inherited from the concept, the allowable representations for the component still apply. Therefore, if a component references a concept with a core representation that is not allowed for the concept, that representation must be locally overridden. For components which can specify a concept role, it is implied that the concept which is referenced also identifies a role for the component.
LocalRepresentation SimpleDataStructureR epresentationType LocalRepresentation references item schemes that may be used to create the representation of a component. The type of this must be refined such that a concrete item scheme reference is used.
=================== ====================================== ==============================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================

**DataStructureRepresentationType: **\ DataStructureRepresentationType
is an abstract base type which defines the allowable representations for
any data structure definition component. The enumeration must be
restricted to the proper type for item scheme for a given component.

Derivation:

| *RepresentationType* (restriction) 
|    |image246|\ *DataStructureRepresentationType*

Content:

(TextFormat \| (Enumeration, EnumerationFormat?))

Element Documentation:

================= =================================== ================================================================================================================
**Name**          **Type**                            **Documentation**
================= =================================== ================================================================================================================
TextFormat        SimpleComponentTextF ormatType      TextFormat describes an uncoded textual format.
Enumeration       *com: ItemSchemeReferenceB aseType* Enumeration references an item scheme that enumerates the allowable values for this representation.
EnumerationFormat CodededTextFormatTyp e              EnumerationFormat describes the facets of the item scheme enumeration. This is for the most part, informational.
================= =================================== ================================================================================================================

**SimpleDataStructureRepresentationType: **\ SimpleDataStructureRepresentationType
defines the representation for any non-measure and non-time dimension
data structure definition component.

Derivation:

| *RepresentationType* (restriction) 
|    |image247|\ *DataStructureRepresentationType* (restriction) 
|          |image248|\ SimpleDataStructureRepresentationType

Content:

(TextFormat \| (Enumeration, EnumerationFormat?))

Element Documentation:

================= ============================== ================================================================================================================
**Name**          **Type**                       **Documentation**
================= ============================== ================================================================================================================
TextFormat        SimpleComponentTextF ormatType TextFormat describes an uncoded textual format.
Enumeration       com: CodelistReferenceTyp e    Enumeration references an item scheme that enumerates the allowable values for this representation.
EnumerationFormat CodededTextFormatTyp e         EnumerationFormat describes the facets of the item scheme enumeration. This is for the most part, informational.
================= ============================== ================================================================================================================

**MeasureDimensionRepresentationType: **\ BaseDimensionRepresentationType
is an abstract base which defines the representation for a measure
dimension.

Derivation:

| *RepresentationType* (restriction) 
|    |image249|\ *DataStructureRepresentationType* (restriction) 
|          |image250|\ MeasureDimensionRepresentationType

Content:

Enumeration

Element Documentation:

=========== ================================ ===================================================================================================
**Name**    **Type**                         **Documentation**
=========== ================================ ===================================================================================================
Enumeration com: ConceptSchemeReferen ceType Enumeration references an item scheme that enumerates the allowable values for this representation.
=========== ================================ ===================================================================================================

**TimeDimensionRepresentationType: **\ TimeDimensionRepresentationType
defines the representation for the time dimension. Enumerated values are
not allowed.

Derivation:

| *RepresentationType* (restriction) 
|    |image251|\ *DataStructureRepresentationType* (restriction) 
|          |image252|\ SimpleDataStructureRepresentationType
  (restriction) 
|                |image253|\ TimeDimensionRepresentationType

Content:

TextFormat

Element Documentation:

========== ================== ===============================================
**Name**   **Type**           **Documentation**
========== ================== ===============================================
TextFormat TimeTextFormatType TextFormat describes an uncoded textual format.
========== ================== ===============================================

**DataflowType: **\ DataflowType describes the structure of a data flow.
A data flow is defined as the structure of data that will provided for
different reference periods. If this type is not referenced externally,
then a reference to a key family definition must be provided.

Derivation:

| *com:AnnotableType* (extension) 
|    |image254|\ *IdentifiableType* (extension) 
|          |image255|\ *NameableType* (extension) 
|                |image256|\ *VersionableType* (restriction) 
|                      |image257|\ *MaintainableBaseType* (extension) 
|                            |image258|\ *MaintainableType* (extension) 
|                                  |image259|\ *StructureUsageType* (restriction) 
|                                        |image260|\ DataflowType

Attributes:

id, urn?, uri?, version?, validFrom?, validTo?, agencyID, isFinal?,
isExternalReference?, serviceURL?, structureURL?

Content:

com:Annotations?, com:Name+, com:Description*, Structure?

Attribute Documentation:

==================================== ======================= ==========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                             **Type**                **Documentation**
==================================== ======================= ==========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
id                                   com:IDType              The id is the identifier for the object.
urn                                  xs:anyURI               The urn attribute holds a valid SDMX Registry URN (see SDMX Registry Specification for details).
uri                                  xs:anyURI               The uri attribute holds a URI that contains a link to a resource with additional information about the object, such as a web page. This uri is not a SDMX message.
version (default: 1.0)               com:VersionType         This version attribute holds a version number in the format of #[.#]+ (see common:VersionType definition for details). If not supplied, the version number is defaulted to 1.0.
validFrom                            xs:dateTime             The validFrom attribute provides the inclusive start date for providing supplemental validity information about the version.
validTo                              xs:dateTime             The validTo attribute provides the inclusive end date for providing supplemental validity information about the version.
agencyID                             com: NestedNCNameIDType The agencyID must be provided, and identifies the maintenance agency of the object.
isFinal (default: false)             xs:boolean              The isFinal attribute indicates whether the object is unchangeable without versioning. If the value is true, the object must be versioned upon change. If the final attribute is not supplied, then the object is assumed not to be final. Note that all production objects must be final.
isExternalReference (default: false) xs:boolean              The isExternalReference attribute, if true, indicates that the actual object is not defined the corresponding element, rather its full details are defined elsewhere - indicated by either the registryURL, the repositoryURL, or the structureURL. The purpose of this is so that each structure message does not have to redefine object that are already defined elsewhere. If the isExternalReference attribute is not set, then it is assumed to be false, and the object should contain the full definition of its contents. If more than one of the registryURL, the repositoryURL, and the structureURL are supplied, then the application processing the object can choose the method it finds best suited to retrieve the details of the object.
serviceURL                           xs:anyURI               The serviceURL attribute indicates the URL of an SDMX SOAP web service from which the details of the object can be retrieved. Note that this can be a registry or and SDMX structural metadata repository, as they both implement that same web service interface.
structureURL                         xs:anyURI               The structureURL attribute indicates the URL of a SDMX-ML structure message (in the same version as the source document) in which the externally referenced object is contained. Note that this may be a URL of an SDMX RESTful web service which will return the referenced object.
==================================== ======================= ==========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================

Element Documentation:

=============== ================================ ==================================================================================================================================================================================
**Name**        **Type**                         **Documentation**
=============== ================================ ==================================================================================================================================================================================
com:Annotations com:AnnotationsType              Annotations is a reusable element the provides for a collection of annotations. It has been made global so that restrictions of types that extend AnnotatableType my reference it.
com:Name        com:TextType                     Name provides for a human-readable name for the object. This may be provided in multiple, parallel language-equivalent forms.
com:Description com:TextType                     Description provides for a longer human-readable description of the object. This may be provided in multiple, parallel language-equivalent forms.
Structure       com: DataStructureReferen ceType Structure provides a reference to the data structure definition which defines the structure of all data for this flow.
=============== ================================ ==================================================================================================================================================================================

**HierarchicalCodelistBaseType: **\ HierarchicalCodelistBaseType is an
abstract base class that is the basis for the HierarchicalCodelistType.
It requires that a name be supplied.

Derivation:

| *com:AnnotableType* (extension) 
|    |image261|\ *IdentifiableType* (extension) 
|          |image262|\ *NameableType* (extension) 
|                |image263|\ *VersionableType* (restriction) 
|                      |image264|\ *MaintainableBaseType* (extension) 
|                            |image265|\ *MaintainableType* (restriction) 
|                                  |image266|\ *HierarchicalCodelistBaseType*

Attributes:

id, urn?, uri?, version?, validFrom?, validTo?, agencyID, isFinal?,
isExternalReference?, serviceURL?, structureURL?

Content:

com:Annotations?, com:Name+, com:Description\*

Attribute Documentation:

==================================== ======================= ==========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                             **Type**                **Documentation**
==================================== ======================= ==========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
id                                   com:IDType              The id is the identifier for the object.
urn                                  xs:anyURI               The urn attribute holds a valid SDMX Registry URN (see SDMX Registry Specification for details).
uri                                  xs:anyURI               The uri attribute holds a URI that contains a link to a resource with additional information about the object, such as a web page. This uri is not a SDMX message.
version (default: 1.0)               com:VersionType         This version attribute holds a version number in the format of #[.#]+ (see common:VersionType definition for details). If not supplied, the version number is defaulted to 1.0.
validFrom                            xs:dateTime             The validFrom attribute provides the inclusive start date for providing supplemental validity information about the version.
validTo                              xs:dateTime             The validTo attribute provides the inclusive end date for providing supplemental validity information about the version.
agencyID                             com: NestedNCNameIDType The agencyID must be provided, and identifies the maintenance agency of the object.
isFinal (default: false)             xs:boolean              The isFinal attribute indicates whether the object is unchangeable without versioning. If the value is true, the object must be versioned upon change. If the final attribute is not supplied, then the object is assumed not to be final. Note that all production objects must be final.
isExternalReference (default: false) xs:boolean              The isExternalReference attribute, if true, indicates that the actual object is not defined the corresponding element, rather its full details are defined elsewhere - indicated by either the registryURL, the repositoryURL, or the structureURL. The purpose of this is so that each structure message does not have to redefine object that are already defined elsewhere. If the isExternalReference attribute is not set, then it is assumed to be false, and the object should contain the full definition of its contents. If more than one of the registryURL, the repositoryURL, and the structureURL are supplied, then the application processing the object can choose the method it finds best suited to retrieve the details of the object.
serviceURL                           xs:anyURI               The serviceURL attribute indicates the URL of an SDMX SOAP web service from which the details of the object can be retrieved. Note that this can be a registry or and SDMX structural metadata repository, as they both implement that same web service interface.
structureURL                         xs:anyURI               The structureURL attribute indicates the URL of a SDMX-ML structure message (in the same version as the source document) in which the externally referenced object is contained. Note that this may be a URL of an SDMX RESTful web service which will return the referenced object.
==================================== ======================= ==========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================

Element Documentation:

=============== =================== ==================================================================================================================================================================================
**Name**        **Type**            **Documentation**
=============== =================== ==================================================================================================================================================================================
com:Annotations com:AnnotationsType Annotations is a reusable element the provides for a collection of annotations. It has been made global so that restrictions of types that extend AnnotatableType my reference it.
com:Name        com:TextType        Name provides for a human-readable name for the object. This may be provided in multiple, parallel language-equivalent forms.
com:Description com:TextType        Description provides for a longer human-readable description of the object. This may be provided in multiple, parallel language-equivalent forms.
=============== =================== ==================================================================================================================================================================================

**HierarchicalCodelistType: **\ HierarchicalCodelistType describes the
structure of a hierarchical codelist. A hierarchical code list is
defined as an organised collection of codes that may participate in many
parent/child relationships with other codes in the list, as defined by
one or more hierarchy of the list.

Derivation:

| *com:AnnotableType* (extension) 
|    |image267|\ *IdentifiableType* (extension) 
|          |image268|\ *NameableType* (extension) 
|                |image269|\ *VersionableType* (restriction) 
|                      |image270|\ *MaintainableBaseType* (extension) 
|                            |image271|\ *MaintainableType* (restriction) 
|                                  |image272|\ *HierarchicalCodelistBaseType* (extension) 
|                                        |image273|\ HierarchicalCodelistType

Attributes:

id, urn?, uri?, version?, validFrom?, validTo?, agencyID, isFinal?,
isExternalReference?, serviceURL?, structureURL?

Content:

com:Annotations?, com:Name+, com:Description*, IncludedCodelist*,
Hierarchy\*

Attribute Documentation:

==================================== ======================= ==========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                             **Type**                **Documentation**
==================================== ======================= ==========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
id                                   com:IDType              The id is the identifier for the object.
urn                                  xs:anyURI               The urn attribute holds a valid SDMX Registry URN (see SDMX Registry Specification for details).
uri                                  xs:anyURI               The uri attribute holds a URI that contains a link to a resource with additional information about the object, such as a web page. This uri is not a SDMX message.
version (default: 1.0)               com:VersionType         This version attribute holds a version number in the format of #[.#]+ (see common:VersionType definition for details). If not supplied, the version number is defaulted to 1.0.
validFrom                            xs:dateTime             The validFrom attribute provides the inclusive start date for providing supplemental validity information about the version.
validTo                              xs:dateTime             The validTo attribute provides the inclusive end date for providing supplemental validity information about the version.
agencyID                             com: NestedNCNameIDType The agencyID must be provided, and identifies the maintenance agency of the object.
isFinal (default: false)             xs:boolean              The isFinal attribute indicates whether the object is unchangeable without versioning. If the value is true, the object must be versioned upon change. If the final attribute is not supplied, then the object is assumed not to be final. Note that all production objects must be final.
isExternalReference (default: false) xs:boolean              The isExternalReference attribute, if true, indicates that the actual object is not defined the corresponding element, rather its full details are defined elsewhere - indicated by either the registryURL, the repositoryURL, or the structureURL. The purpose of this is so that each structure message does not have to redefine object that are already defined elsewhere. If the isExternalReference attribute is not set, then it is assumed to be false, and the object should contain the full definition of its contents. If more than one of the registryURL, the repositoryURL, and the structureURL are supplied, then the application processing the object can choose the method it finds best suited to retrieve the details of the object.
serviceURL                           xs:anyURI               The serviceURL attribute indicates the URL of an SDMX SOAP web service from which the details of the object can be retrieved. Note that this can be a registry or and SDMX structural metadata repository, as they both implement that same web service interface.
structureURL                         xs:anyURI               The structureURL attribute indicates the URL of a SDMX-ML structure message (in the same version as the source document) in which the externally referenced object is contained. Note that this may be a URL of an SDMX RESTful web service which will return the referenced object.
==================================== ======================= ==========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================

Element Documentation:

================ ============================== ==========================================================================================================================================================================================================================================================================================================================================
**Name**         **Type**                       **Documentation**
================ ============================== ==========================================================================================================================================================================================================================================================================================================================================
com:Annotations  com:AnnotationsType            Annotations is a reusable element the provides for a collection of annotations. It has been made global so that restrictions of types that extend AnnotatableType my reference it.
com:Name         com:TextType                   Name provides for a human-readable name for the object. This may be provided in multiple, parallel language-equivalent forms.
com:Description  com:TextType                   Description provides for a longer human-readable description of the object. This may be provided in multiple, parallel language-equivalent forms.
IncludedCodelist IncludedCodelistRefe renceType IndludedCodelist provides a collection of references to the code lists whose codes are arranged in this hierarchical code list.
Hierarchy        HierarchyType                  Hierarchy describes a classification structure arranged in levels of detail from the broadest to the most detailed level. These levels can be formal or informal, and are not necessary to describe. If the hierarchy does contain levels, then each hierarchical code is assumed to exist in the level where the depths of nesting match.
================ ============================== ==========================================================================================================================================================================================================================================================================================================================================

**HierarchyBaseType: **\ HierarchyBaseType is an abstract base type that
serves as the basis for the HierarchyType. It requires a name and id be
provided.

Derivation:

| *com:AnnotableType* (extension) 
|    |image274|\ *IdentifiableType* (extension) 
|          |image275|\ *NameableType* (restriction) 
|                |image276|\ *HierarchyBaseType*

Attributes:

id, urn?, uri?

Content:

com:Annotations?, com:Name+, com:Description\*

Attribute Documentation:

======== ========== ==================================================================================================================================================================
**Name** **Type**   **Documentation**
======== ========== ==================================================================================================================================================================
id       com:IDType The id is the identifier for the object.
urn      xs:anyURI  The urn attribute holds a valid SDMX Registry URN (see SDMX Registry Specification for details).
uri      xs:anyURI  The uri attribute holds a URI that contains a link to a resource with additional information about the object, such as a web page. This uri is not a SDMX message.
======== ========== ==================================================================================================================================================================

Element Documentation:

=============== =================== ==================================================================================================================================================================================
**Name**        **Type**            **Documentation**
=============== =================== ==================================================================================================================================================================================
com:Annotations com:AnnotationsType Annotations is a reusable element the provides for a collection of annotations. It has been made global so that restrictions of types that extend AnnotatableType my reference it.
com:Name        com:TextType        Name provides for a human-readable name for the object. This may be provided in multiple, parallel language-equivalent forms.
com:Description com:TextType        Description provides for a longer human-readable description of the object. This may be provided in multiple, parallel language-equivalent forms.
=============== =================== ==================================================================================================================================================================================

**HierarchyType: **\ The Hierarchy is an abstract type that provides for
a classification structure of referenced codes arranged in levels of
detail from the broadest to the most detailed level. The levels in which
the code exist can be formal or informal.

Derivation:

| *com:AnnotableType* (extension) 
|    |image277|\ *IdentifiableType* (extension) 
|          |image278|\ *NameableType* (restriction) 
|                |image279|\ *HierarchyBaseType* (extension) 
|                      |image280|\ HierarchyType

Attributes:

id, urn?, uri?, leveled?

Content:

com:Annotations?, com:Name+, com:Description*, HierarchicalCode+, Level?

Attribute Documentation:

======================== ========== ==================================================================================================================================================================
**Name**                 **Type**   **Documentation**
======================== ========== ==================================================================================================================================================================
id                       com:IDType The id is the identifier for the object.
urn                      xs:anyURI  The urn attribute holds a valid SDMX Registry URN (see SDMX Registry Specification for details).
uri                      xs:anyURI  The uri attribute holds a URI that contains a link to a resource with additional information about the object, such as a web page. This uri is not a SDMX message.
leveled (default: false) xs:boolean The leveled attribute indicates that the hierarchy has formal levels. In this case, every code should have a level associated with it.
======================== ========== ==================================================================================================================================================================

Element Documentation:

================ ==================== =========================================================================================================================================================================================================================================================================================================================================================================================
**Name**         **Type**             **Documentation**
================ ==================== =========================================================================================================================================================================================================================================================================================================================================================================================
com:Annotations  com:AnnotationsType  Annotations is a reusable element the provides for a collection of annotations. It has been made global so that restrictions of types that extend AnnotatableType my reference it.
com:Name         com:TextType         Name provides for a human-readable name for the object. This may be provided in multiple, parallel language-equivalent forms.
com:Description  com:TextType         Description provides for a longer human-readable description of the object. This may be provided in multiple, parallel language-equivalent forms.
HierarchicalCode HierarchicalCodeType HierarchicalCode is used to assemble the codes from the codelist(s) referenced into a hierarchy.
Level            LevelType            In a formally leveled hierarchy, Level describes a group of codes which are characterised by homogeneous coding, and where the parent of each code in the group is at the same higher level of the hierarchy. In a value based hierarchy Level describes information about the codes at the specified nesting level. This structure is recursive to indicate the hierarchy of the levels.
================ ==================== =========================================================================================================================================================================================================================================================================================================================================================================================

**HierarchicalCodeBaseType: **\ HierarchicalCodeBaseType is an abstract
base type the creates the basis for the HierarchicalCodeType. It removes
the urn and uri.

Derivation:

| *com:AnnotableType* (extension) 
|    |image281|\ *IdentifiableType* (restriction) 
|          |image282|\ *HierarchicalCodeBaseType*

Attributes:

id, urn?, uri?

Content:

com:Annotations?

Attribute Documentation:

======== ========== ==================================================================================================================================================================================================================================================
**Name** **Type**   **Documentation**
======== ========== ==================================================================================================================================================================================================================================================
id       com:IDType The id attribute allows for an id to be assigned to the use of the particular code at that specific point in the hierarchy. This value is unique within the hierarchy being created, and is used to map the hierarchy against external structures.
urn      xs:anyURI  The urn attribute holds a valid SDMX Registry URN (see SDMX Registry Specification for details).
uri      xs:anyURI  The uri attribute holds a URI that contains a link to a resource with additional information about the object, such as a web page. This uri is not a SDMX message.
======== ========== ==================================================================================================================================================================================================================================================

Element Documentation:

=============== =================== ==================================================================================================================================================================================
**Name**        **Type**            **Documentation**
=============== =================== ==================================================================================================================================================================================
com:Annotations com:AnnotationsType Annotations is a reusable element the provides for a collection of annotations. It has been made global so that restrictions of types that extend AnnotatableType my reference it.
=============== =================== ==================================================================================================================================================================================

**HierarchicalCodeType: **\ HierarchicalCodeType describes the structure
of a hierarchical code. A hierarchical code provides for a reference to
a code that is referenced within the hierarchical code list via either a
complete reference to a code through either a URN or full set of
reference fields, or a local reference which utilizes the included
codelist reference alias and the identification of a code from the list.
Codes are arranged in a hierarchy by this reference. Note that it is
possible to reference a single code such that it has multiple parents
within the hierarchy. Further, the hierarchy may or may not be a leveled
one.

Derivation:

| *com:AnnotableType* (extension) 
|    |image283|\ *IdentifiableType* (restriction) 
|          |image284|\ *HierarchicalCodeBaseType* (extension) 
|                |image285|\ HierarchicalCodeType

Attributes:

id, urn?, uri?, version?, validFrom?, validTo?

Content:

com:Annotations?, (Code \| (CodelistAliasRef, CodeID)),
HierarchicalCode*, Level?

Attribute Documentation:

========= =============== ==========================================================================================================================================================================================================================================================================================
**Name**  **Type**        **Documentation**
========= =============== ==========================================================================================================================================================================================================================================================================================
id        com:IDType      The id attribute allows for an id to be assigned to the use of the particular code at that specific point in the hierarchy. This value is unique within the hierarchy being created, and is used to map the hierarchy against external structures.
urn       xs:anyURI       The urn attribute holds a valid SDMX Registry URN (see SDMX Registry Specification for details).
uri       xs:anyURI       The uri attribute holds a URI that contains a link to a resource with additional information about the object, such as a web page. This uri is not a SDMX message.
version   com:VersionType The version attriubte contains a version number for the hierarchical code. A hierarchical code is not formally versionable, therefore each code must have a unique identifier. The version supplied here is for informational purposes only and is not used to uniquely identity the code.
validFrom xs:dateTime     The validFrom attriubte indicates the point in time in which the hiearchical code became effective. This can be used to track the historicity of codes changing over time.
validTo   xs:dateTime     The validTo attriubte indicates the point in time in which the hiearchical code became no longer effective. This can be used to track the historicity of codes changing over time.
========= =============== ==========================================================================================================================================================================================================================================================================================

Element Documentation:

================ ============================= ============================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**         **Type**                      **Documentation**
================ ============================= ============================================================================================================================================================================================================================================================================================================================================================================================================================================
com:Annotations  com:AnnotationsType           Annotations is a reusable element the provides for a collection of annotations. It has been made global so that restrictions of types that extend AnnotatableType my reference it.
Code             com: CodeReferenceType        Code provides a complete, explicit reference to a code through either its URN, or a complete reference to the codelist and code.
CodelistAliasRef com:IDType                    CodelistAliasRef references an alias assigned in a IncludedCodelistReference element in the containing hierarchical codelist. This is used in conjunction with the CodeID element to reference a code from one of the included codelists.
CodeID           com: LocalCodeReferenceTy pe  CodeID references the id of a code from the codelist that is referenced through the CodelistAliaRef element.
HierarchicalCode HierarchicalCodeType          HierarchicalCode is used to nest referenced codes into a value based hierarchy.
Level            com: LocalLevelReferenceT ype Level references a formal level defined within the hierarchy which defines this hierarchical code. This is only necessary if the nesting depth of the hierarchical code does not correspond to the nesting depth of the level to which it belongs (i.e. the hieararchical code is to skip down a level). Otherwise, the code is assumed to exist at the level in which the nesting depth of the level matches the nesting depth of the code.
================ ============================= ============================================================================================================================================================================================================================================================================================================================================================================================================================================

**LevelBaseType: **\ LevelBaseType is an abstract base type that makes
up the basis for the LevelType. It requires a name and id.

Derivation:

| *com:AnnotableType* (extension) 
|    |image286|\ *IdentifiableType* (extension) 
|          |image287|\ *NameableType* (restriction) 
|                |image288|\ *LevelBaseType*

Attributes:

id, urn?, uri?

Content:

com:Annotations?, com:Name+, com:Description\*

Attribute Documentation:

======== ========== ==================================================================================================================================================================
**Name** **Type**   **Documentation**
======== ========== ==================================================================================================================================================================
id       com:IDType The id is the identifier for the object.
urn      xs:anyURI  The urn attribute holds a valid SDMX Registry URN (see SDMX Registry Specification for details).
uri      xs:anyURI  The uri attribute holds a URI that contains a link to a resource with additional information about the object, such as a web page. This uri is not a SDMX message.
======== ========== ==================================================================================================================================================================

Element Documentation:

=============== =================== ==================================================================================================================================================================================
**Name**        **Type**            **Documentation**
=============== =================== ==================================================================================================================================================================================
com:Annotations com:AnnotationsType Annotations is a reusable element the provides for a collection of annotations. It has been made global so that restrictions of types that extend AnnotatableType my reference it.
com:Name        com:TextType        Name provides for a human-readable name for the object. This may be provided in multiple, parallel language-equivalent forms.
com:Description com:TextType        Description provides for a longer human-readable description of the object. This may be provided in multiple, parallel language-equivalent forms.
=============== =================== ==================================================================================================================================================================================

**LevelType: **\ LevelType describes a level in a hierarchical codelist.
Where level is defined as a group where codes can be characterised by
homogeneous coding, and where the parent of each code in the group is at
the same higher level of the hierarchy.

Derivation:

| *com:AnnotableType* (extension) 
|    |image289|\ *IdentifiableType* (extension) 
|          |image290|\ *NameableType* (restriction) 
|                |image291|\ *LevelBaseType* (extension) 
|                      |image292|\ LevelType

Attributes:

id, urn?, uri?

Content:

com:Annotations?, com:Name+, com:Description*, CodingFormat?, Level?

Attribute Documentation:

======== ========== ==================================================================================================================================================================
**Name** **Type**   **Documentation**
======== ========== ==================================================================================================================================================================
id       com:IDType The id is the identifier for the object.
urn      xs:anyURI  The urn attribute holds a valid SDMX Registry URN (see SDMX Registry Specification for details).
uri      xs:anyURI  The uri attribute holds a URI that contains a link to a resource with additional information about the object, such as a web page. This uri is not a SDMX message.
======== ========== ==================================================================================================================================================================

Element Documentation:

=============== ==================== ==================================================================================================================================================================================
**Name**        **Type**             **Documentation**
=============== ==================== ==================================================================================================================================================================================
com:Annotations com:AnnotationsType  Annotations is a reusable element the provides for a collection of annotations. It has been made global so that restrictions of types that extend AnnotatableType my reference it.
com:Name        com:TextType         Name provides for a human-readable name for the object. This may be provided in multiple, parallel language-equivalent forms.
com:Description com:TextType         Description provides for a longer human-readable description of the object. This may be provided in multiple, parallel language-equivalent forms.
CodingFormat    CodingTextFormatType CodingFormat specifies the text formatting of the codes in this level. This includes facets such as the expected characters and the length of the codes.
Level           LevelType            Level describes the next level down in the hierarchy.
=============== ==================== ==================================================================================================================================================================================

**IncludedCodelistReferenceType: **\ IncludedCodelistReferenceType
provides the structure for a referencing a codelist and optionally
providing a local alias identification for this reference.

Derivation:

| *com:ReferenceType* (restriction) 
|    |image293|\ *com:MaintainableReferenceBaseType* (restriction) 
|          |image294|\ *com:ItemSchemeReferenceBaseType* (restriction) 
|                |image295|\ com:CodelistReferenceType (extension) 
|                      |image296|\ IncludedCodelistReferenceType

Attributes:

alias?

Content:

( (Ref, URN?) \| URN)

Attribute Documentation:

======== ========== ==============================================================================================================================================================================================================================================================================================================================================
**Name** **Type**   **Documentation**
======== ========== ==============================================================================================================================================================================================================================================================================================================================================
alias    com:IDType The alias attribute is used to carry the identifier for the referenced codelist, so that codes from that list can be easily referenced by the hierarchical codes contained in the parent hierarchy, without having to repeat the reference to the codelist itself. The alias attribute must be unique within the parent hierarchical codelist.
======== ========== ==============================================================================================================================================================================================================================================================================================================================================

Element Documentation:

======== =================== =============================================================================================================================================================================================================
**Name** **Type**            **Documentation**
======== =================== =============================================================================================================================================================================================================
Ref      com:CodelistRefType Ref is used to provide a complete set of reference fields. Derived reference types will restrict the RefType so that the content of the Ref element requires exactly what is needed for a complete reference.
URN      xs:anyURI           URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
URN      xs:anyURI           URN is used to hold the URN of the referenced object. This must be the same URN that would be constructed from the individual fields in the Ref element.
======== =================== =============================================================================================================================================================================================================

**CodingTextFormatType: **

Derivation:

| TextFormatType (restriction) 
|    |image297|\ BasicComponentTextFormatType (restriction) 
|          |image298|\ SimpleComponentTextFormatType (restriction) 
|                |image299|\ CodingTextFormatType

Attributes:

textType?, isSequence?, interval?, startValue?, endValue?, minLength?,
maxLength?, minValue?, maxValue?, pattern?

Content:

{Empty}

Attribute Documentation:

========== ================== =====================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**   **Type**           **Documentation**
========== ================== =====================================================================================================================================================================================================================================================================================================================================================================================================================
textType   SimpleCodeDataType The textType attribute provides a description of the datatype. If it is not specified, any valid characters may be included in the text field (it corresponds to the xs:string datatype of W3C XML Schema) within the constraints of the facets.
isSequence xs:boolean         The isSequence attribute indicates whether the values are intended to be ordered, and it may work in combination with the interval, startValue, and endValue attributes or the timeInterval, startTime, and endTime, attributes. If this attribute holds a value of true, a start value or time and a numeric or time interval must supplied. If an end value is not given, then the sequence continues indefinitely.
interval   xs:integer         The interval attribute specifies the permitted interval (increment) in a sequence. In order for this to be used, the isSequence attribute must have a value of true.
startValue xs:positiveInteger The startValue attribute is used in conjunction with the isSequence and interval attributes (which must be set in order to use this attribute). This attribute is used for a numeric sequence, and indicates the starting point of the sequence. This value is mandatory for a numeric sequence to be expressed.
endValue   xs:positiveInteger The endValue attribute is used in conjunction with the isSequence and interval attributes (which must be set in order to use this attribute). This attribute is used for a numeric sequence, and indicates that ending point (if any) of the sequence.
minLength  xs:positiveInteger The minLength attribute specifies the minimum and length of the value in characters.
maxLength  xs:positiveInteger The maxLength attribute specifies the maximum length of the value in characters.
minValue   xs:positiveInteger The minValue attribute is used for inclusive and exclusive ranges, indicating what the lower bound of the range is. If this is used with an inclusive range, a valid value will be greater than or equal to the value specified here. If the inclusive and exclusive data type is not specified (e.g. this facet is used with an integer data type), the value is assumed to be inclusive.
maxValue   xs:positiveInteger The maxValue attribute is used for inclusive and exclusive ranges, indicating what the upper bound of the range is. If this is used with an inclusive range, a valid value will be less than or equal to the value specified here. If the inclusive and exclusive data type is not specified (e.g. this facet is used with an integer data type), the value is assumed to be inclusive.
pattern    xs:string          The pattern attribute holds any regular expression permitted in the similar facet in W3C XML Schema.
========== ================== =====================================================================================================================================================================================================================================================================================================================================================================================================================

**MetadataflowType: **\ MetadataflowType describes the structure of a
metadata flow. A dataflow is defined as the structure of reference
metadata that will be provided for different reference periods. If this
type is not referenced externally, then a reference to a metadata
structure definition must be provided

Derivation:

| *com:AnnotableType* (extension) 
|    |image300|\ *IdentifiableType* (extension) 
|          |image301|\ *NameableType* (extension) 
|                |image302|\ *VersionableType* (restriction) 
|                      |image303|\ *MaintainableBaseType* (extension) 
|                            |image304|\ *MaintainableType* (extension) 
|                                  |image305|\ *StructureUsageType* (restriction) 
|                                        |image306|\ MetadataflowType

Attributes:

id, urn?, uri?, version?, validFrom?, validTo?, agencyID, isFinal?,
isExternalReference?, serviceURL?, structureURL?

Content:

com:Annotations?, com:Name+, com:Description*, Structure?

Attribute Documentation:

==================================== ======================= ==========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                             **Type**                **Documentation**
==================================== ======================= ==========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
id                                   com:IDType              The id is the identifier for the object.
urn                                  xs:anyURI               The urn attribute holds a valid SDMX Registry URN (see SDMX Registry Specification for details).
uri                                  xs:anyURI               The uri attribute holds a URI that contains a link to a resource with additional information about the object, such as a web page. This uri is not a SDMX message.
version (default: 1.0)               com:VersionType         This version attribute holds a version number in the format of #[.#]+ (see common:VersionType definition for details). If not supplied, the version number is defaulted to 1.0.
validFrom                            xs:dateTime             The validFrom attribute provides the inclusive start date for providing supplemental validity information about the version.
validTo                              xs:dateTime             The validTo attribute provides the inclusive end date for providing supplemental validity information about the version.
agencyID                             com: NestedNCNameIDType The agencyID must be provided, and identifies the maintenance agency of the object.
isFinal (default: false)             xs:boolean              The isFinal attribute indicates whether the object is unchangeable without versioning. If the value is true, the object must be versioned upon change. If the final attribute is not supplied, then the object is assumed not to be final. Note that all production objects must be final.
isExternalReference (default: false) xs:boolean              The isExternalReference attribute, if true, indicates that the actual object is not defined the corresponding element, rather its full details are defined elsewhere - indicated by either the registryURL, the repositoryURL, or the structureURL. The purpose of this is so that each structure message does not have to redefine object that are already defined elsewhere. If the isExternalReference attribute is not set, then it is assumed to be false, and the object should contain the full definition of its contents. If more than one of the registryURL, the repositoryURL, and the structureURL are supplied, then the application processing the object can choose the method it finds best suited to retrieve the details of the object.
serviceURL                           xs:anyURI               The serviceURL attribute indicates the URL of an SDMX SOAP web service from which the details of the object can be retrieved. Note that this can be a registry or and SDMX structural metadata repository, as they both implement that same web service interface.
structureURL                         xs:anyURI               The structureURL attribute indicates the URL of a SDMX-ML structure message (in the same version as the source document) in which the externally referenced object is contained. Note that this may be a URL of an SDMX RESTful web service which will return the referenced object.
==================================== ======================= ==========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================

Element Documentation:

=============== ==================================== ==================================================================================================================================================================================
**Name**        **Type**                             **Documentation**
=============== ==================================== ==================================================================================================================================================================================
com:Annotations com:AnnotationsType                  Annotations is a reusable element the provides for a collection of annotations. It has been made global so that restrictions of types that extend AnnotatableType my reference it.
com:Name        com:TextType                         Name provides for a human-readable name for the object. This may be provided in multiple, parallel language-equivalent forms.
com:Description com:TextType                         Description provides for a longer human-readable description of the object. This may be provided in multiple, parallel language-equivalent forms.
Structure       com: MetadataStructureRef erenceType Structure provides a reference to the metadata structure definition describing the structure of all reference metadata for this flow.
=============== ==================================== ==================================================================================================================================================================================

**MetadataStructureType: **\ MetadataStructureType is used to describe a
metadata structure definition, which is defined as a collection of
metadata concepts, their structure and usage when used to collect or
disseminate reference metadata.

Derivation:

| *com:AnnotableType* (extension) 
|    |image307|\ *IdentifiableType* (extension) 
|          |image308|\ *NameableType* (extension) 
|                |image309|\ *VersionableType* (restriction) 
|                      |image310|\ *MaintainableBaseType* (extension) 
|                            |image311|\ *MaintainableType* (extension) 
|                                  |image312|\ *StructureType* (restriction) 
|                                        |image313|\ MetadataStructureType

Attributes:

id, urn?, uri?, version?, validFrom?, validTo?, agencyID, isFinal?,
isExternalReference?, serviceURL?, structureURL?

Content:

com:Annotations?, com:Name+, com:Description*,
MetadataStructureComponents?

Attribute Documentation:

==================================== ======================= ==========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                             **Type**                **Documentation**
==================================== ======================= ==========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
id                                   com:IDType              The id is the identifier for the object.
urn                                  xs:anyURI               The urn attribute holds a valid SDMX Registry URN (see SDMX Registry Specification for details).
uri                                  xs:anyURI               The uri attribute holds a URI that contains a link to a resource with additional information about the object, such as a web page. This uri is not a SDMX message.
version (default: 1.0)               com:VersionType         This version attribute holds a version number in the format of #[.#]+ (see common:VersionType definition for details). If not supplied, the version number is defaulted to 1.0.
validFrom                            xs:dateTime             The validFrom attribute provides the inclusive start date for providing supplemental validity information about the version.
validTo                              xs:dateTime             The validTo attribute provides the inclusive end date for providing supplemental validity information about the version.
agencyID                             com: NestedNCNameIDType The agencyID must be provided, and identifies the maintenance agency of the object.
isFinal (default: false)             xs:boolean              The isFinal attribute indicates whether the object is unchangeable without versioning. If the value is true, the object must be versioned upon change. If the final attribute is not supplied, then the object is assumed not to be final. Note that all production objects must be final.
isExternalReference (default: false) xs:boolean              The isExternalReference attribute, if true, indicates that the actual object is not defined the corresponding element, rather its full details are defined elsewhere - indicated by either the registryURL, the repositoryURL, or the structureURL. The purpose of this is so that each structure message does not have to redefine object that are already defined elsewhere. If the isExternalReference attribute is not set, then it is assumed to be false, and the object should contain the full definition of its contents. If more than one of the registryURL, the repositoryURL, and the structureURL are supplied, then the application processing the object can choose the method it finds best suited to retrieve the details of the object.
serviceURL                           xs:anyURI               The serviceURL attribute indicates the URL of an SDMX SOAP web service from which the details of the object can be retrieved. Note that this can be a registry or and SDMX structural metadata repository, as they both implement that same web service interface.
structureURL                         xs:anyURI               The structureURL attribute indicates the URL of a SDMX-ML structure message (in the same version as the source document) in which the externally referenced object is contained. Note that this may be a URL of an SDMX RESTful web service which will return the referenced object.
==================================== ======================= ==========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================

Element Documentation:

============================ ================================ =======================================================================================================================================================================================================================================================================================================================
**Name**                     **Type**                         **Documentation**
============================ ================================ =======================================================================================================================================================================================================================================================================================================================
com:Annotations              com:AnnotationsType              Annotations is a reusable element the provides for a collection of annotations. It has been made global so that restrictions of types that extend AnnotatableType my reference it.
com:Name                     com:TextType                     Name provides for a human-readable name for the object. This may be provided in multiple, parallel language-equivalent forms.
com:Description              com:TextType                     Description provides for a longer human-readable description of the object. This may be provided in multiple, parallel language-equivalent forms.
MetadataStructureCom ponents MetadataStructureCom ponentsType MetadataStructureComponents defines the grouping of the sets of the components that make up the metadata structure definition. All components and component list (target identifiers, identifier components, report structures, and metadata attributes) in the structure definition must have a unique identification.
============================ ================================ =======================================================================================================================================================================================================================================================================================================================

**MetadataStructureComponentsBaseType: **\ MetadataStructureComponentsBaseType
is an abstract base type that forms the basis for the
MetadataStructureComponentsType.

Derivation:

| *GroupingType* (restriction) 
|    |image314|\ MetadataStructureComponentsBaseType

Content:

{Empty}

**MetadataStructureComponentsType: **\ MetadataStructureComponentsType
describes the structure of the grouping of the sets of the components
that make up the metadata structure definition. At a minimum, a full
target identifier and at least one report structure must be defined.

Derivation:

| *GroupingType* (restriction) 
|    |image315|\ MetadataStructureComponentsBaseType (extension) 
|          |image316|\ MetadataStructureComponentsType

Content:

MetadataTarget+, ReportStructure+

Element Documentation:

=============== =================== ===============================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**        **Type**            **Documentation**
=============== =================== ===============================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
MetadataTarget  MetadataTargetType  MetadataTarget is a collection of target objects which when taken together describe a structure which defines the key of an object type to which metadata may be attached and serve to disambiguate reference metadata set reports.
ReportStructure ReportStructureType ReportStructure defines a report structure, which comprises a set of metadata attributes that can be defined as a hierarchy, for reporting reference metadata about a target object. The identification of metadata attributes must be unique at any given level of the report structure. Although there are XML schema constraints to help enforce this, these only apply to explicitly assigned identifiers. Identifiers inherited from a concept from which a metadata attribute takes its identity cannot be validated against this constraint. Therefore, systems processing metadata structure definitions will have to perform this check outside of the XML validation.
=============== =================== ===============================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================

**MetadataTargetBaseType: **\ MetadataTargetBaseType is an abstract base
type which forms the basis for the MetadataTargetType.

Derivation:

| *com:AnnotableType* (extension) 
|    |image317|\ *IdentifiableType* (extension) 
|          |image318|\ *ComponentListType* (restriction) 
|                |image319|\ *MetadataTargetBaseType*

Attributes:

id, urn?, uri?

Content:

com:Annotations?

Attribute Documentation:

======== ========== ==================================================================================================================================================================
**Name** **Type**   **Documentation**
======== ========== ==================================================================================================================================================================
id       com:IDType The id is the identifier for the object.
urn      xs:anyURI  The urn attribute holds a valid SDMX Registry URN (see SDMX Registry Specification for details).
uri      xs:anyURI  The uri attribute holds a URI that contains a link to a resource with additional information about the object, such as a web page. This uri is not a SDMX message.
======== ========== ==================================================================================================================================================================

Element Documentation:

=============== =================== ==================================================================================================================================================================================
**Name**        **Type**            **Documentation**
=============== =================== ==================================================================================================================================================================================
com:Annotations com:AnnotationsType Annotations is a reusable element the provides for a collection of annotations. It has been made global so that restrictions of types that extend AnnotatableType my reference it.
=============== =================== ==================================================================================================================================================================================

**MetadataTargetType: **

Derivation:

| *com:AnnotableType* (extension) 
|    |image320|\ *IdentifiableType* (extension) 
|          |image321|\ *ComponentListType* (restriction) 
|                |image322|\ *MetadataTargetBaseType* (extension) 
|                      |image323|\ MetadataTargetType

Attributes:

id, urn?, uri?

Content:

com:Annotations?, (KeyDescriptorValuesTarget \| DataSetTarget \|
ConstraintContentTarget \| ReportPeriodTarget \|
IdentifiableObjectTarget)+

Attribute Documentation:

======== ========== ==================================================================================================================================================================
**Name** **Type**   **Documentation**
======== ========== ==================================================================================================================================================================
id       com:IDType The id is the identifier for the object.
urn      xs:anyURI  The urn attribute holds a valid SDMX Registry URN (see SDMX Registry Specification for details).
uri      xs:anyURI  The uri attribute holds a URI that contains a link to a resource with additional information about the object, such as a web page. This uri is not a SDMX message.
======== ========== ==================================================================================================================================================================

Element Documentation:

========================== ============================== ==============================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                   **Type**                       **Documentation**
========================== ============================== ==============================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
com:Annotations            com:AnnotationsType            Annotations is a reusable element the provides for a collection of annotations. It has been made global so that restrictions of types that extend AnnotatableType my reference it.
KeyDescriptorValuesT arget KeyDescriptorValuesT argetType KeyDescriptorValuesTarget is target object which references a data key for the purpose of attach reference metadata to portions of data. A data key is a set of dimension references and values for those dimension. This component on its own is not of much use, as the data key only has local references to the dimensions. Therefore it is typical that this is used in combination with some sort of reference to the data (either a data set reference or a reference to the underlying structure, structure usage, or provision agreement of the data.
DataSetTarget              DataSetTargetType              DataSetTarget is target object which references a data set for the purpose of attaching reference metadata data. A data set reference is a full reference to a data provider and an identifier for the data set.
ConstraintContentTar get   ConstraintContentTar getType   ConstraintContentTarget is target object which references an attachment constraint for the purpose of attaching reference metadata data to data key sets or cube regions defined by the constraint.
ReportPeriodTarget         ReportPeriodTargetTy pe        ReportPeriodTarget is target object which specifies a reporting period to which a metadata report applies.
IdentifiableObjectTa rget  IdentifiableObjectTa rgetType  IdentifiableObjectTarget is target object which references an Identifiable object as defined in the SDMX Information Model. The reference must be complete (i.e. a URN or a complete set of reference fields). For an item object, it is possible to define a local representation of an item scheme from which the item must be referenced.
========================== ============================== ==============================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================

**TargetObject: **\ TargetObject is an abstract base type from which all
target objects of a metadata target are derived. It is based on a
component. Implementations of this will refined the local representation
so that the allowed values accurately reflect the representation of the
target object reference.

Derivation:

| *com:AnnotableType* (extension) 
|    |image324|\ *IdentifiableType* (restriction) 
|          |image325|\ *ComponentBaseType* (extension) 
|                |image326|\ *ComponentType* (extension) 
|                      |image327|\ *TargetObject*

Attributes:

id?, urn?, uri?

Content:

com:Annotations?, ConceptIdentity?, LocalRepresentation?

Attribute Documentation:

======== ================ ================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name** **Type**         **Documentation**
======== ================ ================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
id       com:NCNameIDType The id attribute holds an explicit identification of the component. If this identifier is not supplied, then it is assumed to be the same as the identifier of the concept referenced from the concept identity. Because structures require that every component be given a unique identifier, it may be necessary to assign an explicit identifier when more than one component in a structure reference concepts with same identifier. It is important to note that this applies strictly to the identifier of concept and not the URN. Therefore if two concepts with the same identifier from different concept schemes are referenced in the same structure, one of the components will have to provide a unique explicit identifier. The type of this identifier is restricted to the common:NCNameIDType. This is necessary, since component identifiers are used to create XML elements and attributes in data and metadata structure specific schemas and therefore must be compliant with the NCName type in XML Schema (see common:NCNameIDType for further details).
urn      xs:anyURI        The urn attribute holds a valid SDMX Registry URN (see SDMX Registry Specification for details).
uri      xs:anyURI        The uri attribute holds a URI that contains a link to a resource with additional information about the object, such as a web page. This uri is not a SDMX message.
======== ================ ================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================

Element Documentation:

=================== ========================= ==============================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**            **Type**                  **Documentation**
=================== ========================= ==============================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
com:Annotations     com:AnnotationsType       Annotations is a reusable element the provides for a collection of annotations. It has been made global so that restrictions of types that extend AnnotatableType my reference it.
ConceptIdentity     com: ConceptReferenceType ConceptIdentity allows for the referencing of a concept in a concept scheme. The component takes its semantic from this concept, and if an id is not specified, it takes its identification as well. If a representation (LocalRepresentation) is not supplied, then the representation of the component is also inherited from the concept. Note that in the case of the component representation being inherited from the concept, the allowable representations for the component still apply. Therefore, if a component references a concept with a core representation that is not allowed for the concept, that representation must be locally overridden. For components which can specify a concept role, it is implied that the concept which is referenced also identifies a role for the component.
LocalRepresentation *RepresentationType*      LocalRepresentation references item schemes that may be used to create the representation of a component. The type of this must be refined such that a concrete item scheme reference is used.
=================== ========================= ==============================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================

**KeyDescriptorValuesTargetType: **\ KeyDescriptorValuesTargetType
defines the structure of a key descriptor values target object. The key
descriptor values target object has a fixed representation and
identifier.

Derivation:

| *com:AnnotableType* (extension) 
|    |image328|\ *IdentifiableType* (restriction) 
|          |image329|\ *ComponentBaseType* (extension) 
|                |image330|\ *ComponentType* (extension) 
|                      |image331|\ *TargetObject* (restriction) 
|                            |image332|\ KeyDescriptorValuesTargetType

Attributes:

id?, urn?, uri?

Content:

com:Annotations?, LocalRepresentation

Attribute Documentation:

============================================== ================ ================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                                       **Type**         **Documentation**
============================================== ================ ================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
id (fixed: DIMENSION_DESCRIPTOR_VALUES_TARGET) com:NCNameIDType The id attribute holds an explicit identification of the component. If this identifier is not supplied, then it is assumed to be the same as the identifier of the concept referenced from the concept identity. Because structures require that every component be given a unique identifier, it may be necessary to assign an explicit identifier when more than one component in a structure reference concepts with same identifier. It is important to note that this applies strictly to the identifier of concept and not the URN. Therefore if two concepts with the same identifier from different concept schemes are referenced in the same structure, one of the components will have to provide a unique explicit identifier. The type of this identifier is restricted to the common:NCNameIDType. This is necessary, since component identifiers are used to create XML elements and attributes in data and metadata structure specific schemas and therefore must be compliant with the NCName type in XML Schema (see common:NCNameIDType for further details).
urn                                            xs:anyURI        The urn attribute holds a valid SDMX Registry URN (see SDMX Registry Specification for details).
uri                                            xs:anyURI        The uri attribute holds a URI that contains a link to a resource with additional information about the object, such as a web page. This uri is not a SDMX message.
============================================== ================ ================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================

Element Documentation:

=================== ====================================== ==============================================================================================================================================================================================
**Name**            **Type**                               **Documentation**
=================== ====================================== ==============================================================================================================================================================================================
com:Annotations     com:AnnotationsType                    Annotations is a reusable element the provides for a collection of annotations. It has been made global so that restrictions of types that extend AnnotatableType my reference it.
LocalRepresentation KeyDescriptorValuesR epresentationType LocalRepresentation references item schemes that may be used to create the representation of a component. The type of this must be refined such that a concrete item scheme reference is used.
=================== ====================================== ==============================================================================================================================================================================================

**DataSetTargetType: **\ DataSetTargetType defines the structure of a
data set target object. The data set target object has a fixed
representation and identifier.

Derivation:

| *com:AnnotableType* (extension) 
|    |image333|\ *IdentifiableType* (restriction) 
|          |image334|\ *ComponentBaseType* (extension) 
|                |image335|\ *ComponentType* (extension) 
|                      |image336|\ *TargetObject* (restriction) 
|                            |image337|\ DataSetTargetType

Attributes:

id?, urn?, uri?

Content:

com:Annotations?, LocalRepresentation

Attribute Documentation:

=========================== ================ ================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                    **Type**         **Documentation**
=========================== ================ ================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
id (fixed: DATA_SET_TARGET) com:NCNameIDType The id attribute holds an explicit identification of the component. If this identifier is not supplied, then it is assumed to be the same as the identifier of the concept referenced from the concept identity. Because structures require that every component be given a unique identifier, it may be necessary to assign an explicit identifier when more than one component in a structure reference concepts with same identifier. It is important to note that this applies strictly to the identifier of concept and not the URN. Therefore if two concepts with the same identifier from different concept schemes are referenced in the same structure, one of the components will have to provide a unique explicit identifier. The type of this identifier is restricted to the common:NCNameIDType. This is necessary, since component identifiers are used to create XML elements and attributes in data and metadata structure specific schemas and therefore must be compliant with the NCName type in XML Schema (see common:NCNameIDType for further details).
urn                         xs:anyURI        The urn attribute holds a valid SDMX Registry URN (see SDMX Registry Specification for details).
uri                         xs:anyURI        The uri attribute holds a URI that contains a link to a resource with additional information about the object, such as a web page. This uri is not a SDMX message.
=========================== ================ ================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================

Element Documentation:

=================== ========================== ==============================================================================================================================================================================================
**Name**            **Type**                   **Documentation**
=================== ========================== ==============================================================================================================================================================================================
com:Annotations     com:AnnotationsType        Annotations is a reusable element the provides for a collection of annotations. It has been made global so that restrictions of types that extend AnnotatableType my reference it.
LocalRepresentation DataSetRepresentatio nType LocalRepresentation references item schemes that may be used to create the representation of a component. The type of this must be refined such that a concrete item scheme reference is used.
=================== ========================== ==============================================================================================================================================================================================

**ConstraintContentTargetType: **\ ConstraintTargetType defines the
structure of a constraint target object. The constraint target object
has a fixed representation and identifier.

Derivation:

| *com:AnnotableType* (extension) 
|    |image338|\ *IdentifiableType* (restriction) 
|          |image339|\ *ComponentBaseType* (extension) 
|                |image340|\ *ComponentType* (extension) 
|                      |image341|\ *TargetObject* (restriction) 
|                            |image342|\ ConstraintContentTargetType

Attributes:

id?, urn?, uri?

Content:

com:Annotations?, LocalRepresentation

Attribute Documentation:

===================================== ================ ================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                              **Type**         **Documentation**
===================================== ================ ================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
id (fixed: CONSTRAINT_CONTENT_TARGET) com:NCNameIDType The id attribute holds an explicit identification of the component. If this identifier is not supplied, then it is assumed to be the same as the identifier of the concept referenced from the concept identity. Because structures require that every component be given a unique identifier, it may be necessary to assign an explicit identifier when more than one component in a structure reference concepts with same identifier. It is important to note that this applies strictly to the identifier of concept and not the URN. Therefore if two concepts with the same identifier from different concept schemes are referenced in the same structure, one of the components will have to provide a unique explicit identifier. The type of this identifier is restricted to the common:NCNameIDType. This is necessary, since component identifiers are used to create XML elements and attributes in data and metadata structure specific schemas and therefore must be compliant with the NCName type in XML Schema (see common:NCNameIDType for further details).
urn                                   xs:anyURI        The urn attribute holds a valid SDMX Registry URN (see SDMX Registry Specification for details).
uri                                   xs:anyURI        The uri attribute holds a URI that contains a link to a resource with additional information about the object, such as a web page. This uri is not a SDMX message.
===================================== ================ ================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================

Element Documentation:

=================== ============================= ==============================================================================================================================================================================================
**Name**            **Type**                      **Documentation**
=================== ============================= ==============================================================================================================================================================================================
com:Annotations     com:AnnotationsType           Annotations is a reusable element the provides for a collection of annotations. It has been made global so that restrictions of types that extend AnnotatableType my reference it.
LocalRepresentation ConstraintRepresenta tionType LocalRepresentation references item schemes that may be used to create the representation of a component. The type of this must be refined such that a concrete item scheme reference is used.
=================== ============================= ==============================================================================================================================================================================================

**ReportPeriodTargetType: **\ ReportPeriodTargetType defines the
structure of a report period target object. The report period target
object has a fixed representation and identifier.

Derivation:

| *com:AnnotableType* (extension) 
|    |image343|\ *IdentifiableType* (restriction) 
|          |image344|\ *ComponentBaseType* (extension) 
|                |image345|\ *ComponentType* (extension) 
|                      |image346|\ *TargetObject* (restriction) 
|                            |image347|\ ReportPeriodTargetType

Attributes:

id?, urn?, uri?

Content:

com:Annotations?, LocalRepresentation

Attribute Documentation:

================================ ================ ================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                         **Type**         **Documentation**
================================ ================ ================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
id (fixed: REPORT_PERIOD_TARGET) com:NCNameIDType The id attribute holds an explicit identification of the component. If this identifier is not supplied, then it is assumed to be the same as the identifier of the concept referenced from the concept identity. Because structures require that every component be given a unique identifier, it may be necessary to assign an explicit identifier when more than one component in a structure reference concepts with same identifier. It is important to note that this applies strictly to the identifier of concept and not the URN. Therefore if two concepts with the same identifier from different concept schemes are referenced in the same structure, one of the components will have to provide a unique explicit identifier. The type of this identifier is restricted to the common:NCNameIDType. This is necessary, since component identifiers are used to create XML elements and attributes in data and metadata structure specific schemas and therefore must be compliant with the NCName type in XML Schema (see common:NCNameIDType for further details).
urn                              xs:anyURI        The urn attribute holds a valid SDMX Registry URN (see SDMX Registry Specification for details).
uri                              xs:anyURI        The uri attribute holds a URI that contains a link to a resource with additional information about the object, such as a web page. This uri is not a SDMX message.
================================ ================ ================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================

Element Documentation:

=================== =============================== ==============================================================================================================================================================================================
**Name**            **Type**                        **Documentation**
=================== =============================== ==============================================================================================================================================================================================
com:Annotations     com:AnnotationsType             Annotations is a reusable element the provides for a collection of annotations. It has been made global so that restrictions of types that extend AnnotatableType my reference it.
LocalRepresentation ReportPeriodRepresen tationType LocalRepresentation references item schemes that may be used to create the representation of a component. The type of this must be refined such that a concrete item scheme reference is used.
=================== =============================== ==============================================================================================================================================================================================

**IdentifiableObjectTargetBaseType: **\ IdentifiableObjectTargetBaseType
is an abstract base type which forms the basis for the
IdentifiableObjectTargetType.

Derivation:

| *com:AnnotableType* (extension) 
|    |image348|\ *IdentifiableType* (restriction) 
|          |image349|\ *ComponentBaseType* (extension) 
|                |image350|\ *ComponentType* (extension) 
|                      |image351|\ *TargetObject* (restriction) 
|                            |image352|\ *IdentifiableObjectTargetBaseType*

Attributes:

id, urn?, uri?

Content:

com:Annotations?, LocalRepresentation

Attribute Documentation:

======== ================ ================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name** **Type**         **Documentation**
======== ================ ================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
id       com:NCNameIDType The id attribute holds an explicit identification of the component. If this identifier is not supplied, then it is assumed to be the same as the identifier of the concept referenced from the concept identity. Because structures require that every component be given a unique identifier, it may be necessary to assign an explicit identifier when more than one component in a structure reference concepts with same identifier. It is important to note that this applies strictly to the identifier of concept and not the URN. Therefore if two concepts with the same identifier from different concept schemes are referenced in the same structure, one of the components will have to provide a unique explicit identifier. The type of this identifier is restricted to the common:NCNameIDType. This is necessary, since component identifiers are used to create XML elements and attributes in data and metadata structure specific schemas and therefore must be compliant with the NCName type in XML Schema (see common:NCNameIDType for further details).
urn      xs:anyURI        The urn attribute holds a valid SDMX Registry URN (see SDMX Registry Specification for details).
uri      xs:anyURI        The uri attribute holds a URI that contains a link to a resource with additional information about the object, such as a web page. This uri is not a SDMX message.
======== ================ ================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================

Element Documentation:

=================== ===================================== ==============================================================================================================================================================================================
**Name**            **Type**                              **Documentation**
=================== ===================================== ==============================================================================================================================================================================================
com:Annotations     com:AnnotationsType                   Annotations is a reusable element the provides for a collection of annotations. It has been made global so that restrictions of types that extend AnnotatableType my reference it.
LocalRepresentation IdentifiableObjectRe presentationType LocalRepresentation references item schemes that may be used to create the representation of a component. The type of this must be refined such that a concrete item scheme reference is used.
=================== ===================================== ==============================================================================================================================================================================================

**IdentifiableObjectTargetType: **\ IdentifiableObjectTargetType defines
the structure of an identifiable target object. The identifiable target
object has a fixed representation of a reference and can specify a local
representation of any item scheme for the purpose of restricting which
items may be referenced. The identifiable object target must specify the
object type which the target object is meant to reference.

Derivation:

| *com:AnnotableType* (extension) 
|    |image353|\ *IdentifiableType* (restriction) 
|          |image354|\ *ComponentBaseType* (extension) 
|                |image355|\ *ComponentType* (extension) 
|                      |image356|\ *TargetObject* (restriction) 
|                            |image357|\ *IdentifiableObjectTargetBaseType* (extension) 
|                                  |image358|\ IdentifiableObjectTargetType

Attributes:

id, urn?, uri?, objectType

Content:

com:Annotations?, LocalRepresentation

Attribute Documentation:

========== ============================ ================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**   **Type**                     **Documentation**
========== ============================ ================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
id         com:NCNameIDType             The id attribute holds an explicit identification of the component. If this identifier is not supplied, then it is assumed to be the same as the identifier of the concept referenced from the concept identity. Because structures require that every component be given a unique identifier, it may be necessary to assign an explicit identifier when more than one component in a structure reference concepts with same identifier. It is important to note that this applies strictly to the identifier of concept and not the URN. Therefore if two concepts with the same identifier from different concept schemes are referenced in the same structure, one of the components will have to provide a unique explicit identifier. The type of this identifier is restricted to the common:NCNameIDType. This is necessary, since component identifiers are used to create XML elements and attributes in data and metadata structure specific schemas and therefore must be compliant with the NCName type in XML Schema (see common:NCNameIDType for further details).
urn        xs:anyURI                    The urn attribute holds a valid SDMX Registry URN (see SDMX Registry Specification for details).
uri        xs:anyURI                    The uri attribute holds a URI that contains a link to a resource with additional information about the object, such as a web page. This uri is not a SDMX message.
objectType com: ObjectTypeCodelistTy pe
========== ============================ ================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================

Element Documentation:

=================== ===================================== ==============================================================================================================================================================================================
**Name**            **Type**                              **Documentation**
=================== ===================================== ==============================================================================================================================================================================================
com:Annotations     com:AnnotationsType                   Annotations is a reusable element the provides for a collection of annotations. It has been made global so that restrictions of types that extend AnnotatableType my reference it.
LocalRepresentation IdentifiableObjectRe presentationType LocalRepresentation references item schemes that may be used to create the representation of a component. The type of this must be refined such that a concrete item scheme reference is used.
=================== ===================================== ==============================================================================================================================================================================================

**ReportStructureBaseType: **\ ReportStructureBaseType is an abstract
base type that serves as the basis for the ReportStructureType.

Derivation:

| *com:AnnotableType* (extension) 
|    |image359|\ *IdentifiableType* (extension) 
|          |image360|\ *ComponentListType* (restriction) 
|                |image361|\ *ReportStructureBaseType*

Attributes:

id, urn?, uri?

Content:

com:Annotations?, MetadataAttribute+

Attribute Documentation:

======== ========== ==================================================================================================================================================================
**Name** **Type**   **Documentation**
======== ========== ==================================================================================================================================================================
id       com:IDType The id is the identifier for the object.
urn      xs:anyURI  The urn attribute holds a valid SDMX Registry URN (see SDMX Registry Specification for details).
uri      xs:anyURI  The uri attribute holds a URI that contains a link to a resource with additional information about the object, such as a web page. This uri is not a SDMX message.
======== ========== ==================================================================================================================================================================

Element Documentation:

================= ====================== ==================================================================================================================================================================================
**Name**          **Type**               **Documentation**
================= ====================== ==================================================================================================================================================================================
com:Annotations   com:AnnotationsType    Annotations is a reusable element the provides for a collection of annotations. It has been made global so that restrictions of types that extend AnnotatableType my reference it.
MetadataAttribute MetadataAttributeTyp e MetadataAttribute defines the a metadata attribute, which is the value of an attribute, such as the instance of a coded or uncoded attribute in a metadata structure definition.
================= ====================== ==================================================================================================================================================================================

**ReportStructureType: **\ ReportStructureType describes the structure
of a report structure. It comprises a set of metadata attributes that
can be defined as a hierarchy, and identifies the potential attachment
of these attributes to an object by referencing a target identifier.

Derivation:

| *com:AnnotableType* (extension) 
|    |image362|\ *IdentifiableType* (extension) 
|          |image363|\ *ComponentListType* (restriction) 
|                |image364|\ *ReportStructureBaseType* (extension) 
|                      |image365|\ ReportStructureType

Attributes:

id, urn?, uri?

Content:

com:Annotations?, MetadataAttribute+, MetadataTarget+

Attribute Documentation:

======== ========== ==================================================================================================================================================================
**Name** **Type**   **Documentation**
======== ========== ==================================================================================================================================================================
id       com:IDType The id is the identifier for the object.
urn      xs:anyURI  The urn attribute holds a valid SDMX Registry URN (see SDMX Registry Specification for details).
uri      xs:anyURI  The uri attribute holds a URI that contains a link to a resource with additional information about the object, such as a web page. This uri is not a SDMX message.
======== ========== ==================================================================================================================================================================

Element Documentation:

================= ====================================== =======================================================================================================================================================================================================================================================
**Name**          **Type**                               **Documentation**
================= ====================================== =======================================================================================================================================================================================================================================================
com:Annotations   com:AnnotationsType                    Annotations is a reusable element the provides for a collection of annotations. It has been made global so that restrictions of types that extend AnnotatableType my reference it.
MetadataAttribute MetadataAttributeTyp e                 MetadataAttribute defines the a metadata attribute, which is the value of an attribute, such as the instance of a coded or uncoded attribute in a metadata structure definition.
MetadataTarget    com: LocalMetadataTargetR eferenceType MetadataTarget references a metadata target defined in the metadata structure definition. A report structure can reference multiple metadata targets which allows a report structure to be reused for attaching metadata to different types of targets.
================= ====================================== =======================================================================================================================================================================================================================================================

**MetadataAttributeBaseType: **\ MetadataAttributeBaseType is an
abstract base type the serves as the basis for the
MetadataAttributeType.

Derivation:

| *com:AnnotableType* (extension) 
|    |image366|\ *IdentifiableType* (restriction) 
|          |image367|\ *ComponentBaseType* (extension) 
|                |image368|\ *ComponentType* (restriction) 
|                      |image369|\ *MetadataAttributeBaseType*

Attributes:

id?, urn?, uri?

Content:

com:Annotations?, ConceptIdentity, LocalRepresentation?

Attribute Documentation:

======== ================ ================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name** **Type**         **Documentation**
======== ================ ================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
id       com:NCNameIDType The id attribute holds an explicit identification of the component. If this identifier is not supplied, then it is assumed to be the same as the identifier of the concept referenced from the concept identity. Because structures require that every component be given a unique identifier, it may be necessary to assign an explicit identifier when more than one component in a structure reference concepts with same identifier. It is important to note that this applies strictly to the identifier of concept and not the URN. Therefore if two concepts with the same identifier from different concept schemes are referenced in the same structure, one of the components will have to provide a unique explicit identifier. The type of this identifier is restricted to the common:NCNameIDType. This is necessary, since component identifiers are used to create XML elements and attributes in data and metadata structure specific schemas and therefore must be compliant with the NCName type in XML Schema (see common:NCNameIDType for further details).
urn      xs:anyURI        The urn attribute holds a valid SDMX Registry URN (see SDMX Registry Specification for details).
uri      xs:anyURI        The uri attribute holds a URI that contains a link to a resource with additional information about the object, such as a web page. This uri is not a SDMX message.
======== ================ ================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================

Element Documentation:

=================== ==================================== ==============================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**            **Type**                             **Documentation**
=================== ==================================== ==============================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
com:Annotations     com:AnnotationsType                  Annotations is a reusable element the provides for a collection of annotations. It has been made global so that restrictions of types that extend AnnotatableType my reference it.
ConceptIdentity     com: ConceptReferenceType            ConceptIdentity allows for the referencing of a concept in a concept scheme. The component takes its semantic from this concept, and if an id is not specified, it takes its identification as well. If a representation (LocalRepresentation) is not supplied, then the representation of the component is also inherited from the concept. Note that in the case of the component representation being inherited from the concept, the allowable representations for the component still apply. Therefore, if a component references a concept with a core representation that is not allowed for the concept, that representation must be locally overridden. For components which can specify a concept role, it is implied that the concept which is referenced also identifies a role for the component.
LocalRepresentation MetadataAttributeRep resentationType LocalRepresentation references item schemes that may be used to create the representation of a component. The type of this must be refined such that a concrete item scheme reference is used.
=================== ==================================== ==============================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================

**MetadataAttributeType: **\ MetadataAttributeType describes the
structure of a metadata attribute. The metadata attribute takes its
semantic, and in some cases it representation, from its concept
identity. A metadata attribute may be coded (via the local
representation), uncoded (via the text format), or take no value. In
addition to this value, the metadata attribute may also specify
subordinate metadata attributes. If a metadata attribute only serves the
purpose of containing subordinate metadata attributes, then the
isPresentational attribute should be used. Otherwise, it is assumed to
also take a value. If the metadata attribute does take a value, and a
representation is not defined, it will be inherited from the concept it
takes its semantic from. The optional id on the metadata attribute
uniquely identifies it within the metadata structured definition. If
this id is not supplied, its value is assumed to be that of the concept
referenced from the concept identity. Note that a metadata attribute (as
identified by the id attribute) definition must be unique across the
entire metadata structure definition (including target identifier,
identifier component, and report structure ids). A metadata attribute
may be used in multiple report structures and at different levels, but
the content (value and/or child metadata attributes and their
cardinality) of the metadata attribute cannot change.

Derivation:

| *com:AnnotableType* (extension) 
|    |image370|\ *IdentifiableType* (restriction) 
|          |image371|\ *ComponentBaseType* (extension) 
|                |image372|\ *ComponentType* (restriction) 
|                      |image373|\ *MetadataAttributeBaseType* (extension) 
|                            |image374|\ MetadataAttributeType

Attributes:

id?, urn?, uri?, minOccurs?, maxOccurs?, isPresentational?

Content:

com:Annotations?, ConceptIdentity, LocalRepresentation?,
MetadataAttribute\*

Attribute Documentation:

================================= ====================== ================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                          **Type**               **Documentation**
================================= ====================== ================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
id                                com:NCNameIDType       The id attribute holds an explicit identification of the component. If this identifier is not supplied, then it is assumed to be the same as the identifier of the concept referenced from the concept identity. Because structures require that every component be given a unique identifier, it may be necessary to assign an explicit identifier when more than one component in a structure reference concepts with same identifier. It is important to note that this applies strictly to the identifier of concept and not the URN. Therefore if two concepts with the same identifier from different concept schemes are referenced in the same structure, one of the components will have to provide a unique explicit identifier. The type of this identifier is restricted to the common:NCNameIDType. This is necessary, since component identifiers are used to create XML elements and attributes in data and metadata structure specific schemas and therefore must be compliant with the NCName type in XML Schema (see common:NCNameIDType for further details).
urn                               xs:anyURI              The urn attribute holds a valid SDMX Registry URN (see SDMX Registry Specification for details).
uri                               xs:anyURI              The uri attribute holds a URI that contains a link to a resource with additional information about the object, such as a web page. This uri is not a SDMX message.
minOccurs (default: 1)            xs: nonNegativeInteger The minOccurs attribute indicates the minimum number of times this metadata attribute can occur within its parent object.
maxOccurs (default: 1)            com:OccurenceType      The maxOccurs attribute indicates the maximum number of times this metadata attribute can occur within its parent object.
isPresentational (default: false) xs:boolean             The isPresentational attribute indicates whether the metadata attribute should allow for a value. A value of true, meaning the metadata attribute is presentational means that the attribute only contains child metadata attributes, and does not contain a value. If this attribute is not set to true, and a representation (coded or uncoded) is not defined, then the representation of the metadata attribute will be inherited from the concept from which it takes its identity.
================================= ====================== ================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================

Element Documentation:

=================== ==================================== ==============================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**            **Type**                             **Documentation**
=================== ==================================== ==============================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
com:Annotations     com:AnnotationsType                  Annotations is a reusable element the provides for a collection of annotations. It has been made global so that restrictions of types that extend AnnotatableType my reference it.
ConceptIdentity     com: ConceptReferenceType            ConceptIdentity allows for the referencing of a concept in a concept scheme. The component takes its semantic from this concept, and if an id is not specified, it takes its identification as well. If a representation (LocalRepresentation) is not supplied, then the representation of the component is also inherited from the concept. Note that in the case of the component representation being inherited from the concept, the allowable representations for the component still apply. Therefore, if a component references a concept with a core representation that is not allowed for the concept, that representation must be locally overridden. For components which can specify a concept role, it is implied that the concept which is referenced also identifies a role for the component.
LocalRepresentation MetadataAttributeRep resentationType LocalRepresentation references item schemes that may be used to create the representation of a component. The type of this must be refined such that a concrete item scheme reference is used.
MetadataAttribute   MetadataAttributeTyp e               MetadataAttribute defines the a metadata attribute, which is the value of an attribute, such as the instance of a coded or uncoded attribute in a metadata structure definition.
=================== ==================================== ==============================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================

**KeyDescriptorValuesRepresentationType: **\ KeyDescriptorValuesRepresentationType
defines the possible local representations of a key descriptor values
target object. The representation is fixed to always be a data key
(KeyValues).

Derivation:

| *RepresentationType* (restriction) 
|    |image375|\ KeyDescriptorValuesRepresentationType

Content:

TextFormat

Element Documentation:

========== ================================== ===============================================
**Name**   **Type**                           **Documentation**
========== ================================== ===============================================
TextFormat KeyDescriptorValuesT extFormatType TextFormat describes an uncoded textual format.
========== ================================== ===============================================

**DataSetRepresentationType: **\ DataSetRepresentationType defines the
possible local representations of a data set reference target object.
The representation is fixed to always be a data set reference.

Derivation:

| *RepresentationType* (restriction) 
|    |image376|\ DataSetRepresentationType

Content:

TextFormat

Element Documentation:

========== ====================== ===============================================
**Name**   **Type**               **Documentation**
========== ====================== ===============================================
TextFormat DataSetTextFormatTyp e TextFormat describes an uncoded textual format.
========== ====================== ===============================================

**ConstraintRepresentationType: **\ ConstraintRepresentationType defines
the possible local representations of a constraint reference target
object. The representation is fixed to always be an attachment
constraint reference.

Derivation:

| *RepresentationType* (restriction) 
|    |image377|\ ConstraintRepresentationType

Content:

TextFormat

Element Documentation:

========== ========================= ===============================================
**Name**   **Type**                  **Documentation**
========== ========================= ===============================================
TextFormat ConstraintTextFormat Type TextFormat describes an uncoded textual format.
========== ========================= ===============================================

**ReportPeriodRepresentationType: **\ ReportPeriodRepresentationType
defines the possible local representations of a report period target
object. The reprentation must be a time period or a subset of this
representation.

Derivation:

| *RepresentationType* (restriction) 
|    |image378|\ ReportPeriodRepresentationType

Content:

TextFormat

Element Documentation:

========== ================== ===============================================
**Name**   **Type**           **Documentation**
========== ================== ===============================================
TextFormat TimeTextFormatType TextFormat describes an uncoded textual format.
========== ================== ===============================================

**IdentifiableObjectRepresentationType: **\ IdentifiableObjectRepresentationType
defines the possible local representations of an identifiable object
target object.

Derivation:

| *RepresentationType* (restriction) 
|    |image379|\ IdentifiableObjectRepresentationType

Content:

(TextFormat \| Enumeration)

Element Documentation:

=========== ================================= ==================================================================================================================================================================================================================================
**Name**    **Type**                          **Documentation**
=========== ================================= ==================================================================================================================================================================================================================================
TextFormat  IdentifiableObjectTe xtFormatType TextFormat describes an uncoded textual format.
Enumeration com: ItemSchemeReferenceT ype     Enumeration is only permissible if the object type of the identifiable object target is an item in an item scheme. This enumeration is meant to limit the referencable objects to the items defined in the referenced item scheme.
=========== ================================= ==================================================================================================================================================================================================================================

**MetadataAttributeRepresentationType: **\ MetadataAttributeRepresentationType
defines the possible local representations of a metadata attribute.

Derivation:

| *RepresentationType* (restriction) 
|    |image380|\ MetadataAttributeRepresentationType

Content:

(TextFormat \| (Enumeration, EnumerationFormat?))

Element Documentation:

================= ============================= ================================================================================================================
**Name**          **Type**                      **Documentation**
================= ============================= ================================================================================================================
TextFormat        BasicComponentTextFo rmatType TextFormat describes an uncoded textual format.
Enumeration       com: CodelistReferenceTyp e   Enumeration references an item scheme that enumerates the allowable values for this representation.
EnumerationFormat CodededTextFormatTyp e        EnumerationFormat describes the facets of the item scheme enumeration. This is for the most part, informational.
================= ============================= ================================================================================================================

**TargetObjectTextFormatType: **\ TargetObjectTextFormatType is a
restricted version of the TextFormatType that does not allow for any
facets and only allows the text types for target objects.

Derivation:

| TextFormatType (restriction) 
|    |image381|\ TargetObjectTextFormatType

Attributes:

textType?

Content:

{Empty}

Attribute Documentation:

======== ==================== ================================================================================================================================================================================================================================================
**Name** **Type**             **Documentation**
======== ==================== ================================================================================================================================================================================================================================================
textType TargetObjectDataType The textType attribute provides a description of the datatype. If it is not specified, any valid characters may be included in the text field (it corresponds to the xs:string datatype of W3C XML Schema) within the constraints of the facets.
======== ==================== ================================================================================================================================================================================================================================================

**KeyDescriptorValuesTextFormatType: **\ KeyDescriptorValuesTextFormatType
is a restricted version of the NonFacetedTextFormatType that specifies a
fixed KeyValues representation.

Derivation:

| TextFormatType (restriction) 
|    |image382|\ TargetObjectTextFormatType (restriction) 
|          |image383|\ KeyDescriptorValuesTextFormatType

Attributes:

textType?

Content:

{Empty}

Attribute Documentation:

=========================== ==================== ================================================================================================================================================================================================================================================
**Name**                    **Type**             **Documentation**
=========================== ==================== ================================================================================================================================================================================================================================================
textType (fixed: KeyValues) TargetObjectDataType The textType attribute provides a description of the datatype. If it is not specified, any valid characters may be included in the text field (it corresponds to the xs:string datatype of W3C XML Schema) within the constraints of the facets.
=========================== ==================== ================================================================================================================================================================================================================================================

**DataSetTextFormatType: **\ DataSetTextFormatType is a restricted
version of the NonFacetedTextFormatType that specifies a fixed
DataSetReference representation.

Derivation:

| TextFormatType (restriction) 
|    |image384|\ TargetObjectTextFormatType (restriction) 
|          |image385|\ DataSetTextFormatType

Attributes:

textType?

Content:

{Empty}

Attribute Documentation:

================================== ==================== ================================================================================================================================================================================================================================================
**Name**                           **Type**             **Documentation**
================================== ==================== ================================================================================================================================================================================================================================================
textType (fixed: DataSetReference) TargetObjectDataType The textType attribute provides a description of the datatype. If it is not specified, any valid characters may be included in the text field (it corresponds to the xs:string datatype of W3C XML Schema) within the constraints of the facets.
================================== ==================== ================================================================================================================================================================================================================================================

**ConstraintTextFormatType: **\ ConstraintTextFormatType is a restricted
version of the NonFacetedTextFormatType that specifies a fixed
AttachmentConstraintReference representation.

Derivation:

| TextFormatType (restriction) 
|    |image386|\ TargetObjectTextFormatType (restriction) 
|          |image387|\ ConstraintTextFormatType

Attributes:

textType?

Content:

{Empty}

Attribute Documentation:

=============================================== ==================== ================================================================================================================================================================================================================================================
**Name**                                        **Type**             **Documentation**
=============================================== ==================== ================================================================================================================================================================================================================================================
textType (fixed: AttachmentConstraintReference) TargetObjectDataType The textType attribute provides a description of the datatype. If it is not specified, any valid characters may be included in the text field (it corresponds to the xs:string datatype of W3C XML Schema) within the constraints of the facets.
=============================================== ==================== ================================================================================================================================================================================================================================================

**IdentifiableObjectTextFormatType: **\ IdentifiableObjectTextFormatType
is a restricted version of the NonFacetedTextFormatType that specifies a
fixed IdentifiableReference representation.

Derivation:

| TextFormatType (restriction) 
|    |image388|\ TargetObjectTextFormatType (restriction) 
|          |image389|\ IdentifiableObjectTextFormatType

Attributes:

textType?

Content:

{Empty}

Attribute Documentation:

======================================= ==================== ================================================================================================================================================================================================================================================
**Name**                                **Type**             **Documentation**
======================================= ==================== ================================================================================================================================================================================================================================================
textType (fixed: IdentifiableReference) TargetObjectDataType The textType attribute provides a description of the datatype. If it is not specified, any valid characters may be included in the text field (it corresponds to the xs:string datatype of W3C XML Schema) within the constraints of the facets.
======================================= ==================== ================================================================================================================================================================================================================================================

**OrganisationSchemeBaseType: **\ OrganisationSchemeBaseType is an
abstract base type for any organisation scheme.

Derivation:

| *com:AnnotableType* (extension) 
|    |image390|\ *IdentifiableType* (extension) 
|          |image391|\ *NameableType* (extension) 
|                |image392|\ *VersionableType* (restriction) 
|                      |image393|\ *MaintainableBaseType* (extension) 
|                            |image394|\ *MaintainableType* (extension) 
|                                  |image395|\ *ItemSchemeType* (restriction) 
|                                        |image396|\ *OrganisationSchemeBaseType*

Attributes:

id, urn?, uri?, version?, validFrom?, validTo?, agencyID, isFinal?,
isExternalReference?, serviceURL?, structureURL?, isPartial?

Content:

com:Annotations?, com:Name+, com:Description\*

Attribute Documentation:

==================================== ======================= ==========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                             **Type**                **Documentation**
==================================== ======================= ==========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
id                                   com:IDType              The id is the identifier for the object.
urn                                  xs:anyURI               The urn attribute holds a valid SDMX Registry URN (see SDMX Registry Specification for details).
uri                                  xs:anyURI               The uri attribute holds a URI that contains a link to a resource with additional information about the object, such as a web page. This uri is not a SDMX message.
version (default: 1.0)               com:VersionType         This version attribute holds a version number in the format of #[.#]+ (see common:VersionType definition for details). If not supplied, the version number is defaulted to 1.0.
validFrom                            xs:dateTime             The validFrom attribute provides the inclusive start date for providing supplemental validity information about the version.
validTo                              xs:dateTime             The validTo attribute provides the inclusive end date for providing supplemental validity information about the version.
agencyID                             com: NestedNCNameIDType The agencyID must be provided, and identifies the maintenance agency of the object.
isFinal (default: false)             xs:boolean              The isFinal attribute indicates whether the object is unchangeable without versioning. If the value is true, the object must be versioned upon change. If the final attribute is not supplied, then the object is assumed not to be final. Note that all production objects must be final.
isExternalReference (default: false) xs:boolean              The isExternalReference attribute, if true, indicates that the actual object is not defined the corresponding element, rather its full details are defined elsewhere - indicated by either the registryURL, the repositoryURL, or the structureURL. The purpose of this is so that each structure message does not have to redefine object that are already defined elsewhere. If the isExternalReference attribute is not set, then it is assumed to be false, and the object should contain the full definition of its contents. If more than one of the registryURL, the repositoryURL, and the structureURL are supplied, then the application processing the object can choose the method it finds best suited to retrieve the details of the object.
serviceURL                           xs:anyURI               The serviceURL attribute indicates the URL of an SDMX SOAP web service from which the details of the object can be retrieved. Note that this can be a registry or and SDMX structural metadata repository, as they both implement that same web service interface.
structureURL                         xs:anyURI               The structureURL attribute indicates the URL of a SDMX-ML structure message (in the same version as the source document) in which the externally referenced object is contained. Note that this may be a URL of an SDMX RESTful web service which will return the referenced object.
isPartial (default: false)           xs:boolean              The isPartial, if true, indicates that only the relevant portion of the item scheme is being communicated. This is used in cases where a codelist is returned for a key family in the context of a constraint.
==================================== ======================= ==========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================

Element Documentation:

=============== =================== ==================================================================================================================================================================================
**Name**        **Type**            **Documentation**
=============== =================== ==================================================================================================================================================================================
com:Annotations com:AnnotationsType Annotations is a reusable element the provides for a collection of annotations. It has been made global so that restrictions of types that extend AnnotatableType my reference it.
com:Name        com:TextType        Name provides for a human-readable name for the object. This may be provided in multiple, parallel language-equivalent forms.
com:Description com:TextType        Description provides for a longer human-readable description of the object. This may be provided in multiple, parallel language-equivalent forms.
=============== =================== ==================================================================================================================================================================================

**OrganisationSchemeType: **\ OrganisationSchemeType describes the
structure of an organisation scheme.

Derivation:

| *com:AnnotableType* (extension) 
|    |image397|\ *IdentifiableType* (extension) 
|          |image398|\ *NameableType* (extension) 
|                |image399|\ *VersionableType* (restriction) 
|                      |image400|\ *MaintainableBaseType* (extension) 
|                            |image401|\ *MaintainableType* (extension) 
|                                  |image402|\ *ItemSchemeType* (restriction) 
|                                        |image403|\ *OrganisationSchemeBaseType* (extension) 
|                                              |image404|\ *OrganisationSchemeType*

Attributes:

id, urn?, uri?, version?, validFrom?, validTo?, agencyID, isFinal?,
isExternalReference?, serviceURL?, structureURL?, isPartial?

Content:

com:Annotations?, com:Name+, com:Description*, \ *Organisation\**

Attribute Documentation:

==================================== ======================= ==========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                             **Type**                **Documentation**
==================================== ======================= ==========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
id                                   com:IDType              The id is the identifier for the object.
urn                                  xs:anyURI               The urn attribute holds a valid SDMX Registry URN (see SDMX Registry Specification for details).
uri                                  xs:anyURI               The uri attribute holds a URI that contains a link to a resource with additional information about the object, such as a web page. This uri is not a SDMX message.
version (default: 1.0)               com:VersionType         This version attribute holds a version number in the format of #[.#]+ (see common:VersionType definition for details). If not supplied, the version number is defaulted to 1.0.
validFrom                            xs:dateTime             The validFrom attribute provides the inclusive start date for providing supplemental validity information about the version.
validTo                              xs:dateTime             The validTo attribute provides the inclusive end date for providing supplemental validity information about the version.
agencyID                             com: NestedNCNameIDType The agencyID must be provided, and identifies the maintenance agency of the object.
isFinal (default: false)             xs:boolean              The isFinal attribute indicates whether the object is unchangeable without versioning. If the value is true, the object must be versioned upon change. If the final attribute is not supplied, then the object is assumed not to be final. Note that all production objects must be final.
isExternalReference (default: false) xs:boolean              The isExternalReference attribute, if true, indicates that the actual object is not defined the corresponding element, rather its full details are defined elsewhere - indicated by either the registryURL, the repositoryURL, or the structureURL. The purpose of this is so that each structure message does not have to redefine object that are already defined elsewhere. If the isExternalReference attribute is not set, then it is assumed to be false, and the object should contain the full definition of its contents. If more than one of the registryURL, the repositoryURL, and the structureURL are supplied, then the application processing the object can choose the method it finds best suited to retrieve the details of the object.
serviceURL                           xs:anyURI               The serviceURL attribute indicates the URL of an SDMX SOAP web service from which the details of the object can be retrieved. Note that this can be a registry or and SDMX structural metadata repository, as they both implement that same web service interface.
structureURL                         xs:anyURI               The structureURL attribute indicates the URL of a SDMX-ML structure message (in the same version as the source document) in which the externally referenced object is contained. Note that this may be a URL of an SDMX RESTful web service which will return the referenced object.
isPartial (default: false)           xs:boolean              The isPartial, if true, indicates that only the relevant portion of the item scheme is being communicated. This is used in cases where a codelist is returned for a key family in the context of a constraint.
==================================== ======================= ==========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================

Element Documentation:

=============== =================== ==================================================================================================================================================================================
**Name**        **Type**            **Documentation**
=============== =================== ==================================================================================================================================================================================
com:Annotations com:AnnotationsType Annotations is a reusable element the provides for a collection of annotations. It has been made global so that restrictions of types that extend AnnotatableType my reference it.
com:Name        com:TextType        Name provides for a human-readable name for the object. This may be provided in multiple, parallel language-equivalent forms.
com:Description com:TextType        Description provides for a longer human-readable description of the object. This may be provided in multiple, parallel language-equivalent forms.
*Organisation*  *OrganisationType*  Organisation is an abstract substitution head for a generic organisation.
=============== =================== ==================================================================================================================================================================================

**BaseOrganisationType: **\ BaseOrganisationType is an abstract base
type the forms the basis for the OrganisationType.

Derivation:

| *com:AnnotableType* (extension) 
|    |image405|\ *IdentifiableType* (extension) 
|          |image406|\ *NameableType* (restriction) 
|                |image407|\ *ItemBaseType* (extension) 
|                      |image408|\ *ItemType* (restriction) 
|                            |image409|\ *BaseOrganisationType*

Attributes:

id, urn?, uri?

Content:

com:Annotations?, com:Name+, com:Description*, Parent?

Attribute Documentation:

======== ========== ==================================================================================================================================================================
**Name** **Type**   **Documentation**
======== ========== ==================================================================================================================================================================
id       com:IDType The id is the identifier for the object.
urn      xs:anyURI  The urn attribute holds a valid SDMX Registry URN (see SDMX Registry Specification for details).
uri      xs:anyURI  The uri attribute holds a URI that contains a link to a resource with additional information about the object, such as a web page. This uri is not a SDMX message.
======== ========== ==================================================================================================================================================================

Element Documentation:

=============== ========================================== ============================================================================================================================================================================================================================================
**Name**        **Type**                                   **Documentation**
=============== ========================================== ============================================================================================================================================================================================================================================
com:Annotations com:AnnotationsType                        Annotations is a reusable element the provides for a collection of annotations. It has been made global so that restrictions of types that extend AnnotatableType my reference it.
com:Name        com:TextType                               Name provides for a human-readable name for the object. This may be provided in multiple, parallel language-equivalent forms.
com:Description com:TextType                               Description provides for a longer human-readable description of the object. This may be provided in multiple, parallel language-equivalent forms.
Parent          *com: LocalOrganisationRef erenceBaseType* If the particular organisation scheme allows, an organisation may reference a parent organisation defined in the same scheme. This does not affect the identification of the organisation, but rather only serves to state the relationship.
=============== ========================================== ============================================================================================================================================================================================================================================

**OrganisationType: **\ OrganisationType in an abstract type which
describes the structure of the details of an organisation. In addition
to the basic organisation identification, contact details can be
provided.

Derivation:

| *com:AnnotableType* (extension) 
|    |image410|\ *IdentifiableType* (extension) 
|          |image411|\ *NameableType* (restriction) 
|                |image412|\ *ItemBaseType* (extension) 
|                      |image413|\ *ItemType* (restriction) 
|                            |image414|\ *BaseOrganisationType* (extension) 
|                                  |image415|\ *OrganisationType*

Attributes:

id, urn?, uri?

Content:

com:Annotations?, com:Name+, com:Description*, Parent?, Contact\*

Attribute Documentation:

======== ========== ==================================================================================================================================================================
**Name** **Type**   **Documentation**
======== ========== ==================================================================================================================================================================
id       com:IDType The id is the identifier for the object.
urn      xs:anyURI  The urn attribute holds a valid SDMX Registry URN (see SDMX Registry Specification for details).
uri      xs:anyURI  The uri attribute holds a URI that contains a link to a resource with additional information about the object, such as a web page. This uri is not a SDMX message.
======== ========== ==================================================================================================================================================================

Element Documentation:

=============== ========================================== ============================================================================================================================================================================================================================================
**Name**        **Type**                                   **Documentation**
=============== ========================================== ============================================================================================================================================================================================================================================
com:Annotations com:AnnotationsType                        Annotations is a reusable element the provides for a collection of annotations. It has been made global so that restrictions of types that extend AnnotatableType my reference it.
com:Name        com:TextType                               Name provides for a human-readable name for the object. This may be provided in multiple, parallel language-equivalent forms.
com:Description com:TextType                               Description provides for a longer human-readable description of the object. This may be provided in multiple, parallel language-equivalent forms.
Parent          *com: LocalOrganisationRef erenceBaseType* If the particular organisation scheme allows, an organisation may reference a parent organisation defined in the same scheme. This does not affect the identification of the organisation, but rather only serves to state the relationship.
Contact         ContactType                                Contact describes a contact for the organisation,
=============== ========================================== ============================================================================================================================================================================================================================================

**AgencySchemeType: **\ AgencySchemeType defines a specific type of
organisation scheme which contains only maintenance agencies. The agency
scheme maintained by a particular maintenance agency is always provided
a fixed identifier and version, and is never final. Therefore, agencies
can be added or removed without have to version the scheme. Agencies
schemes have no hierarchy, meaning that no agency may define a
relationship with another agency in the scheme. In fact, the actual
parent agency for an agency in a scheme is the agency which defines the
scheme.

Derivation:

| *com:AnnotableType* (extension) 
|    |image416|\ *IdentifiableType* (extension) 
|          |image417|\ *NameableType* (extension) 
|                |image418|\ *VersionableType* (restriction) 
|                      |image419|\ *MaintainableBaseType* (extension) 
|                            |image420|\ *MaintainableType* (extension) 
|                                  |image421|\ *ItemSchemeType* (restriction) 
|                                        |image422|\ *OrganisationSchemeBaseType* (extension) 
|                                              |image423|\ *OrganisationSchemeType* (restriction) 
|                                                    |image424|\ AgencySchemeType

Attributes:

id, urn?, uri?, version?, validFrom?, validTo?, agencyID, isFinal?,
isExternalReference?, serviceURL?, structureURL?, isPartial?

Content:

com:Annotations?, com:Name+, com:Description*, Agency\*

Attribute Documentation:

==================================== ======================= ==========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                             **Type**                **Documentation**
==================================== ======================= ==========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
id (fixed: AGENCIES)                 com:IDType              The id is the identifier for the object.
urn                                  xs:anyURI               The urn attribute holds a valid SDMX Registry URN (see SDMX Registry Specification for details).
uri                                  xs:anyURI               The uri attribute holds a URI that contains a link to a resource with additional information about the object, such as a web page. This uri is not a SDMX message.
version (fixed: 1.0)                 com:VersionType         This version attribute holds a version number in the format of #[.#]+ (see common:VersionType definition for details). If not supplied, the version number is defaulted to 1.0.
validFrom                            xs:dateTime             The validFrom attribute provides the inclusive start date for providing supplemental validity information about the version.
validTo                              xs:dateTime             The validTo attribute provides the inclusive end date for providing supplemental validity information about the version.
agencyID                             com: NestedNCNameIDType The agencyID must be provided, and identifies the maintenance agency of the object.
isFinal (fixed: false)               xs:boolean              The isFinal attribute indicates whether the object is unchangeable without versioning. If the value is true, the object must be versioned upon change. If the final attribute is not supplied, then the object is assumed not to be final. Note that all production objects must be final.
isExternalReference (default: false) xs:boolean              The isExternalReference attribute, if true, indicates that the actual object is not defined the corresponding element, rather its full details are defined elsewhere - indicated by either the registryURL, the repositoryURL, or the structureURL. The purpose of this is so that each structure message does not have to redefine object that are already defined elsewhere. If the isExternalReference attribute is not set, then it is assumed to be false, and the object should contain the full definition of its contents. If more than one of the registryURL, the repositoryURL, and the structureURL are supplied, then the application processing the object can choose the method it finds best suited to retrieve the details of the object.
serviceURL                           xs:anyURI               The serviceURL attribute indicates the URL of an SDMX SOAP web service from which the details of the object can be retrieved. Note that this can be a registry or and SDMX structural metadata repository, as they both implement that same web service interface.
structureURL                         xs:anyURI               The structureURL attribute indicates the URL of a SDMX-ML structure message (in the same version as the source document) in which the externally referenced object is contained. Note that this may be a URL of an SDMX RESTful web service which will return the referenced object.
isPartial (default: false)           xs:boolean              The isPartial, if true, indicates that only the relevant portion of the item scheme is being communicated. This is used in cases where a codelist is returned for a key family in the context of a constraint.
==================================== ======================= ==========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================

Element Documentation:

=============== =================== ======================================================================================================================================================================================
**Name**        **Type**            **Documentation**
=============== =================== ======================================================================================================================================================================================
com:Annotations com:AnnotationsType Annotations is a reusable element the provides for a collection of annotations. It has been made global so that restrictions of types that extend AnnotatableType my reference it.
com:Name        com:TextType        Name provides for a human-readable name for the object. This may be provided in multiple, parallel language-equivalent forms.
com:Description com:TextType        Description provides for a longer human-readable description of the object. This may be provided in multiple, parallel language-equivalent forms.
Agency          AgencyType          Agency is an organisation which maintains structural metadata such as statistical classifications, glossaries, key family structural definitions, and metadata structure definitions..
=============== =================== ======================================================================================================================================================================================

**DataConsumerSchemeType: **\ DataConsumerSchemeType defines a type of
organisation scheme which contains only data consumers. The data
consumer scheme maintained by a particular maintenance agency is always
provided a fixed identifier and version, and is never final. Therefore,
consumers can be added or removed without have to version the scheme.
This scheme has no hierarchy, meaning that no organisation may define a
relationship with another organisation in the scheme.

Derivation:

| *com:AnnotableType* (extension) 
|    |image425|\ *IdentifiableType* (extension) 
|          |image426|\ *NameableType* (extension) 
|                |image427|\ *VersionableType* (restriction) 
|                      |image428|\ *MaintainableBaseType* (extension) 
|                            |image429|\ *MaintainableType* (extension) 
|                                  |image430|\ *ItemSchemeType* (restriction) 
|                                        |image431|\ *OrganisationSchemeBaseType* (extension) 
|                                              |image432|\ *OrganisationSchemeType* (restriction) 
|                                                    |image433|\ DataConsumerSchemeType

Attributes:

id, urn?, uri?, version?, validFrom?, validTo?, agencyID, isFinal?,
isExternalReference?, serviceURL?, structureURL?, isPartial?

Content:

com:Annotations?, com:Name+, com:Description*, DataConsumer\*

Attribute Documentation:

==================================== ======================= ==========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                             **Type**                **Documentation**
==================================== ======================= ==========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
id (fixed: DATA_CONSUMERS)           com:IDType              The id is the identifier for the object.
urn                                  xs:anyURI               The urn attribute holds a valid SDMX Registry URN (see SDMX Registry Specification for details).
uri                                  xs:anyURI               The uri attribute holds a URI that contains a link to a resource with additional information about the object, such as a web page. This uri is not a SDMX message.
version (fixed: 1.0)                 com:VersionType         This version attribute holds a version number in the format of #[.#]+ (see common:VersionType definition for details). If not supplied, the version number is defaulted to 1.0.
validFrom                            xs:dateTime             The validFrom attribute provides the inclusive start date for providing supplemental validity information about the version.
validTo                              xs:dateTime             The validTo attribute provides the inclusive end date for providing supplemental validity information about the version.
agencyID                             com: NestedNCNameIDType The agencyID must be provided, and identifies the maintenance agency of the object.
isFinal (fixed: false)               xs:boolean              The isFinal attribute indicates whether the object is unchangeable without versioning. If the value is true, the object must be versioned upon change. If the final attribute is not supplied, then the object is assumed not to be final. Note that all production objects must be final.
isExternalReference (default: false) xs:boolean              The isExternalReference attribute, if true, indicates that the actual object is not defined the corresponding element, rather its full details are defined elsewhere - indicated by either the registryURL, the repositoryURL, or the structureURL. The purpose of this is so that each structure message does not have to redefine object that are already defined elsewhere. If the isExternalReference attribute is not set, then it is assumed to be false, and the object should contain the full definition of its contents. If more than one of the registryURL, the repositoryURL, and the structureURL are supplied, then the application processing the object can choose the method it finds best suited to retrieve the details of the object.
serviceURL                           xs:anyURI               The serviceURL attribute indicates the URL of an SDMX SOAP web service from which the details of the object can be retrieved. Note that this can be a registry or and SDMX structural metadata repository, as they both implement that same web service interface.
structureURL                         xs:anyURI               The structureURL attribute indicates the URL of a SDMX-ML structure message (in the same version as the source document) in which the externally referenced object is contained. Note that this may be a URL of an SDMX RESTful web service which will return the referenced object.
isPartial (default: false)           xs:boolean              The isPartial, if true, indicates that only the relevant portion of the item scheme is being communicated. This is used in cases where a codelist is returned for a key family in the context of a constraint.
==================================== ======================= ==========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================

Element Documentation:

=============== =================== ==================================================================================================================================================================================
**Name**        **Type**            **Documentation**
=============== =================== ==================================================================================================================================================================================
com:Annotations com:AnnotationsType Annotations is a reusable element the provides for a collection of annotations. It has been made global so that restrictions of types that extend AnnotatableType my reference it.
com:Name        com:TextType        Name provides for a human-readable name for the object. This may be provided in multiple, parallel language-equivalent forms.
com:Description com:TextType        Description provides for a longer human-readable description of the object. This may be provided in multiple, parallel language-equivalent forms.
DataConsumer    DataConsumerType    DataConsumer describes an organisation using data as input for further processing.
=============== =================== ==================================================================================================================================================================================

**DataProviderSchemeType: **\ DataProviderSchemeType defines a type of
organisation scheme which contains only data providers. The data
provider scheme maintained by a particular maintenance agency is always
provided a fixed identifier and version, and is never final. Therefore,
providers can be added or removed without have to version the scheme.
This scheme has no hierarchy, meaning that no organisation may define a
relationship with another organisation in the scheme

Derivation:

| *com:AnnotableType* (extension) 
|    |image434|\ *IdentifiableType* (extension) 
|          |image435|\ *NameableType* (extension) 
|                |image436|\ *VersionableType* (restriction) 
|                      |image437|\ *MaintainableBaseType* (extension) 
|                            |image438|\ *MaintainableType* (extension) 
|                                  |image439|\ *ItemSchemeType* (restriction) 
|                                        |image440|\ *OrganisationSchemeBaseType* (extension) 
|                                              |image441|\ *OrganisationSchemeType* (restriction) 
|                                                    |image442|\ DataProviderSchemeType

Attributes:

id, urn?, uri?, version?, validFrom?, validTo?, agencyID, isFinal?,
isExternalReference?, serviceURL?, structureURL?, isPartial?

Content:

com:Annotations?, com:Name+, com:Description*, DataProvider\*

Attribute Documentation:

==================================== ======================= ==========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                             **Type**                **Documentation**
==================================== ======================= ==========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
id (fixed: DATA_PROVIDERS)           com:IDType              The id is the identifier for the object.
urn                                  xs:anyURI               The urn attribute holds a valid SDMX Registry URN (see SDMX Registry Specification for details).
uri                                  xs:anyURI               The uri attribute holds a URI that contains a link to a resource with additional information about the object, such as a web page. This uri is not a SDMX message.
version (fixed: 1.0)                 com:VersionType         This version attribute holds a version number in the format of #[.#]+ (see common:VersionType definition for details). If not supplied, the version number is defaulted to 1.0.
validFrom                            xs:dateTime             The validFrom attribute provides the inclusive start date for providing supplemental validity information about the version.
validTo                              xs:dateTime             The validTo attribute provides the inclusive end date for providing supplemental validity information about the version.
agencyID                             com: NestedNCNameIDType The agencyID must be provided, and identifies the maintenance agency of the object.
isFinal (fixed: false)               xs:boolean              The isFinal attribute indicates whether the object is unchangeable without versioning. If the value is true, the object must be versioned upon change. If the final attribute is not supplied, then the object is assumed not to be final. Note that all production objects must be final.
isExternalReference (default: false) xs:boolean              The isExternalReference attribute, if true, indicates that the actual object is not defined the corresponding element, rather its full details are defined elsewhere - indicated by either the registryURL, the repositoryURL, or the structureURL. The purpose of this is so that each structure message does not have to redefine object that are already defined elsewhere. If the isExternalReference attribute is not set, then it is assumed to be false, and the object should contain the full definition of its contents. If more than one of the registryURL, the repositoryURL, and the structureURL are supplied, then the application processing the object can choose the method it finds best suited to retrieve the details of the object.
serviceURL                           xs:anyURI               The serviceURL attribute indicates the URL of an SDMX SOAP web service from which the details of the object can be retrieved. Note that this can be a registry or and SDMX structural metadata repository, as they both implement that same web service interface.
structureURL                         xs:anyURI               The structureURL attribute indicates the URL of a SDMX-ML structure message (in the same version as the source document) in which the externally referenced object is contained. Note that this may be a URL of an SDMX RESTful web service which will return the referenced object.
isPartial (default: false)           xs:boolean              The isPartial, if true, indicates that only the relevant portion of the item scheme is being communicated. This is used in cases where a codelist is returned for a key family in the context of a constraint.
==================================== ======================= ==========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================

Element Documentation:

=============== =================== ==================================================================================================================================================================================
**Name**        **Type**            **Documentation**
=============== =================== ==================================================================================================================================================================================
com:Annotations com:AnnotationsType Annotations is a reusable element the provides for a collection of annotations. It has been made global so that restrictions of types that extend AnnotatableType my reference it.
com:Name        com:TextType        Name provides for a human-readable name for the object. This may be provided in multiple, parallel language-equivalent forms.
com:Description com:TextType        Description provides for a longer human-readable description of the object. This may be provided in multiple, parallel language-equivalent forms.
DataProvider    DataProviderType    DataProvider describes an organisation that produces data or reference metadata.
=============== =================== ==================================================================================================================================================================================

**OrganisationUnitSchemeType: **\ OrganisationUnitSchemeType defines a
type of organisation scheme which simply defines organisations and there
parent child relationships. Organisations in this scheme are assigned no
particular role, and may in fact exist within the other type of
organisation schemes as well.

Derivation:

| *com:AnnotableType* (extension) 
|    |image443|\ *IdentifiableType* (extension) 
|          |image444|\ *NameableType* (extension) 
|                |image445|\ *VersionableType* (restriction) 
|                      |image446|\ *MaintainableBaseType* (extension) 
|                            |image447|\ *MaintainableType* (extension) 
|                                  |image448|\ *ItemSchemeType* (restriction) 
|                                        |image449|\ *OrganisationSchemeBaseType* (extension) 
|                                              |image450|\ *OrganisationSchemeType* (restriction) 
|                                                    |image451|\ OrganisationUnitSchemeType

Attributes:

id, urn?, uri?, version?, validFrom?, validTo?, agencyID, isFinal?,
isExternalReference?, serviceURL?, structureURL?, isPartial?

Content:

com:Annotations?, com:Name+, com:Description*, OrganisationUnit\*

Attribute Documentation:

==================================== ======================= ==========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                             **Type**                **Documentation**
==================================== ======================= ==========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
id                                   com:IDType              The id is the identifier for the object.
urn                                  xs:anyURI               The urn attribute holds a valid SDMX Registry URN (see SDMX Registry Specification for details).
uri                                  xs:anyURI               The uri attribute holds a URI that contains a link to a resource with additional information about the object, such as a web page. This uri is not a SDMX message.
version (default: 1.0)               com:VersionType         This version attribute holds a version number in the format of #[.#]+ (see common:VersionType definition for details). If not supplied, the version number is defaulted to 1.0.
validFrom                            xs:dateTime             The validFrom attribute provides the inclusive start date for providing supplemental validity information about the version.
validTo                              xs:dateTime             The validTo attribute provides the inclusive end date for providing supplemental validity information about the version.
agencyID                             com: NestedNCNameIDType The agencyID must be provided, and identifies the maintenance agency of the object.
isFinal (default: false)             xs:boolean              The isFinal attribute indicates whether the object is unchangeable without versioning. If the value is true, the object must be versioned upon change. If the final attribute is not supplied, then the object is assumed not to be final. Note that all production objects must be final.
isExternalReference (default: false) xs:boolean              The isExternalReference attribute, if true, indicates that the actual object is not defined the corresponding element, rather its full details are defined elsewhere - indicated by either the registryURL, the repositoryURL, or the structureURL. The purpose of this is so that each structure message does not have to redefine object that are already defined elsewhere. If the isExternalReference attribute is not set, then it is assumed to be false, and the object should contain the full definition of its contents. If more than one of the registryURL, the repositoryURL, and the structureURL are supplied, then the application processing the object can choose the method it finds best suited to retrieve the details of the object.
serviceURL                           xs:anyURI               The serviceURL attribute indicates the URL of an SDMX SOAP web service from which the details of the object can be retrieved. Note that this can be a registry or and SDMX structural metadata repository, as they both implement that same web service interface.
structureURL                         xs:anyURI               The structureURL attribute indicates the URL of a SDMX-ML structure message (in the same version as the source document) in which the externally referenced object is contained. Note that this may be a URL of an SDMX RESTful web service which will return the referenced object.
isPartial (default: false)           xs:boolean              The isPartial, if true, indicates that only the relevant portion of the item scheme is being communicated. This is used in cases where a codelist is returned for a key family in the context of a constraint.
==================================== ======================= ==========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================

Element Documentation:

================ ==================== ==================================================================================================================================================================================
**Name**         **Type**             **Documentation**
================ ==================== ==================================================================================================================================================================================
com:Annotations  com:AnnotationsType  Annotations is a reusable element the provides for a collection of annotations. It has been made global so that restrictions of types that extend AnnotatableType my reference it.
com:Name         com:TextType         Name provides for a human-readable name for the object. This may be provided in multiple, parallel language-equivalent forms.
com:Description  com:TextType         Description provides for a longer human-readable description of the object. This may be provided in multiple, parallel language-equivalent forms.
OrganisationUnit OrganisationUnitType OrganisationUnit describes a generic organisation, which serves not predefined role in SDMX.
================ ==================== ==================================================================================================================================================================================

**AgencyType: **\ AgencyType defines the structure of an agency
description. The contacts defined for the organisation are specific to
the agency role the organisation is serving.

Derivation:

| *com:AnnotableType* (extension) 
|    |image452|\ *IdentifiableType* (extension) 
|          |image453|\ *NameableType* (restriction) 
|                |image454|\ *ItemBaseType* (extension) 
|                      |image455|\ *ItemType* (restriction) 
|                            |image456|\ *BaseOrganisationType* (extension) 
|                                  |image457|\ *OrganisationType* (restriction) 
|                                        |image458|\ AgencyType

Attributes:

id, urn?, uri?

Content:

com:Annotations?, com:Name+, com:Description*, Contact\*

Attribute Documentation:

======== ================ ==========================================================================================================================================================================================================================================================================================================================================================================================
**Name** **Type**         **Documentation**
======== ================ ==========================================================================================================================================================================================================================================================================================================================================================================================
id       com:NCNameIDType The id attribute holds the identification of the agency. The type of this id is restricted to the common:NCNNameIDType. This is necessary, since the agency identifier will be used as part of the name for simple types in data and metadata structure specific schemas and therefore must be compliant with the NCName type in XML Schema (see common:NCNameIDType for further details).
urn      xs:anyURI        The urn attribute holds a valid SDMX Registry URN (see SDMX Registry Specification for details).
uri      xs:anyURI        The uri attribute holds a URI that contains a link to a resource with additional information about the object, such as a web page. This uri is not a SDMX message.
======== ================ ==========================================================================================================================================================================================================================================================================================================================================================================================

Element Documentation:

=============== =================== ==================================================================================================================================================================================
**Name**        **Type**            **Documentation**
=============== =================== ==================================================================================================================================================================================
com:Annotations com:AnnotationsType Annotations is a reusable element the provides for a collection of annotations. It has been made global so that restrictions of types that extend AnnotatableType my reference it.
com:Name        com:TextType        Name provides for a human-readable name for the object. This may be provided in multiple, parallel language-equivalent forms.
com:Description com:TextType        Description provides for a longer human-readable description of the object. This may be provided in multiple, parallel language-equivalent forms.
Contact         ContactType         Contact describes a contact for the organisation,
=============== =================== ==================================================================================================================================================================================

**DataConsumerType: **\ DataConsumerType defines the structure of a data
consumer description. The contacts defined for the organisation are
specific to the data consumer role the organisation is serving.

Derivation:

| *com:AnnotableType* (extension) 
|    |image459|\ *IdentifiableType* (extension) 
|          |image460|\ *NameableType* (restriction) 
|                |image461|\ *ItemBaseType* (extension) 
|                      |image462|\ *ItemType* (restriction) 
|                            |image463|\ *BaseOrganisationType* (extension) 
|                                  |image464|\ *OrganisationType* (restriction) 
|                                        |image465|\ DataConsumerType

Attributes:

id, urn?, uri?

Content:

com:Annotations?, com:Name+, com:Description*, Contact\*

Attribute Documentation:

======== ========== ==================================================================================================================================================================
**Name** **Type**   **Documentation**
======== ========== ==================================================================================================================================================================
id       com:IDType The id is the identifier for the object.
urn      xs:anyURI  The urn attribute holds a valid SDMX Registry URN (see SDMX Registry Specification for details).
uri      xs:anyURI  The uri attribute holds a URI that contains a link to a resource with additional information about the object, such as a web page. This uri is not a SDMX message.
======== ========== ==================================================================================================================================================================

Element Documentation:

=============== =================== ==================================================================================================================================================================================
**Name**        **Type**            **Documentation**
=============== =================== ==================================================================================================================================================================================
com:Annotations com:AnnotationsType Annotations is a reusable element the provides for a collection of annotations. It has been made global so that restrictions of types that extend AnnotatableType my reference it.
com:Name        com:TextType        Name provides for a human-readable name for the object. This may be provided in multiple, parallel language-equivalent forms.
com:Description com:TextType        Description provides for a longer human-readable description of the object. This may be provided in multiple, parallel language-equivalent forms.
Contact         ContactType         Contact describes a contact for the organisation,
=============== =================== ==================================================================================================================================================================================

**DataProviderType: **\ DataProviderType defines the structure of a data
provider description. The contacts defined for the organisation are
specific to the data provider role the organisation is serving.

Derivation:

| *com:AnnotableType* (extension) 
|    |image466|\ *IdentifiableType* (extension) 
|          |image467|\ *NameableType* (restriction) 
|                |image468|\ *ItemBaseType* (extension) 
|                      |image469|\ *ItemType* (restriction) 
|                            |image470|\ *BaseOrganisationType* (extension) 
|                                  |image471|\ *OrganisationType* (restriction) 
|                                        |image472|\ DataProviderType

Attributes:

id, urn?, uri?

Content:

com:Annotations?, com:Name+, com:Description*, Contact\*

Attribute Documentation:

======== ========== ==================================================================================================================================================================
**Name** **Type**   **Documentation**
======== ========== ==================================================================================================================================================================
id       com:IDType The id is the identifier for the object.
urn      xs:anyURI  The urn attribute holds a valid SDMX Registry URN (see SDMX Registry Specification for details).
uri      xs:anyURI  The uri attribute holds a URI that contains a link to a resource with additional information about the object, such as a web page. This uri is not a SDMX message.
======== ========== ==================================================================================================================================================================

Element Documentation:

=============== =================== ==================================================================================================================================================================================
**Name**        **Type**            **Documentation**
=============== =================== ==================================================================================================================================================================================
com:Annotations com:AnnotationsType Annotations is a reusable element the provides for a collection of annotations. It has been made global so that restrictions of types that extend AnnotatableType my reference it.
com:Name        com:TextType        Name provides for a human-readable name for the object. This may be provided in multiple, parallel language-equivalent forms.
com:Description com:TextType        Description provides for a longer human-readable description of the object. This may be provided in multiple, parallel language-equivalent forms.
Contact         ContactType         Contact describes a contact for the organisation,
=============== =================== ==================================================================================================================================================================================

**OrganisationUnitType: **\ OrganisationUnitType defines the structure
of an organisation unit description. In addition to general
identification and contact information, an organisation unit can specify
a relationship with another organisation unit from the same scheme which
is its parent organisation.

Derivation:

| *com:AnnotableType* (extension) 
|    |image473|\ *IdentifiableType* (extension) 
|          |image474|\ *NameableType* (restriction) 
|                |image475|\ *ItemBaseType* (extension) 
|                      |image476|\ *ItemType* (restriction) 
|                            |image477|\ *BaseOrganisationType* (extension) 
|                                  |image478|\ *OrganisationType* (restriction) 
|                                        |image479|\ OrganisationUnitType

Attributes:

id, urn?, uri?

Content:

com:Annotations?, com:Name+, com:Description*, Parent?, Contact\*

Attribute Documentation:

======== ========== ==================================================================================================================================================================
**Name** **Type**   **Documentation**
======== ========== ==================================================================================================================================================================
id       com:IDType The id is the identifier for the object.
urn      xs:anyURI  The urn attribute holds a valid SDMX Registry URN (see SDMX Registry Specification for details).
uri      xs:anyURI  The uri attribute holds a URI that contains a link to a resource with additional information about the object, such as a web page. This uri is not a SDMX message.
======== ========== ==================================================================================================================================================================

Element Documentation:

=============== ======================================== ============================================================================================================================================================================================================================================
**Name**        **Type**                                 **Documentation**
=============== ======================================== ============================================================================================================================================================================================================================================
com:Annotations com:AnnotationsType                      Annotations is a reusable element the provides for a collection of annotations. It has been made global so that restrictions of types that extend AnnotatableType my reference it.
com:Name        com:TextType                             Name provides for a human-readable name for the object. This may be provided in multiple, parallel language-equivalent forms.
com:Description com:TextType                             Description provides for a longer human-readable description of the object. This may be provided in multiple, parallel language-equivalent forms.
Parent          com: LocalOrganisationUni tReferenceType If the particular organisation scheme allows, an organisation may reference a parent organisation defined in the same scheme. This does not affect the identification of the organisation, but rather only serves to state the relationship.
Contact         ContactType                              Contact describes a contact for the organisation,
=============== ======================================== ============================================================================================================================================================================================================================================

**ContactType: **\ ContactType describes the structure of a contact's
details.

Attributes:

id?

Content:

com:Name*, Department*, Role*, (Telephone \| Fax \| X400 \| URI \|
Email)\*

Attribute Documentation:

======== ========== ======================================================================
**Name** **Type**   **Documentation**
======== ========== ======================================================================
id       com:IDType The id attribute is used to carry user id information for the contact.
======== ========== ======================================================================

Element Documentation:

========== ============ ============================================================================================================================
**Name**   **Type**     **Documentation**
========== ============ ============================================================================================================================
com:Name   com:TextType Name is a reusable element, used for providing a human-readable name for an object.
Department com:TextType Department is designation of the organisational structure by a linguistic expression, within which the contact person works.
Role       com:TextType Role is the responsibility of the contact person with respect to the object for which this person is the contact.
Telephone  xs:string    Telephone holds the telephone number for the contact person.
Fax        xs:string    Fax holds the fax number for the contact person.
X400       xs:string    X400 holds the X.400 address for the contact person.
URI        xs:anyURI    URI holds an information URL for the contact person.
Email      xs:string    Email holds the email address for the contact person.
========== ============ ============================================================================================================================

**ProvisionAgreementType: **\ ProvisionAgreementType describes the
structure of a provision agreement. A provision agreement defines an
agreement for a data provider to report data or reference metadata
against a flow. Attributes which describe how the registry must behave
when data or metadata is registered against this provision agreement are
supplied.

Derivation:

| *com:AnnotableType* (extension) 
|    |image480|\ *IdentifiableType* (extension) 
|          |image481|\ *NameableType* (extension) 
|                |image482|\ *VersionableType* (restriction) 
|                      |image483|\ *MaintainableBaseType* (extension) 
|                            |image484|\ *MaintainableType* (extension) 
|                                  |image485|\ ProvisionAgreementType

Attributes:

id, urn?, uri?, version?, validFrom?, validTo?, agencyID, isFinal?,
isExternalReference?, serviceURL?, structureURL?

Content:

com:Annotations?, com:Name+, com:Description*, StructureUsage,
DataProvider

Attribute Documentation:

==================================== ======================= ==========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                             **Type**                **Documentation**
==================================== ======================= ==========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
id                                   com:IDType              The id is the identifier for the object.
urn                                  xs:anyURI               The urn attribute holds a valid SDMX Registry URN (see SDMX Registry Specification for details).
uri                                  xs:anyURI               The uri attribute holds a URI that contains a link to a resource with additional information about the object, such as a web page. This uri is not a SDMX message.
version (default: 1.0)               com:VersionType         This version attribute holds a version number in the format of #[.#]+ (see common:VersionType definition for details). If not supplied, the version number is defaulted to 1.0.
validFrom                            xs:dateTime             The validFrom attribute provides the inclusive start date for providing supplemental validity information about the version.
validTo                              xs:dateTime             The validTo attribute provides the inclusive end date for providing supplemental validity information about the version.
agencyID                             com: NestedNCNameIDType The agencyID must be provided, and identifies the maintenance agency of the object.
isFinal (default: false)             xs:boolean              The isFinal attribute indicates whether the object is unchangeable without versioning. If the value is true, the object must be versioned upon change. If the final attribute is not supplied, then the object is assumed not to be final. Note that all production objects must be final.
isExternalReference (default: false) xs:boolean              The isExternalReference attribute, if true, indicates that the actual object is not defined the corresponding element, rather its full details are defined elsewhere - indicated by either the registryURL, the repositoryURL, or the structureURL. The purpose of this is so that each structure message does not have to redefine object that are already defined elsewhere. If the isExternalReference attribute is not set, then it is assumed to be false, and the object should contain the full definition of its contents. If more than one of the registryURL, the repositoryURL, and the structureURL are supplied, then the application processing the object can choose the method it finds best suited to retrieve the details of the object.
serviceURL                           xs:anyURI               The serviceURL attribute indicates the URL of an SDMX SOAP web service from which the details of the object can be retrieved. Note that this can be a registry or and SDMX structural metadata repository, as they both implement that same web service interface.
structureURL                         xs:anyURI               The structureURL attribute indicates the URL of a SDMX-ML structure message (in the same version as the source document) in which the externally referenced object is contained. Note that this may be a URL of an SDMX RESTful web service which will return the referenced object.
==================================== ======================= ==========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================

Element Documentation:

=============== ================================= ======================================================================================================================================================================================================
**Name**        **Type**                          **Documentation**
=============== ================================= ======================================================================================================================================================================================================
com:Annotations com:AnnotationsType               Annotations is a reusable element the provides for a collection of annotations. It has been made global so that restrictions of types that extend AnnotatableType my reference it.
com:Name        com:TextType                      Name provides for a human-readable name for the object. This may be provided in multiple, parallel language-equivalent forms.
com:Description com:TextType                      Description provides for a longer human-readable description of the object. This may be provided in multiple, parallel language-equivalent forms.
StructureUsage  com: StructureUsageRefere nceType DataflowReference provides a reference to a pre-existing structure usage (i.e. a dataflow or metadataflow) in the registry. The reference is provided via a URN and/or a full set of reference fields.
DataProvider    com: DataProviderReferenc eType   DataProvider provides a reference to a pre-existing data (or metadata) provider in the registry. The reference is provided via a URN and/or a full set of reference fields.
=============== ================================= ======================================================================================================================================================================================================

**ProcessType: **\ ProcessType describes the structure of a process,
which is a scheme which defines or documents the operations performed on
data in order to validate data or to derive new information according to
a given set of rules. Processes occur in order, and will continue in
order unless a transition dictates another step should occur.

Derivation:

| *com:AnnotableType* (extension) 
|    |image486|\ *IdentifiableType* (extension) 
|          |image487|\ *NameableType* (extension) 
|                |image488|\ *VersionableType* (restriction) 
|                      |image489|\ *MaintainableBaseType* (extension) 
|                            |image490|\ *MaintainableType* (extension) 
|                                  |image491|\ ProcessType

Attributes:

id, urn?, uri?, version?, validFrom?, validTo?, agencyID, isFinal?,
isExternalReference?, serviceURL?, structureURL?

Content:

com:Annotations?, com:Name+, com:Description*, ProcessStep\*

Attribute Documentation:

==================================== ======================= ==========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                             **Type**                **Documentation**
==================================== ======================= ==========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
id                                   com:IDType              The id is the identifier for the object.
urn                                  xs:anyURI               The urn attribute holds a valid SDMX Registry URN (see SDMX Registry Specification for details).
uri                                  xs:anyURI               The uri attribute holds a URI that contains a link to a resource with additional information about the object, such as a web page. This uri is not a SDMX message.
version (default: 1.0)               com:VersionType         This version attribute holds a version number in the format of #[.#]+ (see common:VersionType definition for details). If not supplied, the version number is defaulted to 1.0.
validFrom                            xs:dateTime             The validFrom attribute provides the inclusive start date for providing supplemental validity information about the version.
validTo                              xs:dateTime             The validTo attribute provides the inclusive end date for providing supplemental validity information about the version.
agencyID                             com: NestedNCNameIDType The agencyID must be provided, and identifies the maintenance agency of the object.
isFinal (default: false)             xs:boolean              The isFinal attribute indicates whether the object is unchangeable without versioning. If the value is true, the object must be versioned upon change. If the final attribute is not supplied, then the object is assumed not to be final. Note that all production objects must be final.
isExternalReference (default: false) xs:boolean              The isExternalReference attribute, if true, indicates that the actual object is not defined the corresponding element, rather its full details are defined elsewhere - indicated by either the registryURL, the repositoryURL, or the structureURL. The purpose of this is so that each structure message does not have to redefine object that are already defined elsewhere. If the isExternalReference attribute is not set, then it is assumed to be false, and the object should contain the full definition of its contents. If more than one of the registryURL, the repositoryURL, and the structureURL are supplied, then the application processing the object can choose the method it finds best suited to retrieve the details of the object.
serviceURL                           xs:anyURI               The serviceURL attribute indicates the URL of an SDMX SOAP web service from which the details of the object can be retrieved. Note that this can be a registry or and SDMX structural metadata repository, as they both implement that same web service interface.
structureURL                         xs:anyURI               The structureURL attribute indicates the URL of a SDMX-ML structure message (in the same version as the source document) in which the externally referenced object is contained. Note that this may be a URL of an SDMX RESTful web service which will return the referenced object.
==================================== ======================= ==========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================

Element Documentation:

=============== =================== ==================================================================================================================================================================================
**Name**        **Type**            **Documentation**
=============== =================== ==================================================================================================================================================================================
com:Annotations com:AnnotationsType Annotations is a reusable element the provides for a collection of annotations. It has been made global so that restrictions of types that extend AnnotatableType my reference it.
com:Name        com:TextType        Name provides for a human-readable name for the object. This may be provided in multiple, parallel language-equivalent forms.
com:Description com:TextType        Description provides for a longer human-readable description of the object. This may be provided in multiple, parallel language-equivalent forms.
ProcessStep     ProcessStepType     ProcessStep defines a process step, which is a specific operation, performed on data in order to validate or to derive new information according to a given set of rules.
=============== =================== ==================================================================================================================================================================================

**ProcessStepBaseType: **\ ProcessStepBaseType is an abstract base type
used as the basis for the ProcessStepType.

Derivation:

| *com:AnnotableType* (extension) 
|    |image492|\ *IdentifiableType* (extension) 
|          |image493|\ *NameableType* (restriction) 
|                |image494|\ *ProcessStepBaseType*

Attributes:

id, urn?, uri?

Content:

com:Annotations?, com:Name+, com:Description\*

Attribute Documentation:

======== ========== ==================================================================================================================================================================
**Name** **Type**   **Documentation**
======== ========== ==================================================================================================================================================================
id       com:IDType The id is the identifier for the object.
urn      xs:anyURI  The urn attribute holds a valid SDMX Registry URN (see SDMX Registry Specification for details).
uri      xs:anyURI  The uri attribute holds a URI that contains a link to a resource with additional information about the object, such as a web page. This uri is not a SDMX message.
======== ========== ==================================================================================================================================================================

Element Documentation:

=============== =================== ==================================================================================================================================================================================
**Name**        **Type**            **Documentation**
=============== =================== ==================================================================================================================================================================================
com:Annotations com:AnnotationsType Annotations is a reusable element the provides for a collection of annotations. It has been made global so that restrictions of types that extend AnnotatableType my reference it.
com:Name        com:TextType        Name provides for a human-readable name for the object. This may be provided in multiple, parallel language-equivalent forms.
com:Description com:TextType        Description provides for a longer human-readable description of the object. This may be provided in multiple, parallel language-equivalent forms.
=============== =================== ==================================================================================================================================================================================

**ProcessStepType: **\ ProcessStepType describes the structure of a
process step. A nested process step is automatically sub-ordinate, and
followed as the next step. If the following step is conditional, it
should be referenced in a transition.

Derivation:

| *com:AnnotableType* (extension) 
|    |image495|\ *IdentifiableType* (extension) 
|          |image496|\ *NameableType* (restriction) 
|                |image497|\ *ProcessStepBaseType* (extension) 
|                      |image498|\ ProcessStepType

Attributes:

id, urn?, uri?

Content:

com:Annotations?, com:Name+, com:Description*, Input*, Output*,
Computation?, Transition*, ProcessStep\*

Attribute Documentation:

======== ========== ==================================================================================================================================================================
**Name** **Type**   **Documentation**
======== ========== ==================================================================================================================================================================
id       com:IDType The id is the identifier for the object.
urn      xs:anyURI  The urn attribute holds a valid SDMX Registry URN (see SDMX Registry Specification for details).
uri      xs:anyURI  The uri attribute holds a URI that contains a link to a resource with additional information about the object, such as a web page. This uri is not a SDMX message.
======== ========== ==================================================================================================================================================================

Element Documentation:

=============== =================== =========================================================================================================================================================================================================================
**Name**        **Type**            **Documentation**
=============== =================== =========================================================================================================================================================================================================================
com:Annotations com:AnnotationsType Annotations is a reusable element the provides for a collection of annotations. It has been made global so that restrictions of types that extend AnnotatableType my reference it.
com:Name        com:TextType        Name provides for a human-readable name for the object. This may be provided in multiple, parallel language-equivalent forms.
com:Description com:TextType        Description provides for a longer human-readable description of the object. This may be provided in multiple, parallel language-equivalent forms.
Input           InputOutputType     Input references an object which is an input to the process step.
Output          InputOutputType     Output references an object which is an output form the process step.
Computation     ComputationType     Computation describes the computations involved in the process, in any form desired by the user (these are informational rather than machine-actionable), and so may be supplied in multiple, parallel-language versions.
Transition      TransitionType      Transition describes the next process steps. Each transition in a process step should be evaluated, allowing for multiple process step branches from a single process step.
ProcessStep     ProcessStepType     ProcessStep defines a process step, which is a specific operation, performed on data in order to validate or to derive new information according to a given set of rules.
=============== =================== =========================================================================================================================================================================================================================

**TransitionType: **\ TransitionType describes the details of a
transition, which is an expression in a textual or formalised way of the
transformation of data between two specific operations performed on the
data.

Derivation:

| *com:AnnotableType* (extension) 
|    |image499|\ *IdentifiableType* (extension) 
|          |image500|\ TransitionType

Attributes:

id?, urn?, uri?, localID?

Content:

com:Annotations?, TargetStep, Condition+

Attribute Documentation:

======== ========== ==================================================================================================================================================================
**Name** **Type**   **Documentation**
======== ========== ==================================================================================================================================================================
id       com:IDType The id is the identifier for the object.
urn      xs:anyURI  The urn attribute holds a valid SDMX Registry URN (see SDMX Registry Specification for details).
uri      xs:anyURI  The uri attribute holds a URI that contains a link to a resource with additional information about the object, such as a web page. This uri is not a SDMX message.
localID  com:IDType The localID attribute is an optional identification for the transition within the process.
======== ========== ==================================================================================================================================================================

Element Documentation:

=============== =================================== ===========================================================================================================================================================================================================================
**Name**        **Type**                            **Documentation**
=============== =================================== ===========================================================================================================================================================================================================================
com:Annotations com:AnnotationsType                 Annotations is a reusable element the provides for a collection of annotations. It has been made global so that restrictions of types that extend AnnotatableType my reference it.
TargetStep      com: LocalProcessStepRefe renceType TargetStep references a process step within the process that should be transitioned to, should the conditions described be met.
Condition       com:TextType                        Condition is a textual description of the conditions to be met in order for the target step to be proceeded to. It is informational only (not machine-actionable), and may be supplied in multiple, parallel-language form.
=============== =================================== ===========================================================================================================================================================================================================================

**ComputationType: **\ ComputationType describes a computation in a
process.

Derivation:

| *com:AnnotableType* (extension) 
|    |image501|\ ComputationType

Attributes:

localID?, softwarePackage?, softwareLanguage?, softwareVersion?

Content:

com:Annotations?, com:Description+

Attribute Documentation:

================ ========== =================================================================================================================================
**Name**         **Type**   **Documentation**
================ ========== =================================================================================================================================
localID          com:IDType The localID attribute is an optional identification for the computation within the process.
softwarePackage  xs:string  The softwarePackage attribute holds the name of the software package that is used to perform the computation.
softwareLanguage xs:string  The softwareLanguage attribute holds the coding language that the software package used to perform the computation is written in.
softwareVersion  xs:string  The softwareVersion attribute hold the version of the software package that is used to perform that computation.
================ ========== =================================================================================================================================

Element Documentation:

=============== =================== ==============================================================================================================================================================================================
**Name**        **Type**            **Documentation**
=============== =================== ==============================================================================================================================================================================================
com:Annotations com:AnnotationsType Annotations is a reusable element the provides for a collection of annotations. It has been made global so that restrictions of types that extend AnnotatableType my reference it.
com:Description com:TextType        Description describe the computation in any form desired by the user (these are informational rather than machine-actionable), and so may be supplied in multiple, parallel-language versions,
=============== =================== ==============================================================================================================================================================================================

**InputOutputType: **\ InputOutputType describes the structure of an
input or output to a process step. It provides a reference to the object
that is the input or output.

Derivation:

| *com:AnnotableType* (extension) 
|    |image502|\ InputOutputType

Attributes:

localID?

Content:

com:Annotations?, ObjectReference

Attribute Documentation:

======== ========== ===============================================================================================
**Name** **Type**   **Documentation**
======== ========== ===============================================================================================
localID  com:IDType The localID attribute is an optional identification for the input or output within the process.
======== ========== ===============================================================================================

Element Documentation:

=============== ======================== ==================================================================================================================================================================================
**Name**        **Type**                 **Documentation**
=============== ======================== ==================================================================================================================================================================================
com:Annotations com:AnnotationsType      Annotations is a reusable element the provides for a collection of annotations. It has been made global so that restrictions of types that extend AnnotatableType my reference it.
ObjectReference com: ObjectReferenceType ObjectReference is an abstract substitution head that references the object that is an input or output. It is substituted with a concrete reference to an explicit object type.
=============== ======================== ==================================================================================================================================================================================

**ReportingTaxonomyType: **\ ReportingTaxonomyType describes the
structure of a reporting taxonomy, which is a scheme which defines the
composition structure of a data report where each component can be
described by an independent structure or structure usage description.

Derivation:

| *com:AnnotableType* (extension) 
|    |image503|\ *IdentifiableType* (extension) 
|          |image504|\ *NameableType* (extension) 
|                |image505|\ *VersionableType* (restriction) 
|                      |image506|\ *MaintainableBaseType* (extension) 
|                            |image507|\ *MaintainableType* (extension) 
|                                  |image508|\ *ItemSchemeType* (restriction) 
|                                        |image509|\ ReportingTaxonomyType

Attributes:

id, urn?, uri?, version?, validFrom?, validTo?, agencyID, isFinal?,
isExternalReference?, serviceURL?, structureURL?, isPartial?

Content:

com:Annotations?, com:Name+, com:Description*, ReportingCategory\*

Attribute Documentation:

==================================== ======================= ==========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                             **Type**                **Documentation**
==================================== ======================= ==========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
id                                   com:IDType              The id is the identifier for the object.
urn                                  xs:anyURI               The urn attribute holds a valid SDMX Registry URN (see SDMX Registry Specification for details).
uri                                  xs:anyURI               The uri attribute holds a URI that contains a link to a resource with additional information about the object, such as a web page. This uri is not a SDMX message.
version (default: 1.0)               com:VersionType         This version attribute holds a version number in the format of #[.#]+ (see common:VersionType definition for details). If not supplied, the version number is defaulted to 1.0.
validFrom                            xs:dateTime             The validFrom attribute provides the inclusive start date for providing supplemental validity information about the version.
validTo                              xs:dateTime             The validTo attribute provides the inclusive end date for providing supplemental validity information about the version.
agencyID                             com: NestedNCNameIDType The agencyID must be provided, and identifies the maintenance agency of the object.
isFinal (default: false)             xs:boolean              The isFinal attribute indicates whether the object is unchangeable without versioning. If the value is true, the object must be versioned upon change. If the final attribute is not supplied, then the object is assumed not to be final. Note that all production objects must be final.
isExternalReference (default: false) xs:boolean              The isExternalReference attribute, if true, indicates that the actual object is not defined the corresponding element, rather its full details are defined elsewhere - indicated by either the registryURL, the repositoryURL, or the structureURL. The purpose of this is so that each structure message does not have to redefine object that are already defined elsewhere. If the isExternalReference attribute is not set, then it is assumed to be false, and the object should contain the full definition of its contents. If more than one of the registryURL, the repositoryURL, and the structureURL are supplied, then the application processing the object can choose the method it finds best suited to retrieve the details of the object.
serviceURL                           xs:anyURI               The serviceURL attribute indicates the URL of an SDMX SOAP web service from which the details of the object can be retrieved. Note that this can be a registry or and SDMX structural metadata repository, as they both implement that same web service interface.
structureURL                         xs:anyURI               The structureURL attribute indicates the URL of a SDMX-ML structure message (in the same version as the source document) in which the externally referenced object is contained. Note that this may be a URL of an SDMX RESTful web service which will return the referenced object.
isPartial (default: false)           xs:boolean              The isPartial, if true, indicates that only the relevant portion of the item scheme is being communicated. This is used in cases where a codelist is returned for a key family in the context of a constraint.
==================================== ======================= ==========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================

Element Documentation:

================= ====================== ==================================================================================================================================================================================
**Name**          **Type**               **Documentation**
================= ====================== ==================================================================================================================================================================================
com:Annotations   com:AnnotationsType    Annotations is a reusable element the provides for a collection of annotations. It has been made global so that restrictions of types that extend AnnotatableType my reference it.
com:Name          com:TextType           Name provides for a human-readable name for the object. This may be provided in multiple, parallel language-equivalent forms.
com:Description   com:TextType           Description provides for a longer human-readable description of the object. This may be provided in multiple, parallel language-equivalent forms.
ReportingCategory ReportingCategoryTyp e ReportingCateogry defines a reporting category, which is used to group structure usages into useful sub-packages.
================= ====================== ==================================================================================================================================================================================

**ReportingCategoryBaseType: **\ ReportingCategoryBaseType is an
abstract base type that serves as the basis for the
ReportingCategoryType.

Derivation:

| *com:AnnotableType* (extension) 
|    |image510|\ *IdentifiableType* (extension) 
|          |image511|\ *NameableType* (restriction) 
|                |image512|\ *ItemBaseType* (extension) 
|                      |image513|\ *ItemType* (restriction) 
|                            |image514|\ *ReportingCategoryBaseType*

Attributes:

id, urn?, uri?

Content:

com:Annotations?, com:Name+, com:Description*, ReportingCategory\*

Attribute Documentation:

======== ========== ==================================================================================================================================================================
**Name** **Type**   **Documentation**
======== ========== ==================================================================================================================================================================
id       com:IDType The id is the identifier for the object.
urn      xs:anyURI  The urn attribute holds a valid SDMX Registry URN (see SDMX Registry Specification for details).
uri      xs:anyURI  The uri attribute holds a URI that contains a link to a resource with additional information about the object, such as a web page. This uri is not a SDMX message.
======== ========== ==================================================================================================================================================================

Element Documentation:

================= ====================== ==================================================================================================================================================================================
**Name**          **Type**               **Documentation**
================= ====================== ==================================================================================================================================================================================
com:Annotations   com:AnnotationsType    Annotations is a reusable element the provides for a collection of annotations. It has been made global so that restrictions of types that extend AnnotatableType my reference it.
com:Name          com:TextType           Name provides for a human-readable name for the object. This may be provided in multiple, parallel language-equivalent forms.
com:Description   com:TextType           Description provides for a longer human-readable description of the object. This may be provided in multiple, parallel language-equivalent forms.
ReportingCategory ReportingCategoryTyp e ReportingCateogry defines a reporting category, which is used to group structure usages into useful sub-packages.
================= ====================== ==================================================================================================================================================================================

**ReportingCategoryType: **\ ReportingCategoryType describes the
structure of a reporting category, which groups structure usages into
useful sub-packages. Sub ordinate reporting categories can be nested
within the category definition.

Derivation:

| *com:AnnotableType* (extension) 
|    |image515|\ *IdentifiableType* (extension) 
|          |image516|\ *NameableType* (restriction) 
|                |image517|\ *ItemBaseType* (extension) 
|                      |image518|\ *ItemType* (restriction) 
|                            |image519|\ *ReportingCategoryBaseType* (extension) 
|                                  |image520|\ ReportingCategoryType

Attributes:

id, urn?, uri?

Content:

com:Annotations?, com:Name+, com:Description*, ReportingCategory*,
(StructuralMetadata\* \| ProvisioningMetadata*)

Attribute Documentation:

======== ========== ==================================================================================================================================================================
**Name** **Type**   **Documentation**
======== ========== ==================================================================================================================================================================
id       com:IDType The id is the identifier for the object.
urn      xs:anyURI  The urn attribute holds a valid SDMX Registry URN (see SDMX Registry Specification for details).
uri      xs:anyURI  The uri attribute holds a URI that contains a link to a resource with additional information about the object, such as a web page. This uri is not a SDMX message.
======== ========== ==================================================================================================================================================================

Element Documentation:

==================== ================================= =======================================================================================================================================================================================================================================================================
**Name**             **Type**                          **Documentation**
==================== ================================= =======================================================================================================================================================================================================================================================================
com:Annotations      com:AnnotationsType               Annotations is a reusable element the provides for a collection of annotations. It has been made global so that restrictions of types that extend AnnotatableType my reference it.
com:Name             com:TextType                      Name provides for a human-readable name for the object. This may be provided in multiple, parallel language-equivalent forms.
com:Description      com:TextType                      Description provides for a longer human-readable description of the object. This may be provided in multiple, parallel language-equivalent forms.
ReportingCategory    ReportingCategoryTyp e            ReportingCateogry defines a reporting category, which is used to group structure usages into useful sub-packages.
StructuralMetadata   com: StructureReferenceTy pe      StructuralMetadata provides a reference for data structure definition and metadata structure definition references which are grouped in the reporting category. It is assumed that all structural metadata objects referenced from a category will be of the same type.
ProvisioningMetadata com: StructureUsageRefere nceType ProvisioningMetadata provides a reference for dataflow and metadataflow references which are grouped in the reporting category. It is assumed that all provisioning metadata objects referenced from a category will be of the same type.
==================== ================================= =======================================================================================================================================================================================================================================================================

**StructureSetBaseType: **\ StructureSetBaseType is an abstract base
type that forms the basis for the StructureSetType.

Derivation:

| *com:AnnotableType* (extension) 
|    |image521|\ *IdentifiableType* (extension) 
|          |image522|\ *NameableType* (extension) 
|                |image523|\ *VersionableType* (restriction) 
|                      |image524|\ *MaintainableBaseType* (extension) 
|                            |image525|\ *MaintainableType* (restriction) 
|                                  |image526|\ *StructureSetBaseType*

Attributes:

id, urn?, uri?, version?, validFrom?, validTo?, agencyID, isFinal?,
isExternalReference?, serviceURL?, structureURL?

Content:

com:Annotations?, com:Name+, com:Description\*

Attribute Documentation:

==================================== ======================= ==========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                             **Type**                **Documentation**
==================================== ======================= ==========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
id                                   com:IDType              The id is the identifier for the object.
urn                                  xs:anyURI               The urn attribute holds a valid SDMX Registry URN (see SDMX Registry Specification for details).
uri                                  xs:anyURI               The uri attribute holds a URI that contains a link to a resource with additional information about the object, such as a web page. This uri is not a SDMX message.
version (default: 1.0)               com:VersionType         This version attribute holds a version number in the format of #[.#]+ (see common:VersionType definition for details). If not supplied, the version number is defaulted to 1.0.
validFrom                            xs:dateTime             The validFrom attribute provides the inclusive start date for providing supplemental validity information about the version.
validTo                              xs:dateTime             The validTo attribute provides the inclusive end date for providing supplemental validity information about the version.
agencyID                             com: NestedNCNameIDType The agencyID must be provided, and identifies the maintenance agency of the object.
isFinal (default: false)             xs:boolean              The isFinal attribute indicates whether the object is unchangeable without versioning. If the value is true, the object must be versioned upon change. If the final attribute is not supplied, then the object is assumed not to be final. Note that all production objects must be final.
isExternalReference (default: false) xs:boolean              The isExternalReference attribute, if true, indicates that the actual object is not defined the corresponding element, rather its full details are defined elsewhere - indicated by either the registryURL, the repositoryURL, or the structureURL. The purpose of this is so that each structure message does not have to redefine object that are already defined elsewhere. If the isExternalReference attribute is not set, then it is assumed to be false, and the object should contain the full definition of its contents. If more than one of the registryURL, the repositoryURL, and the structureURL are supplied, then the application processing the object can choose the method it finds best suited to retrieve the details of the object.
serviceURL                           xs:anyURI               The serviceURL attribute indicates the URL of an SDMX SOAP web service from which the details of the object can be retrieved. Note that this can be a registry or and SDMX structural metadata repository, as they both implement that same web service interface.
structureURL                         xs:anyURI               The structureURL attribute indicates the URL of a SDMX-ML structure message (in the same version as the source document) in which the externally referenced object is contained. Note that this may be a URL of an SDMX RESTful web service which will return the referenced object.
==================================== ======================= ==========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================

Element Documentation:

=============== =================== ==================================================================================================================================================================================
**Name**        **Type**            **Documentation**
=============== =================== ==================================================================================================================================================================================
com:Annotations com:AnnotationsType Annotations is a reusable element the provides for a collection of annotations. It has been made global so that restrictions of types that extend AnnotatableType my reference it.
com:Name        com:TextType        Name provides for a human-readable name for the object. This may be provided in multiple, parallel language-equivalent forms.
com:Description com:TextType        Description provides for a longer human-readable description of the object. This may be provided in multiple, parallel language-equivalent forms.
=============== =================== ==================================================================================================================================================================================

**StructureSetType: **\ StructureSetType describes the structure of a
structure set. It allows components in one structure, structure usage,
or item scheme to be mapped to components in another structural
component of the same type.

Derivation:

| *com:AnnotableType* (extension) 
|    |image527|\ *IdentifiableType* (extension) 
|          |image528|\ *NameableType* (extension) 
|                |image529|\ *VersionableType* (restriction) 
|                      |image530|\ *MaintainableBaseType* (extension) 
|                            |image531|\ *MaintainableType* (restriction) 
|                                  |image532|\ *StructureSetBaseType* (extension) 
|                                        |image533|\ StructureSetType

Attributes:

id, urn?, uri?, version?, validFrom?, validTo?, agencyID, isFinal?,
isExternalReference?, serviceURL?, structureURL?

Content:

com:Annotations?, com:Name+, com:Description*, RelatedStructure*,
(OrganisationSchemeMap \| CategorySchemeMap \| CodelistMap \|
ConceptSchemeMap \| ReportingTaxonomyMap \| HybridCodelistMap \|
StructureMap)\*

Attribute Documentation:

==================================== ======================= ==========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                             **Type**                **Documentation**
==================================== ======================= ==========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
id                                   com:IDType              The id is the identifier for the object.
urn                                  xs:anyURI               The urn attribute holds a valid SDMX Registry URN (see SDMX Registry Specification for details).
uri                                  xs:anyURI               The uri attribute holds a URI that contains a link to a resource with additional information about the object, such as a web page. This uri is not a SDMX message.
version (default: 1.0)               com:VersionType         This version attribute holds a version number in the format of #[.#]+ (see common:VersionType definition for details). If not supplied, the version number is defaulted to 1.0.
validFrom                            xs:dateTime             The validFrom attribute provides the inclusive start date for providing supplemental validity information about the version.
validTo                              xs:dateTime             The validTo attribute provides the inclusive end date for providing supplemental validity information about the version.
agencyID                             com: NestedNCNameIDType The agencyID must be provided, and identifies the maintenance agency of the object.
isFinal (default: false)             xs:boolean              The isFinal attribute indicates whether the object is unchangeable without versioning. If the value is true, the object must be versioned upon change. If the final attribute is not supplied, then the object is assumed not to be final. Note that all production objects must be final.
isExternalReference (default: false) xs:boolean              The isExternalReference attribute, if true, indicates that the actual object is not defined the corresponding element, rather its full details are defined elsewhere - indicated by either the registryURL, the repositoryURL, or the structureURL. The purpose of this is so that each structure message does not have to redefine object that are already defined elsewhere. If the isExternalReference attribute is not set, then it is assumed to be false, and the object should contain the full definition of its contents. If more than one of the registryURL, the repositoryURL, and the structureURL are supplied, then the application processing the object can choose the method it finds best suited to retrieve the details of the object.
serviceURL                           xs:anyURI               The serviceURL attribute indicates the URL of an SDMX SOAP web service from which the details of the object can be retrieved. Note that this can be a registry or and SDMX structural metadata repository, as they both implement that same web service interface.
structureURL                         xs:anyURI               The structureURL attribute indicates the URL of a SDMX-ML structure message (in the same version as the source document) in which the externally referenced object is contained. Note that this may be a URL of an SDMX RESTful web service which will return the referenced object.
==================================== ======================= ==========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================

Element Documentation:

====================== =================================== ==============================================================================================================================================================================================================================================================================================
**Name**               **Type**                            **Documentation**
====================== =================================== ==============================================================================================================================================================================================================================================================================================
com:Annotations        com:AnnotationsType                 Annotations is a reusable element the provides for a collection of annotations. It has been made global so that restrictions of types that extend AnnotatableType my reference it.
com:Name               com:TextType                        Name provides for a human-readable name for the object. This may be provided in multiple, parallel language-equivalent forms.
com:Description        com:TextType                        Description provides for a longer human-readable description of the object. This may be provided in multiple, parallel language-equivalent forms.
RelatedStructure       com: StructureOrUsageRefe renceType RelatedStructures contains references to structures (key families and metadata structure definitions) and structure usages (data flows and metadata flows) to indicate that a semantic relationship exist between them. The details of these relationships can be found in the structure maps.
OrganisationSchemeMa p OrganisationSchemeMa pType          OrganisationSchemeMap links a source and target organisations from different schemes where there is a semantic equivalence between them. Organisations are mapped without regard to role.
CategorySchemeMap      CategorySchemeMapTyp e              CategorySchemeMap links a source and target categories from different schemes where there is a semantic equivalence between them.
CodelistMap            CodelistMapType                     CodelistMap links a source and target codes from different lists where there is a semantic equivalence between them.
ConceptSchemeMap       ConceptSchemeMapType                ConceptSchemeMap links a source and target concepts from different schemes where there is a semantic equivalence between them.
ReportingTaxonomyMap   ReportingTaxonomyMap Type           ReportingTaxonomyMap links a source and target reporting categories from different taxonomies where there is a semantic equivalence between them.
HybridCodelistMap      HybridCodelistMapTyp e              HybridCodelistMap links a source and target codes from different codelists, which may be hierarchical or flat, where there is a semantic equivalence between them.
StructureMap           StructureMapType                    StructureMap maps components from one structure to components to another structure, and can describe how the value of the components are related.
====================== =================================== ==============================================================================================================================================================================================================================================================================================

**ItemSchemeMapBaseType: **\ ItemSchemeMapBaseType is an abstract base
type which forms the basis for the ItemSchemeMapType.

Derivation:

| *com:AnnotableType* (extension) 
|    |image534|\ *IdentifiableType* (extension) 
|          |image535|\ *NameableType* (restriction) 
|                |image536|\ *ItemSchemeMapBaseType*

Attributes:

id, urn?, uri?

Content:

com:Annotations?, com:Name+, com:Description\*

Attribute Documentation:

======== ========== ==================================================================================================================================================================
**Name** **Type**   **Documentation**
======== ========== ==================================================================================================================================================================
id       com:IDType The id is the identifier for the object.
urn      xs:anyURI  The urn attribute holds a valid SDMX Registry URN (see SDMX Registry Specification for details).
uri      xs:anyURI  The uri attribute holds a URI that contains a link to a resource with additional information about the object, such as a web page. This uri is not a SDMX message.
======== ========== ==================================================================================================================================================================

Element Documentation:

=============== =================== ==================================================================================================================================================================================
**Name**        **Type**            **Documentation**
=============== =================== ==================================================================================================================================================================================
com:Annotations com:AnnotationsType Annotations is a reusable element the provides for a collection of annotations. It has been made global so that restrictions of types that extend AnnotatableType my reference it.
com:Name        com:TextType        Name provides for a human-readable name for the object. This may be provided in multiple, parallel language-equivalent forms.
com:Description com:TextType        Description provides for a longer human-readable description of the object. This may be provided in multiple, parallel language-equivalent forms.
=============== =================== ==================================================================================================================================================================================

**ItemSchemeMapType: **\ ItemSchemeMapType is an abstract base type
which forms the basis for mapping items between item schemes of the same
type.

Derivation:

| *com:AnnotableType* (extension) 
|    |image537|\ *IdentifiableType* (extension) 
|          |image538|\ *NameableType* (restriction) 
|                |image539|\ *ItemSchemeMapBaseType* (extension) 
|                      |image540|\ *ItemSchemeMapType*

Attributes:

id, urn?, uri?

Content:

com:Annotations?, com:Name+, com:Description*, Source,
Target, \ *ItemAssociation+*

Attribute Documentation:

======== ========== ==================================================================================================================================================================
**Name** **Type**   **Documentation**
======== ========== ==================================================================================================================================================================
id       com:IDType The id is the identifier for the object.
urn      xs:anyURI  The urn attribute holds a valid SDMX Registry URN (see SDMX Registry Specification for details).
uri      xs:anyURI  The uri attribute holds a URI that contains a link to a resource with additional information about the object, such as a web page. This uri is not a SDMX message.
======== ========== ==================================================================================================================================================================

Element Documentation:

================= =================================== ==================================================================================================================================================================================
**Name**          **Type**                            **Documentation**
================= =================================== ==================================================================================================================================================================================
com:Annotations   com:AnnotationsType                 Annotations is a reusable element the provides for a collection of annotations. It has been made global so that restrictions of types that extend AnnotatableType my reference it.
com:Name          com:TextType                        Name provides for a human-readable name for the object. This may be provided in multiple, parallel language-equivalent forms.
com:Description   com:TextType                        Description provides for a longer human-readable description of the object. This may be provided in multiple, parallel language-equivalent forms.
Source            *com: ItemSchemeReferenceB aseType* Source provides a reference to the item scheme which items are mapped from.
Target            *com: ItemSchemeReferenceB aseType* Target provides a reference to the item scheme which items are mapped to.
*ItemAssociation* *ItemAssociationType*               ItemAssociation is an abstract description of the relation between two items for the purpose of mapping.
================= =================================== ==================================================================================================================================================================================

**ItemAssociationType: **\ ItemAssociationType is an abstract type which
defines the relationship between two items from the source and target
item schemes of an item scheme map.

Derivation:

| *com:AnnotableType* (extension) 
|    |image541|\ *ItemAssociationType*

Content:

com:Annotations?, Source, Target

Element Documentation:

=============== ============================== ==================================================================================================================================================================================
**Name**        **Type**                       **Documentation**
=============== ============================== ==================================================================================================================================================================================
com:Annotations com:AnnotationsType            Annotations is a reusable element the provides for a collection of annotations. It has been made global so that restrictions of types that extend AnnotatableType my reference it.
Source          *com: LocalItemReferenceTy pe* Source provides a local reference (id only) to an item from the source item scheme in the item scheme map which is being mapped to another item.
Target          *com: LocalItemReferenceTy pe* Target provides a local reference (id only) to an item from the target item scheme in the item scheme map which is being mapped from another item.
=============== ============================== ==================================================================================================================================================================================

**OrganisationSchemeMapType: **\ OrganisationSchemeMapType defines the
structure of a map which identifies relationships between organisations
in different organisation schemes.

Derivation:

| *com:AnnotableType* (extension) 
|    |image542|\ *IdentifiableType* (extension) 
|          |image543|\ *NameableType* (restriction) 
|                |image544|\ *ItemSchemeMapBaseType* (extension) 
|                      |image545|\ *ItemSchemeMapType* (restriction) 
|                            |image546|\ OrganisationSchemeMapType

Attributes:

id, urn?, uri?

Content:

com:Annotations?, com:Name+, com:Description*, Source, Target,
OrganisationMap+

Attribute Documentation:

======== ========== ==================================================================================================================================================================
**Name** **Type**   **Documentation**
======== ========== ==================================================================================================================================================================
id       com:IDType The id is the identifier for the object.
urn      xs:anyURI  The urn attribute holds a valid SDMX Registry URN (see SDMX Registry Specification for details).
uri      xs:anyURI  The uri attribute holds a URI that contains a link to a resource with additional information about the object, such as a web page. This uri is not a SDMX message.
======== ========== ==================================================================================================================================================================

Element Documentation:

=============== ===================================== ==================================================================================================================================================================================
**Name**        **Type**                              **Documentation**
=============== ===================================== ==================================================================================================================================================================================
com:Annotations com:AnnotationsType                   Annotations is a reusable element the provides for a collection of annotations. It has been made global so that restrictions of types that extend AnnotatableType my reference it.
com:Name        com:TextType                          Name provides for a human-readable name for the object. This may be provided in multiple, parallel language-equivalent forms.
com:Description com:TextType                          Description provides for a longer human-readable description of the object. This may be provided in multiple, parallel language-equivalent forms.
Source          com: OrganisationSchemeRe ferenceType Source provides a reference to the item scheme which items are mapped from.
Target          com: OrganisationSchemeRe ferenceType Target provides a reference to the item scheme which items are mapped to.
OrganisationMap OrganisationMapType                   OrganisationMap relates a source organisation to a target organisation.
=============== ===================================== ==================================================================================================================================================================================

**OrganisationMapType: **\ OrganisationMapType defines the structure for
mapping two organisations. A local reference is provided both the source
and target organisation.

Derivation:

| *com:AnnotableType* (extension) 
|    |image547|\ *ItemAssociationType* (restriction) 
|          |image548|\ OrganisationMapType

Content:

com:Annotations?, Source, Target

Element Documentation:

=============== ==================================== ==================================================================================================================================================================================
**Name**        **Type**                             **Documentation**
=============== ==================================== ==================================================================================================================================================================================
com:Annotations com:AnnotationsType                  Annotations is a reusable element the provides for a collection of annotations. It has been made global so that restrictions of types that extend AnnotatableType my reference it.
Source          com: LocalOrganisationRef erenceType Source provides a local reference (id only) to an item from the source item scheme in the item scheme map which is being mapped to another item.
Target          com: LocalOrganisationRef erenceType Target provides a local reference (id only) to an item from the target item scheme in the item scheme map which is being mapped from another item.
=============== ==================================== ==================================================================================================================================================================================

**CategorySchemeMapType: **\ CategorySchemeMapType defines the structure
of a map which identifies relationships between categories in different
category schemes.

Derivation:

| *com:AnnotableType* (extension) 
|    |image549|\ *IdentifiableType* (extension) 
|          |image550|\ *NameableType* (restriction) 
|                |image551|\ *ItemSchemeMapBaseType* (extension) 
|                      |image552|\ *ItemSchemeMapType* (restriction) 
|                            |image553|\ CategorySchemeMapType

Attributes:

id, urn?, uri?

Content:

com:Annotations?, com:Name+, com:Description*, Source, Target,
CategoryMap+

Attribute Documentation:

======== ========== ==================================================================================================================================================================
**Name** **Type**   **Documentation**
======== ========== ==================================================================================================================================================================
id       com:IDType The id is the identifier for the object.
urn      xs:anyURI  The urn attribute holds a valid SDMX Registry URN (see SDMX Registry Specification for details).
uri      xs:anyURI  The uri attribute holds a URI that contains a link to a resource with additional information about the object, such as a web page. This uri is not a SDMX message.
======== ========== ==================================================================================================================================================================

Element Documentation:

=============== ================================= ==================================================================================================================================================================================
**Name**        **Type**                          **Documentation**
=============== ================================= ==================================================================================================================================================================================
com:Annotations com:AnnotationsType               Annotations is a reusable element the provides for a collection of annotations. It has been made global so that restrictions of types that extend AnnotatableType my reference it.
com:Name        com:TextType                      Name provides for a human-readable name for the object. This may be provided in multiple, parallel language-equivalent forms.
com:Description com:TextType                      Description provides for a longer human-readable description of the object. This may be provided in multiple, parallel language-equivalent forms.
Source          com: CategorySchemeRefere nceType Source provides a reference to the item scheme which items are mapped from.
Target          com: CategorySchemeRefere nceType Target provides a reference to the item scheme which items are mapped to.
CategoryMap     CategoryMapType                   CategoryMap defines the structure of a map which identifies relationships between categories in different category schemes.
=============== ================================= ==================================================================================================================================================================================

**CategoryMapType: **\ CategoryMapType defines the structure for mapping
two categories. A local reference is provided both the source and target
category.

Derivation:

| *com:AnnotableType* (extension) 
|    |image554|\ *ItemAssociationType* (restriction) 
|          |image555|\ CategoryMapType

Content:

com:Annotations?, Source, Target

Element Documentation:

=============== ================================ ==================================================================================================================================================================================
**Name**        **Type**                         **Documentation**
=============== ================================ ==================================================================================================================================================================================
com:Annotations com:AnnotationsType              Annotations is a reusable element the provides for a collection of annotations. It has been made global so that restrictions of types that extend AnnotatableType my reference it.
Source          com: LocalCategoryReferen ceType Source provides a local reference (id only) to an item from the source item scheme in the item scheme map which is being mapped to another item.
Target          com: LocalCategoryReferen ceType Target provides a local reference (id only) to an item from the target item scheme in the item scheme map which is being mapped from another item.
=============== ================================ ==================================================================================================================================================================================

**CodelistMapType: **\ CodelistMapType defines the structure of a map
which identifies relationships between codes in different codelists.

Derivation:

| *com:AnnotableType* (extension) 
|    |image556|\ *IdentifiableType* (extension) 
|          |image557|\ *NameableType* (restriction) 
|                |image558|\ *ItemSchemeMapBaseType* (extension) 
|                      |image559|\ *ItemSchemeMapType* (restriction) 
|                            |image560|\ CodelistMapType

Attributes:

id, urn?, uri?

Content:

com:Annotations?, com:Name+, com:Description*, Source, Target, CodeMap+

Attribute Documentation:

======== ========== ==================================================================================================================================================================
**Name** **Type**   **Documentation**
======== ========== ==================================================================================================================================================================
id       com:IDType The id is the identifier for the object.
urn      xs:anyURI  The urn attribute holds a valid SDMX Registry URN (see SDMX Registry Specification for details).
uri      xs:anyURI  The uri attribute holds a URI that contains a link to a resource with additional information about the object, such as a web page. This uri is not a SDMX message.
======== ========== ==================================================================================================================================================================

Element Documentation:

=============== =========================== ==================================================================================================================================================================================
**Name**        **Type**                    **Documentation**
=============== =========================== ==================================================================================================================================================================================
com:Annotations com:AnnotationsType         Annotations is a reusable element the provides for a collection of annotations. It has been made global so that restrictions of types that extend AnnotatableType my reference it.
com:Name        com:TextType                Name provides for a human-readable name for the object. This may be provided in multiple, parallel language-equivalent forms.
com:Description com:TextType                Description provides for a longer human-readable description of the object. This may be provided in multiple, parallel language-equivalent forms.
Source          com: CodelistReferenceTyp e Source provides a reference to the item scheme which items are mapped from.
Target          com: CodelistReferenceTyp e Target provides a reference to the item scheme which items are mapped to.
CodeMap         CodeMapType                 CodeMap defines the structure of a map which identifies relationships between codes in different codelists.
=============== =========================== ==================================================================================================================================================================================

**CodeMapType: **\ CodeMapType defines the structure for mapping two
codes. A local reference is provided both the source and target code.

Derivation:

| *com:AnnotableType* (extension) 
|    |image561|\ *ItemAssociationType* (restriction) 
|          |image562|\ CodeMapType

Content:

com:Annotations?, Source, Target

Element Documentation:

=============== ============================ ==================================================================================================================================================================================
**Name**        **Type**                     **Documentation**
=============== ============================ ==================================================================================================================================================================================
com:Annotations com:AnnotationsType          Annotations is a reusable element the provides for a collection of annotations. It has been made global so that restrictions of types that extend AnnotatableType my reference it.
Source          com: LocalCodeReferenceTy pe Source provides a local reference (id only) to an item from the source item scheme in the item scheme map which is being mapped to another item.
Target          com: LocalCodeReferenceTy pe Target provides a local reference (id only) to an item from the target item scheme in the item scheme map which is being mapped from another item.
=============== ============================ ==================================================================================================================================================================================

**ConceptSchemeMapType: **\ ConceptSchemeMapType defines the structure
of a map which identifies relationships between concepts in different
concept schemes.

Derivation:

| *com:AnnotableType* (extension) 
|    |image563|\ *IdentifiableType* (extension) 
|          |image564|\ *NameableType* (restriction) 
|                |image565|\ *ItemSchemeMapBaseType* (extension) 
|                      |image566|\ *ItemSchemeMapType* (restriction) 
|                            |image567|\ ConceptSchemeMapType

Attributes:

id, urn?, uri?

Content:

com:Annotations?, com:Name+, com:Description*, Source, Target,
ConceptMap+

Attribute Documentation:

======== ========== ==================================================================================================================================================================
**Name** **Type**   **Documentation**
======== ========== ==================================================================================================================================================================
id       com:IDType The id is the identifier for the object.
urn      xs:anyURI  The urn attribute holds a valid SDMX Registry URN (see SDMX Registry Specification for details).
uri      xs:anyURI  The uri attribute holds a URI that contains a link to a resource with additional information about the object, such as a web page. This uri is not a SDMX message.
======== ========== ==================================================================================================================================================================

Element Documentation:

=============== ================================ ==================================================================================================================================================================================
**Name**        **Type**                         **Documentation**
=============== ================================ ==================================================================================================================================================================================
com:Annotations com:AnnotationsType              Annotations is a reusable element the provides for a collection of annotations. It has been made global so that restrictions of types that extend AnnotatableType my reference it.
com:Name        com:TextType                     Name provides for a human-readable name for the object. This may be provided in multiple, parallel language-equivalent forms.
com:Description com:TextType                     Description provides for a longer human-readable description of the object. This may be provided in multiple, parallel language-equivalent forms.
Source          com: ConceptSchemeReferen ceType Source provides a reference to the item scheme which items are mapped from.
Target          com: ConceptSchemeReferen ceType Target provides a reference to the item scheme which items are mapped to.
ConceptMap      ConceptMapType                   ConceptMap defines the structure of a map which identifies relationships between concepts in different concept schemes.
=============== ================================ ==================================================================================================================================================================================

**ConceptMapType: **\ ConceptMapType defines the structure for mapping
two concepts. A local reference is provided both the source and target
concept.

Derivation:

| *com:AnnotableType* (extension) 
|    |image568|\ *ItemAssociationType* (restriction) 
|          |image569|\ ConceptMapType

Content:

com:Annotations?, Source, Target

Element Documentation:

=============== =============================== ==================================================================================================================================================================================
**Name**        **Type**                        **Documentation**
=============== =============================== ==================================================================================================================================================================================
com:Annotations com:AnnotationsType             Annotations is a reusable element the provides for a collection of annotations. It has been made global so that restrictions of types that extend AnnotatableType my reference it.
Source          com: LocalConceptReferenc eType Source provides a local reference (id only) to an item from the source item scheme in the item scheme map which is being mapped to another item.
Target          com: LocalConceptReferenc eType Target provides a local reference (id only) to an item from the target item scheme in the item scheme map which is being mapped from another item.
=============== =============================== ==================================================================================================================================================================================

**ReportingTaxonomyMapType: **\ ReportingTaxonomyMapType defines the
structure of a map which identifies relationships between reporting
categories in different reporting taxonomies.

Derivation:

| *com:AnnotableType* (extension) 
|    |image570|\ *IdentifiableType* (extension) 
|          |image571|\ *NameableType* (restriction) 
|                |image572|\ *ItemSchemeMapBaseType* (extension) 
|                      |image573|\ *ItemSchemeMapType* (restriction) 
|                            |image574|\ ReportingTaxonomyMapType

Attributes:

id, urn?, uri?

Content:

com:Annotations?, com:Name+, com:Description*, Source, Target,
ReportingCategoryMap+

Attribute Documentation:

======== ========== ==================================================================================================================================================================
**Name** **Type**   **Documentation**
======== ========== ==================================================================================================================================================================
id       com:IDType The id is the identifier for the object.
urn      xs:anyURI  The urn attribute holds a valid SDMX Registry URN (see SDMX Registry Specification for details).
uri      xs:anyURI  The uri attribute holds a URI that contains a link to a resource with additional information about the object, such as a web page. This uri is not a SDMX message.
======== ========== ==================================================================================================================================================================

Element Documentation:

==================== ==================================== ==================================================================================================================================================================================
**Name**             **Type**                             **Documentation**
==================== ==================================== ==================================================================================================================================================================================
com:Annotations      com:AnnotationsType                  Annotations is a reusable element the provides for a collection of annotations. It has been made global so that restrictions of types that extend AnnotatableType my reference it.
com:Name             com:TextType                         Name provides for a human-readable name for the object. This may be provided in multiple, parallel language-equivalent forms.
com:Description      com:TextType                         Description provides for a longer human-readable description of the object. This may be provided in multiple, parallel language-equivalent forms.
Source               com: ReportingTaxonomyRef erenceType Source provides a reference to the item scheme which items are mapped from.
Target               com: ReportingTaxonomyRef erenceType Target provides a reference to the item scheme which items are mapped to.
ReportingCategoryMap ReportingCategoryMap Type            ReportingCategoryMap defines the structure of a map which identifies relationships between reporting categories in different reporting taxonomies.
==================== ==================================== ==================================================================================================================================================================================

**ReportingCategoryMapType: **\ ReportingCategoryMapType defines the
structure for mapping two reporting categories. A local reference is
provided both the source and target category.

Derivation:

| *com:AnnotableType* (extension) 
|    |image575|\ *ItemAssociationType* (restriction) 
|          |image576|\ ReportingCategoryMapType

Content:

com:Annotations?, Source, Target

Element Documentation:

=============== ========================================= ==================================================================================================================================================================================
**Name**        **Type**                                  **Documentation**
=============== ========================================= ==================================================================================================================================================================================
com:Annotations com:AnnotationsType                       Annotations is a reusable element the provides for a collection of annotations. It has been made global so that restrictions of types that extend AnnotatableType my reference it.
Source          com: LocalReportingCatego ryReferenceType Source provides a local reference (id only) to an item from the source item scheme in the item scheme map which is being mapped to another item.
Target          com: LocalReportingCatego ryReferenceType Target provides a local reference (id only) to an item from the target item scheme in the item scheme map which is being mapped from another item.
=============== ========================================= ==================================================================================================================================================================================

**HybridCodelistMapBaseType: **\ HybridCodelistMapBaseType is an
abstract base type which forms the basis for the HybridCodelistMapType.

Derivation:

| *com:AnnotableType* (extension) 
|    |image577|\ *IdentifiableType* (extension) 
|          |image578|\ *NameableType* (restriction) 
|                |image579|\ *HybridCodelistMapBaseType*

Attributes:

id, urn?, uri?

Content:

com:Annotations?, com:Name+, com:Description\*

Attribute Documentation:

======== ========== ==================================================================================================================================================================
**Name** **Type**   **Documentation**
======== ========== ==================================================================================================================================================================
id       com:IDType The id is the identifier for the object.
urn      xs:anyURI  The urn attribute holds a valid SDMX Registry URN (see SDMX Registry Specification for details).
uri      xs:anyURI  The uri attribute holds a URI that contains a link to a resource with additional information about the object, such as a web page. This uri is not a SDMX message.
======== ========== ==================================================================================================================================================================

Element Documentation:

=============== =================== ==================================================================================================================================================================================
**Name**        **Type**            **Documentation**
=============== =================== ==================================================================================================================================================================================
com:Annotations com:AnnotationsType Annotations is a reusable element the provides for a collection of annotations. It has been made global so that restrictions of types that extend AnnotatableType my reference it.
com:Name        com:TextType        Name provides for a human-readable name for the object. This may be provided in multiple, parallel language-equivalent forms.
com:Description com:TextType        Description provides for a longer human-readable description of the object. This may be provided in multiple, parallel language-equivalent forms.
=============== =================== ==================================================================================================================================================================================

**HybridCodelistMapType: **\ HybridCodelistMapType defines the structure
of a map which relates codes (possibly hierarchical) from different code
lists.

Derivation:

| *com:AnnotableType* (extension) 
|    |image580|\ *IdentifiableType* (extension) 
|          |image581|\ *NameableType* (restriction) 
|                |image582|\ *HybridCodelistMapBaseType* (extension) 
|                      |image583|\ HybridCodelistMapType

Attributes:

id, urn?, uri?

Content:

com:Annotations?, com:Name+, com:Description*, Source, Target,
HybridCodeMap+

Attribute Documentation:

======== ========== ==================================================================================================================================================================
**Name** **Type**   **Documentation**
======== ========== ==================================================================================================================================================================
id       com:IDType The id is the identifier for the object.
urn      xs:anyURI  The urn attribute holds a valid SDMX Registry URN (see SDMX Registry Specification for details).
uri      xs:anyURI  The uri attribute holds a URI that contains a link to a resource with additional information about the object, such as a web page. This uri is not a SDMX message.
======== ========== ==================================================================================================================================================================

Element Documentation:

=============== ============================== ==================================================================================================================================================================================
**Name**        **Type**                       **Documentation**
=============== ============================== ==================================================================================================================================================================================
com:Annotations com:AnnotationsType            Annotations is a reusable element the provides for a collection of annotations. It has been made global so that restrictions of types that extend AnnotatableType my reference it.
com:Name        com:TextType                   Name provides for a human-readable name for the object. This may be provided in multiple, parallel language-equivalent forms.
com:Description com:TextType                   Description provides for a longer human-readable description of the object. This may be provided in multiple, parallel language-equivalent forms.
Source          com: AnyCodelistReference Type Source provides a reference to either a codelist or a hierarchical codelist, from which the codes are to be mapped.
Target          com: AnyCodelistReference Type Target provides a reference to either a codelist or a hierarchical codelist, to which the source codes are to be mapped.
HybridCodeMap   HybridCodeMapType              HybridCodeMap defines the relationship of a code in the source list to code in the target list.
=============== ============================== ==================================================================================================================================================================================

**HybridCodeMapType: **\ CodeMapType defines the structure for
associating a code from a source codelist to a code in a target
codelist. Note that either of these may come from a hierarchical
codelist.

Derivation:

| *com:AnnotableType* (extension) 
|    |image584|\ HybridCodeMapType

Content:

com:Annotations?, Source, Target

Element Documentation:

=============== =============================== ==========================================================================================================================================================================================================
**Name**        **Type**                        **Documentation**
=============== =============================== ==========================================================================================================================================================================================================
com:Annotations com:AnnotationsType             Annotations is a reusable element the provides for a collection of annotations. It has been made global so that restrictions of types that extend AnnotatableType my reference it.
Source          com: AnyLocalCodeReferenc eType Source provides a local reference to the code which is to be mapped. If this code is from a hierarchical codelist, a reference to the hierarchy in which it is defined must also be provided.
Target          com: AnyLocalCodeReferenc eType Target provides a local reference to the code to which the source code is mapped. If this code is from a hierarchical codelist, a reference to the hierarchy in which it is defined must also be provided.
=============== =============================== ==========================================================================================================================================================================================================

**StructureMapBaseType: **\ StructureMapBaseType is an abstract base
type which forms the basis for the StructureMapType.

Derivation:

| *com:AnnotableType* (extension) 
|    |image585|\ *IdentifiableType* (extension) 
|          |image586|\ *NameableType* (restriction) 
|                |image587|\ *StructureMapBaseType*

Attributes:

id, urn?, uri?

Content:

com:Annotations?, com:Name+, com:Description\*

Attribute Documentation:

======== ========== ==================================================================================================================================================================
**Name** **Type**   **Documentation**
======== ========== ==================================================================================================================================================================
id       com:IDType The id is the identifier for the object.
urn      xs:anyURI  The urn attribute holds a valid SDMX Registry URN (see SDMX Registry Specification for details).
uri      xs:anyURI  The uri attribute holds a URI that contains a link to a resource with additional information about the object, such as a web page. This uri is not a SDMX message.
======== ========== ==================================================================================================================================================================

Element Documentation:

=============== =================== ==================================================================================================================================================================================
**Name**        **Type**            **Documentation**
=============== =================== ==================================================================================================================================================================================
com:Annotations com:AnnotationsType Annotations is a reusable element the provides for a collection of annotations. It has been made global so that restrictions of types that extend AnnotatableType my reference it.
com:Name        com:TextType        Name provides for a human-readable name for the object. This may be provided in multiple, parallel language-equivalent forms.
com:Description com:TextType        Description provides for a longer human-readable description of the object. This may be provided in multiple, parallel language-equivalent forms.
=============== =================== ==================================================================================================================================================================================

**StructureMapType: **\ StructureMapType defines the structure for
mapping components of one structure to components of another structure.
A structure may be referenced directly meaning the map applies wherever
the structure is used, or it may be a reference via a structure usage
meaning the map only applies within the context of that usage. Using the
related structures, one can make extrapolations between maps. For
example, if key families, A, B, and C, are all grouped in a related
structures container, then a map from key family A to C and a map from
key family B to C could be used to infer a relation between key family A
to C.

Derivation:

| *com:AnnotableType* (extension) 
|    |image588|\ *IdentifiableType* (extension) 
|          |image589|\ *NameableType* (restriction) 
|                |image590|\ *StructureMapBaseType* (extension) 
|                      |image591|\ StructureMapType

Attributes:

id, urn?, uri?, isExtension?

Content:

com:Annotations?, com:Name+, com:Description*, Source, Target,
ComponentMap

Attribute Documentation:

============================ ========== ========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
**Name**                     **Type**   **Documentation**
============================ ========== ========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
id                           com:IDType The id is the identifier for the object.
urn                          xs:anyURI  The urn attribute holds a valid SDMX Registry URN (see SDMX Registry Specification for details).
uri                          xs:anyURI  The uri attribute holds a URI that contains a link to a resource with additional information about the object, such as a web page. This uri is not a SDMX message.
isExtension (default: false) xs:boolean The isExtension attribute, when true, indicates that the target structure definition inherits all properties of the referenced structure definition, and may have additional components. Note that this attribute may only be set to true if the structure map has a source structure and a target structure of either two key families or two metadata structure definitions. It is not possible inherit the underlying concepts of components between the two type of structures using this mechanism.
============================ ========== ========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================

Element Documentation:

=============== =================================== =============================================================================================================================================================================================================
**Name**        **Type**                            **Documentation**
=============== =================================== =============================================================================================================================================================================================================
com:Annotations com:AnnotationsType                 Annotations is a reusable element the provides for a collection of annotations. It has been made global so that restrictions of types that extend AnnotatableType my reference it.
com:Name        com:TextType                        Name provides for a human-readable name for the object. This may be provided in multiple, parallel language-equivalent forms.
com:Description com:TextType                        Description provides for a longer human-readable description of the object. This may be provided in multiple, parallel language-equivalent forms.
Source          com: StructureOrUsageRefe renceType Source provides a reference to a structure (data or metadata) or a structure usage (dataflow or metadataflow) from which components defined by the actual structure are to mapped.
Target          com: StructureOrUsageRefe renceType Target provides a reference to a structure (data or metadata) or a structure usage (dataflow or metadataflow) to which components from the source are to mapped.
ComponentMap    ComponentMapType                    ComponentMap defines the relationship between the components of the source and target structures, including information on how the value from the source component relates to values in the target component.
=============== =================================== =============================================================================================================================================================================================================

**ComponentMapType: **\ ComponentMapType defines the structure for
relating a component in a source structure to a component in a target
structure.

Derivation:

| *com:AnnotableType* (extension) 
|    |image592|\ ComponentMapType

Content:

com:Annotations?, Source, Target, RepresentationMapping?

Element Documentation:

====================== ============================================== ===================================================================================================================================================================================================================================================================================================
**Name**               **Type**                                       **Documentation**
====================== ============================================== ===================================================================================================================================================================================================================================================================================================
com:Annotations        com:AnnotationsType                            Annotations is a reusable element the provides for a collection of annotations. It has been made global so that restrictions of types that extend AnnotatableType my reference it.
Source                 com: LocalComponentListCo mponentReferenceType
Target                 com: LocalComponentListCo mponentReferenceType
RepresentationMappin g RepresentationMapTyp e                         RepresentationMapping describes the mapping rules to map the value of the source component to the target component. Note that is a representation mapping is not supplied, then the value of the source component is mapped directly to the value of the target component without any manipulation.
====================== ============================================== ===================================================================================================================================================================================================================================================================================================

**RepresentationMapType: **\ RepresentationMapType describes the
structure of the mapping of the value of a source to component to a
target component. Either a reference to another map defined within the
containing structure set or a description of the source and target text
formats must be provided. Note that for key family components, only a
reference to a codelist map is relevant, since that is the only type of
coded representation allowed in a key family.

Content:

(CodelistMap \| (ToTextFormat, ToValueType) \| ValueMap)

Element Documentation:

============ =================================== ===========================================================================================================================================================================================================================================================================================================================================================
**Name**     **Type**                            **Documentation**
============ =================================== ===========================================================================================================================================================================================================================================================================================================================================================
CodelistMap  com: LocalCodelistMapRefe renceType CodelistMap references a codelist map defined in the same structure set which maps the enumeration of the representation of the source component to the enumeration of the representation of the target component.
ToTextFormat TextFormatType                      ToTextFormat describes the un-coded representation of the target to which the value of the referenced component should be transformed.
ToValueType  ToValueTypeType                     ToValueType notes whether the value, name, or description of the source value should be used in the target value.
ValueMap     ValueMapType                        ValueMap provides for a simple mapping of a source value to a target value without having to define a codelist map. This is available to allow mappings in situations such as the source or target is not being formally coded, or the source and/or target being a measure dimension in which case its representation is not mappable from a codelist map.
============ =================================== ===========================================================================================================================================================================================================================================================================================================================================================

**ValueMapType: **\ ValueMapType contains a collection of value
mappings, which give a source and target value.

Content:

ValueMapping+

Element Documentation:

============ ================ ===========================================================================
**Name**     **Type**         **Documentation**
============ ================ ===========================================================================
ValueMapping ValueMappingType ValueMapping provides a source and target value for the purpose of mapping.
============ ================ ===========================================================================

**ValueMappingType: **\ ValueMappingType specifies the relationship
between two values as a source and target.

Attributes:

source, target

Content:

{Empty}

Attribute Documentation:

======== ========= =================
**Name** **Type**  **Documentation**
======== ========= =================
source   xs:string
target   xs:string
======== ========= =================

Simple Types
~~~~~~~~~~~~

**UsageStatusType: **\ UsageStatusType provides a list of enumerated
types for indicating whether reporting a given attribute is mandatory or
conditional.

Derived by restriction of xs:NMTOKEN .

Enumerations:

=========== ===================================================================================================
**Value**   **Documentation**
=========== ===================================================================================================
Mandatory   Reporting the associated attribute is mandatory - a value must be supplied.
Conditional Reporting the associated attribute is not mandatory - a value may be supplied, but is not required.
=========== ===================================================================================================

**CodeDataType: **\ CodeDataType is a restriction of the basic data
types that are applicable to codes. Although some of the higher level
time period formats are perimitted, it should be noted that any value
which contains time (which includes a time zone offset) is not allowable
as a code identifier.

Derived by restriction of com:SimpleDataType .

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
Month                   A time datatype corresponding to W3C XML Schema's xs:gMonth datatype.
MonthDay                A time datatype corresponding to W3C XML Schema's xs:gMonthDay datatype.
Day                     A time datatype corresponding to W3C XML Schema's xs:gDay datatype.
Duration                A time datatype corresponding to W3C XML Schema's xs:duration datatype.
======================= =======================================================================================================================================================================================================================================================================================================

**SimpleCodeDataType: **\ SimpleCodeDataType restricts SimpleDataType to
specify the allowable data types for a simple code. The possible values
are simply Alpha, AlphaNumeric, or Numeric.

Derived by restriction of com:SimpleDataType .

Enumerations:

============ ==================================================================================================================================================================
**Value**    **Documentation**
============ ==================================================================================================================================================================
Alpha        A string datatype which only allows for the simple aplhabetic charcter set of A-z.
AlphaNumeric A string datatype which only allows for the simple alphabetic character set of A-z plus the simple numeric character set of 0-9.
Numeric      A string datatype which only allows for the simple numeric character set of 0-9. This format is not treated as an integer, and therefore can having leading zeros.
============ ==================================================================================================================================================================

**TargetObjectDataType: **\ TargetObjectDataType restricts DataType to
specify the allowable data types for representing a target object value.

Derived by restriction of com:DataType .

Enumerations:

============================= ===================================================================================================================================================================================================================================================================
**Value**                     **Documentation**
============================= ===================================================================================================================================================================================================================================================================
KeyValues                     This value indicates that the content of the component will be data key (a set of dimension references and values for the dimensions).
IdentifiableReference         This value indicates that the content of the component will be complete reference (either URN or full set of reference fields) to an Identifiable object in the SDMX Information Model.
DataSetReference              This value indicates that the content of the component will be reference to a data provider, which is actually a formal reference to a data provider and a data set identifier value.
AttachmentConstraintReference This value indicates that the content of the component will be reference to an attachment constraint, which is actually a combination of a collection of full or partial key values and a reference to a data set or data structure, usage, or provision agreement.
============================= ===================================================================================================================================================================================================================================================================

**ToValueTypeType: **\ ToValueTypeType provides an enumeration of
available text-equivalents for translation of coded values into textual
formats.

Derived by restriction of xs:NMTOKEN .

Enumerations:

=========== ======================================================================================
**Value**   **Documentation**
=========== ======================================================================================
Value       Code or other tokenized value, as provided in the representation scheme.
Name        The human-readable name of the Value, as provided in the representation scheme.
Description The human-readable description of the Value, as provided in the representation scheme.
=========== ======================================================================================

.. _section-1:

.. |image0| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image1| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image2| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image3| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image4| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image5| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image6| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image7| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image8| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image9| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image10| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image11| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image12| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image13| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image14| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image15| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image16| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image17| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image18| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image19| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image20| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image21| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image22| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image23| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image24| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image25| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image26| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image27| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image28| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image29| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image30| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image31| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image32| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image33| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image34| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image35| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image36| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image37| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image38| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image39| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image40| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image41| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image42| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image43| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image44| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image45| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image46| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image47| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image48| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image49| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image50| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image51| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image52| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image53| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image54| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image55| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image56| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image57| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image58| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image59| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image60| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image61| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image62| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image63| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image64| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image65| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image66| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image67| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image68| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image69| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image70| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image71| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image72| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image73| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image74| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image75| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image76| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image77| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image78| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image79| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image80| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image81| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image82| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image83| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image84| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image85| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image86| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image87| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image88| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image89| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image90| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image91| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image92| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image93| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image94| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image95| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image96| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image97| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image98| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image99| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image100| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image101| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image102| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image103| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image104| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image105| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image106| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image107| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image108| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image109| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image110| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image111| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image112| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image113| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image114| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image115| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image116| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image117| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image118| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image119| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image120| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image121| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image122| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image123| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image124| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image125| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image126| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image127| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image128| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image129| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image130| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image131| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image132| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image133| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image134| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image135| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image136| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image137| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image138| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image139| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image140| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image141| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image142| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image143| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image144| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image145| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image146| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image147| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image148| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image149| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image150| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image151| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image152| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image153| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image154| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image155| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image156| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image157| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image158| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image159| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image160| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image161| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image162| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image163| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image164| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image165| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image166| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image167| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image168| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image169| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image170| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image171| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image172| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image173| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image174| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image175| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image176| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image177| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image178| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image179| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image180| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image181| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image182| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image183| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image184| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image185| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image186| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image187| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image188| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image189| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image190| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image191| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image192| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image193| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image194| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image195| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image196| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image197| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image198| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image199| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image200| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image201| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image202| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image203| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image204| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image205| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image206| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image207| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image208| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image209| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image210| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image211| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image212| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image213| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image214| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image215| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image216| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image217| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image218| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image219| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image220| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image221| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image222| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image223| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image224| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image225| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image226| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image227| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image228| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image229| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image230| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image231| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image232| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image233| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image234| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image235| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image236| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image237| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image238| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image239| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image240| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image241| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image242| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image243| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image244| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image245| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image246| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image247| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image248| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image249| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image250| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image251| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image252| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image253| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image254| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image255| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image256| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image257| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image258| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image259| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image260| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image261| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image262| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image263| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image264| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image265| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image266| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image267| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image268| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image269| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image270| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image271| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image272| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image273| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image274| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image275| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image276| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image277| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image278| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image279| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image280| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image281| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image282| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image283| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image284| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image285| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image286| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image287| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image288| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image289| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image290| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image291| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image292| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image293| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image294| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image295| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image296| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image297| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image298| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image299| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image300| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image301| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image302| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image303| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image304| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image305| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image306| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image307| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image308| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image309| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image310| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image311| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image312| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image313| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image314| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image315| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image316| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image317| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image318| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image319| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image320| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image321| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image322| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image323| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image324| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image325| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image326| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image327| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image328| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image329| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image330| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image331| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image332| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image333| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image334| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image335| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image336| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image337| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image338| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image339| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image340| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image341| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image342| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image343| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image344| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image345| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image346| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image347| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image348| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image349| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image350| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image351| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image352| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image353| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image354| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image355| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image356| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image357| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image358| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image359| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image360| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image361| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image362| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image363| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image364| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image365| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image366| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image367| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image368| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image369| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image370| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image371| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image372| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image373| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image374| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image375| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image376| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image377| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image378| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image379| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image380| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image381| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image382| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image383| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image384| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image385| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image386| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image387| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image388| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image389| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image390| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image391| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image392| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image393| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image394| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image395| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image396| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image397| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image398| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image399| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image400| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image401| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image402| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image403| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image404| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image405| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image406| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image407| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image408| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image409| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image410| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image411| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image412| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image413| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image414| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image415| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image416| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image417| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image418| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image419| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image420| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image421| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image422| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image423| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image424| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image425| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image426| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image427| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image428| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image429| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image430| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image431| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image432| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image433| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image434| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image435| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image436| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image437| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image438| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image439| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image440| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image441| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image442| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image443| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image444| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image445| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image446| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image447| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image448| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image449| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image450| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image451| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image452| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image453| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image454| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image455| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image456| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image457| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image458| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image459| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image460| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image461| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image462| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image463| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image464| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image465| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image466| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image467| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image468| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image469| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image470| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image471| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image472| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image473| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image474| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image475| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image476| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image477| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image478| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image479| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image480| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image481| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image482| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image483| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image484| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image485| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image486| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image487| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image488| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image489| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image490| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image491| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image492| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image493| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image494| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image495| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image496| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image497| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image498| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image499| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image500| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image501| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image502| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image503| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image504| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image505| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image506| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image507| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image508| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image509| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image510| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image511| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image512| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image513| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image514| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image515| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image516| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image517| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image518| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image519| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image520| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image521| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image522| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image523| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image524| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image525| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image526| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image527| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image528| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image529| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image530| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image531| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image532| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image533| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image534| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image535| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image536| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image537| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image538| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image539| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image540| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image541| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image542| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image543| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image544| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image545| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image546| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image547| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image548| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image549| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image550| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image551| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image552| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image553| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image554| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image555| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image556| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image557| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image558| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image559| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image560| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image561| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image562| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image563| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image564| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image565| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image566| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image567| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image568| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image569| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image570| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image571| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image572| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image573| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image574| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image575| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image576| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image577| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image578| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image579| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image580| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image581| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image582| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image583| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image584| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image585| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image586| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image587| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image588| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image589| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image590| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image591| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png
.. |image592| image:: ./media-SDMX_2_1_SECTION_3A_PART_III_STRUCTURE/media/image2.png

