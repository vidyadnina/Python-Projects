import pandas as pd
import numpy as np
from datetime import datetime

data = pd.read_csv("bank_marketing.csv")

data['education'] = data['education'].str.replace('.','_')
data['education'] = data['education'].replace('unknown',np.NaN)
data['job'] = data['job'].str.replace('.','_')
data['credit_default'] = data['credit_default'].map({'yes': 1,'no':0,'unknown':0}).astype(bool)
data['mortgage'] = data['mortgage'].map({'yes': 1,'no':0,'unknown':0}).astype(bool)
data['campaign_outcome'] = data['campaign_outcome'].map({'no': 0, 'yes': 1}).astype(bool)
data['previous_outcome'] = data['previous_outcome'].map({'success':1,'failure':0,'nonexistent':0}).astype(bool)

client = data[['client_id','age','job','marital','education','credit_default','mortgage']].copy()

campaign = data[['client_id','number_contacts','contact_duration','previous_campaign_contacts','previous_outcome','campaign_outcome']].copy()

data['month'] = data['month'].str.capitalize()
month_map = {
    'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04', 'May': '05', 'Jun': '06',
    'Jul': '07', 'Aug': '08', 'Sep': '09', 'Oct': '10', 'Nov': '11', 'Dec': '12'
}
data['month'] = data['month'].map(month_map)

campaign['last_contact_date'] = pd.to_datetime('2022-'+data['month'].astype(str) + '-'+data['day'].astype(str), format="%Y-%m-%d")

economics = data[["client_id","cons_price_idx","euribor_three_months"]].copy()

client.to_csv('client.csv', index=False)  
campaign.to_csv('campaign.csv', index=False)  
economics.to_csv('economics.csv', index=False)
