import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeRateOfChange_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeRateOfChange und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'VolumeRateOfChange': {
                'class': VolumeRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeRateOfChange'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'VolumeRateOfChange': 1.0,
            'HilbertSinewave': 1.0
        })
    )
