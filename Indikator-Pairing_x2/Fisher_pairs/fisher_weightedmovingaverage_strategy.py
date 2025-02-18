import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_WeightedMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und WeightedMovingAverage
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'WeightedMovingAverage': {
                'class': WeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedMovingAverage'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'WeightedMovingAverage': 1.0
        })
    )
