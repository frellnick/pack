# Pack

**UDRC** data preparation and packaging utility for use with importer.  This module will take .csv's in a given directory, profile and clean each dataset, and translate those profile into Oracle specific metadata for ingest.  

Outputs a single .zip file of specified or default name.


## Parameters

**zipname**: Output filename.  Include extension .zip for OS type inference.

**save**: 'True' or 'False'.  Default 'True'. Whether or not to retain cleaned datasets in data directory (creates copies of data) and not just in .zip output.


## Usage

```bash
python pack.py <PATH TO DIRECTORY> --zipname <OUTPUT_FILENAME.zip> --save <TRUE/FALSE>
```

**Example**

```bash
python pack.py data/ --zipname adhoc_igp_2020-09-07.zip --save False
```


## Tests

Run tests with: 

```python
python -m unittest discover
```