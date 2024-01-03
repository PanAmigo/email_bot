import pandas as pd
from pathlib import Path
import os
import time
from datetime import timedelta


start_time = time.monotonic()
imiona_path = Path("imiona.csv").resolve()
names_df = pd.read_csv(imiona_path, sep=',')
end_time = time.monotonic()
print(timedelta(seconds = end_time - start_time))


start_time = time.monotonic()
names_path = os.path.abspath("imiona.csv")
names_df = pd.read_csv(names_path, sep=',')
end_time = time.monotonic()
print(timedelta(seconds = end_time - start_time))


gecodriver_path = os.path.abspath("geckodriver.exe")
print(gecodriver_path)

