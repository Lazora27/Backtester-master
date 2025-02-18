import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendExhaustion_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendExhaustion und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'TrendExhaustion': 1.0,
            'HilbertSinewave': 1.0
        })
    )
