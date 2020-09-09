import fire
import io
import os
import pandas as pd

class DataReportGenerator:
    def read_file(self, path, sep=','):
        try:
            ftype = path.split('/')[0].split('.')[-1]
        except IndexError:
            raise Exception('Invalid file name.')

        if ftype == 'csv':
            df = pd.read_csv(path, sep=sep)
        elif ftype == 'xlsx':
            df = pd.read_excel(path)
        elif ftype == 'parquet':
            df = pd.read_parquet(path)
        else:
            raise Exception(f"File type '{ftype}' is not supported.")

        return df

    def generate(self, path, output=None, sep=','):
        fdir, fname = '/'.join(path.split('/')[:-1]), path.split('/')[-1]
        assert '.' in fname, f"Unrecognized file type '{fname}'."

        df = self.read_file(path, sep)
        
        if not output:
            report_fname = f"report_{fname.split('.')[0]}.txt"
            output = f'{fdir}/{report_fname}' if fdir else report_fname
        else:
            assert output.split('/')[-1].split('.')[-1] == 'txt', "Output file type can only be 'txt'."

        file_ = open(output, 'w')

        file_.write(f"\n___Report for {path}___\n{'*'*int(len(path)*2)}\n\n")

        file_.write(f'Shape: {df.shape}\n')
        file_.write(f'Has duplicates: {df[df.duplicated()].shape[0] != 0}\n')
        file_.write(f'Has duplicates ignoring missing: {df.dropna()[df.dropna().duplicated()].shape[0] != 0}')
        file_.write(f'\n\n{"-"*200}\n\n')


        # Columns
        file_.write('Columns:\n')
        for idx, (column, dtype) in enumerate(zip(list(df.columns), list(df.dtypes))):
            file_.write(f'\t{idx} {column} -> {dtype}\n')
            file_.write(f'\t  """ __description__ """\n\n')
            file_.write(f'\t\t- UniqueCount:\t{df[column].unique().shape[0]}\n\n')
            sample_size = 10 if df.shape[0] > 10 else df.shape[0]
            sample = list(map(lambda val: str(val) if len(str(val)) < 200 else str(val)[:200]+'...', df.sample(sample_size)[column].tolist()))
            head_tail_x = 20 if df.shape[0] > 40 else df.shape[0] // 2
            file_.write(f'\t\t- {sample_size} Random values:\t{list(sample)}\n\n')
            file_.write(f'\t\t- {head_tail_x} First values:\t{df[column].head(head_tail_x).tolist()}\n\n')
            file_.write(f'\t\t- {head_tail_x} Last values:\t{df[column].tail(head_tail_x).tolist()}\n\n\n')
        file_.write(f"{'-'*200}\n\n")
        
        # Info
        file_.write('Info:\n')
        buf = io.StringIO()
        df.info(buf=buf)
        info = '\n'.join(map(lambda x: f'\t{x}', buf.getvalue().split('\n')[1:-3]))
        file_.write(info + f'\n\n{"-"*200}\n\n')

        # 10 Random rows
        file_.write('10 Random rows:\n')
        sample_size = 10 if df.shape[0] > 10 else df.shape[0]
        for idx, row in df.sample(sample_size).iterrows():
            row = {col: str(val) if len(str(val)) < 200 else str(val)[:200]+'...' for col, val in row.items()}
            file_.write(f'\tIndex {idx}\t{row}\n\n')
        file_.write(f'\n{"-"*200}\n\n')

        file_.write('Rows with missing data in columns:\n\n')
        for column in df.columns:
            df_col_miss = df[df[column].isna()]
            if df_col_miss.shape[0] != 0:
                file_.write(f'\t* {column} -> missing {df_col_miss.shape[0]} values\t{"-" * 100}\n\n')
                sample_size = 10 if df_col_miss.shape[0] > 10 else df_col_miss.shape[0]
                for idx, row in df_col_miss.sample(sample_size).iterrows():
                    row = {col: str(val) if len(str(val)) < 200 else str(val)[:200]+'...' for col, val in row.items()}
                    file_.write(f'\t\tIndex {idx}\t{row}\n\n')
                file_.write('\n')

        file_.close()
        print(f'Report path : {output}')


if __name__ == '__main__':
    fire.Fire(DataReportGenerator)
