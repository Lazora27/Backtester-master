import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquareReversal_HullMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquareReversal und HullMovingAverage
    """
    
    params = (
        ('indicators', {
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            },
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            }
        }),
        ('weights', {
            'GannSquareReversal': 1.0,
            'HullMovingAverage': 1.0
        })
    )
