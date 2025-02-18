import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickActivityIndex_SuperTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickActivityIndex und SuperTrend
    """
    
    params = (
        ('indicators', {
            'TickActivityIndex': {
                'class': TickActivityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickActivityIndex'>
            },
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            }
        }),
        ('weights', {
            'TickActivityIndex': 1.0,
            'SuperTrend': 1.0
        })
    )
