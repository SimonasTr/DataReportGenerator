Data Report Generator
-----------------
Data Report Generator is a script for generating data overview reports for tabular datasets.

Currently supports .xlsx .csv .parquet files.

Output file
- Shape
- Columns
    * __description__ requires manual input
    * Column name -> Column type
    * Unique count
    * 10 Random sample
    * 20 First values
    * 20 Last values
- Info pd.DataFrame.info()
- 10 Random rows
- 10 Random rows for every column with missing values in that column

Requirements
------------

There are several extra requirements which you might to install to get full
feature set. This cal be easily specified during pip installation::

    # Install with XML support
    pip install translate-toolkit[XML]

    # Install all optional dependencies
    pip install translate-toolkit[all]

.. note:: Please check ``requirements/*.txt``::

       pip install -r requirements/optional.txt

   Will install all optional dependencies convering support for many other
   formats.

The Toolkit requires Python 3.5 or newer.

The package lxml is required. You should install version 4.0.0 or later.
<http://lxml.de/> Depending on your platform, the easiest way to install might
be through your system's package management. Alternatively you can try ::

    pip install lxml

which should install the newest version from the web.

For Mac OSX, the following pages might be of help:
<http://lxml.de/build.html#building-lxml-on-macos-x>
<http://lxml.de/installation.html#macos-x>

The package lxml has dependencies on libxml2 and libxslt. Please check the lxml
site for the recommended versions of these libraries if you need to install
them separately at all. Most packaged versions of lxml will already contain
these dependencies.

When the environment variable USECPO is set to 1, the toolkit will attempt to
use libgettextpo from the gettext-tools package (it might have a slightly
different name on your distribution). This can greatly speed up access to PO
files, but has not yet been tested as extensively. Feedback is most welcome.

The package iniparse is necessary for ini2po and po2ini:
<https://pypi.org/project/iniparse/>

The python-Levenshtein package will improve performance for fuzzy matching if
it is available. This can improve the performance of pot2po, for example.  It
is optional and no functionality is lost if it is not installed, only speed.
<http://sourceforge.net/projects/translate/files/python-Levenshtein/>

Functions in the `lang.data` module can supply functions to translate language
names using the `pycountry` package. It can even translate names in the format
``Language (Country)`` such as ``English (South Africa)`` This is used by
Pootle and Virtaal. If the package is not installed, the language names will
simply appear in English. It is therefore recommended you install the
`pycountry` package.

The package vobject is needed for ical2po and po2ical.

The aeidon package (or gaupol if aeidon is not available) is needed for sub2po
and po2sub. Some Unicode encoded files (including most files from
<http://dotsub.com/>) require version 0.14 or later.
<http://home.gna.org/gaupol/>
Gaupol might need the 'Universal Encoding Detector'
<http://pypi.python.org/pypi/chardet>

Trados TXT TM support requires the BeautifulSoup parser
<http://www.crummy.com/software/BeautifulSoup/>


Program overview
----------------

Use ``--help`` to find the syntax and options for all programs.

* Converters::

        oo2po    - convert between OpenOffice.org GSI files and PO
        oo2xliff - convert between OpenOffice.org GSI files and XLIFF
        moz2po   - convert between Mozilla files and PO
        csv2po   - convert PO format to CSV for editing in a spreadsheet program
        php2po   - PHP localisable string arrays converter.
        ts2po    - convert Qt Linguist (.ts) files to PO
        txt2po   - convert simple text files to PO
        html2po  - convert HTML to PO (beta)
        xliff2po - XLIFF (XML Localisation Interchange File Format) converter
        prop2po  - convert Java .properties files to PO
        po2wordfast - Wordfast Translation Memory converter
        po2tmx   - TMX (Translation Memory Exchange) converter
        pot2po   - PO file initialiser
        csv2tbx  - Create TBX (TermBase eXchange) files from Comma Separated
                   Value (CSV) files
        ini2po   - convert .ini files to to PO
        ical2po  - Convert iCalendar files (*.ics) to PO
        sub2po   - Convert many subtitle files to PO
        resx2po  - convert .Net Resource (.resx) files to PO

* Tools (Quality Assurance)::

        pofilter - run any of the 40+ checks on your PO files
        pomerge  - merge corrected translations from pofilter back into
                   your existing PO files.
        poconflicts - identify conflicting use of terms
        porestructure - restructures po files according to poconflict directives
        pogrep   - find words in PO files

* Tools (Other)::

        pocompile - create a Gettext MO files from PO or XLIFF files
        pocount   - count translatable file formats (PO, XLIFF)
        podebug   - Create comment in your PO files' msgstr which can
                    then be used to quickly track down mistranslations
                    as the comments appear in the application.
        posegment - Break a PO or XLIFF files into sentence segments,
                    useful for creating a segmented translation memory.
        poswap    - uses a translation of another language that you
                    would rather use than English as source language
        poterminology - analyse PO or POT files to build a list of
                        frequently occurring words and phrases
