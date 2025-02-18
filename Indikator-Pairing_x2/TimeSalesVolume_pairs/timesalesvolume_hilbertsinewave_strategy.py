import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSalesVolume_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSalesVolume und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'TimeSalesVolume': 1.0,
            'HilbertSinewave': 1.0
        })
    )
