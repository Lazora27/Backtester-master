import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_MarketOrderFlow_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und MarketOrderFlow
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'MarketOrderFlow': 1.0
        })
    )
