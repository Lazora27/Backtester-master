import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketOrderFlow_HyperbolicVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketOrderFlow und HyperbolicVolatility
    """
    
    params = (
        ('indicators', {
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            },
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            }
        }),
        ('weights', {
            'MarketOrderFlow': 1.0,
            'HyperbolicVolatility': 1.0
        })
    )
