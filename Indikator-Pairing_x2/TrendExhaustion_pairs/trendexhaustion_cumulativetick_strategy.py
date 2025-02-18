import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendExhaustion_CumulativeTick_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendExhaustion und CumulativeTick
    """
    
    params = (
        ('indicators', {
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            },
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            }
        }),
        ('weights', {
            'TrendExhaustion': 1.0,
            'CumulativeTick': 1.0
        })
    )
