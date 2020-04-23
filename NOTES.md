# SDMX Standard technical documentation
## Choosen documentation system
It was decided that from SDMX 3.0, the TWG would rely on [Sphynx](http://sphinx-doc.org/) to generete and keep up to date the SDMX standard's documentation. 

Each repository under `sdmx-twg` in GitHub that will participate in this documentation generation will follow the same rules and have a common sidebar generator script that should be kept in sync.


## Repository structure
The idea is to have a `docs` folder in the repositories where the source of the documentation will be stored. This folder is automatically recognized by readthedocs hooks that are put in place (more on that later) when the code is pushed GitHub.

Within that folder, the structure followed corresponds to the best practices of `sphynx`. There is an `index.rst` file and a `conf.py` file that are the basis of the whole documentation system.


## Hosting platform
There was a single user (and project: `sdmx`) registered with the site. In that project, multiple projects have been configured with links (watches) on the various branches of the corresponding repositories on Github.

The generated documentation will then be hosted on readthedocs.org and linked toa subdomain of the sdmx web site: [docs.sdmx.org](http://docs.sdmx.org). 
The DNS was modified to create a new **sub-domain** called `docs`. It has been configured to point to the [latest production release](http://readthedocs.org/project/sdmx/latest).

The `sdmx`project linking to the `sdmx-im` acts as the glue between all the other repositories (e.g.: formats, rest, ...).


## Documentation source language
Sphynx uses the **RST** (ReStructuredText) syntax to code the documentation instead of the more simple and perhaps more well known MD (Markdown). **RST** allows for far more possibilities and more complex structure, linking, etc. and is thus much better suited for a technical documentation.


# Creation, adaptation & compilation process
## Existing documents conversion
Most if not all the current (v2.1) documentation is in word or markdown format; it thus needs to be converted into the **RST** syntax that **sphynx** utilises.

There is a well known and practical tool that allows us to more or less easily convert our existing word documents into **RST** source files. This tool is called [pandoc](htts://pandoc.org/) and can be executed in a linux or windows environment to do the majority of the work.

The process for the initial documentation was executed in a windows environment to have access to Microsoft Office. One needs to follow these steps:

1. Open the `filename.doc` in a recent version of Microsoft Word (or equivalent) and use the `file->Save As...` command to save the docuemnt the newer format (docx): `filename.docx` \
(below, you'll find VBA script to automate the conversion within a folder)
1. use `pandoc` to convert the newly created `filename.docx` to `filename.rst` \
(below, you'll find a shell script to automate the process as well)

Here is a bit of VBA script that allows you to batch these conversions from `doc` to `docx`:
```vb
Sub TranslateDocIntoDocx()
  Dim objWordApplication As New Word.Application
  Dim objWordDocument As Word.Document
  Dim strFile As String
  Dim strFolder As String

  strFolder = "C:\<<PATH_TO_FOLDER_WHERE_DOCS_ARE>>\"
  strFile = Dir(strFolder & "*.doc", vbNormal)
  
  While strFile <> ""
    With objWordApplication
      Set objWordDocument = .Documents.Open(FileName:=strFolder & strFile, AddToRecentFiles:=False, ReadOnly:=True, Visible:=False)
          
      With objWordDocument
        .SaveAs FileName:=strFolder & Replace(strFile, "doc", "docx"), FileFormat:=16
        .Close
      End With
    End With
    strFile = Dir()
  Wend

  Set objWordDocument = Nothing
  Set objWordApplication = Nothing
End Sub
```

Here is a bit of shell magic to batch the **pandoc** conversion to `RST`:
```sh
for f in *.docx
do
  filenameOnly="${f%.*}"
  echo -n "Converting ${f}..."
  mkdir ./media-${filenameOnly}
  pandoc --extract-media=./media-${filenameOnly} -f docx -t rst -o ${filenameOnly}.rst ${f}
  echo " done !"
done
```

Unfortunatly, we are not quite done yet since we were dealing with Microsoft words to start with... the problem with Word documents is the way they store images... \
Sometimes, when we are lucky, this may be in `png` or `jpeg` format but most often than not, it is in `EMF` format...\
There is therefore an extra step that we have to take that will convert these `.emf` files to a proper format. We can use the command line possibilities of a very nice application called **InkScape**.
*ref*: [emf to xxx conversion](https://stackoverflow.com/questions/15063349/imagemagick-on-linux-to-convert-emf-to-png/38589531#38589531)

Here below is (yet another) script that will help automate the conversion of the image files by looping in the media folders previously created and converting them.

```sh
inkscapePath="... inkscape.exe"
for f in **/*/*.emf
do 
  filenameOnly="${f%.*}"
  echo -n "Converting ${f}... "
  ${inkscapePath} -e ${filenameOnly}.png ${f}
  echo "done !"
done
```


## Converted files integration
Once the newly converted files (`.rst`) have been made available, they need ot be integrated in to the main documentation. This can be as simple as refering to them from an already integrated `rst` file. In our case, we simply copied them into the project, structured them in sub-folders and referenced them either in the TOC or in the `index.rst`file.


## Site generation (local)
On windows, use `make.bat html` to generate the documentation in the sub-folder `build/html` \
On linux, use `make html`  to generate the documentation in the sub-folder`build/html`\
Open the `index.html` file found in the `build/html` folder.

Please mind that the inter-links (between repositories) will not work in the local generated content. It will instead link to the online version - *I did not find a way to re-direct to the local sibling folder easily...*


## Site generation(online)
ONce the documentation has been written locally and verified, the code commited, it is usually pushed back to the origin repository (GitHub). Using Git, the documentation can be created and version controled locally. Once the documentation is deemed to have reached a correct level and is thus ready to be published, the repository can be pushed back to the online SDMX-TWG repositories. \
This action will actually trigger a documentation re-compilation on readthedocs.org because a project was configured there to watch for such changes in the repositories.


# Particularities
## Special files of the `docs` folder
  * `Makefile` - Sphinx file to manage the documentation building system
  * `make.bat` - Sphinx file to manage the documentation building system
  * `sidebarGenerator.py` -  Functions for managing and generating the TOC (this files needs to be **synced** accross repositories of the SDMX-TWG)
  * `_sidebar.rst.inc` - generated file (from sidebarGenerator.py) - do not commit (part of the .gitignore file)
  * `plantuml.conf` - Common configuration for the PlantUML diagrams
  * `conf.py` - configuration of the Sphynx system & configuration of the TOC
  * `index.rst` - entry point of the documentation

There are essentially two TOC item creation functions: `sdmxLocalToc(...)` and `sdmxPrjToc`. They are used to create either an internal or an extarnal (to the docuemntation of another repository in sdmx-twg) link.

Example:
```python
from sidebarGenerator import SidebarGenerator
s = SidebarGenerator(globals(), "sdmx-im")
s.toctree("Technical Specification", 3) \
  .sdmxLocalToc("", "informationModel/informationModelINdex") \
  .newLine()
s.toctree("Formats") \
  .subPrjToc("sdmx-ml", "SDMX ML")  \
  .newLine()
s.writeIfChanged("_sidebar.rst.inc")
```


# Other considerations/references
## RegEx used for Replacements
Usage: regex to search and replace some figure captions from the automatic conversion of docx => rst using pandoc.

- `^={1,}$\n(\|.*\|)$\n^={1,}$\n(Figure .*)\n^={1,}$` to `$1 $2`
- `(\|.*\|)$\n\n(Figure .*)`to `$1 $2`

