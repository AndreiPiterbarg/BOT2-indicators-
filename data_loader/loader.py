import numpy as np

def read_data():
    # First, define the dtype for each column
    dtype = [
        ('date', 'datetime64[s]'),
        ('open', 'float64'),
        ('high', 'float64'),
        ('low', 'float64'),
        ('close', 'float64'),
        ('volume_btc', 'float64'),
        ('volume_usd', 'float64')
    ]
    
    # Load data with specified dtypes
    data = np.genfromtxt("data/BTC_historical.csv", 
                         delimiter=',', 
                         skip_header=1,
                         usecols=(1,3,4,5,6,7,8),
                         dtype=dtype)
    
    # Sort data by date in ascending order (oldest to newest)
    data = np.sort(data, order='date')
    
    return data

def test_data_load():
    data = read_data()
    
    print("Array shape:", data.shape)
    
    print("\nFirst 3 rows of data:")
    print(data[:3])
    
    print("\nSample of each column:")
    print("Date:", data['date'][0], type(data['date'][0]))
    print("Open:", data['open'][0], type(data['open'][0]))
    print("High:", data['high'][0], type(data['high'][0]))
    print("Low:", data['low'][0], type(data['low'][0]))
    print("Close:", data['close'][0], type(data['close'][0]))
    print("Volume BTC:", data['volume_btc'][0], type(data['volume_btc'][0]))
    print("Volume USD:", data['volume_usd'][0], type(data['volume_usd'][0]))
