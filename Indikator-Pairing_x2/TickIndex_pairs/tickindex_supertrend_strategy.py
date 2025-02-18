import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_SuperTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und SuperTrend
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'SuperTrend': 1.0
        })
    )
