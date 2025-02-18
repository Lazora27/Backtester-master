import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_RainbowMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und RainbowMovingAverage
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'RainbowMovingAverage': 1.0
        })
    )
