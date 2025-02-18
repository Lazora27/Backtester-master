import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendExhaustion_MarketOrderFlow_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendExhaustion und MarketOrderFlow
    """
    
    params = (
        ('indicators', {
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            },
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            }
        }),
        ('weights', {
            'TrendExhaustion': 1.0,
            'MarketOrderFlow': 1.0
        })
    )
