# tests/indicator_test.py
import data_loader.loader 
import indicators.atr
import indicators.vwap
import indicators.ema
import numpy as np

def test_indicators():
    # Load data
    data = data_loader.loader.read_data()
    
    # Calculate indicators
    atr_values = indicators.atr.atr(data, period=14, sequential=True)
    vwap_values = indicators.vwap.vwap(data, sequential=True)
    ema_values = indicators.ema.ema(data, period=20, sequential=True)  # Using 20-period EMA
    
    # Filter for December 2024 data
    dec_mask = (data['date'] >= np.datetime64('2024-12-01')) & (data['date'] < np.datetime64('2025-01-01'))
    dec_data = data[dec_mask]
    dec_atr = atr_values[dec_mask]
    dec_vwap = vwap_values[dec_mask]
    dec_ema = ema_values[dec_mask]
    
    print("\nDecember 2024 Indicator Values:")
    for i in range(len(dec_data)):
        if not np.isnan(dec_atr[i]) and not np.isnan(dec_vwap[i]) and not np.isnan(dec_ema[i]):
            print(f"\nDate: {dec_data['date'][i]}")
            print(f"Price: Open=${dec_data['open'][i]:,.2f}, High=${dec_data['high'][i]:,.2f}, Low=${dec_data['low'][i]:,.2f}, Close=${dec_data['close'][i]:,.2f}")
            print(f"Volume BTC: {dec_data['volume_btc'][i]:.2f}")
            print(f"ATR: ${dec_atr[i]:,.2f}")
            print(f"VWAP: ${dec_vwap[i]:,.2f}")
            print(f"EMA(20): ${dec_ema[i]:,.2f}")
            print("---")
    
    # Print summary statistics
    valid_dec_atr = dec_atr[~np.isnan(dec_atr)]
    valid_dec_vwap = dec_vwap[~np.isnan(dec_vwap)]
    valid_dec_ema = dec_ema[~np.isnan(dec_ema)]
    
    print("\nDecember 2024 Summary:")
    print(f"ATR - Average: ${np.mean(valid_dec_atr):,.2f}")
    print(f"ATR - Max: ${np.max(valid_dec_atr):,.2f}")
    print(f"ATR - Min: ${np.min(valid_dec_atr):,.2f}")
    print(f"VWAP - Average: ${np.mean(valid_dec_vwap):,.2f}")
    print(f"VWAP - Max: ${np.max(valid_dec_vwap):,.2f}")
    print(f"VWAP - Min: ${np.min(valid_dec_vwap):,.2f}")
    print(f"EMA(20) - Average: ${np.mean(valid_dec_ema):,.2f}")
    print(f"EMA(20) - Max: ${np.max(valid_dec_ema):,.2f}")
    print(f"EMA(20) - Min: ${np.min(valid_dec_ema):,.2f}")

if __name__ == "__main__":
    test_indicators()