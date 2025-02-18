import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketOrderFlow_AdaptiveATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketOrderFlow und AdaptiveATR
    """
    
    params = (
        ('indicators', {
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            },
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            }
        }),
        ('weights', {
            'MarketOrderFlow': 1.0,
            'AdaptiveATR': 1.0
        })
    )
