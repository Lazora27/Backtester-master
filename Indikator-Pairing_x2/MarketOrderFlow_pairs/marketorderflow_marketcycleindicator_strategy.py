import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketOrderFlow_MarketCycleIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketOrderFlow und MarketCycleIndicator
    """
    
    params = (
        ('indicators', {
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            },
            'MarketCycleIndicator': {
                'class': MarketCycleIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketCycleIndicator'>
            }
        }),
        ('weights', {
            'MarketOrderFlow': 1.0,
            'MarketCycleIndicator': 1.0
        })
    )
