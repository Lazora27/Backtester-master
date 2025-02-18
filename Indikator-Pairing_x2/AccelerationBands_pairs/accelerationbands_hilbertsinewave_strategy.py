import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AccelerationBands_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AccelerationBands und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'AccelerationBands': 1.0,
            'HilbertSinewave': 1.0
        })
    )
