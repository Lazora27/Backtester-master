import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendExhaustion_PriceDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendExhaustion und PriceDelta
    """
    
    params = (
        ('indicators', {
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            },
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            }
        }),
        ('weights', {
            'TrendExhaustion': 1.0,
            'PriceDelta': 1.0
        })
    )
