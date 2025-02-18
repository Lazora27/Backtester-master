import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HeikenAshiTrend_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HeikenAshiTrend und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'HeikenAshiTrend': 1.0,
            'HilbertSinewave': 1.0
        })
    )
