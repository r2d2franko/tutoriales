import pandas as pd
import glob
import os

def leer_archivo(path):
    df_csv= pd.read_csv(path, usecols=["fecha", "producto", "cantidad", "precio_unitario"])
    df_csv['archivo_origen'] = path
    df_csv
    return df_csv