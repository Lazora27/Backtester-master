import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_MarketOrderFlow_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und MarketOrderFlow
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'MarketOrderFlow': 1.0
        })
    )
