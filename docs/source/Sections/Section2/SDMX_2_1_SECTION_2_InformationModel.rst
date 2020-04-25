Information Model
+++++++++++++++++

Change History
==============

Version 1.0 – initial release September 2004.

Version 2.0 – release November 2005

Major functional enhancements by addition of new packages:

-  Metadata Structure Definition

-  Metadata Set

-  Hierarchical Code Scheme

-  Data and Metadata Provisioning

-  Structure Set and Mappings

-  Transformations and Expressions

-  Process and Transitions

Re-engineering of some SDMX Base structures to give more functionality:

-  Item Scheme and Item can have properties – this gives support for
   complex hierarchical code schemes (where the property can be used to
   sequence codes in scheme), and Item Scheme mapping tables (where the
   property can give additional information about the map between the
   two schemes and the between two Items)

-  revised Organisation pattern to support maintained schemes of
   organisations, such as a data provider

-  modified Component Structure pattern to support identification of
   roles played by components and the attachment of attributes

-  change to inheritance to enable more artefacts to be identifiable and
   versionable

Introduction of new types of Item Scheme:

-  Object Type Scheme to specify object types in support of the Metadata
   Structure Definition (principally the object types (classes) in this
   Information Model)

-  Type Scheme to specify types other than object type

-  A generic Item Scheme Association to specify the association between
   Items in two or more Item Schemes, where such associations cannot be
   described in the Structure Set and Transformation.

The Data Structure Definition is introduced as a synonym for Key Family
though the term Key Family is retained and used in this specification.

Modification to Data Structure Definition (DSD) to

-  align the cross sectional structures with the functionality of the
   schema

-  support Data Structure Definition extension (i.e. to derive and
   extend a Data Structure Definition from another Data Structure
   Definition), thus supporting the definition of a related “set” of key
   families

-  distinguish between data attributes (which are described in a Data
   Structure Definition) from metadata attributes (which are described
   in a metadata structure definition)

-  attach data attributes to specific identifiable artefacts (formally
   this was supported by attachable artefact)

Domain Category Scheme re-named Category Scheme to better reflect the
multiple usage of this type of scheme (e.g. subject matter domain,
reporting taxonomy).

Concept Scheme enhanced to allow specification of the representation of
the Concept. This specification is the default (or core) representation
and can be overridden by a construct that uses it (such as a Dimension
in a Data Structure Definition).

Revision of cross sectional data set to reflect the functionality of the
version 1.0 schema.

Revision of Actors and Use Cases to reflect better the functionality
supported.

Version 2.1 – release April 2011

The purpose of this revision is threefold:

-  To introduce requested changes to functionality

-  To align the model and syntax implementations more closely (note,
   however, that the model remains syntax neutral)

-  To correct errors in version 2.0

*SDMX Base*

*Basic inheritance and patterns*

1. The following attributes are added to Maintainable:

..

   i) isExternalReference

   ii) structure URL

   iii) serviceURL

2.  Added Nameable Artefact and moved the Name and Description
    associations from Identifiable Artefact to Nameable Artefact. This
    allows an artefact to be identified (with id and urn) without the
    need to specify a Name.

3.  Removed any inheritance from Versionable Artefact with the exception
    of Maintainable Artefact – this means that only Maintainable objects
    can be versioned, and objects contained in a maintainable object
    cannot be independently versioned.

4.  Renamed MaintenanceAgency to Agency 0 this is its name in the schema
    and the URN.

5.  Removed abstract class Association as a subclass of Item (as these
    association types are not maintained in Item Schemes). Specific
    associations are modelled explicitly (e.g. Categorisation,
    ItemScheme, Item).

6.  Added ActionType to data types.

7.  Removed Coded Artefact and Uncoded Artefact and all subclasses (e.g.
    Coded Data Attribute and Uncoded Data Attribute) as the
    “Representation” is more complex than just a distinction between
    coded and uncoded.

8.  Added Representation to the Component. Removed association to Type.

9.  Removed concept role association (to Item) as roles are identified
    by a relationship to a Concept.

10. Removed abstract class Attribute as both Data Attribute and Metadata
    Attribute have different properties. Data Attribute and Metadata
    Attribute inherit directly from Component.

11. isPartial attribute added to Item Scheme to support partial Item
    Schemes (e.g. partial Code list).

*Representation*

1. Removed interval and enumeration from Facet.

2. added facetValueType to Facet.

3. Re-named DataType to facetValueType.

4. Added observationalTimePeriod, inclusiveValueRange and
   exclusiveValueRange to facetValueType.

5. Added ExtendedFacetType as a sub class of FacetType. This includes
   Xhtml as a facet type to support this as an allowed representation
   for a Metadata Attribute

*Organisations*

1. Organisation Role is removed and replaced with specific Organisation
   Schemes of Agency, Data Provider, Data Consumer, Organisation Unit.

*Mapping (Structure Maps)*

Updated Item Scheme Association as follows:

1.  Renamed to Item Scheme Map to reflect better the sub classes and
    relate better to the naming in the schema.

2.  Removed inheritance of Item Scheme Map from Item Scheme, and
    inherited directly from Nameable Artefact.

3.  Item Association inherits from Identifiable Artefact.

4.  Removed Property from the model as this is not supported in the
    schema.

5.  Removed association type between Item Scheme Map and Item, and
    Association and Item.

6.  Removed Association from the model.

7.  Made Item Association a sub class of Identifiable, was a sub class
    Item.

8.  Removed association to Property from both Item Scheme Map and Item.

9.  Added attribute alias to both Item Scheme Association and Item
    Association.

10. Made Item Scheme Map and Item Association abstract.

11. Added sub-classes to Item Scheme Map – there is a subclass for each
    type of Item Scheme Association (e.g. Code list Map).

12. Added mapping between Reporting Taxonomy as this is an Item Scheme
    and can be mapped in the same way as other Item Schemes.

13. Added Hybrid Code list Map and Hybrid Code Map to support code
    mappings between a Code list and a Hierarchical Code list.

*Mapping: Structure Map*

1. This is a new diagram. Essentially removed inherited /hierarchy
   association between the various maps, as these no longer inherit from
   Item, and replaced the associations to the abstract Maintainable and
   Versionable Artefact classes with the actual concrete classes.

2. Removed associations between Code list Map, Category Scheme Map, and
   Concept Scheme Map and made this association to Item Scheme Map.

3. Removed hierarchy of Structure Map.

*Concept*

1. Added association to Representation.

*Data Structure Definition*

1.  Added Measure Dimension to support structure-specific renderings of
    the DSD. The Measure Dimension is associated to a Concept Scheme
    that specifies the individual measures that are valid.

2.  The three types of “Dimension”, - Dimension, Measure Dimension, Time
    Dimension – have a super class – Dimension Component

3.  Added association to a Concept that defines the role that the
    component (Dimension, Data Attribute, Measure Dimension) plays in
    the DSD. This replaces the Boolean attributes on the components.

4.  Added Primary Measure and removed this as role of Measure.

5.  Deleted the derived Data Structure Definition association from Data
    Structure Definition to itself as this is not supported directly in
    DSD.

6.  Deleted attribute GroupKeyDescriptor.isAttachmentConstraint and
    replaced with an association to an Attachment Constraint.

7.  Replaced association from Data Attribute to Attachable Artefact with
    association to Attribute Relationship.

8.  Added a set of classes to support Attribute Relationship.

9.  Renamed KeyDescriptor to DimensionDescriptor to better reflect its
    purpose.

10. Renamed GroupKeyDescriptor to GroupDimensionDescriptor to better
    reflect its purpose.

*Code list*

1. CodeList classname changed to Codelist.

2. Removed codevalueLength from Codelist as this is supported by Facet.

3. Removed hierarchyView association between Code and Hierarchy as this
   association is not implemented.

Metadata Structure Definition(MSD)

1. Full Target Identifier, Partial Target Identifier, and Identifier
   Component are replaced by Metadata Target and Target Object.
   Essentially this eliminates one level of specification and reference
   in the MSD, and so makes the MSD more intuitive and easier to specify
   and to understand.

2. Re-named Identifiable Object Type to Identifiable Object Target and
   moved to the MSD package.

3. Added sub classes to Target Object as these are the actual types of
   object to which metadata can be attached. These are Identifiable
   Object Target (allows reporting of metadata to any identifiable
   object), Key Descriptor Values Target (allows reporting of metadata
   for a data series key, Data Set Target (allows reporting of metadata
   to a data set), and Reporting Period Target (allows the metadata set
   to specify a reporting period).

4. Allowed Target Object can have any type of Representation, this was
   restricted in version 2.0 to an enumerated representation in the
   model (but not in the schemas).

5. Removed Object Type Scheme (as users cannot maintain their own list
   of object types), and replaced with an enumeration of Identifiable
   Objects.

6. Removed association between Metadata Attribute and Identifiable
   Artefact and replaced this with an association between Report
   Structure and Metadata Target, and allowed one Report Structure to
   reference more than on Metadata Target. This allowing a single Report
   Structure to be defined for many object types.

7. Added the ability to specify that a Metadata Attribute can be
   repeated in a Metadata Set and that a Metadata Attribute can be
   specified as “presentational” meaning that it is present for
   structural and presentational purposes, and will not have content in
   a Metadata Set.

8. The Representation of a Metadata Attribute uses Extended Facet (to
   support Xhtml).

*Metadata Set*

1. Added link to Data Provider - 0..1 but note that for metadata set
   registration this will be 1.

2. Removed Attribute Property as the underlying Property class has been
   removed.

3. One Metadata Set is restricted to reporting metadata for a single
   Report Structure.

4. The Metadata Report classes are re-structured and re-named to be
   consistent with the renaming and restructuring of the MSD.

5. Metadata Attribute Value is renamed Reported Attribute to be
   consistent with the schemas.

6. Deleted XML attribute and Contact Details from the inheritance
   diagram.

*Category Scheme*

1. Added Categorisation. Category no longer has a direct association to
   Dataflow and Metadataflow.

2. Changed Reporting Taxonomy inheritance from Category Scheme to
   Maintainable Artefact.

3. Added Reporting Category and associated this to Structure Usage.

*Data Set*

1. Removed the association to Provision Agreement from the diagram.

2. Added association to Data Structure Definition. This association was
   implied via the dataflow but this is optional in the implementation
   whereas the association to the Data Structure Definition is
   mandatory.

3. Added attributes to Data Set.

4. There is a single, unified, model of the Data Set which supports four
   types of data set:

   -  Generic Data Set – for reporting any type of data series,
      including time series and what is sometimes known as “cross
      sectional data”. In this data set, the value of any one dimension
      (including the Time Dimension) can be reported with the
      observation (this must be for the same dimension for the entire
      data set)

   -  Structure-specific Data Set – for reporting a data series that is
      specific to a DSD

   -  Generic Time Series Data Set – this is identical to the Generic
      Data Set except it must contain only time series, which means that
      a value for the Time Dimension is reported with the Observation

   -  Structure-specific Time Series Data Set - this is identical to the
      Structure-specific Data Set except it must contain only time
      series, which means that a value for the Time Dimension is
      reported with the Observation.

5. Removed Data Set as a sub class of Identifiable – but note that Data
   Set has a “setId” attribute.

6. Added coded and uncoded variants of Key Value, Observation, and
   Attribute Value in order to show the relationship between the coded
   values in the data set and the Codelist in the Data Structure
   Definition.

7. Made Key Value abstract with sub classes for coded, uncoded, measure
   (MeasureKeyValue) ads time(TimeKeyValue) The Measure Key Value is
   associated to a Concept as it must take its identify from a Concept.

*XSDataSet*

1. This is removed and replaced with the single, unified data set model.

*Constraint*

1. Constraint is made Maintainable (was Identifiable).

2. Added artefacts that better support and distinguish (from data) the
   constraints for metadata.

3. Added Constraint Role to specify the purpose of the Constraint. The
   values are allowable content (for validation of sub set code code
   lists), and actual content (to specify the content of a data or
   metadata source).

*Process*

1. Removed inheritance from Item Scheme and Item: Process inherits
   directly from Maintainable and Process Step from Identifiable.

2. Removed specialisation association between Transition and
   Association.

3. Removed Transition Scheme - transitions are explicitly specified and
   not maintained as Items in a Item Scheme.

4. Removed Expression and replaced with Computation.

5. Transition is associated to Process Step and not Process itself.
   Therefore the source association to Process Step is removed.

6. Removed Expressions as these are not implemented in the schemas. But
   note that the Transformations and Expressions model is retained,
   though it is not implemented in the schemas.

*Hierarchical Codelist*

1. Renamed HierarchicalCodeList to HierarchicalCodelist.

2. This is re-modelled to reflect more accurately the way this is
   implemented: this is as an actual hierarchy rather than a set of
   relational associations from which the hierarchy can be derived.

3. Code Association is re-named Hierarchical Code and the association
   type association to Code is removed (as these association types are
   not maintained in an Item Scheme).

4. Hierarchical Code is made an aggregate of Hierarchy, and not of
   Hierarchical Codelist.

5. Removed root node in the Hierarchy – there can be many top-level
   codes in Hierarchical Code.

6. Added reference association between Hierarchical Code and Level to
   indicate the Level if the Hierarchy is a level based hierarchy.

*Provisioning and Registration*

1. Data Provider and Provision Agreement have an association to
   Datasource (was Query Datasource), as the association is to any of
   Query Datasource and Simple Datasource.

2. Provision Agreement is made Maintainable and indexing attributes
   moved to Registration

3. Registration has a registry assigned Id and indexing attributes.

Introduction
============

This document is not normative, but provides a detailed view of the
information model on which the normative SDMX specifications are based.
Those new to the UML notation or to the concept of Data Structure
Definitions may wish to read the appendixes in this document as an
introductory exercise.

Related Documents
-----------------

This document is one of two documents concerned with the SDMX
Information Model. The complete set of documents is:

SDMX SECTION 02 INFORMATION MODEL: UML CONCEPTUAL DESIGN (this document)

This document comprises the complete definition of the information
model, with the exception of the registry interfaces. It is intended for
technicians wishing to understand the complete scope of the SDMX
technical standards in a syntax neutral form.

SDMX SECTION 05 REGISTRY SPECIFICATION: LOGICAL INTERFACES

This document provides the logical specification for the registry
interfaces, including subscription/notification, registration/submission
of data and metadata, and querying.

Modelling Technique and Diagrammatic Notes
------------------------------------------

The modelling technique used for the SDMX Information Model (SDMX-IM) is
the Unified Modelling Language (UML). An overview of the constructs of
UML that are used in the SDMX-IM can be found in the Appendix “A Short
Guide to UML in the SDMX Information Model”

UML diagramming allows a class to be shown with or without the
compartments for one or both of attributes and operations (sometimes
called methods). In this document the operations compartment is not
shown as there are no operations.

.. _image0:
.. figure:: /_static/media-SDMX_2_1_SECTION_2_InformationModel/media/image2.png
    :alt: Class with operations suppressed
    :align: center
    
    Class with operations suppressed

.. _uml1:
.. uml::
   :align: center
   :caption: Class with operations suppressed
  
   object ExtendedFacet {
    facetType : ExtendedFacetType
    facetValue: String
    facetValueType : ExtendedFacetType
   }

In some diagrams for some classes the attribute compartment is
suppressed even though there may be some attributes. This is deliberate
and is done to aid clarity of the diagram. The method used is:

-  The attributes will always be present on the class diagram where the
   class is defined and its attributes and associations are defined.

-  On other diagrams, such as inheritance diagrams, the attributes may
   be suppressed from the class for clarity.

|image1|

Figure 2 Class with attributes also suppressed

Note that, in any case, attributes inherited from a super class are not
shown in the sub class.

The following table structure is used in the definition of the classes,
attributes, and associations.

========= =============== ===========
Class     Feature         Description
ClassName                
\         attributeName   .
\         associationName
\         +roleName      
========= =============== ===========

The content in the “Feature” column comprises or explains one of the
following structural features of the class:

-  Whether it is an abstract class. Abstract classes are shown in
   *italic Courier* font

-  The superclass this class inherits from, if any

-  The sub classes of this class, if any

-  Attribute – the attributeName is shown in Courier font

-  Association – the associationName is shown in Courier font. If the
   association is derived from the association between super classes
   then the format is /associationName

-  Role – the +roleName is shown in Courier font

The Description column provides a short definition or explanation of the
Class or Feature. UML class names may be used in the description and if
so, they are presented in normal font with spaces between words. For
example the class ConceptScheme will be written as Concept Scheme.

Overall Functionality
---------------------

Information Model Packages
~~~~~~~~~~~~~~~~~~~~~~~~~~

The SDMX Information Model (SDMX-IM) is a conceptual metamodel from
which syntax specific implementations are developed. The model is
constructed as a set of functional packages which assist in the
understanding, re-use and maintenance of the model.

In addition to this, in order to aid understanding each package can be
considered to be in one of three conceptual layers:

-  the SDMX Base layer comprises fundamental building blocks which are
   used by the Structural Definitions layer and the Reporting and
   Dissemination layer

-  the Structural Definitions layer comprises the definition of the
   structural artefacts needed to support data and metadata reporting
   and dissemination

-  the Reporting and Dissemination layer comprises the definition of the
   data and metadata containers used for reporting and dissemination

In reality the layers have no implicit or explicit structural function
as any package can make use of any construct in another package.

Version 1.0
~~~~~~~~~~~

In version 1.0 the metamodel supported the requirements for:

-  Data Structure Definition definition including (domain) category
   scheme, (metadata) concept scheme, and code list

-  Data and related metadata reporting and dissemination

The SDMX-IM comprises a number of packages. These packages act as
convenient compartments for the various sub models in the SDMX-IM. The
diagram below shows the sub models of the SDMX-IM that were included in
the version 1.0 specification.

|image2|

Figure 3: SDMX Information Model Version 1.0 package structure

Version 2.0/2.1
~~~~~~~~~~~~~~~

The version 2.0/2.1 model extends the functionality of version 1.0.
principally in the area of metadata, but also in various ways to define
structures to support data analysis by systems with knowledge of cube
type structures such as OLAP [1]_ systems. The following major
constructs have been added at version 2.0/2.1

-  Metadata structure definition

-  Metadata set

-  Hierarchical Codelist

-  Data and Metadata Provisioning

-  Process

-  Mapping

-  Constraints

-  Constructs supporting the Registry

Furthermore, the term Data Structure Definition replaces the term Key
Family: as both of these terms are used in various communities they are
synonymous. The term Data Structure Definition is used in the model and
this document.

|image3|

Figure 4 SDMX Information Model Version 2.0/2.1 package structure

Additional constructs that are specific to a registry based scenario can
be found in the Specification of Registry Interfaces. For information
these are shown on the diagram below and comprise:

-  Subscription and Notification

-  Registration

-  Discovery

Note that the data and metadata required for registry functions are not
confined to the registry, and the registry also makes use of the other
packages in the Information Model.

|image4|

Figure 5: SDMX Information Model Version 2.0/2.1 package structure
including the registry

Actors and Use Cases
====================

.. _introduction-1:

Introduction
------------

In order to develop the data models it is necessary to understand the
functions to be supported resulting from the requirements definition.
These are defined in a use case model. The use case model comprises
actors and use cases and these are defined below.

Actor

“\ *An actor defines a coherent set of roles that users of the system
can play when interacting with it. An actor instance can be played by
either an individual or an external system*\ ”

Use case

“A use case defines a set of use-case instances, where each instance is
a sequence of actions a system performs that yields an observable result
of value to a particular actor”

The overall intent of the model is to support data and metadata
reporting, dissemination, and exchange in the field of aggregated
statistical data and related metadata. In order to achieve this, the
model needs to support three fundamental aspects of this process:

-  Maintenance of structural and provisioning definitions

-  Data and reference metadata publishing (reporting), and consuming
   (using)

-  Access to data, reference metadata, and structural and provisioning
   definitions

This document covers the first two aspects, whilst the document on the
Registry logical model covers the last aspect.

Use Case Diagrams
-----------------

Maintenance of Structural and Provisioning Definitions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use cases
^^^^^^^^^

|image5|

Figure 6 **Use cases for maintaining data and metadata structural and provisioning definitions**

Explanation of the Diagram
^^^^^^^^^^^^^^^^^^^^^^^^^^

In order for applications to publish and consume data and reference
metadata it is necessary for the structure and permitted content of the
data and reference metadata to be defined and made available to the
applications, as well as definitions that support the actual process of
publishing and consuming. This is the responsibility of a Maintenance
Agency.

All maintained artefacts are maintained by a Maintenance Agency. For
convenience the Maintenance Agency actor is sub divided into two actor
roles:

-  maintaining structural definitions

-  maintaining provisioning definitions

Whilst both these functions may be carried out by the same person, or at
least by the same maintaining organization, the purpose of the
definitions is different and so the roles have been differentiated:
structural definitions define the format and permitted content of data
and reference metadata when reported or disseminated, whilst
provisioning definitions support the process of reporting and
dissemination (who reports what to whom, and when).

In a community based scenario where at least the structural definitions
may be shared, it is important that the scheme of maintenance agencies
is maintained by a responsible organization (called here the Community
Administrator), as it is important that the Id of the Maintenance Agency
is unique.

Definitions
^^^^^^^^^^^

========= ========= ==================================================================================================================================================================================================================================================================================
Actor     Use Case  Description
|image6|            Responsible organisation that administers structural definitions common to the community as a whole.
\         |image7|  Creation and maintenance of the top-level scheme of maintenance agencies for the Community.
|image8|            Responsible agency for maintaining structural artefacts such as code lists, concept schemes, Data Structure Definition structural definitions, metadata structure definitions, data and metadata provisioning artefacts such as provision agreement, and sub-maintenance agencies.
                   
                    sub roles are:
                   
                    Structural Definitions Maintenance Agency
                   
                    Provisioning Definitions Maintenance Agency
|image9|            Responsible for maintaining structural definitions.
\         |image10| The maintenance of structural definitions. This use case has sub class use cases for each of the structural artefacts that are maintained.
\         |image11| Creation and maintenance of the Data Structure Definition, Metadata Structure Definition, and the supporting artefacts that they use, such as code list and concepts
                   
          |image12| This includes Agency, Data Provider, Data Consumer, and Organisation Unit Scheme
                   
          |image13|
                   
          |image14|
                   
          |image15|
                   
          |image16|
                   
          |image17|
                   
          |image18|
                   
          |image19|
                   
          |image20|
                   
          |image21|
|image22|           Responsible for maintaining data and metadata provisioning definitions.
\         |image23| The maintenance of provisioning definitions.
========= ========= ==================================================================================================================================================================================================================================================================================

Figure 7: Table of Actors and Use Cases for Maintenance of Structural
and Provisioning Definitions

Publishing and Using Data and Reference Metadata
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _use-cases-1:

Use Cases
^^^^^^^^^

|image24|

Figure 8: Actors and use cases for data and metadata publishing and
consuming

.. _explanation-of-the-diagram-1:

Explanation of the Diagram
^^^^^^^^^^^^^^^^^^^^^^^^^^

Note that in this diagram “publishing” data and reference metadata is
deemed to be the same as “reporting” data and reference metadata. In
some cases the act of making the data available fulfils both functions.
Aggregated data is published and in order for the Data Publisher to do
this and in order for consuming applications to process the data and
reference metadata its structure must be known. Furthermore, consuming
applications may also require access to reference metadata in order to
present this to the Data Consumer so that the data is better understood.
As with the data, the reference metadata also needs to be formatted in
accordance with a maintained structure. The Data Consumer and Metadata
Consumer cannot use the data or reference metadata unless it is
“published” and so there is a “data source” or “metadata source”
dependency between the “uses” and “publish” use cases.

In any data and reference metadata publishing and consuming scenario
both the publishing and the consuming applications will need access to
maintained Provisioning Definitions. These definitions may be as simple
as who provides what data and reference metadata to whom, and when, or
it can be more complex with constraints on the data and metadata that
can be provided by a particular publisher, and, in a data sharing
scenario where data and metadata are “pulled” from data sources, details
of the source.

.. _definitions-1:

Definitions
^^^^^^^^^^^

========= ========= ===========================================================================================================================================================================================================================
Actor     Use Case  Description
|image25|           Responsible for publishing data according to a specified Data Structure Definition (data structure) definition, and relevant provisioning definitions.
\         |image26| Publish a data set. This could mean a physical data set or it could mean to make the data available for access at a data source such as a database that can process a query.
|image27|           The user of the data. It may be a human consumer accessing via a user interface, or it could be an application such as a statistical production system.
\         |image28| Use data that is formatted according to the structural definitions and made available according to the provisioning definitions.
                   
                    Data are often linked to metadata that may reside in a different location and be published and maintained independently.
|image29|           Responsible for publishing reference metadata according to a specified metadata structure definition, and relevant provisioning definitions.
\         |image30| Publish a reference metadata set. This could mean a physical metadata set or it could mean to make the reference metadata available for access at a metadata source such as a metadata repository that can process a query.
|image31|           The user of the reference metadata. It may be a human consumer accessing via a user interface, or it could be an application such as a statistical production or dissemination system.
\         |image32| Use reference metadata that is formatted according to the structural definitions and made available according to the provisioning definitions.
========= ========= ===========================================================================================================================================================================================================================

SDMX Base Package
=================

.. _introduction-2:

Introduction
------------

The constructs in the SDMX Base package comprise the fundamental
building blocks that support many of the other structures in the model.
For this reason, many of the classes in this package are abstract (i.e.
only derived sub-classes can exist in an implementation).

The motivation for establishing the SDMX Base package is as follows:

-  it is accepted “Best Practise” to identify fundamental archetypes
   occurring in a model

-  identification of commonly found structures or “patterns” leads to
   easier understanding

-  identification of patterns encourages re-use

Each of the class diagrams in this section views classes from the SDMX
Base package from a different perspective. There are detailed views of
specific patterns, plus overviews showing inheritance between classes,
and relationships amongst classes.

Base Structures - Identification, Versioning, and Maintenance
-------------------------------------------------------------

Class Diagram
~~~~~~~~~~~~~

|image33|

Figure 9: SDMX Identification, Maintenance and Versioning

.. _explanation-of-the-diagram-2:

Explanation of the Diagram
~~~~~~~~~~~~~~~~~~~~~~~~~~

Narrative
^^^^^^^^^

This group of classes forms the nucleus of the administration facets of
SDMX objects. They provide features which are reusable by derived
classes to support horizontal functionality such as identity, versioning
etc.

All classes derived from the abstract class *AnnotableArtefact* may have
Annotations (or notes): this supports the need to add notes to all
SDMX-ML elements. The Annotation is used to convey extra information to
describe any SDMX construct. This information may be in the form of a
URL reference and/or a multilingual text (represented by the association
to InternationalString).

The *IdentifiableArtefact* is an abstract class that comprises the basic
attributes needed for identification. Concrete classes based on
*IdentifiableArtefact* all inherit the ability to be uniquely
identified.

The *NamableArtefact* is an abstract class that inherits from
*IdentifiableArtefact* and in addition the +description and +name roles
support multilingual descriptions and names for all objects based on
*NameableArtefact*. The InternationalString supports the representation
of a description in multiple locales (locale is similar to language but
includes geographic variations such as Canadian French, US English
etc.). The *LocalisedString* supports the representation of a
description in one locale.

*VersionableArtefact* is an abstract class which inherits from
*NameableArtefact* and adds versioning ability to all classes derived
from it.

*MaintainableArtefact* further adds the ability for derived classes to
be maintained via its association to *Agency, and adds locational
information (i.e. from where the object can be retrieved)*. It is
possible to define whether the artefact is draft or final with the final
attribute.

The inheritance chain from *AnnotableArtefact* through to
*MaintainableArtefact* allows SDMX classes to inherit the features they
need, from simple annotation, through identity, naming, to versioning
and maintenance.

.. _definitions-2:

Definitions
^^^^^^^^^^^

====================== ==================================== ===================================================================================================================================================================================
Class                  Feature                              Description
*AnnotableArtefact*    Base inheritance sub classes are:    Objects of classes derived from this can have attached annotations.
                                                           
                       *IdentifiableArtefact*              
Annotation                                                  Additional descriptive information attached to an object.
\                      id                                   Identifier for the Annotation. It can be used to disambiguate one Annotation from another where there are several Annotations for the same annotated object.
\                      title                                A title used to identify an annotation.
\                      type                                 Specifies how the annotation is to be processed.
\                      url                                  A link to external descriptive text.
\                      +text                                An International String provides the multilingual text content of the annotation via this role.
*IdentifiableArtefact* Superclass is *AnnotableArtefact*    Provides identity to all derived classes. It also provides annotations to derived classes because it is a subclass of Annotable Artefact.
                                                           
                       Base inheritance sub classes are:   
                                                           
                       NameableArtefact                    
\                      id                                   The unique identifier of the object.
\                      uri                                  Universal resource identifier that may or may not be resolvable.
\                      urn                                  Universal resource name – this is for use in registries: all registered objects have a urn.
*NameableArtefact*     Superclass is *IdentifiableArtefact* Provides a Name and Description to all derived classes in addition to identification and annotations.
                                                           
                       Base inheritance sub classes are:   
                                                           
                       *VersionableArtefact*               
\                      +description                         A multi-lingual description is provided by this role via the International String class.
\                      +name                                A multi-lingual name is provided by this role via the International String class
InternationalString                                         The International String is a collection of Localised Strings and supports the representation of text in multiple locales.
LocalisedString                                             The Localised String supports the representation of text in one locale (locale is similar to language but includes geographic variations such as Canadian French, US English etc.).
\                      label                                Label of the string.
\                      locale                               The geographic locale of the string e.g French, Canadian French.
*VersionableArtefact*  Superclass is *NameableArtefact*     Provides versioning information for all derived objects.
                                                           
                       Base inheritance sub classes are:   
                                                           
                       MaintainableArtefact                
\                      version                              A version string following an agreed convention
\                      validFrom                            Date from which the version is valid
\                      validTo                              Date from which version is superceded
*MaintainableArtefact* Inherits from                        An abstract class to group together primary structural metadata artefacts that are maintained by an Agency.
                                                           
                       *VersionableArtefact*               
\                      final                                Defines whether a maintained artefact is draft or final.
\                      isExternalReference                  If set to “true” it indicates that the content of the object is held externally.
\                      structureURL                         The URL of an SDMX-ML document containing the external object.
\                      serviceURL                           The URL of an SDMX-compliant web service from which the external object can be retrieved.
\                      +maintainer                          Association to the Maintenance Agency responsible for maintaining the artefact.
Agency                                                      See section on “Organisations”
====================== ==================================== ===================================================================================================================================================================================

Basic Inheritance
-----------------

Class Diagram– Basic Inheritance from the Base Inheritance Classes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|image34|

Figure 10: Basic Inheritance from the Base Structures

.. _explanation-of-the-diagram-3:

Explanation of the Diagram
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _narrative-1:

Narrative
^^^^^^^^^

The diagram above shows the inheritance within the base structures. The
concrete classes are introduced and defined in the specific package to
which they relate.

Data Types
----------

.. _class-diagram-1:

Class Diagram
~~~~~~~~~~~~~

|image35|

Figure 11: Class Diagram of Basic Data Types

.. _explanation-of-the-diagram-4:

Explanation of the Diagram
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _narrative-2:

Narrative
^^^^^^^^^

The UsageStatus enumeration is used as a data type on a DataAttribute
where the value of the attribute in an instance of the class must take
one of the values in the UsageStatus (i.e. mandatory, conditional).

The FacetType and FacetValueType enumerations are used to specify the
valid format of the content of a non enumerated Concept or the usage of
a Concept when specified for use on a *Component* on a *Structure* (such
as a Dimension in a DataStructureDefinition). The description of the
various types can be found in the section on *ConceptScheme* (section
4.4).

The ActionType enumeration is used to specify the action that a
receiving system should take when processing the content that is the
object of the action. It is enumerated as follows:

-  Append

..

   Data or metadata is an incremental update for an existing
   data/metadata set or the provision of new data or documentation
   (attribute values) formerly absent. If any of the supplied data or
   metadata is already present, it will not replace that data or
   metadata. This corresponds to the "Update" value found in version 1.0
   of the SDMX Technical Standards

-  Replace

..

   Data/metadata is to be replaced, and may also include additional
   data/metadata to be appended.

-  Delete

..

   Data/Metadata is to be deleted.

-  Information

Data and metadata are for information purposes.

The IdentifiableObjectType enumeration is used to specify an object type
whose class is a sub class of IdentifiableArtefact either directly of
via NameableArtefact, VersionableArtefact or MaintainableArtefact.

The ToValueType data type contains the attributes to support
transformations defined in the StructureMap (see Section 9).

The ConstraintRoleType data type contains the attributes that identify
the purpose of a Constraint (allowableContent, actualContent).

The Item Scheme Pattern
-----------------------

Context
~~~~~~~

The Item Scheme is a basic architectural pattern that allows the
creation of list schemes for use in simple taxonomies, for example.

The ItemScheme is the basis for CategoryScheme, Codelist, ConceptScheme,
*ReportingTaxonomy*, and *OrganisationScheme*.

.. _class-diagram-2:

Class Diagram
~~~~~~~~~~~~~

|image36|

Figure 12 The Item Scheme pattern

.. _explanation-of-the-diagram-5:

Explanation of the Diagram
~~~~~~~~~~~~~~~~~~~~~~~~~~

Narratve 
^^^^^^^^^

The *ItemScheme* is an abstract class which defines a set of *Item*
(this class is also abstract). Its main purpose is to define a mechanism
which can be used to create taxonomies which can classify other parts of
the SDMX Information Model. It is derived from *MaintainableArtefact*
which gives it the ability to be annotated, have identity, naming,
versioning and be associated with an Agency. An example of a concrete
class is a CategoryScheme. The associated Category are *Items*.

In an exchange environment an ItemScheme is allowed to contain a sub-set
of the Items in the maintained *ItemScheme*. If such an *ItemScheme* is
disseminated with a sub-set of the Items then the fact that this is a
sub-set is denoted by setting the isPartial attribute to “true”.

A “partial” *ItemScheme* cannot be maintained independently in its
partial form i.e. it cannot contain *Item*\ s that are not present in
the full *ItemScheme* and the content of any one *Item* (e.g. names and
descriptions) cannot deviate from the content in the full *ItemScheme*.
Furthermore, the Id of the *ItemScheme* where isPartial is set to “true”
is the same as the Id of the full *ItemScheme* (maintenance agency, id,
version). This is important as this is the Id that that is referenced in
other structures (e.g. a Codelist referenced in a DSD) and this Id is
always the same, regardless of whether the disseminated *ItemScheme* is
the full *ItemScheme* or a partial *ItemScheme*.

The purpose of a partial *ItemScheme* is to support the exchange and
dissemination of a sub-set ItemScheme without the need to maintain
multiple *ItemScheme*\ s which contain the same *Item*\ s. For instance
when a Codelist is used in a DataStructureDefinition it is sometimes the
case that only a sub-set of the Codes in a Codelist are relevant. In
this case a partial Codelist can be constructed using the Constraint
mechanism explained later in this document.

*Item* inherits from *NameableArtefact* which gives it the ability to be
annotated and have identity, and therefore has id, uri and urn
attributes, a name and a description in the form of an
InternationalString. Unlike the parent *ItemScheme*, the *Item* itself
is not a *MaintainableArtefact* and therefore cannot have an independent
Agency (i.e. it implicitly has the same agency as the *ItemScheme*).

The *Item* can be hierarchic and so one *Item* can have child *Item*\ s.
The restriction of the hierarchic association is that a child *Item* can
have only parent *Item*.

.. _definitions-3:

Definitions
^^^^^^^^^^^

============ ======================= =============================================================================================================================================
Class        Feature                 Description
*ItemScheme* Inherits from:          The descriptive information for an arrangement or division of objects into groups based on characteristics, which the objects have in common.
                                    
             *MaintainableArtefact* 
                                    
             Direct sub classes are:
                                    
             | CategoryScheme       
             | ConceptScheme        
             | Codelist             
                                    
             ReportingTaxonomy      
                                    
             *OrganisationScheme*   
\            isPartial               Denotes whether the Item Scheme contains a sub set of the full set of Items in the maintained scheme.
\            items                   Association to the Items in the scheme.
*Item*       Inherits from:          The Item is an item of content in an Item Scheme. This may be a node in a taxonomy or ontology, a code in a code list etc.
                                    
             *NameableArtefact*      Node that at the conceptual level the Organisation is not hierarchic
                                    
             Direct sub classes are 
                                    
             | Category             
             | Concept              
             | Code                 
             | ReportingCategory    
             | *Organisation*       
\            hierarchy               This allows an Item optionally to have one or more child Items.
============ ======================= =============================================================================================================================================

The Structure Pattern
---------------------

.. _context-1:

Context
~~~~~~~

The Structure Pattern is a basic architectural pattern which allows the
specification of complex tabular structures which are often found in
statistical data (such as Data Structure Definition, and Metadata
Structure Definition). A Structure is a set of ordered lists. A pattern
to underpin this tabular structure has been developed, so that
commonalities between these structure definitions can be supported by
common software and common syntax structures.

Class Diagrams
~~~~~~~~~~~~~~

|image37|

Figure 13: The Structure Pattern

|image38|

Figure 14: Representation within the Structure Pattern

Explanation of the Diagrams
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _narrative-3:

Narrative
^^^^^^^^^

The *Structure* is an abstract class which contains a set of one or more
*ComponentList*\ (s) (this class is also abstract). An example of a
concrete *Structure* is DataStructureDefinition.

The *ComponentList* is a list of one or more *Component*\ (s*)*. The
*ComponentList* has several concrete descriptor classes based on it:
DimensionDescriptor, GroupDimensionDescriptor, MeasureDescriptor, and
AttributeDescriptor of the DataStructureDefinition and MetadataTarget,
and ReportStructure of the MetaDataStructureDefinition.

The Component is contained in a ComponentList. The type of Component in
a ComponentList is dependent on the concrete class of the ComponentList
as follows:

DimensionDescriptor: Dimension, Measure Dimension, Time Dimension

GroupDimensionDescriptor: Dimension, Measure Dimension, Time Dimension

MeasureDescriptor: PrimaryMeasure

AttributeDescriptor: Data Attribute

MetadataTarget: *TargetObject* and its sub classes

ReportStructure: MetadataAttribute

Each Component takes its semantic (and possibly also its representation)
from a Concept in a ConceptScheme. This is represented by the
conceptIdentity association to *Concept*.

The *Component* may also have a localRepresentation, This allows a
concrete class, such as Dimension, to specify its representation which
is local to the *Structure* in which it is contained (for Dimension this
will be DataStructureDefinition), and thus overrides any
coreRepresentation specified for the Concept.

The Representation can be enumerated or non-enumerated. The valid
content of an enumerated representation is specified either in an
*ItemScheme* which can be one of ConceptScheme, Codelist,
*OrganisationScheme*, CategoryScheme, and ReportingTaxonomy. The valid
content of a non-enumerated representation is specified as one or more
Facet (for example these may specify minimum and maximum values). For a
MetadataAttribute this is achieved by one of more Extended Facet which
allows the additional representation of XHTML.

The types of representation that are valid for specific components is
expressed in the model as a constraint on the association viz:

-  The MeasureDimension must be enumerated and use a ConceptScheme

-  The Dimension (but not MeasureDimension), DataAttribute,
   PrimaryMeasure, MetadataAttribute may be enumerated and, if so, use a
   Codelist

-  The *TargetObject* may be enumerated and, if so, can use any
   ItemScheme (Codelist, ConceptScheme, *OrganisationScheme*,
   CategoryScheme, ReportingTaxonomy)

-  The Dimension (but not MeasureDimension), Data Attribute,
   PrimaryMeasure, *TargetObject* may be non-enumerated and, if so, use
   one of more Facet, note that the FacetValueType applicable to the
   TimeDimension is restricted to those that represent time

-  The MetadataAttribute may be non-enumerated and, if so, uses one or
   more ExtendedFacet

The *Structure* may be used by one or more *StructureUsage*. An example
of this in terms of concrete classes is that a DataflowDefinition (sub
class of *StructureUsage*) may use a particular DataStructureDefinition
(sub class of *Structure*), and similar constructs apply for the
MetadataflowDefinition (link to MetadataStructureDefinition).

.. _definitions-4:

Definitions
^^^^^^^^^^^

================ ============================== ========================================================================================================================================================================================================================================================================================================================================================================================
Class            Feature                        Description
*StructureUsage* Inherits from:                 An artefact whose components are described by a Structure. In concrete terms (sub-classes) an example would be a Dataflow Definition which is linked to a given structure – in this case the Data Structure Definition.
                                               
                 *MaintainableArtefact*        
                                               
                 Sub classes are:              
                                               
                 | DataflowDefinition          
                 | MetadataflowDefinition      
\                structure                      An association to a Structure specifying the structure of the artefact.
*Structure*      Inherits from:                 Abstract specification of a list of lists to define a complex tabular structure. A concrete example of this would be statistical concepts, code lists, and their organisation in a data or metadata structure definition, defined by a centre institution, usually for the exchange of statistical information with its partners.
                                               
                 *MaintainableArtefact*        
                                               
                 Sub classes are:              
                                               
                 | DataStructure               
                 | Definition                  
                 | MetadataStructure Definition
\                grouping                       A composite association to one or more component lists.
*ComponentList*  Inherits from:                 An abstract definition of a list of components. A concrete example is a Dimension Descriptor which defines the list of Dimensions in a Data Structure Definition.
                                               
                 *IdentifiableArtefact*        
                                               
                 Sub classes are:              
                                               
                 | DimensionDescriptor         
                 | GroupDimension              
                 | Descriptor                  
                 | MeasureDescriptor           
                 | AttributeDescriptor         
                 | MetadataTarget              
                 | ReportStructure             
\                components                     An aggregate association to one or more components which make up the list.
*Component*      Inherits from:                 A component is an abstract super class used to define qualitative and quantitative data and metadata items that belong to a Component List and hence a Structure. Component is refined through its sub-classes.
                                               
                 *IdentifiableArtefact*        
                                               
                 Sub classes are:              
                                               
                 | *PrimaryMeasure             
                   DataAttribute               
                   DimensionComponent          
                   TargetObject*               
                 | MetadataAttribute           
\                conceptIdentity                Association to a Concept in a Concept Scheme that identifies and defines the semantic of the Component
\                localRepresentation            Association to the Representation of the Component if this is different from the coreRepresentation of the Concept which the Component uses (ConceptUsage)
*Representation*                                The allowable value or format for Component or Concept
\                +enumerated                    Association to an enumerated list that contains the allowable content for the Component when reported in a data or metadata set. The type of enumerated list that is allowed for any concrete Component is shown in the constraints on the association (e.g. Identifier Component can have any of the sub classes of Item Scheme, whereas Measure Dimension must have a Concept Scheme).
\                +nonEnumerated                 Association to a set of Facets that define the allowable format for the content of the Component when reported in a data or metadata set.
*Facet*                                         Defines the format for the content of the Component when reported in a data or metadata set.
\                facetType                      A specific content type which is constrained by the FacetType enumeration
\                facetValueType                 The format of the value of a Component when reported in a data or metadata set. This is contrained by the FacetValueType enumeration.
\                +itemSchemeFacet               Defines the format of the identifiers in an Item Scheme used by a Component. Typically this would define the number of characters (length) of the identifier.
*ExtendedFacet*                                 This has the same function as Facet but allows additionally an XHTML representation. This is constrained for use with a Metadata Attribute
================ ============================== ========================================================================================================================================================================================================================================================================================================================================================================================

The specification of the content and use of the sub classes to
*ComponentList* and *Component* can be found in the section in which
they are used (*DataStructureDefinition* and
*MetadataStructureDefinition*)

Representation Constructs
^^^^^^^^^^^^^^^^^^^^^^^^^

The majority of SDMX FacetValueTypes are compatible with those found in
XML Schema, and have equivalents in most current implementation
platforms:

========================= ======================== ======================= =======================================
**SDMX Facet Value Type** **XML Schema Data Type** **.NET Framework Type** **Java Data Type**
========================= ======================== ======================= =======================================
**String**                **xsd:string**           **System.String**       **java.lang.String**
**Big Integer**           **xsd:integer**          **System.Decimal**      **java.math.BigInteger**
**Integer**               **xsd:int**              **System.Int32**        **int**
**Long**                  **xsd.long**             **System.Int64**        **long**
**Short**                 **xsd:short**            **System.Int16**        **short**
**Decimal**               **xsd:decimal**          **System.Decimal**      **java.math.BigDecimal**
**Float**                 **xsd:float**            **System.Single**       **float**
**Double**                **xsd:double**           **System.Double**       **double**
**Boolean**               **xsd:boolean**          **System.Boolean**      **boolean**
URI                       xsd:anyURI               **System.Uri**          Java.net.URI or java.lang.String
DateTime                  xsd:dateTime             **System.DateTime**     javax.xml.datatype.XMLGregorianCalendar
Time                      xsd:time                 **System.DateTime**     javax.xml.datatype.XMLGregorianCalendar
GregorianYear             xsd:gYear                **System.DateTime**     javax.xml.datatype.XMLGregorianCalendar
GregorianMonth            xsd:gYearMonth           **System.DateTime**     javax.xml.datatype.XMLGregorianCalendar
GregorianDay              xsd:date                 **System.DateTime**     javax.xml.datatype.XMLGregorianCalendar
Day, MonthDay, Month      xsd:g\*                  **System.DateTime**     javax.xml.datatype.XMLGregorianCalendar
**Duration**              **xsd:duration**         **System.TimeSpan**     **javax.xml.datatype.Duration**
========================= ======================== ======================= =======================================

There are also a number of SDMX data types which do not have these
direct correspondences, often because they are composite representations
or restrictions of a broader data type. These are detailed in Section 6
of the standards.

The Representation is composed of Facets, each of which conveys
characteristic information related to the definition of a value domain.
Often a set of Facets are needed to convey the required semantic. For
example, a sequence is defined by a minimum of two Facets: one to define
the start value, and one to define the interval.

============ ========================================================================================================================================================================================================================================================================================================================================================================================================
Facet Type   Explanation
============ ========================================================================================================================================================================================================================================================================================================================================================================================================
isSequence   The isSequence facet indicates whether the values are intended to be ordered, and it may work in combination with the interval, startValue, and endValue facet or the timeInterval, startTime, and endTime, facets. If this attribute holds a value of true, a start value or time and a numeric or time interval must supplied. If an end value is not given, then the sequence continues indefinitely.
interval     The interval attribute specifies the permitted interval (increment) in a sequence. In order for this to be used, the isSequence attribute must have a value of true.
startValue   The startValue facet is used in conjunction with the isSequence and interval facets (which must be set in order to use this facet). This facet is used for a numeric sequence, and indicates the starting point of the sequence. This value is mandatory for a numeric sequence to be expressed.
endValue     The endValue facet is used in conjunction with the isSequence and interval facets (which must be set in order to use this facet). This facet is used for a numeric sequence, and indicates that ending point (if any) of the sequence.
timeInterval The timeInterval facet indicates the permitted duration in a time sequence. In order for this to be used, the isSequence facet must have a value of true.
startTime    The startTime facet is used in conjunction with the isSequence and timeInterval facets (which must be set in order to use this facet). This attribute is used for a time sequence, and indicates the start time of the sequence. This value is mandatory for a time sequence to be expressed.
endTime      The endTime facet is used in conjunction with the isSequence and timeInterval facets (which must be set in order to use this facet). This facet is used for a time sequence, and indicates that ending point (if any) of the sequence.
minLength    The minLength facet specifies the minimum and length of the value in characters.
maxLength    The maxLength facet specifies the maximum length of the value in characters.
minValue     The minValue facet is used for inclusive and exclusive ranges, indicating what the lower bound of the range is. If this is used with an inclusive range, a valid value will be greater than or equal to the value specified here. If the inclusive and exclusive data type is not specified (e.g. this facet is used with an integer data type), the value is assumed to be inclusive.
maxValue     The maxValue facet is used for inclusive and exclusive ranges, indicating what the upper bound of the range is. If this is used with an inclusive range, a valid value will be less than or equal to the value specified here. If the inclusive and exclusive data type is not specified (e.g. this facet is used with an integer data type), the value is assumed to be inclusive.
decimals     The decimals facet indicates the number of characters allowed after the decimal separator.
pattern      The pattern attribute holds any regular expression permitted in the implementation syntax (e.g. W3C XML Schema).
============ ========================================================================================================================================================================================================================================================================================================================================================================================================

Specific Item Schemes
=====================

.. _introduction-3:

Introduction
------------

The structures that are an arrangement of objects into hierarchies or
lists based on characteristics, and which are maintained as a group
inherit from *ItemScheme*. These concrete classes are:

-  Codelist

-  ConceptScheme

-  CategoryScheme

-  AgencyScheme, DataProviderScheme, DataConsumerScheme,
   OrganisationUnitScheme which all inherit from the abstract class
   *OrganisationScheme*

-  Reporting Taxonomy

Inheritance View
----------------

The inheritance and relationship views are shown together in each of the
diagrams in the specific sections below.

Codelist
--------

.. _class-diagram-3:

Class Diagram
~~~~~~~~~~~~~

|image39|

Figure 15 Class diagram of the Codelist

.. _explanation-of-the-diagram-6:

Explanation of the Diagram
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _narrative-4:

Narrative
^^^^^^^^^

The Codelist inherits from the *ItemScheme* and therefore has the
following attributes:

-  id

-  uri

-  urn

-  version

-  validFrom

-  validTo

-  *isExternalReference*

-  *serviceURL*

-  *structureURL*

-  final

-  isPartial

The Code inherits from *Item* and has the following attributes:

-  id

-  uri

-  urn

Both Codelist and Code have the association to InternationalString to
support a multi-lingual name, an optional multi-lingual description, and
an association to Annotation to support notes (not shown).

Through the inheritance the Codelist comprise one or more Codes, and the
Code itself can have one or more child Codes in the (inherited)
hierarchy association. Note that a child Code can have only one parent
Code in this association. A more complex HierachicalCodelist which allow
multiple parents and multiple hierarchies is described later.

A partial Codelist (where isPartial is set to “true”) is identical to a
Codelist and contains the Code and associated names and descriptions,
just as in a normal code list. However, its content is a sub set of the
full Codelist. The way this works is described in section 3.5.3.1 on
*ItemScheme*.

.. _definitions-5:

Definitions
^^^^^^^^^^^

======== ============= ====================================================================================================================================
Class    Feature       Description
Codelist Inherits from A list from which some statistical concepts (coded concepts) take their values.
                      
         *ItemScheme* 
Code     Inherits from A language independent set of letters, numbers or symbols that represent a concept whose meaning is described in a natural language.
                      
         *Item*       
\        /hierarchy    Associates the parent and the child codes.
======== ============= ====================================================================================================================================

Concept Scheme and Concepts
---------------------------

Class Diagram - Inheritance
~~~~~~~~~~~~~~~~~~~~~~~~~~~

|image40|

Figure 16 Class diagram of the Concept Scheme

.. _explanation-of-the-diagram-7:

Explanation of the Diagram
~~~~~~~~~~~~~~~~~~~~~~~~~~

The ConceptScheme inherits from the *ItemScheme* and therefore has the
following attributes:

-  id

-  uri

-  urn

-  version

-  validFrom

-  validTo

-  *isExternalReference*

-  *registryURL*

-  *structureURL*

-  *repositoryURL*

-  final

-  isPartial

Concept inherits from Item and has the following attributes:

-  id

-  uri

-  urn

Through the inheritance from *NameableArtefact* both ConceptScheme and
Concept have the association to InternationalString to support a
multi-lingual name, an optional multi-lingual description, and an
association to Annotation to support notes (not shown).

Through the inheritance from *ItemScheme* the ConceptScheme comprise one
or more Concepts, and the Concept itself can have one or more child
Concepts in the (inherited) hierarchy association. Note that a child
Concept can have only one parent Concept in this association.

A partial ConceptScheme (where isPartial is set to “true”) is identical
to a ConceptScheme and contains the Concept and associated names and
descriptions, just as in a normal ConceptScheme. However, its content is
a sub set of the full ConceptScheme. The way this works is described in
section 3.5.3.1 on ItemScheme.

Class Diagram - Relationship
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|image41|

Figure 17: Relationship class diagram of the Concept Scheme

.. _explanation-of-the-diagram-8:

Explanation of the diagram
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _narrative-5:

Narrative
^^^^^^^^^

The ConceptScheme can have one or more Concepts. A Concept can have zero
or more child Concepts, thus supporting a hierarchy of Concepts. Note
that a child Concept can have only one parent Concept in this
association. The purpose of the hierarchy is to relate concepts that
have a semantic relationship: for example a Reporting_Country and
Vis_a_Vis_Country may both have Country as a parent concept, or a
CONTACT may have a PRIMARY_CONTACT as a child concept. It is not the
purpose of such schemes to define reporting structures: these reporting
structures are defined in the MetadataStructureDefinition.

The Concept can be associated with a *coreRepresentation*. The
coreRepresentation is the specification of the format and value domain
of the Concept when used on a structure like a DataStructureDefinition
or a MetadataStructureDefinition, unless the specification of the
Representation is overridden in the relevant structure definition. In a
hierarchical ConceptScheme the Representation is inherited from the
parent Concept unless overridden at the level of the child Concept.

Note that the *ConceptScheme* is used as the *Representation* of the
*MeasureDimension* in a *DataStructureDefinition* (see 5.3.2). Each
*Concept* in this *ConceptScheme* is a specific measure, each of which
can be given a *coreRepresentation*. Thus the valid format of the
observation for each measure when reported in a data set for the
*MeasureDimension* is specified in the *Concept*. This allows a
different format for each measure. This is covered in more detail in
5.3.

The *Representation* is documented in more detail in the section on the
SDMX Base.

The *Concept* may be related to a concept described in terms of the
ISO/IEC 11179 standard. The *ISOConceptReference* identifies this
concept and concept scheme in which it is contained.

.. _definitions-6:

Definitions
^^^^^^^^^^^

=================== ================== ==============================================================================================================================================
Class               Feature            Description
ConceptScheme       Inherits from      The descriptive information for an arrangement or division of concepts into groups based on characteristics, which the objects have in common.
                                      
                    *ItemScheme*      
Concept             Inherits from      A concept is a unit of knowledge created by a unique combination of characteristics.
                                      
                    *Item*            
\                   /hierarchy         Associates the parent and the child concept.
\                   coreRepresentation Associates a Representation.
\                   +ISOConcept        Association to an ISO concept reference.
ISOConceptReference                    The identity of an ISO concept definition.
\                   conceptAgency      The maintenance agency of the concept scheme containing the concept.
\                   conceptSchemeID    The identifier of the concept scheme.
\                   conceptID          The identifier of the concept.
=================== ================== ==============================================================================================================================================

Category Scheme
---------------

.. _context-2:

Context
~~~~~~~

This package defines the structure that supports the definition of and
relationships between categories in a category scheme. It is similar to
the package for concept scheme. An example of a category scheme is one
which categorises data – sometimes known as a subject matter domain
scheme or a data category scheme. Importantly, as will be seen later,
the individual nodes in the scheme (the “categories”) can be associated
to any set of IdentiableArtefacts in a Categorisation.

.. _class-diagram---inheritance-1:

Class diagram - Inheritance
~~~~~~~~~~~~~~~~~~~~~~~~~~~

|image42|

Figure 18 Inheritance Class diagram of the Category Scheme

.. _explanation-of-the-diagram-9:

Explanation of the Diagram
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _narrative-6:

Narrative
^^^^^^^^^

The categories are modelled as a hierarchical *ItemScheme*. The
CategoryScheme inherits from the *ItemScheme* and has the following
attributes:

-  id

-  uri

-  urn

-  version

-  validFrom

-  validTo

-  *isExternalReference*

-  *structureURL*

-  *serviceURL*

-  final

-  isPartial

Category inherits from *Item* and has the following attributes:

-  id

-  uri

-  urn

Both CategoryScheme and Category have the association to
InternationalString to support a multi-lingual name, an optional
multi-lingual description, and an association to Annotation to support
notes (not shown on the model).

Through the inheritance the CategoryScheme comprise one or more
Categorys, and the Category itself can have one or more child Category
in the (inherited) hierarchy association. Note that a child Category can
have only one parent Category in this association.

A partial CategoryScheme (where isPartial is set to “true”) is identical
to a CategoryScheme and contains the Category and associated names and
descriptions, just as in a normal CategoryScheme. However, its content
is a sub set of the full CategoryScheme. The way this works is described
in section 3.5.3.1 on ItemScheme.

.. _class-diagram---relationship-1:

Class diagram - Relationship
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|image43|

Figure 19: Relationship Class diagram of the Category Scheme

The CategoryScheme can have one or more Categorys. The Category is
Identifiable and has identity information. A Category can have zero or
more child Categorys, thus supporting a hierarchy of Categorys. Any
IdentifiableArtefact can be +categorisedBy a Category. This is achieved
by means of a Categorisation. Each Categorisation can associate one
IdentifiableArtefact with one Category. Multiple Categorisations can be
used to build a set of IdentifiableArtefacts that are +categorisedBy the
same Category. Note that there is no navigation (i.e. no embedded
reference) to the Categorisation from the Category. From an
implementation perspective this is necessary as Categorisation has no
affect on the versioning of either the Category or the
IdentifiableArtefact.

.. _definitions-7:

Definitions
^^^^^^^^^^^

============== ==================== =========================================================================================================================================================================
Class          Feature              Description
CategoryScheme Inherits from        The descriptive information for an arrangement or division of categories into groups based on characteristics, which the objects have in common.
                                   
               *ItemScheme*        
\              /items               Associates the categories.
Category       Inherits from        An item at any level within a classification, typically tabulation categories, sections, subsections, divisions, subdivisions, groups, subgroups, classes and subclasses.
                                   
               *Item*              
\              /hierarchy           Associates the parent and the child Category.
Categorisation Inherits from        Associates an IdentifableArtefact with a Category.
                                   
               MaintainableArtefact
\              +categorisedArtefact Associates the IdentifableArtefact.
\              +categorisedBy       Associates the Category.
============== ==================== =========================================================================================================================================================================

Organisation Scheme
-------------------

.. _class-diagram-4:

Class Diagram
~~~~~~~~~~~~~

|image44|

Figure 20 The Organisation Scheme class diagram

.. _explanation-of-the-diagram-10:

Explanation of the Diagram
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _narrative-7:

Narrative
^^^^^^^^^

The *OrganisationScheme* is abstract. It contains *Organisation* which
is also abstract. The Organisation can have child Organisation.

The *OrganisationScheme* can be one of four types:

1. AgencyScheme – contains Agency which is restricted to a flat list of
   agencies (i.e. there is no hierarchy). Note that the SDMX system of
   (Maintenance) Agency can be hierarchic and this is explained in more
   detail in the separate document “Technical Notes”.

2. DataProviderScheme – contains DataProvider which is restricted to a
   flat list of agencies (i.e. there is no hierarchy).

3. DataConsumerScheme – contains DataConsumer which is restricted to a
   flat list of agencies (i.e. there is no hierarchy).

4. OrganisationUnitScheme – contains OrganisationUnit which does inherit
   the /hierarchy association from Organisation.

Reference metadata can be attached to the *Organisation* by means of the
metadata attachment mechanism. This mechanism is explained in the
Reference Metadata section of this document (see section 7). This means
that the model does not specify the specific reference metadata that can
be attached to a DataProvider, DataConsumer,OrganisationUnit or Agency,
except for limited Contact information.

A partial *OrganisationScheme* (where isPartial is set to “true”) is
identical to a *OrganisationScheme* and contains the Organisation and
associated names and descriptions, just as in a normal
*OrganisationScheme* However, its content is a sub set of the full
*OrganisationScheme*. The way this works is described in section 3.5.3.1
on ItemScheme.

.. _definitions-8:

Definitions
^^^^^^^^^^^

====================== ======================= ============================================================================================================================================================================================================================
Class                  Feature                 Description
*OrganisationScheme*   Abstract Class          A maintained collection of Organisations.
                                              
                       Inherits from          
                                              
                       *ItemScheme*           
                                              
                       Sub classes are:       
                                              
                       *AgencyScheme          
                       DataProviderScheme     
                       DataConsumerScheme     
                       OrganisationUnitScheme*
\                      /items                  Association to the Organisations in the scheme.
*Organisation*         Inherits from           An organisation is a unique framework of authority within which a person or persons act, or are designated to act, towards some purpose.
                                              
                       *Item*                 
                                              
                       Sub classes are:       
                                              
                       *Agency                
                       DataProvider           
                       DataConsumer           
                       OrganisationUnit*      
\                      +contact                Association to the Contact information.
\                      /hierarchy              Association to child Organisations.
Contact                                        An instance of a role of an individual or an organization (or organization part or organization person) to whom an information item(s), a material object(s) and/or person(s) can be sent to or from in a specified context.
\                      name                    The designation of the Contact person by a linguistic expression.
\                      organisationUnit        The designation of the organisational structure by a linguistic expression, within which Contact person works.
\                      responsibility          The function of the contact person with respect to the organisation role for which this person is the Contact.
\                      telephone               The telephone number of the Contact.
\                      fax                     The fax number of the Contact.
\                      email                   The Internet e-mail address of the Contact.
\                      X400                    The X400 address of the Contact.
\                      uri                     The URL address of the Contact.
AgencyScheme                                   A maintained collection of Maintenace Agencies.
\                      /items                  Association to the Maintenance Agency in the scheme.
DataProviderScheme                             A maintained collection of Data Providers.
\                      /items                  Association to the Data Providers in the scheme.
DataConsumerScheme                             A maintained collection of Data Consumers.
\                      /items                  Association to the Data Consumers in the scheme.
OrganisationUnitScheme                         A maintained collection of Organisation Units.
\                      /items                  Association to the Organisation Units in the scheme.
Agency                 Inherits from           Responsible agency for maintaining artefacts such as statistical classifications, glossaries, structural metadata such as Data and Metadata Structure Definitions, Concepts and Code lists.
                                              
                       *Organisation*         
DataProvider           Inherits from           An organisation that produces data or reference metadata.
                                              
                       *Organisation*         
DataConsumer           Inherits from           An organisation using data as input for further processing.
                                              
                       *Organisation*         
OrganisationUnit       Inherits from           A designation in the organisational structure.
                                              
                       *Organisation*         
\                      /hierarchy              Association to child Organisation Units
====================== ======================= ============================================================================================================================================================================================================================

Reporting Taxonomy
------------------

.. _class-diagram-5:

Class Diagram
~~~~~~~~~~~~~

|image45|

Figure 21: Class diagram of the Reporting Taxonomy

.. _explanation-of-the-diagram-11:

Explanation of the Diagram
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _narrative-8:

Narrative
^^^^^^^^^

In some data reporting environments, and in particular those in primary
reporting, a report may comprise a variety of heterogeneous data, each
described by a different *Structure*. Equally, a specific disseminated
or published report may also comprise a variety of heterogeneous data.
The definition of the set of linked sub reports is supported by the
ReportingTaxonomy.

The ReportingTaxonomy is a specialised form of ItemScheme. Each
ReportingCategory of the ReportingTaxonomy can link to one or more
*StructureUsage* which itself can be one of DataflowDefinition, or
MetadataflowDefinition, and one or more *Structure*, which itself can be
one of DataStructureDefinition or MetadataStructureDefinition. It is
expected that within a specific ReportingTaxonomy each Category that is
linked in this way will be linked to the same class (e.g. all Category
in the scheme will link to a DataflowDefinition). Note that a
ReportingCategory can have child ReportingCategory and in this way it is
possible to define a hierarchical ReportingTaxonomy. It is possible in
this taxonomy that some ReportingCategory are defined just to give a
reporting structure. For instance:

Section 1

1. linked to DatafowDefinition_1

2 linked to DatafowDefinition_2

Section 2

1 linked toDatafowDefinition_3

2 linked to DatafowDefinition_4

Here, the nodes of Section 1 and Section 2 would not be linked to
DataflowDefinition but the other would be linked to a DataflowDefinition
(and hence the DataStructureDefinition).

A partial ReportingTaxonomy (where isPartial is set to “true”) is
identical to a ReportingTaxonomy and contains the ReportingCategory and
associated names and descriptions, just as in a normal ReportingTaxonomy
However, its content is a sub set of the full ReportingTaxonomy The way
this works is described in section 3.5.3.1 on ItemScheme.

.. _definitions-9:

Definitions
^^^^^^^^^^^

================= ============= ====================================================================================================================================================================================================
Class             Feature       Description
ReportingTaxonomy Inherits from A scheme which defines the composition structure of a data report where each component can be described by an independent Dataflow Definition or Metdataflow Definition.
                               
                  *ItemScheme* 
\                 items         Associates the Reporting Category
ReportingCategory Inherits from A component that gives structure to the report and links to data and metadata.
                               
                  *Item*       
\                 hierarchy     Associates child Reporting Category.
\                 +flow         Association to the data and metadata flows that link to metadata about the provisioning and related data and metadata sets, and the structures that define them.
\                 +structure    Association to the Data Structure Definition and Metadata Structure Definitions which define the structural metadata describing the data and metadata that are contained at this part of the report.
================= ============= ====================================================================================================================================================================================================

Data Structure Definition and Dataset
=====================================

.. _introduction-4:

Introduction
------------

The DataStructureDefiniton is the class name for a structure definition
for data. Some organisations know this type of definition as a “Key
Family” and so the two names are synonymous. The term Data Structure
Definition (also referred to as DSD) is used in this specification.

Many of the constructs in this layer of the model inherit from the SDMX
Base Layer. Therefore, it is necessary to study both the inheritance and
the relationship diagrams to understand the functionality of individual
packages. In simple sub models these are shown in the same diagram, but
are omitted from the more complex sub models for the sake of clarity. In
these cases, the inheritance diagram below shows the full inheritance
tree for the classes concerned with data structure definitions.

There are very few additional classes in this sub model other than those
shown in the inheritance diagram below. In other words, the SDMX Base
gives most of the structure of this sub model both in terms of
associations and in terms of attributes. The relationship diagrams shown
in this section show clearly when these associations are inherited from
the SDMX Base (see the Appendix “A Short Guide to UML in the SDMX
Information Model” to see the diagrammatic notation used to depict
this).

The actual SDMX Base construct from which the concrete classes inherit
depends upon the requirements of the class for:

-  Annotation - *AnnotableArtefact*

-  Identification - *IdentifiableArtefact*

-  Naming - *NameableArtefact*

-  Versioning – *VersionableArtefact*

-  Maintenance - *MaintainableArtefact*

.. _inheritance-view-1:

Inheritance View
----------------

.. _class-diagram-6:

Class Diagram
~~~~~~~~~~~~~

|image46|

Figure 22 Class inheritance in the Data Structure Definition and Data Set Packages

.. _explanation-of-the-diagram-12:

Explanation of the Diagram
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _narrative-9:

Narrative
^^^^^^^^^

Those classes in the SDMX metamodel which require annotations inherit
from *AnnotableArtefact* . These are:

-  IdentifiableArtefact

-  DataSet (and therefore StructureSpecificDataSet, GenericDataSet,
   GenericTimeSeriesDataSet StructureSpecificTimeSeriesDataSet)

-  Key (and therefore SeriesKey and GroupKey)

Those classes in the SDMX metamodel which require annotations and global
identity are derived from *IdentifiableArtefact* . These are:

-  NameableArtefact

-  ComponentList

-  Component

Those classes in the SDMX metamodel which require annotations, global
identity, multilingual name and multilingual description are derived
from *NameableArtefact* . These are:

-  VersionableArtefact

-  Item

The classes in the SDMX metamodel which require annotations, global
identity, multilingual name and multilingual description, and versioning
are derived from *VersionableArtefact* . These are:

-  *MaintainableArtefact*

Abstract classes which represent information that is maintained by
Maintenance Agencies all inherit from *MaintainableArtefact*, they also
inherit all the features of a *VersionableArtefact*, and are:

-  *StructureUsage*

-  *Structure*

-  *ItemScheme*

All the above classes are abstract. The key to understanding the class
diagrams presented in this section are the concrete classes that inherit
from these abstract classes.

Those concrete classes in the SDMX Data Structure Definition and Dataset
packages of the metamodel which require to be maintained by Agencies all
inherit (via other abstract classes) from *MaintainableArtefact*, these
are:

-  DataflowDefinition

-  DataStructureDefinition

The component structures that are lists of lists, inherit directly from
*Structure*. A *Structure* contains several lists of components. The
concrete class that inherits from Structure is:

-  DataStructureDefinition

A DataStructureDefinition contains a list of dimensions, a list of
measures and a list of attributes.

The concrete classes which inherit from *ComponentList* and are sub
components of the DataStructureDefinition are:

-  DimensionDescriptor – content is Dimension, MeasureDimension and Time
   Dimension

-  DimensionGroupDescriptor – content is an association to Dimension,
   MeasureDimension, TimeDimension

-  MeasureDescriptor – content is PrimaryMeasure

-  AttributeDescriptor – content is DataAttribute

The classes that inherit from *Component* are:

-  *PrimaryMeasure*

-  DimensionComponent and thereby its sub classes of Dimension,
   MeasureDimension, and TimeDimension

-  DataAttribute

The class that inherit from DataAttribute is:

-  ReportingYearStartDay

The concrete classes identified above are the majority of the classes
required to define the metamodel for the DataStructureDefinition. The
diagrams and explanations in the rest of this section show how these
concrete classes are related in order to support the functionality
required.

Data Structure Definition – Relationship View
---------------------------------------------

.. _class-diagram-7:

Class Diagram 
~~~~~~~~~~~~~~

|image47|

Figure 23 Relationship class diagram of the Data Structure Definition excluding representation

.. _explanation-of-the-diagrams-1:

Explanation of the Diagrams
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _narrative-10:

Narrative
^^^^^^^^^

A DataStructureDefinition defines the Dimensions, MeasureDimension,
TimeDimension, *DataAttribute*\ s, and PrimaryMeasure, and associated
Representation that comprise the valid structure of data and related
attributes that are contained in a DataSet, which is defined by a
DataflowDefinition.

The DataflowDefinition may also have additional metadata attached that
defines qualitative information and Constraints on the use of the
DataStructureDefinition such as the sub set of Codes used in a Dimension
(this is covered later in this document – see “Data Constraints and
Provisioning” section 9). Each DataflowDefinition has a maximum of one
DataStructureDefinition specified which defines the structure of any
DataSets to be reported/disseminated.

There are three types of dimension each having a common association to
Concept:

-  Dimension

-  MeasureDimension

-  TimeDimension

Note that In the description here *DimensionComponent* can be oany or
all of its sub classes i.e. Dimension, MeasureDimension, TimeDimension.,
and the term “DataAttribute” refers to both DataAttribute and its sub
class ReportingYearStartDate.

The *DimensionComponent*, *DataAttribute*, and *PrimaryMeasure* link to
the Concept that defines its name and semantic (/conceptIdentity
association to Concept). The *DataAttribute*, Dimension, and
*MeasureDimension* (but not *TimeDimension*) can optionally have a
+conceptRole association with a Concept that identifies its role in the
DataStructureDefinition. Therefore, the allowable roles of a Concept are
maintained in a ConceptScheme. Examples of roles are: geography, entity,
count, unit of measure. The use of these roles is to enable applications
to process the data in a meaningful way (e.g. relating a dimension value
to a mapping vector). It is expected that communities (such as the
official statistics community) will harmonise these roles with their
community so that data can be exchanged and shared in a meaningful way
in the community.

The valid values for a *DimensionComponent*, PrimaryMeasure, or
*DataAttribute*, when used in this DataStructureDefinition, are defined
by the Representation. This Representation is taken from the Concept
definition (coreRepresentation) unless it is overridden in this
DataStructureDefinition (localRepresentation) – see Figure 23. Note that
for the MeasureDimension the Representation must be a ConceptScheme and
this must always be referenced from the MeasureDimension and cannot
therefore be defaulted to the Representation of the Concept associated
by the/conceptIdentity. Note also that TimeDimension and
ReportingYearStartDate are constrained to specific FacetValueTypes

There will always be a DimensionDescriptor grouping that identifies all
of the Dimension comprising the full key. Together the Dimensions
specify the key of an Observation.

The *DimensionComponent* can optionally be grouped by multiple
GroupDimensionDescriptors each of which identifies the group of
Dimensions that can form a partial key. The GroupDimensionDescriptor
must be identified (GroupDimensionDescriptor.id) and this is used in the
GroupKey of the DataSet to declare which *DataAttribute*\ s are reported
at this group level in the DataSet.

There may be a maximum of one MeasureDimension specified in the
DimensionDescriptor. The purpose of a MeasureDimension is to specify
formally the meaning of the measures (because the PrimaryMeasure
typically has a generic meaning e.g. observation value) and to enable
multiple measures to be defined and reported in a
*StructureSpecificDataSet*. Note that the MeasureDimension references a
ConceptScheme as its Representation (see later) whereas a Dimension can
have either an enumerated (Codelis*t*) or non-enumerated (Facet)
representation. For a MeasureDimension the Concepts in the ConceptScheme
comprise the list of allowable measures. This enables the representation
for each individual measure (Concept) to be declared as the
coreRepresentation of the Concept, thus overriding the Representation
specified for the PrimaryMeasure for the observation value of this
*Measure*\ Dimension *Concept.*

There can be a maximum of one TimeDimension specified in the
DimensionDescriptor. The TimeDimension is used to specify the Concept
used to convey the time period of the observation in a data set. The
TimeDimension must contain a valid representation of time and cannot be
coded

The Primary\ *Measure* is the observable phenomenon, and, although there
can be only one PrimaryMeasure, for consistency with the
ComponentList/Component pattern it is grouped by a MeasureDescriptor.

The *DataAttribute* defines a characteristic of data that are collected
or disseminated and is grouped in the DataStructureDefinition by a
single AttributeDescriptor. The *DataAttribute* can be specified as
being mandatory, or conditional, as defined in usageStatus. The
*DataAttribute* may play a specific role in the structure and this is
specified by the *+role* association to the *Concept* that identifies
its role.

A *DataAttribute* is specified as being +relatedTo an
AttributeRelationship which defines the constructs to which the
DataAttribute is to be reported present in a *DataSet*. The
*DataAttribute* can be specified as being related to one of the
following artefacts:

-  DataSet (NoSpecifiedRelationship)

-  Dimension or set of Dimensions (DimensionRelationship)

-  Set of Dimensions specified by a GroupKey (GroupRelationship – this
   is retained for compatibility reasons – or +groupKey of the
   DimensionRelationship)

-  Observation (PrimaryMeasureRelationship)

|image48|

Figure 24: Attribute Attachment Defined in the Data Structure Definition

The following table details the possible relationships a DataAttribute
may specify. Note that these relationships are mutually exclusive, and
therefore only one of the following is possible.

================ ============================================================================================================================================================================================================================================================================================== ==========================================================================================================================================================================
**Relationship** **Meaning**                                                                                                                                                                                                                                                                                    **Location in Data Set at which the Attribute is reported**
================ ============================================================================================================================================================================================================================================================================================== ==========================================================================================================================================================================
None             The value of the attribute does not vary with the values of any other Component.                                                                                                                                                                                                               The attribute is reported at the level of the Dataset Attribute.
Dimension (1..n) The value of the attribute will vary with the value(s) of the referenced Dimension(s). In this case, Group(s) to which the attribute should be attached may optionally be specified.                                                                                                           The attribute is reported at the lowest level of the Dimension to which the Attribute is related, otherwise at the level of the Group if Attachment Group(s) is specified.
Group            The value of the Attribute varies with combination of values for all of the Dimensions contained in the Group. This is added as a convenience to listing all Dimensions and the attachment Group, but should only be used when the Attribute value varies based on all Group Dimension values. The attribute is reported at the level of Group.
Primary Measure  The value of the Attribute varies with the observed value.                                                                                                                                                                                                                                     The attribute is reported at the level of Observation.
================ ============================================================================================================================================================================================================================================================================================== ==========================================================================================================================================================================

|image49|

Figure 25: Representation of DSD Components

Each of Dimension, MeasureDimension, TimeDimension, PrimaryMeasure, and
*DataAttribute* can have a *Representation* specified (using the
localRepresentation association). If this is not specified in the
DataStructureDefinition then the representation specified for Concept
(coreRepresentation) is used. For the *MeasureDimension* the
representation for the individual measures is specified for the
*Concept* in the *ConceptScheme* referenced by the *MeasureDimension*.

A DataStructureDefinition can be extended to form a derived
DataStructureDefinition. This is supported in the StructureMap.

.. _definitions-10:

Definitions
^^^^^^^^^^^
.. _table_demo1:
.. list-table:: The general table 1
  :align: center
  :width: 100%
  :widths: 20 20 60
  :header-rows: 1

  * - Class
    - Feature
    - Description
  * - StructureUsage
    - 
    - See “SDMX Base”.
  * - DataflowDefinition
    - Inherits from *StructureUsage*
    - Abstract concept (i.e. the structure without any data) of a flow of data that providers will provide for different reference periods.
  * - DataStructureDefinition
    - 
    - A collection of metadata concepts, their structure and usage when used to collect or disseminate data.
  * - 
    - /grouping
    - An association to a set of metadata concepts that have an identified structural role in a Data Structure Definition.
  * - GroupDimensionDescriptor
    - Inherits from *ComponentList*
    - A set metadata concepts that define a partial key derived from the Dimension Descriptor in a Data Structure Definition.
  * -
    - +constraint
    - Identifies an Attachment Constraint that specifies the sub set of Dimension, Measure, or Attribute values to which an Attribute can be attached.
  * -
    - /components
    - An association to the Dimension and Measure Dimension components that comprise the group.
  * - DimensionDescriptor
    - Inherits from *ComponentList*
    - An ordered set of metadata concepts that, combined, classify a statistical series, and whose values, when combined (the key) in an instance such as a data set, uniquely identify a specific observation.
  * - 
    - /components
    - An association to the Dimension, Measure Dimension, and Time Dimension comprising the Key Descriptor.
  * - AttributeDescriptor
    - Inherits from *ComponentList*
    - A set metadata concepts that define the attributes of a Data Structure Definition.
  * - 
    - /components
    - An association to a Data Attribute component.
  * - MeasureDescriptor
    - Inherits from *ComponentList*
    - A metadata concept that defines the measure of a Data Structure Definition.
  * - 
    - /components
    - 
  * - Dimension
    - Inherits from *Component*
    - A metadata concept used (most probably together with other metadata concepts) to classify a statistical series, e.g. a statistical concept indicating a certain economic activity or a geographical reference area.
  * - 
    - /role
    - Association to the Concept that specifies the role that that the Dimension plays in the Data Structure Definition. 
  * - 
    - /conceptIdentity
    - An association to the metadata concept which defines the semantic of the Dimension.
  * - MeasureDimension
    - Inherits from *Dimension*
    - A statistical concept that identifies the component in the key structure that has an enumerated list of measures. This dimension has, as its representation the Concept Scheme that enumerates the measure concepts.
  * - TimeDimension
    - Inherits from *Dimension*
    - A metadata concept that identifies the component in the key structure that has the role of “time”.
  * - DataAttribute
    - Inherits from *Component*; Sub class *ReportingYear*, *StartDay*
    - A characteristic of an object or entity.
  * - 
    - 
    - 
  * - 
    - 
    - 
  * - 
    - 
    - 
  * - 
    - 
    - 
  * - 
    - 
    - 
  * - 
    - 
    - 
  * - 
    - 
    - 
  * - 
    - 
    - 
  * - 
    - 
    - 
  * - 
    - 
    - 
  * - 
    - 
    - 
  * - 
    - 
    - 

**THIS IS AN ALTERNATE WAY OF CREATING TABLES THAT IS MORE CUMBERSONE
BUT ALLOWS FOR MUCH MORE FLEXIBILITY SUCH AS MULTI-LINE AND LISTS
ETC.**

.. _table_demo2:
.. table:: The general table 2
  :align: center
  :width: 100%
  :widths: 20, 20, 60

  +--------------------+------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
  |       Class        |     Feature                        |                                                              Description                                                              |
  +====================+====================================+=======================================================================================================================================+
  | StructureUsage     | Feature                            | See “SDMX Base”.                                                                                                                      |
  +--------------------+------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
  | DataflowDefinition | Inherits from                      | Abstract concept (i.e. the structure without any data) of a flow of data that providers will provide for different reference periods. |
  |                    |                                    |                                                                                                                                       |
  |                    | StructureUsage                     |                                                                                                                                       |
  +--------------------+------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+

The explanation of the classes, attributes, and associations comprising
the Representation is described in the section on the SDMX Base.

Data Set – Relationship View
----------------------------

.. _context-3:

Context
~~~~~~~

A data set comprises the collection of data values and associated
metadata that are collected or disseminated according to a known
DataStructureDefinition.

.. _class-diagram-8:

Class Diagram
~~~~~~~~~~~~~

|image50|

Figure 26 Class Diagram of the Data Set

.. _explanation-of-the-diagram-13:

Explanation of the Diagram
~~~~~~~~~~~~~~~~~~~~~~~~~~

Narrative – Data Set
^^^^^^^^^^^^^^^^^^^^

Note that the *DataSet* must conform to the DataStructureDefinition
associated to the DataflowDefinition for which this DataSet is an
“instance of data”. Whilst the model shows the association to the
classes of the DataStructureDefinition, this is for conceptual purposes
to show the link to the DataStructureDefinition. In the actual DataSet
as exchanged there must, of course, be a reference to the
DataStructureDefinition and optionally a DataflowDefinition, but the
DataStructureDefinition is not necessarily exchanged with the data.
Therefore, the DataStructureDefinition classes are shown in the grey
areas, as these are not a part of the *DataSet* when the DataSet is
exchanged. However, the structural metadata in the
*DataStructureDefinition* can be used by an application to validate the
contents of the *DataSet* in terms of the valid content of a *KeyValue*
as defined by the Representation in the *DataStructureDefinition*.

An organisation playing the role of DataProvider can be responsible for
one or more *DataSet*.

A *DataSet* can be formatted either as a generic data set
(GenericDataSet, GenericTimeseriesDataSet) or a DataStructureDefinition
specific data set (StructureSpecificDataSet,
StructureSpecificTimeseriesDataSet). The generic data set is structured
in exactly the same way no matter which DataStructureDefinition the
DataSet expresses. The structured data set is structured according to
one specific DataStructureDefinition. Depending on the syntax chosen for
the implementation the structured data set should support better
validation at the syntax level.

A *DataSet* is a collection of a set of *Observation*\ s that share the
same dimensionality, which is specified by a set of unique components
(Dimension, MeasureDimension, TimeDimension) defined in the
DimensionDescriptor of the DataStructureDefinition, together with
associated *AttributeValue*\ s that define specific characteristics
about the artefact to which it is attached. - DataSet, Observation, set
of *Dimension*\ s. It is structured in terms of a SeriesKey to which
*Observation*\ s are reported.

The Observation can be the value of the variable being measured for the
Concept associated to the Primary\ *Measure* in the MeasureDescriptor of
the DataStructureDefinition. This is true when there is no
MeasureDimension that specifies the precise meaning of each Observation.
Each Observation associates an ObservationValue with a KeyValue
(+observationDimension) which is the value for the “Dimension at the
Observation Level”. Any dimension can be specified as being the
“Dimension at the Observation Level”, and this specification is made at
the level of the *DataSet* (i.e. it must be the same dimension for the
entire *DataSet*).

If the “Dimension at the Observation Level” is the MeasureDimension it
is possible (but not mandatory) that an Observation can be reported with
an explicit identification of one or more Concept in the ConceptScheme
referenced by the MeasureDimension as its Representation. In other
words, the actual Concepts are explicitly stated in the Observation.

If it is required to specify explicitly that the DataSet is time series
then one of GenericTimeSeriesDataSet or
StructureSpecificTimeSeriesDataSet is used and the *KeyValue* for the
+observationDimension must be a TimeKeyValue. In a GenericDataSet and a
StructureSpecificDataSet it is permissible to have any dimension as the
+observationDimension including the TimeDimension.

The *KeyValue* is a value for one of MeasureDimension, TimeDimension, or
Dimension specified in the DataStructureDefinition. If it is a Dimension
it can be coded (CodedKeyValue) or uncoded (UncodedKeyValue). If it is a
MeasureDimension then it is MeasureKeyValue. If it is TimeDimension then
it is a TimeKeyValue. The actual value that the CodedDimensionValue can
take must be one of the Codes in the Codelist specified as the
Representation of the Dimension in the DataStructureDefinition. The
actual value that the MeasureDimensionValue can take must be a valid
representation specified for the Concept in the ConceptScheme to which
this MeasureDimensionValue is related (+valueFor).

The ObservationValue can be coded - this is the CodedObservation – or it
can be uncoded – this is the UncodedObservation.

The GroupKey is a sub unit of the *Key* that has the same dimensionality
as the SeriesKey, but defines a subset of the KeyValues of the
SeriesKey. Its sub dimension structure is defined in the
GroupDimensionDescriptor of the DataStructureDefinition identified by
the same id as the GroupKey. The id identifies a “type” of group and the
purpose of the GroupKey is to report one or more AttributeValue that are
contained at this group level. The GroupKey is present when the
GroupDimensionDescriptor is related to the GroupRelationship in the
DataStructureDefinition. There can be many types of groups in a
*DataSet*. If the Group is related to the DimensionRelationship in the
DataStructureDefinition then the AttributeValue will be reported with
the appropriate dimension in the SeriesKey or Observation.

In this way each of *DataSet*, SeriesKey, GroupKey, and Observation can
have zero or more AttributeValue that defines some metadata about the
object to which it is associated. The allowable Concepts and the objects
to which these metadata can be associated (attached) are defined in the
DataStructureDefinition.

The *AttributeValue* links to the object type (DataSet, SeriesKey,
GroupKey, Observation,) to which it is associated.

.. _definitions-11:

Definitions
^^^^^^^^^^^

================== ========================= =====================================================================================================================================================================================================================================================================================
Class              Feature                   Description
*DataSet*          Abstract Class            An organised collection of data.
                                            
                   Sub classes              
                                            
                   GenericDataSet           
                                            
                   StructureSpecificDataSet 
                                            
                   | GenericTime            
                   | SeriesDataSet          
                                            
                   | StructureSpecificTime  
                   | SeriesDataSet          
\                  reportingBegin            A specific time period in a known system of time periods that identifies the start period of a report.
\                  reportingEnd              A specific time period in a known system of time periods that identifies the end period of a report.
\                  dataExtractionDate        A specific time period that identifies the date and time that the data are extracted from a data source.
\                  validFrom                 Indicates the inclusive start time indicating the validity of the information in the data set.
\                  validTo                   Indicates the inclusive end time indicating the validity of the information in the data set.
\                  publicationYear           Specifies the year of publication of the data or metadata in terms of whatever provisioning agreements might be in force.
\                  publicationPeriod         Specifies the period of publication of the data or metadata in terms of whatever provisioning agreements might be in force.
\                  setId                     Provides an identification of the data set.
\                  action                    Defines the action to be taken by the recipient system (update, append, delete)
\                  describedBy               Associates a data flow definition and thereby a Data Structure Definition to the data set.
\                  +structuredBy             Associates the Data Structure Definition that defines the structure of the Data Set. Note that the Data Structure Definition is the same as that associated (non-mandatory) to the Dataflow Definition.
\                  +publishedBy              Associates the Data Provider that reports/publishes the data.
\                  +attachedAttribute        Association to the Attribute Values relating to the Data Set
GenericDataSet                               A data format structure that is able to contain data corresponding to any Data Structure Definition.
StructureSpecific                            A data format structure that contains data corresponding to one specific Data Structure Definition.
DataSet                                     
GenericTimeseries                            A data format structure that is able to contain timeseries data corresponding to any Data Structure Definition.
DataSet                                     
StructureSpecific                            A data format structure that contains timeseries data corresponding to one specific Data Structure Definition.
TimeseriesDataSet                           
Key                Abstract class            Comprises the cross product of values of dimensions that identify uniquely an Observation.
                                            
                   Sub classes              
                                            
                   | SeriesKey              
                   | GroupKey               
\                  keyValues                 Association to the individual Key Values that comprise the Key.
\                  +attachedAttribute        Association to the Attribute Values relating to the Series Key or Group Key.
*KeyValue*         Abstract class            The value of a component of a key such as the value of the instance a Dimension in a Dimension Descriptor of a Data Structure Definition.
                                            
                   Sub classes              
                                            
                   MeasureKeyValue          
                                            
                   TimeKeyValue             
                                            
                   | CodedKeyValue          
                   | UncodedKeyValue        
\                  +valueFor                 Association to the key component in the Data Structure Definition for which this Key Value is a valid representation.
                                            
                                             Note that this is conceptual association as the key component is identified explicitly in the data set.
MeasureKeyValue    Inherits from             The value of the Measure Dimension component of the key. The value is the Concept to which this class is associated.
                                            
                   *KeyValue*               
\                  +value                    Association to the Concept.
                                            
                                             Note that this is a conceptual association showing that the Concept must exist in the Concept Scheme associated with the Measure Dimension in the Data Structure Definition. In the actual Data Set the value of the Concept is placed in the Key Value.
TimeKeyValue       Inherits from             The value of the Time Dimension component of the key.
                                            
                   *KeyValue*               
CodedKeyValue      Inherits from             The value of a coded component of the key. The value is the Code to which this class is associated.
                                            
                   *KeyValue*               
\                  +value                    Association to the Code.
                                            
                                             Note that this is a conceptual association showing that the Code must exist in the Code list associated with the Dimension in the Data Structure Definition. In the actual Data Set the value of the Code is placed in the Key Value.
UnCodedKeyValue    Inherits from             The value of an uncoded component of the key.
                                            
                   *KeyValue*               
\                  value                     The value of the key component.
\                  startTime                 This attribute is only used if the textFormat of the attribute is of the Timespan type in the Data Structure Definition (in which case the value field takes a duration).
\                  +valueFor                 Associates Dimension, Measure Dimension, or Time Dimension to the Key Value, and thereby to the Concept that is the semantic of the Dimension, or Time Dimension.
GroupKey           Inherits from             A set of Key Values that comprise a partial key, of the same dimensionality as the Time Series Key for the purpose of attaching Data Attributes.
                                            
                   Key                      
\                  +describedBy              Associates the Group Dimension Descriptor defined in the Data Structure Definition.
SeriesKey          Inherits from             Comprises the cross product of values of all the Key Values that, together with the Key Value of the +observation Dimension identify uniquely an Observation.
                                            
                   Key                      
\                  +describedBy              Associates the Dimension Descriptor defined in the Data Structure Definition.
*Observation*                                The value of the observed phenomenon in the context of the Key Values comprising the key.
\                  +valueFor                 Associates the Primary Measure defined in the Data Structure Definition.
\                  +attachedAttribute        Association to the Attribute Values relating to the Observation.
\                  *+observationDimension*   Association to the Key Value that holds the value of the “Dimension at the Observation Level”.
*ObservationValue* Abstract class           
                                            
                   Sub classes              
                                            
                   | UncodedObservation     
                   | CodedObservation       
UncodedObservation Inherits from             An observation that has a text value.
                                            
                   ObservationValue         
\                  value                     The value of the Uncoded Observation.
CodedObservation   Inherits from             An Observation that takes its value from a code in a Code list.
                                            
                   ObservationValue         
\                  +value                    Association to the Code that is the value of the Observation.
                                            
                                             Note that this is a conceptual association showing that the Code must exist in the Code list associated with the Primary Measure or the Concept of the Measure Dimension in the Data Structure Definition. In the actual Data Set the value of the Code is placed in the Observation.
*AttributeValue*   Abstract class            The value of an attribute, such as the instance of a Coded Attribute or of an Uncoded Attribute in a structure such as a Data Structure Definition.
                                            
                   Sub classes              
                                            
                   | *UncodedAttributeValue*
                   | *CodedAttributeValue*  
\                  value                     The value of the attribute.
\                  +valueFor                 Association to the Data Attribute defined in the Data Structure Definition. Note that this is conceptual association as the Concept is identified explicitly in the data set.
UncodedAttribute   Inherits from             An attribute value that has a text value.
Value                                       
                   *AttributeValue*         
\                  startTime                 This attribute is only used if the textFormat of the attribute is of the Timespan type in the Data Structure Definition (in which case the value field takes a duration).
CodedAttribute     Inherits from             An attribute that takes it value from a Code in Code list.
Value                                       
                   *AttributeValue*         
\                  +value                    Association to the Code that is the value of the Attribute Value.
                                            
                                             Note that this is a conceptual association showing that the Code must exist in the Code list associated with the Data Attribute in the Data Structure Definition. In the actual Data Set the value of the Code is placed in the Attribute Value.
================== ========================= =====================================================================================================================================================================================================================================================================================

Cube
====

.. _context-4:

Context
-------

Some statistical systems create views of data based on a “cube”
structure. In essence, a cube is an n-dimensional object where the value
of each dimension can be derived from a hierarchical code list. The
utility of such cube systems is that it is possible to “roll up” or
“drill down” each of the hierarchy levels for each of the dimensions to
specify the level of granularity required to give a “view” of the data –
some dimensions may be rolled up, others may be drilled down. Such
systems give a dynamic view of the data, with aggregated values for
rolled up dimension positions. For example, the individual countries may
be rolled up into an economic region such as the EU, or a geographical
region such as Europe, whilst another dimension, such as “type of road”
may be drilled down to its lower level. The resulting measure (such as
“number of accidents”) would then be an aggregation of the value for
each individual country for the specific type of road.

Such cube systems rely, not on simple code lists, but on hierarchical
code sets (see section 8).

Support for the Cube in the Information Model
---------------------------------------------

Data reported using a Data Structure Definition structure (where each
dimension value, if coded, is taken from a flat code list) can be
described by a cube definition and can be processed by cube aware
systems. The SDMX-IM supports the definition of such cubes in the
following way:

-  The HierachicalCodelist defines the (often complex) hierarchies of
   codes

-  If required, the StructureSet can

   -  group DataStructureDefinition that describe the cube

   -  provide a mapping mechanism between the codes in the flat code
      lists used by the DataStructureDefinition and a
      HierarchicalCodelist where the HierarchicalCodelist uses code
      lists that are not used in the DataStructureDefinition

 Metadata Structure Definition and Metadata Set
==============================================

.. _context-5:

Context
-------

The SDMX metamodel allows metadata:

1. To be exchanged without the need to embed it within the object that
   it is describing.

2. To be stored separately from the object that it describes, yet be
   linked to it (for example, an organisation has a metadata repository
   which supports the dissemination of metadata resulting from metadata
   requests generated by systems or services that have access to the
   object for which the metadata pertains. This is common in web
   dissemination where additional metadata is available for viewing (and
   eventually downloading) by clicking on an “information” icon next to
   the object to which the metadata is attached).

3. To be indexed to aid searching (example: a registry service can
   process a metadata report and extract structural information that
   allows it to catalogue the metadata in a way that will enable users
   to query for it).

4. To be reported according to a defined structure.

In order to achieve this, the following structures are modelled:

-  metadata structure definition which has the following components:

   -  the object types to which the metadata are to be associated
      (attached)

   -  the components that, together, comprise a unique key of the object
      type to which the metadata are to be associated

   -  the reporting structure comprising the metadata attributes that
      can be attached to the various object types (these attributes can
      be structured in a hierarchy), together with any constraints that
      may apply (e.g. association to a code list that contains valid
      values for the attribute when reported in a metadata set)

-  the metadata set, which contains reported metadata

Inheritance
-----------

.. _introduction-5:

Introduction
~~~~~~~~~~~~

As with the Data Structure Definition Structure, many of the constructs
in this layer of the model inherit from the SDMX Base layer. Therefore,
it is necessary to study both the inheritance and the relationship
diagrams to understand the functionality of individual packages. The
diagram below shows the full inheritance tree for the classes concerned
with the MetadataStructureDefinition and the MetadataSet.

There are very few additional classes in the MetadataStructureDefinition
package that do not themselves inherit from classes in the SDMX Base. In
other words, the SDMX Base gives most of the structure of this sub model
both in terms of associations and in terms of attributes. The
relationship diagrams shown in this section show clearly when these
associations are inherited from the SDMX Base (see the Appendix “A Short
Guide to UML in the SDMX Information Model” to see the diagrammatic
notation used to depict this). It is important to note that SDMX base
structures used for the MetadataStructureDefinition are the same as
those used for the DataStructureDefinition and so, even though the usage
is slightly different, the underlying way of defining a
MetadataStructureDefinition is similar to that used for defining a
DataStructureDefinition.

.. _class-diagram---inheritance-2:

Class Diagram - Inheritance
~~~~~~~~~~~~~~~~~~~~~~~~~~~

|image51|

Figure 27: Inheritance class diagram of the Metadata Structure
Definition

.. _explanation-of-the-diagram-14:

Explanation of the Diagram
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _narrative-11:

Narrative
^^^^^^^^^

It is important to the understanding of the relationship class diagrams
presented in this section to identify the concrete classes that inherit
from the abstract classes.

The concrete classes in this part of the SDMX metamodel which require to
be maintained by Maintenance Agencies all inherit from
MaintainableArtefact. These are:

-  *StructureUsage* (concrete class is MetadataflowDefinition)

-  *Structure* (concrete class is MetadataStructureDefinition)

These classes also inherit the identity and versioning facets of
*IdentifiableArtefact, NameableArtefact,* and *VersionableArtefact*.

A *Structure* contains several lists of components. The concrete classes
which inherit from *ComponentList* and in themselves are sub components
of the MetadataStructureDefinition are:

-  MetadataTarget

-  ReportStructure

*ComponentList* contains Components. The classes that inherit from
*Component* are:

-  *Sub Classes of TargetObject*

-  *MetadataAttribute*

Metadata Structure Definition
-----------------------------

.. _introduction-6:

Introduction
~~~~~~~~~~~~

The diagrams and explanations in the rest of this section show how these
concrete classes are related so as to support the functionality
required.

Structures Already Described
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The MetadataStructureDefinition makes use of the following *ItemScheme*
structures either as explicit concrete classes in the model, or as
possible lists which comprise the value domain of a TargetObject.

-  CategoryScheme

-  ConceptScheme

-  Codelist

-  *OrganisationScheme*

-  Reporting Taxonomy

Class Diagram – Relationship
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|image52|

Figure 28: Relationship class diagram of the Metadata Structure
Definition

.. _explanation-of-the-diagram-15:

Explanation of the Diagram
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _narrative-12:

Narrative
^^^^^^^^^

In brief a MetadataStructureDefinition (MSD) defines:

-  The MetadataTarget which defines the components (*TargetObject*) and
   their Representation which are valid for this
   MetadataStructureDefinition, and which are the metadata target object
   of one or more ReportStructure

-  The ReportStructures comprising the *MetadataAttribute*\ s that can
   be associated with the object type identified in the referenced
   MetadataTargets, and hierarchical structure of the attributes

The MetadataTarget comprises one or more *TargetObject*\ s\ *.* The
combination of *TargetObject*\ s identifies a specific object type to
which metadata can be attached in a MetadataSet.

The *TargetObject* is one of the following:

-  DimensionDescriptorValuesTarget - this allows the specification of a
   full or partial key (as used in a dataset) to be specified in a
   MetadataSet as the target object

-  IdentifiableObjectTarget – this defines a specific object type, which
   can be any IdentifiableArtefact

-  DataSetTarget – this specifies that the target object is a DataSet

-  ReportPeriodTarget - this specifies that the report period must be
   present in the MetadataSet

-  ConstraintContentTarget – this specifies that target object is the
   content of an AttachmentConstraint i.e. the part of the data set or
   metadata set identified by the content of an AttachmentConstraint

The valid content of a *TargetObject* when reported in a MetadataSet is
defined in the Representation. This can be an enumerated representation
(i.e. a reference to one of the sub clases of ItemScheme – these are
Codelist, ConceptScheme, *OrganisationScheme,* CategoryScheme, or
ReportingTaxonomy) or non-enumerated.

Thus a single MetadataStructureDefinition can be defined for a discrete
set of related object types. For example, a single definition can be
constructed to define the metadata that can be attached to any part of a
Data Structure Definition, or that can be attached to any artefact
concerned with the reporting of quality metadata (such as data provider
and (data) category). The MetadataTarget specifies the identification
properties of a specific object type to which metadata can be attached
in a MetadataSet. For example, in a DataStructureDefinition the
MetadataTarget might be a Dimension, and therefore the *TargetObject*\ s
are those that uniquely identify a Dimension. This will include both the
DataStructureDefinition and the Dimension (both of these are an
*IdentifiableArtefact* and will use the IdentitifableObjectTarget) as
both *TargetObject*\ s are required in order to identify uniquely a
Dimension).

The ReportStructure comprises a set of *MetadataAttribute*\ s - these
can be defined as a hierarchy. Each *MetadataAttribute* identifies a
Concept that is reported or disseminated in a MetadataSet
(*/*\ conceptIdentity) that uses this MetadataStructureDefinition.
Different *MetadataAttribute*\ s in the same ReportStructure can use
Concepts from different ConceptSchemes. Note that a *MetadataAttribute*
does not link to a Concept that defines its role in this
MetadataStructureDefinition (i.e. the MetadataAttribute does not play a
role).

The *MetadataAttribute* can be specified as having multiple occurrences
and/or specified as being mandatory (minOccurs=1 or more) or conditional
(minOccurs=0). A hierarchical ReportStructure can be defined by
specifying a hierarchy for a MetadataAttribute.

The ReportStructure is associated to one or more of the MetadataTargets
which specify to which object the MetadataAttributes specified in the
ReportStructure are attached when reported in a MetadataSet.

It can be seen from this that the specification of the object types to
which a *MetadataAttribute* can be attached is indirect: the
*MetadataAttributes* are defined in a ReportStructure which itself is
attached to one or more MetadataTarget and the actual object is
identified by the *TargetObject*\ s comprising the MetadataTarget. This
gives a flexible mechanism by which the actual object types need not be
defined in concrete terms in the model, but are defined dynamically in
the MetadataStructureDefinition, in much the same way as the keys to
which data observation are “attached” in a DataStructureDefinition. In
this way the MetadataStructureDefinition can be used to define any set
of *MetadataAttribute*\ s and any set of object types to which they can
be attached.

Each *MetadataAttribute* can have a *Representation* specified (using
the /localRepresentation association). If this is not specified in the
MetadataStructureDefinition then the *Representation* is taken from that
defined for the Concept (the coreRepresentation association).

The definition of the various types of *Representation* can be found in
the specification of the Base constructs. Note that if the
Representation is non-enumerated then the association is to the
ExtendedFacet (which allows for xhtml as a FacetValueType). If the
Representation is enumerated then is must use a Codelist.

The MetadataStructureDefinition is linked to a MetadataflowDefinition.
The MetadataflowDefinition does not have any attributes in addition to
those inherited from the Base classes.

.. _definitions-12:

Definitions
^^^^^^^^^^^

=============================== ========================================================== =================================================================================================================================================================================================================================================================================================================================================================================
Class                           Feature                                                    Description
StructureUsage                                                                             See “SDMX Base”.
Metadataflow Definition         Inherits from:                                             Abstract concept (i.e. the structure without any metadata) of a flow of metadata that providers will provide for different reference periods.
                                                                                          
                                *StructureUsage*                                          
\                               /structure                                                 Associates a Metadata Structure Definition.
MetadataStructure Definition                                                               A collection of metadata concepts, their structure and usage when used to collect or disseminate reference metadata.
\                               /grouping                                                  An association to a Metadata Target or Report Structure.
MetadataTarget                  Inherits from                                              A set of components that define a key of an object type to which metadata may be attached.
                                                                                          
                                *ComponentList*                                           
\                               /components                                                Associates the Target Object components that define the key of the Metadata Target.
*TargetObject*                  Abstract Class                                            
                                                                                          
                                | Sub Classes                                             
                                | DimensionDescriptorValuesTarget IdentifiableObjectTarget
                                | DataSetTarget                                           
                                | ReportPeriodTarget                                      
\                               /localRepresentation                                       Associates a Representation to the Target Object that must be respected when the object is identified in a Metadata Set. This may be enumerated or non-enumerated.
DimensionDescriptorValuesTarget Inherits from                                              The target object is the key of a data series.
                                                                                          
                                *TargetObject*                                            
IdentifiableObject Target       Inherits from                                              The target object is a specified object type.
                                                                                          
                                *TargetObject*                                            
\                               objectType                                                 Identifies the object type.
DataSetTarget                   Inherits from                                              The target object is a Data Set.
                                                                                          
                                *TargetObject*                                            
ReportPeriodTarget              Inherits from                                              The target is a report period. Note that this does not describe the use of an object, but rather serves as a unique metadata key for metadata reports. Metadata reports attached to a particular object may vary over time, and this time identifier component can be used to disambiguate the reports, much like the time dimension disambiguates observations in a data series.
                                                                                          
                                *TargetObject*                                            
ConstraintTarget                Inherits from                                              The target object is the data or reference metadata that is identified in the content of an Attachment Constraint.
                                                                                          
                                *TargetObject*                                            
ReportStructure                 Inherits from:                                             Defines a set of concepts that comprises the Metadata Attributes to be reported.
                                                                                          
                                *ComponentList*                                           
\                               /components                                                An association to the Metadata Attributes relevant to the Report Structure.
\                               +reportFor                                                 Associates the Metadata Targets for which this Report Structure is used.
*MetadataAttribute*                                                                        Identifies a Concept for which a value may be reported in a Metadata Set.
\                               /hierarchy                                                 Association to one or more child Metadata Attribute.
\                               /conceptIdentity                                           An association to the concept which defines the semantic of the attribute.
\                               isPresentational                                           Indication that the Metadata Attribute is present for structural purposes (i.e. it has child attributes) and that no value for this attribute is expected to be reported in a Metadata Set using this Report Structure.
\                               minOccurs                                                  Specifies how many occurrences of the Metadata Attribute may be reported at this point in the Metadata Report.
                                maxOccurs                                                 
*ConceptUsage*                                                                             The use of a Concept as Metadata Attribute.
\                               concept                                                    Association to a Concept in a ConceptScheme.
\                               /localRepresentation                                       Associates a Representation that overrides any core representation specified for the Concept itself.
Representation                                                                             The representation of the Metadata Attribute.
=============================== ========================================================== =================================================================================================================================================================================================================================================================================================================================================================================

Metadata Set
------------

.. _class-diagram-9:

Class Diagram
~~~~~~~~~~~~~

|image53|

Figure 29: Relationship Class Diagram of the Metadata Set

.. _explanation-of-the-diagram-16:

Explanation of the Diagram
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _narrative-13:

Narrative
^^^^^^^^^

Note that the MetadataSet must conform to the
MetadataStructureDefinition associated to the MetadataflowDefinition for
which this MetadataSet is an “instance of metadata”. Whilst the model
shows the association to the classes of the MetadataStructureDefinition,
this is for conceptual purposes to show the link to the
MetadataStructureDefinition. In the actual MetadataSet as exchanged
there must, of course, be a reference to the MetadataStructureDefinition
and the ReportStructure, and optionally a MetadataflowDefinition, but
the MetadataStructureDefinition is not necessarily exchanged with the
metadata. Therefore, the MetadataStructureDefinition classes are shown
in the grey areas, as these are not a part of the MetadataSet itself.

An organisation playing the role of DataProvider can be responsible for
one or more MetadataSet.

A MetadataSet comprises one or more MetadataReport, each of which must
be for the same ReportStructure. It references both a MetadataTarget,
defined in the MetadataStructureDefinition, and contains a
TargetObjectKey and ReportedAttributes.

The identified ReportStructure specifies which MetadataAttributes are
expected as *ReportedAttribute*\ s. The identified MetadataTarget
specifies the expected content of the TargetObjectKey i.e. it specifies
the information required to identify the object for which the
*ReportedAttribute*\ s are reported.

The TargetObjectValue can be one of:

-  TargetDataKey – this can contain:

   -  a SeriesKey (set of dimension values)

   -  a SeriesKey plus a value or values (giving time range) for the
      TimeDimension (TimeDimensionValue)

   -  a value of values for the TimeDimension

-  TargetIdentifiableObject -this identifies any identifiable object
   (which includes both Maintainable and Identifiable objects

-  TargetDataSet – this identifies a DataSet

-  TargetReportPeriod – this specifies the report period for the Report

A simple text value for the *ReportedAttribute* uses the
*NonEnumeratedAttributeValue* sub class of *ReportedAttribute* whilst a
coded value uses the EnumeratedAttributeValue sub class.

The *NonEnumeratedAttributeValue* can be one of:

-  XHTMLAttributeValue – the content is XHTML

-  TextAttributeValue – the content is textual and may contain the text
   in multiple languages

-  OtherNonEnumeratedAttributeValue – the content is a string value that
   must conform to the Representation specified for the
   MetadataAttribute in the MetadataStructureDefinition for the relevant
   ReportStructure

The EnumeratedAttributeValue contains a value for a Code specified as
the Representation for the MetadataAttribute in the
MetadataStructureDefinition for the relevant ReportStructure.

.. _definitions-13:

Definitions
^^^^^^^^^^^

================================= ============================= ===================================================================================================================================================================================
Class                             Feature                       Description
MetadataSet                                                     Any organised collection of metadata.
\                                 reportingBegin                A specific time period in a known system of time periods that identifies the start period of a report.
\                                 reportingEnd                  A specific time period in a known system of time periods that identifies the ebd period of a report.
\                                 dataExtractionDate            A specific time period that identifies the date and time that the data are extracted from a data source.
\                                 validFrom                     Indicates the inclusive start time indicating the validity of the information in the data set.
\                                 validTo                       Indicates the inclusive end time indicating the validity of the information in the metadata set.
\                                 publicationYear               Specifies the year of publication of the data or metadata in terms of whatever provisioning agreements might be in force.
\                                 publicationPeriod             Specifies the period of publication of the data or metadata in terms of whatever provisioning agreements might be in force.
\                                 setId                         Provides an identification of the metadata set.
\                                 action                        Defines the action to be taken by the recipient system (update, replace, delete)
\                                 +describedBy                  Associates a Metadataflow Definition to the Metadata Set.
\                                 +structuredBy                 Associates the Metadata Structure Definition that defines the structure of the Metadata Set. Note that the Metadata Structure Definition
                                                               
                                                                is the same as that associated (non-mandatory) to the Metadataflow Definition.
\                                 +publishedBy                  Associates the Data Provider that reports/publishes the metadata.
\                                 +describedBy                  Reference to the Report Structure.
MetadataReport                                                  A set of values for Metadata Attributes defined in a Report Structure of a Metadata Structure Definition.
\                                 +attachesTo                   Associates the object key to which metadata is to be attached.
\                                 +target                       Associates the Metadata Target that defines the target object to which the metadata are to be associated.
\                                 +metadata                     Associates the Reported Attribute values which are to be associated with the object or objects identified by the Target Object Key.
*TargetObjectKey*                                               Identifies the key of the object to which the metadata are to be attached.
\                                 +valueFor                     Associates the Metadata Target that identifies the object type and the component structure of the Target Object Key.
                                                               
                                                                Note that this is a conceptual association showing the link to the MSD construct.
\                                 +keyValues                    Associates the Target Object Values of the Target Object Key.
*TargetObjectValue*               Abstract class                The key of an individual object of the type specified in the Metadata Target of the Metadata Structure Definition.
                                                               
                                  Sub classes are              
                                                               
                                  | TargetDataKey              
                                  | TargetIdentifiableObject   
                                  | TargetDataSet              
                                  | TargetReportPeriod         
\                                 +valueFor                     Associates the Target Object for which this value is provided.
                                                               
                                                                Note that this is a conceptual association showing the link to the MSD construct.
TargetDataKey                     Inherits from                 The identification of the components and the values that form the data or metadata key.
                                                               
                                  *TargetObjectValue*          
ComponentValue                                                  Collectively contain the identification of the components and the values that form the data key.
value                                                           The key value.
\                                 +valueFor                     Associates the Component for which the value is declared.
TimeDimensionValue                                              Contains identification of the Time Dimension and the value.
TargetIdentifiable                Inherits from                 Specifies the identification of an Identifiable object.
Object                                                         
                                  *TargetObjectValue*          
StructureRef                                                    Contains the identification of an Identifiable object.
\                                 structureType                 The object type of the target object.
Maintainable                                                    Identification of the target object by means of its identifier constructs i.e agency ID, id, version for Maintainable Object plus, for Identifiable Object, the id.
ArtefactRef                                                    
Identifiable                                                   
ArtefactRef                                                    
\                                 +containedObject              Association to a contained object in a hierarchy of Identifiable Objects such as a Transition in a Process Step.
TargetDataSet                     Inherits from                 Contains the identification of a Data Set
                                                               
                                  *TargetObjectValue*          
TargetReportPeriod                Inherits from                 Contains the period covered by the Metadata Report.
                                                               
                                  *TargetObjectValue*          
*ReportedAttribute*               Abstract class                The value for a Metadata Attribute.
                                                               
                                  Sub classes are:             
                                                               
                                  | NonEnumeratedAttributeValue
                                  | EnumeratedAttributeValue   
\                                 +valueFor                     Association to the Metadata Attribute in the Metadata Structure Definition that identifies the Concept and allowed Representation for the Reported Attribute.
                                                               
                                                                Note that this is a conceptual association showing the link to the MSD construct. The syntax for the Reported Attribute will state, in some form, the id of the Metadata Attribute.
\                                 +child                        Association to a child Reported Attribute consistent with the hierarchy defined in the Report Structure for the Metadata Attribute for which this child is a Reported Attribute.
*NonEnumerated AttributeValue*    Inherits from                 The content of a Reported Attribute where this is textual.
                                                               
                                  ReportedAttribute            
                                                               
                                  Sub class:                   
                                                               
                                  | XHTMLAttributeValue        
                                  | TextAttributeValue         
                                  | OtherNonEnumerated         
                                  | AttributeValue             
XHTMLAttributeValue                                             This contains XHTML.
\                                 value                         The string value of the XHTML.
TextAttributeValue                                              This value of a Reported Attribute where the content is human-readable text.
\                                 text                          The string value is text. This can be present in multiple language versions.
OtherNonEnumerated AttributeValue                               The value of a Reported Attribute where the content is not of human-readable text.
\                                 value                         A text string that is consistent in format to that defined in the Representation of the Metadata Attribute for which this is a Reported Attribute.
EnumeratedAttributeValue          Inherits from                 The content of a Reported Attribute that is taken from a Code in a Code list.
                                                               
                                  MetadataAttributeValue       
\                                 value                         The Code value of the Reported Attribute.
\                                 +value                        Association to a Code in the Code list specified in the Representation of the Metadata Attribute for which this Reported Attribute is the value
                                                               
                                                                Note that this shows the conceptual link to the Item that is the value. In reality, the value itself will be contained in the Enumerated Attribute Value.
================================= ============================= ===================================================================================================================================================================================

Hierarchical Code List
======================

Scope
-----

The Codelist described in the section on structural definitions supports
a simple hierarchy of Codes, and restricts any child Code to having just
one parent Code. Whilst this structure is useful for supporting the
needs of the DataStructureDefinition and the
MetadataStructureDefinition, it may not sufficient for supporting the
more complex associations between codes that are often found in coding
schemes such as a classification scheme. Often, the Codelist used in a
DataStructureDefinition is derived from a more complex coding scheme.
Access to such a coding scheme can aid applications, such as OLAP
applications or data visualisation systems, to give more views of the
data than would be possible with the simple Codelist used in the
DataStructureDefinition.

Note that a hierarchical code list is not necessarily a balanced tree. A
balanced tree is where levels are pre-defined and fixed, (i.e. a level
always has the same set of codes, and any code has a fixed parent and
child relationship to other codes). A statistical classification is an
example of a balanced tree, and the support for a balanced hierarchy is
a sub set, and special case, of the hierarchical code list.

The principal features of the Hierarchical Codelist are:

1. A child code can have more than one parent.

2. There can be more than one code that has no parent (i.e. more than
   one “root node”).

3. There may be many hierarchies (or “views”) defined, in terms of the
   associations between the codes. Each hierarchy serves a particular
   purpose in the reporting, analysis, or dissemination of data.

4. The levels in a hierarchy can be explicitly defined or they can be
   implicit: (i.e. they exist only as parent/child relationships in the
   coding structure).

.. _inheritance-1:

Inheritance
-----------

.. _class-diagram-10:

Class Diagram
~~~~~~~~~~~~~

|image54|

Figure 30: Inheritance class diagram for the Hierarchical Codelist

.. _explanation-of-the-diagram-17:

Explanation of the Diagram
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _narrative-14:

Narrative
^^^^^^^^^

The HierarchicalCodelist inherits from *MaintainableArtefact* and thus
has identification, naming, versioning and a maintenance agency. Both
*Hierarchy* and Level are a *NameableArtefact* and therefore have an Id,
multi-lingual name and multi-lingual description. A HierachicalCode is
an *IdentifiableArtefact*.

It is important to understand that the Codes participating in a
HierarchicalCodelist are not themselves contained in the list – they are
referenced from the list and are maintained in one or more Codelists.
This is explained in the narrative of the relationship class diagram
below..

.. _definitions-14:

Definitions
^^^^^^^^^^^

The definitions of the various classes, attributes, and associations are
shown in the relationship section below.

Relationship
------------

.. _class-diagram-11:

Class Diagram
~~~~~~~~~~~~~

|image55|

Figure 31: Relationship class diagram of the Hierarchical Code Scheme

.. _explanation-of-the-diagram-18:

Explanation of the Diagram
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _narrative-15:

Narrative
^^^^^^^^^

The basic principles of the HierarchicalCodelist are:

1. The HierarchicalCodelist is a specification of the Codes comprising
   the scheme and the specification of the structure of the Codes in the
   scheme in terms of one or more *Hierarchy.*

2. The Codes in the HierarchicalCodelist are not themselves a part of
   the scheme, rather they are references to Codes in one or more
   external Codelists.

3. Any individual Code may participate in many Hierarchys, in order to
   give structure to the HierarchicalCodelist.

4. The Hierarchy of Codes is specified in HierarchicalCode. This
   references the Code and its immediate child HierarchicalCodes.

A *Hierarchy* can have formal levels (hasFormalLevels=”true”). However,
even if hasFormalLevels=”false” the *Hierarchy* can still have one or
more Levels associated in order to document information about the
HierarchicalCodes.

If hasFormalLevels=”false the Hierarchy is “value based” comprising a
hierarchy of codes with no formal Levels. If hasFormalLevels=”true” then
the hierarchy is “level based” where each Level is a formal Level in the
HierarchicalCodeList, such as those present in statistical
classifications. In a “level based” hierarchy each HierarchicalCode is
linked to the Level in which it resides (which must be in the same
Hierarchy as the HierarchicalCode). It is expected that all
HierarchicalCodes at the same hierarchic level defined by the
+parent/+child association will be linked to the same Level. Note that
the +level association need only be specified if the HierarchicalCode is
at a different hierarchical level ((implied by the HierarchicalCode
parent/child association) than the actual Level in the level hierarchy
(implied by the Level parent/child association).

[Note that organisations wishing to be compliant with accepted models
for statistical classifications should ensure that the Id is the number
associated with the Level, where Levels are numbered consecutively
starting with level 1 at the highest Level].

The Level may have CodingFormat information defined (e.g. coding type at
that level).

.. _definitions-15:

Definitions
^^^^^^^^^^^

================ ====================== ========================================================================================================================================================================================================
Class            Feature                Description
HierarchicalCode Inherits from:         An organised collection of codes that may participate in many parent/child relationships with other Codes in the scheme, as defined by one or more Hierarchy of the scheme.
list                                   
                 *MaintainableArtefact*
\                +hierarchy             Association to Hierarchies of Codes.
Hierarchy        Inherits from:         A classification structure arranged in levels of detail from the broadest to the most detailed level.
                                       
                 *NameableArtefact*    
\                hasFormalLevels        If “true” this indicates a hierarchy where the structure is arranged in levels of detail from the broadest to the most detailed level.
                                       
                                        If “false” this indicates a hierarchy structure where the items in the hierarchy have no formal level structure.
\                +codes                 Association to the top-level Hierarchical Codes in the Hierarchy.
\                +level                 Association to the top Level in the Hierarchy.
Level            Inherits from          In a “level based” hierarchy this describes a group of Codes which are characterised by homogeneous coding, and where the parent of each Code in the group is at the same higher level of the Hierarchy.
                                       
                 *NameableArtefact*     In a “value based’ hierarchy this describes information about the HierarchicalCodes at the specified nesting level.
\                +codeFormat            Association to the Coding Format.
\                +child                 Association to a child Level of Level.
CodingFormat                            Specifies format information for the codes at this level in the hierarchy such as whether the codes at the level are alphabetic, numeric or alphanumeric and the code length.
HierarchicalCode                        A hierarchic structure of code references.
\                validFrom              Date from which the construct is valid
\                validTo                Date from which construct is superseded.
\                +code                  Association to the Code that is used at the specific point in the hierarchy.
\                +child                 Association to a child Code in the hierarchy.
\                +level                 Association to a Level where levels have been defined for the Hierarchy.
Code                                    The Code to be used at this point in the hierarchy.
\                /items                 Association to the Code list containing the Code.
Codelist                                The Code list containing the Code.
================ ====================== ========================================================================================================================================================================================================

Structure Set and Mappings
==========================

.. _scope-1:

Scope
-----

A StructureSet allows components in one structure to be mapped to
components in another structure of the same type. In this context the
term “structure” is used loosely to include types of *ItemScheme*, types
of *Structure*, and types of *StructureUsage*. The allowable structures
that can be mapped, and the components that can be mapped within these
structures are:

============================= ======================================================================================================================================
Structure Type                Component type
============================= ======================================================================================================================================
Codelist                      Code
Category Scheme               Category
Concept Scheme                Concept
Organisation Scheme           Organisation – this allows mapping any type of Organisation to any type of Organisation (e.g. a Data Provider to an Organisation Unit)
Hierarchical Codelist         Hierachical Code to Code or vice-versa
Data Structure Definition     Dimension, Measure Dimension, Time Dimension. Data Attribute, Primary Measure
Metadata Structure Definition Target Object, Metadata Attribute
Dataflow Definition           None
Metadataflow Definition       None
============================= ======================================================================================================================================

The StructureSet can contain one or more “maps” and can define related
structures (via the association +relatedStructure) which group related
DataStructureDefinitions, MetadataStructureDefinitions,
DataflowDefinintions, MetadataflowDefinintions.

Structure Set
-------------

Class Diagram – Inheritance
~~~~~~~~~~~~~~~~~~~~~~~~~~~

|image56|

Figure 32: Inheritance Class Diagram of the Structure Set

.. _class-diagram-relationship-1:

Class Diagram – Relationship
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|image57|

Figure 33: Relationship Class diagram of the Structure Set

.. _explanation-of-the-diagram-19:

Explanation of the Diagram
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _narrative-16:

Narrative
^^^^^^^^^

The StructureSet is a *MaintainableArtefact*. It can contain:

1. A set of references to concrete sub-classes of *Structure* and
   *StructureUsage* (DataStructureDefinition,
   MetadataStructureDefinition, DataflowDefinition or
   MetadataflowDefinition) to indicate that a relationship exists
   between them. For example there may be a group of
   DataStructureDefinition which, together, form the definition of a
   cube, each DataStructureDefinition defining a part of the cube.

2. A set of StructureMaps which define which components of one structure
   are equivalent to those in another in a ComponentMap.

3. A set of ItemSchemeMaps which define the mapping between two concrete
   classes of ItemScheme, and the mapping of the Items in these schemes,
   such as the mapping of Codes in two Codelists..

4. A set of HybridCodelistMaps which define the mapping between a
   Codelist and a HierachicalCodelist.

The StructureMap references two *Structure*\ s or *StructureUsage*\ s.
In concrete terms these references will be to DataStructureDefinitions,
MetadataStructureDefinitions, DataflowDefinitions or
MetadataflowDefinitions.

.. _definitions-16:

Definitions
^^^^^^^^^^^

============ ====================== ==============================================================================================================================================================================================
Class        Feature                Description
StructureSet Inherits from          A maintainable collection of structural maps that link components together in a source/target relationship where there is a semantic equivalence between the source and the target components.
             *MaintainableArtefact*
\            +relatedStructure      Association to a set of Data Structure Definitions and Metadata Structure Definitions.
\            +relatedStructureUsage Association to a set of Dataflow Definition and Metadataflow Definition.
\            +map                   Association to Structure Map.
\            +itemSchemeMap         Association to Item Scheme Map
StructureMap Inherits from          Links a source and target structure where there is a semantic equivalence between the source and the target structures.
             *NameableArtefact*    
\            sourceStructure        Association to the source Structure.
\            targetStructure        Association to the target Structure which must be of the same type as the source Structure.
\            sourceStructureUsage   Association to the source Structure Usage.
\            targetStructureUsage   Association to the target Structure Usage which must be of the same type as the source Structure Usage.
============ ====================== ==============================================================================================================================================================================================

Structure Map
-------------

.. _class-diagram-12:

Class Diagram
~~~~~~~~~~~~~

|image58|

Figure 34: Class diagram of the Structure Map

.. _explanation-of-the-diagram-20:

Explanation of the Diagram
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _narrative-17:

Narrative
^^^^^^^^^

The StructureMap contains a set of ComponentMaps, each one indicating
equivalence between Components of the referenced *Structure*.
ComponentMap has a *RepresentationMapping* which can be one of the
concete classes of *ItemSchemeMap* (e.g. for a Dimension this would be a
CodelistMap) or ToTextFormat which takes values: id, name, description.
This instructs mapping tools to use the id, name or description of a
coded component to determine equivalence with an uncoded component's
value.

An example of a ComponentMap is linking the source *Component* that is a
Dimension in the source DataStructureDefinition (identified in the
StructureMap) to the equivalent target *Component* that is a Dimension
in the target DataStructureDefinition).

.. _definitions-17:

Definitions
^^^^^^^^^^^

======================== ======================= ===================================================================================================================================================================
Class                    Feature                 Description
StructureMap             Inherits from           Links a source and target structure where there is a semantic equivalence between the source and the target structures.
                         *NameableArtefact*     
\                        alias                   An alternate identification of the map, that allows the relation of multiple maps to be expressed by the sharing of this value.
\                        +map                    Association to the Component Map.
ComponentMap             Inherits from           Links a source and target Component where there is a semantic equivalence between the source and the target Components.
                         *AnnotableArtefact*    
\                        alias                   An alternate identification of the map, that allows the relation of multiple maps to be expressed by the sharing of this value.
\                        preferredLanguage       Specifies the language to use for the content of the To Text Format option of RepresentationMap
\                        +source                 Association to the source Component.
\                        +target                 Association to the target Component.
\                        +contentMap             Association to the constructs that map the content of the Components – this will be either one of sub classes of Item Scheme or a mapping to text.
*Representation Mapping* AbstractClass           Defines the mapping of the content of the source Component to the content of the target Component.
                                                
                         Sub classes:           
                                                
                         | SchemeMap            
                         | ToTextFormat         
SchemeMap                Inherits from           Associates an Item Scheme Map
                                                
                         *RepresentationMapping*
ToTextFormat             Inherits from           Defines the text format
                                                
                         *RepresentationMapping*
\                        textFormat              Text format type.
\                        toValueType             Identifies the construct to be taken from the Item of the source Component when mapping the content of the source Component to the content of the target Component.
ToValueType                                      Enumeration of the construct in the Item.
======================== ======================= ===================================================================================================================================================================

Item Scheme Map
---------------

.. _context-6:

Context
~~~~~~~

The ItemSchemeMap is used to associate the *Item*\ s in two different
*ItemSchemes*. This is a generic mechanism that can be used to map
*Item*\ s. Specific models exist for mapping schemes where there is a
semantic equivalence between *Item*\ s in the *ItemScheme*. The model
supports the mapping of any two *ItemScheme*\ s of the same type. These
are:

-  ConceptScheme

-  CategoryScheme

-  *OrganisationScheme*

-  Codelist

-  ReportingTaxonomy

.. _class-diagram-13:

Class Diagram
~~~~~~~~~~~~~

|image59|

Figure 35: Class diagram of the Item Scheme Map

.. _explanation-of-the-diagram-21:

Explanation of the Diagram
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _narrative-18:

Narrative
^^^^^^^^^

Both the ItemSchemeMap and the ItemAssociation inherit from
NameableArtefact.

Each of ConceptSchemeMap, CategorySchemeMap, CodelistMap and
*OrganisationSchemeMap,* ReportingTaxonomyMap provides a mechanism for
specifying semantic equivalence between the items (Concept,
Category,Code, *Organisation,* ReportingCategory) in the scheme. Note
that any type of *OrganisationScheme* and *Organisation* can be mapped
(e.g. an Agency in an AgencyScheme can be mapped to an OrganisationUnit
in an OrganisationUnitScheme).

Each scheme map identifies a +source and +target scheme whose content is
to be mapped. Note that many schemes can be joined together via a set of
pair-wise mappings. The ConceptMap, CategoryMap, CodelistMap,
OrganisationMap, and ReportingTaxonomyMap denotes which Concepts,
Categorys, Codes, Organisations, and ReportingCategorys are semantically
equivalent and a shared alias can be specified to refer to a set of
mapped concepts to facilitate querying.

.. _definitions-18:

Definitions
^^^^^^^^^^^

===================== ============================ ===============================================================================================================================
Class                 Feature                      Description
*ItemSchemeMap*       Inherits from                Associates two Item Schemes
                                                  
                      *NameableArtefact*          
                                                  
                      *Sub Classes*               
                                                  
                      | ConceptSchemeMap          
                      | CategorySchemeMap         
                      | CodelistMap               
                      | OrganisationSchemeMap     
                      | ReportingTaxonomySchemeMap
\                     alias                        An alternate identification of the map, that allows the relation of multiple maps to be expressed by the sharing of this value.
\                     source                       Association to the source Item Scheme.
\                     target                       Association to the target Item Scheme.
\                     ItemAssociation              Association to the Item Association.
*ItemAssociation*     Inherits from               
                                                  
                      *AnnotableArtefact*         
                                                  
                      *Sub Classes*               
                                                  
                      | ConceptMap                
                      | CategoryMap               
                      | CodeMap                   
                      | OrganisationMap           
                      | ReportingCategoryMap      
\                     source                       Association to the source Item.
\                     target                       Association to the target Item.
ConceptSchemeMap      Inherits from                Associates a source and target Concept Scheme
                                                  
                      *ItemSchemeMap*             
\                     /source                      Association to the source Concept Scheme.
\                     /target                      Association to the target Concept Scheme.
ConceptMap            Inherits from                Associates a source and target Concept.
                                                  
                      *ItemAssociation*           
\                     /source                      Association to the source Concept.
\                     /target                      Association to the target Concept.
CodelistMap           Inherits from                Associates a source and target Code list.
                                                  
                      *ItemSchemeMap*             
\                     /source                      Association to the source Code list.
\                     /target                      Association to the target Code list.
CodeMap               Inherits from                Associates a source and target Code.
                                                  
                      *ItemAssociation*           
\                     /source                      Association to the source Code.
\                     /target                      Association to the target Code.
CategorySchemeMap     Inherits from                Associates a source and target Category Scheme.
                                                  
                      *ItemSchemeMap*             
\                     /source                      Association to the source Category Scheme.
\                     /target                      Association to the target Category Scheme.
CategoryMap           Inherits from                Associates a source and target Category.
                                                  
                      *ItemAssociation*           
\                     /source                      Association to the source Category.
\                     /target                      Association to the target Category.
OrganisationSchemeMap Inherits from                Associates a source and target Organisation Scheme.
                                                  
                      *ItemSchemeMap*             
\                     /source                      Association to the source Organisation Scheme.
\                     /target                      Association to the target Organisation Scheme.
OrganisationMap       Inherits from                Associates a source and target Organisation.
                                                  
                      *ItemAssociation*           
\                     /source                      Association to the source Organisation.
\                     /target                      Association to the target Organisation.
ReportingTaxonomyMap  Inherits from                Associates a source and target Reporting Taxonomy.
                                                  
                      *ItemSchemeMap*             
\                     /source                      Association to the source Reporting Taxonomy.
\                     /target                      Association to the target Reporting Taxonomy.
ReportingCategoryMap  Inherits from                Associates a source and target Reporting Category.
                                                  
                      *ItemAssociation*           
\                     /source                      Association to the source Reporting Category.
\                     /target                      Association to the target Reporting Category.
===================== ============================ ===============================================================================================================================

Hybrid Codelist Map
-------------------

.. _class-diagram-14:

Class Diagram
~~~~~~~~~~~~~

|image60|

Figure 36: Class diagram of the Hybrid Codelist Map

.. _explanation-of-the-diagram-22:

Explanation of the Diagram
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _narrative-19:

Narrative
^^^^^^^^^

The HybridCodelistMap maps the content of a Codelist and a
HierachicalCodelist. It contains a mapping of the codes in the two
schemes (HybridCodeMap). The HybridCodeMap maps either a Code or
HierachicalCode to a Code or HierarchicalCode. The HierarchicalCode is
identified by a combination of the Hierarchy and the HierarchicalCode.

.. _definitions-19:

Definitions
^^^^^^^^^^^

========================== ==================== ===============================================================================================================================
Class                      Feature              Description
HybridCodelist             Inherits from        Associates a Codelist and a Hierarchical Codelist.
Map                                            
                           *NameableArtefact*  
\                          alias                An alternate identification of the map, that allows the relation of multiple maps to be expressed by the sharing of this value.
\                          +source              Association to the source List.
\                          +target              Association to the target List.
\                          +hybridCodeMap       Association to the set of Hybrid Code Maps in the Hybrid Codelist Map.
*SourceList*               Abstract Class      
                                               
                           Sub classes         
                                               
                           | SourceCodelist    
                           | SourceHierarchical
                           | Codelist          
*TargetList*               Abstract Class      
                                               
                           Sub classes         
                                               
                           | TargetCodelist    
                           | TargetHierarchical
                           | Codelist          
SourceCodelist                                  Identifies the Codelist where this is the source of the map.
TargetCodelist                                  Identifies the Codelist where this is the target of the map.
SourceHierarchical                              Identifies the Hierarchical Codelist where this is the source of the map.
Codelist                                       
TargetHierarchical                              Identifies the Hierarchical Codelist where this is the target of the map.
Codelist                                       
HybridCodeMap              Inherits from        Associates the source and target codes in Hybrid Codelist Map.
                                               
                           *AnnotableArtefact* 
\                          +source              Associates the Source Code Map.
\                          +target              Associates the Target Code Map.
*SourceCodeMap*            Abstract Class      
                                               
                           Sub classes         
                                               
                           | SourceCode        
                           | SourceHierarchical
                           | Code              
*TargetCodeMap*            Abstract Class      
                                               
                           Sub classes         
                                               
                           | TargetCode        
                           | TargetHierarchical
                           | Code              
SourceCode                                      Identifies the Code where this is the source of the map.
TargetCode                                      Identifies the Code where this is the target of the map.
SourceHierarchical                              Identifies the Hierarchical Code where this is the source of the map
Code                                           
TargetHierarchical                              Identifies the Hierarchical Code where this is the target of the map.
Code                                           
HierarchicalCode Reference                      References both the Hierarchy and the Hierarchical Code in a Hierarchical Codelist.
\                          +hierarchy           Associates the Hierarchical Code in the Hierarchy of the Hierarchical Codelist.
                                               
                           +codeAssociation    
========================== ==================== ===============================================================================================================================

Constraints
===========

.. _scope-2:

Scope
-----

The scope of this section is to describe the support in the metamodel
for specifying both the access to and the content of a data source. The
information may be stored in a resource such as a registry for use by
applications wishing to locate data and metadata which is available via
the Internet. The Constraint is also used to specify a sub set of a
Codelist which may used as a partial code list which is relevant in the
context of the artefact to which the Constraint is attached e.g. Data
Structure Definition, Dataflow, Provision Agreement.

Note that in this metamodel the term data source refers to both data and
metadata sources, and data provider refers to both data and metadata
providers.

A data source may be a simple file of data or metadata (in SDMX-ML
format), or a database or metadata repository. A data source may contain
data for many data or metadataflows (called DataflowDefinition, and
MetadataflowDefinition in the model), and the mechanisms described in
this section allow an organisation to specify precisely the scope of the
content of the data source where this data source is registered
(SimpleDataSource, QueryDataSource).

The DataflowDefinition and MetadataflowDefinition, themselves may be
specified as containing only a sub set of all the possible keys that
could be derived from a DataStructureDefinition or
MetadataStructureDefinition.

These specifications are called *Constraint* in this model.

.. _inheritance-2:

Inheritance
-----------

Class Diagram of Constrainable Artefacts - Inheritance
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|image61|

Figure 37: Inheritance class diagram of constrainable and provisioning
artefacts

.. _explanation-of-the-diagram-23:

Explanation of the Diagram
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _narrative-20:

Narrative
^^^^^^^^^

Any artefact that is derived from *ConstrainableArtefact* can have
constraints defined. The artefacts that can have constraint metadata
attached are:

-  DataflowDefinition

-  ProvisionAgreement

-  DataProvider – this is restricted to release calendar

-  MetadataflowDefinition

-  DataStructureDefinition

-  MetadataStructureDefinition

-  DataSet

-  SimpleDataSource – this is a registered data source where the
   registration references the actual DataSet or MetadataSet

-  QueryDataSource

Note that, because the Constraint can specify a sub set of the component
values implied by a specific *Structure* (such a specific
DataStructureDefinition or specific MetadataStructureDefinition), the
*ConstrainableArtefact*\ s must be associated with a specific
*Structure*. Therefore, whilst the Constraint itself may not be linked
directly to a DataStructureDefinition or MetadataStructureDefinition,
the artefact that it is constraining will be linked to a
DataStructureDefinition or MetadataStructureDefinition. As a Data
Provider does not link to any one specific DSD or MSD the type of
information that can be contained in a Constraint linked to a
DataProvider is restricted to Release Calendar.

.. _constraints-1:

Constraints
-----------

Relationship Class Diagram – high level view
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|image62|

Figure 38: Relationship class diagram showing constraint metadata

.. _explanation-of-the-diagram-24:

Explanation of the Diagram
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _narrative-21:

Narrative
^^^^^^^^^

The constraint mechanism allows specific constraints to be attached to a
*ConstrainableArtefact*. With the exception of ReferencePeriod, and
ReleaseCalendar these constraints specify a sub set of the total set of
values or keys that may be present in any of the ConstrainableArtefacts.

For instance a DataStructureDefinition specifies, for each Dimension,
the list of allowable code values. However, a specific
DataflowDefinition that uses the DataStructureDefinition may contain
only a sub set of the possible range of keys that is theoretically
possible from the DataStructureDefinition definition (the total range of
possibilities is sometimes called the Cartesian product of the dimension
values). In addition to this, a DataProvider that is capable of
supplying data according to the DataflowDefinition has a
ProvisionAgreement, and the DataProvider may also wish to supply
constraint information which may further constrain the range of
possibilities in order to describe the data that the provider can
supply. It may also be useful to describe the content of a datasource in
terms of the KeySets or CubeRegions contained within it.

A *ConstrainableArtefact* can have two types of *Constraint*:

1. ContentConstraint – is used solely as a mechanism to specify either
   the available set of keys (DataKeySet, MetadataKeySet) or set of
   component values (CubeRegion, MetadatTargetRegion) in a *DataSource*
   such as a DataSet or a database (*QueryDatasource*), or the allowable
   keys that can be constructed from a DataStructureDefinition. Multiple
   such constraints may be present for a *ConstrainableArtefact.* For
   instance, there may be a ContentConstraint that specifies the values
   allowed for the *ConstrainableArtefact* (role is allowableContent)
   which can be used for validation or for constructing a partial code
   list, whilst another constraint can specify the actual content of a
   data or metadata source (role is actualContent).

2. AttachmentConstraint – is used as a mechanism to define slices of the
   full set of data and to which metadata can be attached in a Data Set
   or MetadataSet. These slices can be defined either as a set of keys
   (KeySet) or a set of component values (CubeRegion). There can be many
   AttachmentConstraints specified for a specific AttachableArtefact.

In addition to (DataKeySet, MetadataKeySet, CubeRegion,
MetadataTargetRegion, a Constraint can have a ReferencePeriod defining
one of more date ranges (ValidityPeriod) specifying the time period for
which data or metadata are available in the *ConstrainableArtefact* and
a ReleaseCalendar specifying when data are released for publication or
reporting.

Relationship Class Diagram – Detail
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|image63|

Figure 39: Constraints - Key Set Constraints

|image64|

Figure 40: Constraints - Cube Region and Metadata Target Region
Constraints

.. _explanation-of-the-diagram-25:

Explanation of the Diagram
^^^^^^^^^^^^^^^^^^^^^^^^^^

A *Constraint* is a *MaintainableArtefact*.

A *Constraint* has a choice of two ways of specifying value sub sets:

1. As a set of keys that can be present in the DataSet (DataKeySet) or
   MetadataSet (MetadataKeySet). Each DataKey or MetadataKey specifies a
   number of ComponentValues each of which reference a *Component* (e.g.
   Dimension, TargetObject). Each ComponentValue is a value that may be
   present for a *Component* of a structure when contained in a DataSet
   or MetadataSet. The MetadataKeySet must also identify the
   MetadataTarget as there can be many of each of these in a
   MetadataStructureDefinition. For the DataKeySet the equivalent
   identification is not necessary as there is only one
   DimensionDescriptor and one AttributeDescriptor.

2. As a set of CubeRegions or MetadataTaregetRegions each of which
   defines a “slice” of the total structure (MemberSelection) in terms
   of one or more MemberValues that may be present for a *Component* of
   a structure when contained in a *DataSet* or MetadataSet.

The difference between (1) and (2) above is that in (1) a complete key
is defined whereas in (2) above the “slice” defines a list of possible
values for each of the *Component*\ s but does not specify specific key
combinations. In addition, in (1) the association between *Component*
and DataKeyValue or MetadataKeyValue is constrained to the components
that comprise the key or identifier, whereas in (2) it can contain other
component types (such as attributes). The value in ComponentValue.value
and MemberValue.value must be consistent with the *Representation*
declared for the *Component* in the DataStructureDefinition or
MetadataStructureDefinition. Note that in all cases the “operator” on
the value is deemed to be “equals”. Furthermore, it is possible in a
MemberValue to specify that child values (e.g. child codes) are included
in the constraint by means of the cascadeValues attribute.

It is possible to define for the DataKeySet, DataKey, MetadataKeySet,
MetadataKey, CubeRegion, MetadataTargetRegion, and MemberSelection
whether the set is included (isIncluded = “true”) or excluded
(isIncluded = ”false”) from the constraint definition. This attribute is
useful if, for example, only a small sub-set of the possible values are
not included in the set, then this smaller sub-set can be defined and
excluded from the constraint. Note that if the child construct is
“included: and the parent construct is “excluded” then the child
construct is included in the list of constructs that are “excluded”.

.. _definitions-20:

Definitions
^^^^^^^^^^^

========================== ================================ =========================================================================================================================================================================================================
Class                      Feature                          Description
*Constrainable* *Artefact* | Abstract Class                 An artefact that can have Constraints specified.
                           | Sub classes are:              
                                                           
                           | DataflowDefinition            
                           | Metadataflow                  
                           | Definition                    
                           | ProvisionAgreement            
                           | DataProvider                  
                           | *QueryDatasource*             
                           | SimpleDatasource              
                           | DataStructure                 
                           | Definition                    
                           | MetadataStructure Definition  
\                          content                          Associates the metadata that constrains the content to be found in a data or metadata source linked to the Constrainable Artefact.
\                          attachment                       Associates the metadata that constrains the valid content of a Constrainable Artefact to which metadata may be attached.
*Constraint*               Inherits from                    Specifies a sub set of the definition of the allowable or actual content of a data or metadata source that can be derived from the Structure that defines code lists and other valid content.
                                                           
                           *MaintainableArtefact*          
                                                           
                           Abstract class. Sub classes are:
                                                           
                           | AttachmentConstraint          
                           | ContentConstraint             
\                          +availableDates                  Association to the time period that identifies the time range for which data or metadata are available in the data source.
\                          +dataContentKeys                 Association to a sub set of Data Key Sets (i.e. value combinations) that can be derived from the definition of the structure to which the Constrainable Artefact is linked.
\                          +metadataContentKeys             Association to a sub set of Metdata Key Sets (i.e. value combinations) that can be derived from the definition of the Structure to which the Constrainable Artefact is linke
\                          +dataContentRegion               Association to a sub set of component values that can be derived from the Data Structure Definition to which the Constrainable Artefact is linked.
\                          +metadataContentRegion           Association to a sub set of component values that can be derived from the Metadata Structure Definition to which the Constrainable Artefact is linked.
ContentConstraint          Inherits from                    Defines a Constraint in terms of the content that can be found in data or metadata sources linked to the Constrainable Artefact to which this constraint is associated.
                                                           
                           *Constraint*                    
\                          +role                            Association to the role that the Constraint plays
ConstraintRole                                              Specifies the way the type of content of a Constraint in terms of its purpose.
\                          allowableContent                 The Constraint contains a specification of the valid sub set of the Component values or keys.
\                          actualContent                    The Constraint contains a specification of the actual content of a data or metadata source in terms of the Component values or keys in the source.
Attachment                 Inherits from                    Defines a Constraint in terms of the combination of component values that may be found in a data source, and to which a Constrainable Artefact may be associated in a structure definition.
Constraint                                                 
                           *Constraint*                    
DataKeySet                                                  A set of data keys.
\                          isIncluded                       Indicates whether the Data Key Set is included in the constraint definition or excluded from the constraint definition.
\                          +keys                            Association to the Data Keys in the set.
MetadataKeySet                                              A set of metadata keys.
\                          isIncluded                       Indicates whether the Metadata Key Set is included in the constraint definition or excluded from the constraint definition.
\                          +keys                            Association to the Metadata Keys in the set.
DataKey                                                     The values of a key in a data set.
\                          isIncluded                       Indicates whether the Data Key is included in the constraint definition or excluded from the constraint definition.
\                          +keyValue                        Associates the Component Values that comprise the key.
MetadataKey                                                 The values of a key in a metadata set.
\                          isIncluded                       Indicates whether the Metdadata Key is included in the constraint definition or excluded from the constraint definition.
\                          +keyValue                        Associates the Component Values that comprise the key.
ComponentValue                                              The identification of and value of a Component of the key (e.g. Dimension)
\                          value                            The value of Component
\                          +valueFor                        Association to the Component (e.g. Dimension) in the Structure to which the Constrainable Artefact is linked.
TimeDimensionValue                                          The value of the Time Dimension component.
\                          timeValue                        The value of the time period.
\                          operator                         Indicates whether the specified value represents and exact time or time period, or whether the value should be handled as a range.
                                                           
                                                            A value of greaterThan or greaterThanOrEqual indicates that the value is the beginning of a range (exclusive or inclusive, respectively).
                                                           
                                                            A value of lessThan or lessThanOrEqual indicates that the value is the end or a range (exclusive or inclusive, respectively).
                                                           
                                                            In the absence of the opposite bound being specified for the range, this bound is to be treated as infinite (e.g. any time period after the beginning of the provided time period for greaterThanOrEqual)
CubeRegion                                                  A set of Components and their values that defines a sub set or “slice” of the total range of possible content of a data structure to which the Constrainable Artefact is linked.
\                          isIncluded                       Indicates whether the Cube Region is included in the constraint definition or excluded from the constraint definition.
\                          +member                          Associates the set of Components that define the sub set of values.
MetadataTargetRegion                                        A set of Components and their values that defines a sub set or “slice” of the total range of possible content of a metadata structure to which the Constrainable Artefact is linked.
\                          isIncluded                       Indicates whether the Metadata Target Region is included in the constraint definition or excluded from the constraint definition.
\                          +member                          Associates the set of Components that define the sub set of values.
MemberSelection                                             A set of permissible values for one component of the axis.
\                          isIncluded                       Indicates whether the Member Selection is included in the constraint definition or excluded from the constraint definition.
\                          +valuesFor                       Association to the Component in the Structure to which the Constrainable Artefact is linked, which defines the valid Representation for the Member Values.
MemberValue                                                 A single value of the set of values for the Member Selection.
\                          value                            A value of the member.
\                          cascadeValues                    Indicates that the child nodes of the member are included in the Member Selection (e.g. child codes)
*TimeRangeValue*           Abstract Class                   A time value or values that specifies the date or dates for which the constrained selection is valid.
                                                           
                           Concrete Classes                
                                                           
                           | BeforePeriod                  
                           | AfterPeriod                   
                           | RangePeriod                   
BeforePeriod               Inherits from                    The period before which the constrained selection is valid.
                                                           
                           *TimeRangeValue*                
\                          isInclusive                      Indication of whether the date is inclusive in the period.
AfterPeriod                Inherits from                    The period after which the constrained selection is valid.
                                                           
                           *TimeRangeValue*                
\                          isInclusive                      Indication of whether the date is inclusive in the period.
RangePeriod                                                 The start and end periods in a date range.
\                          +start                           Association to the Start Period.
\                          +end                             Association to the End Period.
StartPeriod                Inherits from                    The period from which the constrained selection is valid.
                                                           
                           *TimeRangeValue*                
\                          isInclusive                      Indication of whether the date is inclusive in the period.
EndPeriod                  Inherits from                    The period to which the constrained selection is valid.
                                                           
                           *TimeRangeValue*                
\                          isInclusive                      Indication of whether the date is inclusive in the period.
ReferencePeriod                                             A set of dates that constrain the content that may be found in a data or metadata set.
\                          startDate                        The start date of the period.
\                          endDate                          The end date of the period.
ReleaseCalendar                                             The schedule of publication or reporting of the data or metadata
\                          periodicity                      The time period between the releases of the data or metadata
\                          offset                           Interval between January 1\ :sup:`st` and the first release of the data
\                          tolerance                        Period after which the data or metadata may be deemed late.
========================== ================================ =========================================================================================================================================================================================================

Data Provisioning
=================

.. _class-diagram-15:

Class Diagram
-------------

|image65|

Figure 41: Relationship and inheritance class diagram of data
provisioning

.. _explanation-of-the-diagram-26:

Explanation of the Diagram
--------------------------

.. _narrative-22:

Narrative
~~~~~~~~~

This sub model links many artefacts in the SDMX-IM and is pivotal to an
SDMX metadata registry, as all of the artefacts in this sub model must
be accessible to an application that is responsible for data and
metadata registration or for an application that requires access to the
data or metadata.

Whilst a registry contains all of the metadata depicted on the diagram
above, the classes in the grey shaded area are specific to a registry
based scenario where data sources (either physical data and metadata
sets or databases and metadata repositories) are registered. More
details on how these classes are used in a registry scenario can be
found in the SDMX Registry Interface document. (Section 5 of the SDMX
Standards).

A ProvisionAgreement links the artefact that defines how data and
metadata are structured and classified (*StructureUsage*) to the
DataProvider, and, by means of a data or metadata registration, it
references the Datasource (this can be data or metadata), whether this
be an SDMX conformant file on a website (SimpleDatasource) or a database
service capable of supporting an SDMX query and responding with an SDMX
conformant document (*QueryDatasource*).

The *StructureUsage*, which has concrete classes of DataflowDefinition
and MetadataflowDefinition identifies the corresponding
DataStructureDefinition or MetadataStructureDefinition, and, via
Categorisation, can link to one or more Category in a CategoryScheme
such as a subject matter domain scheme, by which the *StructureUsage*
can be classified. This can assist in drilling down from subject matter
domains to find the data or metadata that may be relevant.

The SimpleDatasource links to the actual DataSet or MetadataSet on a
website (this is shown on the diagram as a dependency called
“references”). The sourceURL is obtained during the registration process
of the DataSet or the MetadataSet. Additional information about the
content of the SimpleDatasource is stored in the registry in terms of a
ContentConstraint (see 10.3) for the Registration.

The QueryDatasource is an abstract class that represents a data source
which can understand an SDMX-ML query (SOAPDatasource) or RESTful query
(RESTDatasource) and respond appropriately. Each of these different
Datasources inherit the dataURL from Datasource, and the QueryDatasource
has an additional URL to locate a WSDL or WADL document to describe how
to access it. All other supported protocols are assumed to use the
SimpleDatasource URL.

The diagram below shows in schematic way the essential navigation
through the SDMX structural artefacts that eventually link to a data or
metadata registration.

|image66|

Figure 42: Schematic of the linking of structural metadata to data and
metadata registration

.. _definitions-21:

Definitions
~~~~~~~~~~~

================== ======================== ============================================================================================================================================================================================================================================================================
Class              Feature                  Description
*StructureUsage*   Abstract class:          This is described in the Base.
                                           
                   Sub classes are:        
                                           
                   | DataflowDefinition    
                   | MetadataflowDefinition
\                  controlledBy             Association to the Provision Agreements that comprise the metadata related to the provision of data.
DataProvider                                See Organisation Scheme.
\                  hasAgreement             Association to the Provision Agreements for which the provider supplies data or metadata.
\                  +source                  Association to a data or metadata source which can process a data or metadata query.
ProvisionAgreement                          Links the Data Provider to the relevant Structure Usage (e.g. Dataflow Definition or Metadataflow Definition) for which the provider supplies data or metadata The agreement may constrain the scope of the data or metadata that can be provided, by means of a Constraint.
\                  +source                  Association to a data or reference metadata source which can process a data or metadata query.
*Datasource*       Abstract class:          Identification of the location or service from where data or reference metadata can be obtained.
                                           
                   Sub classes are:        
                                           
                   SimpleDatasource        
                                           
                   *WebServices            
                   Datasource*             
\                  +sourceURL               The URL of the data or reference metadata source (a file or a web service).
SimpleDatasource                            An SDMX-ML data set accessible as a file at a URL.
*WebServices       Abstract class:          A data or reference metadata source which can process a data or metadata query.
Datasource*                                
                   Inherits from:          
                                           
                   *Datasource*            
                                           
                   Sub classes are:        
                                           
                   RESTDatasource          
                                           
                   SOAPDatasource          
RESTDatasource                              A data or reference metadata source that is accessible via a RESTful web services interface.
SOAPDatasource                              A data or reference metadata source that conforms to a SOAP web service interface.
\                  +WSDLURL                 Association to the URL of the Web Service Definition Language (SOAP) or Web Service Application Language (REST) profile of the web service.
Registration                                This is not detailed here but is shown as the link between the SDMX-IM and the Registry Service API. It denotes a data or metadata registration document.
================== ======================== ============================================================================================================================================================================================================================================================================

Process
=======

.. _introduction-7:

Introduction
------------

In any system that processes data and reference metadata the system
itself is a series of processes and in each of these processes the data
or reference metadata may undergo a series of transitions. This is
particularly true of its path from raw data to published data and
reference metadata. The process model presented here is a generic model
that can capture key information about these stages in both a textual
way and also in a more formalised way by linking to specific
identifiable objects, and by identifying software components that are
used.

Model – Inheritance and Relationship view
-----------------------------------------

.. _class-diagram-16:

Class Diagram
~~~~~~~~~~~~~

|image67|

Figure 43: Inheritance and Relationship class diagram of Process and
Transitions

.. _explanation-of-the-diagram-27:

Explanation of the Diagram
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _narrative-23:

Narrative
^^^^^^^^^

The Process is a set of hierarchical ProcessSteps. Each ProcessStep can
take zero or more *IdentifiableArtefact*\ s as input and output. Each of
the associations to the input and output *IdentifiableArtefact*\ s
(ProcessArtefact) can be assigned a localID.

The computation performed by a ProcessStep is optionally described by a
Computation, which can identify the software used by the ProcessStep and
can also be described in textual form (+description) in multiple
language variants. The Transition describes the execution of
ProcessSteps from +source ProcessStep to +target ProcessStep based on
the outcome of a +condition that can be described in multiple language
variants.

.. _definitions-22:

Definitions
^^^^^^^^^^^

=============== ====================== ===================================================================================================================================================================================
Class           Feature                Description
Process         Inherits from          A scheme which defines or documents the operations performed on data or metadata in order to validate data or metadata to derive new information according to a given set of rules.
                                      
                *Maintainable*        
\               +step                  Associates the Process Steps.
ProcessStep     Inherits from          A specific operation, performed on data or metadata in order to validate or to derive new information according to a given set of rules.
                                      
                *IdentifiableArtefact*
\               +input                 Association to the Process Artefact that identifies the objects which are input to the Process Step.
\               +output                Association to the Process Artefact that identifies the objects which are output from the Process Step.
\               +child                 Association to child Processes that combine to form a part of this Process.
\               +computation           Association to one or more Computations.
\               +transition            Association to one or more Transitions.
Computation                            Describes in textual form the computations involved in the process.
\               localId                Distinguishes between Computations in the same Process.
\               softwarePackage        Information about the software that is used to perform the computation.
                softwareLanguage      
                softwareVersion       
\               +description           Text describing or giving additional information about the computation. This can be in multiple language variants.
Transition      Inherits from          An expression in a textual or formalised way of the transformation of data between two specific operations (Processes) performed on the data.
                                      
                *IdentifiableArtefact*
\               +target                Associates the Process Step that is the target of the Transition.
\               +condition             Associates a textual description of the Transition.
ProcessArtefact                        Identification of an object that is an input to or an output from a Process Step.
\               +artefact              Association to an Identifiable Artefact that is the input to or the output from the Process Step.
=============== ====================== ===================================================================================================================================================================================

Transformations and Expressions
===============================

.. _scope-3:

Scope
-----

The purpose of this package in the model is to be able to track the
derivation of data. It is similar in concept to lineage in data
warehousing – i.e. how data are derived.

The functionality of this part of the model allows the identification
and documentation of the calculations performed (these will normally be
automated, program calculations), as well as defining structures that
support a syntax neutral expression “grammar” that can specify the
operations at a granular level such that a program can “read” the
metadata and compose the expression required in whatever computer
language is appropriate.

This part of the model also allows specifying and documenting the
coherence rules among different data, expressing them as calculations
(for example, the coherence rule “a + b = c” can be written as “a + b -
c = 0” and checked through the calculation “if((a + b – c) = 0, then …,
else …)”).

It should be noted that the model represented below is similar in scope
and content to the Expression metamodel in the Common Warehouse
Metamodel (CWM) developed by the Object Management Group (OMG). This
specification can be found at:

http://www.omg.org/cwm

The Expression metamodel is described in Section 8.5 of Part 1 of the
CWM specification. The class diagram shown below is an interpretation of
the CWM Expression metamodel expressed in the base classes of the
SDMX-IM.

Model - Inheritance View
------------------------

.. _class-diagram-17:

Class Diagram
~~~~~~~~~~~~~

|image68|

Figure 44: Inheritance and relationship class diagram of transformation
classes

.. _explanation-of-the-diagram-28:

Explanation of the Diagram
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _narrative-24:

Narrative
^^^^^^^^^

There are three type of *ItemScheme* relevant to this model.

1. A TransformationScheme which comprises one or more Transformations.

2. An OperatorScheme which comprises one or more *Operator*\ s.

3. An ExpressionNodeScheme scheme which contains one or more
   ExpressionNodes..

The model presented here is a basic framework which can be used for
expressions and transformations, but requires more work on elaborating
its integration into the model and its actual use within the model. This
elaboration will be in a future release of the standard.

The expression concept in the SDMX-IM takes a functional view of
expression trees, resulting in the ability of relatively few expression
node types to represent a broad range of expressions. Every function or
traditional mathematical operator that appears in an expression
hierarchy is represented by the +operator role on the association to
Operator which in turn comprises input and output Parameter. For
example, the arithmetic plus operation “a + b” can be thought of as the
function “sum(a, b).” The “sum” is the Operator, and “a” and “b” are its
Parameters. A parameter is a generic possible input and output of an
operator (e.g. base and exponent are the parameters of the power
operator), while an argument is the specific value that a parameter
takes in a specific calculation (e.g. in the Einstein equation “E =
MC\ :sup:`2`\ ”. the arguments of the “power” operation are “C” (the
base) and “2” (the exponent)).The actual semantics of a particular
function or operation are left to specific tool implementations and are
not captured by the SDMX-IM.

The hierarchical nature of the SDMX-IM representation of expressions is
achieved by the recursive nature of the OperatorNode association. This
association allows the sub-hierarchies within an expression to be
treated as actual arguments of their parent nodes.

The model can be used equally to define data derivations and to define
integrity checks (e.g. the Sum of A+B must equal C).

Although the model defines the data structures that are used to contain
a syntax neutral expression, the model itself does not specify a syntax
neutral expression grammar. Alternatively, the function can be described
in a text form either as an unstructured explanation of the function, or
as a more formal language like BNF [2]_.

The data structures work as follows:

The actual basic mathematical functions that need to be performed (e.g.
sum, multiply, divide, assign (=), <, > etc.) are defined as Operators
an OperatorScheme. For each Operator the input and output Parameters,
are defined in the Parameter class.

The calculations are defined as Transformations in a
TransformationScheme. A Transformation is a specific calculation and is
specified by means of an expression, which is obtained by applying one
or more Operators in the desired order (for example, in the textual
form, using parenthesis) and specifying the actual arguments for the
Operators’ Parameters; the result of the whole expression is assigned
(=) to the model item that is the result of the Transformation (that is
“E” in the Einstein equation). A Transformation operates on existing
IdentifiableArtefacts and its result is another IdentifiableArtefact. A
calculated IdentifiableArtefact may be in its turn be an operand of
other Transformations.

The expression of a Transformation (for example, for the Einstein
equation calculus, “E = M*(C**2)”) may be decomposed in a hierarchy of
ExpressionNodes (in the example, “M”, “C”, “2”, \*, \**). The
ExpressionNode can be a ReferenceNode, a ConstantNode or an
OperatorNode. The ReferenceNode references an identifiable model
artefact (in the example, “M” and “C”). The ConstantNode is by
definition a constant value (in the example “2”). The OperatorNode
references an Operator in the OperatorScheme (in the example \*, \**).
The Transformation has an association to its component ExpressionNodes.

The hierarchy of the ExpressionNodes conveys the order in which the
operators are applied in the expression and is obtained by means of the
/hierarchy association of the OperatorNode class, in which the child
ExpressionNodes are the arguments of the parent OperatorNode. The child
ExpressionNodes must correspond to the formal parameters of the Operator
referenced by the parent OperatorNode in the correct sequence. The
(child) ExpressionNode can be the result of another operation (that is
another OperatorNode) or can be a Constant or can be a reference to an
*IdentifiableArtefact* (ReferenceNode). All *IdentifiableArtefacts* in
the SDMX-IM have a unique urn comprising the values of the individual
objects that identify it. The structure of this urn is defined in the
Registry Specification. An example would be the urn of a code which
comprises the agency:code-list-id.code-id – an actual example is
"urn:sdmx:org.sdmx.infomodel.codelist.Code=TFFS:CL_AREA(1.0).1A".

.. _definitions-23:

Definitions
^^^^^^^^^^^

================ ==================== =====================================================================================================================
Class            Feature              Description
Transformation   Inherits from        A scheme which defines or documents the transformations required in order to derive or validate data from other data.
Scheme                               
                 *ItemScheme*        
Transformation   Inherits from        An individual Transformation.
                                     
                 *Item*              
\                +expressionComponent Association to an Expression Node.
*ExpressionNode* Abstract class       A node in a possible hierarchy of nodes that together define or document an expression.
                                     
                 Sub Classes         
                                     
                 *ReferenceNode*     
                                     
                 *ConstantNode*      
                                     
                 *OperatorNode*      
\                /hierarchy           Association to child Expression Nodes
ReferenceNode    Inherits from        A specific type of Expression Node that references a specific object.
                                     
                 *ExpressionNode*    
\                references           Association to the Identifiable Artefact that is the referenced object.
ConstantNode     Inherits from        A specific type of Expression Node that contains a constant value.
                                     
                 *ExpressionNode*    
\                *value*              The value of the Constant
OperatorNode     Inherits from        A specific type of Expression Node that references an Operator
                                     
                 *ExpressionNode*    
\                +operator            Association to an Operator that defines the mathematical operator of the Operator Node.
\                +arguments           Association to mathematical arguments of an Operator Node.
OperatorScheme   Inherits from        A scheme which defines mathematical operators.
                                     
                 *ItemScheme*        
Operator         Inherits from        The mathematical operator in an Operator Scheme.
                                     
                 *Item*              
\                +input               Association to the input Parameters of the Operator
\                +output              Association to the output Parameter of the Operator.
Parameter                             The input or output of an Operator.
================ ==================== =====================================================================================================================

Appendix 1: A Short Guide To UML in the SDMX Information Model
==============================================================

.. _scope-4:

Scope
-----

The scope of this document is to give a brief overview of the diagram
notation used in UML. The examples used in this document have been taken
from the SDMX UML model.

.. _use-cases-2:

Use Cases
---------

In order to develop the data models it is necessary to understand the
functions that require to be supported. These are defined in a use case
model. The use case model comprises actors and use cases and these are
defined below.

The **actor** can be defined as follows:

   “An actor defines a coherent set of roles that users of the system
   can play when interacting with it. An actor instance can be played by
   either an individual or an external system”

The actor is depicted as a stick man as shown below.

|image69|

Figure 45 Actor

The **use cas**\ e can be defined as follows:

   “A use case defines a set of use-case instances, where each instance
   is a sequence of actions a system performs that yields an observable
   result of value to a particular actor”

|image70|

Figure 46 Use case

|image71|

Figure 47 Actor and use case

|image72|

Figure 48 Extend use cases

An extend use case is where a use case may be optionally extended by a
use case that is independent of the using use case. The arrow in the
association points to he owning use case of the extension. In the
example above the Uses Data use case is optionally extended by the Uses
Metadata use case.

Classes and Attributes
----------------------

General
~~~~~~~

A class is something of interest to the user. The equivalent name in an
entity-relationship model (E-R model) is the entity and the attribute.
In fact, if the UML is used purely as a means of modelling data, then
there is little difference between a class and an entity.

|image73|

Figure 49 Class and its attributes

Figure 49 shows that a class is represented by a rectangle split into
three compartments. The top compartment is for the class name, the
second is for attributes and the last is for operations. Only the first
compartment is mandatory. The name of the class is Annotation, and it
belongs to the package SDMX-Base. It is common to group related
artefacts (classes, use-cases, etc.) together in packages. . Annotation
has three “String” attributes – name, type, and url. The full identity
of the attribute includes its class e.g. the name attribute is
Annotation.name.

Note that by convention the class names use UpperCamelCase – the words
are concatenated and the first letter of each word is capitalized. An
attribute uses lowerCamelCase - the first letter of the first (or only)
word is not capitalized, the remaining words have capitalized first
letters.

Abstract Class
~~~~~~~~~~~~~~

An abstract class is drawn because it is a useful way of grouping
classes, and avoids drawing a complex diagram with lots of association
lines, but where it is not foreseen that the class serves any other
purpose (i.e. it is always implemented as one of its sub classes). In
the diagram in this document an abstract class is depicted with its name
in italics, and coloured white.

|image74|

Figure 50 Abstract and concrete classes

Associations
------------

.. _general-1:

General
~~~~~~~

In an E-R model these are known as relationships. A UML model can give
more meaning to the associations than can be given in an E-R
relationship. Furthermore, the UML notation is fixed (i.e. there is no
variation in the way associations are drawn). In an E-R diagram, there
are many diagramming techniques, and it is the relationship in an E-R
diagram that has many forms, depending on the particular E-R notation
used.

Simple Association
~~~~~~~~~~~~~~~~~~

|image75|

Figure 51 A simple association

Here the DataflowDefinition class has an association with the
DataStructureDefinition class. The diagram shows that a
DataflowDefinition can have an association with only one
DataStructureDefinition (1) and that a DataStructureDefinition can be
linked to many DataflowDefinitions (0..*). The association is sometimes
named to give more semantics.

In UML it is possible to specify a variety of “multiplicity” rules. The
most common ones are:

-  Zero or one (0..1)

-  Zero or many (0..*)

-  One or many (1..*)

-  Many (*)

-  Unspecified (blank)

Aggregation
~~~~~~~~~~~

|image76|

Figure 52: A simple aggregate association

|image77|

Figure 53 A composition aggregate association

An association with an aggregation relationship indicates that one class
is a subordinate class (or a part) of another class. In an aggregation
relationship. There are two types of aggregation, a simple aggregation
where the child class instance can outlive its parent class, and a
composition aggregation where

the child class's instance lifecycle is dependent on the parent class's
instance lifecycle. In the simple aggregation it is usual, in the SDMX
Information model, for this association to also be a reference to the
associated class.

Association Names and Association-end (role) Names
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

It can be useful to name associations as this gives some more semantic
meaning to the model i.e. the purpose of the association. It is possible
for two classes to be joined by two (or more) associations, and in this
case it is extremely useful to name the purpose of the association.
Figure 54 shows a simple aggregation between CategoryScheme and Category
called /*items* (this means it is derived from the association between
the super classes – in this case between the *ItemScheme* and the
*Item,* and another between Category called /*hierarchy*.

|image78|

Figure 54 Association names and end names

Furthermore, it is possible to give role names to the association-ends
to give more semantic meaning – such as parent and child in a tree
structure association. The role is shown with “+” preceding the role
name (e.g. in the diagram above the semantic of the association is that
a Item can have zero or one parent Items and zero or many child Item).

In this model the preference has been to use role names for associations
between concrete classes and association names for associations between
abstract classes. The reason for using an association name is often
useful to show a physical association between two sub classes that
inherit the actual association between the super class from which they
inherit. This is possible to show in the UML with association names, but
not with role names. This is covered later in “Derived Association”.

Note that in general the role name is given at just one end of the
association.

Navigability
~~~~~~~~~~~~

Associations are, in general, navigable in both directions. For a
conceptual data model it is not necessary to give any more semantic than
this.

However, UML allows a notation to express navigability in one direction
only. In this model this “navigability” feature has been used to
represent referencing. In other words, the class at the navigable end of
the association is referenced from the class at the non-navigable end.
This is aligned, in general, with the way this is implemented in the XML
schemas.

|image79|

Figure 55 One way association

Here it is possible to navigate from A to B, but there is no
implementation support for navigatation from B to A using this
association.

.. _inheritance-3:

Inheritance
~~~~~~~~~~~

Sometimes it is useful to group common attributes and associations
together in a super class. This is useful if many classes share the same
associations with other classes, and have many (but not necessarily all)
attributes in common. Inheritance is shown as a triangle at the super
class.

|image80|

Figure 56 Inheritance

Here the Dimension is derived from Component which itself is derived
from *IdentifiableArtefact*. Both Component and IdentifiableArtefact are
abstract superclasses. The Dimension inherits the attributes and
associations of all of the the super classes in the inheritance tree.
Note that a super class can be a concrete class (i.e. it exists in its
own right as well as in the context of one of its sub classes), or an
abstract class.

Derived association
~~~~~~~~~~~~~~~~~~~

It is often useful in a relationship diagram to show associations
between sub classes that are derived from the associations of the super
classes from which the sub classes inherit. A derived association is
shown by “/” preceding the association name e.g. */name*.

|image81|

Figure 57 Derived associations

.. [1]
   OLAP: On line analytical processing

.. [2]
   BNF: Backus Naur Form

.. |image0| image:: /_static/media-SDMX_2_1_SECTION_2_InformationModel/media/image2.png
.. |image1| image:: /_static/media-SDMX_2_1_SECTION_2_InformationModel/media/image3.png
.. |image2| image:: /_static/media-SDMX_2_1_SECTION_2_InformationModel/media/image4.jpeg
.. |image3| image:: /_static/media-SDMX_2_1_SECTION_2_InformationModel/media/image5.png
.. |image4| image:: /_static/media-SDMX_2_1_SECTION_2_InformationModel/media/image6.png
.. |image5| image:: /_static/media-SDMX_2_1_SECTION_2_InformationModel/media/image7.png
.. |image6| image:: /_static/media-SDMX_2_1_SECTION_2_InformationModel/media/image8.png
.. |image7| image:: /_static/media-SDMX_2_1_SECTION_2_InformationModel/media/image9.png
.. |image8| image:: /_static/media-SDMX_2_1_SECTION_2_InformationModel/media/image10.png
.. |image9| image:: /_static/media-SDMX_2_1_SECTION_2_InformationModel/media/image11.png
.. |image10| image:: /_static/media-SDMX_2_1_SECTION_2_InformationModel/media/image12.png
.. |image11| image:: /_static/media-SDMX_2_1_SECTION_2_InformationModel/media/image13.png
.. |image12| image:: /_static/media-SDMX_2_1_SECTION_2_InformationModel/media/image14.png
.. |image13| image:: /_static/media-SDMX_2_1_SECTION_2_InformationModel/media/image15.png
.. |image14| image:: /_static/media-SDMX_2_1_SECTION_2_InformationModel/media/image16.png
.. |image15| image:: /_static/media-SDMX_2_1_SECTION_2_InformationModel/media/image17.png
.. |image16| image:: /_static/media-SDMX_2_1_SECTION_2_InformationModel/media/image18.png
.. |image17| image:: /_static/media-SDMX_2_1_SECTION_2_InformationModel/media/image19.png
.. |image18| image:: /_static/media-SDMX_2_1_SECTION_2_InformationModel/media/image20.png
.. |image19| image:: /_static/media-SDMX_2_1_SECTION_2_InformationModel/media/image21.png
.. |image20| image:: /_static/media-SDMX_2_1_SECTION_2_InformationModel/media/image22.png
.. |image21| image:: /_static/media-SDMX_2_1_SECTION_2_InformationModel/media/image23.png
.. |image22| image:: /_static/media-SDMX_2_1_SECTION_2_InformationModel/media/image24.png
.. |image23| image:: /_static/media-SDMX_2_1_SECTION_2_InformationModel/media/image25.png
.. |image24| image:: /_static/media-SDMX_2_1_SECTION_2_InformationModel/media/image26.png
.. |image25| image:: /_static/media-SDMX_2_1_SECTION_2_InformationModel/media/image27.png
.. |image26| image:: /_static/media-SDMX_2_1_SECTION_2_InformationModel/media/image28.png
.. |image27| image:: /_static/media-SDMX_2_1_SECTION_2_InformationModel/media/image29.png
.. |image28| image:: /_static/media-SDMX_2_1_SECTION_2_InformationModel/media/image30.png
.. |image29| image:: /_static/media-SDMX_2_1_SECTION_2_InformationModel/media/image31.png
.. |image30| image:: /_static/media-SDMX_2_1_SECTION_2_InformationModel/media/image32.png
.. |image31| image:: /_static/media-SDMX_2_1_SECTION_2_InformationModel/media/image33.png
.. |image32| image:: /_static/media-SDMX_2_1_SECTION_2_InformationModel/media/image34.png
.. |image33| image:: /_static/media-SDMX_2_1_SECTION_2_InformationModel/media/image35.png
.. |image34| image:: /_static/media-SDMX_2_1_SECTION_2_InformationModel/media/image36.png
.. |image35| image:: /_static/media-SDMX_2_1_SECTION_2_InformationModel/media/image37.png
.. |image36| image:: /_static/media-SDMX_2_1_SECTION_2_InformationModel/media/image38.png
.. |image37| image:: /_static/media-SDMX_2_1_SECTION_2_InformationModel/media/image39.png
.. |image38| image:: /_static/media-SDMX_2_1_SECTION_2_InformationModel/media/image40.png
.. |image39| image:: /_static/media-SDMX_2_1_SECTION_2_InformationModel/media/image41.png
.. |image40| image:: /_static/media-SDMX_2_1_SECTION_2_InformationModel/media/image42.png
.. |image41| image:: /_static/media-SDMX_2_1_SECTION_2_InformationModel/media/image43.png
.. |image42| image:: /_static/media-SDMX_2_1_SECTION_2_InformationModel/media/image44.png
.. |image43| image:: /_static/media-SDMX_2_1_SECTION_2_InformationModel/media/image45.png
.. |image44| image:: /_static/media-SDMX_2_1_SECTION_2_InformationModel/media/image46.png
.. |image45| image:: /_static/media-SDMX_2_1_SECTION_2_InformationModel/media/image47.png
.. |image46| image:: /_static/media-SDMX_2_1_SECTION_2_InformationModel/media/image48.png
.. |image47| image:: /_static/media-SDMX_2_1_SECTION_2_InformationModel/media/image49.png
.. |image48| image:: /_static/media-SDMX_2_1_SECTION_2_InformationModel/media/image50.png
.. |image49| image:: /_static/media-SDMX_2_1_SECTION_2_InformationModel/media/image51.png
.. |image50| image:: /_static/media-SDMX_2_1_SECTION_2_InformationModel/media/image52.png
.. |image51| image:: /_static/media-SDMX_2_1_SECTION_2_InformationModel/media/image53.png
.. |image52| image:: /_static/media-SDMX_2_1_SECTION_2_InformationModel/media/image54.png
.. |image53| image:: /_static/media-SDMX_2_1_SECTION_2_InformationModel/media/image55.png
.. |image54| image:: /_static/media-SDMX_2_1_SECTION_2_InformationModel/media/image56.png
.. |image55| image:: /_static/media-SDMX_2_1_SECTION_2_InformationModel/media/image57.png
.. |image56| image:: /_static/media-SDMX_2_1_SECTION_2_InformationModel/media/image58.png
.. |image57| image:: /_static/media-SDMX_2_1_SECTION_2_InformationModel/media/image59.png
.. |image58| image:: /_static/media-SDMX_2_1_SECTION_2_InformationModel/media/image60.png
.. |image59| image:: /_static/media-SDMX_2_1_SECTION_2_InformationModel/media/image61.png
.. |image60| image:: /_static/media-SDMX_2_1_SECTION_2_InformationModel/media/image62.png
.. |image61| image:: /_static/media-SDMX_2_1_SECTION_2_InformationModel/media/image63.png
.. |image62| image:: /_static/media-SDMX_2_1_SECTION_2_InformationModel/media/image64.png
.. |image63| image:: /_static/media-SDMX_2_1_SECTION_2_InformationModel/media/image65.png
.. |image64| image:: /_static/media-SDMX_2_1_SECTION_2_InformationModel/media/image66.png
.. |image65| image:: /_static/media-SDMX_2_1_SECTION_2_InformationModel/media/image67.png
.. |image66| image:: /_static/media-SDMX_2_1_SECTION_2_InformationModel/media/image68.jpeg
.. |image67| image:: /_static/media-SDMX_2_1_SECTION_2_InformationModel/media/image69.png
.. |image68| image:: /_static/media-SDMX_2_1_SECTION_2_InformationModel/media/image70.png
.. |image69| image:: /_static/media-SDMX_2_1_SECTION_2_InformationModel/media/image71.png
.. |image70| image:: /_static/media-SDMX_2_1_SECTION_2_InformationModel/media/image72.png
.. |image71| image:: /_static/media-SDMX_2_1_SECTION_2_InformationModel/media/image73.png
.. |image72| image:: /_static/media-SDMX_2_1_SECTION_2_InformationModel/media/image74.png
.. |image73| image:: /_static/media-SDMX_2_1_SECTION_2_InformationModel/media/image75.png
.. |image74| image:: /_static/media-SDMX_2_1_SECTION_2_InformationModel/media/image76.png
.. |image75| image:: /_static/media-SDMX_2_1_SECTION_2_InformationModel/media/image77.png
.. |image76| image:: /_static/media-SDMX_2_1_SECTION_2_InformationModel/media/image78.png
.. |image77| image:: /_static/media-SDMX_2_1_SECTION_2_InformationModel/media/image79.png
.. |image78| image:: /_static/media-SDMX_2_1_SECTION_2_InformationModel/media/image80.png
.. |image79| image:: /_static/media-SDMX_2_1_SECTION_2_InformationModel/media/image81.png
.. |image80| image:: /_static/media-SDMX_2_1_SECTION_2_InformationModel/media/image82.png
.. |image81| image:: /_static/media-SDMX_2_1_SECTION_2_InformationModel/media/image83.png

