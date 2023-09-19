from lib import generate_data, describe_with_pandas, generate_scatter_plot

# Generate example data using common library
df = generate_data("iris.csv")

# Perform descriptive statistics using common library and Pandas
pandas_stats = describe_with_pandas(df)
print("Descriptive statistics using Pandas:")
print(pandas_stats)

# Generate scatter plot 
generate_scatter_plot(df, "Id", "SepalLengthCm")