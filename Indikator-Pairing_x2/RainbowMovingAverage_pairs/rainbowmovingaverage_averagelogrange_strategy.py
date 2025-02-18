import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RainbowMovingAverage_AverageLogRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RainbowMovingAverage und AverageLogRange
    """
    
    params = (
        ('indicators', {
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            },
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            }
        }),
        ('weights', {
            'RainbowMovingAverage': 1.0,
            'AverageLogRange': 1.0
        })
    )
