import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsVIXFix_MarketOrderFlow_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsVIXFix und MarketOrderFlow
    """
    
    params = (
        ('indicators', {
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            },
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            }
        }),
        ('weights', {
            'WilliamsVIXFix': 1.0,
            'MarketOrderFlow': 1.0
        })
    )
