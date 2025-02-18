import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketOrderFlow_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketOrderFlow und OpenInterest
    """
    
    params = (
        ('indicators', {
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'MarketOrderFlow': 1.0,
            'OpenInterest': 1.0
        })
    )
