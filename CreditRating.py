import pandas as pd
import numpy as np

# Load your dataset
df = pd.read_csv('muni_bonds_2000.csv')

# Function to assign synthetic credit ratings based on realistic bond logic
def assign_credit_rating(row):
    if row['Yield'] < 2 and row['Duration'] < 5:
        return 'AAA'
    elif row['Yield'] < 3.5 and row['Duration'] < 10:
        return 'AA'
    elif row['Yield'] < 5:
        return 'A'
    else:
        return 'BBB'

# Apply the function
df['CreditRating'] = df.apply(assign_credit_rating, axis=1)

# Save the updated CSV
df.to_csv('muni_bonds_with_ratings.csv', index=False)
