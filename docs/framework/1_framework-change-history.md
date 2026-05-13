# Change History

The 2.0 version of this standard represented a significant increase in
scope, and also provided more complete support in those areas covered in
the version 1.0 specification. Version 2.0 of this standard is
backward-compatible with version 1.0, so that existing implementations
can be easily migrated to conformance with version 2.0.

The 2.1 version of this standard represents a set of changes resulting
from several years of implementation experience with the 2.0 standard.
The changes do not represent a major increase in scope or functionality,
but do correct some bugs, and add functionalities in some cases. Major
changes in SDMX-ML include a much stronger alignment of the XML Schemas
with the Information Model, to emphasize inheritance and object-oriented
features, and increased precision and flexibility in the attachment of
metadata reports to specific objects in the SDMX Information Model.

The 3.0 version incorporates new features, improvements and changes
arising from the collective knowledge gained from a decade of operating
experience with the 2.1 standard. In pursuit of modernisation and
simplification, features considered obsolete have been deprecated -- in
particular the EDI transmission format, the lesser-used XML data
messages and the SOAP web services API. Many areas remain backwardly
compatible with 2.1, but there are some breaking changes where the
information model has been redesigned to better support practical use
case. Structure mapping and reference metadata are examples. The
opportunity has been taken to revise the RESTful web services API which
is also not backwardly compatible, but benefits from a rationalisation
and better organisations of resources, and a much richer data query URL
syntax.

The 3.1 version provides supports for data models to increase dimensionality
over time without impacting existing data collections. The Data Constraint
model was adjusted to separate concerns of data reporting and data dissemination.

## Major Changes from 1.0 to 2.0

- **Reference Metadata:** In addition to describing and specifying
    data structures and formats (along with related structural
    metadata), the version 2.0 specification also provides for the
    exchange of metadata which is distinct from the structural metadata
    in the 1.0 version. This category includes "reference" metadata
    (regarding data quality, methodology, and similar types -- it can be
    configured by the user to include whatever concepts require
    reporting); metadata related to data provisioning (release calendar
    information, description of the data and metadata provided, etc.);
    and metadata relevant to the exchange of categorization schemes.
- **SDMX Registry:** Provision is made in the 2.0 standard for
    standard communication with registry services, to support a
    data-sharing model of statistical exchange. These services include
    registration of data and metadata, querying of registered data and
    metadata, and subscription/notification.
- **Structural Metadata:** The support for exchange of statistical
    data and related structural metadata has been expanded. Some support
    is provided for qualitative data; data cube structures are
    described; hierarchical code lists are supported; relationships
    between data structures can be expressed, providing support for
    extensibility of data structures; and the description of functional
    dependencies within cubes are supported.

## Major Changes from 2.0 to 2.1

- **Web-Services-Oriented Changes:** Several organizations have been
    implementing web services applications using SDMX, and these
    implementations have resulted in several changes to the
    specifications. Because the nature of SDMX web services could not be
    anticipated at the time of the original drafting of the
    specifications, the web services guidelines have been completely
    re-developed.
- **Presentational Changes:** Much work has gone into using various
    technologies for the visualization of SDMX data and metadata, and
    some changes have been proposed as a result, to better leverage this
    graphical visualization. These changes are largely to leverage the
    Cross-domain Concepts of the Content Oriented Guidelines.
- **Consistency Issues:** There have been some areas where the draft
    specifications were inconsistent in minor ways, and these have been
    addressed.
- **Clarifications in Documentation:** In some cases, it has been
    identified that the documentation of specific fields within the
    standard needed clarification and elaboration, and these issues have
    been addressed.
- **Optimization for XML Technologies:** Implementation has shown that
    it is possible to better organize the XML schemas for use within
    common technology development tools which work with XML. These
    changes are primarily focused on leveraging the object-oriented
    features of W3C XML Schema to allow for easier processing of SDMX
    data and metadata.
- **Consistency between the SDMX-ML and the SDMX Information Model:**
    Certain aspects of the XML schemas and UML model have been more
    closely aligned, to allow for easier comprehension of the SDMX
    model.
- **Technical Bugs:** Some minor technical bugs have been identified
    in the registry interfaces and elsewhere. These bugs have been
    addressed.
- **Support for Non-Time-Series Data in the Generic Format:** One area
    which has been extended is the ability to express non-time-series
    data as part of the generic data message.
- **Simplification of the data structure definition - specific message types:**
    Both time series (version 2.0 Compact) and non-time series
    data sets (version 2.0 Cross Sectional) use the same underlying
    structure for a structure-specific formatted message, which is
    specific to the Data Structure Definition of the data set.
- **Simplification and better support for the metadata structure:**
    New use cases have been reported and these are now supported by a
    re-modelled metadata structure definition.
- **Support for partial item schemes such as a code list:** The
    concept of a partial (sub-set) item scheme such as a partial code
    list for use in exchange scenarios has been introduced**.**

## Major Changes from 2.1 to 3.0

SDMX version 3.0 introduces new features, improvements and changes to
the Standard in the following key areas:

### Information Model

- Simplification and improvement of the reference metadata model
- Support for microdata
- Support for geospatial data
- Support for code list extension and discriminated union of code
    lists
- Improvements to structure mapping
- Improvements to code hierarchies for data discovery
- Improvements to constraints

### Versioning of Structural Metadata Artefacts

- Adoption of the three-number semantic versioning standard for
    structural metadata artefacts (<https://semver.org>)

### REST Web Services Application Programming Interface (API)*

- Change to a single 'structure' resource for structure queries
    simplifying the REST API specification by reducing the number of
    resources to five
- Improvements to data queries
- Improvements to reference metadata queries
- Support for structural metadata maintenance using HTTP PUT, POST and
    DELETE verbs

### SOAP Web Services API

- The SOAP web services API has been deprecated with version 3.0
    standardising on REST

### XML, JSON, CSV and EDI Transmission formats

- The SDMX-ML, SDMX-JSON and SDMX-CSV specifications have been
    extended and modified where needed to support the new features and
    changes such as reference metadata and microdata
- Obsolete SDMX-ML data message variants including Generic, Compact,
    Utility and Cross-sectional have been deprecated standardising on
    Structure Specific Data as the sole XML format for data exchange
- The SDMX-EDI transmission format for structures and data has been
    deprecated
- The organisation of structures into 'collections' in SDMX-ML and
    SDMX-JSON structure messages has been flattened and simplified
- The option to reference structures in SDMX-ML and SDMX-JSON messages
    using Agency, ID and Version has been deprecated with URN now
    exclusively used for all non-local referencing purpose

Several of the changes are 'breaking' meaning that, in specific cases,
the version 3.0 specification is not backwardly compatible with earlier
versions of the Standard.

The principle breaking changes are:

- REST API -- The REST API is not backwardly compatible due to
    modifications to the URLs and query parameters resulting in breaking
    changes in four of the five main resources.
- SOAP API -- Deprecation of the SOAP API means that existing systems
    designed to use SOAP will not work with version 3.0 registries.
- SDMX-ML -- SDMX 2.1 and earlier structure, data and metadata XML
    messages are not valid in version 3.0. Specifically: legacy data
    messages including Generic, Compact and Utility are no longer
    supported. The remaining Structure Specific data message has been
    changed to support new features such as reporting of reference
    metadata as part of the dataset, Structure messages have a number of
    breaking changes, principally modification to the information model,
    removal of the agency-version-id option for referencing artefacts
    and changes to the way the structures are organised into
    'collections' within the message.
- SDMX-JSON -- SDMX 2.1 structure, data and metadata JSON messages are
    not valid in version 3.0. The data message has been changed to
    support the improved REST data queries, in particular the ability to
    retrieve in one operation data from multiple datasets with
    potentially different Data Structure Definitions. Breaking changes
    similar to those for the SDMX-ML transmission format have been made
    to the structure message.
- SDMX-CSV -- The CSV data and reference metadata messages are not
    backwardly compatible with those under version 2.1 due to changes to
    the structure of the messages needed to support new features such as
    the improved REST API data queries.
- SDMX-EDI -- Deprecation of the EDI transmission format means that
    existing systems designed to send or receive structures or data in
    EDI will not work with version 3.0 registries.
- Information Model -- Several structures have been changed in the
    version 3.0 model and three removed. For these reasons the version
    3.0 model is not directly compatible with version 2.1 or earlier,
    although conversion of specific artefacts is possible under some
    circumstances. Loss of information during the conversion process
    however means that in cases like structure mapping, the conversion
    is not reversible i.e. it is not possible to recreate the 2.1
    structure once it has been converted to the 3.0 model.

The SDMX 3.0 Major Changes document provides more information including
an analysis of the breaking changes.

## Major Changes from 3.0 to 3.1

Information Model

- Addition of Dimension Constraint property to a Dataflow
- Addition of evolving structure property to a Data Structure Definition
- Remove version property on Categorisation
- Simplification of Constraints
    - Removal of Advanced Release Calendar
    - Removal of Role, Data Constraints only restrict data that can be reported
    - Restrict constraint targets to Identifiable structures (not URLs)
    - Addition of Availability Constraint to define actual data

Documentation

- Registering Reference Metadata removed from documentation, to align with XML
  Registration object which is unable to reference a Metadata Provision, and
  REST API which is unable to query for registered reference metadata sources.
