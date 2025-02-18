import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_MarketOrderFlow_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und MarketOrderFlow
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'MarketOrderFlow': 1.0
        })
    )
