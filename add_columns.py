import pandas as pd
import uuid

# Load the CSV file into a DataFrame
csv_file = 'bulk_data_2009_2010.csv'  # Replace with your CSV file path
df = pd.read_csv(csv_file)

# Generate unique values for each column
df['ref_og'] = [str(uuid.uuid4()) for _ in range(len(df))]
df['ref_etab'] = [str(uuid.uuid4()) for _ in range(len(df))]
df['ref_formation'] = [str(uuid.uuid4()) for _ in range(len(df))]
df['ref_diplome'] = [str(uuid.uuid4()) for _ in range(len(df))]
df['ref_entreprise'] = [str(uuid.uuid4()) for _ in range(len(df))]
df['ref_jeune'] = [str(uuid.uuid4()) for _ in range(len(df))]

# Append the new columns to the CSV file
df.to_csv('bulk_with_primary.csv', index=False)
