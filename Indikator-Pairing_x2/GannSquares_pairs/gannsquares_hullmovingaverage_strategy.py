import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquares_HullMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquares und HullMovingAverage
    """
    
    params = (
        ('indicators', {
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            },
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            }
        }),
        ('weights', {
            'GannSquares': 1.0,
            'HullMovingAverage': 1.0
        })
    )
