import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketBalance_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketBalance und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'MarketBalance': 1.0,
            'HilbertSinewave': 1.0
        })
    )
