import io
from sklearn.linear_model import LinearRegression

def add_delimiters(fpath, delimiter=','):
    """
    Add delimiters to a file that is missing them.
    modified from https://stackoverflow.com/questions/52861571/pandas-read-csv-load-data-with-irregular-rows
    """
    s_data = ''
    max_num_delimiters = 0
    # use encoding='utf-8-sig' when opring a csv file with special characters
    with open(fpath, 'r', encoding="utf-8-sig") as f:
        for line in f:
            s_data += line
            delimiter_count = line.count(delimiter)
            if delimiter_count > max_num_delimiters:
                max_num_delimiters = delimiter_count

    s_delimiters = delimiter * max_num_delimiters + '\n'
    return io.StringIO(s_delimiters + s_data)



def plot_correlation(df, weather_variable, sales_variable, condition, condition_value, ax):
    df= df[df[condition] == condition_value]
    ax.scatter(df[weather_variable], df[sales_variable])
    ax.set_xlabel(weather_variable)
    ax.set_ylabel(sales_variable)
    X = df[weather_variable].values.reshape(-1, 1)
    y = df[sales_variable].values.reshape(-1, 1)
    reg = LinearRegression().fit(X, y)
    ax.plot(X, reg.predict(X), color="red")
    corr = df[sales_variable].corr(df[weather_variable])
    ax.set_title(f"{condition}: {condition_value}: Corr = {corr.round(2)}")