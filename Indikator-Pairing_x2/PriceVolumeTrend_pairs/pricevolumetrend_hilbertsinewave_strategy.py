import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceVolumeTrend_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceVolumeTrend und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'PriceVolumeTrend': 1.0,
            'HilbertSinewave': 1.0
        })
    )
