import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquares_ExponentialMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquares und ExponentialMovingAverage
    """
    
    params = (
        ('indicators', {
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            },
            'ExponentialMovingAverage': {
                'class': ExponentialMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExponentialMovingAverage'>
            }
        }),
        ('weights', {
            'GannSquares': 1.0,
            'ExponentialMovingAverage': 1.0
        })
    )
