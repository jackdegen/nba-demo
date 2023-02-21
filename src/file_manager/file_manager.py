# Basic class for managing files: saving, loading, creating, organizing, etc.
import os
import pandas as pd

class FileManager:
    
    def __init__(self):
        
#         self.data_dir: str = ''.join([
#             os.getcwd().split('src')[0],
#             'data'
#         ])

        self.data_dir: str = os.path.join(os.getcwd().split('src')[0], 'data')
    
    def raw_path(self) -> str:
        return os.path.join(self.data_dir, 'season-data-raw.csv')
    
    def clean_path(self) -> str:
        return self.raw_path().replace('raw', 'clean')
    
    def load_raw_data(self) -> pd.DataFrame:
        return pd.read_csv(self.raw_path())
    
    def load_clean_data(self) -> pd.DataFrame:
        return pd.read_csv(self.clean_path())
    
    
    def save_dataframe(self, df_save: pd.DataFrame, fname: str, **kwargs) -> None:
        
        fpath: str = os.path.join(self.data_dir, fname)
        
        if '.csv' not in fpath:
            fpath: str = '.'.join([fpath, 'csv'])
        
        df_save.to_csv(
            fpath,
            index=False
        )
        
        return None
    
    
    