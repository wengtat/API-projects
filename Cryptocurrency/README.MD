* Downloading bitcoin prices
    - Setting start date and end date
    - use BtcConverter to get the Bitcoin price for the period of start and end date
* Reading bitcoin prices into pandas
    - import pandas
    - assign 2 columns: date and price
    - convert date column into index column
* Making simple plot
    - df.plot()
* Improving plots
    - Create rolling mean for 30 days
    - import matplotlib
    - import matplotlib.style >> style.use('fivethirtyeight')
    - include title, tick_labels
    - highlight the peak and decline line
    - highlight the background with axvspan
