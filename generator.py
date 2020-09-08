import fire
import io
import os
import pandas as pd

class DataReportGenerator:
    def read_file(self, fpath, ftype=None, sep=','):
        if not ftype:
            try:
                ftype = fpath.split('.')[-1]
            except IndexError:
                raise Exception('Invalid file name.')

        if ftype == 'csv':
            df = pd.read_csv(fpath, sep=sep)
        elif ftype == 'xlsx':
            df = pd.read_excel(fpath)
        elif ftype == 'parquet':
            df = pd.read_parquet(fname)
        else:
            raise Exception(f"File type '{ftype}' is not supported.")

        return df

    def generate(self, fpath, ftype=None, sep=',', output_path=None):
        print(os.getcwd())
        fdir, fname = '/'.join(fpath.split('/')[:-1]), fpath.split('/')[-1]

        df = self.read_file(fpath, ftype, sep)

        if ftype and '.' not in fpath:
            report_fname = f'report_{fname}.txt'
        else:
            report_fname = f"report_{fname.split('.')[0]}.txt"
        
        if not output_path:
            output_path = fdir
        output_file = f'{output_path}/{report_fname}' if output_path else report_fname
        file_ = open(output_file, 'w')

        file_.write(f"\n___Report for {fpath}___\n{'*'*int(len(fpath)*2)}\n\n")

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
        print(f'Report path : {output_file}')


if __name__ == '__main__':
    fire.Fire(DataReportGenerator)
