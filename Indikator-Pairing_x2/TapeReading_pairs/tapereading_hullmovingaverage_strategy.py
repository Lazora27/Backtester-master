import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TapeReading_HullMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TapeReading und HullMovingAverage
    """
    
    params = (
        ('indicators', {
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            },
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            }
        }),
        ('weights', {
            'TapeReading': 1.0,
            'HullMovingAverage': 1.0
        })
    )
