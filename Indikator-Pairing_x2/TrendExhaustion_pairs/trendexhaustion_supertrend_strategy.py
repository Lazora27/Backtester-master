import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendExhaustion_SuperTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendExhaustion und SuperTrend
    """
    
    params = (
        ('indicators', {
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            },
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            }
        }),
        ('weights', {
            'TrendExhaustion': 1.0,
            'SuperTrend': 1.0
        })
    )
