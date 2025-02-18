import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketOrderFlow_PriceSquawk_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketOrderFlow und PriceSquawk
    """
    
    params = (
        ('indicators', {
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            },
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            }
        }),
        ('weights', {
            'MarketOrderFlow': 1.0,
            'PriceSquawk': 1.0
        })
    )
