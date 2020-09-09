## Data Report Generator

#### Data Report Generator is a script for generating data overview reports for tabular datasets

##### *Currently supports .xlsx .csv .parquet files*


#### Output file
* *Shape*
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

### Requirements



### Installation


### Usage
If alias is not set:

```bash
python3 generator.py generate --path=path_to_file
```

If alias is set:
```bash
generate_report --path=path_to_file
```