import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendExhaustion_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendExhaustion und MarketBalance
    """
    
    params = (
        ('indicators', {
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'TrendExhaustion': 1.0,
            'MarketBalance': 1.0
        })
    )
