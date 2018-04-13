import pandas as pd

file = 'Clicks-Conv.csv'
names = ['clicks', 'convertions', 'ConvVal', 'cost', 'ConvVal_cost',
        'profit', 'clicks_conv', 'cost_clicks', 'ConvVal_clicks']


# set a threshold
for threshold in range(1, 16):

    dataset = pd.read_csv(file, names=names)
    dropped_rows = []

    # check every row if its data meets the conditions
    for x in range(1, len(dataset.index)):
        row = dataset.iloc[x]
        click = pd.to_numeric(row[0])
        ConvVal_cost = pd.to_numeric(row[4])
        clicks_conv = pd.to_numeric(row[6])
        if click >= threshold and ConvVal_cost < 0.8 and clicks_conv > threshold:
            dropped_rows.append(x)
    dataset = dataset.drop(dataset.index[dropped_rows])
    # count the average yield after deleting keys
    new_yield = pd.to_numeric(dataset.ConvVal_cost[1:]).mean()
    profit = pd.to_numeric(dataset.profit[1:]).sum()
    print("threshold: %s, dropped keys %s, remained keys %s, yield %s, profit %s" % (
            threshold,
            len(dropped_rows),
            len(dataset.index),
            new_yield,
            profit,
        ))
