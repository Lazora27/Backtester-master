import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquares_SimpleMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquares und SimpleMovingAverage
    """
    
    params = (
        ('indicators', {
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            },
            'SimpleMovingAverage': {
                'class': SimpleMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SimpleMovingAverage'>
            }
        }),
        ('weights', {
            'GannSquares': 1.0,
            'SimpleMovingAverage': 1.0
        })
    )
