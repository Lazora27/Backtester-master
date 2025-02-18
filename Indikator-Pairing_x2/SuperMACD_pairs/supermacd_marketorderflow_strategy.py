import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_MarketOrderFlow_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und MarketOrderFlow
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'MarketOrderFlow': 1.0
        })
    )
