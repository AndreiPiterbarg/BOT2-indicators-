from typing import Union
import numpy as np
import talib

def atr(data: np.ndarray, period: int = 14, sequential: bool = False) -> Union[float, np.ndarray]:
    """
    ATR - Average True Range
    :param data: np.ndarray - structured array with 'high', 'low', 'close' columns
    :param period: int - default: 14
    :param sequential: bool - default: False
    :return: float | np.ndarray
    """
    # Get the required price data from structured array
    high = data['high']
    low = data['low']
    close = data['close']
    
    # Calculate ATR using talib
    res = talib.ATR(high, low, close, timeperiod=period)
    
    # Return either the full sequence or just the last value
    return res if sequential else res[-1]

# Example usage:
# data = read_data()  # Your structured array
# atr_value = atr(data, period=14)  # Get single value
# atr_series = atr(data, period=14, sequential=True)  # Get full series