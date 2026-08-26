# Specific Item Schemes

## Introduction

The structures that are an arrangement of objects into hierarchies or
lists based on characteristics, and which are maintained as a group
inherit from `ItemScheme`. These concrete classes are:

- `Codelist`
- `ConceptScheme`
- `CategoryScheme`
- `AgencyScheme`, `DataProviderScheme`, `MetadataProviderScheme`,
    `DataConsumerScheme`, `OrganisationUnitScheme`, which all inherit from the
    abstract class `OrganisationScheme`
- `ReportingTaxonomy`
- `TransformationScheme`
- `RulesetScheme`
- `UserDefinedOperatorScheme`
- `NamePersonalisationScheme`
- `CustomTypeScheme`
- `VtlMappingScheme`

Note that the VTL related schemes (the last 6 of the above list) are
detailed in a dedicated [section below](./14_Validation_and_Transformation_Language.md).

## Inheritance View

The inheritance and relationship views are shown together in each of the
diagrams in the specific sections below.

## `Codelist`

### Class Diagram

![](media/image42.png){ width="450" }
/// figure-caption | 16
Class diagram of the `Codelist`
///

### Explanation of the Diagram

#### Narrative

The `Codelist` inherits from the `ItemScheme` and therefore has the
following attributes:

- `id`
- `uri`
- `urn`
- `version`
- `validFrom`
- `validTo`
- `isExternalReference`
- `serviceURL`
- `structureURL`
- `isPartial`

The `Code` inherits from `Item` and has the following attributes:

- `id`
- `uri`
- `urn`

Both `Codelist` and `Code` have the association to `InternationalString` to
support a multi-lingual name, an optional multi-lingual description, and
an association to Annotation to support notes (not shown).

Through the inheritance the `Codelist` comprise one or more `Code`s, and the
`Code` itself can have one or more child `Code`s in the (inherited)
hierarchy association. Note that a child `Code` can have only one parent
`Code` in this association. A more complex Hierarchy, which allows
multiple parents is described later.

A partial `Codelist` (where `isPartial` is set to `true`) is identical to a
`Codelist` and contains the `Code` and associated names and descriptions,
just as in a normal `Codelist`. However, its content is a subset of the
full `Codelist`. The way this works is described in Section [The Item Scheme Pattern](./2_SDMX_Base_Package.md#the-item-scheme-pattern), 
paragraph "Explanation of the Diagram" - "Narrative".

#### Definitions

| Class    | Feature   | Description |
| :---     | :---      | :--- |
| `Codelist` | Inherits from: `ItemScheme` | A list from which some statistical concepts (coded concepts) take their values. |
| `Code`     | Inherits from: `Item` | A language independent set of letters, numbers or symbols that represent a concept whose meaning is described in a natural language. |
|          | hierarchy  | Associates the parent and the child codes. |
|          | extends    | Associates a `Codelist` with any `Codelist`s that it may extend. |

### Class Diagram – `Codelist` Extension

![](media/image43.png){ width="450" }
/// figure-caption
Class diagram for `Codelist` Extension
///

#### Narrative

A `Codelist` may extend other `Codelist`s via the `CodelistExtension` class.
The latter, via the sequence, indicates the order of precedence of the
extended `Codelist`s for conflict resolution of `Code`s. Besides that, the
prefix property is used to ensure uniqueness of inherited `Code`s in the
extending[^1] `Codelist` in case conflicting `Code`s must be included in the
latter. Each `CodelistExtension` association may include one
`Inclusive`Code`Selection` or one `Exclusive`Code`Selection`; those allow
including or excluding a specific selection of `Code`s from the extended
`Codelist`s.

[^1]: The `Codelist` that extends 0..* `Codelist`s is the 'extending' `Codelist`, 
    while the `Codelist`(s) that are inherited is/are the 'extended' `Codelist`(s).

The code selection classes may have `MemberValues` in order to specify the
subset of the `Code`s that should be included or excluded from the
extended `Codelist`. A `MemberValue` may have a value that corresponds to a
`Code`, including its children `Code`s (via the `cascadeValues` property), or
even include instances of the wildcard character ‘%’ in order to point
to a set of `Code`s with common parts in their identifiers.

#### Definitions

| Class                  | Feature      | Description                                                                                                   |
| :---                   | :---         | :---                                                                                                         |
| `CodelistExtension`    |              | The association between `Codelist`s that may extend other `Codelist`s.                                           |
|                        | `prefix`     | A prefix to be used for a `Codelist` used in an extension, in order to avoid `Code` Conflicts.                   |
|                        | `sequence`   | The order that will be used when extending a `Codelist`, for resolving `Code` conflicts. The latest `Codelist` used overrides any previous `Codelist`. |
| `Inclusive`Code`Selection` |             | The subset of `Code`s to be included when extending a `Codelist`.                                                |
| `Exclusive`Code`Selection` |             | The subset of `Code`s to be excluded when extending a `Codelist`.                                                |
| `MemberValue`            | Inherits from: `SelectionValue` | A collection of values based on `Code`s and their children.                                                    |
|                        | `cascadeValues` | A property to indicate if the child `Code`s of the selected `Code` shall be included in the selection. It is also possible to include children and exclude the `Code` by using the `excluderoot` value. |
|                        | `value`      | The value of the `Code` to include in the selection. It may include the `%` character as a wildcard.           |

### Class Diagram – Geospatial `Codelist`

The geospatial support is implemented via an extension of the normal
`Codelist`. This is illustrated in the following diagrams.

![](media/image44.png){ width="350" }
/// figure-caption
Inheritance for the `GeoCodelist`
///

![](media/image45.png)
/// figure-caption
Class diagram for Geospatial `Codelist`
///

#### Narrative

A `GeoCodelist` is a specialisation of `Codelist` that includes geospatial
information, by comprising a set of special `Code`s, i.e., `GeoRefCode`s.
A `GeoCodelist` may be implemented by any of the two following classes,
via the `geoType` property:

- `GeographicCodelist`
- `GeoGridCodelist`

The former, i.e., `GeographicCodelist`, comprises a set of
`GeoFeatureSet`Code`s`, by adding a value in the `Code` that follows a pattern
to represent a geo feature set.

The latter, i.e., `GeoGridCodelist`, comprises a set of `Grid`Code`s`, which
are related to the `gridDefinition` specified in the `GeoGridCodelist`.

#### Definitions

| Class                | Feature      | Description                                                                                                                                         |
| :------------------- | :----------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| `GeoCodelist`        | Abstract Class<br>Sub Classes: `GeographicCodelist`, `GeoGridCodelist` | The abstract class that represents a special type of `Codelist`, which includes geospatial information.                                               |
|                      | `geoType`      | The type of Geo `Codelist` that the `Codelist` will become.                                                                                             |
| `GeoRefCode`         | Abstract Class<br>Sub Classes: `GeoFeatureSetCode`, `GeoGridCode` | The abstract class that represents a special type of `Code`, which includes geospatial information.                                                   |
| `GeographicCodelist`   |              | A special `Codelist` that has been extended to add a geographical feature set to each of its items, typically including all types of administrative geographies. |
| `GeoGridCodelist`      |              | A code list that has defined a geographical grid composed of cells representing regular squared portions of the Earth.                              |
|                      | `gridDefinition` | Contains a regular expression string corresponding to the grid definition for the `GeoGrid` `Codelist`.                                                 |
| `GeoFeatureSetCode`    |              | A `Code` that has a geo feature set.                                                                                                                  |
|                      | value        | The geo feature set of the `Code`, which represents a set of points defining a feature in a format defined by a predefined pattern (see section 6).   |
| `GeoGridCode`          |              | A `Code` that represents a Geo Grid Cell belonging in a specific grid definition.                                                                     |
|                      | `geoCell`      | The value used to assign the `Code` to one cell in the grid.                                                                                          |

## `ValueList`

### Class Diagram

![](media/image46.png){ width="550" }
/// figure-caption
Class diagram of the `ValueList`
///

### Explanation of the Diagram

#### Narrative

A `ValueList` inherits from `EnumeratedList` (and hence the
`MaintenableArtefact`) and thus has the following attributes:

- `id`
- `uri`
- `urn`
- `version`
- `validFrom`
- `validTo`
- `isExternalReference`
- `registryURL`
- `structureURL`
- `repositoryURL`
- `ValueItem` inherits from `EnumeratedItem`, which adds an id, with relaxed constraints, to the former.

Through the inheritance from `NameableArtefact` the `ValueList` has the
association to `InternationalString` to support a multi-lingual name, an
optional multi-lingual description, and an association to Annotation to
support notes (not shown). Similarly, the `ValueItem`, inherits the
association to `InternationalString` and to the Annotation from the
`EnumeratedItem`.

The `ValueList` can have one or more `ValueItems`.

#### Definitions
| Class      | Feature         | Description                                                                                   |
| :---       | :---            | :---                                                                                          |
| `ValueList`  | Inherits from: `EnumeratedList` | A list from which some statistical concepts (enumerated concepts) take their values.        |
| `ValueItem`  | Inherits from: `EnumeratedItem` | A language independent set of letters, numbers or symbols that represent a concept whose meaning is described in a natural language. |

## Concept Scheme and Concepts

### Class Diagram - Inheritance

![](media/image47.png){ width="550" }
/// figure-caption
Class diagram of the Concept Scheme
///

### Explanation of the Diagram

The `ConceptScheme` inherits from the `ItemScheme` and therefore has the
following attributes:

- `id`
- `uri`
- `urn`
- `version`
- `validFrom`
- `validTo`
- `isExternalReference`
- `registryURL`
- `structureURL`
- `repositoryURL`
- `isPartial`

Concept inherits from Item and has the following attributes:

- id
- uri
- urn

Through the inheritance from `NameableArtefact` both `ConceptScheme` and
Concept have the association to `InternationalString` to support a
multi-lingual name, an optional multi-lingual description, and an
association to Annotation to support notes (not shown).

Through the inheritance from `ItemScheme` the `ConceptScheme` comprise one
or more Concepts, and the Concept itself can have one or more child
Concepts in the (inherited) hierarchy association. Note that a child
Concept can have only one parent Concept in this association.

A partial `ConceptScheme` (where `isPartial` is set to `true`) is identical
to a `ConceptScheme` and contains the Concept and associated names and
descriptions, just as in a normal `ConceptScheme`. However, its content is
a subset of the full `ConceptScheme`. The way this works is described in
Section [The Item Scheme Pattern](./2_SDMX_Base_Package.md#the-item-scheme-pattern), 
paragraph "Explanation of the Diagram" - "Narrative".

### Class Diagram - Relationship

![](media/image48.png)
/// figure-caption
Relationship class diagram of the Concept Scheme
///

### Explanation of the diagram

#### Narrative

The `ConceptScheme` can have one or more Concepts. A Concept can have zero
or more child Concepts, thus supporting a hierarchy of Concepts. Note
that a child Concept can have only one parent Concept in this
association. The purpose of the hierarchy is to relate concepts that
have a semantic relationship: for example, a Reporting\_Country and
Vis\_a\_Vis\_Country may both have Country as a parent concept, or a
CONTACT may have a PRIMARY\_CONTACT as a child concept. It is not the
purpose of such schemes to define reporting structures: these reporting
structures are defined in the `MetadataStructureDefinition`.

The Concept can be associated with a `coreRepresentation`. The
`coreRepresentation` is the specification of the format and value domain
of the Concept when used on a structure like a `DataStructureDefinition`
or a `MetadataStructureDefinition`, unless the specification of the
Representation is overridden in the relevant structure definition. In a
hierarchical `ConceptScheme` the Representation is inherited from the
parent Concept unless overridden at the level of the child Concept.

The Representation is documented in more detail in the section on the
SDMX Base.

The Concept may be related to a concept described in terms of the
ISO/IEC 11179 standard. The `ISOConceptReference` identifies this concept
and concept scheme in which it is contained.

#### Definitions

| Class               | Feature                | Description                                                                                                   |
| :------------------ | :--------------------- | :------------------------------------------------------------------------------------------------------------ |
| `ConceptScheme`     | Inherits from `ItemScheme` | The descriptive information for an arrangement or division of concepts into groups based on characteristics, which the objects have in common. |
| `Concept`           | Inherits from `Item`   | A concept is a unit of knowledge created by a unique combination of characteristics.                          |
|                     | `/hierarchy`           | Associates the parent and the child concept.                                                                  |
|                     | `coreRepresentation`   | Associates a `Representation`.                                                                                |
|                     | `+ISOConcept`          | Association to an ISO concept reference.                                                                      |
| `ISOConceptReference` |                       | The identity of an ISO concept definition.                                                                    |
|                     | `conceptAgency`        | The maintenance agency of the concept scheme containing the concept.                                          |
|                     | `conceptSchemeID`      | The identifier of the concept scheme.                                                                         |
|                     | `conceptID`            | The identifier of the concept.                                                                                |

## `Category` Scheme

### Context

This package defines the structure that supports the definition of and
relationships between categories in a category scheme. It is similar to
the package for concept scheme. An example of a category scheme is one
which categorises data – sometimes known as a subject matter domain
scheme or a data category scheme. Importantly, as will be seen later,
the individual nodes in the scheme (the “categories”) can be associated
to any set of `IdentiableArtefacts` in a Categorisation.

### Class diagram - Inheritance

![](media/image49.png){ width="350" }
/// figure-caption
Inheritance Class diagram of the `Category` Scheme
///

### Explanation of the Diagram

#### Narrative

The categories are modelled as a hierarchical `ItemScheme`. The
`CategoryScheme` inherits from the `ItemScheme` and has the following
attributes:

- `id`
- `uri`
- `urn`
- `version`
- `validFrom`
- `validTo`
- `isExternalReference`
- `structureURL`
- `serviceURL`
- `isPartial`

`Category` inherits from `Item` and has the following attributes:

- `id`
- `uri`
- `urn`

Both `CategoryScheme` and `Category` have the association to
`InternationalString` to support a multi-lingual name, an optional
multi-lingual description, and an association to Annotation to support
notes (not shown on the model).

Through the inheritance the `CategoryScheme` comprise one or more
`Category`s, and the `Category` itself can have one or more child `Category`
in the (inherited) hierarchy association. Note that a child `Category` can
have only one parent `Category` in this association.

A partial `CategoryScheme` (where `isPartial` is set to `true`) is identical
to a `CategoryScheme` and contains the `Category` and associated names and
descriptions, just as in a normal `CategoryScheme`. However, its content
is a subset of the full `CategoryScheme`. The way this works is described
in Section [The Item Scheme Pattern](./2_SDMX_Base_Package.md#the-item-scheme-pattern), 
paragraph "Explanation of the Diagram" - "Narrative".

### Class diagram - Relationship

![](media/image50.png)
/// figure-caption
Relationship Class diagram of the `Category` Scheme
///

The `CategoryScheme` can have one or more `Category`s. The `Category` is
Identifiable and has identity information. A `Category` can have zero or
more child `Category`s, thus supporting a hierarchy of `Category`s. Any
`IdentifiableArtefact` can be `+categorisedBy` a `Category`. This is achieved
by means of a Categorisation. Each Categorisation can associate one
`IdentifiableArtefact` with one `Category`. Multiple Categorisations can be
used to build a set of `IdentifiableArtefacts` that are `+categorisedBy` the
same `Category`. Note that there is no navigation (i.e. no embedded
reference) to the Categorisation from the `Category`. From an
implementation perspective this is necessary as Categorisation has no
effect on the versioning of either the `CategoryScheme` or the
`IdentifiableArtefact`.

#### Definitions

| Class             | Feature                | Description                                                                                                    |
| :---------------- | :--------------------- | :------------------------------------------------------------------------------------------------------------- |
| `CategoryScheme`  | Inherits from `ItemScheme` | The descriptive information for an arrangement or division of categories into groups based on characteristics, which the objects have in common. |
|                   | /items                 | Associates the categories.                                                                                     |
| `Category`        | Inherits from `Item`   | An item at any level within a classification, typically tabulation categories, sections, subsections, divisions, subdivisions, groups, subgroups, classes and subclasses. |
|                   | /hierarchy             | Associates the parent and the child `Category`.                                                                |
| `Categorisation`  | Inherits from `MaintainableArtefact` | Associates an identifiable artefact with a `Category`.                                                         |
|                   | `categorisedArtefact`  | Associates the identifiable artefact.                                                                          |
|                   | `categorisedBy`        | Associates the `Category`.                                                                                     |

## Organisation Scheme

### Class Diagram

![](media/image51.png)
/// figure-caption
The Organisation Scheme class diagram
///

### Explanation of the Diagram

#### Narrative

The `OrganisationScheme` is abstract. It contains `Organisation` which
is also abstract. The `Organisation` can have child `Organisation`.

The `OrganisationScheme` can be one of five types:

1. `AgencyScheme` – contains `Agency` which is restricted to a flat list of
    agencies (i.e., there is no hierarchy). Note that the SDMX system of
    (Maintenance) `Agency` can be hierarchic and this is explained in more
    detail in the SDMX Standards Section 6 “Technical Notes”.
2. `DataProviderScheme` – contains `DataProvider` which is restricted to a
    flat list of agencies (i.e., there is no hierarchy).
3. `MetadataProviderScheme` – contains `MetadataProvider` which is
    restricted to a flat list of agencies (i.e., there is no hierarchy).
4. `DataConsumerScheme` – contains `DataConsumer` which is restricted to a
    flat list of agencies (i.e., there is no hierarchy).
5. `OrganisationUnitScheme` – contains `OrganisationUnit` which does
    inherit the /hierarchy association from Organisation.

Reference metadata can be attached to the `Organisation` by means of the
metadata attachment mechanism. This mechanism is explained in the
Reference Metadata section of this document (see section 7). This means
that the model does not specify the specific reference metadata that can
be attached to a `DataProvider`, `MetadataProvider`, `DataConsumer`,
`OrganisationUnit` or `Agency`, except for limited Contact information.

A partial `OrganisationScheme` (where `isPartial` is set to `true`) is
identical to an `OrganisationScheme` and contains the `Organisation` and
associated names and descriptions, just as in a normal
`OrganisationScheme`. However, its content is a subset of the full
`OrganisationScheme`. The way this works is described in section Section [The Item Scheme Pattern](./2_SDMX_Base_Package.md#the-item-scheme-pattern), 
paragraph "Explanation of the Diagram" - "Narrative".

#### Definitions

| Class | Feature | Description |
| :--- | :--- | :--- |
| `OrganisationScheme` | Abstract Class. Inherits from `ItemScheme`. Subclasses are: `AgencyScheme`, `DataProviderScheme`, `MetadataProviderScheme`, `DataConsumerScheme`, `OrganisationUnitScheme` | A maintained collection of Organisations. |
|  | `/items` | Association to the Organisations in the scheme. |
| `Organisation` | Abstract Class. Inherits from `Item`. Subclasses are: `Agency`, `DataProvider`, `MetadataProvider`, `DataConsumer`, `OrganisationUnit` | An organisation is a unique framework of authority within which a person or persons act, or are designated to act, towards some purpose. |
|  | `+contact` | Association to the contact information. |
|  | `/hierarchy` | Association to child Organisations. |
| `Contact` |  | An instance of a role of an individual or an organization (or organization part or organization person) to whom an information item(s), a material object(s) and/or person(s) can be sent to or from in a specified context. |
|  | `name` | The designation of the contact person by a linguistic expression. |
|  | `organisationUnit` | The designation of the organisational structure by a linguistic expression, within which contact person works. |
|  | `responsibility` | The function of the contact person with respect to the organisation role for which this person is the contact. |
|  | `telephone` | The telephone number of the contact. |
|  | `fax` | The fax number of the contact. |
|  | `email` | The Internet e-mail address of the contact. |
|  | `X400` | The X400 address of the contact. |
|  | `uri` | The URL address of the contact. |
| `AgencyScheme` |  | A maintained collection of Maintenance Agencies. |
|  | `/items` | Association to the Maintenance Agency in the scheme. |
| `DataProviderScheme` |  | A maintained collection of Data Providers. |
|  | `/items` | Association to the Data Providers in the scheme. |
| `MetadataProviderScheme` |  | A maintained collection of Metadata Providers. |
|  | `/items` | Association to the Metadata Providers in the scheme. |
| `DataConsumerScheme` |  | A maintained collection of Data Consumers. |
|  | `/items` | Association to the Data Consumers in the scheme. |
| `OrganisationUnitScheme` |  | A maintained collection of Organisation Units. |
|  | `/items` | Association to the Organisation Units in the scheme. |
| `Agency` | Inherits from `Organisation` | Responsible agency for maintaining artefacts such as statistical classifications, glossaries, structural metadata such as Data and Metadata Structure Definitions, Concepts and `Code` lists. |
| `DataProvider` | Inherits from `Organisation` | An organisation that produces data. |
| `MetadataProvider` | Inherits from `Organisation` | An organisation that produces reference metadata. |
| `DataConsumer` | Inherits from `Organisation` | An organisation using data as input for further processing. |
| `OrganisationUnit` | Inherits from `Organisation` | A designation in the organisational structure. |
|  | `/hierarchy` | Association to child Organisation Units |

## Reporting Taxonomy

### Class Diagram

![](media/image52.png){ width="550" }
/// figure-caption
Class diagram of the Reporting Taxonomy
///

### Explanation of the Diagram

#### Narrative

In some data reporting environments, and in particular those in primary
reporting, a report may comprise a variety of heterogeneous data, each
described by a different `Structure`. Equally, a specific disseminated
or published report may also comprise a variety of heterogeneous data.
The definition of the set of linked sub reports is supported by the
`ReportingTaxonomy`.

The `ReportingTaxonomy` is a specialised form of `ItemScheme`. Each
`ReportingCategory` of the `ReportingTaxonomy` can link to one or more
`StructureUsage` which itself can be one of `Dataflow`, or `Metadataflow`,
and one or more `Structure`, which itself can be one of
`DataStructureDefinition` or `MetadataStructureDefinition`. It is expected
that within a specific `ReportingTaxonomy` each `Category` that is linked in
this way will be linked to the same class (e.g. all `Category` in the
scheme will link to a Dataflow). Note that a `ReportingCategory` can have
child `ReportingCategory` and in this way it is possible to define a
hierarchical `ReportingTaxonomy`. It is possible in this taxonomy that
some `ReportingCategory` are defined just to give a reporting structure.
For instance:

Section 1

1. linked to `Dataflow_1`
2. linked to `Dataflow_2`

Section 2

1. linked to `Dataflow_3`
2. linked to `Dataflow_4`

Here, the nodes of Section 1 and Section 2 would not be linked to
Dataflow but the other would be linked to a Dataflow (and hence the
`DataStructureDefinition`).

A partial `ReportingTaxonomy` (where `isPartial` is set to `true`) is
identical to a `ReportingTaxonomy` and contains the `ReportingCategory` and
associated names and descriptions, just as in a normal
`ReportingTaxonomy`. However, its content is a sub set of the full
`ReportingTaxonomy` The way this works is described in Section [The Item Scheme Pattern](./2_SDMX_Base_Package.md#the-item-scheme-pattern), 
paragraph "Explanation of the Diagram" - "Narrative".

#### Definitions

| Class | Feature | Description |
| :--- | :--- | :--- |
| `ReportingTaxonomy` | Inherits from `ItemScheme` | A scheme which defines the composition structure of a data report where each component can be described by an independent `Dataflow` or `Metadataflow`. |
|  | `/items` | Associates the Reporting `Category`. |
| `ReportingCategory` | Inherits from `Item` | A component that gives structure to the report and links to data and metadata. |
|  | `/hierarchy` | Associates child Reporting `Category`. |
|  | `+flow` | Association to the data and metadata flows that link to metadata about the provisioning and related data and metadata sets, and the structures that define them. |
|  | `+structure` | Association to the `DataStructureDefinition` and `MetadataStructureDefinition` which define the structural metadata describing the data and metadata that are contained at this part of the report. |
