import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'HilbertSinewave': 1.0
        })
    )
