# General Notes for Implementers

This section discusses a number of topics other than the exchange of
data sets in SDMX formats. Supported only in SDMX-ML (and some in
SDMX-JSON), these topics include the use of the reference metadata
mechanism in SDMX, the use of Structure Sets and Reporting Taxonomies,
the use of Processes, a discussion of time and data-typing, and the
conventional mechanisms within the SDMX-ML Structure message regarding
versioning and referencing.

## Representations

This section does not go into great detail on these topics but provides
a useful overview of these features to assist implementors in further
use of the parts of the specification which are relevant to them.

There are several different representations in SDMX-ML, taken from XML
Schemas and common programming languages. The table below describes the
various representations, which are found in SDMX-ML, and their
equivalents.

| SDMX-ML Data Type | XML Schema Data Type | .NET Framework Type | Java Data Type |
| :--- | :--- | :--- | :--- |
| `String` | `xsd:string` | `System.String` | `java.lang.String` |
| `Big Integer` | `xsd:integer` | `System.Decimal` | `java.math.BigInteger` |
| `Integer` | `xsd:int` | `System.Int32` | `int` |
| `Long` | `xsd:long` | `System.Int64` | `long` |
| `Short` | `xsd:short` | `System.Int16` | `short` |
| `Decimal` | `xsd:decimal` | `System.Decimal` | `java.math.BigDecimal` |
| `Float` | `xsd:float` | `System.Single` | `float` |
| `Double` | `xsd:double` | `System.Double` | `double` |
| `Boolean` | `xsd:boolean` | `System.Boolean` | `boolean` |
| `URI` | `xsd:anyURI` | `System.Uri` | `Java.net.URI` or `java.lang.String` |
| `DateTime` | `xsd:dateTime` | `System.DateTime` | `javax.xml.datatype.XMLGregorianCalendar` |
| `Time` | `xsd:time` | `System.DateTime` | `javax.xml.datatype.XMLGregorianCalendar` |
| `GregorianYear` | `xsd:gYear` | `System.DateTime` | `javax.xml.datatype.XMLGregorianCalendar` |
| `GregorianMonth` | `xsd:gYearMonth` | `System.DateTime` | `javax.xml.datatype.XMLGregorianCalendar` |
| `GregorianDay` | `xsd:date` | `System.DateTime` | `javax.xml.datatype.XMLGregorianCalendar` |
| `Day`, `MonthDay`, `Month` | `xsd:g*` | `System.DateTime` | `javax.xml.datatype.XMLGregorianCalendar` |
| `Duration` | `xsd:duration` | `System.TimeSpan` | `javax.xml.datatype.Duration` |

There are also a number of SDMX-ML data types which do not have these
direct correspondences, often because they are composite representations
or restrictions of a broader data type. For most of these, there are
simple types which can be referenced from the SDMX schemas, for others a
derived simple type will be necessary:

- `AlphaNumeric` (`common:AlphaNumericType`, string which only
    allows `A-z` and `0-9`)
- `Alpha` (`common:AlphaType`, string which only allows `A-z`)
- `Numeric` (`common:NumericType`, string which only allows 0-9,
    but is not numeric so that is can having leading zeros)
- `Count` (`xs:integer`, a sequence with an interval of "1")
- `InclusiveValueRange` (`xs:decimal` with the `minValue` and
    `maxValue` facets supplying the bounds)
- `ExclusiveValueRange` (`xs:decimal` with the `minValue` and
    `maxValue` facets supplying the bounds)
- `Incremental` (`xs:decimal` with a specified `interval`; the
    interval is typically enforced outside of the XML validation)
- `TimeRange` (`common:TimeRangeType`, `startDateTime` +
    `Duration`)
- `ObservationalTimePeriod` (`common:ObservationalTimePeriodType`,
    a union of `StandardTimePeriod` and `TimeRange`).
- `StandardTimePeriod` (`common:StandardTimePeriodType`, a union
    of `BasicTimePeriod` and `ReportingTimePeriod`).
- `BasicTimePeriod` (`common:BasicTimePeriodType`, a union of
    `GregorianTimePeriod` and `DateTime`)
- `GregorianTimePeriod` (`common:GregorianTimePeriodType`, a union
    of `GregorianYear`, `GregorianMonth`, and `GregorianDay`)
- `ReportingTimePeriod` (`common:ReportingTimePeriodType`, a union
    of `ReportingYear`, `ReportingSemester`, `ReportingTrimester`,
    `ReportingQuarter`, `ReportingMonth`, `ReportingWeek`, and
    `ReportingDay`).
- `ReportingYear` (`common:ReportingYearType`)
- `ReportingSemester` (`common:ReportingSemesterType`)
- `ReportingTrimester` (`common:ReportingTrimesterType`)
- `ReportingQuarter` (`common:ReportingQuarterType`)
- `ReportingMonth` (`common:ReportingMonthType`)
- `ReportingWeek` (`common:ReportingWeekType`)
- `ReportingDay` (`common:ReportingDayType`)
- `XHTML` (`common:StructuredText`, allows for multi-lingual text
    content that has `XHTML` markup)
- `KeyValues` (`common:DataKeyType`)
- `IdentifiableReference` (types for each IdentifiableObject)
- `GeospatialInformation` (a geo feature set, according to the
    pattern in section 7.2)

Data types also have a set of facets:

- `isSequence = true | false` (indicates a sequentially increasing
    value)
- `minLength = positive integer` (# of characters/digits)
- `maxLength = positive integer` (# of characters/digits)
- `startValue = decimal` (for numeric sequence)
- `endValue = decimal` (for numeric sequence)
- `interval = decimal` (for numeric sequence)
- `timeInterval = duration`
- `startTime = BasicTimePeriod` (for time range)
- `endTime = BasicTimePeriod` (for time range)
- `minValue = decimal` (for numeric range)
- `maxValue = decimal` (for numeric range)
- `decimal = Integer` (# of digits to right of decimal point)
- `pattern =` (a regular expression, as per W3C XML Schema)
- `isMultiLingual = boolean` (for specifying text can occur in more
    than one language)

Note that code lists may also have textual representations assigned to
them, in addition to their enumeration of codes.

### Data Types

XML and JSON schemas support a variety of data types that, although
rich, are not mapped one-to-one in all cases. This section provides an
explanation of the mapping performed in SDMX 3.0, between such cases.

For identifiers, text fields and Codes there are no restriction from
either side, since a generic type (e.g., that of string) accompanied by
the proper regular expression works equally well for both XML and JSON.

For example, for the id type, this is the XML schema definition:

```xml
<xs:simpleType name="IDType">
  <xs:restriction base="NestedIDType">
    <xs:pattern value="[A-Za-z0-9_@$\-]+"/>
  </xs:restriction>
</xs:simpleType>
```

Where the `NestedIDType` is also a restriction of `string`.

The above looks like this, in JSON schema:

```json
"idType": {
    "type": "string",
    "pattern": "^\[A-Za-z0-9\_@$-\]+$"
}
```

There are also cases, though, that data types cannot be mapped like
above. One such case is the array data type, which was introduced in
SDMX 3.0 as a new representation. In JSON schema an array is already
natively foreseen, while in the XML schema, this has to be defined as a
complex type, with an SDMX specific definition (i.e., specific
element/attribute names for SDMX). Beyond that, the minimum and/or
maximum number of items within an array is possible in both cases.

Further to the above, the mapping between the non-native data types is
presented in the table below:

| SDMX Facet | XML Schema | JSON schema "pattern"[^1] for "string" type |
| :--- | :--- | :--- |
| `GregorianYear` | `xsd:gYear` | `"^-?([1-9][0-9]{3,}\|0[0-9]{3})(Z\|(\+\|-)((0[0-9]\|1[0-3]):[0-5][0-9]\|14:00))?$"` |
| `GregorianMonth` | `xsd:gYearMonth` | `"^-?([1-9][0-9]{3,}\|0[0-9]{3})-(0[1-9]\|1[0-2])(Z\|(\+\|-)((0[0-9]\|1[0-3]):[0-5][0-9]\|14:00))?$"` |
| `GregorianDay` | `xsd:date` | `"^-?([1-9][0-9]{3,}\|0[0-9]{3})-(0[1-9]\|1[0-2])-(0[1-9]\|[12][0-9]\|3[01])(Z\|(\+\|-)((0[0-9]\|1[0-3]):[0-5][0-9]\|14:00))?$"` |
| `Day` | `xsd:gDay` | `"^---(0[1-9]\|[12][0-9]\|3[01])(Z\|(\+\|-)((0[0-9]\|1[0-3]):[0-5][0-9]\|14:00))?$"` |
| `MonthDay` | `xsd:gMonthDay` | `"^--(0[1-9]\|1[0-2])-(0[1-9]\|[12][0-9]\|3[01])(Z\|(\+\|-)((0[0-9]\|1[0-3]):[0-5][0-9]\|14:00))?$"` |
| `Month` | `xsd:Month` | `"^--(0[1-9]\|1[0-2])(Z\|(\+\|-)((0[0-9]\|1[0-3]):[0-5][0-9]\|14:00))?$"` |
| `Duration` | `xsd:duration` | `"^-?P[0-9]+Y?([0-9]+M)?([0-9]+D)?(T([0-9]+H)?([0-9]+M)?([0-9]+(\.[0-9]+)?S)?)?$"` |

[^1]: Regular expressions, as specified in [W3C XML Schema Definition](https://www.w3.org/TR/xmlschema11-2/).

## Time and Time Format

This section does not go into great detail on these topics but provides
a useful overview of these features to assist implementors in further
use of the parts of the specification which are relevant to them.

### Introduction

First, it is important to recognize that most observation times are a
period. SDMX specifies precisely how Time is handled.

The representation of time is broken into a hierarchical collection of
representations. A data structure definition can use of any of the
representations in the hierarchy as the representation of time. This
allows for the time dimension of a particular data structure definition
allow for only a subset of the default representation.

The hierarchy of time formats is as follows (**bold** indicates a
category which is made up of multiple formats, *italic* indicates a
distinct format):

- **Observational Time Period**
    - **Standard Time Period**
        - **Basic Time Period**
            - **Gregorian Time Period**
            - *Date Time*
        - **Reporting Time Period**
    - *Time Range*

The details of these time period categories and of the distinct formats
which make them up are detailed in the sections to follow.

### Observational Time Period

This is the superset of all time representations in SDMX. This allows
for time to be expressed as any of the allowable formats.

### Standard Time Period

This is the superset of any predefined time period or a distinct point
in time. A time period consists of a distinct start and end point. If
the start and end of a period are expressed as date instead of a
complete date time, then it is implied that the start of the period is
the beginning of the start day (i.e. 00:00:00) and the end of the period
is the end of the end day (i.e. 23:59:59).

### Gregorian Time Period

A Gregorian time period is always represented by a Gregorian year,
year-month, or day. These are all based on ISO 8601 dates. The
representation in SDMX-ML messages and the period covered by each of the
Gregorian time periods are as follows:

- **Gregorian Year:**
    - Representation: `xs:gYear (YYYY)`
    - Period: the start of January 1 to the end of December 31
- **Gregorian Year Month**:
    - Representation: `xs:gYearMonth (YYYY-MM)`
    - Period: the start of the first day of the month to end of the last day of the month
- **Gregorian Day**:
    - Representation: `xs:date (YYYY-MM-DD)`
    - Period: the start of the day (00:00:00) to the end of the day (23:59:59)

### Date Time

This is used to unambiguously state that a date-time represents an
observation at a single point in time. Therefore, if one wants to use
SDMX for data which is measured at a distinct point in time rather than
being reported over a period, the date-time representation can be used.

 Representation: `xs:dateTime YYYY-MM-DDThh:mm:ss`[^2]

[^2]: The seconds can be reported fractionally

### Standard Reporting Period

Standard reporting periods are periods of time in relation to a
reporting year. Each of these standard reporting periods has a duration
(based on the ISO 8601 definition) associated with it. The general
format of a reporting period is as follows:

 `[REPORTING_YEAR]-[PERIOD_INDICATOR][PERIOD_VALUE]`

Where:

- `REPORTING_YEAR` represents the reporting year as four digits (`YYYY`)
- `PERIOD_INDICATOR` identifies the type of period which determines the duration of the period
- `PERIOD_VALUE` indicates the actual period within the year

The following section details each of the standard reporting periods
defined in SDMX:

- **Reporting Year**:
    - Period Indicator: `A`
    - Period Duration: `P1Y` (one year)
    - Limit per year: 1
    - Representation: `common:ReportingYearType` (`YYYY-A1`, e.g. `2000-A1`)
- **Reporting Semester:**
    - Period Indicator: `S`
    - Period Duration: `P6M` (six months)
    - Limit per year: 2
    - Representation: `common:ReportingSemesterType` (`YYYY-Ss`, e.g. `2000-S2`)
- **Reporting Trimester:**
    - Period Indicator: `T`
    - Period Duration: `P4M` (four months)
    - Limit per year: 3
    - Representation: `common:ReportingTrimesterType` (`YYYY-Tt`, e.g. `2000-T3`)
- **Reporting Quarter:**
    - Period Indicator: `Q`
    - Period Duration: `P3M` (three months)
    - Limit per year: 4
    - Representation: `common:ReportingQuarterType` (`YYYY-Qq`, e.g. `2000-Q4`)
- **Reporting Month**:
    - Period Indicator: `M`
    - Period Duration: `P1M` (one month)
    - Limit per year: 1
    - Representation: `common:ReportingMonthType` (`YYYY-Mmm`, e.g. `2000-M12`)
    - Notes: The reporting month is always represented as two digits, therefore 1-9 are 0 padded (e.g. 01). This allows the values to be sorted chronologically using textual sorting methods.
- **Reporting Week**:
    - Period Indicator: `W`
    - Period Duration: `P7D` (seven days)
    - Limit per year: 53
    - Representation: `common:ReportingWeekType` (`YYYY-Www`, e.g. `2000-W53`)
    - Notes: There are either 52 or 53 weeks in a reporting year. This is based on the ISO 8601 definition of a week (Monday - Saturday), where the first week of a reporting year is defined as the week with the first Thursday on or after the reporting year start day.[^3] The reporting week is always represented as two digits, therefore 1-9 are 0 padded (e.g. 01). This allows the values to be sorted chronologically using textual sorting methods.
- **Reporting Day**:
    - Period Indicator: `D`
    - Period Duration: `P1D` (one day)
    - Limit per year: 366
    - Representation: `common:ReportingDayType` (`YYYY-Dddd`, e.g. `2000-D366`)
    - Notes: There are either 365 or 366 days in a reporting year, depending on whether the reporting year includes leap day (February 29). The reporting day is always represented as three digits, therefore 1-99 are 0 padded (e.g. 001). This allows the values to be sorted chronologically using textual sorting methods.

[^3]: 
    ISO 8601 defines alternative definitions for the first week, all of
    which produce equivalent results. Any of these definitions could be
    substituted so long as they are in relation to the reporting year start
    day.

The meaning of a reporting year is always based on the start day of the
year and requires that the reporting year is expressed as the year at
the start of the period. This start day is always the same for a
reporting year, and is expressed as a day and a month (e.g. July 1).
Therefore, the reporting year 2000 with a start day of July 1 begins on
July 1, 2000.

A specialized attribute (reporting year start day) exists for the
purpose of communicating the reporting year start day. This attribute
has a fixed identifier (`REPORTING_YEAR_START_DAY`) and a fixed
representation (`xs:gMonthDay`) so that it can always be easily identified
and processed in a data message. Although this attribute exists in
specialized sub-class, it functions the same as any other attribute
outside of its identification and representation. It must takes its
identity from a concept and state its relationship with other components
of the data structure definition. The ability to state this relationship
allows this reporting year start day attribute to exist at the
appropriate levels of a data message. In the absence of this attribute,
the reporting year start date is assumed to be January 1; therefore if
the reporting year coincides with the calendar year, this Attribute is
not necessary.

Since the duration and the reporting year start day are known for any
reporting period, it is possible to relate any reporting period to a
distinct calendar period. The actual Gregorian calendar period covered
by the reporting period can be computed as follows (based on the
standard format of
`[REPROTING_YEAR]-[PERIOD_INDICATOR][PERIOD_VALUE]` and the
reporting year start day as `[REPORTING_YEAR_START_DAY]`):

1. Determine `[REPORTING_YEAR_BASE]`:

    Combine `[REPORTING_YEAR]` of the reporting period value (`YYYY`) with
    `[REPORTING_YEAR_START_DAY]` (MM-DD) to get a date (`YYYY-MM-DD`).
    This is the `[REPORTING_YEAR_START_DATE]`

   1. If the `[PERIOD_INDICATOR]` is W:

      1. If `[REPORTING_YEAR_START_DATE]` is a Friday, Saturday, or
           Sunday:

           Add[^4] (`P3D`, `P2D`, or `P1D` respectively) to the
           `[REPORTING_YEAR_START_DATE]`. The result is the
           `[REPORTING_YEAR_BASE]`.

      2. **If `[REPORTING_YEAR_START_DATE]` is a Monday, Tuesday,
          Wednesday, or Thursday:

              Add[^4] (`P0D`, `-P1D`, `-P2D`, or `-P3D` respectively) to the
              `[REPORTING_YEAR_START_DATE]`. The result is the
              `[REPORTING_YEAR_BASE]`.

   2. Else:

    The `[REPORTING_YEAR_START_DATE]` is the `[REPORTING_YEAR_BASE]`.

2. Determine `[PERIOD_DURATION]`:

    1. If the `[PERIOD_INDICATOR]` is A, the `[PERIOD_DURATION]` is
        P1Y.
    2. If the `[PERIOD_INDICATOR]` is S, the `[PERIOD_DURATION]` is
        P6M.
    3. If the `[PERIOD_INDICATOR]` is T, the `[PERIOD_DURATION]` is
        P4M.
    4. If the `[PERIOD_INDICATOR]` is Q, the `[PERIOD_DURATION]` is
        P3M.
    5. If the `[PERIOD_INDICATOR]` is M, the `[PERIOD_DURATION]` is
        P1M.
    6. If the `[PERIOD_INDICATOR]` is W, the `[PERIOD_DURATION]` is
        P7D.
    7. If the `[PERIOD_INDICATOR]` is D, the `[PERIOD_DURATION]` is
        P1D.

3. Determine `[PERIOD_START]`:

    Subtract one from the `[PERIOD_VALUE]` and multiply this by the
    `[PERIOD_DURATION]`. Add[^4] this to the `[REPORTING_YEAR_BASE]`.
    The result is the `[PERIOD_START]`.

4. Determine the `[PERIOD_END]`:

    Multiply the `[PERIOD_VALUE]` by the `[PERIOD_DURATION]`.
    Add[^4] this to the `[REPORTING_YEAR_BASE]` add[^4]
    -P1D. The result is the `[PERIOD_END]`.

[^4]:
    The rules for adding durations to a date time are described in the W3C XML Schema specification.
    See [w3.org](http://www.w3.org/TR/xmlschema-2/#adding-durations-to-dateTimes) for further details.

For all of these ranges, the bounds include the beginning of the
`[PERIOD_START]` (i.e. 00:00:00) and the end of the `[PERIOD_END]`
(i.e. 23:59:59).

#### Examples:

??? example "2010-Q2, REPORTING_YEAR_START_DAY = --07-01 (July 1)"

    1. `[REPORTING_YEAR_START_DATE] = 2010-07-01`

        case b) `[REPORTING_YEAR_BASE] = 2010-07-01`

    2. `[PERIOD_DURATION] = P3M`
    3. `(2-1) * P3M = P3M`

        `2010-07-01 + P3M = 2010-10-01`

        `[PERIOD_START] = 2010-10-01`

    4. `2 * P3M = P6M`

        `2010-07-01 + P6M = 2010-13-01 = 2011-01-01`

        `2011-01-01 + -P1D = 2010-12-31`
          
        `[PERIOD_END] = 2010-12-31`

        The actual calendar range covered by `2010-Q2` (assuming the reporting
        year begins July 1) is `2010-10-01T00:00:00`/`2010-12-31T23:59:59`

??? example "2011-W36, REPORTING\_YEAR\_START\_DAY = --07-01 (July 1)"

    1. `[REPORTING_YEAR_START_DATE] = 2010-07-01`

        case a) `2011-07-01 = Friday`

        `2011-07-01 + P3D = 2011-07-04`

        `[REPORTING_YEAR_BASE] = 2011-07-04`

    2. `[PERIOD_DURATION] = P7D`
    3. `(36-1) \* P7D = P245D`

        `2011-07-04 + P245D = 2012-03-05`

        `[PERIOD_START] = 2012-03-05`

    4. `36 * P7D = P252D`

        `2011-07-04 + P252D =2012-03-12`

        `2012-03-12 + -P1D = 2012-03-11`

        `[PERIOD_END] = 2012-03-11`

        The actual calendar range covered by `2011-W36` (assuming the reporting year begins July 1) is `2012-03-05T00:00:00`/`2012-03-11T23:59:59`

### Distinct Range

In the case that the reporting period does not fit into one of the
prescribe periods above, a distinct time range can be used. The value of
these ranges is based on the ISO 8601 time interval format of
start/duration. Start can be expressed as either an ISO 8601 date or a
date-time, and duration is expressed as an ISO 8601 duration. However,
the duration can only be positive.

### Time Format

In version 2.0 of SDMX there is a recommendation to use the time format
attribute to gives additional information on the way time is represented
in the message. Following an appraisal of its usefulness this is no
longer required. However, it is still possible, if required , to include
the time format attribute in SDMX-ML.

| Code | Format |
| :--- | :--- |
| OTP | Observational Time Period: Superset of all SDMX time formats(Gregorian Time Period, Reporting Time Period, and Time Range) |
| STP | Standard Time Period: Superset of Gregorian and Reporting TimePeriods |
| GTP | Superset of all Gregorian Time Periods and date-time |
| RTP | Superset of all Reporting Time Periods |
| TR | Time Range: Start time and duration(`YYYY-MM-DD(Thh:mm:ss)?/<duration>`) |
| GY | Gregorian Year (`YYYY`) |
| GTM | Gregorian Year Month (`YYYY-MM`) |
| GD | Gregorian Day (`YYYY-MM-DD`) |
| DT | Distinct Point: date-time (`YYYY-MM-DDThh:mm:ss`) |
| RY | Reporting Year (`YYYY-A1`) |
| RS | Reporting Semester (`YYYY-Ss`) |
| RT | Reporting Trimester (`YYYY-Tt`) |
| RQ | Reporting Quarter (`YYYY-Qq`) |
| RM | Reporting Month (`YYYY-Mmm`) |
| RW | Reporting Week (`YYYY-Www`) |
| RD | Reporting Day (`YYYY-Dddd`) |

### Time Zones

In alignment with ISO 8601, SDMX allows the specification of a time zone
on all time periods and on the reporting year start day. If a time zone
is provided on a reporting year start day, then the same time zone (or
none) should be reported for each reporting time period. If the
reporting year start day and the reporting period time zone differ, the
time zone of the reporting period will take precedence. Examples of each
format with time zones are as follows (time zone indicated in bold):

- Time Range (start date): 2006-06-05**-05:00**/P5D
- Time Range (start date-time): 2006-06-05T00:00:00**-05:00**/P5D
- Gregorian Year: 2006**-05:00**
- Gregorian Month: 2006-06**-05:00**
- Gregorian Day: 2006-06-05**-05:00**
- Distinct Point: 2006-06-05T00:00:00**-05:00**
- Reporting Year: 2006-A1**-05:00**
- Reporting Semester: 2006-S2**-05:00**
- Reporting Trimester: 2006-T2**-05:00**
- Reporting Quarter: 2006-Q3**-05:00**
- Reporting Month: 2006-M06**-05:00**
- Reporting Week: 2006-W23**-05:00**
- Reporting Day: 2006-D156**-05:00**
- Reporting Year Start Day: --07-01**-05:00**

According to ISO 8601, a date without a time-zone is considered "local
time". SDMX assumes that local time is that of the sender of the
message. In this version of SDMX, an optional field is added to the
sender definition in the header for specifying a time zone. This field
has a default value of 'Z' (UTC). This determination of local time
applies for all dates in a message.

### Representing Time Spans Elsewhere

It has been possible since SDMX 2.0 for a Component to specify a
representation of a time span. Depending on the format of the data
message, this resulted in either an element with 2 XML attributes for
holding the start time and the duration or two separate XML attributes
based on the underlying Component identifier. For example, if
`REF_PERIOD` were given a representation of time span, then in the
Compact data format, it would be represented by two XML attributes;
`REF_PERIODStartTime` (holding the start) and `REF_PERIOD` (holding the
duration). If a new simple type is introduced in the SDMX schemas that
can hold ISO 8601 time intervals, then this will no longer be necessary.
What was represented as this:

```xml
<Series REF_PERIODStartTime="2000-01-01T00:00:00" REF_PERIOD="P2M">
```

can now be represented with this:

```xml
<Series REF_PERIOD="2000-01-01T00:00:00/P2M">
```

### Notes on Formats

There is no ambiguity in these formats so that for any given value of
time, the category of the period (and thus the intended time period
range) is always clear. It should also be noted that by utilizing the
ISO 8601 format, and a format loosely based on it for the report
periods, the values of time can easily be sorted chronologically without
additional parsing.

### Effect on Time Ranges

All SDMX-ML data messages are capable of functioning in a manner similar
to SDMX-EDI if the Dimension at the observation level is time: the time
period for the first observation can be stated and the rest of the
observations can omit the time value as it can be derived from the start
time and the frequency. Since the frequency can be determined based on
the actual format of the time value for everything but distinct points
in time and time ranges, this makes is even simpler to process as the
interval between time ranges is known directly from the time value.

### Time in Query Messages

When querying for time values, the value of a time parameter can be
provided as any of the Observational Time Period formats and must be
paired with an operator. This section will detail how systems processing
query messages should interpret these parameters.

Fundamental to processing a time value parameter in a query message is
understanding that all time periods should be handled as a distinct
range of time. Since the time parameter in the query is paired with an
operator, this also effectively represents a distinct range of time.
Therefore, a system processing the query must simply match the data
where the time period for requested parameter is encompassed by the time
period resulting from value of the query parameter. The following table
details how the operators should be interpreted for any time period
provided as a parameter.

| Operator | Rule |
| :--- | :--- |
| Greater Than | Any data after the last moment of the period |
| Less Than | Any data before the first moment of the period |
| Greater Than or Equal To | Any data on or after the first moment of the period |
| Less Than or Equal To | Any data on or before the last moment of the period |
| Equal To | Any data which falls on or after the first moment of the period and before or on the last moment of the period |

Reporting Time Periods as query parameters are handled like this: any
data within the bounds of the reporting period for the year is matched,
regardless of the actual start day of the reporting year. In addition,
data reported against a normal calendar period is matched if it falls
within the bounds of the time parameter based on a reporting year start
day of January 1. When determining whether another reporting period
falls within the bounds of a report period query parameter, one will
have to take into account the actual time period to compare weeks and
days to higher order report periods. This will be demonstrated in the
examples to follow.

??? example "Gregorian Period"

    Query Parameter: Greater than 2010

    Literal Interpretation: Any data where the start period occurs after
    2010-12-31T23:59:59.

    Example Matches:

    - 2011 or later
    - 2011-01 or later
    - 2011-01-01 or later
    - 2011-01-01/P\[Any Duration\] or any later start date
    - 2011-\[Any reporting period\] (any reporting year start day)
    - 2010-S2 (reporting year start day --07-01 or later)
    - 2010-T3 (reporting year start day --07-01 or later)
    - 2010-Q3 or later (reporting year start day --07-01 or later)
    - 2010-M07 or later (reporting year start day --07-01 or later)
    - 2010-W28 or later (reporting year start day --07-01 or later)
    - 2010-D185 or later (reporting year start day --07-01 or later)

??? example "Reporting Period"

    Query Parameter: Greater than or equal to 2010-Q3

    Literal Interpretation: Any data with a reporting period where the
    start period is on or after the start period of 2010-Q3 for the same
    reporting year start day, or and data where the start period is on or
    after 2010-07-01.

    Example Matches:

    - 2011 or later
    - 2010-07 or later
    - 2010-07-01 or later
    - 2010-07-01/P\[Any Duration\] or any later start date
    - 2011-\[Any reporting period\] (any reporting year start day)
    - 2010-S2 (any reporting year start day)
    - 2010-T3 (any reporting year start day)
    - 2010-Q3 or later (any reporting year start day)
    - 2010-M07 or later (any reporting year start day)
    - 2010-W27 or later \[reporting year start day --01-01\][^5]
    - 2010-D182 or later (reporting year start day --01-01)
    - 2010-W28 or later \[reporting year start day --07-01\][^6]
    - 2010-D185 or later (reporting year start day --07-01)

[^5]:
    2010-Q3 (with a reporting year start day of --01-01) starts on 2010-07-01. This is day 4 of week 26, therefore the first week matched is week 27.
[^6]: 
    2010-Q3 (with a reporting year start day of --07-01) starts on 2011-01-01. This is day 6 of week 27, therefore the first week matched is week 28.


## Versioning

Versioning operates at the level of versionable and maintainable objects
in the SDMX information model. Within the SDMX Structure and MetadataSet
messages, there is a well-defined pattern for artefact versioning and
referencing. The artefact identifiers are qualified by their version
numbers – that is, an object with an Agency of "A", and ID of "X" and a
version of "1.0.0" is a different object than one with an Agency of "A",
an ID of "X", and a version of "1.1.0".

As of SDMX 3.0, the versioning rules are extended to allow for truly
versioned artefacts through the implementation of the rules of the
well-known practice called [Semantic Versioning](http://semver.org),
in addition to the legacy non-restrictive versioning scheme. In
addition, the `"isFinal"` property is removed from `MaintainableArtefact`.
According to the legacy versioning, any artefact defined without a
version is equivalent to following the legacy versioning, thus having
version ‘1.0’.

### Non-versioned artefacts

Indeed, some use cases do not need or are incompatible with versioning
for some or all their structural artefacts, such as the Agency, Data
Providers, Metadata Providers and Data Consumer Schemes. These artefacts
follow the legacy versioning, with a fixed version set to ‘1.0’.

Many existing organisation’s data management systems work with
version-less structures and apply ad-hoc structural metadata governance
processes. The new non-versioned artefacts will allow supporting those
numerous situations, where organisations do not manage version numbers.

### Semantically versioned artefacts

Since the purpose of SDMX versioning is to allow communicating the
structural artefact changes to data exchange partners and connected
systems, SDMX 3.0 offers Semantic Versioning (aka SemVer) with a clear
and unambiguous syntax to all semantically versioned SDMX 3.0 structural
artefacts. Semantic versioning will thus better respond to situations
where the SDMX standard itself is the only structural contract between
data providers and data consumers and where changes in structures can
only be communicated through the version number increases.

The semantic version number consists of four parts: `MAJOR`, `MINOR`, `PATCH`
and `EXTENSION`, the first three parts being separated by a dot (`.`), the
last two parts being separated by a hyphen (`-`):
`MAJOR.MINOR.PATCH-EXTENSION`. All versions are ordered.

The detailed rules for semantic versioning are listed in chapter 14 in
the annex for “Semantic Versioning”. In short, they define:

Given a version number `MAJOR.MINOR.PATCH` (without `EXTENSION`), when
making changes to that semantically versioned SDMX artefact, then one
must increment the:

1. `MAJOR` version when backwards incompatible artefact changes are made,
2. `MINOR` version when artefact elements are added in a backwards
    compatible manner, or
3. `PATCH` version when backwards compatible artefact property changes
    are made.

When incrementing a version part, the right-hand side parts are 0-ed
(reset to ‘0’).

Extensions can be added, changed or dropped.

Given an extended version number `MAJOR.MINOR.PATCH-EXTENSION`, when
making changes to that versioned artefact, then one is not required to
increment the version if those changes are within the allowed scope of
the version increment from the previous version (if that existed);
otherwise, the above version increment rules apply. `EXTENSION`s can be
used e.g., for drafting or a pre-release.

Semantically versioned SDMX artefacts will thus be safe to use. Specific
version patterns allow them to become either immutable, i.e., the
maintainer commits to never change their content, or changeable only
within a well-defined scope. If any further change is required, a new
version must be created first. Furthermore, the impact of the further
change is communicated using a clear version increment. The built-in
version extension facility allows for eased drafting of new SDMX
artefact versions.

The production versions of identifiable artefacts are assumed stable,
i.e., they do not have an `EXTENSION`. This is because once in production,
an artefact cannot change in any way, or it must change the version. For
cases where an artefact is not static, like during the drafting, the
version must indicate this by including an `EXTENSION`. Draft artefacts
should not be used outside of a specific system designed to accommodate
them. For most purposes, all artefacts should become stable before being
used in production.

### Legacy-versioned artefacts

Organisations wishing to keep a maximum of backwards compatibility with
existing implementations can continue using the previous 2-digit
convention for version numbers (`MAJOR.MINOR`) as in the past, such as
'2.3', but without the ‘isFinal’ property. The new SDMX 3.0 standard
does not add any strict rules or guarantees about changes in those
artefacts, since the legacy versioning rules were rather loose and
non-binding, including the meaning of the ‘isFinal’ property, and their
implementations were varying.

In order to make artefacts immutable or changes truly predictable, a
move to the new semantic versioning syntax is required.

### Dependency management and references

New flexible dependency specifications with wildcarding allow for easier
data model maintenance and enhancements for semantically versioned SDMX
artefacts. This allows implementing a smart referencing mechanism,
whereby an artefact may reference:

- a fixed version of another artefact
- the **latest available** version of another artefact
- the **latest backward compatible** version of another artefact, or the **latest backward and forward** **compatible** version of another artefact.

References not representing a strict artefact dependency, such as the
target artefacts defined in a `MetadataProvisionAgreement` allow for
linking to **all currently available** versions of another artefact.
Another illustrative case for such loose referencing is that of
Constraints and flows. A Constraint may reference many Dataflows or
Metadataflows, the addition of more references to flow objects does not
version the Constraint. This is because the Constraints are not
properties of the flows – they merely make references to them.

Semantically versioned artefacts must only reference other semantically
versioned artefacts, which may include extended versions. Non-versioned
and legacy-versioned artefacts can reference any other non-versioned or
versioned (whether semantic or legacy) artefacts. The scope of wildcards
in references adapts correspondingly.

The mechanism named "early binding" refers to a dependency on a stable
versioned artefact – everything with a stable versioned identity is a
known quantity and will not change. The "late binding" mechanism is
based on a wildcarded reference, and it resolves that reference and
determines the currently related artefact at runtime.

One area which is much impacted by this versioning scheme is the ability
to reference external objects. With the many dependencies within the
various structural objects in SDMX, it is useful to have a scheme for
external referencing. This is done at the level of maintainable objects
(DSDs, Codelists, Concept Schemes, etc.) In an SDMX Structure Message,
whenever an `"isExternalReference"` attribute is set to true, then the
application must resolve the address provided in the associated `"uri"`
attribute and use the SDMX Structure Message stored at that location for
the full definition of the object in question. Alternately, if a
registry `"urn"` attribute has been provided, the registry can be used to
supply the full details of the object.

The detailed rules for dependency management and references are listed
in chapter 14 in the annex for “Semantic Versioning”.

In order to allow resolving the described new forms of dependencies, the
SDMX 3.0 Rest API supports retrievals legacy-versioned, wildcarded and
extended artefact versions:

- Artefact queries for a **specific** version (X.Y, X.Y.Z or
    X.Y.Z-EXT).
- Artefact queries for **latest available** semantic versions within
    the wildcard scope (X+.Y.Z, X.Y+.Z or X.Y.Z+).
- Queries for **non-versioned** artefacts.
- Artefact queries for **all available** semantic versions within the
    wildcard scope  
    (\*, X.\* or X.Y.\*), where only the first form is required for
    resolving wildcarded loose references.

The combination of wildcarded queries with a specific version extension
is not permitted.

Full details can be found in the SDMX RESTful web services
specification.

## Structural Metadata Querying Best Practices

When querying for structural metadata, the ability to state how
references should be resolved is quite powerful. However, this mechanism
is not always necessary and can create an undue burden on the systems
processing the queries if it is not used properly.

Any structural metadata object which contains a reference to an object
can be queried based on that reference. For example, a categorisation
references both a category and the object is it categorising. As this is
the case, one can query for categorisations which categorise a
particular object or which categorise against a particular category or
category scheme. This mechanism should be used when the referenced
object is known.

When the referenced object is not known, then the reference resolution
mechanism could be used. For example, suppose one wanted to find all
category schemes and the related categorisations for a given maintenance
agency. In this case, one could query for the category scheme by the
maintenance agency and specify that parent and sibling references should
be resolved. This would result in the categorisations which reference
the categories in the matched schemes to be returned, as well as the
object which they categorise.
