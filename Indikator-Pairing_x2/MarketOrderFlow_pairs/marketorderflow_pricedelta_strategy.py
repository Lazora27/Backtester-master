import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketOrderFlow_PriceDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketOrderFlow und PriceDelta
    """
    
    params = (
        ('indicators', {
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            },
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            }
        }),
        ('weights', {
            'MarketOrderFlow': 1.0,
            'PriceDelta': 1.0
        })
    )
