goods = []
features = {'name': '', 'price': '', 'quantity': '', 'unit': ''}
analytics = {'name': [], 'price': [], 'quantity': [], 'unit': []}
num = 0
feature_ = None
control = None
while True:
    control = input("For quit press 'q', for continue press 'Enter', for analytics press 'a'")
    if control == 'q':
        break
    num += 1
    if control == 'a':
        print(f'\nCurrent analytics \n{"-" * 98}')
        for key, value in analytics.items():
            print(f'{key[:10]:>1}: {value}')
            print("-" * 99)
    for f in features.keys():
        feature_ = input(f'Input feature "{f}"')
        features[f] = int(feature_) if (f == 'price' or f == 'quantity') else feature_
        analytics[f].append(features[f])
    goods.append((num, features))
