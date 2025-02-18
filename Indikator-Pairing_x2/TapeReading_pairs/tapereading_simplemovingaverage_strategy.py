import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TapeReading_SimpleMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TapeReading und SimpleMovingAverage
    """
    
    params = (
        ('indicators', {
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            },
            'SimpleMovingAverage': {
                'class': SimpleMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SimpleMovingAverage'>
            }
        }),
        ('weights', {
            'TapeReading': 1.0,
            'SimpleMovingAverage': 1.0
        })
    )
