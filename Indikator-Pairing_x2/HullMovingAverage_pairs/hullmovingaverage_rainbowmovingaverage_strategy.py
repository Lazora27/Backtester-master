import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HullMovingAverage_RainbowMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HullMovingAverage und RainbowMovingAverage
    """
    
    params = (
        ('indicators', {
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            },
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            }
        }),
        ('weights', {
            'HullMovingAverage': 1.0,
            'RainbowMovingAverage': 1.0
        })
    )
