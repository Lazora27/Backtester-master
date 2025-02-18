import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketOrderFlow_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketOrderFlow und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'MarketOrderFlow': 1.0,
            'HilbertTrendline': 1.0
        })
    )
