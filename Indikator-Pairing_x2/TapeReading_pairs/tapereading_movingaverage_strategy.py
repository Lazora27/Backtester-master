import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TapeReading_MovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TapeReading und MovingAverage
    """
    
    params = (
        ('indicators', {
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            },
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            }
        }),
        ('weights', {
            'TapeReading': 1.0,
            'MovingAverage': 1.0
        })
    )
