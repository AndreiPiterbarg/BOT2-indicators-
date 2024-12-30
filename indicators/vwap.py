from typing import Union
import numpy as np
from numba import njit
from numpy_groupies import aggregate_nb as aggregate

def get_candle_source(data: np.ndarray, source_type: str = "hlc3") -> np.ndarray:
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

def vwap(
        data: np.ndarray, source_type: str = "hlc3", anchor: str = "D", sequential: bool = False
) -> Union[float, np.ndarray]:
    """
    VWAP
    :param data: np.ndarray
    :param source_type: str - default: "hlc3"
    :param anchor: str - default: "D"
    :param sequential: bool - default: False
    :return: float | np.ndarray
    """
    source = get_candle_source(data, source_type=source_type)
    group_idx = data['date'].astype('datetime64[ms]').astype(f'datetime64[{anchor}]').astype('int')
    vwap_values = aggregate(group_idx, data['volume_btc'] * source, func='cumsum')
    vwap_values /= aggregate(group_idx, data['volume_btc'], func='cumsum')
    
    if sequential:
        return vwap_values
    else:
        return None if np.isnan(vwap_values[-1]) else vwap_values[-1]