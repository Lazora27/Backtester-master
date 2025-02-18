import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_WeightedMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und WeightedMovingAverage
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'WeightedMovingAverage': {
                'class': WeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedMovingAverage'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'WeightedMovingAverage': 1.0
        })
    )
