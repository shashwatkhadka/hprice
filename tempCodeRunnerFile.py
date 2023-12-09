def has_multiple_dots(cell):
    return cell.count('.') > 1

columns_to_process = ['LA_N', 'RA_N']

for column in columns_to_process:
    mask = df[column].apply(lambda x: has_multiple_dots(x))
    fdf = df[~mask].copy()  # Create a copy of the filtered DataFrame
    
    fdf.loc[:, column] = fdf[column].astype(float)
    # Update the original DataFrame with the processed values
    df.loc[fdf.index, column] = fdf[column]
