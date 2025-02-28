from config import usernames
import pandas as pd
#新增帳號的程式

df = pd.DataFrame(columns=['檔名','文案','tag'])
for user in usernames:
    df.to_csv( f"C:/data/{user}.csv",index=False)

