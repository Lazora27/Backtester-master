import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketOrderFlow_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketOrderFlow und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'MarketOrderFlow': 1.0,
            'HilbertSinewave': 1.0
        })
    )
