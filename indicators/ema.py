# indicators/ema.py
from typing import Union
import numpy as np
import talib

def get_source(data: np.ndarray, source_type: str = "close") -> np.ndarray:
    """Helper function to get price source"""
    if source_type == "hlc3":
        return (data['high'] + data['low'] + data['close']) / 3
    elif source_type == "hl2":
        return (data['high'] + data['low']) / 2
    elif source_type == "close":
        return data['close']
    elif source_type == "high":
        return data['high']
    elif source_type == "low":
        return data['low']
    else:
        raise ValueError(f"Invalid source_type: {source_type}")

def ema(data: np.ndarray, period: int = 5, source_type: str = "close", sequential: bool = False) -> Union[float, np.ndarray]:
    """
    EMA - Exponential Moving Average

    :param data: np.ndarray - structured array with OHLCV data
    :param period: int - default: 5
    :param source_type: str - default: "close"
    :param sequential: bool - default: False

    :return: float | np.ndarray
    """
    source = get_source(data, source_type)
    res = talib.EMA(source, timeperiod=period)
    
    return res if sequential else res[-1]