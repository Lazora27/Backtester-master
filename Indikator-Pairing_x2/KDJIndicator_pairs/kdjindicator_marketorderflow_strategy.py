import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KDJIndicator_MarketOrderFlow_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KDJIndicator und MarketOrderFlow
    """
    
    params = (
        ('indicators', {
            'KDJIndicator': {
                'class': KDJIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KDJIndicator'>
            },
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            }
        }),
        ('weights', {
            'KDJIndicator': 1.0,
            'MarketOrderFlow': 1.0
        })
    )
