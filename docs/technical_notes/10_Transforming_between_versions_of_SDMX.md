# Transforming between versions of SDMX

## Scope

The scope of this section is to define both best practices and mandatory
behaviour for specific aspects of transformation between different
versions of SDMX.

## Compatibility and new DSD features

The following table provides an overview of the backwards compatibility
between SDMX 3.0 and 2.1.

| SDMX 3.0 feature       | SDMX 2.1 compatibility                     | Comments                                                                 |
| :-------------------------- | :--------------------------------------------- | :--------------------------------------------------------------------------- |
| Multiple Measures           | Create a Measure Dimension<br>Or<br>Model Measures as Attributes | For Measure Dimensions, all Concepts must reside in the same Concept Scheme |
| Arrays for values           | Cannot be supported                            | Arrays are always reported in a verbose format, even if one value is reported |
| Measure Relationship        | Can be ignored, as it does not affect dataset format |                                                                             |
| Metadata Attributes         | Can be created as Data Attributes              | Not for extended facets                                                     |
| Multilingual Components     | Cannot be supported                            |                                                                             |
| No Measure                  | Can only be emulated by ignoring the Primary Measure value |                                                                             |
| Use extended Codelist       | A new Codelist with all Codes must be created  |                                                                             |
| Sentinel values             | Cannot be supported in the DSD                | Rules may be supported outside the DSD, in bilateral agreements             |

The following table illustrates forward compatibility issues from SDMX
2.1 to 3.0.

| SDMX 2.1 feature | SDMX 3.0 compatibility | Comments |
| :-------------------- | :------------------------- | :----------- |
| Measure Dimension     | Create a Dimension with role `‘MEASURE’`<br>Or<br>Create multiple Measures from the Measure Dimension Concept Scheme | If the dataset has to resemble that of SDMX 2.1 Structure Specific, then the first option must be used |
| Primary Measure       | Create one Measure with role `‘PRIMARY’`; use `id=”OBS_VALUE”` | |
