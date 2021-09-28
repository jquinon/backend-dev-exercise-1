from django.shortcuts import render
from django.conf import settings
import sqlalchemy
import pandas as pd
import numpy as np

# Create your views here.
def index(request):

    # Access database via sqlalchemy
    db_path = "./exercise01.sqlite"
    dbEngine = sqlalchemy.create_engine("sqlite:///" + db_path)

    # Import into pandas for analysis
    df = pd.read_sql("select * from combined", dbEngine)
    df.replace(to_replace="?", value=np.NaN, inplace=True)

    count = len(df.index)

    # Perform same analysis code done in python script
    zero_capital_loss = df["capital_loss"].value_counts().to_dict()[0]

    countries_by_percent = (
        df["country"].value_counts(normalize=True).apply(lambda x: x * 100).round(2)
    )

    missing_data = df.isnull().sum().to_dict()

    # Put analysis data into dictionary for template
    data = {
        "count": count,
        "zero_capital_loss": zero_capital_loss,
        "non_zero_capital_loss": count - zero_capital_loss,
        "countries_by_percent": countries_by_percent,
        "missing_data": missing_data,
    }

    # Render template with data
    return render(request, "dataDisplayApp/index.html", data)
