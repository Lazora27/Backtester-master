import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquares_SuperTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquares und SuperTrend
    """
    
    params = (
        ('indicators', {
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            },
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            }
        }),
        ('weights', {
            'GannSquares': 1.0,
            'SuperTrend': 1.0
        })
    )
