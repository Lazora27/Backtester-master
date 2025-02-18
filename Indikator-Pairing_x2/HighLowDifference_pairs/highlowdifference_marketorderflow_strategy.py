import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_MarketOrderFlow_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und MarketOrderFlow
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'MarketOrderFlow': 1.0
        })
    )
