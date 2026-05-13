# Change History

## Version 1.0 – initial release September 2004

## Version 2.0 – release November 2005

Major functional enhancements by addition of new packages:

- Metadata Structure Definition
- Metadata Set
- Hierarchical Code Scheme
- Data and Metadata Provisioning
- Structure Set and Mappings
- Transformations and Expressions
- Process and Transitions

Re-engineering of some SDMX Base structures to give more functionality:

- Item Scheme and Item can have properties – this gives support for
complex hierarchical code schemes (where the property can be used to
sequence codes in scheme), and Item Scheme mapping tables (where the
property can give additional information about the map between the two
schemes and the between two Items)
- revised Organisation pattern to support maintained schemes of
organisations, such as a data provider
- modified Component Structure pattern to support identification of roles
played by components and the attachment of attributes
- change to inheritance to enable more artefacts to be identifiable and
versionable

Introduction of new types of Item Scheme:

- Object Type Scheme to specify object types in support of the
    Metadata Structure Definition (principally the object types
    (classes) in this Information Model)
- Type Scheme to specify types other than object type
- A generic Item Scheme Association to specify the association between
    Items in two or more Item Schemes, where such associations cannot be
    described in the Structure Set and Transformation.

The Data Structure Definition is introduced as a synonym for Key Family
though the term Key Family is retained and used in this specification.

Modification to Data Structure Definition (DSD) to

- align the cross sectional structures with the functionality of the
schema
- support Data Structure Definition extension (i.e. to derive and extend a
Data Structure Definition from another Data Structure Definition), thus
supporting the definition of a related “set” of key families
- distinguish between data attributes (which are described in a Data
Structure Definition) from metadata attributes (which are described in a
metadata structure definition)
- attach data attributes to specific identifiable artefacts (formally this
was supported by attachable artefact)
- Domain Category Scheme re-named Category Scheme to better reflect the
multiple usage of this type of scheme (e.g. subject matter domain,
reporting taxonomy).
- Concept Scheme enhanced to allow specification of the representation of
the Concept. This specification is the default (or core) representation
and can be overridden by a construct that uses it (such as a Dimension
in a Data Structure Definition).
- Revision of cross sectional data set to reflect the functionality of the
version 1.0 schema.
- Revision of Actors and Use Cases to reflect better the functionality
supported.

## Version 2.1 – release April 2011

The purpose of this revision is threefold:

- To introduce requested changes to functionality
- To align the model and syntax implementations more closely (note,
    however, that the model remains syntax neutral)
- To correct errors in version 2.0

### SDMX Base

#### Basic inheritance and patterns

1. The following attributes are added to Maintainable:
    1. `isExternalReference`
    2. structure URL
    3. `serviceURL`
2. Added Nameable Artefact and moved the Name and Description
    associations from Identifiable Artefact to Nameable Artefact. This
    allows an artefact to be identified (with id and urn) without the
    need to specify a Name.
3. Removed any inheritance from Versionable Artefact with the exception
    of Maintainable Artefact – this means that only Maintainable objects
    can be versioned, and objects contained in a maintainable object
    cannot be independently versioned.
4. Renamed `MaintenanceAgency` to Agency 0 this is its name in the schema
    and the URN.
5. Removed abstract class Association as a subclass of Item (as these
    association types are not maintained in Item Schemes). Specific
    associations are modelled explicitly (e.g. `Categorisation`,
    `ItemScheme`, `Item`).
6. Added `ActionType` to data types.
7. Removed Coded Artefact and Uncoded Artefact and all subclasses (e.g.
    Coded Data Attribute and Uncoded Data Attribute) as the
    “Representation” is more complex than just a distinction between
    coded and uncoded.
8. Added Representation to the Component. Removed association to Type.
9. Removed concept role association (to Item) as roles are identified
    by a relationship to a Concept.
10. Removed abstract class Attribute as both Data Attribute and Metadata
    Attribute have different properties. Data Attribute and Metadata
    Attribute inherit directly from Component.
11. `isPartial` attribute added to Item Scheme to support partial Item
    Schemes (e.g. partial Code list).

#### Representation

1. Removed interval and enumeration from Facet.
2. added `facetValueType` to Facet.
3. Re-named `DataType` to `facetValueType`.
4. Added `observationalTimePeriod`, `inclusiveValueRange` and
    `exclusiveValueRange` to `facetValueType`.
5. Added `ExtendedFacetType` as a sub class of `FacetType`. This includes
    Xhtml as a facet type to support this as an allowed representation
    for a Metadata Attribute

#### Organisations

1. Organisation Role is removed and replaced with specific Organisation
    Schemes of Agency, Data Provider, Data Consumer, Organisation Unit.

#### Mapping (Structure Maps)

Updated Item Scheme Association as follows:

1. Renamed to Item Scheme Map to reflect better the sub classes and
    relate better to the naming in the schema.
2. Removed inheritance of Item Scheme Map from Item Scheme, and
    inherited directly from Nameable Artefact.
3. Item Association inherits from Identifiable Artefact.
4. Removed Property from the model as this is not supported in the
    schema.
5. Removed association type between Item Scheme Map and Item, and
    Association and Item.
6. Removed Association from the model.
7. Made Item Association a sub class of Identifiable, was a sub class
    Item.
8. Removed association to Property from both Item Scheme Map and Item.
9. Added attribute alias to both Item Scheme Association and Item
    Association.
10. Made Item Scheme Map and Item Association abstract.
11. Added sub-classes to Item Scheme Map – there is a subclass for each
    type of Item Scheme Association (e.g. Code list Map).
12. Added mapping between Reporting Taxonomy as this is an Item Scheme
    and can be mapped in the same way as other Item Schemes.
13. Added Hybrid Code list Map and Hybrid Code Map to support code
    mappings between a Code list and a Hierarchical Code list.

#### Mapping: Structure Map

1. This is a new diagram. Essentially removed inherited /hierarchy
    association between the various maps, as these no longer inherit
    from Item, and replaced the associations to the abstract
    Maintainable and Versionable Artefact classes with the actual
    concrete classes.
2. Removed associations between Code list Map, Category Scheme Map, and
    Concept Scheme Map and made this association to Item Scheme Map.
3. Removed hierarchy of Structure Map.

#### Concept

1. Added association to Representation.

#### Data Structure Definition

1. Added Measure Dimension to support structure-specific renderings of
    the DSD. The Measure Dimension is associated to a Concept Scheme
    that specifies the individual measures that are valid.
2. The three types of “Dimension”, - Dimension, Measure Dimension, Time
    Dimension – have a super class – Dimension Component
3. Added association to a Concept that defines the role that the
    component (Dimension, Data Attribute, Measure Dimension) plays in
    the DSD. This replaces the Boolean attributes on the components.
4. Added Primary Measure and removed this as role of Measure.
5. Deleted the derived Data Structure Definition association from Data
    Structure Definition to itself as this is not supported directly in
    DSD.
6. Deleted attribute `GroupKeyDescriptor.isAttachmentConstraint` and
    replaced with an association to an Attachment Constraint.
7. Replaced association from Data Attribute to Attachable Artefact with
    association to Attribute Relationship.
8. Added a set of classes to support Attribute Relationship.
9. Renamed `KeyDescriptor` to `DimensionDescriptor` to better reflect its
    purpose.
10. Renamed `GroupKeyDescriptor` to `GroupDimensionDescriptor` to better
    reflect its purpose.

#### Code list

1. `CodeList` classname changed to `Codelist`.
2. Removed `codevalueLength` from `Codelist` as this is supported by Facet.
3. Removed `hierarchyView` association between Code and Hierarchy as this
    association is not implemented.

#### Metadata Structure Definition(MSD)

1. Full Target Identifier, Partial Target Identifier, and Identifier
    Component are replaced by Metadata Target and Target Object.
    Essentially this eliminates one level of specification and reference
    in the MSD, and so makes the MSD more intuitive and easier to
    specify and to understand.
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
    reference more than on Metadata Target. This allowing a single
    Report Structure to be defined for many object types.
7. Added the ability to specify that a Metadata Attribute can be
    repeated in a Metadata Set and that a Metadata Attribute can be
    specified as “presentational” meaning that it is present for
    structural and presentational purposes, and will not have content in
    a Metadata Set.
8. The Representation of a Metadata Attribute uses Extended Facet (to
    support Xhtml).

#### Metadata Set

1. Added link to Data Provider - 0..1 but note that for metadata set
    registration this will be 1.
2. Removed Attribute Property as the underlying Property class has been
    removed.
3. One Metadata Set is restricted to reporting metadata for a single
    MSD.
4. The Metadata Report classes are re-structured and re-named to be
    consistent with the renaming and restructuring of the MSD.
5. Metadata Attribute Value is renamed Reported Attribute to be
    consistent with the schemas.
6. Deleted XML attribute and Contact Details from the inheritance
    diagram.

#### Category Scheme

1. Added Categorisation. Category no longer has a direct association to
    Dataflow and Metadataflow.
2. Changed Reporting Taxonomy inheritance from Category Scheme to
    Maintainable Artefact.
3. Added Reporting Category and associated this to Structure Usage.

#### Data Set

1. Removed the association to Provision Agreement from the diagram.
2. Added association to Data Structure Definition. This association was
    implied via the dataflow but this is optional in the implementation
    whereas the association to the Data Structure Definition is
    mandatory.
3. Added attributes to Data Set.
4. There is a single, unified, model of the Data Set which supports
    four types of data set:
    - Generic Data Set – for reporting any type of data series,
        including time series and what is sometimes known as “cross
        sectional data”. In this data set, the value of any one
        dimension (including the Time Dimension) can be reported with
        the observation (this must be for the same dimension for the
        entire data set)
    - Structure-specific Data Set – for reporting a data series that
        is specific to a DSD
    - Generic Time Series Data Set – this is identical to the Generic
        Data Set except it must contain only time series, which means
        that a value for the Time Dimension is reported with the
        Observation
    - Structure-specific Time Series Data Set - this is identical to
        the Structure-specific Data Set except it must contain only time
        series, which means that a value for the Time Dimension is
        reported with the Observation.
5. Removed Data Set as a sub class of Identifiable – but note that Data
    Set has a `setId` attribute.
6. Added coded and uncoded variants of Key Value, Observation, and
    Attribute Value in order to show the relationship between the coded
    values in the data set and the Codelist in the Data Structure
    Definition.
7. Made Key Value abstract with sub classes for coded, uncoded, measure
    (`MeasureKeyValue`) ads time (`TimeKeyValue`) The Measure Key Value is
    associated to a Concept as it must take its identify from a Concept.

#### XSDataSet

1. This is removed and replaced with the single, unified data set
    model.

#### Constraint

1. Constraint is made Maintainable (was Identifiable).
2. Added artefacts that better support and distinguish (from data) the
    constraints for metadata.
3. Added Constraint Role to specify the purpose of the Constraint. The
    values are allowable content (for validation of sub set code code
    lists), and actual content (to specify the content of a data or
    metadata source).

#### Process

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

#### Hierarchical Codelist

1. Renamed `HierarchicalCodeList` to `HierarchicalCodelist`.
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

#### Provisioning and Registration

1. Data Provider and Provision Agreement have an association to
    Datasource (was Query Datasource), as the association is to any of
    Query Datasource and Simple Datasource.
2. Provision Agreement is made Maintainable and indexing attributes
    moved to Registration
3. Registration has a registry assigned Id and indexing attributes.

## Version 2.1 (Revision 2.0) – release June 2020

The package 13, previously named “Expressions and Transformations” is
completely reformulated, renamed as “Validation and Transformation
Language” and implemented also in the other Sections of the SDMX
standards for actual use.

## Version 3.0 – release September 2021

New Maintainable Artefacts

- Structure Map
- Representation Map
- Organisation Scheme Map
- Concept Scheme Map
- Category Scheme Map
- Reporting Taxonomy Map
- Value List
- Hierarchy
- Hierarchy Association
- Metadata Constraint
- Data Constraint
- Metadata Provision Agreement
- Metadata Provider Scheme
- Metadataset

New Identifiable Artefacts

- `GeoFeatureSetCode`
- `GeoGridCode`
- Metadata Provider

Removed Maintainable Artefacts

- Structure Set – replaced by Structure Map and the four item scheme
    maps
- Hierarchical Codelist – replaced by Hierarchy and Hierarchy
    Association
- Constraint – replaced by Data Constraint and Metadata Constraint

Changed Maintainable Artefacts

- Data Structure Definition – support for microdatasets and reference
    metadata linked to data
- Metadataflow – simplifies exchange of reference metadata, in
    particular those linked to structures
- Metadata Structure Definition – simplified model for reference
    metadata
- Codelist – support for codelist extension and geospatial specialised
    codelists (`GeographicCodelist`, `GeoGridCodelist`)
- VTL Mapping Scheme – VTL Concept Mapping Scheme removed to align the
    VTL / SDMX interface with the 3.0 model

New Component Representation Types

- `GeospatialInformation` – a string type where the value is an
    expression defining a set of geographical features using a
    purpose-designed syntax

## Version 3.1 - release March 2025

Changed Maintainable Artefacts 

- Availability Constraint no longer a Maintainable, inherits from Annotatable
- Categorisation – added a fixed version of 1.0
- Data Constraint
    - Advanced Release Calendar: removed 
    - Attachment: removed data source attachments
- Data Structure new property: Evolving Structure
- Dataflow new property: Dimension Constraint 
