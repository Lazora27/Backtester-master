import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_ExponentialMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und ExponentialMovingAverage
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'ExponentialMovingAverage': {
                'class': ExponentialMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExponentialMovingAverage'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'ExponentialMovingAverage': 1.0
        })
    )
