import pandas as pd

file = 'Clicks-Conv.csv'
names = ['clicks', 'convertions', 'ConvVal', 'cost', 'ConvVal_cost',
        'profit', 'clicks_conv', 'cost_clicks', 'ConvVal_clicks']


# set a threshold
for threshold in range(1, 16):

    dataset = pd.read_csv(file, names=names)
    changed_rows = []
    # convert columns to numeric
    clicks = pd.to_numeric(dataset['clicks'], errors='coerce')
    ConvVal_cost = pd.to_numeric(dataset['ConvVal_cost'], errors='coerce')
    clicks_conv = pd.to_numeric(dataset['clicks_conv'], errors='coerce')
    ConvVal_clicks = pd.to_numeric(dataset['ConvVal_clicks'], errors='coerce')
    cost_clicks = pd.to_numeric(dataset['cost_clicks'], errors='coerce')

    # check every row if its data meets the conditions
    for x in range(1, len(dataset.index)):
        row = dataset.iloc[x]
        if clicks[x] >= threshold and ConvVal_cost[x] < 0.8 and clicks_conv[x] > threshold:
            dataset.loc[x, 'clicks'] = threshold
            dataset.loc[x, 'ConvVal'] = dataset.ConvVal_clicks[x] * threshold
            dataset.loc[x, 'cost'] = dataset.cost_clicks[x] * threshold
            dataset.loc[x, 'profit'] = (ConvVal_clicks[x] * threshold)-(cost_clicks[x] * threshold)
            changed_rows.append(x)

    # count the average yield after deleting keys
    new_yield = ConvVal_cost[1:].mean()
    profit = pd.to_numeric(dataset.profit[1:]).sum()
    print("threshold: %s, changed keys %s, unchanged keys %s, yield %s, profit %s" % (
            threshold,
            len(changed_rows),
            len(dataset.index),
            new_yield,
            profit,
        ))
