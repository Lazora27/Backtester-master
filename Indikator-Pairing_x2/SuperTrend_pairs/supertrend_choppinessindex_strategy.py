import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperTrend_ChoppinessIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperTrend und ChoppinessIndex
    """
    
    params = (
        ('indicators', {
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            },
            'ChoppinessIndex': {
                'class': ChoppinessIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChoppinessIndex'>
            }
        }),
        ('weights', {
            'SuperTrend': 1.0,
            'ChoppinessIndex': 1.0
        })
    )
