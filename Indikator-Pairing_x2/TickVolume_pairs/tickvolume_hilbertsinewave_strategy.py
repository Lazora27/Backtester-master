import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'HilbertSinewave': 1.0
        })
    )
