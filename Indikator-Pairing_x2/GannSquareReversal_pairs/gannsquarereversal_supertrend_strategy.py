import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquareReversal_SuperTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquareReversal und SuperTrend
    """
    
    params = (
        ('indicators', {
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            },
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            }
        }),
        ('weights', {
            'GannSquareReversal': 1.0,
            'SuperTrend': 1.0
        })
    )
