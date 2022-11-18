import pandas as pd
import numpy as np
import dataclasses
from typing import Dict, Optional
import more_itertools
import os

@dataclasses.dataclass(frozen=True)
class DataSource:
    """ 
    A dataset with columns to be renamed to be comibed with other DataSources.
    """
    
    data: pd.DataFrame
    column_mapping: Dict[str, str] # maps New Column Name -> Old Column Name
    name: Optional[str] = None
    
    def remap(self):
        """
        Rename and select a subset of data columns.
        """
        
        # Values mapped to None mean that value isn't available in the given dataset
        rename_dict = {v: k for k, v in self.column_mapping.items() if v is not None}
        
        df = self.data[rename_dict.keys()]
        df = df.rename(columns=rename_dict)
        
        if self.name is not None: 
            if "data_source" in df.columns:
                raise ValueError("df already contains data source column.")
            
            df["data_source"] = self.name
            #df["data_source"] = df["data_source"].astype("category")
            
        return df
    
def combine(*data_sources, require_matched_columns: bool = False) -> pd.DataFrame:
    """
    Concatenate DataSources into a single df.
    """
        
    column_names = [s.column_mapping.keys() for s in data_sources]
    if require_matched_columns and not more_itertools.all_equal(column_names):
        raise ValueError("All DataSources must list the same set of new column names.")
        
    processed = [data_source.remap() for data_source in data_sources]
    result = pd.concat(processed, ignore_index = True)
        
    if any([s.name for s in data_sources]):
        result["data_source"] = result["data_source"].astype("category")
            
    return result