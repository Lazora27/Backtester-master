import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_MarketOrderFlow_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und MarketOrderFlow
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'MarketOrderFlow': 1.0
        })
    )
