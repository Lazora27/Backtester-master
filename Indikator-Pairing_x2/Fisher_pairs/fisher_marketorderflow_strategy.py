import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_MarketOrderFlow_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und MarketOrderFlow
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'MarketOrderFlow': 1.0
        })
    )
