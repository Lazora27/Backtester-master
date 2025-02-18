import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TapeReading_WeightedMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TapeReading und WeightedMovingAverage
    """
    
    params = (
        ('indicators', {
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            },
            'WeightedMovingAverage': {
                'class': WeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedMovingAverage'>
            }
        }),
        ('weights', {
            'TapeReading': 1.0,
            'WeightedMovingAverage': 1.0
        })
    )
