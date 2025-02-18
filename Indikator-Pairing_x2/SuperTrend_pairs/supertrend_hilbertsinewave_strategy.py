import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperTrend_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperTrend und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'SuperTrend': 1.0,
            'HilbertSinewave': 1.0
        })
    )
