# CoffeClimateCorrelation

In this projekt, we analysed whether coffee sales in Tübingen are correlated to weather variables such as temperatur, sunshine duration and precipitation.

## Datasets
For our weather dataset, we chose the historic weather data recordings from [ECAD](https://www.ecad.eu/) (European Climate Assessment & Dataset) . We chose the weather station in Stuttgart-Echterdingen. The data is available from 1951 to 2022. The data is available in the folder `/raw_weatherdata`. 

For our coffee sales dataset, we got access to the sales data of a local café, the [SUEDHANG](https://www.suedhang.org/) . The data is available from 2020 to 2022. The data is located in the folder `/raw_coffee_sales`. However, raw coffee sales data is available only on request due to privacy reasons, here only the processed data is available in the folder `/processed_data`.


## Data processing
The data processing is done in the jupyter notebooks. The data processing is done in the following order:

1. `01_find_coffeproducts.ipynb`
2. `01_load_coffeesalesdata.ipynb`
3. `02_load_weatherdata.ipynb`


## Data analysis and results
The data analysis is done in the jupyter notebooks `03_plot_combined_data.ipynb`

## Authors
Nadia Vohwinkel and Magnus Kaut

put the hyperlink 
hyperlink: [
    ,
    {
        "text": "SUEDHANG",
        "url": "https://www.suedhang.de/"
    }
    ]

