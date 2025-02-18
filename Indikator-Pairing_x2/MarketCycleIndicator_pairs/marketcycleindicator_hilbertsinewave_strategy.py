import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketCycleIndicator_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketCycleIndicator und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'MarketCycleIndicator': {
                'class': MarketCycleIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketCycleIndicator'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'MarketCycleIndicator': 1.0,
            'HilbertSinewave': 1.0
        })
    )
