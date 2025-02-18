import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquares_WeightedMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquares und WeightedMovingAverage
    """
    
    params = (
        ('indicators', {
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            },
            'WeightedMovingAverage': {
                'class': WeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedMovingAverage'>
            }
        }),
        ('weights', {
            'GannSquares': 1.0,
            'WeightedMovingAverage': 1.0
        })
    )
