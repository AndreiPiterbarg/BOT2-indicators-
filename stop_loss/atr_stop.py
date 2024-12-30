import indicators.atr

def stop_loss(data, atr_multiplier=2):
    atr_value = indicators.atr.atr(data, period=14)
    #CHOOSE CUSTOM VALUE between 2 or 3

    stop_loss = atr_value * atr_multiplier
    return stop_loss