## Data Report Generator

#### Data Report Generator is a script for generating data overview reports for tabular datasets

##### *Currently supports `.xlsx` `.csv` `.parquet` files*


#### Output file
* *Shape*
* *Has duplicates (based on all columns)*
* *Duplicate count based on [column_1, column_2, ...] (if `--duplicate_check_cols` is set)*
* *Columns*
    * *description (requires manual input)*
    * *Column name -> Column type*
    * *Unique count*
    * *10 Random sample*
    * *20 First values*
    * *20 Last values*
* *Info (pandas.DataFrame.info)*
* *10 Random rows*
* *10 Random rows for every column containing missing values in that column*

## Requirements
```bash
>= python3.6
```

## Installation
1. Ensure `>= python3.6` is installed
1. `pip install -r requirements.txt`
1. Add `alias generate_report="python3 path_to_generator.py generate"` to `.bashrc` and source it *(optional)*


## Basic Usage
*If alias is not set:*

```bash
python3 generator.py generate --path=path_to_file
```

*If alias is set:*
```bash
generate_report --path=path_to_file
```

### Reference

| Argument       | Notes     | Optional     |
| :------------------ | :----------: | -----------: |
|  `--path` | Path to tabular file   | `False`    |
| `--output`   | If not set, report is generated in dataset directory | `True` |
| `--duplicate_check_cols` | `,` separated column names | `True` |
| `--sep`   | Separator *(for `.csv` files)* | `True` |