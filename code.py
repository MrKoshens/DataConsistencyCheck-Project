import pandas as pd
from check_data_consistency import DataConsistencyChecker


df = pd.read_csv("~/Breast_Cancer_Global_Dataset.csv")


dc = DataConsistencyChecker()
dc.init_data(df)


dc.check_data_quality()


dc.display_detailed_results(save_to_disk=True)