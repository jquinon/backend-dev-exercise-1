import sqlalchemy
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

db_path = "exercise01.sqlite"

dbEngine = sqlalchemy.create_engine("sqlite:///" + db_path)

df = pd.read_sql("select * from combined", dbEngine)

df.replace(to_replace="?", value=np.NaN, inplace=True)

# Get count of data
count = len(df.index)
print("Number of Rows: " + str(count))
print()

# Zero vs Non-Zero Capital Loss
zero_capital_loss = df["capital_loss"].value_counts().to_dict()[0]
print("Zero Capital Loss: " + str(zero_capital_loss))
print("Non-Zero Capital Loss: " + str(count - zero_capital_loss))
print()


# Countries by percent
countries_by_percent = df["country"].value_counts(normalize=True)
print("Countries by percent:")
print(countries_by_percent)
print()

# Table with missing data for each column
missing_data = df.isnull().sum()
print("Missing Data:")
print(missing_data)
print()

# workclass and occupation compared to different variables (education, over_50k, age, country, etc)
chart_df = df[["marital_status", "capital_gain"]].groupby("marital_status").mean()
print(chart_df)
chart_df.plot.bar(title="Marital Status vs Capital Gain")
plt.tight_layout()
plt.show()
plt.savefig("marital_status_vs_capital_gain.png", format="png")
