import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquareReversal_SimpleMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquareReversal und SimpleMovingAverage
    """
    
    params = (
        ('indicators', {
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            },
            'SimpleMovingAverage': {
                'class': SimpleMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SimpleMovingAverage'>
            }
        }),
        ('weights', {
            'GannSquareReversal': 1.0,
            'SimpleMovingAverage': 1.0
        })
    )
