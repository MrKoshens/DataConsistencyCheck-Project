import pandas as pd
from check_data_consistency import DataConsistencyChecker


df = pd.read_csv("your_dataset.csv")


dc = DataConsistencyChecker()
dc.init_data(df)


dc.check_data_quality()


dc.display_detailed_results(save_to_disk=True)