
def filter_males(df):
	"""Return rows where the sex column equals 'male'."""
	# If there is no 'sex' column return an empty dataframe with same columns
	if "sex" not in df.columns:
		return df.iloc[0:0]
	# Normalize values to string and compare case-insensitively
	sex_series = df["sex"].astype(str).str.lower()
	return df[sex_series == "male"]
