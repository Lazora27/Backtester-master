import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperTrend_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperTrend und MarketBalance
    """
    
    params = (
        ('indicators', {
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'SuperTrend': 1.0,
            'MarketBalance': 1.0
        })
    )
