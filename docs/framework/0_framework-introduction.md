# Introduction

The Statistical Data and Metadata Exchange (SDMX) initiative
(<https://www.sdmx.org>) sets standards that can facilitate the exchange
of statistical data and metadata using modern information technology.

The SDMX Technical Specifications are organised into several discrete
sections.

The following are published on the SDMX website
(<https://www.sdmx.org>):

- **Section 1 -- Framework for SDMX Technical Standards** --- this
  document providing an introduction to the technical standards.
- **Section 2 -- SDMX Information Model** --- the SDMX information model is
    a standardised object model for modelling statistical domains centring
    on the structure of their data and metadata sets, the coding schemes
    used for classification, and the rules for controlling the exchange of
    data and metadata between organisations. This document provides a UML
    specification with supporting narrative.
- **Section 5 -- SDMX Registry Specification** --- an SDMX 'registry' acts
    as a repository for structural metadata and provisioning information,
    and a registry of data and metadata sources. This document sets out the
    specification.
- **Section 6 -- SDMX Technical Notes** --- detailed technical guidance
    for implementors of the SDMX standard.

The following are published on the [GitHub repository](https://github.com/sdmx-twg) of the SDMX
Technical Working Group (TWG):

- **sdmx-twg/sdmx-rest -- REST API** ---
    Technical specifications for the SDMX RESTful web services application
    programming interfaces (API).
- **sdmx-twg/sdmx-ml -- SDMX-ML** ---
    Technical specifications for the XML transmission format including XSD
    schemas, documentation and samples for data, structure and reference
    metadata messages.
- **sdmx-twg/sdmx-json -- SDMX-JSON** ---
    Technical specifications for the JSON transmission format including
    documentation, schemas and samples for data, structure and reference
    metadata messages.
- **sdmx-twg/sdmx-csv -- SDMX-CSV** ---
    Technical specifications for the SDMX-CSV transmission format for
    'comma-separated values' (CSV) data and reference metadata.

The following sections are obsolete:

- **Section 3 -- SDMX-ML** --- replaced by the sdmx-twg/sdmx-ml GitHub repository
- **Section 4 -- SDMX-EDI**
- **Section 7 -- API** --- replaced by the sdmx-twg/sdmx-rest GitHub repository
- **VTL** ---
    In July 2020 the SDMX 2.1 specifications were revised to add support for
    the Validation and Transformation Language (VTL). For 3.0, the VTL
    specification has been updated to align with changes to the information
    model and other modifications to the Standard such as the introduction
    of Semantic Versioning for the versioning of structural metadata
    artefacts. Section 2 (Information Model) sets out details of the
    'Transformation and Expressions' package for defining and managing VTL
    2.0 programs and Section 6 (Technical Notes) provides detailed guidance
    on implementing and using VTL with SDMX.