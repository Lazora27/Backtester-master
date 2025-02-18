import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperTrend_UlcerIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperTrend und UlcerIndex
    """
    
    params = (
        ('indicators', {
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            },
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            }
        }),
        ('weights', {
            'SuperTrend': 1.0,
            'UlcerIndex': 1.0
        })
    )
