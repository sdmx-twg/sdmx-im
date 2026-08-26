# Geospatial information support

SDMX recognizes that statistics refers to units or facts sited in places
or areas that may be referenced to geodesic coordinates. This section
presents the technical specifications to "geo-reference" those objects
and facts in SDMX, by establishing ways to make relations to geographic
features over the Earth using a defined coordinates system.

SDMX can support three different ways for referencing geospatial data:

1. **Indirect Reference to Geospatial Information.** Including a
    link to an external file containing the geospatial information. This
    is the only backwards compatible approach. Since this representation
    of geospatial information is not included inside the data message,
    the main use case would be connecting dissemination systems for
    making use of external tools, like GIS software.
2. **Geographic Coordinates.** Including the coordinates of a
    specific geospatial feature as a set of coordinates. This is
    suitable for any statistical information that needs to be
    georeferenced especially for the exchange of microdata.
3. **A Geographic Codelist.** Includes a type of Codelist, listing
    predefined geographies that are represented by geospatial
    information. These geographies could be administrative (including
    administrative boundaries or enumeration areas), lines, points, or
    gridded geographies. Regardless, the geospatial information used to
    represent the geography would contain both dimensions and/or
    attributes; therefore, representing an advantage for the data
    modellers as it provides a clear way to identify those dimensions
    developing a "Geospatial" role.

## Indirect Reference to Geospatial Information

This option provides a way to include external references to geospatial
information through a file containing it. The external content may be
geographical or thematic maps with different levels of precision. All
the processing of geospatial data is made through external applications
that can interpret the information in different formats.

The reference to the external files containing geospatial information is
made using some recommended SDMX Attributes, with the following content:

- `GEO_INFO_TEXT`. A description of the kind of information being
    referenced.
- `GEO_INFO_URL`. A URL which points to the resource containing
    the referred geospatial information. The resource might be a file
    with static geodesic information or a web service providing dynamic
    construction of geometries.
- `GEO_INFO_TYPE`. Coded information describing a standard format
    of the file that contains the geospatial information. The format
    types are taken from the list of 
    [Format descriptions for Geospatial Data managed by the US Library of the Congress](https://www.loc.gov/preservation/digital/formats/fdd/gis_fdd.shtml).
    Allowed types in SDMX are listed in the **Geographical Formats**
    code list (`CL_GEO_FORMATS`). Examples of the codes contained in
    the document are:

    | Code          | Description              |
    |---------------|------------------------------|
    | GML           | Geography Markup Language    |
    | GeoTIFF       | GeoTIFF                      |
    | KML_2_2       | KML Version 2.2             |
    | GEOJSON_1_1   | GeoJSON Version 1.1         |

Depending on the intended use, these attributes may be attached at the
dataflow level, the series level or the observation level.

The indirect reference to geospatial information in SDMX is recommended
to be used for dissemination purposes, where the statistical information
is complemented by geographical representations of places or regions.

## Geographic Coordinates

This option to represent geospatial information in SDMX provides an
efficient way for including geographic information with different levels
of granularity, due to its flexibility. Geospatial information is
represented using the `GeospatialInformation` type, as defined in the data
types of the SDMX Information Model. A `"GEO_FEATURE_SET"` role should
be assigned to any Component of this type.

The `GeospatialInformation` data type can be assigned to a `Dimension`,
`DataAttribute`, `MetadataAttribute` or a `Measure` with the
`"GEO_FEATURE_SET"` role assigned; it can be included in a dataset or
metadataset.

Any Component used for representing a Geographical Feature Set, i.e.,
used to describe geographical characteristics, must have a
`“GEO_FEATURE_SET”` role. Its Representation would be of
`textType="GeospatialInformation"`. The `GeospatialInformation` type is not
intended to replace standard geospatial information formats, but instead
provide a simple way to describe precise geographical characteristics in
SDMX data sets agnostic of any particular geospatial software product or
use case.

The `GeospatialInformation` type should be used to describe geographical
features like points (e.g., locations of places, landmarks, buildings,
etc.), lines (e.g., rivers, roads, streets, etc.), or areas (e.g.,
geographical regions, countries, islands, land lots, etc.). A mix of
different features is possible too, e.g., combining polygons and
geographical points to describe a country and the location of its
capital.

The components that conform to the structure of the
`GeospatialInformation` type are:

- `X_COORDINATE`: The horizontal (longitude) value of a pair of
    coordinates expressed in the Coordinate Reference System (CRS),
    mandatory.
- `Y_COORDINATE`: The vertical value (latitude) of a pair of
    coordinates expressed in the CRS units, mandatory.
- `ALT`: The height (altitude) from the reference surface is expressed
    in meters, optional.
- `CRS`: The code of the Coordinate Reference System is used to
    reference the coordinates in the flow, optional.

    The code of the CRS will be as it appears in the
    [EPSG Geodetic Parameter Registry](http://www.epsg-registry.org/)
    maintained by the
    International Association of Oil and Gas Producers. If this element is
    omitted, by default, the CRS will be the World Geodetic System 1984
    (WGS 84, EPSG:4326).

- `PRECISION`: Precision of the coordinates, expressing the possible
    deviation in meters from the exact geodesic point, optional.

    This component is only allowed if the CRS is specified too. If
    omitted, it will be interpreted as limited it to the expected
    measurement accuracy (e. g. a standard GPS has an accuracy of ~ 10m).

- `GEO_DESCRIPTION`: Text for additional information about the place,
    geographical feature, or set of geographical features, optional.

Geographical features (`GEO_FEATURES`) are collections of geographical
features intended to be used to represent geographical areas like
countries, regions, etc., or objects, like water bodies (e. g. rivers,
lakes, oceans, etc.), roads (streets, highways, etc.), hospitals,
schools, and the like. They are represented in the following way:

```text
(GEO_FEATURE, GEO_FEATURE): GEO_DESCRIPTION
```

- `GEO_FEATURE` represents a set of points defining a feature following
    the ISO/IEC 13249-3:2016 standard to conform Well-known Text (WKT)
    for the representation of geometries in a format defined in the
    following way:

    ```text
    GEOMETRY_TYPE (GEOMETRY_REP)
    ```

- `GEOMETRY_TYPE`: A string with a closed vocabulary defining the type
    of the geometry that represents a geographical component of the
    `GEO_FEATURES` collection, mandatory.

    Three types are allowed:

    1. `Point`, a specific geodesic point, like the centroid of a city or
        a hospital. It is represented with the string `“POINT”`
    2. `Line`, a feature defining a line like a road, a river, or
        similar. It is represented with the string `“LINESTRING”`
    3. `Area`, a polygon defining a closed area. It is represented with
        the string `“POLYGON”`

    If the `GEOMETRY_REP` is going to be including the height (`ALT`)
    component, a `“Z”` must be added after the string qualifying the
    `GEOMETRY_TYPE`. In this way, we will have: `“POINT Z”`, `“LINESTRING Z”`
    and `“POLYGON Z”`
    
    Other feature types (e.g. Triangular irregular networks, “TIN”) are
    not supported yet directly, except grids that are detailed in 7.3.

- `GEOMETRY_REP`: Representation of each of the types The way to
    represent each `GEO_FEATURE_TYPE` will be:
    - A point (`POINT`): `“COORDINATES”`
    - A line (`LINESTRING`): `“COORDINATES, COORDINATES, …”`
    - An area (`POLYGON`): `“(COORDINATES, COORDINATES, …), (COORDINATES, COORDINATES, …)”`

Where:

- `COORDINATES`: Represents an individual set of coordinates composed by
    the `X_COORDINATE` (`X`), `Y_COORDINATE` (`Y`), and `ALT` (`Z`) in the
    following way `“X Y Z”` or `“X Y”` defining a single point of the
    polygon. Altitude is to be reported in meters.

In an expanded way, `GEO_FEATURE` may be represented in the following
ways:


```xml
POINT (X_COORDINATE Y_COORDINATE): GEO_DESCRIPTION
POINT Z (X_COORDINATE Y_COORDINATE ALT): GEO_DESCRIPTION
LINESTRING (X_COORDINATE Y_COORDINATE, X_COORDINATE Y_COORDINATE, …): GEO_DESCRIPTION
LINESTRING Z (X_COORDINATE Y_COORDINATE ALT, X_COORDINATE Y_COORDINATE ALT, …): GEO_DESCRIPTION
POLYGON  ((X_COORDINATE Y_COORDINATE, X_COORDINATE Y_COORDINATE, …), (X_COORDINATE Y_COORDINATE, X_COORDINATE Y_COORDINATE, …), …): GEO_DESCRIPTION
POLYGON Z ((X_COORDINATE Y_COORDINATE ALT, X_COORDINATE Y_COORDINATE ALT, …), (X_COORDINATE Y_COORDINATE ALT, X_COORDINATE Y_COORDINATE ALT, …), …): GEO_DESCRIPTION
```

An example of how `GEO_FEATURES` may be represented in an expanded way
would be:

```xml
(POLYGON Z (
    (X_COORDINATE Y_COORDINATE ALT, X_COORDINATE Y_COORDINATE ALT, …), 
    (X_COORDINATE Y_COORDINATE ALT, X_COORDINATE Y_COORDINATE ALT, …), …),
 POLYGON Z (
    (X_COORDINATE Y_COORDINATE ALT, X_COORDINATE Y_COORDINATE ALT, …), 
    (X_COORDINATE Y_COORDINATE ALT, X_COORDINATE Y_COORDINATE ALT, …), …), 
 POLYGON Z (
    (X_COORDINATE Y_COORDINATE ALT, X_COORDINATE Y_COORDINATE ALT, …), 
    (X_COORDINATE Y_COORDINATE ALT, X_COORDINATE Y_COORDINATE ALT, …), …), …): 
    GEO_DESCRIPTION
```

Accordingly to this logic, an example of an expanded expression
representing a value of the `GeospatialInformation` may be the following:

```xml
“CRS, PRECISION: {(POLYGON Z ((X_COORDINATE Y_COORDINATE ALT,
X_COORDINATE Y_COORDINATE ALT, …), (X_COORDINATE Y_COORDINATE ALT,
X_COORDINATE Y_COORDINATE ALT, …), …), POLYGON Z ((X_COORDINATE
Y_COORDINATE ALT, X_COORDINATE Y_COORDINATE ALT, …), (X_COORDINATE
Y_COORDINATE ALT, X_COORDINATE Y_COORDINATE ALT, …), …), POLYGON Z
((X_COORDINATE Y_COORDINATE ALT, X_COORDINATE Y_COORDINATE ALT, …),
(X_COORDINATE Y_COORDINATE ALT, X_COORDINATE Y_COORDINATE ALT, …),
…), …): GEO _DESCRIPTION}, {(POLYGON Z ((X_COORDINATE Y_COORDINATE
ALT, X_COORDINATE Y_COORDINATE ALT, …), (X_COORDINATE Y_COORDINATE
ALT, X_COORDINATE Y_COORDINATE ALT, …), …), POLYGON Z ((X_COORDINATE
Y_COORDINATE ALT, X_COORDINATE Y_COORDINATE ALT, …), (X_COORDINATE
Y_COORDINATE ALT, X_COORDINATE Y_COORDINATE ALT, …), …), POLYGON Z
((X_COORDINATE Y_COORDINATE ALT, X_COORDINATE Y_COORDINATE ALT, …),
(X_COORDINATE Y_COORDINATE ALT, X_COORDINATE Y_COORDINATE ALT, …),
…), …): GEO _DESCRIPTION}, …: GEO_DESCRIPTION”
```

Validation rules must be added to the XML Schema to ensure the integrity
of the specification according to the proposed syntax.

## A Geographic Codelist

Geography is represented by geospatial information. Within SDMX,
geospatial information is conceptually represented by the
`"GEO_FEATURE_SET"` role/specification. This approach uses a specialized
form of SDMX Codelist, named `"GeoCodelist"`, which is a Codelist
containing the Geography used to demarcate the geographic extent. This
is implemented in two ways:

1. `Geographic`. It is a regular codelist that has been extended to add a
    geographical feature set to each of its items, typically, this would
    include all types of administrative geographies;
2. `Grid`. As a codelist that has defined a geographical grid composed of
    cells representing regular squared portions of the Earth.

A `GeoCodelist` is a Codelist as defined in the SDMX Information Model
that has the `GeoType` property added. `GeoType` can take one of two values
`"Geographic"` or `"GeoGrid"`.

`"Geographic"` corresponds to the first way to implement a `GeoCodelist`.
When the `GeoCodelist` includes a `GeoType="Geographic"` property, a
`GeoFeatureSet` property is added to each of the items in the code list to
implement a Geographic `GeoCodelist`.

On the other hand, when `GeoType="GeoGrid"` it is defining a gridded
`GeoCodelist`, and it is necessary to add a grid definition to the
Codelist identifier using the `gridDefinition` property. The components
needed to define a geographical grid are the following:

- `CRS`: The code of the Coordinate Reference System is used to
    reference the coordinates in the flow, optional. The code of the CRS
    will be as it appears in the 
    [EPSG Geodetic Parameter Registry](http://www.epsg-registry.org/) 
    maintained by the International
    Association of Oil and Gas Producers. If this component is omitted,
    by default the CRS will be the World Geodetic System 1984 (WGS 84,
    EPSG:4326).
- `REFERENCE_CORNER`: A code composed of two characters to define the
    position of the coordinates that will be used as a starting
    reference to locate the cells. The possible values of this code can
    be `UL` (Upper Left), `UR` (Upper Right), `LL` (Lower Left), or `LR` (Lower
    Right). If this component is omitted the value `LL` (Lower Left) will
    be taken by default. This element is optional.
- `REFERENCE_COORDINATES`: Represents the starting point to reference
    the cells of the grid, accordingly to the `CRS` and the
    `REFERENCE_CORNER`. It is represented by an individual set of
    coordinates composed by the `X_COORDINATE` (`X`) and `Y_COORDINATE` (`Y`)
    in the following way `"X,Y"`. This element is mandatory if `GEO_STD` is
    omitted.
- `CELL_WIDTH`: The size in meters of a horizontal side of the cells in
    the grid. This element is mandatory if `GEO_STD` is omitted.
- `CELL_HEIGHT`: The size in meters of a vertical side of the cells in
    the grid. This element is mandatory if `GEO_STD` is omitted .
- `GEO_STD`: A restricted text value expressing that the cells in the
    grid will provide information about matching codes existing in
    another reference system that establishes a mechanism to define the
    grid. This element is optional.

    Accepted values for this component are included in the Geographical
    Grids Codelist (`CL_GEO_GRIDS`). Examples contained in the mentioned
    document are:

    | Value | Description |
    | :--- | :--- |
    | `GEOHASH` | GeoHash |
    | `GEOREF` | World Geographic Reference System |
    | `MGRS` | Military Grid Reference System |
    | `OLC` | Open Location Code / Plus Code |
    | `QTH` | Maidenhead Locator System /QTH Locator / IAURU Locator |
    | `W3W` | What3words™ |
    | `WOEID` | Where On Earth Identifier |

The `GRID_DEFINITION` element will contain a regular expression string
corresponding to the following format:

```text
"CRS: REFERENCE_CORNER; REFERENCE_COORDINATES; CELL_WIDTH,
CELL_HEIGHT: GEO_STD"
```

In an expanded way we would have:

```text
"CRS:REFERENCE_CORNER; X_COORDINATE, Y_COORDINATE; CELL_WIDTH,
CELL_HEIGHT: GEO_STD"
```

If the grid will be fully adhering to a standard declared in the
GEO_STD, the definition of each code in the code list will be optional.
In other case, each item in the code list must be assigned to one cell
in the grid, which is made by adding the GEO_CELL element to each item
of the code list that will contain a regular expression string composed
of the following components:

- `GEO_COL`: The number of the column in the grid starting by zero.
- `GEO_ROW`: The number of the row in the grid starting by zero.
- `GEO_TAG`: An optional text to include additional information to
    the cell.
- `GEO_CELL` will have values with the following format: `"GEO_COL, GEO_ROW: GEO_TAG"`

When using a gridded `GeoCodelist` we may use the `GEO_TAG` to integrate
the cells in the grid to the codes used by other standard defined grids.
As an example, `GEO_TAG` can take the values of the Open Location Codes,
GeoHash, etc. If this is done, the `GEO_STD` component must have been
added to the definition of the grid. If the `GEO_STD` is omitted, the
`GEO_TAG` contents will be taken just as free text.
