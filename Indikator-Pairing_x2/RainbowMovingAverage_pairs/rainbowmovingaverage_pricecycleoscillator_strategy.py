import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RainbowMovingAverage_PriceCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RainbowMovingAverage und PriceCycleOscillator
    """
    
    params = (
        ('indicators', {
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            },
            'PriceCycleOscillator': {
                'class': PriceCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceCycleOscillator'>
            }
        }),
        ('weights', {
            'RainbowMovingAverage': 1.0,
            'PriceCycleOscillator': 1.0
        })
    )
