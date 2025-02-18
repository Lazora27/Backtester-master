import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PercentagePriceOscillator_RainbowMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PercentagePriceOscillator und RainbowMovingAverage
    """
    
    params = (
        ('indicators', {
            'PercentagePriceOscillator': {
                'class': PercentagePriceOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PercentagePriceOscillator'>
            },
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            }
        }),
        ('weights', {
            'PercentagePriceOscillator': 1.0,
            'RainbowMovingAverage': 1.0
        })
    )
