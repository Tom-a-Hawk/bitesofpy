import pandas as pd

#data = "http://projects.bobbelderbos.com/data/summer.csv"



def athletes_most_medals():
    file_name = 'summer.csv'
    df = pd.read_csv(file_name, header=0)
    w = df[df['Gender'] == 'Men'].groupby(['Athlete'])['Medal'].count().sort_values(ascending=False).head(1)
    x = df[df['Gender'] == 'Women'].groupby(['Athlete'])['Medal'].count().sort_values(ascending=False).head(1)
    y = pd.concat([w,x])
    return y

