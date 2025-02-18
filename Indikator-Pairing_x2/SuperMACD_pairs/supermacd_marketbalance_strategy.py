import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und MarketBalance
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'MarketBalance': 1.0
        })
    )
