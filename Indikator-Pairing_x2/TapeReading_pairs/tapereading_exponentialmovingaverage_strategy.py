import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TapeReading_ExponentialMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TapeReading und ExponentialMovingAverage
    """
    
    params = (
        ('indicators', {
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            },
            'ExponentialMovingAverage': {
                'class': ExponentialMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExponentialMovingAverage'>
            }
        }),
        ('weights', {
            'TapeReading': 1.0,
            'ExponentialMovingAverage': 1.0
        })
    )
